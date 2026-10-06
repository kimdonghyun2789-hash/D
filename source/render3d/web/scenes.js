import { THREE, initMaterials, MAT, buildHand, HAND_DEFAULT_POSE, makeRenderer, makeScene, addLights, shadowCatcher, buildCobot, setJoints, solveIK, buildMachine, buildPart, buildTrayStation, rbox, cyl, softCyl } from './lib.js';
const D = Math.PI / 180;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const num = (p, k, d) => (p.get(k) !== null && p.get(k) !== undefined && p.get(k) !== '' ? +p.get(k) : d);
const vec = (p, k, d) => (p.get(k) ? p.get(k).split(',').map(Number) : d);

function frameXZ(xAxis, zAxis, pos) {
  const x = xAxis.clone().normalize(); const z0 = zAxis.clone().normalize();
  const y = new THREE.Vector3().crossVectors(z0, x).normalize(); const z = new THREE.Vector3().crossVectors(x, y).normalize();
  return new THREE.Matrix4().makeBasis(x, y, z).setPosition(pos);
}
function frameYZ(yAxis, zAxis, pos) {
  const y = yAxis.clone().normalize(); const z0 = zAxis.clone().normalize();
  const x = new THREE.Vector3().crossVectors(y, z0).normalize(); const z = new THREE.Vector3().crossVectors(x, y).normalize();
  return new THREE.Matrix4().makeBasis(x, y, z).setPosition(pos);
}
function placeHand(robot, graspWorld, graspLocal, q0) {
  const target = graspWorld.clone().multiply(new THREE.Matrix4().makeTranslation(-graspLocal.x, -graspLocal.y, -graspLocal.z));
  return solveIK(robot, target, q0, 800);
}
function capture(r, s, cam, name) { r.render(s, cam); (window.__images = window.__images || []).push({ name, data: r.domElement.toDataURL('image/png') }); }
function captureMask(r, s, cam, keep, name) {
  const white = new THREE.MeshBasicMaterial({ color: 0xffffff }); const black = new THREE.MeshBasicMaterial({ color: 0x000000 });
  const saved = new Map(); const keepSet = new Set(); keep.forEach(k => k && k.traverse(o => keepSet.add(o)));
  const hidden = [];
  s.traverse(o => { if (o.isMesh) { if (o.material.isShadowMaterial) { if (o.visible) { o.visible = false; hidden.push(o); } return; } saved.set(o, o.material); o.material = keepSet.has(o) ? white : black; } });
  const env = s.environment; s.environment = null; const tm = r.toneMapping; r.toneMapping = THREE.NoToneMapping;
  capture(r, s, cam, name);
  saved.forEach((m, o) => o.material = m); hidden.forEach(o => o.visible = true); s.environment = env; r.toneMapping = tm;
}
function addPedestal(s, x, z, h = 75) {
  const ped = rbox(30, h, 30, 1.2, MAT.graphite2); ped.position.set(x, h / 2, z); s.add(ped);
  const top = rbox(34, 2.5, 34, 0.8, MAT.graphite); top.position.set(x, h - 1.0, z); s.add(top);
  const foot = rbox(44, 3, 44, 1.0, MAT.graphite); foot.position.set(x, 1.5, z); s.add(foot);
}
const POSES = {
  open: { fingers: [ { spread: -6, mcp: 14, pip: 18, dip: 12 }, { spread: -1, mcp: 10, pip: 14, dip: 10 }, { spread: 4, mcp: 6, pip: 10, dip: 8 } ], thumb: { swing: 28, roll: 40, cmc: 14, mcp: 16, ip: 10 } },
  hook: { fingers: [ { spread: -3, mcp: 52, pip: 72, dip: 40 }, { spread: 0, mcp: 50, pip: 72, dip: 40 }, { spread: 3, mcp: 48, pip: 70, dip: 40 } ], thumb: { swing: 18, roll: 75, cmc: 35, mcp: 35, ip: 25 } },
  wrapTop: { fingers: [ { spread: -6, mcp: 62, pip: 48, dip: 22 }, { spread: 0, mcp: 60, pip: 48, dip: 22 }, { spread: 6, mcp: 58, pip: 46, dip: 22 } ], thumb: { swing: 10, roll: 82, cmc: 48, mcp: 30, ip: 22 } },
  press: { fingers: [ { spread: -2, mcp: 82, pip: 95, dip: 55 }, { spread: 0, mcp: 80, pip: 95, dip: 55 }, { spread: 2, mcp: 4, pip: 6, dip: 4 } ], thumb: { swing: 6, roll: 85, cmc: 45, mcp: 55, ip: 40 } },
};
function getPose(p) { const k = p.get('pose'); if (!k) return null; if (POSES[k]) return JSON.parse(JSON.stringify(POSES[k])); try { return JSON.parse(k); } catch (e) { return null; } }

function setupStage(W, H, p, o = {}) {
  initMaterials();
  const r = makeRenderer(W, H); r.toneMappingExposure = num(p, 'exp', 1.0);
  const s = makeScene(r, num(p, 'env', 0.9));
  addLights(s, { keyPos: vec(p, 'keyPos', o.keyPos || [-120, 260, 220]), key: num(p, 'key', 1.7), shadowSize: o.shadowSize || 220, rim: num(p, 'rim', 0.8), rimPos: o.rimPos || [200, 120, -60], target: o.target || [0, 60, 60] });
  if (o.floor !== false) shadowCatcher(s, 0, 3000, 0.32);
  return { r, s };
}
function buildCell(s, p, o) {
  const m = buildMachine({ doorOpen: o.door ?? 0, theme: p.get('theme') || 'dark', partInVise: o.partInVise, viseFinished: o.viseFinished, leverAngle: o.leverAngle });
  s.add(m); m.updateMatrixWorld(true);
  const bx = num(p, 'bx', 24), bz = num(p, 'bz', 108), ph = 75;
  addPedestal(s, bx, bz, ph);
  const robot = buildCobot(p.get('style') || 'A'); robot.position.set(bx, ph, bz); robot.rotation.y = num(p, 'ry', 0) * D;
  const rs = num(p, 'rscale', 1.2); robot.scale.setScalar(rs); robot.userData.rs = rs; s.add(robot); robot.updateMatrixWorld(true);
  let tray = null;
  if (o.tray) { tray = buildTrayStation(4, 3, o.trayFilled || null); tray.position.set(num(p, 'trayX', 8), 0, num(p, 'trayZ', 168)); s.add(tray); tray.updateMatrixWorld(true); }
  return { m, robot, tray };
}
function finish(r, s, cam, p, keep) {
  if (p.get('mask') === '1') { capture(r, s, cam, 'color'); captureMask(r, s, cam, keep, 'mask'); }
  else r.render(s, cam);
}
function makeCam(W, H, p, defCam, defLook, defFov) {
  const cam = new THREE.PerspectiveCamera(num(p, 'fov', defFov), W / H, 1, 6000);
  cam.position.set(...vec(p, 'cam', defCam)); cam.lookAt(...vec(p, 'look', defLook)); return cam;
}

export const SCENES = {
  async product(W, H, p) {
    initMaterials();
    const r = makeRenderer(W, H); r.toneMappingExposure = num(p, 'exp', 1.0); const s = makeScene(r, num(p, 'env', 1.0));
    addLights(s, { keyPos: [-60, 90, 120], key: 1.5, rim: 0.7, rimPos: [80, 60, -80], shadowSize: 40 });
    const pose = getPose(p) || POSES.open;
    const hand = buildHand(pose, { cutaway: p.get('cut') === '1' });
    hand.rotation.y = num(p, 'yaw', -28) * D; hand.rotation.x = num(p, 'pitch', -4) * D; hand.rotation.z = num(p, 'roll', 0) * D;
    s.add(hand);
    const cam = makeCam(W, H, p, [0, 16, 112], [0, 15.5, 0], 18);
    r.render(s, cam); return { ok: 1 };
  },

  // hand + tool on bare wrist (tech demo)
  async tool(W, H, p) {
    initMaterials();
    const r = makeRenderer(W, H); r.toneMappingExposure = num(p, 'exp', 1.0); const s = makeScene(r, num(p, 'env', 0.95));
    addLights(s, { keyPos: [-80, 140, 120], key: 1.6, rim: 0.8, rimPos: [90, 60, -90], shadowSize: 60, target: [0, 0, 0] });
    if (p.get('floor') === '1') shadowCatcher(s, 0, 600, 0.3);
    const kind = p.get('kind') || 'screwdriver';
    const root = new THREE.Group(); s.add(root);
    if (kind === 'screwdriver') {
      const plate = rbox(36, 2.2, 24, 0.6, MAT.graphite2); plate.position.set(0, 1.1, 0); s.add(plate);
      for (let i = 0; i < 4; i++) for (let k = 0; k < 3; k++) { const sc = cyl(0.55, 0.5, MAT.metal, 20); sc.position.set(-12 + i * 8, 2.45, -7 + k * 7); s.add(sc); }
      const pose = { fingers: [ { spread: -4, mcp: 66, pip: 80, dip: 45 }, { spread: 0, mcp: 64, pip: 80, dip: 45 }, { spread: 4, mcp: 62, pip: 78, dip: 45 } ], thumb: { swing: 12, roll: 80, cmc: 40, mcp: 40, ip: 30 } };
      const hand = buildHand(pose); root.add(hand);
      // screwdriver along hand X, centered in grasp
      const sd = new THREE.Group(); sd.position.set(0, 19.0, 4.2); hand.add(sd);
      const grip = softCyl(1.45, 10, 0.6, new THREE.MeshStandardMaterial({ color: 0x2f3338, roughness: 0.6 })); grip.rotation.z = Math.PI / 2; sd.add(grip);
      const ring = softCyl(1.5, 1.2, 0.3, MAT.yellow); ring.rotation.z = Math.PI / 2; ring.position.x = -5.6; sd.add(ring);
      const shaft = cyl(0.35, 14, MAT.metal, 16); shaft.rotation.z = Math.PI / 2; shaft.position.x = -13; sd.add(shaft);
      const bit = cyl(0.12, 1.2, MAT.metal, 8, 0.35); bit.rotation.z = Math.PI / 2; bit.position.x = -20.6; sd.add(bit);
      // orient: tool axis (-X hand) pointing down onto a screw
      hand.rotation.set(0, 0, -Math.PI / 2); // hand X -> -Y? rotate so that -X_hand = -Y_world
      hand.rotation.z = Math.PI / 2; hand.rotation.y = num(p, 'yaw', -35) * D;
      hand.updateMatrixWorld(true);
      const tipW = sd.localToWorld(V(-21.2, 0, 0)); hand.position.add(V(-4 - tipW.x, 2.7 - tipW.y, 0 - tipW.z));
    } else {
      // tongs picking a food piece over a plate
      const plate = softCyl(11, 1.0, 0.4, MAT.plate); plate.position.set(0, 0.5, 0); s.add(plate);
      const food = []; [[-3, 0.0, 1, MAT.food1], [2.5, 0.0, -2, MAT.food2], [0.5, 0.0, 3.5, MAT.food1]].forEach(([x, _, z, mt]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.6, 24, 16), mt); f.scale.set(1.3, 0.7, 1.0); f.position.set(x, 1.9, z); f.castShadow = true; s.add(f); food.push(f); });
      const pose = { fingers: [ { spread: -8, mcp: 70, pip: 85, dip: 50 }, { spread: -2, mcp: 46, pip: 40, dip: 20 }, { spread: 6, mcp: 40, pip: 35, dip: 18 } ], thumb: { swing: 20, roll: 70, cmc: 30, mcp: 20, ip: 12 } };
      const hand = buildHand(pose); root.add(hand);
      const tg = new THREE.Group(); tg.position.set(1.5, 22.5, 2.6); hand.add(tg);
      const armA = rbox(1.1, 0.35, 22, 0.15, MAT.metal); armA.position.set(0, 0.0, 10); armA.rotation.x = 0.0; tg.add(armA);
      const armB = rbox(1.1, 0.35, 22, 0.15, MAT.metal); armB.position.set(0, 2.2, 10); armB.rotation.x = 0.1; tg.add(armB);
      const loop = new THREE.Mesh(new THREE.TorusGeometry(1.3, 0.22, 12, 24, Math.PI), MAT.metal); loop.rotation.y = Math.PI / 2; loop.position.set(0, 1.1, -1.0); loop.rotation.z = Math.PI / 2; tg.add(loop);
      hand.rotation.set(-Math.PI / 2 + num(p, 'pitch', 0.35), num(p, 'yaw', 0.6), 0);
      hand.updateMatrixWorld(true);
      const tipW = tg.localToWorld(V(0, 1.1, 21)); hand.position.add(V(-0.5 - tipW.x, 2.6 - tipW.y, 0.5 - tipW.z));
    }
    const cam = makeCam(W, H, p, [-60, 55, 85], [0, 12, 0], 26);
    finish(r, s, cam, p, [root]);
    return { ok: 1 };
  },
  // bench-scale kitchen: single arm, pan handle grasp over cooktop
  async kitchen(W, H, p) {
    const { r, s } = setupStage(W, H, p, { shadowSize: 160, target: [0, 90, 0] });
    const counterTop = rbox(150, 4, 70, 0.8, MAT.plate); counterTop.position.set(0, 90, 0); s.add(counterTop);
    const cab = rbox(146, 88, 66, 1.0, new THREE.MeshStandardMaterial({ color: 0x2d3137, roughness: 0.55 })); cab.position.set(0, 44, 0); s.add(cab);
    for (let i = 0; i < 3; i++) { const dr = rbox(46, 80, 1.2, 0.6, new THREE.MeshStandardMaterial({ color: 0x353a41, roughness: 0.5 })); dr.position.set(-48 + i * 48, 46, 33.4); s.add(dr);
      const hd = rbox(16, 1.4, 2.2, 0.6, MAT.metal); hd.position.set(-48 + i * 48, 80, 35); s.add(hd); }
    const cook = rbox(44, 1.0, 36, 0.4, new THREE.MeshPhysicalMaterial({ color: 0x15171a, roughness: 0.12, clearcoat: 1 })); cook.position.set(-30, 92.5, 2); s.add(cook);
    const ringM = new THREE.MeshBasicMaterial({ color: 0x3a3f46 });
    [[-40, -4], [-20, 8]].forEach(([x, z]) => { const rg = new THREE.Mesh(new THREE.TorusGeometry(8, 0.15, 6, 48), ringM); rg.rotation.x = Math.PI / 2; rg.position.set(x, 93.05, z); s.add(rg); });
    // pan
    const pan = new THREE.Group(); s.add(pan);
    const pb = softCyl(10.5, 4.2, 1.2, new THREE.MeshPhysicalMaterial({ color: 0x1f2226, roughness: 0.35, clearcoat: 0.6 })); pb.position.y = 2.1; pan.add(pb);
    const pin = cyl(9.4, 0.5, new THREE.MeshStandardMaterial({ color: 0x2b2f35, roughness: 0.6 }), 48); pin.position.y = 4.0; pan.add(pin);
    [[-3, 2, MAT.food1], [2.5, -1.5, MAT.food2], [0, 3.5, MAT.food2], [4, 2.5, MAT.food1]].forEach(([x, z, mt]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.5, 20, 14), mt); f.scale.set(1.2, 0.6, 1.0); f.position.set(x, 4.6, z); pan.add(f); });
    const ph = cyl(1.3, 20, new THREE.MeshPhysicalMaterial({ color: 0x24272c, roughness: 0.4, clearcoat: 0.4 }), 24); ph.rotation.z = Math.PI / 2; ph.position.set(20, 4.0, 0); pan.add(ph);
    pan.position.set(-38, 98 + num(p, 'lift', 6), -2); pan.rotation.z = num(p, 'tilt', 0.08);
    pan.updateMatrixWorld(true);
    // plate with food
    const plate = softCyl(11, 1.2, 0.5, MAT.plate); plate.position.set(18, 92.6, 14); s.add(plate);
    [[15, 13, MAT.food1], [20, 16, MAT.food2], [19, 11, MAT.food1]].forEach(([x, z, mt]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.6, 20, 14), mt); f.scale.set(1.2, 0.6, 1.0); f.position.set(x, 94.2, z); f.castShadow = true; s.add(f); });
    const tongs = rbox(1.0, 0.4, 24, 0.15, MAT.metal); tongs.position.set(30, 93, -12); tongs.rotation.y = 0.5; s.add(tongs);
    // robot on counter back-right
    const robot = buildCobot('A'); robot.position.set(num(p, 'bx', 45), 92, num(p, 'bz', -22)); robot.scale.setScalar(1.0); s.add(robot); robot.updateMatrixWorld(true);
    const handleW = pan.localToWorld(V(24, 4.0, 0));
    const hand = buildHand(POSES.hook); robot.userData.flange.add(hand);
    // grasp handle: bar axis along X_world (handle direction), palm facing -Y? -> palm faces handle from above-front
    const gw = frameXZ(V(1, 0, 0), V(0, -1, num(p, 'tz', 0.25)), handleW);
    const res = placeHand(robot, gw, V(0, 19.2, 4.6), vec(p, 'q0', [120, -40, -80, -60, 90, 0]).map(v => v * D));
    const cam = makeCam(W, H, p, [-70, 160, 150], [0, 108, -6], 30);
    finish(r, s, cam, p, [robot, pan]);
    return { posErr: +res.posErr.toFixed(3), q: res.q.map(v => +(v / D).toFixed(1)) };
  },
  // closing: hand on cobot wrist, upright, palm toward camera
  async closing(W, H, p) {
    const { r, s } = setupStage(W, H, p, { floor: false, keyPos: [-90, 200, 220] });
    const robot = buildCobot('A'); robot.position.set(0, 0, 0); s.add(robot); robot.updateMatrixWorld(true);
    const hand = buildHand(POSES.open); robot.userData.flange.add(hand);
    const yaw = num(p, 'yaw', -25) * D;
    const target = frameYZ(V(num(p, 'tx', -0.15), 1, 0), V(Math.sin(yaw), 0, Math.cos(yaw)), V(num(p, 'px', -10), num(p, 'py', 95), num(p, 'pz', 30)));
    const res = solveIK(robot, target, vec(p, 'q0', [20, -20, -70, -40, 90, 0]).map(v => v * D), 800);
    const cam = makeCam(W, H, p, [-30, 120, 190], [-6, 102, 30], 18);
    r.render(s, cam);
    return { posErr: +res.posErr.toFixed(3), q: res.q.map(v => +(v / D).toFixed(1)) };
  },
  // generic machine-tending cell; task = door | pick | load | press | unload | close | idle
  async cell(W, H, p) {
    const task = p.get('task') || 'door';
    const { r, s } = setupStage(W, H, p);
    const o = { door: num(p, 'door', task === 'load' || task === 'unload' ? 0.85 : 0.12), tray: p.get('tray') === '1' || task === 'pick',
      partInVise: task === 'unload' || task === 'press' || p.get('vpart') === '1', viseFinished: task === 'unload' };
    const { m, robot, tray } = buildCell(s, p, o);
    let pose = getPose(p); let gw, gl, held = null, q0 = vec(p, 'q0', [150, -30, -80, -60, 90, 0]).map(v => v * D);
    let focus = V(0, 100, 60);
    if (task === 'door' || task === 'close') {
      pose = pose || POSES.hook;
      const door = m.userData.door; const hW = door.localToWorld(door.userData.handle.clone().add(V(0, num(p, 'hy', 6), 0)));
      gw = frameXZ(V(0, 1, 0), V(-1, 0, num(p, 'tz', 0.15)), hW); gl = V(0, num(p, 'gy', 19.2), num(p, 'gz', 4.6)); focus = hW;
    } else if (task === 'pick' || task === 'load' || task === 'unload' || task === 'carry') {
      pose = pose || POSES.wrapTop;
      let top;
      if (task === 'pick') {
        const idx = num(p, 'part', 9); const part = tray.userData.parts[idx];
        top = part.localToWorld(V(0, 7.0 + num(p, 'lift', 0), 0)); held = part;
      } else {
        const vise = m.userData.vise; top = vise.localToWorld(V(-0.75, 12.0 + num(p, 'lift', task === 'unload' ? 9 : 2.5), 0));
        if (task === 'load') { held = buildPart('blank'); s.add(held); held.position.copy(top).add(V(0, -7.0, 0)); }
        if (task === 'unload') { const vp = m.userData.visePart; vp.parent.remove(vp); held = buildPart('finished'); s.add(held); held.position.copy(top).add(V(0, -7.0, 0)); }
      }
      // palm down, fingers toward -X, thumb toward +Z
      const yaw = num(p, 'gyaw', 0) * D;
      gw = frameXZ(V(Math.sin(yaw), 0, Math.cos(yaw)), V(0, -1, 0), top); gl = V(0, num(p, 'gy', 18.6), num(p, 'gz', 2.7)); focus = top;
    } else if (task === 'press') {
      pose = pose || POSES.press;
      const btn = m.userData.startBtn; btn.updateMatrixWorld(true);
      const front = btn.localToWorld(V(0, 0.75, 0)); // cylinder axis along local Y (rotated to Z)
      const n = btn.localToWorld(V(0, 1, 0)).sub(btn.localToWorld(V(0, 0, 0))).normalize();
      // finger direction into the button, palm facing down
      gw = frameYZ(n.clone().negate(), V(0, -1, 0), front); focus = front;
      // compute tip local position from the posed hand
      const tmp = buildHand(pose); tmp.updateMatrixWorld(true); const tipW = tmp.userData.fingers[2].tip.getWorldPosition(new THREE.Vector3());
      gl = tipW.add(V(0, 0.2, 0));
    }
    const hand = buildHand(pose); hand.scale.setScalar(1 / (robot.userData.rs || 1)); robot.userData.flange.add(hand);
    const res = placeHand(robot, gw, gl, q0);
    const off = vec(p, 'off', [-60, 38, 105]);
    const lookOff = vec(p, 'lookOff', [0, 0, 0]);
    const cam = makeCam(W, H, p, [focus.x + off[0], focus.y + off[1], focus.z + off[2]], [focus.x + lookOff[0], focus.y + lookOff[1], focus.z + lookOff[2]], 24);
    const keep = [robot]; if (held) keep.push(held);
    if (task === 'door' || task === 'close') { const door = m.userData.door; door.children.forEach(c => { if (c.isMesh && c.geometry.type === 'CylinderGeometry') keep.push(c); }); }
    if (task === 'press') keep.push(m.userData.panel);
    if (task === 'load' || task === 'unload') keep.push(m.userData.vise);
    if (task === 'pick' && tray) keep.push(...tray.userData.parts);
    finish(r, s, cam, p, keep);
    return { posErr: +res.posErr.toFixed(4), rotErr: +res.rotErr.toFixed(4), q: res.q.map(v => +(v / D).toFixed(1)), focus: focus.toArray().map(v => +v.toFixed(1)) };
  },
};
