// MH deck figures, group "flow" (opt-in scenes only; every existing scene renders unchanged). Units: cm.
// World: back wall face z = 0, x right, y up, z toward the viewer (same frame as arki.js).
//   flowPlain   : ordinary kitchen, no MH element. Appliances (fridge · induction · oven · dishwasher) + the
//                 between-appliance human tasks as numbered dark dashed paths 1-4 (m02). q: cam, lx, ly, lz, fov
//   flowInstall : the same kitchen run at three integration levels, one camera (m10).
//                 q: level=retrofit|remodel|newbuild, cam, lx, ly, lz, fov
import { THREE, makeRenderer, makeScene, MAT, cyl } from './lib.js';
import { robotCapsules, collectObstacles, penetration, selfPenetration } from './collide.js';
import { amat, plate, bowl, cup, human, makeRobot, reach, arkiRunV2,
  bx, obst, baseRun, counter, sink, induction, upperRun, backsplash, underDW,
  table, zone, pathCurve, room, lights, camPersp, project, placeRobot, attachHeld, RB_Q0 } from './arki.js';

const V = (x, y, z) => new THREE.Vector3(x, y, z);
const D = Math.PI / 180;
const INK = 0x15171a, INK2 = 0x4a4f57;

// ---------------------------------------------------------------- parts
// dark dashed path for HUMAN work (never orange): tube dashes + cone head ending exactly at the last point
function inkPath(g, pts, opts = {}) {
  const mat = new THREE.MeshBasicMaterial({ color: opts.color ?? INK });
  const curve = new THREE.CatmullRomCurve3(pts.map(q => q.clone())); const L = curve.getLength();
  const r = opts.r ?? 1.45, dash = opts.dash ?? 8, gap = opts.gap ?? 5.5, hl = r * 8;
  let s = 0;
  while (s < L - hl) {
    const s1 = Math.min(L - hl, s + dash); const sub = [];
    for (let k = 0; k <= 6; k++) sub.push(curve.getPointAt((s + (s1 - s) * k / 6) / L));
    g.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(sub), 6, r, 8, false), mat)); s = s1 + gap;
  }
  const end = curve.getPointAt(1), tan = curve.getTangentAt(1);
  const head = new THREE.Mesh(new THREE.ConeGeometry(r * 3.0, hl, 18), mat);
  head.position.copy(end.clone().sub(tan.clone().multiplyScalar(hl / 2))); head.quaternion.setFromUnitVectors(V(0, 1, 0), tan); g.add(head);
  const along = {}; for (let t = 15; t <= 85; t += 10) along[t] = curve.getPointAt(t / 100);
  return { start: curve.getPointAt(0), mid: curve.getPointAt(opts.at ?? 0.5), end, along };
}
function fridge(g, x0, w = 76, opts = {}) {
  const a = amat(); const d = opts.d ?? 66, h = opts.h ?? 192;
  const m = new THREE.MeshPhysicalMaterial({ color: 0xdadde1, roughness: 0.3, metalness: 0.3, clearcoat: 0.45 });
  return obst('fridge', () => {
    g.add(bx(x0, 0, 0, x0 + w, 5, d - 4, a.dark));
    g.add(bx(x0 + 0.4, 5, 0, x0 + w - 0.4, h, d - 2.2, m));
    const ys = h * 0.38;
    g.add(bx(x0 + 0.8, ys + 0.4, d - 2.2, x0 + w / 2 - 0.3, h - 0.8, d, m)); g.add(bx(x0 + w / 2 + 0.3, ys + 0.4, d - 2.2, x0 + w - 0.8, h - 0.8, d, m));
    g.add(bx(x0 + 0.8, 5.6, d - 2.2, x0 + w - 0.8, ys - 0.4, d, m));
    g.add(bx(x0 + w / 2 - 3.4, h * 0.5, d, x0 + w / 2 - 2.0, h * 0.82, d + 2.6, a.steelDark));
    g.add(bx(x0 + w / 2 + 2.0, h * 0.5, d, x0 + w / 2 + 3.4, h * 0.82, d + 2.6, a.steelDark));
    g.add(bx(x0 + w * 0.3, ys - 7, d, x0 + w * 0.7, ys - 5.6, d + 2.6, a.steelDark));
    return { x0, x1: x0 + w, d, h, center: V(x0 + w / 2, h * 0.66, d) };
  });
}
// built-in oven unit (base cabinet with a glass oven door), local frame like baseRun
function oven(g, x0, w = 60) {
  const a = amat(); const d = 58;
  const glass = new THREE.MeshPhysicalMaterial({ color: 0x1b1e22, roughness: 0.14, clearcoat: 1.0, clearcoatRoughness: 0.06 });
  return obst('oven', () => {
    g.add(bx(x0, 0, 0, x0 + w, 10, d - 5, a.dark));
    g.add(bx(x0, 10, 0, x0 + w, 85, d - 2, a.cabLower));
    g.add(bx(x0 + 1, 24, d - 2, x0 + w - 1, 80, d - 0.4, glass));
    g.add(bx(x0 + 1, 76.2, d - 0.4, x0 + w - 1, 80, d - 0.2, new THREE.MeshStandardMaterial({ color: 0x3a3e45, roughness: 0.5 })));
    g.add(bx(x0 + 8, 70.5, d - 0.4, x0 + w - 8, 72, d + 2.6, a.steel));
    g.add(bx(x0 + 1, 11, d - 2, x0 + w - 1, 23, d - 1.2, a.cabLower));
    return { center: V(x0 + w / 2, 52, d) };
  });
}
// wall cabinet with its door swung open (dish storage = destination of the put-away task)
function upperOpen(g, x0, w = 60, opts = {}) {
  const a = amat(); const y0 = 145, y1 = 225, d = 35, t = 1.6;
  obst('upper', () => {
    g.add(bx(x0, y0, 0, x0 + t, y1, d - 1.5, a.cabUpper)); g.add(bx(x0 + w - t, y0, 0, x0 + w, y1, d - 1.5, a.cabUpper));
    g.add(bx(x0, y0, 0, x0 + w, y0 + t, d - 1.5, a.cabUpper)); g.add(bx(x0, y1 - t, 0, x0 + w, y1, d - 1.5, a.cabUpper));
    g.add(bx(x0, y0, 0, x0 + w, y1, 1.2, a.cabInside));
    g.add(bx(x0 + t, y0 + 38, 1.2, x0 + w - t, y0 + 39.4, d - 3, a.cabUpper));
  });
  for (let i = 0; i < 5; i++) { const p = plate(11.5); p.position.set(x0 + 17, y0 + t + i * 1.4, 17); g.add(p); }
  for (let i = 0; i < 2; i++) { const b = bowl(6.5, 5.8); b.position.set(x0 + 44, y0 + t + i * 2.8, 16); g.add(b); }
  for (let i = 0; i < 3; i++) { const c = cup(); c.position.set(x0 + 13 + i * 14, y0 + 39.4, 15); g.add(c); }
  const door = new THREE.Group(); door.position.set(x0 + 0.3, y0, d - 0.4); door.rotation.y = -(opts.open ?? 100) * D; g.add(door);
  door.add(bx(0, 0.3, -1.1, w - 0.6, y1 - y0 - 0.3, 0, a.cabUpper));
  return { x0, x1: x0 + w, mouth: V(x0 + w / 2, y0 + 14, d - 4), center: V(x0 + w / 2, y0 + 22, 18) };
}
// AprilTag-like fiducial (Vision reference point) on a surface facing +z
function fiducial(g, x, y, z, s = 7) {
  const k = new THREE.MeshBasicMaterial({ color: INK }), w = new THREE.MeshBasicMaterial({ color: 0xffffff });
  g.add(bx(x - s / 2, y - s / 2, z, x + s / 2, y + s / 2, z + 0.25, k));
  g.add(bx(x - s * 0.32, y - s * 0.32, z + 0.25, x + s * 0.32, y + s * 0.32, z + 0.35, w));
  g.add(bx(x - s * 0.32, y - s * 0.32, z + 0.35, x - s * 0.02, y + s * 0.02, z + 0.45, k));
  g.add(bx(x + s * 0.06, y + s * 0.08, z + 0.35, x + s * 0.22, y + s * 0.24, z + 0.45, k));
  return V(x, y, z);
}
function dishesAt(g, x, z, y = 88.2) {
  const a = amat(); const out = [];
  const p1 = plate(12.5); p1.position.set(x, y, z); g.add(p1); out.push(p1);
  const p2 = plate(12.5, a.ceramicB); p2.position.set(x, y + 2.4, z); g.add(p2); out.push(p2);
  return out;
}
function tools(g, x0, y0, z0) {      // ladle · tongs · spatula hanging on a dock panel (local)
  const st = amat().steel;
  const lad = cyl(0.55, 24, st, 10); lad.position.set(x0, y0, z0); g.add(lad);
  const ladB = bowl(3.2, 2.6, st); ladB.position.set(x0, y0 - 14, z0 + 1); g.add(ladB);
  for (const dx of [-0.9, 0.9]) { const t = cyl(0.5, 26, st, 8); t.position.set(x0 + 9 + dx, y0 - 1, z0); t.rotation.z = dx * 0.05; g.add(t); }
  const sp = cyl(0.55, 18, st, 10); sp.position.set(x0 + 18, y0 + 3, z0); g.add(sp);
  g.add(bx(x0 + 15.5, y0 - 13, z0 - 0.4, x0 + 20.5, y0 - 5, z0 + 0.4, st));
}

// ---------------------------------------------------------------- scenes
export const FLOW_SCENES = {
  // m02: ordinary kitchen (no MH element). Return on the left wall: oven under the induction + hood. Back wall:
  // sink | wall cabinet (opened) | dishwasher | fridge. Dining table in front. Human tasks = dark dashed paths 1-4.
  async flowPlain(W, H, p) {
    const renderer = makeRenderer(W, H); const scene = makeScene(renderer, 0.42); const a = amat();
    const g = new THREE.Group(); scene.add(g);
    const XW = -60, RL = 172, RZ0 = 62;
    // return run on the left wall (local x along the wall toward -z, local z into the room)
    const sg = new THREE.Group(); sg.rotation.y = Math.PI / 2; sg.position.set(XW, 0, RZ0 + RL); g.add(sg);
    const oc = RL / 2;
    baseRun(sg, 0, oc - 30, { doorW: 56 }); const ov = oven(sg, oc - 30, 60); baseRun(sg, oc + 30, RL, { doorW: 56 });
    counter(sg, 0, RL, {}); const ih = induction(sg, oc, { w: 58 }); backsplash(sg, 0, RL);
    sg.add(bx(oc - 32, 158, 0, oc + 32, 170, 46, a.cabTall)); sg.add(bx(oc - 14, 170, 0, oc + 14, 240, 26, a.cabTall));
    // back wall run: corner base | counter | sink | wall cabinet opened above | dishwasher | fridge
    const XS = 140, XD = 246, XF = 308;
    baseRun(g, XW, XD, { doorW: 61 });
    const sk = sink(g, XS, { w: 76 });
    counter(g, XW, XD + 60, { holes: [[sk.x0, sk.x1, 10, 52]] });
    const dw = underDW(g, XD, { open: 1, rackL: 1, rackU: 0.0 });
    backsplash(g, XW, XD + 60);
    upperRun(g, XW, 176, { doorW: 59 }); const up = upperOpen(g, 176, 60, { open: 98 }); upperRun(g, 236, XD + 60, { doorW: 35 });
    const fr = fridge(g, XF, 76);
    obst('upper', () => g.add(bx(XF, 200, 0, XF + 76, 225, 60, a.cabUpper)));
    room(g, XW, XF + 76, 330, 240, { left: false });
    obst('wall', () => g.add(bx(XW - 20, 0, -22, XW, 240, 250, a.wall)));
    // clean plates standing in the lower rack
    const lr = dw.racks[0];
    for (let i = 0; i < 4; i++) { const pl = plate(11); pl.rotation.set(0, 0, Math.PI / 2); pl.position.set(-12 + i * 4, 11, 4); lr.add(pl); }
    // dining table with the used dishes
    const T0 = [96, 196, 236, 282];
    table(g, T0[0], T0[1], T0[2], T0[3], { chairs: false });
    for (const [x, z, s] of [[124, 226, 0], [158, 252, 1], [206, 230, 0]]) { const pl = plate(12.5, s ? a.ceramicB : a.ceramic); pl.position.set(x, 73, z); g.add(pl); }
    const b1 = bowl(6.5, 6, a.ceramicG); b1.position.set(184, 73, 216); g.add(b1);
    const c1 = cup(); c1.position.set(214, 73, 262); g.add(c1);
    // neutral human figure next to the table, facing the sink
    const hx = +(p.get('hx') || 84), hz = +(p.get('hz') || 128);
    g.add(human(hx, hz, +(p.get('hr') || 3.0)));
    // human workflow (dark, numbered on the slide): 1 table -> sink, 2 sink -> dishwasher, 3 dishwasher -> counter, 4 counter -> wall cabinet
    const dwx = (dw.x0 + dw.x1) / 2;
    const P1 = inkPath(g, [V(174, 82, 234), V(180, 130, 150), V(162, 140, 84), V(XS + 2, 130, 44), V(XS + 2, 100, 38)], { at: 0.4 });
    const P2 = inkPath(g, [V(XS + 26, 100, 36), V(196, 116, 64), V(232, 92, 84), V(dwx - 10, 46, 80)], { at: 0.4 });
    const P3 = inkPath(g, [V(dwx + 10, 46, 88), V(dwx + 14, 104, 84), V(256, 110, 52), V(236, 100, 44), V(224, 97, 42)], { at: 0.5 });
    const P4 = inkPath(g, [V(214, 100, 40), V(196, 126, 50), V(196, 152, 46), V(up.mouth.x - 4, up.mouth.y + 2, up.mouth.z - 6)], { at: 0.5 });
    const look = V(+(p.get('lx') || 150), +(p.get('ly') || 88), +(p.get('lz') || 120));
    const cam = camPersp(W, H, +(p.get('fov') || 32), V(...(p.get('cam') || '520,330,640').split(',').map(Number)), look);
    lights(scene, { keyPos: [300, 520, 600], target: [160, 60, 120], shadowSize: 460 });
    renderer.render(scene, cam);
    g.updateMatrixWorld(true);
    const wv = (o, v) => o.localToWorld(v.clone());
    const along = {}; for (const [n, P] of [[1, P1], [2, P2], [3, P3], [4, P4]]) for (const [t, v] of Object.entries(P.along)) along[`p${n}_${t}`] = v;
    const anchors = project(cam, W, H, { ...along,
      fridge: fr.center, fridgeTop: V(XF + 38, 192, 33), ih: wv(sg, ih.center), oven: wv(sg, ov.center), dw: V(dwx, 50, 60), dwDoor: V(dwx, 12, 100),
      sink: V(XS, 92, 30), table: V(160, 73, 240), cabinet: up.center, human: V(hx, 172, hz),
      p1: P1.mid, p2: P2.mid, p3: P3.mid, p4: P4.mid, p1s: P1.start, p1e: P1.end, p2s: P2.start, p2e: P2.end, p3s: P3.start, p3e: P3.end, p4s: P4.start, p4e: P4.end });
    return { anchors };
  },

  // m10: one product, three integration levels, same camera and scale.
  //  retrofit : existing run kept as is; compact counter dock + robot (no rail), vision fiducials, drop zone
  //  remodel  : v2 run (rail · Robot Home · dishwasher interface · dish drawer) = run2 geometry
  //  newbuild : v2 run + elements built in at design stage (in-wall power · data line, tool dock, service bay)
  async flowInstall(W, H, p) {
    const renderer = makeRenderer(W, H); const scene = makeScene(renderer, 0.42); const a = amat();
    const g = new THREE.Group(); scene.add(g);
    const lv = p.get('level') || 'remodel';
    let ik = null, A = {};
    if (lv === 'retrofit') {
      // same footprint as the v2 run (x 0..325): base cabinets | sink 76 @165 | base | dishwasher 265..325
      const XD = 265, XE = 325, XS = 165;
      baseRun(g, 0, XD, { doorW: 60 });
      const dw = underDW(g, XD, { open: 1, rackL: 1, rackU: 0 });
      const sk = sink(g, XS, { w: 76 });
      counter(g, 0, XE, { holes: [[sk.x0, sk.x1, 10, 52]] });
      backsplash(g, 0, XE); upperRun(g, 0, XE, { doorW: 65 });
      room(g, 0, XE, 330, 240, { left: false });
      const lr = dw.racks[0];
      for (let i = 0; i < 4; i++) { const pl = plate(11); pl.rotation.set(0, 0, Math.PI / 2); pl.position.set(-12 + i * 4, 11, 4); lr.add(pl); }
      // compact counter dock (mount + charging / controller) above the dishwasher: no rail, no cabinet work
      const MXc = 300, MZc = 45, MY = 97;
      const dock = new THREE.Group(); g.add(dock);
      dock.add(bx(MXc - 18, 88.2, MZc - 16, MXc + 18, MY, MZc + 16, MAT.graphite, 2.2));
      dock.add(bx(MXc - 12, MY - 3.2, MZc + 16, MXc + 12, MY - 2.2, MZc + 16.3, new THREE.MeshBasicMaterial({ color: 0xdfe3e8 })));
      // drop zone between sink and dock (robot zone = orange)
      const DZ = [192, 18, 252, 60];
      zone(g, 'robot', DZ[0], DZ[1], DZ[2], DZ[3], 88.9);
      const dishes = dishesAt(g, 212, 38);
      const b1 = bowl(6.5, 6, a.ceramicG); b1.position.set(240, 88.2, 52); g.add(b1); dishes.push(b1);
      // vision reference points on the backsplash
      const f1 = fiducial(g, 104, 118, 0.1, 9), f2 = fiducial(g, 226, 118, 0.1, 9), f3 = fiducial(g, 300, 124, 0.1, 9);
      // robot upright on the dock, picking the top plate in the drop zone (collision-aware IK; the dock is excluded only for the base links)
      g.updateMatrixWorld(true);
      const obstacles = collectObstacles(g); obstacles.push(new THREE.Box3().setFromObject(b1));   // furniture + the bowl (the plates are the grasp target)
      const dockBox = new THREE.Box3(V(MXc - 18, 88.2, MZc - 16), V(MXc + 18, MY, MZc + 16));
      const robot = makeRobot(1.0); robot.position.set(MXc, MY, MZc); g.add(robot);
      const tcp = V(212 + 12.5, 97.9, 38);
      const r = reach(robot, tcp, V(0, -1, 0), V(0, 0, 1), RB_Q0, { obstacles });
      const caps = robotCapsules(robot);
      const pen = penetration(caps, obstacles).total + penetration(caps.filter(c => c.link !== -1 && c.link !== 0), [dockBox]).total + selfPenetration(caps).total;
      ik = { posErr: +r.posErr.toFixed(2), rotErr: +r.rotErr.toFixed(3), pen: +pen.toFixed(2), hits: penetration(caps, obstacles).hits, dock: +penetration(caps.filter(c => c.link !== -1 && c.link !== 0), [dockBox]).total.toFixed(2), self: +selfPenetration(caps).total.toFixed(2) };
      // reach check (not drawn): loading the dishwasher lower rack from the same dock
      { const t2 = makeRobot(1.0); t2.position.set(MXc, MY, MZc); g.add(t2); attachHeld(t2, 'plateV'); g.updateMatrixWorld(true);
        const rl = dw.racks[0].position; const r2 = reach(t2, V((dw.x0 + dw.x1) / 2 + 2, rl.y + 23, rl.z + 4), V(0, -1, 0), V(1, 0, 0), RB_Q0, { obstacles });
        const c2 = robotCapsules(t2); const pen2 = penetration(c2, obstacles).total + penetration(c2.filter(c => c.link !== -1 && c.link !== 0), [dockBox]).total;
        ik.load = { posErr: +r2.posErr.toFixed(2), rotErr: +r2.rotErr.toFixed(3), pen: +pen2.toFixed(2) }; g.remove(t2); }
      // robot path: drop zone -> dishwasher lower rack (orange)
      const dwx = (dw.x0 + dw.x1) / 2;
      pathCurve(g, [V(218, 104, 44), V(250, 118, 68), V(278, 86, 88), V(dwx, 44, 80)]);
      A = { mount: V(MXc, 92, MZc + 16), robot: V(MXc - 10, 150, MZc), dock: V(MXc + 14, 93, MZc + 16), fid: f2, fid1: f1, fid3: f3, drop: V(200, 89, 54),
        dropC: V((DZ[0] + DZ[2]) / 2, 89, (DZ[1] + DZ[3]) / 2), dw: V(dwx, 40, 70), sink: V(XS, 90, 30), rail: V(160, 140, 30), path: V(279, 84, 86) };
    } else {
      // remodel / newbuild: the verified v2 run (same parameters as run2 task=hero, railz=30)
      const k = arkiRunV2(g, 0, { railZ: 30, dwOpen: 1, rackL: 1, rackU: 0, drawerOut: 0, garageOpen: 0, dirty: true });
      room(g, 0, k.xe, 330, 240, { left: false });
      zone(g, 'robot', k.xz + 2, 14, k.xz + k.drop - 2, 60, 88.9);
      const R = placeRobot(g, k, 'hero', 1.0); ik = R.ik;
      const dwx = (k.dw.x0 + k.dw.x1) / 2;
      pathCurve(g, [V(k.xz + 36, 100, 40), V(k.xs - 20, 126, 60), V(k.xs + 30, 130, 68), V(k.xw - 20, 116, 78), V(dwx, 66, 80)]);
      A = { garage: V((k.gar.x0 + k.gar.x1) / 2, 175, 62), rail: V((k.xz + k.xs) / 2, 142, k.rl.z + 4), railR: V(k.xw - 10, 142, k.rl.z + 4), dw: V(dwx, 40, 70),
        drawer: V((k.dr.x0 + k.dr.x1) / 2, 62, 56), drop: V(k.xz + 14, 89, 54), dropC: V(k.xz + k.drop / 2, 89, 37), sink: k.sk.center, robot: V(k.xs + 20, 128, 40) };
      if (lv === 'newbuild') {
        const ink = new THREE.MeshBasicMaterial({ color: INK2 });
        // in-wall power · data line (hidden-line convention: dashed): floor -> left of the Robot Home -> under the wall cabinets -> dishwasher end
        const seg = (x0, y0, x1, y1, z = 0.6, dash = 6, gap = 4) => { const L = Math.hypot(x1 - x0, y1 - y0); let s = 0;
          while (s < L) { const s1 = Math.min(L, s + dash); const u0 = s / L, u1 = s1 / L;
            const m = new THREE.Mesh(new THREE.CylinderGeometry(0.75, 0.75, (u1 - u0) * L, 8), ink);
            m.position.set(x0 + (x1 - x0) * (u0 + u1) / 2, y0 + (y1 - y0) * (u0 + u1) / 2, z); m.rotation.z = Math.atan2(-(x1 - x0), y1 - y0); g.add(m); s = s1 + gap; } };
        const XR = k.xe + 14;                    // service riser on the wall beside the run end -> rail end + dishwasher
        seg(XR, 2, XR, 141.5); seg(XR, 141.5, k.xe - 2, 141.5); seg(XR, 96, k.xe, 96);
        const jb = (x, y) => { g.add(bx(x - 4.5, y - 4.5, 0, x + 4.5, y + 4.5, 2.4, MAT.graphite2)); };
        jb(XR, 141.5); jb(XR, 96);
        // tool dock on the backsplash next to the Robot Home (inside the robot zone)
        obst('tooldock', () => g.add(bx(k.xz + 4, 96, 0, k.xz + 30, 134, 2.4, MAT.graphite)));
        tools(g, k.xz + 8, 120, 3.4);
        // service bay below the Robot Home: vented access panel replaces the cabinet door
        const grille = new THREE.MeshStandardMaterial({ color: 0x3a3e45, roughness: 0.6 });
        g.add(bx(k.xg + 1, 11, 55.5, k.xz - 1, 84, 57.4, new THREE.MeshStandardMaterial({ color: 0xd5d8dc, roughness: 0.55 })));
        for (let i = 0; i < 9; i++) g.add(bx(k.xg + 7, 20 + i * 3.2, 57.4, k.xz - 7, 21.2 + i * 3.2, 57.9, grille));
        A = { ...A, line: V(k.xe + 14, 60, 0.6), lineTop: V(k.xe + 14, 141.5, 2.4), lineR: V(k.xe + 14, 96, 2.4), tooldock: V(k.xz + 17, 112, 3), service: V((k.xg + k.xz) / 2, 50, 58) };
      }
    }
    const look = V(+(p.get('lx') || 165), +(p.get('ly') || 96), +(p.get('lz') || 36));
    const cam = camPersp(W, H, +(p.get('fov') || 30), V(...(p.get('cam') || '430,236,520').split(',').map(Number)), look);
    lights(scene, { keyPos: [300, 520, 600], target: [180, 60, 60] });
    renderer.render(scene, cam);
    return { ik, level: lv, anchors: project(cam, W, H, A) };
  },
};
