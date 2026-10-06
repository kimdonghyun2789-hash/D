// Premium built-in kitchen (style reference: dark cabinetry, backlit white niche, marble counter,
// chrome tools on a rail). Robot arm mounted under the upper cabinet, SoftHand-4 using ordinary human utensils.
import { THREE, initMaterials, MAT, buildHand, makeRenderer, makeScene, buildCobot, solveIK, rbox, cyl, softCyl } from './lib.js';
import { KPOSES, buildPan, buildPot, buildTongs, buildLadle, buildTurner, buildKnob, buildBarHandle, buildPlate, buildBowl } from './kitchen.js';

const D = Math.PI / 180;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const num = (p, k, d) => (p.get(k) !== null && p.get(k) !== undefined && p.get(k) !== '' ? +p.get(k) : d);
const vec = (p, k, d) => (p.get(k) ? p.get(k).split(',').map(Number) : d);

let LM = null;
function lmat() {
  if (LM) return LM;
  LM = {
    cab: new THREE.MeshPhysicalMaterial({ color: 0x16171a, roughness: 0.5, clearcoat: 0.18, clearcoatRoughness: 0.5 }),
    cab2: new THREE.MeshPhysicalMaterial({ color: 0x1c1d21, roughness: 0.42, clearcoat: 0.25 }),
    groove: new THREE.MeshStandardMaterial({ color: 0x0b0c0e, roughness: 0.6 }),
    back: new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0xffffff, emissiveIntensity: 0.92, roughness: 0.9 }),
    side: new THREE.MeshStandardMaterial({ color: 0xf1f1f0, emissive: 0xffffff, emissiveIntensity: 0.42, roughness: 0.85 }),
    led: new THREE.MeshBasicMaterial({ color: 0xffffff }),
    chrome: new THREE.MeshStandardMaterial({ color: 0xe9ebee, metalness: 1.0, roughness: 0.1 }),
    steel: new THREE.MeshStandardMaterial({ color: 0xcdd1d6, metalness: 0.95, roughness: 0.22 }),
    sinkIn: new THREE.MeshStandardMaterial({ color: 0x9da2a8, metalness: 0.9, roughness: 0.3 }),
    hob: new THREE.MeshPhysicalMaterial({ color: 0x0e0f11, roughness: 0.08, clearcoat: 1.0, clearcoatRoughness: 0.05 }),
    glass: new THREE.MeshPhysicalMaterial({ color: 0xffffff, roughness: 0.04, transparent: true, opacity: 0.22, clearcoat: 1.0, depthWrite: false }),
    amber: new THREE.MeshPhysicalMaterial({ color: 0x8a5a1c, roughness: 0.1, transparent: true, opacity: 0.7, clearcoat: 1.0 }),
    floor: new THREE.MeshStandardMaterial({ color: 0x1b1c1f, roughness: 0.32 }),
    ovenGlass: new THREE.MeshPhysicalMaterial({ color: 0x0c0d0f, roughness: 0.06, clearcoat: 1.0 }),
    noodle: new THREE.MeshStandardMaterial({ color: 0xf0cf8a, roughness: 0.6 }),
    herb: new THREE.MeshStandardMaterial({ color: 0x3f7f2c, roughness: 0.65 }),
    tomato: new THREE.MeshPhysicalMaterial({ color: 0xd8432a, roughness: 0.3, clearcoat: 0.7 }),
    pepper: new THREE.MeshPhysicalMaterial({ color: 0xf0b229, roughness: 0.35, clearcoat: 0.5 }),
    leaf: new THREE.MeshStandardMaterial({ color: 0x6fae3f, roughness: 0.6 }),
    meat: new THREE.MeshStandardMaterial({ color: 0xa8603a, roughness: 0.7 }),
    onion: new THREE.MeshStandardMaterial({ color: 0xf1e6d2, roughness: 0.55 }),
    jarFill: [0xf0cf8a, 0x8b5a2b, 0xf4f1e8, 0xd96b2b, 0x6b8e3a, 0xc9a26b].map(c => new THREE.MeshStandardMaterial({ color: c, roughness: 0.8 })),
  };
  LM.marble = new THREE.MeshPhysicalMaterial({ map: marbleTexture(), roughness: 0.22, clearcoat: 0.6, clearcoatRoughness: 0.2 });
  return LM;
}
function marbleTexture() {
  const c = document.createElement('canvas'); c.width = 2048; c.height = 512; const g = c.getContext('2d');
  g.fillStyle = '#f2f1ee'; g.fillRect(0, 0, c.width, c.height);
  let seed = 7; const rnd = () => { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
  for (let i = 0; i < 46; i++) {
    g.strokeStyle = `rgba(${120 + rnd() * 40},${122 + rnd() * 40},${128 + rnd() * 40},${0.08 + rnd() * 0.22})`;
    g.lineWidth = 0.6 + rnd() * 3.2; g.filter = `blur(${rnd() * 1.6}px)`;
    g.beginPath(); let x = rnd() * c.width, y = rnd() * c.height; g.moveTo(x, y);
    for (let k = 0; k < 6; k++) { const nx = x + (rnd() - 0.3) * 420, ny = y + (rnd() - 0.5) * 160; g.quadraticCurveTo((x + nx) / 2 + (rnd() - 0.5) * 120, (y + ny) / 2 + (rnd() - 0.5) * 80, nx, ny); x = nx; y = ny; }
    g.stroke();
  }
  g.filter = 'none';
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t;
}
function mulberry(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }

// ---------------------------------------------------------------- props
function buildTray(w = 30, d = 20, h = 6) {
  const L = lmat(); const g = new THREE.Group(); g.name = 'tray';
  const base = rbox(w, 0.5, d, 0.2, L.chrome); base.position.y = 0.25; g.add(base);
  [[0, d / 2, w, 0.5], [0, -d / 2, w, 0.5]].forEach(([x, z, ww, t]) => { const s = rbox(ww, h, t, 0.2, L.chrome); s.position.set(x, h / 2, z); s.rotation.x = z > 0 ? -0.12 : 0.12; g.add(s); });
  [[w / 2, 0], [-w / 2, 0]].forEach(([x]) => { const s = rbox(0.5, h, d, 0.2, L.chrome); s.position.set(x, h / 2, 0); s.rotation.z = x > 0 ? 0.12 : -0.12; g.add(s); });
  for (const s of [-1, 1]) { const hd = new THREE.Mesh(new THREE.TorusGeometry(3.2, 0.5, 12, 24, Math.PI), L.steel); hd.position.set(s * (w / 2 + 0.6), h - 0.6, 0); hd.rotation.set(Math.PI / 2, 0, s > 0 ? -Math.PI / 2 : Math.PI / 2); hd.castShadow = true; g.add(hd); }
  const rnd = mulberry(11);
  const pasta = new THREE.CylinderGeometry(0.55, 0.55, 2.6, 10);
  for (let i = 0; i < 170; i++) {
    const m = new THREE.Mesh(pasta, L.noodle); const r = Math.sqrt(rnd());
    m.position.set((rnd() - 0.5) * (w - 4), 1.2 + rnd() * 2.6 * (1 - r * 0.4), (rnd() - 0.5) * (d - 4)); m.rotation.set(rnd() * 3, rnd() * 3, rnd() * 3); m.castShadow = true; g.add(m);
  }
  for (let i = 0; i < 70; i++) { const hb = rbox(0.9, 0.12, 0.5, 0.05, L.herb); hb.position.set((rnd() - 0.5) * (w - 6), 4.2 + rnd() * 0.8, (rnd() - 0.5) * (d - 6)); hb.rotation.set(rnd(), rnd() * 3, rnd()); g.add(hb); }
  return g;
}
function buildJar(h = 16, r = 5, fill = 0) {
  const L = lmat(); const g = new THREE.Group();
  const body = cyl(r, h, L.glass, 40); body.position.y = h / 2; body.castShadow = false; g.add(body);
  const content = cyl(r - 0.5, h * 0.62, L.jarFill[fill % L.jarFill.length], 32); content.position.y = h * 0.31 + 0.2; g.add(content);
  const lid = softCyl(r + 0.2, 1.4, 0.3, L.steel, 40); lid.position.y = h + 0.7; g.add(lid);
  return g;
}
function buildBottle(h = 26, r = 3.6) {
  const L = lmat();
  const pts = [V(0, 0), V(r, 0), V(r, h * 0.62), V(r * 0.45, h * 0.8), V(r * 0.35, h * 0.95), V(r * 0.38, h)].map(v => new THREE.Vector2(v.x, v.y));
  const m = new THREE.Mesh(new THREE.LatheGeometry(pts, 32), L.amber); m.castShadow = true;
  const cap = cyl(r * 0.42, 2.0, L.steel, 24); cap.position.y = h + 1.0;
  const g = new THREE.Group(); g.add(m); g.add(cap); return g;
}
function buildFaucet() {
  const L = lmat(); const g = new THREE.Group();
  const base = cyl(2.2, 3, L.chrome, 32); base.position.y = 1.5; g.add(base);
  const curve = new THREE.CatmullRomCurve3([V(0, 2, 0), V(0, 26, 0), V(0, 36, 6), V(0, 33, 15), V(0, 26, 17)]);
  const tube = new THREE.Mesh(new THREE.TubeGeometry(curve, 64, 1.1, 20, false), L.chrome); tube.castShadow = true; g.add(tube);
  const lever = rbox(1.0, 1.0, 7, 0.4, L.chrome); lever.position.set(2.6, 12, 0); lever.rotation.x = -0.4; g.add(lever);
  return g;
}
function hangTool(tool, upRot) { const g = new THREE.Group(); tool.rotation.x = upRot; g.add(tool); return g; }
// ladle held at its grip (origin) with the bowl along +z
function ladleTool(len = 26) { const L = buildLadle(len); const g = new THREE.Group(); L.position.set(0, -1.9, len + 1); g.add(L); g.userData.tip = V(0, -1.9 - 3.0, len + 1); return g; }
function potLid(r = 12) {
  const L = lmat(); const g = new THREE.Group(); g.name = 'potLid';
  const disk = softCyl(r + 0.4, 1.2, 0.5, L.steel, 64); disk.position.y = 0.6; g.add(disk);
  const dome = new THREE.Mesh(new THREE.SphereGeometry(r, 48, 16, 0, Math.PI * 2, 0, 0.32), L.steel); dome.position.y = -r * Math.cos(0.32) + 1.6; dome.castShadow = true; g.add(dome);
  const knob = softCyl(1.8, 2.6, 0.6, MAT.graphite, 32); knob.position.y = 4.3; g.add(knob);
  g.userData.grip = V(0, 5.2, 0);
  return g;
}

// ---------------------------------------------------------------- kitchen
// niche x in [-125, 125], counter top y=92, niche ceiling y=186, back z=-60, counter front z=+2
export function buildLuxe(s, p) {
  const L = lmat();
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(2000, 1400), L.floor); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; s.add(floor);
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(2000, 700), new THREE.MeshStandardMaterial({ color: 0x141518, roughness: 0.8 })); wall.position.set(0, 300, -64); s.add(wall);
  // lower cabinets
  const lower = rbox(250, 84, 60, 0.4, L.cab); lower.position.set(0, 46, -30); s.add(lower);
  for (const y of [30, 62]) { const gr = rbox(248, 0.5, 0.6, 0.1, L.groove); gr.position.set(0, y, 0.1); s.add(gr); }
  for (const x of [-62.5, 0, 62.5]) { const gr = rbox(0.5, 82, 0.6, 0.1, L.groove); gr.position.set(x, 46, 0.1); s.add(gr); }
  const plinth = rbox(248, 4, 56, 0.3, L.groove); plinth.position.set(0, 2, -32); s.add(plinth);
  const top = rbox(252, 4.0, 64, 0.5, L.marble); top.position.set(0, 90, -29); s.add(top);
  // niche
  const back = new THREE.Mesh(new THREE.PlaneGeometry(250, 94), L.back); back.position.set(0, 139, -59.5); s.add(back);
  for (const sx of [-1, 1]) { const sw = new THREE.Mesh(new THREE.PlaneGeometry(60, 94), L.side); sw.rotation.y = -sx * Math.PI / 2; sw.position.set(sx * 124.4, 139, -30); sw.receiveShadow = false; sw.castShadow = false; s.add(sw); }
  const ceil = rbox(250, 2, 60, 0.2, L.side); ceil.position.set(0, 187, -30); ceil.receiveShadow = false; ceil.castShadow = false; s.add(ceil);
  const ledStrip = rbox(240, 0.6, 1.4, 0.2, L.led); ledStrip.position.set(0, 185.6, -6); s.add(ledStrip);
  // bulkhead / upper frame and pillars
  const bulk = rbox(360, 70, 66, 0.4, L.cab); bulk.position.set(0, 223, -31); s.add(bulk);
  for (const sx of [-1, 1]) { const pil = rbox(56, 256, 66, 0.4, L.cab); pil.position.set(sx * 153, 128, -31); s.add(pil); }
  // left pillar: built-in oven; right pillar: fridge column
  const oven = rbox(48, 52, 1.2, 0.4, L.ovenGlass); oven.position.set(-153, 120, 2.6); s.add(oven);
  const ovenH = buildBarHandle(36, L.steel); ovenH.rotation.z = Math.PI / 2; ovenH.position.set(-135, 141, 2.6); s.add(ovenH);
  const ovenPanel = rbox(48, 8, 1.0, 0.3, L.ovenGlass); ovenPanel.position.set(-153, 152, 2.6); s.add(ovenPanel);
  for (const x of [-166, -140]) { const k = cyl(1.4, 1.4, L.steel, 24); k.rotation.x = Math.PI / 2; k.position.set(x, 152, 3.5); s.add(k); }
  const frH = buildBarHandle(80, L.steel); frH.position.set(129, 70, 2.0); s.add(frH);
  const fgr = rbox(0.6, 250, 0.6, 0.1, L.groove); fgr.position.set(126, 128, 2.2); s.add(fgr);
  // hob + knob, sink + faucet
  const hob = rbox(62, 0.7, 48, 0.3, L.hob); hob.position.set(-48, 92.35, -30); s.add(hob);
  const ringM = new THREE.MeshBasicMaterial({ color: 0x34383e });
  [[-62, -38], [-34, -24]].forEach(([x, z]) => { const rg = new THREE.Mesh(new THREE.TorusGeometry(10, 0.16, 6, 64), ringM); rg.rotation.x = Math.PI / 2; rg.position.set(x, 92.74, z); s.add(rg); });
  const knob = buildKnob(2.6, 2.2); knob.position.set(-48, 92.7, -11); s.add(knob);
  const sinkRim = rbox(52, 0.5, 40, 0.3, L.steel); sinkRim.position.set(62, 92.3, -32); s.add(sinkRim);
  const sinkIn = rbox(46, 0.6, 34, 0.3, L.sinkIn); sinkIn.position.set(62, 92.45, -32); s.add(sinkIn);
  const drain = cyl(2.2, 0.2, L.steel, 24); drain.position.set(62, 92.8, -32); s.add(drain);
  const fau = buildFaucet(); fau.position.set(62, 92, -55); s.add(fau);
  // tools rail with hanging human utensils
  const rail = cyl(0.7, 210, L.chrome, 24); rail.rotation.z = Math.PI / 2; rail.position.set(0, 154, -55); s.add(rail);
  for (const x of [-104, 104]) { const br = cyl(0.6, 4, L.chrome, 16); br.rotation.x = Math.PI / 2; br.position.set(x, 154, -57.5); s.add(br); }
  const tools = [];
  const mk = [() => buildLadle(24), () => buildTurner(26), () => buildTongs(26, 0.03), () => buildLadle(20), () => buildTurner(24), () => buildTongs(24, 0.03), () => buildLadle(24), () => buildTurner(26)];
  const xs = [-92, -70, -48, 4, 26, 48, 74, 96];
  xs.forEach((x, i) => {
    const t = mk[i % mk.length](); const isT = t.name === 'tongs';
    const h = hangTool(t, isT ? Math.PI / 2 : Math.PI / 2); h.position.set(x, isT ? 152.5 : 151, -54); s.add(h); tools.push(h);
    const hook = new THREE.Mesh(new THREE.TorusGeometry(1.1, 0.18, 8, 16, Math.PI * 1.3), L.chrome); hook.position.set(x, 153.5, -54.5); hook.rotation.y = Math.PI / 2; s.add(hook);
  });
  // jar shelf
  const shelf = rbox(200, 1.0, 16, 0.3, L.glass); shelf.position.set(0, 166, -52); s.add(shelf);
  for (const x of [-98, 98]) { const br = cyl(0.5, 14, L.chrome, 12); br.rotation.x = Math.PI / 2; br.position.set(x, 165.4, -52); s.add(br); }
  [-84, -66, -48, -30, 30, 48, 66, 84].forEach((x, i) => { const j = buildJar(i % 2 ? 14 : 17, 5, i); j.position.set(x, 166.5, -52); s.add(j); });
  // counter props
  const pot = buildPot(12, 14); pot.position.set(-62, 92.7, -38); s.add(pot);
  const pan = buildPan(12, 19); pan.position.set(-34, 92.7, -24); pan.rotation.y = num(p, 'panYaw', -150) * D; s.add(pan);
  [[-4, 2, L.meat], [3, -2, L.leaf], [0, 5, L.pepper], [5, 4, L.meat], [-3, -4, L.onion], [1, 0, L.pepper]].forEach(([x, z, m]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.9, 18, 12), m); f.scale.set(1.4, 0.55, 1.0); f.position.set(x, 5.0, z); f.castShadow = true; pan.add(f); });
  const tray = buildTray(30, 20, 6); tray.position.set(10, 92.2, -14); tray.rotation.y = 0.12; s.add(tray);
  const bowl = buildBowl(8, 5.5); bowl.position.set(-6, 92, -44); s.add(bowl);
  const toms = [];
  [[-8, -45], [-4, -42], [-6, -48]].forEach(([x, z], i) => { const t = new THREE.Mesh(new THREE.SphereGeometry(2.9, 28, 18), L.tomato); t.position.set(x, 95.6 + i * 0.8, z); t.castShadow = true; s.add(t); toms.push(t); });
  const plate = buildPlate(12); plate.position.set(34, 92.2, -6); s.add(plate);
  [[-3, 1, L.meat], [2.5, -2, L.leaf], [1, 3.5, L.pepper]].forEach(([x, z, m]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.9, 18, 12), m); f.scale.set(1.4, 0.55, 1.0); f.position.set(x, 1.9, z); f.castShadow = true; plate.add(f); });
  [[92, -50], [100, -46]].forEach(([x, z], i) => { const b = buildBottle(i ? 22 : 26, 3.4); b.position.set(x, 92.2, z); s.add(b); });
  return { pot, pan, tray, bowl, toms, plate, knob, tools };
}

function luxeLights(s, p) {
  const key = new THREE.DirectionalLight(0xffffff, num(p, 'key', 1.25)); key.position.set(...vec(p, 'keyPos', [-120, 360, 420])); key.castShadow = true;
  key.shadow.mapSize.set(4096, 4096); Object.assign(key.shadow.camera, { left: -200, right: 200, top: 200, bottom: -200, near: 1, far: 1600 });
  key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02; key.shadow.radius = 5; key.target.position.set(0, 100, -30); s.add(key); s.add(key.target);
  const down = new THREE.DirectionalLight(0xfff8ee, num(p, 'down', 0.85)); down.position.set(10, 400, -20); down.castShadow = true;
  down.shadow.mapSize.set(2048, 2048); Object.assign(down.shadow.camera, { left: -140, right: 140, top: 80, bottom: -80, near: 1, far: 800 }); down.shadow.radius = 8; down.shadow.bias = -0.0005;
  down.target.position.set(10, 90, -30); s.add(down); s.add(down.target);
  const rim = new THREE.DirectionalLight(0xdfe8ff, 0.35); rim.position.set(260, 180, -80); s.add(rim);
  const fill = new THREE.HemisphereLight(0xffffff, 0x202124, num(p, 'hemi', 0.32)); s.add(fill);
}

function frameXZ(xAxis, zAxis, pos) {
  const x = xAxis.clone().normalize(); const z0 = zAxis.clone().normalize();
  const y = new THREE.Vector3().crossVectors(z0, x).normalize(); const z = new THREE.Vector3().crossVectors(x, y).normalize();
  return new THREE.Matrix4().makeBasis(x, y, z).setPosition(pos);
}
// hand frame such that a tool held in the hand points along `dir` with its tip at `tipW`
function toolFrame(tool, dir, sideHint, tipW) {
  const handTmp = new THREE.Group(); const tl = tool.clone(); handTmp.add(tl); handTmp.updateMatrixWorld(true);
  const tipL = tl.localToWorld(tool.userData.tip.clone()); const baseL = tl.localToWorld(V(0, 0, 0));
  const axisL = tipL.clone().sub(baseL).normalize();
  const xL0 = V(1, 0, 0); const zL = axisL; const yL = new THREE.Vector3().crossVectors(zL, xL0).normalize(); const xL = new THREE.Vector3().crossVectors(yL, zL).normalize();
  const mL = new THREE.Matrix4().makeBasis(xL, yL, zL);
  const zW = dir.clone().normalize(); const yW = new THREE.Vector3().crossVectors(zW, sideHint.clone().normalize()).normalize(); const xW = new THREE.Vector3().crossVectors(yW, zW).normalize();
  const mW = new THREE.Matrix4().makeBasis(xW, yW, zW);
  const R = mW.clone().multiply(mL.clone().invert());
  const pos = tipW.clone().sub(tipL.clone().applyMatrix4(new THREE.Matrix4().extractRotation(R)));
  return R.setPosition(pos);
}
function placeHand(robot, graspWorld, graspLocal, q0) {
  const target = graspWorld.clone().multiply(new THREE.Matrix4().makeTranslation(-graspLocal.x, -graspLocal.y, -graspLocal.z));
  return solveIK(robot, target, q0, 900);
}
function capture(r, s, cam, name) { r.render(s, cam); (window.__images = window.__images || []).push({ name, data: r.domElement.toDataURL('image/png') }); }

// task: stir (ladle in pot) | toss | tongs | lid | pick | drop | knob | plate | serve ; view: front | wide | close
async function kluxe(W, H, p) {
  initMaterials(); lmat();
  const r = makeRenderer(W, H); r.toneMappingExposure = num(p, 'exp', 1.0);
  const s = makeScene(r, num(p, 'env', 0.55));
  luxeLights(s, p);
  const K = buildLuxe(s, p);
  const task = p.get('task') || 'stir';
  const rs = num(p, 'rscale', 1.0);
  const mountR = (bx, bz) => {
    const plate = rbox(22, 2, 22, 0.5, MAT.graphite); plate.position.set(bx, 185, bz); s.add(plate);
    const robot = buildCobot('A'); robot.scale.setScalar(rs); robot.rotation.set(Math.PI, num(p, 'ry', 0) * D, 0); robot.position.set(bx, 184, bz); s.add(robot); robot.updateMatrixWorld(true);
    return robot;
  };
  if (p.get('norobot') === '1') {
    const cam0 = new THREE.PerspectiveCamera(num(p, 'fov', 30), W / H, 1, 8000); cam0.position.set(...vec(p, 'cam', [10, 150, 170])); cam0.lookAt(...vec(p, 'look', [10, 140, -50]));
    capture(r, s, cam0, 'color'); return { ok: 1 };
  }
  const robot = mountR(num(p, 'bx', -8), num(p, 'bz', -30));
  let pose = KPOSES.hook, gw = null, gl = V(0, 0, 0), tool = null, focus = V(-40, 105, -30);
  const q0 = vec(p, 'q0', [0, 30, 80, 40, -90, 0]).map(v => v * D);
  if (task === 'stir' || task === 'tongs' || task === 'plate' || task === 'serve') {
    pose = KPOSES.tongs;
    tool = task === 'stir' ? ladleTool(24) : buildTongs(26, 0.06);
    tool.position.set(num(p, 'tx0', 0.5), num(p, 'ty0', 21.0), num(p, 'tz0', 1.0)); tool.rotation.set(num(p, 'trx', 0.62), 0, 0);
    let tip, dir;
    if (task === 'stir') { tip = K.pot.position.clone().add(V(2, 8.5, 0)); dir = V(...vec(p, 'tdir', [-0.45, -0.85, -0.15])); }
    else if (task === 'tongs') { tip = K.pan.position.clone().add(V(1, 6.5, 0)); dir = V(...vec(p, 'tdir', [-0.35, -0.8, -0.3])); }
    else if (task === 'plate') { tip = K.plate.position.clone().add(V(2, 5, 1)); dir = V(...vec(p, 'tdir', [0.25, -0.85, 0.1])); }
    else { tip = K.tray.position.clone().add(V(0, 6.5, 0)); dir = V(...vec(p, 'tdir', [0.1, -0.85, 0.35])); }
    if (task !== 'stir') { const piece = new THREE.Mesh(new THREE.SphereGeometry(2.0, 18, 12), task === 'plate' ? lmat().meat : lmat().pepper); piece.scale.set(1.4, 0.6, 1.0); piece.position.copy(tool.userData.tip).add(V(0, 0, -1.2)); piece.castShadow = true; tool.add(piece); }
    gw = toolFrame(tool, dir, V(...vec(p, 'tside', [0, 0, 1])), tip); focus = tip;
  } else if (task === 'toss') {
    const pan = K.pan; pan.position.y += num(p, 'lift', 10); pan.rotation.z = num(p, 'tilt', -0.16); pan.updateMatrixWorld(true);
    [[-2, 9, 1, lmat().pepper], [3, 12, -2, lmat().leaf], [0, 14, 3, lmat().meat]].forEach(([x, y, z, m]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.8, 16, 12), m); f.scale.set(1.4, 0.55, 1.0); f.position.set(x, y, z); f.rotation.set(0.6, 0.3, 0.9); f.castShadow = true; pan.add(f); });
    pan.updateMatrixWorld(true);
    const hw = pan.localToWorld(pan.userData.handle.clone()); const ax = pan.localToWorld(V(1, 4.3, 0)).sub(pan.localToWorld(V(0, 4.3, 0))).normalize();
    gw = frameXZ(ax, V(0, -1, num(p, 'tz', 0.2)), hw); gl = V(0, 19.2, 4.6); focus = hw;
  } else if (task === 'lid') {
    pose = KPOSES.knob; const lid = potLid(12); lid.position.copy(K.pot.position).add(V(0, 14.5 + num(p, 'lift', 8), 0)); lid.rotation.x = num(p, 'ltilt', -0.25); s.add(lid); lid.updateMatrixWorld(true);
    const g = lid.localToWorld(lid.userData.grip.clone()); const yaw = num(p, 'gyaw', 0) * D;
    gw = frameXZ(V(Math.cos(yaw), 0, Math.sin(yaw)), V(0, -1, 0), g); gl = V(0, 18.0, 2.4); focus = g;
  } else if (task === 'pick' || task === 'drop') {
    pose = KPOSES.wrapTop; const t = K.toms[0];
    let top;
    if (task === 'pick') { top = t.position.clone().add(V(0, 3.0 + num(p, 'lift', 2), 0)); t.position.y += num(p, 'lift', 2); }
    else { top = K.pan.position.clone().add(V(0, 26 + num(p, 'lift', 0), 0)); t.position.copy(top).add(V(0, -3.0, 0)); }
    const yaw = num(p, 'gyaw', 0) * D; gw = frameXZ(V(Math.cos(yaw), 0, Math.sin(yaw)), V(0, -1, 0), top); gl = V(0, 17.8, 2.6); focus = top;
  } else if (task === 'knob') {
    pose = KPOSES.knob; K.knob.rotation.y = 0.6; K.knob.updateMatrixWorld(true);
    const top = K.knob.localToWorld(V(0, 4.4, 0)); const yaw = num(p, 'gyaw', 0) * D;
    gw = frameXZ(V(Math.cos(yaw), 0, Math.sin(yaw)), V(0, -1, 0), top); gl = V(0, 18.0, 2.4); focus = top;
  }
  const hand = buildHand(pose); hand.scale.setScalar(1 / rs); robot.userData.flange.add(hand);
  if (tool) hand.add(tool);
  const res = gw ? placeHand(robot, gw, gl, q0) : { posErr: 0, rotErr: 0, q: q0 };
  // optional second (idle) arm for the wide/front views
  if (p.get('arms') === '2') {
    const r2 = mountR(num(p, 'bx2', 62), num(p, 'bz2', -30));
    const h2 = buildHand(KPOSES.open); h2.scale.setScalar(1 / rs); r2.userData.flange.add(h2);
    const g2 = frameXZ(V(1, 0, 0), V(0, -0.2, 1), V(...vec(p, 'idle2', [70, 128, -18])));
    solveIK(r2, g2, vec(p, 'q02', [0, 30, 80, 40, -90, 0]).map(v => v * D), 700);
  }
  const view = p.get('view') || 'close';
  const CAMS = { stir: [[40, 22, 92], [-6, -2, 0], 30], toss: [[-50, 18, 100], [10, -4, 0], 30], tongs: [[-40, 26, 96], [6, 2, 0], 30],
    lid: [[46, 18, 92], [-6, -6, 0], 30], pick: [[44, 24, 96], [-6, -4, 0], 30], drop: [[-46, 18, 96], [6, -10, 0], 30], knob: [[-26, 34, 76], [4, 4, 0], 30],
    plate: [[40, 30, 90], [-4, 2, 0], 30], serve: [[34, 26, 92], [-2, 2, 0], 30] };
  let camPos, look, fov;
  if (view === 'front') { camPos = V(...vec(p, 'cam', [0, 140, 335])); look = V(...vec(p, 'look', [0, 132, -30])); fov = num(p, 'fov', 32); }
  else if (view === 'wide') { camPos = V(...vec(p, 'cam', [-230, 175, 300])); look = V(...vec(p, 'look', [-8, 124, -30])); fov = num(p, 'fov', 32); }
  else { const cd = CAMS[task]; const off = vec(p, 'off', cd[0]); const lo = vec(p, 'lookOff', cd[1]); camPos = focus.clone().add(V(...off)); look = focus.clone().add(V(...lo)); fov = num(p, 'fov', cd[2]); }
  const cam = new THREE.PerspectiveCamera(fov, W / H, 1, 8000); cam.position.copy(camPos); cam.lookAt(look);
  capture(r, s, cam, 'color');
  return { task, view, posErr: +res.posErr.toFixed(3), rotErr: +(res.rotErr || 0).toFixed(3), q: res.q.map(v => +(v / D).toFixed(1)), focus: focus.toArray().map(v => +v.toFixed(1)) };
}

export const LSCENES = { kluxe };
