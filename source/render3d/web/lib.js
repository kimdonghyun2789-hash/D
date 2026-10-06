// SoftHand-4 concept model + props (units: cm). One canonical design used by every render.
import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

export const MAT = {};
export function initMaterials() {
  MAT.white = new THREE.MeshPhysicalMaterial({ color: 0xedede9, roughness: 0.42, clearcoat: 0.25, clearcoatRoughness: 0.4 });
  MAT.whiteMatte = new THREE.MeshStandardMaterial({ color: 0xe9e9e5, roughness: 0.6 });
  MAT.graphite = new THREE.MeshPhysicalMaterial({ color: 0x24272d, roughness: 0.36, metalness: 0.12, clearcoat: 0.35, clearcoatRoughness: 0.3 });
  MAT.graphite2 = new THREE.MeshPhysicalMaterial({ color: 0x2d3138, roughness: 0.45, metalness: 0.1, clearcoat: 0.2 });
  MAT.orange = new THREE.MeshStandardMaterial({ color: 0xd4521b, roughness: 0.7 });
  MAT.metal = new THREE.MeshStandardMaterial({ color: 0xc5c9cf, metalness: 1.0, roughness: 0.26 });
  MAT.metalDark = new THREE.MeshStandardMaterial({ color: 0x8d939b, metalness: 1.0, roughness: 0.32 });
  MAT.alu = new THREE.MeshStandardMaterial({ color: 0xd7dade, metalness: 0.9, roughness: 0.3 });
  MAT.machine = new THREE.MeshPhysicalMaterial({ color: 0xd9dbde, roughness: 0.5, clearcoat: 0.15 });
  MAT.machineDark = new THREE.MeshPhysicalMaterial({ color: 0x2f333a, roughness: 0.45, clearcoat: 0.2 });
  MAT.glass = new THREE.MeshPhysicalMaterial({ color: 0x2a3440, roughness: 0.06, metalness: 0.0, transparent: true, opacity: 0.32, clearcoat: 1.0 });
  MAT.screen = new THREE.MeshStandardMaterial({ color: 0x0f1a24, roughness: 0.2, emissive: 0x16324a, emissiveIntensity: 0.6 });
  MAT.green = new THREE.MeshStandardMaterial({ color: 0x2bb673, roughness: 0.35, emissive: 0x0d5a35, emissiveIntensity: 0.4 });
  MAT.red = new THREE.MeshStandardMaterial({ color: 0xd83a34, roughness: 0.35 });
  MAT.yellow = new THREE.MeshStandardMaterial({ color: 0xe9b949, roughness: 0.4 });
  MAT.tray = new THREE.MeshStandardMaterial({ color: 0x4a4f57, roughness: 0.55 });
  MAT.table = new THREE.MeshStandardMaterial({ color: 0x30343b, roughness: 0.5 });
  MAT.ghost = new THREE.MeshPhysicalMaterial({ color: 0xffffff, roughness: 0.15, transparent: true, opacity: 0.18, clearcoat: 1.0, depthWrite: false });
  MAT.motor = new THREE.MeshStandardMaterial({ color: 0x6b7079, metalness: 0.6, roughness: 0.35 });
  MAT.pcb = new THREE.MeshStandardMaterial({ color: 0x1f4d3a, roughness: 0.5 });
  MAT.tendon = new THREE.MeshStandardMaterial({ color: 0xb0b5bd, metalness: 0.7, roughness: 0.3 });
  MAT.bone = new THREE.MeshStandardMaterial({ color: 0x9aa0a8, metalness: 0.75, roughness: 0.32 });
  MAT.food1 = new THREE.MeshStandardMaterial({ color: 0x8cc152, roughness: 0.7 });
  MAT.food2 = new THREE.MeshStandardMaterial({ color: 0xe8a33c, roughness: 0.7 });
  MAT.plate = new THREE.MeshPhysicalMaterial({ color: 0xf4f4f1, roughness: 0.25, clearcoat: 0.6 });
  return MAT;
}

export function rbox(w, h, d, r, mat, seg = 5) {
  const rr = Math.min(r, w / 2 - 1e-3, h / 2 - 1e-3, d / 2 - 1e-3);
  const m = new THREE.Mesh(new RoundedBoxGeometry(w, h, d, seg, rr), mat);
  m.castShadow = true; m.receiveShadow = true;
  return m;
}
export function cyl(r, h, mat, seg = 48, rTop = null) {
  const m = new THREE.Mesh(new THREE.CylinderGeometry(rTop ?? r, r, h, seg), mat);
  m.castShadow = true; m.receiveShadow = true;
  return m;
}
// cylinder with softly rounded edges (lathe profile), axis = Y, centered
export function softCyl(r, h, bevel, mat, seg = 64) {
  const pts = [];
  const b = Math.min(bevel, r * 0.5, h * 0.5);
  pts.push(new THREE.Vector2(0, -h / 2));
  const n = 6;
  for (let i = 0; i <= n; i++) { const a = -Math.PI / 2 + (i / n) * Math.PI / 2; pts.push(new THREE.Vector2(r - b + b * Math.cos(a), -h / 2 + b + b * Math.sin(a))); }
  for (let i = 0; i <= n; i++) { const a = (i / n) * Math.PI / 2; pts.push(new THREE.Vector2(r - b + b * Math.cos(a), h / 2 - b + b * Math.sin(a))); }
  pts.push(new THREE.Vector2(0, h / 2));
  const m = new THREE.Mesh(new THREE.LatheGeometry(pts, seg), mat);
  m.castShadow = true; m.receiveShadow = true;
  return m;
}
const X = new THREE.Vector3(1, 0, 0), Y = new THREE.Vector3(0, 1, 0), Z = new THREE.Vector3(0, 0, 1);
const D = Math.PI / 180;

// ---------------------------------------------------------------- SoftHand-4
// Frame: origin = robot flange face, +Y toward fingertips, +Z palm normal (palmar), +X thumb side.
export const HAND_DEFAULT_POSE = {
  fingers: [ { spread: -5, mcp: 8, pip: 10, dip: 8 }, { spread: 0, mcp: 8, pip: 10, dip: 8 }, { spread: 5, mcp: 8, pip: 10, dip: 8 } ],
  thumb: { swing: 30, roll: 35, cmc: 10, mcp: 10, ip: 8 },
};

function fingerSegment(L, isDistal, opts) {
  const g = new THREE.Group();
  // joint barrel + side brackets
  const barrel = cyl(0.62, 2.45, MAT.graphite, 32); barrel.rotation.z = Math.PI / 2; g.add(barrel);
  for (const s of [-1, 1]) { const cap = cyl(0.72, 0.16, MAT.graphite2, 32); cap.rotation.z = Math.PI / 2; cap.position.x = s * 1.3; g.add(cap); }
  const brL = rbox(0.18, 1.5, 1.25, 0.08, MAT.graphite); brL.position.set(-1.16, 0.55, 0); g.add(brL);
  const brR = brL.clone(); brR.position.x = 1.16; g.add(brR);
  if (!opts.cutaway) {
    const bodyH = isDistal ? L - 1.55 : L - 0.95;
    const body = rbox(2.08, bodyH, 1.92, 0.72, MAT.white); body.position.set(0, 0.62 + bodyH / 2, -0.04); g.add(body);
    if (!isDistal) {
      const pad = rbox(1.82, L - 1.75, 0.62, 0.28, MAT.orange); pad.position.set(0, 0.62 + (L - 1.75) / 2 + 0.22, 0.98); g.add(pad);
    } else {
      const pad = rbox(1.82, L - 2.05, 0.6, 0.27, MAT.orange); pad.position.set(0, 0.62 + (L - 2.05) / 2 + 0.15, 0.98); g.add(pad);
      const tip = rbox(2.2, 1.55, 2.12, 0.68, MAT.orange); tip.position.set(0, L - 0.72, 0.03); g.add(tip);
    }
  } else {
    // cutaway: ghost shell + inner bone + tendon
    const bodyH = isDistal ? L - 1.55 : L - 0.95;
    const body = rbox(2.08, bodyH, 1.92, 0.72, MAT.ghost); body.position.set(0, 0.62 + bodyH / 2, -0.04); body.castShadow = false; g.add(body);
    const bone = rbox(0.75, L - 0.7, 0.7, 0.3, MAT.bone); bone.position.set(0, (L - 0.7) / 2 + 0.35, -0.25); g.add(bone);
    const tendon = cyl(0.09, L, MAT.tendon, 12); tendon.position.set(0, L / 2, 0.45); g.add(tendon);
    if (!isDistal) { const pad = rbox(1.82, L - 1.75, 0.62, 0.28, MAT.orange); pad.position.set(0, 0.62 + (L - 1.75) / 2 + 0.22, 0.98); g.add(pad); }
    else { const pad = rbox(1.82, L - 2.05, 0.6, 0.27, MAT.orange); pad.position.set(0, 0.62 + (L - 2.05) / 2 + 0.15, 0.98); g.add(pad);
      const tip = rbox(2.2, 1.55, 2.12, 0.68, MAT.orange); tip.position.set(0, L - 0.72, 0.03); g.add(tip); }
  }
  return g;
}

function buildFinger(lengths, opts) {
  // returns root group and joint groups [mcp, pip, dip]
  const joints = [];
  const root = new THREE.Group();
  let parent = root;
  lengths.forEach((L, i) => {
    const j = new THREE.Group(); parent.add(j); joints.push(j);
    const seg = fingerSegment(L, i === lengths.length - 1, opts); j.add(seg);
    const next = new THREE.Group(); next.position.y = L; j.add(next); parent = next;
  });
  const tip = new THREE.Object3D(); tip.position.set(0, 0.0, 0.25); parent.add(tip);
  return { root, joints, tip };
}

export function buildHand(pose = HAND_DEFAULT_POSE, opts = {}) {
  const hand = new THREE.Group(); hand.name = 'SoftHand4';
  const cut = !!opts.cutaway;
  // ---- wrist module
  const flange = softCyl(3.15, 0.9, 0.12, MAT.graphite); flange.position.y = 0.45; hand.add(flange);
  const ring1 = softCyl(3.58, 0.38, 0.1, MAT.graphite2); ring1.position.y = 1.08; hand.add(ring1);
  const body = softCyl(3.5, 5.3, 0.25, cut ? MAT.ghost : MAT.white); body.position.y = 3.92; hand.add(body);
  if (cut) {
    body.castShadow = false;
    // actuator pack inside wrist
    const plate = cyl(3.0, 0.25, MAT.graphite2); plate.position.y = 1.55; hand.add(plate);
    const motors = [[-1.35, -0.6], [1.35, -0.6], [0, 1.25], [-0.2, -1.9]];
    motors.forEach(([x, z], i) => { const mm = cyl(i === 3 ? 0.62 : 0.95, i === 3 ? 3.2 : 3.8, MAT.motor, 32); mm.position.set(x, 3.6, z); hand.add(mm);
      const cap = cyl(i === 3 ? 0.64 : 0.97, 0.3, MAT.graphite, 32); cap.position.set(x, 5.6, z); hand.add(cap); });
    const pcb = rbox(3.6, 0.16, 2.2, 0.05, MAT.pcb); pcb.position.set(0, 6.0, 0.3); hand.add(pcb);
  }
  const ring2 = softCyl(3.58, 0.38, 0.1, MAT.graphite2); ring2.position.y = 6.75; hand.add(ring2);
  const neck = softCyl(3.05, 0.95, 0.15, MAT.graphite); neck.position.y = 7.4; hand.add(neck);
  if (!cut) {
    // connector (single cable exit, internal routing)
    const conn = rbox(1.55, 1.25, 0.8, 0.22, MAT.graphite); conn.position.set(0, 3.5, 3.55); hand.add(conn);
    const port = cyl(0.36, 0.3, MAT.graphite2, 24); port.rotation.x = Math.PI / 2; port.position.set(0, 3.5, 3.98); hand.add(port);
    const portIn = cyl(0.2, 0.32, new THREE.MeshStandardMaterial({ color: 0x0a0b0d, roughness: 0.6 }), 16); portIn.rotation.x = Math.PI / 2; portIn.position.set(0, 3.5, 4.0); hand.add(portIn);
  }
  // ---- palm
  const palm = new THREE.Group(); palm.position.y = 7.85; hand.add(palm);
  const core = rbox(8.8, 9.6, 3.4, 0.45, MAT.graphite); core.position.set(0, 4.8, 0.25); palm.add(core);
  const shell = rbox(9.25, 10.0, 2.5, 1.05, cut ? MAT.ghost : MAT.white); shell.position.set(0, 4.95, -1.35); palm.add(shell);
  if (cut) {
    shell.castShadow = false;
    const frame = rbox(7.4, 8.6, 0.6, 0.25, MAT.bone); frame.position.set(0, 4.9, -0.9); palm.add(frame);
    for (const x of [-2.75, 0, 2.75]) { const t = cyl(0.09, 8.2, MAT.tendon, 12); t.position.set(x, 4.9, 0.95); palm.add(t); }
  }
  const pad = rbox(5.5, 4.7, 0.72, 0.36, MAT.orange); pad.position.set(-0.85, 3.25, 2.05); palm.add(pad);
  const band = rbox(7.9, 1.25, 0.22, 0.12, MAT.graphite2); band.position.set(0, 7.85, 1.97); palm.add(band);
  for (const [x, y] of [[-3.95, 0.55], [3.95, 0.55], [-3.95, 9.05], [3.95, 9.05]]) { const s = cyl(0.19, 0.16, MAT.graphite2, 16); s.rotation.x = Math.PI / 2; s.position.set(x, y, 1.98); palm.add(s); }
  // side pad (radial) for wrap grasps
  const spad = rbox(0.55, 2.6, 1.6, 0.22, MAT.orange); spad.position.set(4.5, 6.4, 0.9); palm.add(spad);
  const knuckle = cyl(0.62, 8.3, MAT.graphite, 32); knuckle.rotation.z = Math.PI / 2; knuckle.position.set(0, 9.75, 0.35); palm.add(knuckle);
  // ---- fingers
  const fingerX = [-2.75, 0, 2.75];
  const fingerLens = [[4.0, 3.0, 2.6], [4.3, 3.2, 2.7], [4.1, 3.05, 2.65]];
  const fingers = [];
  fingerX.forEach((fx, i) => {
    const base = new THREE.Group(); base.position.set(fx, 10.15, 0.35); palm.add(base);
    const p = pose.fingers[i];
    base.rotation.z = -(p.spread || 0) * D;
    const f = buildFinger(fingerLens[i], opts); base.add(f.root);
    f.joints[0].rotation.x = p.mcp * D; f.joints[1].rotation.x = p.pip * D; f.joints[2].rotation.x = p.dip * D;
    fingers.push({ base, ...f });
  });
  // ---- thumb (opposable)
  const tp = pose.thumb;
  const tBase = new THREE.Group(); tBase.position.set(4.55, 2.6, 0.9); palm.add(tBase);
  const cmcDisc = cyl(1.12, 1.35, MAT.graphite, 40); cmcDisc.rotation.x = Math.PI / 2; tBase.add(cmcDisc);
  const cmcCap = cyl(0.62, 1.45, MAT.graphite2, 32); cmcCap.rotation.x = Math.PI / 2; tBase.add(cmcCap);
  const tSwing = new THREE.Group(); tBase.add(tSwing); tSwing.rotation.z = -(tp.swing) * D; // swing away from palm side (toward +X)
  const tRoll = new THREE.Group(); tSwing.add(tRoll); tRoll.rotation.y = -(tp.roll) * D; // opposition roll
  const tCmc = new THREE.Group(); tRoll.add(tCmc); tCmc.rotation.x = tp.cmc * D;
  const th = buildFinger([3.3, 3.0, 2.55], opts); th.root.position.y = 0.9; tCmc.add(th.root);
  th.joints[0].rotation.x = 0; th.joints[1].rotation.x = tp.mcp * D; th.joints[2].rotation.x = tp.ip * D;
  hand.userData = { palm, fingers, thumb: { base: tBase, swing: tSwing, roll: tRoll, cmc: tCmc, ...th } };
  hand.traverse(o => { if (o.isMesh) { o.castShadow = o.castShadow !== false && o.material !== MAT.ghost; } });
  return hand;
}

// ---------------------------------------------------------------- 6R cobot (two styles)
// Joint axes (local): J1 Y, J2 X, J3 X, J4 X, J5 Z->(we use Y), J6 tool axis.
export function buildCobot(style = 'A') {
  const S = style === 'A'
    ? { link: MAT.white, joint: MAT.white, cap: MAT.graphite, ring: MAT.graphite2, r: 1.0 }
    : { link: MAT.graphite2, joint: MAT.graphite, cap: MAT.metalDark, ring: MAT.white, r: 1.0 };
  const robot = new THREE.Group(); robot.name = 'cobot' + style;
  const J = [];
  // base
  const base = style === 'A' ? softCyl(8.0, 3.0, 0.6, MAT.graphite) : rbox(17, 3.0, 17, 1.2, MAT.graphite);
  base.position.y = 1.5; robot.add(base);
  const baseBody = style === 'A' ? softCyl(6.6, 9.0, 0.8, S.link) : softCyl(6.8, 9.0, 0.6, S.joint);
  baseBody.position.y = 7.5; robot.add(baseBody);
  const j1 = new THREE.Group(); j1.position.y = 12.0; robot.add(j1); J.push(j1);
  const ringA = softCyl(6.75, 0.5, 0.15, S.ring); ringA.position.y = -0.1; j1.add(ringA);
  const shoulderBody = softCyl(6.5, 8.5, 0.8, S.joint); shoulderBody.position.y = 4.2; j1.add(shoulderBody);
  // shoulder joint housing (horizontal, axis X), offset sideways
  const j2 = new THREE.Group(); j2.position.set(0, 8.6, 0); j1.add(j2); J.push(j2);
  const sh = softCyl(6.6, 13.5, 1.2, S.joint); sh.rotation.z = Math.PI / 2; sh.position.x = 2.0; j2.add(sh);
  const shCap = softCyl(5.4, 0.9, 0.3, S.cap); shCap.rotation.z = Math.PI / 2; shCap.position.x = 9.0; j2.add(shCap);
  const shRing = softCyl(6.7, 0.45, 0.12, S.ring); shRing.rotation.z = Math.PI / 2; shRing.position.x = -4.6; j2.add(shRing);
  // upper arm (along +Y), offset in x
  const UA = style === 'A' ? 42.5 : 36.0, FA = style === 'A' ? 39.2 : 46.0;
  const ua = style === 'A' ? softCyl(4.6, UA - 8.5, 1.0, S.link) : rbox(8.4, UA - 8.5, 8.4, 2.2, S.link);
  ua.position.set(5.6, UA / 2 + 0.25, 0); j2.add(ua);
  const elbowOff = new THREE.Group(); elbowOff.position.set(0, UA, 0); j2.add(elbowOff);
  const j3 = new THREE.Group(); elbowOff.add(j3); J.push(j3);
  const el = softCyl(5.4, 12.0, 1.0, S.joint); el.rotation.z = Math.PI / 2; el.position.x = 3.6; j3.add(el);
  const elCap = softCyl(4.4, 0.8, 0.25, S.cap); elCap.rotation.z = Math.PI / 2; elCap.position.x = 9.9; j3.add(elCap);
  const elRing = softCyl(5.5, 0.4, 0.1, S.ring); elRing.rotation.z = Math.PI / 2; elRing.position.x = -2.5; j3.add(elRing);
  const fa = style === 'A' ? softCyl(3.8, FA - 8.2, 0.9, S.link) : rbox(7.0, FA - 8.2, 7.0, 1.8, S.link);
  fa.position.set(0.5, FA / 2 + 0.9, 0); j3.add(fa);
  const wrist1Off = new THREE.Group(); wrist1Off.position.set(0, FA, 0); j3.add(wrist1Off);
  const j4 = new THREE.Group(); wrist1Off.add(j4); J.push(j4);
  const w1 = softCyl(4.4, 10.0, 0.8, S.joint); w1.rotation.z = Math.PI / 2; w1.position.x = 0.5; j4.add(w1);
  const w1Cap = softCyl(3.6, 0.7, 0.2, S.cap); w1Cap.rotation.z = Math.PI / 2; w1Cap.position.x = 5.8; j4.add(w1Cap);
  const w1Ring = softCyl(4.5, 0.35, 0.1, S.ring); w1Ring.rotation.z = Math.PI / 2; w1Ring.position.x = -3.2; j4.add(w1Ring);
  // wrist 2 housing along Y
  const w2Off = new THREE.Group(); w2Off.position.set(-0.5, 0, 0); j4.add(w2Off);
  const w2body = softCyl(4.3, 9.0, 0.8, S.joint); w2body.position.y = 4.8; w2Off.add(w2body);
  const j5 = new THREE.Group(); j5.position.y = 9.6; w2Off.add(j5); J.push(j5);
  const w2Ring = softCyl(4.4, 0.35, 0.1, S.ring); w2Ring.position.y = -0.3; j5.add(w2Ring);
  // wrist 3 housing (axis Z -> rotate) : tool axis along +Z of j5 frame, we map tool axis to +Y of j6
  const w3 = softCyl(4.3, 9.0, 0.8, S.joint); w3.rotation.x = Math.PI / 2; w3.position.set(0, 4.3, 0.5); j5.add(w3);
  const w3Cap = softCyl(3.5, 0.6, 0.2, S.cap); w3Cap.rotation.x = Math.PI / 2; w3Cap.position.set(0, 4.3, -4.2); j5.add(w3Cap);
  const j6 = new THREE.Group(); j6.position.set(0, 4.3, 5.0); j6.rotation.x = Math.PI / 2; j5.add(j6); J.push(j6);
  // j6 local +Y is tool axis
  const toolRing = softCyl(4.35, 0.4, 0.1, S.ring); toolRing.position.y = -0.1; j6.add(toolRing);
  const toolFl = softCyl(3.3, 1.0, 0.2, MAT.graphite); toolFl.position.y = 0.5; j6.add(toolFl);
  const flange = new THREE.Group(); flange.position.y = 1.0; j6.add(flange);
  robot.userData = { J, flange, axes: ['y', 'x', 'x', 'x', 'y', 'y'] };
  return robot;
}

export function setJoints(robot, q) {
  const { J, axes } = robot.userData;
  J.forEach((j, i) => { j.rotation[axes[i]] = (q[i] || 0); });
  robot.updateMatrixWorld(true);
}

// damped least squares IK to put flange at target world matrix (position + orientation)
export function solveIK(robot, targetMatrix, q0, iters = 400) {
  const q = q0.slice();
  const tPos = new THREE.Vector3(), tQuat = new THREE.Quaternion(), tS = new THREE.Vector3();
  targetMatrix.decompose(tPos, tQuat, tS);
  const fl = robot.userData.flange;
  const pos = new THREE.Vector3(), quat = new THREE.Quaternion(), sc = new THREE.Vector3();
  const err = () => {
    setJoints(robot, q); fl.matrixWorld.decompose(pos, quat, sc);
    const ep = tPos.clone().sub(pos);
    const qe = tQuat.clone().multiply(quat.clone().invert());
    if (qe.w < 0) { qe.x *= -1; qe.y *= -1; qe.z *= -1; qe.w *= -1; }
    const ang = 2 * Math.acos(Math.min(1, qe.w)); const s = Math.sqrt(1 - qe.w * qe.w) || 1;
    const er = new THREE.Vector3(qe.x / s, qe.y / s, qe.z / s).multiplyScalar(ang);
    return [ep.x, ep.y, ep.z, er.x * 25, er.y * 25, er.z * 25];
  };
  let lambda = 2.0;
  for (let it = 0; it < iters; it++) {
    const e = err(); const n = Math.hypot(...e); if (n < 1e-3) break;
    const Jm = []; const h = 1e-4;
    for (let i = 0; i < 6; i++) { const old = q[i]; q[i] = old + h; const e2 = err(); q[i] = old; Jm.push(e.map((v, k) => (v - e2[k]) / h)); }
    // J is 6x6 with columns i: d(err)/dq_i (negated), solve (J^T J + l^2 I) dq = J^T e
    const JT = Jm; // JT[i][k] = dErr_k/dq_i (negated sign)
    const A = Array.from({ length: 6 }, (_, i) => Array.from({ length: 6 }, (_, j) => JT[i].reduce((s, v, k) => s + v * JT[j][k], 0) + (i === j ? lambda * lambda : 0)));
    const b = JT.map(row => row.reduce((s, v, k) => s + v * e[k], 0));
    const dq = gauss(A, b);
    for (let i = 0; i < 6; i++) q[i] += Math.max(-0.2, Math.min(0.2, dq[i]));
    const e3 = err(); if (Math.hypot(...e3) < n) lambda = Math.max(0.05, lambda * 0.7); else lambda = Math.min(20, lambda * 2);
  }
  setJoints(robot, q);
  const ef = err();
  return { q, posErr: Math.hypot(ef[0], ef[1], ef[2]), rotErr: Math.hypot(ef[3], ef[4], ef[5]) / 25 };
}
function gauss(A, b) {
  const n = b.length; const M = A.map((r, i) => [...r, b[i]]);
  for (let c = 0; c < n; c++) {
    let p = c; for (let r = c + 1; r < n; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r;
    [M[c], M[p]] = [M[p], M[c]];
    const d = M[c][c] || 1e-9;
    for (let r = 0; r < n; r++) { if (r === c) continue; const f = M[r][c] / d; for (let k = c; k <= n; k++) M[r][k] -= f * M[c][k]; }
  }
  return M.map((r, i) => r[n] / (r[i] || 1e-9));
}

// ---------------------------------------------------------------- Machine tool (brownfield CNC)
export function buildMachine(opts = {}) {
  const g = new THREE.Group(); g.name = 'machine';
  const W = 150, H = 190, Dp = 120;
  const doorOpen = opts.doorOpen ?? 0; // 0..1
  // main enclosure as frame pieces so the door opening is real
  const darkTheme = opts.theme === 'dark';
  const shell = darkTheme ? new THREE.MeshPhysicalMaterial({ color: 0x4b5058, roughness: 0.38, clearcoat: 0.6, clearcoatRoughness: 0.25 }) : MAT.machine;
  const dark = darkTheme ? new THREE.MeshPhysicalMaterial({ color: 0x1e2126, roughness: 0.45, clearcoat: 0.2 }) : MAT.machineDark;
  const back = rbox(W, H, 4, 1.0, shell); back.position.set(0, H / 2, -Dp / 2 + 2); g.add(back);
  const left = rbox(4, H, Dp, 1.0, shell); left.position.set(-W / 2 + 2, H / 2, 0); g.add(left);
  const right = rbox(4, H, Dp, 1.0, shell); right.position.set(W / 2 - 2, H / 2, 0); g.add(right);
  const top = rbox(W, 22, Dp, 2.0, shell); top.position.set(0, H - 11, 0); g.add(top);
  const bottom = rbox(W, 62, Dp, 1.5, shell); bottom.position.set(0, 31, 0); g.add(bottom);
  const plinth = rbox(W - 6, 10, Dp - 6, 1.0, dark); plinth.position.set(0, 5, 0); g.add(plinth);
  // front frame around opening: opening x in [-55, 35], y in [62, 168]
  const fx0 = -58, fx1 = 32, fy0 = 64, fy1 = 166;
  const fL = rbox(fx0 + W / 2, fy1 - fy0, 6, 0.8, shell); fL.position.set((-W / 2 + fx0) / 2, (fy0 + fy1) / 2, Dp / 2 - 3); g.add(fL);
  const fR = rbox(W / 2 - fx1, fy1 - fy0, 6, 0.8, shell); fR.position.set((W / 2 + fx1) / 2, (fy0 + fy1) / 2, Dp / 2 - 3); g.add(fR);
  // dark trim strips
  const trim = rbox(W - 2, 3.5, 1.2, 0.5, dark); trim.position.set(0, 64, Dp / 2 + 0.2); g.add(trim);
  const trim2 = trim.clone(); trim2.position.y = 168; g.add(trim2);
  // interior: dark cavity, table, vise, spindle
  const cav = rbox(fx1 - fx0 - 2, fy1 - fy0 - 2, 2, 0.4, new THREE.MeshStandardMaterial({ color: 0x1b1e23, roughness: 0.8 })); cav.position.set((fx0 + fx1) / 2, (fy0 + fy1) / 2, -Dp / 2 + 6); g.add(cav);
  const floorIn = rbox(fx1 - fx0, 2, Dp - 10, 0.4, new THREE.MeshStandardMaterial({ color: 0x3a3f47, roughness: 0.7 })); floorIn.position.set((fx0 + fx1) / 2, 63, 0); g.add(floorIn);
  const tableM = rbox(56, 5, 34, 0.6, MAT.metalDark); tableM.position.set(-12, 67.5, 16); g.add(tableM);
  // vise
  const vise = new THREE.Group(); vise.position.set(-12, 70, 20); g.add(vise);
  const vb = rbox(20, 5, 12, 0.6, MAT.graphite2); vb.position.y = 2.5; vise.add(vb);
  const jaw1 = rbox(3, 6, 12, 0.3, MAT.metal); jaw1.position.set(-6, 7.5, 0); vise.add(jaw1);
  const jaw2 = rbox(3, 6, 12, 0.3, MAT.metal); jaw2.position.set(4.5, 7.5, 0); vise.add(jaw2);
  const screwV = cyl(0.9, 10, MAT.metal, 24); screwV.rotation.z = Math.PI / 2; screwV.position.set(15, 3.5, 0); vise.add(screwV);
  // vise lever (manual clamp handle) sticking toward the door
  const lever = new THREE.Group(); lever.position.set(20, 3.5, 0); vise.add(lever);
  const lhub = cyl(1.6, 2.2, MAT.metal, 24); lhub.rotation.z = Math.PI / 2; lever.add(lhub);
  const larm = cyl(0.75, 14, MAT.metal, 20); larm.rotation.x = Math.PI / 2; larm.position.z = 7; lever.add(larm);
  const lgrip = cyl(1.25, 5, MAT.graphite, 24); lgrip.rotation.x = Math.PI / 2; lgrip.position.z = 15.5; lever.add(lgrip);
  lever.rotation.x = (opts.leverAngle ?? -0.25);
  if (opts.partInVise) { const pv = buildPart(opts.viseFinished ? 'finished' : 'blank'); pv.position.set(-0.75, 5.0, 0); vise.add(pv); g.userData.visePart = pv; }
  g.userData.lever = lever; g.userData.vise = vise;
  // spindle
  const sp = softCyl(6, 26, 1.0, MAT.machineDark); sp.position.set(-12, 140, 12); g.add(sp);
  const spn = cyl(2.6, 8, MAT.metal, 32); spn.position.set(-12, 123, 12); g.add(spn);
  const tool = cyl(0.8, 9, MAT.metal, 16); tool.position.set(-12, 114, 12); g.add(tool);
  // sliding door with window, slides to the right (+x) behind the right frame
  const door = new THREE.Group(); door.name = 'door'; g.add(door);
  const dw = fx1 - fx0 + 6, dh = fy1 - fy0 + 6;
  const doorX0 = (fx0 + fx1) / 2;
  door.position.set(doorX0 - doorOpen * (dw - 8), (fy0 + fy1) / 2, Dp / 2 + 2.5);
  const dFrame = new THREE.Group(); door.add(dFrame);
  const doorMat = darkTheme ? new THREE.MeshPhysicalMaterial({ color: 0xb9bdc3, roughness: 0.4, clearcoat: 0.5, clearcoatRoughness: 0.3 }) : shell;
  const t = 7; // frame thickness
  const dTop = rbox(dw, t, 3, 0.8, doorMat); dTop.position.y = dh / 2 - t / 2; dFrame.add(dTop);
  const dBot = rbox(dw, t * 1.4, 3, 0.8, doorMat); dBot.position.y = -dh / 2 + t * 0.7; dFrame.add(dBot);
  const dL = rbox(t, dh, 3, 0.8, doorMat); dL.position.x = -dw / 2 + t / 2; dFrame.add(dL);
  const dR = rbox(t * 1.8, dh, 3, 0.8, doorMat); dR.position.x = dw / 2 - t * 0.9; dFrame.add(dR);
  const win = rbox(dw - t * 2.8, dh - t * 2.4, 0.8, 0.3, MAT.glass); win.position.set(-t * 0.4, 0, 0.2); win.castShadow = false; dFrame.add(win);
  // vertical door handle (bar) on the left edge of the door
  const hx = dw / 2 - t * 0.9, hz = 1.5 + 5.5;
  const hb1 = rbox(2.2, 3.0, 5.5, 0.6, MAT.graphite); hb1.position.set(hx, 18, 1.5 + 2.75); door.add(hb1);
  const hb2 = hb1.clone(); hb2.position.y = -18; door.add(hb2);
  const hbar = cyl(1.55, 40, MAT.graphite, 32); hbar.position.set(hx, 0, hz); door.add(hbar);
  door.userData.handle = new THREE.Vector3(hx, 0, hz);
  g.userData.door = door; g.userData.doorOpen = doorOpen;
  // control panel (right side, angled)
  const panel = new THREE.Group(); panel.position.set(W / 2 - 4, 128, Dp / 2 + 6); panel.rotation.y = -0.18; g.add(panel);
  const pb = rbox(30, 44, 7, 1.2, MAT.machineDark); panel.add(pb);
  const scr = rbox(22, 15, 0.6, 0.4, MAT.screen); scr.position.set(0, 10, 3.6); panel.add(scr);
  const keyMat = new THREE.MeshStandardMaterial({ color: 0x4b5058, roughness: 0.5 });
  for (let r = 0; r < 3; r++) for (let c = 0; c < 4; c++) { const k = rbox(3.6, 2.6, 0.8, 0.4, keyMat); k.position.set(-7.5 + c * 5, -3 - r * 3.6, 3.7); panel.add(k); }
  const start = cyl(2.0, 1.4, MAT.green, 32); start.rotation.x = Math.PI / 2; start.position.set(-6, -16.5, 4.0); panel.add(start);
  const hold = cyl(2.0, 1.4, MAT.yellow, 32); hold.rotation.x = Math.PI / 2; hold.position.set(0.5, -16.5, 4.0); panel.add(hold);
  const estop = cyl(2.6, 2.0, MAT.red, 32); estop.rotation.x = Math.PI / 2; estop.position.set(8, -16.5, 4.3); panel.add(estop);
  g.userData.panel = panel; g.userData.startBtn = start;
  // interior work light
  if (opts.workLight !== false) { const wl = new THREE.PointLight(0xfff1dc, opts.workLightI ?? 22000, 260, 2); wl.position.set(-12, 158, 10); g.add(wl);
    const wl2 = new THREE.PointLight(0xfff1dc, (opts.workLightI ?? 9000) * 0.5, 200, 2); wl2.position.set(-40, 100, 30); g.add(wl2); }
  // status light tower
  const tw = cyl(1.4, 4, MAT.green, 24); tw.position.set(W / 2 - 12, H + 2, -Dp / 2 + 12); g.add(tw);
  const tw2 = cyl(1.4, 4, MAT.yellow, 24); tw2.position.set(W / 2 - 12, H + 6, -Dp / 2 + 12); g.add(tw2);
  const tw3 = cyl(1.4, 4, MAT.red, 24); tw3.position.set(W / 2 - 12, H + 10, -Dp / 2 + 12); g.add(tw3);
  return g;
}

export function buildPart(type = 'blank') {
  const g = new THREE.Group();
  if (type === 'blank') { const c = cyl(2.6, 7.0, MAT.alu, 40); c.position.y = 3.5; g.add(c); }
  else { // finished part: stepped shaft with groove
    const c1 = cyl(2.6, 3.4, MAT.alu, 40); c1.position.y = 1.7; g.add(c1);
    const c2 = cyl(1.8, 2.6, MAT.metal, 40); c2.position.y = 4.7; g.add(c2);
    const c3 = cyl(2.2, 1.0, MAT.alu, 40); c3.position.y = 6.5; g.add(c3);
  }
  return g;
}

export function buildTrayStation(nx = 4, nz = 3, filled = null) {
  const g = new THREE.Group();
  const stand = rbox(52, 72, 44, 1.2, MAT.table); stand.position.y = 36; g.add(stand);
  const tray = rbox(40, 3, 32, 0.8, MAT.tray); tray.position.y = 73.5; g.add(tray);
  const parts = [];
  for (let i = 0; i < nx; i++) for (let k = 0; k < nz; k++) {
    const idx = i * nz + k; const has = filled ? filled(idx) : true;
    const x = -15 + i * 10, z = -10 + k * 10;
    const hole = cyl(3.0, 0.4, new THREE.MeshStandardMaterial({ color: 0x2c3036, roughness: 0.7 }), 32); hole.position.set(x, 75.1, z); g.add(hole);
    if (has) { const p = buildPart(idx % 2 === 0 && filled ? 'blank' : 'blank'); p.position.set(x, 75.0, z); g.add(p); parts.push(p); }
  }
  g.userData.parts = parts;
  return g;
}

// ---------------------------------------------------------------- scene helpers
export function makeRenderer(W, H) {
  const r = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });
  r.setPixelRatio(1); r.setSize(W, H); r.setClearColor(0x000000, 0);
  r.toneMapping = THREE.ACESFilmicToneMapping; r.toneMappingExposure = 1.0;
  r.outputColorSpace = THREE.SRGBColorSpace;
  r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap;
  document.body.appendChild(r.domElement);
  return r;
}
export function makeScene(renderer, envIntensity = 1.0) {
  const s = new THREE.Scene();
  const pm = new THREE.PMREMGenerator(renderer);
  s.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
  s.environmentIntensity = envIntensity;
  return s;
}
export function addLights(scene, opts = {}) {
  const key = new THREE.DirectionalLight(0xffffff, opts.key ?? 1.6);
  key.position.set(...(opts.keyPos ?? [60, 120, 90])); key.castShadow = true;
  key.shadow.mapSize.set(4096, 4096); const sc = opts.shadowSize ?? 120;
  Object.assign(key.shadow.camera, { left: -sc, right: sc, top: sc, bottom: -sc, near: 1, far: 800 });
  key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02; key.shadow.radius = 6;
  if (opts.target) key.target.position.set(...opts.target);
  scene.add(key); scene.add(key.target);
  const rim = new THREE.DirectionalLight(0xdfe8ff, opts.rim ?? 0.55); rim.position.set(...(opts.rimPos ?? [-80, 60, -100])); scene.add(rim);
  const fill = new THREE.HemisphereLight(0xffffff, 0x30343a, opts.hemi ?? 0.35); scene.add(fill);
  return { key, rim, fill };
}
export function shadowCatcher(scene, y = 0, size = 600, opacity = 0.28) {
  const g = new THREE.Mesh(new THREE.PlaneGeometry(size, size), new THREE.ShadowMaterial({ opacity }));
  g.rotation.x = -Math.PI / 2; g.position.y = y; g.receiveShadow = true; scene.add(g); return g;
}
export { THREE };
