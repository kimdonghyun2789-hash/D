// MH Adaptive Kitchen Hand — concept model + grasp scenes (units: cm). CONCEPT only, not a validated design.
// Frame: origin = robot flange face, +Y toward fingertips. Side A (2 fingers) at -Z, side B (1 opposing finger) at +Z.
import * as THREE from 'three';
import { MAT, initMaterials, rbox, cyl, softCyl, makeRenderer, makeScene, addLights, shadowCatcher } from './lib.js';

const D = Math.PI / 180;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
let PAD = null, SEAM = null, GLAZE = null, STEEL = null, COUNTER = null;
function mats() {
  initMaterials();
  PAD = new THREE.MeshPhysicalMaterial({ color: 0x9fb0bf, roughness: 0.62, sheen: 0.5, sheenColor: new THREE.Color(0xdde6ee), clearcoat: 0.12 });
  SEAM = new THREE.MeshStandardMaterial({ color: 0x2a2e34, roughness: 0.5 });
  GLAZE = new THREE.MeshPhysicalMaterial({ color: 0xf3f1ec, roughness: 0.22, clearcoat: 0.7, clearcoatRoughness: 0.15, side: THREE.DoubleSide });
  STEEL = new THREE.MeshStandardMaterial({ color: 0xc9cdd3, metalness: 1.0, roughness: 0.22, side: THREE.DoubleSide });
  COUNTER = new THREE.MeshStandardMaterial({ color: 0xe6e3dd, roughness: 0.75 });
}

// ---------------------------------------------------------------- finger (local +Y along finger, inner face +Z)
function finger(opts = {}) {
  const root = new THREE.Group();
  const knuckle = cyl(0.78, 2.5, MAT.graphite, 32); knuckle.rotation.z = Math.PI / 2; root.add(knuckle);
  const mcp = new THREE.Group(); root.add(mcp);
  const prox = rbox(2.1, 4.4, 1.7, 0.62, MAT.white); prox.position.set(0, 2.45, -0.15); mcp.add(prox);
  const ppad = rbox(1.78, 3.1, 0.5, 0.22, PAD); ppad.position.set(0, 2.55, 0.86); mcp.add(ppad);
  const pip = new THREE.Group(); pip.position.y = 4.7; mcp.add(pip);
  const barrel = cyl(0.64, 2.3, MAT.graphite, 32); barrel.rotation.z = Math.PI / 2; pip.add(barrel);
  for (const s of [-1, 1]) { const cap = cyl(0.72, 0.14, MAT.graphite2, 32); cap.rotation.z = Math.PI / 2; cap.position.x = s * 1.2; pip.add(cap); }
  const dist = rbox(1.98, 3.7, 1.45, 0.55, MAT.white); dist.position.set(0, 1.95, -0.3); pip.add(dist);
  // replaceable food-contact module (distal pad + tip cap), seam line marks the swap boundary
  const mod = new THREE.Group(); pip.add(mod);
  const dpad = rbox(2.12, 3.25, 0.74, 0.3, PAD); dpad.position.set(0, 2.15, 0.78); mod.add(dpad);
  const cap = rbox(2.2, 0.95, 2.05, 0.42, PAD); cap.position.set(0, 3.95, 0.12); mod.add(cap);
  const seam = rbox(2.16, 0.12, 0.8, 0.04, SEAM); seam.position.set(0, 0.5, 0.8); mod.add(seam);
  if (opts.lip) { const lip = rbox(1.9, 0.75, 0.28, 0.12, PAD); lip.position.set(0, 4.55, 0.95); lip.rotation.x = -14 * D; mod.add(lip); }
  const tip = new THREE.Object3D(); tip.position.set(0, 3.2, 1.2); pip.add(tip);           // pad contact point
  const end = new THREE.Object3D(); end.position.set(0, 4.4, 0.2); pip.add(end);           // fingertip end
  return { root, mcp, pip, tip, end, mod };
}

// pose: { a: [mcp, pip] side-A fingers, b: [mcp, pip] side-B finger, splay: deg, suction: 0..1 }
export function buildMHHand(pose = {}) {
  const P = Object.assign({ a: [8, 10], b: [8, 10], splay: 6, suction: 0 }, pose);
  const hand = new THREE.Group(); hand.name = 'MHHand';
  const fl = softCyl(3.15, 0.6, 0.1, MAT.graphite); fl.position.y = 0.3; hand.add(fl);
  const qc = softCyl(3.55, 1.5, 0.22, MAT.graphite2); qc.position.y = 1.35; hand.add(qc);
  const latch = rbox(1.3, 0.9, 0.9, 0.25, MAT.graphite); latch.position.set(0, 1.35, 3.55); hand.add(latch);
  const ft = softCyl(3.32, 1.25, 0.12, MAT.metal); ft.position.y = 2.75; hand.add(ft);
  const ftg = softCyl(3.38, 0.18, 0.05, MAT.graphite); ftg.position.y = 2.75; hand.add(ftg);
  const wr = softCyl(3.3, 2.9, 0.35, MAT.white); wr.position.y = 4.85; hand.add(wr);
  const palm = rbox(8.4, 3.7, 7.0, 1.05, MAT.white); palm.position.y = 7.95; hand.add(palm);
  const face = rbox(7.3, 0.36, 5.9, 0.16, MAT.graphite); face.position.y = 9.85; hand.add(face);
  // wrist camera (looks along the fingers) on side B
  const camb = rbox(2.7, 1.7, 1.3, 0.35, MAT.graphite2); camb.position.set(-2.4, 8.7, 3.95); hand.add(camb);
  const lens = cyl(0.42, 0.5, new THREE.MeshStandardMaterial({ color: 0x07090b, roughness: 0.15 }), 24); lens.position.set(-2.4, 9.75, 4.05); hand.add(lens);
  const led = cyl(0.16, 0.3, MAT.green, 12); led.position.set(-1.45, 9.65, 4.15); hand.add(led);
  // palm suction (retractable, food-contact seal)
  const bell = cyl(0.95, 0.5 + 0.9 * P.suction, PAD, 32); bell.position.y = 10.1 + (0.5 + 0.9 * P.suction) / 2; hand.add(bell);
  const lipS = cyl(1.25, 0.22, PAD, 32, 1.0); lipS.position.y = 10.1 + 0.5 + 0.9 * P.suction + 0.08; hand.add(lipS);
  // fingers
  const top = 10.05;
  const A = [], fingers = [];
  for (const [i, x] of [[0, -2.15], [1, 2.15]]) {
    const base = new THREE.Group(); base.position.set(x, top, -2.45); base.rotation.z = (i ? -1 : 1) * P.splay * D; hand.add(base);
    const f = finger(); base.add(f.root); f.mcp.rotation.x = P.a[0] * D; f.pip.rotation.x = P.a[1] * D; A.push(f); fingers.push(f);
  }
  const bBase = new THREE.Group(); bBase.position.set(0, top, 2.45); bBase.rotation.y = Math.PI; hand.add(bBase);
  const B = finger({ lip: true }); bBase.add(B.root); B.mcp.rotation.x = P.b[0] * D; B.pip.rotation.x = P.b[1] * D; fingers.push(B);
  hand.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } });
  hand.userData = { A, B, fingers, anchors: {
    qc: V(0, 1.35, 3.6), ft: V(3.3, 2.75, 0), cam: V(-2.4, 9.8, 4.1), suction: V(0, 11.0, 0),
    palm: V(4.2, 7.9, 0) } };
  return hand;
}
function world(o) { o.updateWorldMatrix(true, false); return new THREE.Vector3().setFromMatrixPosition(o.matrixWorld); }
function handAnchors(hand) {
  hand.updateMatrixWorld(true);
  const out = {};
  for (const [k, v] of Object.entries(hand.userData.anchors)) out[k] = v.clone().applyMatrix4(hand.matrixWorld);
  const { A, B } = hand.userData;
  out.fingerA = world(A[1].mcp).lerp(world(A[1].pip), 0.5);
  out.fingerB = world(B.pip);
  out.pad = world(B.tip);
  out.padA = world(A[0].tip);
  return out;
}

// ---------------------------------------------------------------- kitchen objects (lathe profiles, cm)
function lathe(pts, mat, seg = 96) {
  const m = new THREE.Mesh(new THREE.LatheGeometry(pts.map(([r, y]) => new THREE.Vector2(r, y)), seg), mat);
  m.castShadow = true; m.receiveShadow = true; return m;
}
export function plate() {   // 26cm dinner plate, axis +Y, foot on y=0
  return lathe([[0, 0.45], [5.6, 0.45], [5.9, 0], [6.3, 0], [6.5, 0.5], [10.9, 1.15], [12.4, 1.85], [12.95, 2.1], [13.05, 2.32],
                [12.85, 2.42], [12.2, 2.15], [10.7, 1.5], [6.4, 0.98], [0, 0.98]], GLAZE);
}
export function mug() {     // 8.4cm mug with handle, foot on y=0
  const g = new THREE.Group();
  g.add(lathe([[0, 0.2], [3.6, 0.0], [4.05, 0.3], [4.2, 1.2], [4.2, 9.1], [4.3, 9.5], [3.85, 9.55], [3.8, 9.0], [3.8, 0.9], [0, 0.75]], GLAZE));
  const h = new THREE.Mesh(new THREE.TorusGeometry(2.4, 0.55, 20, 48, Math.PI * 1.15), GLAZE);
  h.rotation.z = -Math.PI / 2 - Math.PI * 0.075; h.position.set(4.1, 5.0, 0); h.castShadow = true; g.add(h);
  return g;
}
export function bowl() {    // Korean soup bowl (국그릇) D 14.6cm, H 6.6cm
  return lathe([[0, 0.35], [3.2, 0.35], [3.35, 0], [3.8, 0], [3.95, 0.6], [5.6, 2.2], [6.9, 4.6], [7.35, 6.4], [7.3, 6.65],
                [6.95, 6.5], [6.55, 4.6], [5.2, 2.5], [3.6, 1.0], [0, 0.9]], GLAZE);
}
export function ladle() {   // stainless ladle (국자): bowl R 4.2 at origin, handle along +X
  const g = new THREE.Group();
  const bw = new THREE.Mesh(new THREE.SphereGeometry(4.2, 48, 24, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), STEEL);
  bw.castShadow = true; g.add(bw);
  const rim = new THREE.Mesh(new THREE.TorusGeometry(4.2, 0.12, 12, 64), STEEL); rim.rotation.x = Math.PI / 2; g.add(rim);
  const pts = [V(3.9, 0.2, 0), V(9, 4.5, 0), V(18, 6.5, 0), V(30, 7.2, 0)];
  const tube = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 64, 0.62, 20, false), STEEL); tube.castShadow = true; g.add(tube);
  const endc = new THREE.Mesh(new THREE.SphereGeometry(0.62, 20, 12), STEEL); endc.position.copy(pts[3]); g.add(endc);
  g.userData.grip = V(19.5, 6.7, 0);    // handle grip point
  return g;
}

// ---------------------------------------------------------------- scene helpers
function cam(W, H, fov, pos, look) {
  const c = new THREE.PerspectiveCamera(fov, W / H, 1, 2000); c.position.copy(pos); c.lookAt(look); c.updateMatrixWorld(); return c;
}
function project(c, W, H, pts) {
  const out = {};
  for (const [k, p] of Object.entries(pts)) { const v = p.clone().project(c); out[k] = [Math.round((v.x + 1) / 2 * W), Math.round((1 - v.y) / 2 * H)]; }
  return out;
}
function setup(W, H, opts = {}) {
  mats();
  const renderer = makeRenderer(W, H); const scene = makeScene(renderer, opts.env ?? 0.55);
  const L = addLights(scene, { key: 1.9, keyPos: opts.keyPos ?? [40, 90, 70], rim: 0.5, rimPos: [-60, 50, -70], hemi: 0.4, shadowSize: 40, target: opts.target ?? [0, 0, 0] });
  L.key.shadow.radius = 5; L.key.shadow.bias = -0.0005;
  return { renderer, scene };
}
// orient the hand: tool axis (+Y local) along `dir`, local +Z (side B) roughly along `side`
function orient(hand, dir, side, flangePos) {
  const y = dir.clone().normalize(); let z = side.clone().sub(y.clone().multiplyScalar(side.dot(y))).normalize();
  const x = new THREE.Vector3().crossVectors(y, z).normalize(); z = new THREE.Vector3().crossVectors(x, y).normalize();
  const m = new THREE.Matrix4().makeBasis(x, y, z); m.setPosition(flangePos);
  hand.matrixAutoUpdate = false; hand.matrix.copy(m); hand.updateMatrixWorld(true);
}

export const HAND_SCENES = {
  // Hero close-up (hand alone). p: view = hero | side
  async handHero(W, H, p) {
    const { renderer, scene } = setup(W, H, { keyPos: [60, 80, 90] });
    const hand = buildMHHand({ a: [6, 12], b: [6, 12], splay: 7, suction: 0.15 });
    scene.add(hand);
    orient(hand, V(0.05, 1, 0.0), V(0.6, 0, 1), V(0, 0, 0));
    const c = cam(W, H, +(p.get('fov') || 24), V(...(p.get('cam') || '30,26,34').split(',').map(Number)), V(...(p.get('look') || '0,9.5,0').split(',').map(Number)));
    renderer.render(scene, c);
    return { anchors: project(c, W, H, handAnchors(hand)) };
  },
  // Grasp panels. p: obj = plate | cup | bowl | tool. Finger angles are fitted so pad contacts meet the object surface.
  async handGrasp(W, H, p) {
    const obj = p.get('obj') || 'plate';
    const { renderer, scene } = setup(W, H, { keyPos: [50, 110, 80] });
    const down = V(0, -1, 0);
    // build a hand, fit MCP so the pad contact sits at local |z| = half (pip = k * mcp + pip0)
    const fit = (half, opts) => {
      const mk = (m) => buildMHHand({ a: [m, opts.k * m + opts.pip0], b: [m, opts.k * m + opts.pip0], splay: opts.splay ?? 3 });
      let lo = opts.lo ?? -60, hi = opts.hi ?? 60, h = null;
      for (let it = 0; it < 40; it++) {
        const mid = (lo + hi) / 2; h = mk(mid); h.updateMatrixWorld(true);
        const z = world(h.userData.B.tip).z;          // side B contact (local frame = world frame here)
        if (z > half) lo = mid; else hi = mid;          // more curl -> smaller z
      }
      return mk((lo + hi) / 2);
    };
    let hand, o, c, look;
    if (obj === 'plate') {
      // vertical plate (as in the dishwasher rack), rim pinch from above; opposing finger has the edge lip
      hand = fit(0.42, { k: -0.45, pip0: 2, splay: 3, lo: -10, hi: 40 });
      scene.add(hand); orient(hand, down, V(0, 0, 1), V(0, 0, 0));
      const t = handAnchors(hand); const pc = t.pad.clone().add(t.padA).multiplyScalar(0.5);
      o = plate(); o.rotation.x = Math.PI / 2;            // axis +Z, rim circle in XY, rim mid-thickness z ~ 0.0 after shift
      o.position.set(pc.x, pc.y - 13.05 + 1.6, pc.z - 2.26); scene.add(o);
      look = V(pc.x - 2.5, pc.y + 0.5, pc.z);
      c = cam(W, H, 30, look.clone().add(V(40, 18, 36)), look);
    } else if (obj === 'cup') {
      // pinch the mug body from above (fingers open around it, distal pads vertical)
      hand = fit(4.22, { k: -1.0, pip0: 0, splay: 2, lo: -70, hi: 10 });
      scene.add(hand); orient(hand, down, V(0, 0, 1), V(0, 0, 0));
      const t = handAnchors(hand); const pc = t.pad.clone().add(t.padA).multiplyScalar(0.5);
      o = mug(); o.rotation.y = -Math.PI * 0.5; o.position.set(pc.x, pc.y - 6.4, pc.z); scene.add(o);
      shadowCatcher(scene, o.position.y, 200, 0.22);
      look = V(pc.x, pc.y + 4.5, pc.z);
      c = cam(W, H, 30, look.clone().add(V(34, 19, 30)), look);
    } else if (obj === 'bowl') {
      // rim pinch: opposing finger inside the rim, side A outside; hand tilted outward
      hand = fit(0.3, { k: 0.4, pip0: 0, splay: 4, lo: -10, hi: 40 });
      scene.add(hand);
      const dir = V(0.3, -1, 0).normalize();
      orient(hand, dir, V(-1, -0.3, 0).normalize(), V(0, 0, 0));
      const t = handAnchors(hand); const pc = t.pad.clone().add(t.padA).multiplyScalar(0.5);
      o = bowl(); o.position.set(pc.x - 6.95, pc.y - 5.6, pc.z); scene.add(o);
      shadowCatcher(scene, o.position.y, 200, 0.14);
      look = V(pc.x - 5, pc.y + 4, pc.z);
      c = cam(W, H, 30, look.clone().add(V(-12, 38, 34)), look);
    } else {
      // power grasp on the ladle handle (fingers wrap under the handle)
      hand = buildMHHand({ a: [28, 70], b: [30, 70], splay: 2 });
      scene.add(hand); orient(hand, down, V(0, 0, 1), V(0, 0, 0));
      const t = handAnchors(hand);
      const pc = t.pad.clone().add(t.padA).multiplyScalar(0.5).add(V(0, 1.05, 0));
      o = ladle(); const gp = o.userData.grip; o.position.set(pc.x - gp.x, pc.y - gp.y, pc.z - gp.z); scene.add(o);
      look = V(pc.x - 4.5, pc.y + 6.5, pc.z);
      c = cam(W, H, 30, look.clone().add(V(26, 17, 34)), look);
    }
    renderer.render(scene, c);
    const t = handAnchors(hand);
    return { obj, anchors: project(c, W, H, { contact: t.pad, ...t }) };
  },
};
