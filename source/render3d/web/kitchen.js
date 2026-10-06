// Kitchen scenes for the SoftHand-4 concept renders (units: cm).
// Commercial line, home kitchen with a mobile robot, human-tool lineup, and kitchen task panels.
import { THREE, initMaterials, MAT, buildHand, makeRenderer, makeScene, addLights, shadowCatcher, buildCobot, solveIK, rbox, cyl, softCyl } from './lib.js';

const D = Math.PI / 180;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const num = (p, k, d) => (p.get(k) !== null && p.get(k) !== undefined && p.get(k) !== '' ? +p.get(k) : d);
const vec = (p, k, d) => (p.get(k) ? p.get(k).split(',').map(Number) : d);

export const KPOSES = {
  hook: { fingers: [{ spread: -3, mcp: 52, pip: 72, dip: 40 }, { spread: 0, mcp: 50, pip: 72, dip: 40 }, { spread: 3, mcp: 48, pip: 70, dip: 40 }], thumb: { swing: 18, roll: 75, cmc: 35, mcp: 35, ip: 25 } },
  wrapTop: { fingers: [{ spread: -6, mcp: 62, pip: 48, dip: 22 }, { spread: 0, mcp: 60, pip: 48, dip: 22 }, { spread: 6, mcp: 58, pip: 46, dip: 22 }], thumb: { swing: 10, roll: 82, cmc: 48, mcp: 30, ip: 22 } },
  knob: { fingers: [{ spread: -10, mcp: 58, pip: 52, dip: 30 }, { spread: 0, mcp: 56, pip: 52, dip: 30 }, { spread: 10, mcp: 54, pip: 50, dip: 30 }], thumb: { swing: 12, roll: 84, cmc: 50, mcp: 34, ip: 26 } },
  tongs: { fingers: [{ spread: -4, mcp: 74, pip: 88, dip: 50 }, { spread: 0, mcp: 72, pip: 88, dip: 50 }, { spread: 4, mcp: 70, pip: 86, dip: 50 }], thumb: { swing: 14, roll: 80, cmc: 42, mcp: 40, ip: 30 } },
  open: { fingers: [{ spread: -6, mcp: 14, pip: 18, dip: 12 }, { spread: -1, mcp: 10, pip: 14, dip: 10 }, { spread: 4, mcp: 6, pip: 10, dip: 8 }], thumb: { swing: 28, roll: 40, cmc: 14, mcp: 16, ip: 10 } },
};

let KM = null;
function kmat() {
  if (KM) return KM;
  KM = {
    steel: new THREE.MeshStandardMaterial({ color: 0xc3c8ce, metalness: 0.85, roughness: 0.36 }),
    steelBrushed: new THREE.MeshStandardMaterial({ color: 0xb9bec5, metalness: 0.8, roughness: 0.46 }),
    steelDark: new THREE.MeshStandardMaterial({ color: 0x8f959d, metalness: 0.85, roughness: 0.42 }),
    black: new THREE.MeshStandardMaterial({ color: 0x1d1f23, roughness: 0.5 }),
    hob: new THREE.MeshPhysicalMaterial({ color: 0x121417, roughness: 0.12, clearcoat: 1.0, clearcoatRoughness: 0.08 }),
    wall: new THREE.MeshStandardMaterial({ color: 0xeceae6, roughness: 0.92 }),
    tile: new THREE.MeshStandardMaterial({ color: 0x2b2d31, roughness: 0.38 }),
    floorPro: new THREE.MeshStandardMaterial({ color: 0x2a2b2e, roughness: 0.5 }),
    floorHome: new THREE.MeshStandardMaterial({ color: 0xc8ab86, roughness: 0.7 }),
    oak: new THREE.MeshStandardMaterial({ color: 0xc69f72, roughness: 0.62 }),
    cabWhite: new THREE.MeshPhysicalMaterial({ color: 0xf2f1ed, roughness: 0.5, clearcoat: 0.1 }),
    quartz: new THREE.MeshPhysicalMaterial({ color: 0xf4f3f0, roughness: 0.28, clearcoat: 0.5 }),
    fridge: new THREE.MeshPhysicalMaterial({ color: 0xdfe1e3, roughness: 0.32, metalness: 0.35, clearcoat: 0.4 }),
    ceramic: new THREE.MeshPhysicalMaterial({ color: 0xf6f5f2, roughness: 0.22, clearcoat: 0.7 }),
    board: new THREE.MeshStandardMaterial({ color: 0xd8b98c, roughness: 0.7 }),
    tomato: new THREE.MeshPhysicalMaterial({ color: 0xd8432a, roughness: 0.35, clearcoat: 0.6 }),
    leaf: new THREE.MeshStandardMaterial({ color: 0x6fae3f, roughness: 0.6 }),
    pepper: new THREE.MeshPhysicalMaterial({ color: 0xf0b229, roughness: 0.35, clearcoat: 0.5 }),
    onion: new THREE.MeshStandardMaterial({ color: 0xf1e6d2, roughness: 0.55 }),
    meat: new THREE.MeshStandardMaterial({ color: 0xa8603a, roughness: 0.7 }),
    noodle: new THREE.MeshStandardMaterial({ color: 0xf1d49a, roughness: 0.7 }),
    glassDark: new THREE.MeshPhysicalMaterial({ color: 0x20262c, roughness: 0.1, transparent: true, opacity: 0.45, clearcoat: 1 }),
    plant: new THREE.MeshStandardMaterial({ color: 0x5d8a46, roughness: 0.7 }),
  };
  return KM;
}

// ---------------------------------------------------------------- props
export function buildPan(r = 12, handleLen = 20, mat = null) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'pan';
  const body = softCyl(r, 4.4, 1.3, mat || new THREE.MeshPhysicalMaterial({ color: 0x23262b, roughness: 0.34, clearcoat: 0.6 })); body.position.y = 2.2; g.add(body);
  const inner = cyl(r - 1.0, 0.5, new THREE.MeshStandardMaterial({ color: 0x2d3137, roughness: 0.62 }), 48); inner.position.y = 4.2; g.add(inner);
  const h = cyl(1.25, handleLen, M.black, 24); h.rotation.z = Math.PI / 2; h.position.set(r + handleLen / 2 - 0.5, 4.3, 0); g.add(h);
  const rivet = cyl(1.0, 2.2, M.steel, 20); rivet.rotation.z = Math.PI / 2; rivet.position.set(r + 0.4, 4.3, 0); g.add(rivet);
  g.userData.handle = V(r + handleLen * 0.62, 4.3, 0); g.userData.r = r;
  return g;
}
export function buildPot(r = 11, h = 13) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'pot';
  const body = softCyl(r, h, 0.8, M.steel); body.position.y = h / 2; g.add(body);
  const rim = new THREE.Mesh(new THREE.TorusGeometry(r, 0.35, 10, 64), M.steel); rim.rotation.x = Math.PI / 2; rim.position.y = h; g.add(rim);
  for (const s of [-1, 1]) { const lp = new THREE.Mesh(new THREE.TorusGeometry(2.4, 0.45, 10, 24, Math.PI), M.steelDark); lp.position.set(s * (r + 0.4), h - 2.2, 0); lp.rotation.y = s > 0 ? -Math.PI / 2 : Math.PI / 2; lp.rotation.x = Math.PI / 2; lp.castShadow = true; g.add(lp); }
  return g;
}
export function buildTongs(len = 26, open = 0.07) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'tongs';
  // hinge loop at z=0, arms toward +z; tips at z=len
  for (const s of [-1, 1]) {
    const arm = new THREE.Group(); arm.rotation.x = s * open; g.add(arm);
    const bar = rbox(1.7, 0.45, len, 0.18, M.steel); bar.position.set(0, s * 0.6, len / 2); arm.add(bar);
    const grip = rbox(1.95, 0.75, 10, 0.3, M.black); grip.position.set(0, s * 0.72, 6.0); arm.add(grip);
    const tip = rbox(2.4, 0.5, 3.6, 0.2, M.steel); tip.position.set(0, s * 0.35, len - 0.8); tip.rotation.x = -s * 0.35; arm.add(tip);
  }
  const loop = new THREE.Mesh(new THREE.TorusGeometry(1.0, 0.25, 10, 24), M.steel); loop.rotation.y = Math.PI / 2; loop.position.set(0, 0, -0.6); g.add(loop);
  g.userData.tip = V(0, 0, len + 0.4);
  return g;
}
export function buildLadle(len = 30) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'ladle';
  const pts = []; for (let i = 0; i <= 12; i++) { const a = (i / 12) * Math.PI / 2; pts.push(new THREE.Vector2(Math.sin(a) * 4.2, -Math.cos(a) * 3.2)); }
  const bowl = new THREE.Mesh(new THREE.LatheGeometry(pts, 40), new THREE.MeshStandardMaterial({ color: 0xc3c8ce, metalness: 0.85, roughness: 0.3, side: THREE.DoubleSide })); bowl.castShadow = true; g.add(bowl);
  const stem = rbox(1.0, 0.4, len, 0.15, M.steel); stem.position.set(0, 0.2, -len / 2 - 3.4); stem.rotation.x = -0.12; g.add(stem);
  const grip = rbox(1.6, 0.8, 10, 0.3, M.black); grip.position.set(0, 1.9, -len - 1); grip.rotation.x = -0.12; g.add(grip);
  return g;
}
export function buildTurner(len = 28) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'turner';
  const blade = rbox(8.5, 0.3, 10, 0.12, M.steel); blade.position.set(0, 0, 5); g.add(blade);
  for (let i = 0; i < 3; i++) { const slot = rbox(0.6, 0.34, 6, 0.1, M.black); slot.position.set(-2.4 + i * 2.4, 0.02, 5.2); g.add(slot); }
  const neck = rbox(1.2, 0.35, 6, 0.12, M.steel); neck.position.set(0, 1.0, -2.6); neck.rotation.x = -0.35; g.add(neck);
  const grip = rbox(1.8, 1.0, len - 12, 0.4, M.black); grip.position.set(0, 2.6, -5.6 - (len - 12) / 2); grip.rotation.x = -0.08; g.add(grip);
  return g;
}
export function buildKnife(len = 32) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'knife';
  const shape = new THREE.Shape(); shape.moveTo(0, 0); shape.lineTo(19, 0); shape.quadraticCurveTo(21.5, 0.6, 22, 2.6); shape.lineTo(0, 4.2); shape.lineTo(0, 0);
  const blade = new THREE.Mesh(new THREE.ExtrudeGeometry(shape, { depth: 0.18, bevelEnabled: false }), new THREE.MeshStandardMaterial({ color: 0xd2d6db, metalness: 0.9, roughness: 0.22 }));
  blade.rotation.x = -Math.PI / 2; blade.position.set(0, 0.3, 0); blade.castShadow = true; g.add(blade);
  const handle = rbox(11, 1.6, 2.4, 0.6, M.black); handle.position.set(-5.6, 1.0, -2.0); g.add(handle);
  return g;
}
export function buildKnob(r = 2.6, h = 2.6) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'knob';
  const base = softCyl(r + 0.9, 0.5, 0.15, M.steel); base.position.y = 0.25; g.add(base);
  const body = softCyl(r, h, 0.5, M.black); body.position.y = 0.5 + h / 2; g.add(body);
  const ridge = rbox(r * 1.7, 1.0, 0.8, 0.3, M.black); ridge.position.y = 0.5 + h + 0.35; g.add(ridge);
  const mark = rbox(0.3, 0.12, r * 0.9, 0.05, new THREE.MeshStandardMaterial({ color: 0xe2571b, roughness: 0.5 })); mark.position.set(0, 0.5 + h + 0.9, r * 0.35); g.add(mark);
  g.userData.top = V(0, 0.5 + h + 0.9, 0);
  return g;
}
export function buildBarHandle(len = 18, mat = null) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'barHandle';
  const bar = cyl(0.75, len, mat || M.steel, 24); bar.position.set(0, len / 2, 3.2); g.add(bar);
  for (const y of [1.6, len - 1.6]) { const post = cyl(0.55, 3.2, mat || M.steel, 16); post.rotation.x = Math.PI / 2; post.position.set(0, y, 1.6); g.add(post); }
  g.userData.grip = V(0, len / 2, 3.2);
  return g;
}
export function buildPlate(r = 12) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'plate';
  const pts = [V(0, 0, 0), V(r * 0.62, 0, 0), V(r * 0.7, 0.5, 0), V(r, 1.6, 0), V(r, 1.9, 0), V(r * 0.68, 0.95, 0), V(0, 0.95, 0)].map(v => new THREE.Vector2(v.x, v.y));
  const pl = new THREE.Mesh(new THREE.LatheGeometry(pts, 64), M.ceramic); pl.castShadow = true; pl.receiveShadow = true; g.add(pl);
  return g;
}
export function buildBowl(r = 7.5, h = 5.5, mat = null) {
  const M = kmat();
  const pts = []; for (let i = 0; i <= 12; i++) { const a = (i / 12) * Math.PI / 2; pts.push(new THREE.Vector2(Math.sin(a) * r, h - Math.cos(a) * h)); }
  pts.push(new THREE.Vector2(r - 0.4, h)); for (let i = 12; i >= 0; i--) { const a = (i / 12) * Math.PI / 2; pts.push(new THREE.Vector2(Math.sin(a) * (r - 0.4), h - Math.cos(a) * (h - 0.4))); }
  const b = new THREE.Mesh(new THREE.LatheGeometry(pts, 56), mat || M.ceramic); b.castShadow = true; b.receiveShadow = true;
  const g = new THREE.Group(); g.add(b); return g;
}
// GN container (stainless hotel pan) with contents
export function buildGN(w = 17.6, d = 16.2, h = 10, content = null, n = 7) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'gn';
  const wallT = 0.25;
  const bottom = rbox(w - 1.2, wallT, d - 1.2, 0.1, M.steel); bottom.position.y = wallT / 2; g.add(bottom);
  [[0, d / 2, w, wallT], [0, -d / 2, w, wallT]].forEach(([x, z, ww, t]) => { const s = rbox(ww, h, t, 0.1, M.steel); s.position.set(x, h / 2, z); g.add(s); });
  [[w / 2, 0], [-w / 2, 0]].forEach(([x, z]) => { const s = rbox(wallT, h, d, 0.1, M.steel); s.position.set(x, h / 2, z); g.add(s); });
  const lip = rbox(w + 1.6, 0.3, d + 1.6, 0.15, M.steel); lip.position.y = h; g.add(lip);
  const lipHole = rbox(w - 0.2, 0.32, d - 0.2, 0.1, new THREE.MeshStandardMaterial({ color: 0x202226 })); lipHole.position.y = h + 0.01; lipHole.visible = false; g.add(lipHole);
  const items = [];
  if (content) {
    const fill = new THREE.Mesh(new THREE.BoxGeometry(w - 0.8, h - 3.5, d - 0.8), content.base || M.leaf); fill.position.y = (h - 3.5) / 2 + 0.3; fill.receiveShadow = true; g.add(fill);
    const rnd = mulberry(content.seed || 3);
    for (let i = 0; i < n; i++) {
      const r = content.r || 2.6;
      const m = new THREE.Mesh(content.geo ? content.geo(r) : new THREE.SphereGeometry(r, 24, 16), content.mat);
      const x = (rnd() - 0.5) * (w - 2 * r - 1), z = (rnd() - 0.5) * (d - 2 * r - 1);
      m.position.set(x, h - 3.0 + r * 0.55, z); if (content.squash) m.scale.set(1, content.squash, 1);
      m.rotation.set(rnd() * 3, rnd() * 3, rnd() * 3); m.castShadow = true; g.add(m); items.push(m);
    }
  }
  g.userData = { w, d, h, items };
  return g;
}
export function buildGNLid(w = 17.6, d = 16.2) {
  const M = kmat(); const g = new THREE.Group(); g.name = 'lid';
  const plate = rbox(w + 1.6, 0.5, d + 1.6, 0.2, M.steel); plate.position.y = 0.25; g.add(plate);
  const rise = rbox(w - 1.5, 0.9, d - 1.5, 0.4, M.steel); rise.position.y = 0.8; g.add(rise);
  const handle = buildBarHandle(7.0, M.black); handle.rotation.set(-Math.PI / 2, 0, Math.PI / 2); handle.position.set(-3.5, 1.2, 0); g.add(handle);
  // handle grip (bar along X at height ~4.4)
  g.userData.grip = V(0, 1.2 + 3.2, 0);
  return g;
}
function mulberry(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }

// ---------------------------------------------------------------- frames
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
  return solveIK(robot, target, q0, 900);
}
function capture(r, s, cam, name) { r.render(s, cam); (window.__images = window.__images || []).push({ name, data: r.domElement.toDataURL('image/png') }); }
function makeCam(W, H, p, defCam, defLook, defFov) {
  const cam = new THREE.PerspectiveCamera(num(p, 'fov', defFov), W / H, 1, 8000);
  cam.position.set(...vec(p, 'cam', defCam)); cam.lookAt(...vec(p, 'look', defLook)); return cam;
}

// ---------------------------------------------------------------- commercial line
// counter top y=90, x in [-115, 115], z in [-36, 34]; robot mounted on the counter back center
function buildCommercial(s, p) {
  const M = kmat();
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(1200, 900), M.floorPro); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; s.add(floor);
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(1200, 400), M.tile); wall.position.set(0, 200, -62); wall.receiveShadow = true; s.add(wall);
  const splash = rbox(232, 56, 1.2, 0.3, M.steelBrushed); splash.position.set(0, 120, -60.5); s.add(splash);
  // base cabinets (stainless doors)
  const cab = rbox(230, 86, 66, 0.8, M.steelBrushed); cab.position.set(0, 47, -1); s.add(cab);
  const kick = rbox(226, 8, 60, 0.5, M.black); kick.position.set(0, 4, -3); s.add(kick);
  for (let i = 0; i < 4; i++) { const seam = rbox(0.3, 74, 0.3, 0.1, M.steelDark); seam.position.set(-57.5 + i * 57.5, 48, 32.2); s.add(seam); }
  for (let i = 0; i < 4; i++) { const hd = rbox(22, 1.2, 2.0, 0.5, M.steel); hd.position.set(-86 + i * 57.5, 80, 33.4); s.add(hd); }
  const top = rbox(234, 4, 72, 0.6, M.steel); top.position.set(0, 90, -1); s.add(top);
  // induction range zone (left)
  const hob = rbox(64, 0.8, 50, 0.3, M.hob); hob.position.set(-62, 92.3, -6); s.add(hob);
  const ringM = new THREE.MeshBasicMaterial({ color: 0x3b4047 });
  [[-76, -10], [-48, -10]].forEach(([x, z]) => { const rg = new THREE.Mesh(new THREE.TorusGeometry(10, 0.18, 6, 64), ringM); rg.rotation.x = Math.PI / 2; rg.position.set(x, 92.75, z); s.add(rg); });
  const knobs = [];
  [-80, -62, -44].forEach((x) => { const k = buildKnob(2.4, 2.4); k.position.set(x, 92.2, 13.5); s.add(k); knobs.push(k); });
  // prep rail with GN pans (right)
  // countertop cold rail: open-top stainless frame holding GN 1/6 pans
  const ux = 62, uz = -14, uw = 84, ud = 22, uh = 11;
  [[ux, uz - ud / 2, uw, 0.9], [ux, uz + ud / 2, uw, 0.9]].forEach(([x, z, w, t]) => { const wl = rbox(w, uh, t, 0.2, M.steelBrushed); wl.position.set(x, 92 + uh / 2, z); s.add(wl); });
  [[ux - uw / 2, uz], [ux + uw / 2, uz]].forEach(([x, z]) => { const wl = rbox(0.9, uh, ud, 0.2, M.steelBrushed); wl.position.set(x, 92 + uh / 2, z); s.add(wl); });
  const gns = [];
  const contents = [
    { mat: M.tomato, r: 3.3, base: new THREE.MeshStandardMaterial({ color: 0xb23a25, roughness: 0.6 }), seed: 5 },
    { mat: M.leaf, r: 2.2, base: new THREE.MeshStandardMaterial({ color: 0x4f8a2e, roughness: 0.7 }), seed: 9, squash: 0.7 },
    { mat: M.pepper, r: 2.0, base: new THREE.MeshStandardMaterial({ color: 0xd99a20, roughness: 0.7 }), seed: 13, squash: 0.6 },
    { mat: M.onion, r: 2.0, base: new THREE.MeshStandardMaterial({ color: 0xe5d8c0, roughness: 0.7 }), seed: 21, squash: 0.6 },
  ];
  [33, 52, 71, 90].forEach((x, i) => { const g = buildGN(17.6, 16.2, 10, contents[i], i === 0 ? 5 : 9); g.position.set(x, 92.6, -14); s.add(g); gns.push(g); });
  // upper shelf with plates
  const shelf = rbox(150, 2.0, 30, 0.4, M.steel); shelf.position.set(20, 168, -46); s.add(shelf);
  for (const x of [-30, 70]) { const br = rbox(2, 18, 26, 0.3, M.steelDark); br.position.set(x, 158, -48); s.add(br); }
  for (let k = 0; k < 4; k++) { const pl = buildPlate(11); pl.position.set(-20, 169 + k * 1.9, -44); s.add(pl); }
  for (let k = 0; k < 3; k++) { const b = buildBowl(7, 5); b.position.set(10 + k * 17, 169, -44); s.add(b); }
  const pot = buildPot(12, 14); pot.position.set(60, 169, -44); s.add(pot);
  // utensil holder
  const holder = cyl(5, 14, M.steel, 40); holder.position.set(104, 99, -22); s.add(holder);
  const lad = buildLadle(26); lad.rotation.set(-1.35, 0.3, 0.2); lad.position.set(103, 120, -21); s.add(lad);
  // plate on the pass (front right)
  const plate = buildPlate(12.5); plate.position.set(48, 92.1, 18); s.add(plate);
  [[-3, 1, KM.meat], [2.5, -2, KM.leaf], [1, 3.5, KM.pepper], [-1, -3.5, KM.onion]].forEach(([x, z, m]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.9, 18, 12), m); f.scale.set(1.4, 0.55, 1.0); f.position.set(x, 1.9, z); f.castShadow = true; plate.add(f); });
  return { knobs, gns, plate, hobCenter: V(-62, 92.8, -10) };
}

function stage(W, H, p, o = {}) {
  initMaterials(); kmat();
  const r = makeRenderer(W, H); r.toneMappingExposure = num(p, 'exp', 1.0);
  const s = makeScene(r, num(p, 'env', 0.85));
  addLights(s, { keyPos: vec(p, 'keyPos', o.keyPos || [-140, 300, 260]), key: num(p, 'key', 1.6), shadowSize: o.shadowSize || 260, rim: num(p, 'rim', 0.6), rimPos: o.rimPos || [220, 160, 40], target: o.target || [0, 90, 0], hemi: 0.45 });
  return { r, s };
}

// task: wide | lid | pick | drop | tongs | toss | knob | plate
async function kpro(W, H, p) {
  const task = p.get('task') || 'wide';
  const { r, s } = stage(W, H, p);
  const K = buildCommercial(s, p);
  const robot = buildCobot('A'); const rs = num(p, 'rscale', 1.1); robot.scale.setScalar(rs);
  if (p.get('mount') === 'over') {
    const beam = rbox(180, 4, 18, 0.6, KM.steel); beam.position.set(10, 168, -30); s.add(beam);
    const mount = rbox(22, 2, 22, 0.5, MAT.graphite); mount.position.set(num(p, 'bx', -8), 165, num(p, 'bz', -30)); s.add(mount);
    robot.rotation.set(Math.PI, num(p, 'ry', 0) * D, 0); robot.position.set(num(p, 'bx', -8), 164, num(p, 'bz', -30)); s.add(robot); robot.updateMatrixWorld(true);
  } else {
    const mount = rbox(26, 2.5, 26, 0.6, MAT.graphite); mount.position.set(num(p, 'bx', 2), 93.2, num(p, 'bz', -24)); s.add(mount);
    robot.position.set(num(p, 'bx', 2), 94.5, num(p, 'bz', -24)); robot.rotation.y = num(p, 'ry', 0) * D; s.add(robot); robot.updateMatrixWorld(true);
  }
  const pan = buildPan(12, 20); pan.position.set(-62, 92.8, -10); pan.rotation.y = num(p, 'panYaw', -20) * D; s.add(pan);
  // food in pan
  const panFood = [];
  [[-4, 2, KM.meat], [3, -2, KM.leaf], [0, 5, KM.pepper], [5, 4, KM.meat], [-3, -4, KM.onion], [1, 0, KM.pepper]].forEach(([x, z, m]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.9, 18, 12), m); f.scale.set(1.4, 0.55, 1.0); f.position.set(x, 5.0, z); f.castShadow = true; pan.add(f); panFood.push(f); });
  let pose = KPOSES.hook, gw = null, gl = null, held = null, tool = null;
  const q0 = vec(p, 'q0', [140, -35, -85, -50, 90, 0]).map(v => v * D);
  let focus = V(-40, 100, 0);
  const gn0 = K.gns[0];
  const lid = buildGNLid(17.6, 16.2);
  if (task === 'lid') {
    // lid lifted and tilted up from the front edge
    lid.position.copy(gn0.position).add(V(0, 10.3 + num(p, 'lift', 7), 0)); lid.rotation.x = num(p, 'ltilt', -0.35); s.add(lid); lid.updateMatrixWorld(true);
    const g = lid.localToWorld(lid.userData.grip.clone());
    pose = KPOSES.hook; gw = frameXZ(V(1, 0, 0), V(0, -1, num(p, 'tz', 0.25)), g); gl = V(0, num(p, 'gy', 19.2), num(p, 'gz', 4.6)); focus = g;
  } else {
    lid.position.copy(K.gns[1].position).add(V(0, 0, 0)); // closed lid on the second pan? keep scene tidy: park lid on counter
    lid.position.set(8, 92.4, 14); lid.rotation.y = 0.2; s.add(lid);
  }
  if (task === 'pick' || task === 'drop') {
    const tom = gn0.userData.items[num(p, 'item', 2)];
    const tw = tom.getWorldPosition(new THREE.Vector3());
    held = tom;
    let top;
    if (task === 'pick') { top = tw.clone().add(V(0, 3.3 + num(p, 'lift', 2), 0)); held.position.y += num(p, 'lift', 2); }
    else {
      top = V(-62 + num(p, 'dx', 0), 120 + num(p, 'lift', 0), -10 + num(p, 'dz', 0));
      gn0.remove(tom); s.add(tom); tom.position.copy(top).add(V(0, -3.3, 0));
    }
    pose = KPOSES.wrapTop; const yaw = num(p, 'gyaw', 90) * D;
    gw = frameXZ(V(Math.sin(yaw), 0, Math.cos(yaw)), V(0, -1, 0), top); gl = V(0, num(p, 'gy', 17.8), num(p, 'gz', 2.6)); focus = top;
  }
  if (task === 'tongs' || task === 'plate' || task === 'wide') {
    pose = KPOSES.tongs;
    tool = buildTongs(26, 0.06);
    // tongs in hand frame: hinge near palm, arms along hand -X? -> we hold across the fingers with tool axis along hand +Z (out of palm) bent forward
    tool.position.set(num(p, 'tx0', 0.5), num(p, 'ty0', 21.0), num(p, 'tz0', 1.0)); tool.rotation.set(num(p, 'trx', 0.62), 0, 0);
    const tipTarget = task === 'plate' ? K.plate.position.clone().add(V(3, 5.0, 2)) : V(-58, 98.5, -8);
    // desired direction of tongs (world): down and toward -z (away from camera) slightly
    const dir = V(...vec(p, 'tdir', task === 'plate' ? [0.15, -0.8, -0.55] : [0.35, -0.75, -0.55])).normalize();
    const side = V(...vec(p, 'tside', [0, 0, 1])).cross(dir).normalize();
    // build hand frame: hand X = side, tool axis (in hand) known -> solve by aligning tool axis with dir
    const handTmp = new THREE.Group(); const tl = tool.clone(); handTmp.add(tl); handTmp.updateMatrixWorld(true);
    const tipL = tl.localToWorld(tool.userData.tip.clone()); const hingeL = tl.localToWorld(V(0, 0, 0));
    const axisL = tipL.clone().sub(hingeL).normalize();
    // rotation that maps axisL -> dir and hand X -> side (approx): build orthonormal frames
    const xL = V(1, 0, 0); const zL = axisL.clone(); const yL = new THREE.Vector3().crossVectors(zL, xL).normalize(); const xL2 = new THREE.Vector3().crossVectors(yL, zL).normalize();
    const mL = new THREE.Matrix4().makeBasis(xL2, yL, zL);
    const zW = dir.clone(); const xW0 = side.clone(); const yW = new THREE.Vector3().crossVectors(zW, xW0).normalize(); const xW = new THREE.Vector3().crossVectors(yW, zW).normalize();
    const mW = new THREE.Matrix4().makeBasis(xW, yW, zW);
    const R = mW.clone().multiply(mL.clone().invert()); // hand rotation in world
    const handPos = tipTarget.clone().sub(tipL.clone().applyMatrix4(new THREE.Matrix4().extractRotation(R)));
    gw = R.clone().setPosition(handPos); gl = V(0, 0, 0); focus = tipTarget;
    const piece = new THREE.Mesh(new THREE.SphereGeometry(2.0, 18, 12), task === 'plate' ? KM.meat : KM.pepper); piece.scale.set(1.4, 0.6, 1.0);
    piece.position.copy(tool.userData.tip).add(V(0, 0, -1.2)); piece.castShadow = true; tool.add(piece);
  }
  if (task === 'toss') {
    pose = KPOSES.hook;
    pan.position.y += num(p, 'lift', 9); pan.rotation.z = num(p, 'tilt', 0.18); pan.updateMatrixWorld(true);
    // a couple of pieces in the air
    [[-2, 9, 1, KM.pepper], [3, 12, -2, KM.leaf], [0, 14, 3, KM.meat]].forEach(([x, y, z, m]) => { const f = new THREE.Mesh(new THREE.SphereGeometry(1.8, 16, 12), m); f.scale.set(1.4, 0.55, 1.0); f.position.set(x, y, z); f.rotation.set(0.6, 0.3, 0.9); f.castShadow = true; pan.add(f); });
    pan.updateMatrixWorld(true);
    const hw = pan.localToWorld(pan.userData.handle.clone());
    const ax = pan.localToWorld(V(1, 4.3, 0)).sub(pan.localToWorld(V(0, 4.3, 0))).normalize();
    gw = frameXZ(ax, V(0, -1, num(p, 'tz', 0.2)), hw); gl = V(0, num(p, 'gy', 19.2), num(p, 'gz', 4.6)); focus = hw;
  }
  if (task === 'knob') {
    pose = KPOSES.knob; const k = K.knobs[num(p, 'kn', 2)]; k.rotation.y = num(p, 'krot', 0.6); k.updateMatrixWorld(true);
    const top = k.localToWorld(V(0, 4.6 + num(p, 'lift', 0), 0)); const yaw = num(p, 'gyaw', 90) * D;
    gw = frameXZ(V(Math.sin(yaw), 0, Math.cos(yaw)), V(0, -1, 0), top); gl = V(0, num(p, 'gy', 18.0), num(p, 'gz', 2.4)); focus = top;
  }
  const hand = buildHand(pose); hand.scale.setScalar(1 / rs); robot.userData.flange.add(hand);
  if (tool) { hand.add(tool); }
  const res = gw ? placeHand(robot, gw.multiply(new THREE.Matrix4().makeScale(1, 1, 1)), gl.clone().multiplyScalar(1), q0) : { posErr: 0, rotErr: 0, q: q0 };
  // place held object in hand if moving with it
  if (task === 'wide' && p.get('cam') === null) {}
  const CAMS = { lid: [[38, 34, 92], [-2, -6, 0], 26], pick: [[34, 40, 88], [-2, -4, 0], 26], drop: [[-38, 22, 96], [0, -9, 0], 28],
    tongs: [[-46, 30, 88], [2, 4, 0], 27], toss: [[-52, 24, 96], [8, -2, 0], 28], knob: [[-30, 42, 72], [4, 2, 0], 27], plate: [[34, 42, 84], [-2, 4, 0], 27] };
  const cd = CAMS[task] || [[-55, 40, 95], [0, 0, 0], 26];
  const off = vec(p, 'off', cd[0]); const lookOff = vec(p, 'lookOff', cd[1]);
  const def = task === 'wide' ? [[-150, 205, 250], [-5, 110, -6], 30] : [[focus.x + off[0], focus.y + off[1], focus.z + off[2]], [focus.x + lookOff[0], focus.y + lookOff[1], focus.z + lookOff[2]], cd[2]];
  const cam = makeCam(W, H, p, def[0], def[1], def[2]);
  capture(r, s, cam, 'color');
  return { task, posErr: +res.posErr.toFixed(3), rotErr: +(res.rotErr || 0).toFixed(3), q: res.q.map(v => +(v / D).toFixed(1)), focus: focus.toArray().map(v => +v.toFixed(1)) };
}

// ---------------------------------------------------------------- home kitchen with a mobile manipulator
function buildHomeKitchen(s, p) {
  const M = kmat();
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(1200, 900), M.floorHome); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; s.add(floor);
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(1200, 400), M.wall); wall.position.set(0, 200, -40); wall.receiveShadow = true; s.add(wall);
  // base cabinets x in [-140, 60]
  const cab = rbox(200, 86, 60, 0.6, M.oak); cab.position.set(-40, 45, -8); s.add(cab);
  for (let i = 0; i < 4; i++) { const seam = rbox(0.4, 78, 0.4, 0.1, new THREE.MeshStandardMaterial({ color: 0x9c7a52 })); seam.position.set(-140 + 50 * (i + 1), 46, 22.1); s.add(seam); }
  const drawers = [];
  for (let i = 0; i < 4; i++) { const h = rbox(18, 1.2, 1.6, 0.5, M.black); h.position.set(-115 + i * 50, 80, 23.2); s.add(h); drawers.push(h); }
  const top = rbox(204, 4, 64, 0.8, M.quartz); top.position.set(-40, 90, -8); s.add(top);
  const kick = rbox(198, 6, 54, 0.4, M.black); kick.position.set(-40, 3, -12); s.add(kick);
  // cooktop (touch) + pot + pan
  const hob = rbox(58, 0.6, 48, 0.3, M.hob); hob.position.set(-85, 92.2, -12); s.add(hob);
  const ringM = new THREE.MeshBasicMaterial({ color: 0x3b4047 });
  [[-98, -18], [-72, -6]].forEach(([x, z]) => { const rg = new THREE.Mesh(new THREE.TorusGeometry(9, 0.16, 6, 64), ringM); rg.rotation.x = Math.PI / 2; rg.position.set(x, 92.55, z); s.add(rg); });
  const pot = buildPot(11, 13); pot.position.set(-98, 92.5, -18); s.add(pot);
  // cutting board with vegetables, bowl, plant
  const board = rbox(34, 2.0, 24, 0.6, M.board); board.position.set(-28, 93, -2); s.add(board);
  [[-34, 1, M.tomato, 3.2], [-26, -4, M.pepper, 3.0], [-20, 4, M.leaf, 2.4]].forEach(([x, z, m, r]) => { const v = new THREE.Mesh(new THREE.SphereGeometry(r, 24, 16), m); v.position.set(x, 94 + r, z); v.castShadow = true; s.add(v); });
  const knife = buildKnife(); knife.position.set(-36, 94.1, 7); knife.rotation.y = 0.25; s.add(knife);
  const bowl = buildBowl(8, 6); bowl.position.set(5, 92, -14); s.add(bowl);
  const pplant = cyl(5, 10, M.ceramic, 32); pplant.position.set(38, 97, -26); s.add(pplant);
  for (let i = 0; i < 6; i++) { const l = new THREE.Mesh(new THREE.SphereGeometry(4, 16, 12), M.plant); l.scale.set(0.5, 1.4, 0.5); l.position.set(38 + Math.sin(i) * 3, 108 + (i % 3) * 2, -26 + Math.cos(i) * 3); l.rotation.z = (i - 3) * 0.25; l.castShadow = true; s.add(l); }
  // upper cabinets
  const upper = rbox(150, 70, 36, 0.6, M.cabWhite); upper.position.set(-55, 185, -22); s.add(upper);
  for (let i = 0; i < 3; i++) { const sm = rbox(0.4, 66, 0.4, 0.1, new THREE.MeshStandardMaterial({ color: 0xd5d4cf })); sm.position.set(-80 + i * 50, 185, -3.8); s.add(sm); }
  const hood = rbox(60, 10, 40, 0.6, KM.steel); hood.position.set(-85, 145, -20); s.add(hood);
  // fridge (right), door front at z=+20
  const fr = rbox(76, 192, 66, 1.2, M.fridge); fr.position.set(102, 96, -12); s.add(fr);
  const doorSplit = rbox(74, 0.4, 0.4, 0.1, new THREE.MeshStandardMaterial({ color: 0xa9adb2 })); doorSplit.position.set(102, 120, 21.2); s.add(doorSplit);
  const fh = buildBarHandle(46, KM.steelDark); fh.position.set(70, 128, 21); s.add(fh);
  const fh2 = buildBarHandle(30, KM.steelDark); fh2.position.set(70, 70, 21); s.add(fh2);
  return { fridgeHandle: fh, pot, board, drawers };
}
function buildMobileBase() {
  const g = new THREE.Group(); g.name = 'mobileBase';
  const base = rbox(46, 22, 52, 6, MAT.white); base.position.y = 15; g.add(base);
  const bumper = rbox(48, 6, 54, 3, MAT.graphite); bumper.position.y = 5; g.add(bumper);
  for (const [x, z] of [[-17, 18], [17, 18], [-17, -18], [17, -18]]) { const w = cyl(4.5, 3, MAT.graphite2, 32); w.rotation.z = Math.PI / 2; w.position.set(x, 4.5, z); g.add(w); }
  const col = rbox(16, 56, 16, 3, MAT.graphite); col.position.set(0, 54, -8); g.add(col);
  const head = rbox(20, 6, 20, 2, MAT.white); head.position.set(0, 84, -8); g.add(head);
  const cam = rbox(10, 3, 3, 1, MAT.graphite2); cam.position.set(0, 80, 2.2); g.add(cam);
  const lens = cyl(0.9, 0.6, new THREE.MeshStandardMaterial({ color: 0x0b0d10, roughness: 0.2 }), 16); lens.rotation.x = Math.PI / 2; lens.position.set(-2.5, 80, 3.8); g.add(lens);
  const lens2 = lens.clone(); lens2.position.x = 2.5; g.add(lens2);
  g.userData.mountY = 87; g.userData.mountZ = -8;
  return g;
}
// task: fridge | pot
async function khome(W, H, p) {
  const task = p.get('task') || 'fridge';
  const { r, s } = stage(W, H, p, { keyPos: [-160, 320, 300], target: [0, 90, 0] });
  const K = buildHomeKitchen(s, p);
  const mb = buildMobileBase(); const bx = num(p, 'bx', 40), bz = num(p, 'bz', 66); mb.position.set(bx, 0, bz); mb.rotation.y = num(p, 'ry', 180) * D; s.add(mb); mb.updateMatrixWorld(true);
  const robot = buildCobot('A'); const rs = num(p, 'rscale', 0.95); robot.scale.setScalar(rs);
  const mw = mb.localToWorld(V(0, mb.userData.mountY, mb.userData.mountZ)); robot.position.copy(mw); robot.rotation.y = num(p, 'ary', 180) * D; s.add(robot); robot.updateMatrixWorld(true);
  let pose = KPOSES.hook, gw, gl, focus;
  const q0 = vec(p, 'q0', [60, -30, -70, -60, 90, 0]).map(v => v * D);
  if (task === 'fridge') {
    K.fridgeHandle.updateMatrixWorld(true);
    const hw = K.fridgeHandle.localToWorld(V(0, num(p, 'hy', 12), 3.2));
    gw = frameXZ(V(0, 1, 0), V(num(p, 'nx', 0.15), 0, -1), hw); gl = V(0, num(p, 'gy', 19.2), num(p, 'gz', 4.6)); focus = hw;
  } else {
    pose = KPOSES.hook;
    const pw = K.pot.localToWorld(V(11.4, 10.8, 0));
    gw = frameXZ(V(0, 0, 1), V(0, -1, 0.2), pw); gl = V(0, 19.2, 4.6); focus = pw;
  }
  const hand = buildHand(pose); hand.scale.setScalar(1 / rs); robot.userData.flange.add(hand);
  const res = placeHand(robot, gw, gl, q0);
  const off = vec(p, 'off', [-60, 30, 120]); const lookOff = vec(p, 'lookOff', [0, 0, 0]);
  const def = p.get('wide') === '1' ? [[-150, 165, 360], [5, 98, 10], 34] : [[focus.x + off[0], focus.y + off[1], focus.z + off[2]], [focus.x + lookOff[0], focus.y + lookOff[1], focus.z + lookOff[2]], 26];
  const cam = makeCam(W, H, p, def[0], def[1], def[2]);
  capture(r, s, cam, 'color');
  return { task, posErr: +res.posErr.toFixed(3), rotErr: +res.rotErr.toFixed(3), q: res.q.map(v => +(v / D).toFixed(1)), focus: focus.toArray().map(v => +v.toFixed(1)) };
}

// ---------------------------------------------------------------- human-tool lineup (product shot)
async function ktools(W, H, p) {
  initMaterials(); const M = kmat();
  const r = makeRenderer(W, H); r.toneMappingExposure = num(p, 'exp', 1.0);
  const s = makeScene(r, num(p, 'env', 1.0));
  addLights(s, { keyPos: [-60, 160, 90], key: 1.5, rim: 0.6, rimPos: [90, 80, -80], shadowSize: 70, target: [0, 0, 0], hemi: 0.5 });
  shadowCatcher(s, 0, 800, 0.22);
  const items = [];
  const put = (o, x, z, ry = 0, y = 0) => { o.position.set(x, y, z); o.rotation.y = ry; s.add(o); items.push(o); };
  const pan = buildPan(11, 18); put(pan, -42, -14, -0.35);
  const pot = buildPot(9.5, 11); put(pot, -6, -18, 0.4);
  const t = buildTongs(24, 0.05); t.rotation.set(0, 0, 0); const tg = new THREE.Group(); tg.add(t); t.position.y = 0.9; put(tg, 18, -26, -0.9);
  const lad = buildLadle(24); const lg = new THREE.Group(); lg.add(lad); lad.position.y = 3.3; lad.rotation.x = 0.0; put(lg, 36, -4, 2.3);
  const tu = buildTurner(26); const tug = new THREE.Group(); tug.add(tu); tu.position.y = 0.4; put(tug, -38, 22, 2.6);
  const kn = buildKnife(); put(kn, -10, 24, 0.15, 0);
  const gn = buildGN(17.6, 16.2, 8, null); put(gn, 10, 12, 0.1);
  const lid = buildGNLid(17.6, 16.2); lid.rotation.x = 0; put(lid, 34, 26, -0.3, 0);
  const knob = buildKnob(3.0, 3.0); put(knob, 52, 6, 0.4);
  const bh = buildBarHandle(16, M.steel); bh.rotation.set(-Math.PI / 2, 0, 0); const bg = new THREE.Group(); bg.add(bh); bh.position.set(0, 0, 0); put(bg, 54, -24, 0.7, 0);
  const plate = buildPlate(10); put(plate, -66, 14, 0);
  const cam = makeCam(W, H, p, [0, 150, 120], [-2, 0, 0], 34);
  capture(r, s, cam, 'color');
  return { ok: 1 };
}

// single human tool, transparent background, auto-framed (for a labeled grid)
async function ktool(W, H, p) {
  initMaterials(); const M = kmat();
  const r = makeRenderer(W, H); r.toneMappingExposure = num(p, 'exp', 1.0);
  const s = makeScene(r, num(p, 'env', 1.0));
  addLights(s, { keyPos: [-60, 160, 110], key: 1.45, rim: 0.65, rimPos: [90, 80, -80], shadowSize: 40, target: [0, 0, 0], hemi: 0.55 });
  shadowCatcher(s, 0, 400, 0.2);
  const item = p.get('item') || 'pan'; let o;
  const wrap = (child, y = 0) => { const g = new THREE.Group(); child.position.y = y; g.add(child); return g; };
  if (item === 'pan') o = buildPan(11, 18);
  else if (item === 'pot') o = buildPot(10, 12);
  else if (item === 'tongs') o = wrap(buildTongs(24, 0.05), 1.0);
  else if (item === 'ladle') { const l = buildLadle(24); o = wrap(l, 3.3); }
  else if (item === 'turner') o = wrap(buildTurner(26), 0.4);
  else if (item === 'knife') o = buildKnife();
  else if (item === 'gn') { o = buildGN(17.6, 16.2, 8, { mat: KM.tomato, r: 3.0, base: new THREE.MeshStandardMaterial({ color: 0xb23a25, roughness: 0.6 }), seed: 5 }, 5); }
  else if (item === 'lid') o = buildGNLid(17.6, 16.2);
  else if (item === 'knob') o = buildKnob(3.0, 3.0);
  else if (item === 'handle') { const h = buildBarHandle(16, M.steel); h.rotation.set(-Math.PI / 2, 0, 0); o = wrap(h, 0); }
  else if (item === 'plate') o = buildPlate(11);
  else if (item === 'bowl') o = buildBowl(8, 6);
  o.rotation.y = num(p, 'ry', 0) * D; s.add(o); o.updateMatrixWorld(true);
  const box = new THREE.Box3().setFromObject(o); const c = box.getCenter(new THREE.Vector3()); const sz = box.getSize(new THREE.Vector3());
  const rad = Math.max(sz.x, sz.y, sz.z) * 0.62;
  const dir = V(...vec(p, 'dir', [0.0, 0.95, 0.75])).normalize(); const fov = 24;
  const dist = rad / Math.sin(fov * D / 2) * num(p, 'pad', 1.0);
  const cam = new THREE.PerspectiveCamera(fov, W / H, 1, 4000); cam.position.copy(c.clone().add(dir.multiplyScalar(dist))); cam.lookAt(c);
  capture(r, s, cam, 'color');
  return { item, size: sz.toArray().map(v => +v.toFixed(1)) };
}

export const KSCENES = { kpro, khome, ktools, ktool };
