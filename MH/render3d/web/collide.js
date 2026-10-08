// Robot-vs-furniture collision check (units: cm).
// Robot links are approximated by capsules taken from the cobot geometry in lib.js (style A);
// furniture by axis-aligned boxes collected from meshes tagged userData.obst = true.
import * as THREE from 'three';

const V = (x, y, z) => new THREE.Vector3(x, y, z);

// capsule list in each joint frame: [frameIndex, a, b, r]; frame -1 = robot root, 6 = flange
function capsuleDefs(robot) {
  const UA = 42.5, FA = 39.2;
  return [
    [-1, V(0, 1.5, 0), V(0, 5.5, 0), 7.6],              // base disc + body (end caps reach y -6.1..13.1)
    [0, V(0, 0, 0), V(0, 8.4, 0), 6.5],                 // shoulder body (j1)
    [1, V(-4.0, 0, 0), V(16.5, 0, 0), 6.6],             // shoulder housing (j2, along x)
    [1, V(13.0, 6.0, 0), V(13.0, UA - 5.0, 0), 4.6],    // upper arm (offset 13 cm from the base axis)
    [2, V(-1.5, 0, 0), V(16.5, 0, 0), 5.4],             // elbow housing (j3)
    [2, V(0.5, 5.0, 0), V(0.5, FA - 3.2, 0), 3.8],      // forearm
    [3, V(-4.5, 0, 0), V(5.5, 0, 0), 4.4],              // wrist 1 (j4)
    [3, V(-0.5, 0.3, 0), V(-0.5, 9.3, 0), 4.3],         // wrist 2 body
    [4, V(0, 4.3, -4.0), V(0, 4.3, 5.0), 4.3],          // wrist 3 (j5)
    [6, V(0, 0, 0), V(0, 13.5, 0), 4.2],                // gripper (flange frame)
  ];
}

export function robotCapsules(robot, extra = []) {
  robot.updateMatrixWorld(true);
  const J = robot.userData.J, fl = robot.userData.flange;
  const frames = [...J, fl];   // J[0..5] = j1..j6, index 6 = flange
  const out = [];
  const s = robot.getWorldScale(V(1, 1, 1)).x;
  for (const [fi, a, b, r] of capsuleDefs(robot)) {
    const m = fi === -1 ? robot.matrixWorld : frames[fi].matrixWorld;
    out.push({ a: a.clone().applyMatrix4(m), b: b.clone().applyMatrix4(m), r: r * s, link: fi });
  }
  // held object (plate / bowl) attached to the tcp: approximate by two crossing thin capsules / a small capsule
  const tcp = robot.userData.tcp;
  if (tcp && tcp.children.length) {
    for (const o of tcp.children) {
      o.updateMatrixWorld(true);
      const bb = new THREE.Box3().setFromObject(o);
      const c = bb.getCenter(V(0, 0, 0)), sz = bb.getSize(V(0, 0, 0));
      const ax = sz.x >= sz.y && sz.x >= sz.z ? 'x' : (sz.y >= sz.z ? 'y' : 'z');
      const half = sz[ax] / 2 - 1.0, rad = Math.max(1.2, Math.min(...['x', 'y', 'z'].filter(k => k !== ax).map(k => sz[k])) / 2);
      const d = V(0, 0, 0); d[ax] = half;
      out.push({ a: c.clone().sub(d), b: c.clone().add(d), r: rad, link: 'held' });
    }
  }
  for (const e of extra) out.push(e);
  return out;
}

export function collectObstacles(root, filter = null) {
  const boxes = [];
  root.updateMatrixWorld(true);
  root.traverse(o => {
    if (!o.isMesh || !o.userData.obst) return;
    if (filter && !filter(o)) return;
    const b = new THREE.Box3().setFromObject(o);
    if (b.isEmpty()) return;
    b.userData = { name: o.userData.obstName || o.name || '', mesh: o };
    boxes.push(b);
  });
  return boxes;
}

// signed distance point -> AABB (negative inside)
function sdBox(p, b) {
  const dx = Math.max(b.min.x - p.x, 0, p.x - b.max.x);
  const dy = Math.max(b.min.y - p.y, 0, p.y - b.max.y);
  const dz = Math.max(b.min.z - p.z, 0, p.z - b.max.z);
  const out = Math.hypot(dx, dy, dz);
  if (out > 0) return out;
  return -Math.min(p.x - b.min.x, b.max.x - p.x, p.y - b.min.y, b.max.y - p.y, p.z - b.min.z, b.max.z - p.z);
}

// total penetration depth (cm) of the capsules into the boxes, plus a per-link report
export function penetration(caps, boxes, margin = 0.3, step = 1.0) {
  let total = 0; const hits = [];
  for (const c of caps) {
    const L = c.a.distanceTo(c.b); const n = Math.max(1, Math.ceil(L / step));
    let worst = 0, worstBox = null;
    for (let i = 0; i <= n; i++) {
      const p = c.a.clone().lerp(c.b, i / n);
      for (const b of boxes) {
        // quick reject
        if (p.x < b.min.x - c.r || p.x > b.max.x + c.r || p.y < b.min.y - c.r || p.y > b.max.y + c.r || p.z < b.min.z - c.r || p.z > b.max.z + c.r) continue;
        const pen = c.r - margin - sdBox(p, b);
        if (pen > worst) { worst = pen; worstBox = b; }
      }
    }
    if (worst > 0) { total += worst; hits.push({ link: c.link, depth: +worst.toFixed(2), box: worstBox.userData?.name || '' }); }
  }
  return { total, hits };
}

// closest distance between segments p1-q1 and p2-q2
function segSegDist(p1, q1, p2, q2) {
  const d1 = q1.clone().sub(p1), d2 = q2.clone().sub(p2), r = p1.clone().sub(p2);
  const a = d1.dot(d1), e = d2.dot(d2), f = d2.dot(r);
  let s, t;
  if (a < 1e-9 && e < 1e-9) return p1.distanceTo(p2);
  if (a < 1e-9) { s = 0; t = Math.min(1, Math.max(0, f / e)); }
  else {
    const c = d1.dot(r);
    if (e < 1e-9) { t = 0; s = Math.min(1, Math.max(0, -c / a)); }
    else {
      const b = d1.dot(d2), den = a * e - b * b;
      s = den > 1e-9 ? Math.min(1, Math.max(0, (b * f - c * e) / den)) : 0;
      t = (b * s + f) / e;
      if (t < 0) { t = 0; s = Math.min(1, Math.max(0, -c / a)); }
      else if (t > 1) { t = 1; s = Math.min(1, Math.max(0, (b - c) / a)); }
    }
  }
  return p1.clone().add(d1.multiplyScalar(s)).distanceTo(p2.clone().add(d2.multiplyScalar(t)));
}

// self-collision between non-neighbouring links (capsule order of capsuleDefs; 'held' objects ignored)
export function selfPenetration(caps, slack = 1.0) {
  const arm = caps.filter(c => c.link !== 'held');
  let total = 0; const hits = [];
  for (let i = 0; i < arm.length; i++) for (let j = i + 2; j < arm.length; j++) {
    if (j - i === 2 && !(i === 3 && j === 5)) continue;          // only UA-forearm among the second neighbours
    const pen = arm[i].r + arm[j].r - slack - segSegDist(arm[i].a, arm[i].b, arm[j].a, arm[j].b);
    if (pen > 0) { total += pen; hits.push({ pair: [i, j], depth: +pen.toFixed(2) }); }
  }
  return { total, hits };
}

// world AABB of a capsule list
export function capsuleBounds(caps) {
  const b = { xmin: 1e9, ymin: 1e9, zmin: 1e9, xmax: -1e9, ymax: -1e9, zmax: -1e9 };
  for (const c of caps) for (const p of [c.a, c.b]) {
    b.xmin = Math.min(b.xmin, p.x - c.r); b.xmax = Math.max(b.xmax, p.x + c.r);
    b.ymin = Math.min(b.ymin, p.y - c.r); b.ymax = Math.max(b.ymax, p.y + c.r);
    b.zmin = Math.min(b.zmin, p.z - c.r); b.zmax = Math.max(b.zmax, p.z + c.r);
  }
  return b;
}
