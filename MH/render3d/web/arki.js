// ARKI Robotics — concept scenes (units: cm). Semi-realistic technical visualization, not product photography.
// World: x right, y up, z toward the viewer. Kitchen back wall face at z = 0 unless noted.
import { THREE, initMaterials, MAT, makeRenderer, makeScene, addLights, buildCobot, solveIK, setJoints, rbox, cyl, softCyl } from './lib.js';
import { robotCapsules, collectObstacles, penetration, selfPenetration, capsuleBounds } from './collide.js';
import { planMats, buildWalls, buildFloors, buildFixtures, roomAnchors, planBounds } from './plan3d.js';

const D = Math.PI / 180;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const ORANGE = 0xe2571b;

// ---------------------------------------------------------------- materials
let A = null;
function canvasTex(w, h, draw, repeat = [1, 1]) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const g = c.getContext('2d'); draw(g, w, h);
  const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(...repeat);
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  return t;
}
export function amat() {
  if (A) return A;
  initMaterials();
  const oak = canvasTex(1024, 1024, (g, w, h) => {
    g.fillStyle = '#c6a882'; g.fillRect(0, 0, w, h);
    const rows = 8;
    for (let r = 0; r < rows; r++) {
      let x = (r % 2) * 260;
      while (x < w + 520) {
        const len = 420 + ((r * 37 + x) % 3) * 90;
        const shade = 178 + ((r * 13 + x * 7) % 22);
        g.fillStyle = `rgb(${shade + 20},${shade + 2},${shade - 26})`;
        g.fillRect(x - 520, r * (h / rows) + 2, len - 3, h / rows - 4);
        for (let k = 0; k < 6; k++) { g.fillStyle = 'rgba(120,90,60,0.05)'; g.fillRect(x - 520, r * (h / rows) + 6 + k * 18, len - 3, 3); }
        x += len;
      }
    }
  }, [1, 1]);
  const hatch = canvasTex(256, 256, (g, w, h) => {
    g.clearRect(0, 0, w, h); g.fillStyle = 'rgba(255,255,255,0.55)'; g.fillRect(0, 0, w, h); g.strokeStyle = 'rgba(60,64,70,0.9)'; g.lineWidth = 10;
    for (let i = -h; i < w + h; i += 40) { g.beginPath(); g.moveTo(i, h); g.lineTo(i + h, 0); g.stroke(); }
  }, [1, 1]);
  A = {
    oak, hatch,
    floor: new THREE.MeshStandardMaterial({ color: 0xffffff, map: oak, roughness: 0.72 }),
    floorPlain: new THREE.MeshStandardMaterial({ color: 0xe6dfd4, roughness: 0.85 }),
    floorWet: new THREE.MeshStandardMaterial({ color: 0xd9dcdf, roughness: 0.6 }),
    wall: new THREE.MeshStandardMaterial({ color: 0xebe7e0, roughness: 0.92 }),
    wallCap: new THREE.MeshStandardMaterial({ color: 0x2b2e33, roughness: 0.8 }),
    cabUpper: new THREE.MeshPhysicalMaterial({ color: 0xe6e1d8, roughness: 0.45, clearcoat: 0.12 }),
    cabLower: new THREE.MeshPhysicalMaterial({ color: 0x8f877c, roughness: 0.52, clearcoat: 0.1 }),
    cabTall: new THREE.MeshPhysicalMaterial({ color: 0xdcd6cc, roughness: 0.48, clearcoat: 0.12 }),
    cabInside: new THREE.MeshStandardMaterial({ color: 0xcfc9bf, roughness: 0.8 }),
    gap: new THREE.MeshStandardMaterial({ color: 0x8e8b86, roughness: 0.8 }),
    quartz: new THREE.MeshPhysicalMaterial({ color: 0xe9e6e0, roughness: 0.3, clearcoat: 0.45 }),
    steel: new THREE.MeshStandardMaterial({ color: 0xc7ccd2, metalness: 0.85, roughness: 0.32 }),
    steelDark: new THREE.MeshStandardMaterial({ color: 0x8e949c, metalness: 0.85, roughness: 0.42 }),
    sinkIn: new THREE.MeshStandardMaterial({ color: 0x9aa0a7, metalness: 0.8, roughness: 0.38 }),
    hob: new THREE.MeshPhysicalMaterial({ color: 0x15171a, roughness: 0.12, clearcoat: 1.0, clearcoatRoughness: 0.06 }),
    hobRing: new THREE.MeshStandardMaterial({ color: 0x5b6068, roughness: 0.5 }),
    dwIn: new THREE.MeshStandardMaterial({ color: 0x5d636b, metalness: 0.6, roughness: 0.5 }),
    rack: new THREE.MeshStandardMaterial({ color: 0xa9aeb5, metalness: 0.7, roughness: 0.35 }),
    ceramic: new THREE.MeshPhysicalMaterial({ color: 0xf7f6f2, roughness: 0.2, clearcoat: 0.8 }),
    ceramicB: new THREE.MeshPhysicalMaterial({ color: 0xdbe2e8, roughness: 0.22, clearcoat: 0.7 }),
    ceramicG: new THREE.MeshPhysicalMaterial({ color: 0xcfd3c8, roughness: 0.25, clearcoat: 0.7 }),
    rail: new THREE.MeshStandardMaterial({ color: 0x33373e, metalness: 0.6, roughness: 0.35 }),
    railAccent: new THREE.MeshStandardMaterial({ color: ORANGE, roughness: 0.5, emissive: ORANGE, emissiveIntensity: 0.35 }),
    homeBack: new THREE.MeshStandardMaterial({ color: 0xf0c7b2, roughness: 0.8 }),
    dark: new THREE.MeshStandardMaterial({ color: 0x22252a, roughness: 0.6 }),
    wood: new THREE.MeshStandardMaterial({ color: 0xb08a63, roughness: 0.65 }),
    chair: new THREE.MeshStandardMaterial({ color: 0x9a9fa6, roughness: 0.6 }),
    human: new THREE.MeshStandardMaterial({ color: 0xb8bdc4, roughness: 0.75 }),
    sofa: new THREE.MeshStandardMaterial({ color: 0x9d968b, roughness: 0.85 }),
    bed: new THREE.MeshStandardMaterial({ color: 0xc9c1b4, roughness: 0.85 }),
    fridge: new THREE.MeshPhysicalMaterial({ color: 0xd9dcdf, roughness: 0.3, metalness: 0.3, clearcoat: 0.4 }),
    glass: new THREE.MeshPhysicalMaterial({ color: 0xbfd2de, roughness: 0.05, transparent: true, opacity: 0.25 }),
    zoneRobot: new THREE.MeshBasicMaterial({ color: ORANGE, transparent: true, opacity: 0.34, depthWrite: false }),
    zoneHuman: new THREE.MeshBasicMaterial({ color: 0x7f8a96, transparent: true, opacity: 0.30, depthWrite: false }),
    zoneNoGo: new THREE.MeshBasicMaterial({ map: hatch, transparent: true, opacity: 0.85, depthWrite: false }),
    reach: new THREE.MeshBasicMaterial({ color: ORANGE, transparent: true, opacity: 0.06, depthWrite: false, side: THREE.DoubleSide }),
    edgeOrange: new THREE.LineBasicMaterial({ color: ORANGE, transparent: true, opacity: 0.9 }),
    edgeGrey: new THREE.LineBasicMaterial({ color: 0x4a4f57, transparent: true, opacity: 0.9 }),
    path: new THREE.MeshBasicMaterial({ color: ORANGE }),
    cone: new THREE.MeshBasicMaterial({ color: ORANGE, transparent: true, opacity: 0.16, depthWrite: false, side: THREE.DoubleSide }),
    roomFloor: [0xdccfbc, 0xd6c9b5, 0xd9ccb9, 0xd3c6b2],
  };
  return A;
}

// ---------------------------------------------------------------- primitives
export const OB = { on: false, name: '' };   // while on, every bx() mesh is tagged as a collision obstacle
function bx(x0, y0, z0, x1, y1, z1, mat, r = 0) {
  const w = x1 - x0, h = y1 - y0, d = z1 - z0;
  const m = r > 0 ? rbox(w, h, d, r, mat, 3) : new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat);
  m.position.set((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2); m.castShadow = true; m.receiveShadow = true;
  if (OB.on) { m.userData.obst = true; m.userData.obstName = OB.name; }
  return m;
}
function obst(name, fn) { const prev = { ...OB }; OB.on = true; OB.name = name; try { return fn(); } finally { OB.on = prev.on; OB.name = prev.name; } }
function plane(x0, z0, x1, z1, y, mat) {
  const m = new THREE.Mesh(new THREE.PlaneGeometry(x1 - x0, z1 - z0), mat);
  m.rotation.x = -Math.PI / 2; m.position.set((x0 + x1) / 2, y, (z0 + z1) / 2); m.receiveShadow = true;
  return m;
}
function edges(mesh, mat) {
  const e = new THREE.LineSegments(new THREE.EdgesGeometry(mesh.geometry), mat);
  e.position.copy(mesh.position); e.rotation.copy(mesh.rotation); e.scale.copy(mesh.scale);
  return e;
}
function strip(x0, z0, x1, z1, y, wid, mat) {     // thin flat bar (for crisp outlines / paths)
  const dx = x1 - x0, dz = z1 - z0, L = Math.hypot(dx, dz);
  const m = new THREE.Mesh(new THREE.BoxGeometry(L, 0.4, wid), mat);
  m.position.set((x0 + x1) / 2, y, (z0 + z1) / 2); m.rotation.y = -Math.atan2(dz, dx);
  return m;
}
function outline(g, x0, z0, x1, z1, y, wid, mat, dashed = false) {
  const segs = [[x0, z0, x1, z0], [x1, z0, x1, z1], [x1, z1, x0, z1], [x0, z1, x0, z0]];
  for (const [a, b, c, d] of segs) {
    if (!dashed) { g.add(strip(a, b, c, d, y, wid, mat)); continue; }
    const L = Math.hypot(c - a, d - b), n = Math.max(1, Math.floor(L / 14));
    for (let i = 0; i < n; i += 2) {
      const t0 = i / n, t1 = Math.min(1, (i + 1) / n);
      g.add(strip(a + (c - a) * t0, b + (d - b) * t0, a + (c - a) * t1, b + (d - b) * t1, y, wid, mat));
    }
  }
}

// ---------------------------------------------------------------- tableware
export function plate(r = 12.5, mat) {
  const a = amat(); const pts = [];
  pts.push(new THREE.Vector2(0, 0)); pts.push(new THREE.Vector2(r * 0.55, 0)); pts.push(new THREE.Vector2(r * 0.62, 0.9));
  pts.push(new THREE.Vector2(r * 0.95, 1.6)); pts.push(new THREE.Vector2(r, 2.1)); pts.push(new THREE.Vector2(r * 0.98, 2.35));
  pts.push(new THREE.Vector2(r * 0.6, 1.5)); pts.push(new THREE.Vector2(0, 1.2));
  const m = new THREE.Mesh(new THREE.LatheGeometry(pts, 48), mat || a.ceramic); m.castShadow = true; m.receiveShadow = true;
  return m;
}
export function bowl(r = 6.5, h = 6, mat) {
  const a = amat(); const pts = [];
  for (let i = 0; i <= 10; i++) { const t = i / 10; pts.push(new THREE.Vector2(r * 0.45 + r * 0.55 * Math.sin(t * Math.PI / 2), h * t)); }
  for (let i = 10; i >= 0; i--) { const t = i / 10; pts.push(new THREE.Vector2(r * 0.4 + r * 0.52 * Math.sin(t * Math.PI / 2), 0.6 + (h - 0.6) * t)); }
  const m = new THREE.Mesh(new THREE.LatheGeometry(pts, 40), mat || a.ceramic); m.castShadow = true; m.receiveShadow = true;
  return m;
}
export function cup(r = 3.8, h = 9, mat) {
  const a = amat(); const g = new THREE.Group();
  const pts = [new THREE.Vector2(0, 0), new THREE.Vector2(r, 0), new THREE.Vector2(r * 1.06, h), new THREE.Vector2(r * 0.94, h), new THREE.Vector2(r * 0.88, 0.6), new THREE.Vector2(0, 0.6)];
  const m = new THREE.Mesh(new THREE.LatheGeometry(pts, 32), mat || a.glass); m.castShadow = true; g.add(m);
  return g;
}

// ---------------------------------------------------------------- kitchen parts (all along the back wall, z from 0)
function baseRun(...a) { return obst('base', () => _baseRun(...a)); }
function _baseRun(g, x0, x1, opts = {}) {
  const a = amat(); const z0 = opts.z0 ?? 0, d = opts.depth ?? 58, h = opts.h ?? 85, plinth = 10;
  g.add(bx(x0, 0, z0, x1, plinth, z0 + d - 5, a.dark));
  g.add(bx(x0, plinth, z0, x1, h, z0 + d - 2, a.cabLower));
  const doorW = opts.doorW ?? 60; let x = x0;
  while (x < x1 - 1) { const w = Math.min(doorW, x1 - x); g.add(bx(x + 0.3, plinth + 0.5, z0 + d - 2, x + w - 0.3, h - 0.5, z0 + d - 1.2, a.cabLower)); x += w; }
}
function counter(...a) { return obst('counter', () => _counter(...a)); }
function _counter(g, x0, x1, opts = {}) {
  const a = amat(); const z0 = opts.z0 ?? 0, d = opts.depth ?? 62, y = opts.y ?? 85, t = 3.2;
  const holes = (opts.holes || []).slice().sort((p, q) => p[0] - q[0]);
  let x = x0;
  for (const [hx0, hx1, hz0, hz1] of holes) {
    if (hx0 > x) g.add(bx(x, y, z0, hx0, y + t, z0 + d, a.quartz));
    g.add(bx(hx0, y, z0, hx1, y + t, z0 + hz0, a.quartz));
    g.add(bx(hx0, y, z0 + hz1, hx1, y + t, z0 + d, a.quartz));
    x = hx1;
  }
  if (x < x1) g.add(bx(x, y, z0, x1, y + t, z0 + d, a.quartz));
}
function sink(g, cx, opts = {}) {
  const a = amat(); const w = opts.w ?? 80, y = 88.2, z0 = 10, z1 = 52;
  const x0 = cx - w / 2, x1 = cx + w / 2;
  g.add(bx(x0, y - 22, z0, x1, y - 21, z1, a.sinkIn));                      // bottom
  g.add(bx(x0, y - 22, z0, x0 + 1, y, z1, a.sinkIn)); g.add(bx(x1 - 1, y - 22, z0, x1, y, z1, a.sinkIn));
  g.add(bx(x0, y - 22, z0, x1, y, z0 + 1, a.sinkIn)); g.add(bx(x0, y - 22, z1 - 1, x1, y, z1, a.sinkIn));
  const drain = cyl(2.2, 0.4, a.steelDark, 24); drain.position.set(cx, y - 21.2, (z0 + z1) / 2); g.add(drain);
  const f = new THREE.Group(); f.position.set(cx + w * 0.28, y, 6); g.add(f);
  const base = cyl(2.6, 4, a.steel, 24); base.position.y = 2; f.add(base);
  const col = cyl(1.4, 28, a.steel, 20); col.position.y = 16; f.add(col);
  const arc = new THREE.Mesh(new THREE.TorusGeometry(9, 1.4, 12, 32, Math.PI), a.steel); arc.position.set(0, 30, 9); arc.rotation.y = Math.PI / 2; arc.castShadow = true; f.add(arc);
  const spout = cyl(1.3, 7, a.steel, 20); spout.position.set(0, 26.5, 18); f.add(spout);
  f.traverse(o => { if (o.isMesh) { o.userData.obst = true; o.userData.obstName = 'faucet'; } });
  return { x0, x1, z0, z1, y, center: V(cx, y - 10, (z0 + z1) / 2) };
}
function induction(g, cx, opts = {}) {
  const a = amat(); const w = opts.w ?? 58, z0 = opts.z0 ?? 4, d = 51, y = 88.2;
  const hob = rbox(w, 0.7, d, 0.3, a.hob, 2); hob.position.set(cx, y + 0.35, z0 + d / 2); g.add(hob);
  for (const [dx, dz, r] of [[-w * 0.25, d * 0.28, 9], [w * 0.25, d * 0.28, 8], [-w * 0.25, -d * 0.22, 8], [w * 0.22, -d * 0.2, 10]]) {
    const ring = new THREE.Mesh(new THREE.TorusGeometry(r, 0.25, 6, 48), a.hobRing); ring.rotation.x = Math.PI / 2; ring.position.set(cx + dx, y + 0.75, z0 + d / 2 + dz); g.add(ring);
  }
  return { center: V(cx, y, z0 + d / 2) };
}
function upperRun(...a) { return obst('upper', () => _upperRun(...a)); }
function _upperRun(g, x0, x1, opts = {}) {
  const a = amat(); const y0 = opts.y0 ?? 145, y1 = opts.y1 ?? 225, d = opts.depth ?? 35;
  g.add(bx(x0, y0, 0, x1, y1, d - 1.5, a.cabUpper));
  const doorW = opts.doorW ?? 45; let x = x0;
  while (x < x1 - 1) { const w = Math.min(doorW, x1 - x); g.add(bx(x + 0.3, y0 + 0.3, d - 1.5, x + w - 0.3, y1 - 0.3, d - 0.4, a.cabUpper)); x += w; }
  // under-cabinet light
  const led = new THREE.Mesh(new THREE.BoxGeometry(x1 - x0 - 6, 0.4, 2), new THREE.MeshBasicMaterial({ color: 0xfff6e8 })); led.position.set((x0 + x1) / 2, y0 - 0.25, d - 6); g.add(led);
}
function backsplash(...a) { return obst('wall', () => _backsplash(...a)); }
function _backsplash(g, x0, x1, y0 = 88, y1 = 145) {
  const a = amat(); g.add(bx(x0, y0, -1.2, x1, y1, 0, new THREE.MeshStandardMaterial({ color: 0xc8c2b8, roughness: 0.35 })));
}

// elevated dishwasher + robot-friendly storage tall unit (x0..x0+w)
function tallDW(...a) { return obst('tall', () => _tallDW(...a)); }
function _tallDW(g, x0, opts = {}) {
  const a = amat(); const w = opts.w ?? 60, d = 60, H = opts.H ?? 225;
  const x1 = x0 + w, dwY0 = opts.dwY0 ?? 46, dwY1 = dwY0 + 80, stY0 = dwY1 + 6, stY1 = stY0 + 26;
  const dwOpen = opts.dwOpen ?? 1, rackOut = opts.rackOut ?? 1, stOut = opts.stOut ?? 1;
  // carcass sides / back / shelves
  g.add(bx(x0, 0, 0, x0 + 1.8, H, d, a.cabTall)); g.add(bx(x1 - 1.8, 0, 0, x1, H, d, a.cabTall));
  g.add(bx(x0, 0, 0, x1, 10, d - 5, a.dark));
  g.add(bx(x0 + 1.8, 10, 0, x1 - 1.8, dwY0, d - 1.2, a.cabTall));                      // below DW
  g.add(bx(x0 + 1.8, H - 58, 0, x1 - 1.8, H, d - 1.2, a.cabTall));                     // top storage closed
  if (!opts.homeTop) g.add(bx(x0 + 1.8, stY1 + 2, 0, x1 - 1.8, H - 58, d - 1.2, a.cabTall));   // between storage and top
  g.add(bx(x0 + 1.8, dwY0, 0, x1 - 1.8, dwY1 + 6, 1.5, a.cabInside));
  // dishwasher cavity
  const cav = new THREE.Group(); g.add(cav);
  cav.add(bx(x0 + 2.5, dwY0, 1.5, x1 - 2.5, dwY0 + 1, d - 3, a.dwIn));
  cav.add(bx(x0 + 2.5, dwY1 - 1, 1.5, x1 - 2.5, dwY1, d - 3, a.dwIn));
  cav.add(bx(x0 + 2.5, dwY0, 1.5, x0 + 3.5, dwY1, d - 3, a.dwIn)); cav.add(bx(x1 - 3.5, dwY0, 1.5, x1 - 2.5, dwY1, d - 3, a.dwIn));
  cav.add(bx(x0 + 2.5, dwY0, 1.5, x1 - 2.5, dwY1, 2.5, a.dwIn));
  // door (hinged at bottom front edge)
  const door = new THREE.Group(); door.position.set((x0 + x1) / 2, dwY0, d - 2); door.rotation.x = dwOpen * 88 * D; g.add(door);
  const dp = bx(-(w / 2 - 2.2), 0, -1.2, w / 2 - 2.2, dwY1 - dwY0, 1.2, a.cabTall); door.add(dp);
  const dIn = bx(-(w / 2 - 5), 3, -2.2, w / 2 - 5, dwY1 - dwY0 - 4, -1.2, a.dwIn); door.add(dIn);
  // racks (lower + upper), pulled out
  const racks = [];
  for (const [ry, out] of [[dwY0 + 8, rackOut * 34], [dwY0 + 44, rackOut * 0.6 * 30]]) {
    const r = new THREE.Group(); r.position.set((x0 + x1) / 2, ry, (d - 3) / 2 + 2 + out); g.add(r);
    const rw = w - 10, rd = d - 12;
    const frame = [[-rw / 2, -rd / 2, rw / 2, -rd / 2], [rw / 2, -rd / 2, rw / 2, rd / 2], [rw / 2, rd / 2, -rw / 2, rd / 2], [-rw / 2, rd / 2, -rw / 2, -rd / 2]];
    for (const [p, q, s, t] of frame) { const L = Math.hypot(s - p, t - q); const bar = cyl(0.35, L, a.rack, 8); bar.rotation.z = Math.PI / 2; bar.rotation.y = -Math.atan2(t - q, s - p); bar.position.set((p + s) / 2, 0, (q + t) / 2); r.add(bar);
      const bar2 = bar.clone(); bar2.position.y = 9; r.add(bar2); }
    for (let i = -rw / 2 + 4; i <= rw / 2 - 4; i += 4) { const tine = cyl(0.25, rd, a.rack, 6); tine.rotation.x = Math.PI / 2; tine.position.set(i, 0, 0); r.add(tine); }
    racks.push(r);
  }
  if (opts.homeTop) {   // robot home niche replaces the storage zone: open, orange-tinted back panel
    g.add(bx(x0 + 1.8, stY0 - 6, 1.2, x1 - 1.8, H - 58, 2.4, a.homeBack));
  }
  // storage pull-out (robot-friendly, top access)
  const st = new THREE.Group(); st.position.set((x0 + x1) / 2, stY0, d / 2 + stOut * 38); if (!opts.homeTop) g.add(st);
  const obPrev = OB.on; OB.on = false;
  st.add(bx(-(w / 2 - 3), 0, -(d / 2 - 2), w / 2 - 3, 1.2, d / 2 - 2, a.cabInside));
  st.add(bx(-(w / 2 - 3), 0, d / 2 - 3, w / 2 - 3, 14, d / 2 - 1.5, a.cabTall));
  st.add(bx(-(w / 2 - 3), 0, -(d / 2 - 2), -(w / 2 - 4.5), 10, d / 2 - 2, a.cabTall)); st.add(bx(w / 2 - 4.5, 0, -(d / 2 - 2), w / 2 - 3, 10, d / 2 - 2, a.cabTall));
  for (let i = 0; i < 7; i++) { const peg = cyl(0.5, 6, a.steelDark, 8); peg.position.set(-w / 2 + 12, 4, -d / 2 + 10 + i * 5); st.add(peg); }
  OB.on = obPrev;
  return { x0, x1, d, dwY0, dwY1, stY0, racks, storage: st, door };
}
// slim tall cabinet with robot garage niche (Robot Home) at the top
function garageTall(...a) { return obst('garage', () => _garageTall(...a)); }
function _garageTall(g, x0, w = 44, opts = {}) {
  const a = amat(); const d = 60, H = 225, x1 = x0 + w, n0 = opts.niche0 ?? 100;
  g.add(bx(x0, 0, 0, x1, 10, d - 5, a.dark));
  g.add(bx(x0, 10, 0, x1, n0, d - 1.2, a.cabTall));
  g.add(bx(x0, n0, 0, x0 + 1.8, H, d - 1.2, a.cabTall)); g.add(bx(x1 - 1.8, n0, 0, x1, H, d - 1.2, a.cabTall));
  g.add(bx(x0, H - 6, 0, x1, H, d - 1.2, a.cabTall));
  g.add(bx(x0 + 1.8, n0, 0, x1 - 1.8, H - 6, 1.2, a.homeBack));
  // door folded open (pocket door, pushed back)
  g.add(bx(x1 - 0.4, n0 + 1, d - 1.2, x1 + 1.4, H - 7, d + 32, a.cabTall));
  return { x0, x1, home: V((x0 + x1) / 2, (n0 + H) / 2, d / 2) };
}
function rail(g, x0, x1, opts = {}) {
  const a = amat(); const y = opts.y ?? 139, z = opts.z ?? 24;
  g.add(bx(x0, y, z - 4, x1, y + 6, z + 4, a.rail, 0.6));
  g.add(bx(x0, y + 1.5, z + 4, x1, y + 2.6, z + 4.4, a.railAccent));
  return { y, z, x0, x1 };
}
// carriage on the rail; lift > 0 adds a telescopic vertical column (Z axis) between carriage and robot base
function carriage(x, y = 139, z = 24, lift = 0) {
  const a = amat(); const g = new THREE.Group();
  g.add(bx(x - 13, y - 6, z - 7, x + 13, y, z + 7, a.rail, 1.0));
  if (lift > 0.5) {
    const outer = Math.min(lift, 22);
    g.add(bx(x - 5.5, y - 6 - outer, z - 5.5, x + 5.5, y - 6, z + 5.5, a.rail, 0.8));
    g.add(bx(x - 4.2, y - 6 - lift, z - 4.2, x + 4.2, y - 6 - outer + 0.5, z + 4.2, a.steel, 0.5));
    g.add(bx(x - 7, y - 7 - lift, z - 7, x + 7, y - 6 - lift, z + 7, a.rail, 0.5));
  }
  return g;
}

// ---------------------------------------------------------------- robot (inverted on rail, or on a pedestal)
function gripper() {
  const g = new THREE.Group(); const a = amat();
  const body = rbox(7.5, 7, 5, 1.2, MAT.graphite); body.position.y = 3.5; g.add(body);
  const cam = rbox(3.6, 2.2, 2.4, 0.6, MAT.graphite2); cam.position.set(0, 4.5, 3.6); g.add(cam);
  const lens = cyl(0.7, 0.6, new THREE.MeshStandardMaterial({ color: 0x0b0d10, roughness: 0.2 }), 16); lens.rotation.x = Math.PI / 2; lens.position.set(0, 4.5, 4.9); g.add(lens);
  for (const s of [-1, 1]) { const f = rbox(1.4, 9, 3.2, 0.5, MAT.white); f.position.set(s * 2.6, 11, 0); g.add(f);
    const pad = rbox(0.6, 4, 2.8, 0.25, MAT.graphite2); pad.position.set(s * 1.75, 13.5, 0); g.add(pad); }
  return g;
}
export function makeRobot(scale = 1.0) {
  const r = buildCobot('A'); r.scale.setScalar(scale);
  const gr = gripper(); r.userData.flange.add(gr);
  const tcp = new THREE.Object3D(); tcp.position.y = 14; r.userData.flange.add(tcp); r.userData.tcp = tcp;
  r.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } });
  return r;
}
// orientation: tool axis (flange +Y) along `dir`, flange +X roughly along `side`
function poseMat(tcpPos, dir, side, tcpLen) {
  const y = dir.clone().normalize(); let x = side.clone().sub(y.clone().multiplyScalar(side.dot(y))).normalize();
  const z = new THREE.Vector3().crossVectors(x, y).normalize(); x = new THREE.Vector3().crossVectors(y, z).normalize();
  const m = new THREE.Matrix4().makeBasis(x, y, z); m.setPosition(tcpPos.clone().sub(y.clone().multiplyScalar(tcpLen)));
  return m;
}
let SEEDS = null;
function seeds() {
  if (SEEDS) return SEEDS;
  SEEDS = [];
  for (const a of [-2.6, -1.6, -0.6, 0.4, 1.4, 2.4]) for (const b of [0.3, 0.9, 1.5]) for (const c of [0.9, 1.7]) SEEDS.push([a, b, c, 0.6, 0, 0]);
  return SEEDS;
}
// IK with collision-aware seed selection: among reachable solutions, prefer the one with the least penetration into furniture
export function reach(robot, tcpPos, dir, side, q0, opts = {}) {
  const tcpLen = 14 * robot.scale.x;
  const T = poseMat(tcpPos, dir, side, tcpLen);
  const all = opts.obstacles ? q0.concat(seeds()) : q0;
  let best = null;
  for (const qs of all) {
    const r = solveIK(robot, T, qs, opts.obstacles ? 400 : 500);
    const okReach = r.posErr < 2 && r.rotErr < 0.08;
    let pen = 0, hits = [];
    if (opts.obstacles && okReach) { const P = penetration(robotCapsules(robot), opts.obstacles); pen = P.total; hits = P.hits; }
    const score = r.posErr + r.rotErr * 10 + (okReach ? pen * 4 : 1000);
    if (!best || score < best.score) best = { ...r, pen, hits, score };
    if (r.posErr < 0.6 && r.rotErr < 0.02 && pen < 0.05) break;
  }
  if (opts.obstacles && best.pen > 0.05 && best.posErr < 2) {
    let rng = 12345;
    const rnd = () => { rng = (rng * 1103515245 + 12345) % 2147483648; return rng / 2147483648 - 0.5; };
    let cur = best;
    for (let t = 0; t < (opts.refine ?? 80); t++) {
      const amp = 0.9 * (1 - t / 100);
      const q1 = cur.q.map((v, i) => v + rnd() * amp * (i < 3 ? 1.2 : 1.6));
      const r = solveIK(robot, T, q1, 250);
      if (r.posErr > 1 || r.rotErr > 0.04) continue;
      const P = penetration(robotCapsules(robot), opts.obstacles);
      const score = r.posErr + r.rotErr * 10 + P.total * 4;
      if (score < cur.score) { cur = { ...r, pen: P.total, hits: P.hits, score }; if (P.total < 0.05) break; }
    }
    best = cur;
  }
  setJoints(robot, best.q);
  return best;
}

// ---------------------------------------------------------------- people / furniture / zones
export function human(x, z, rotY = 0, scale = 1) {
  const a = amat(); const g = new THREE.Group(); g.position.set(x, 0, z); g.rotation.y = rotY; g.scale.setScalar(scale);
  for (const s of [-1, 1]) { const leg = new THREE.Mesh(new THREE.CapsuleGeometry(6.2, 70, 6, 16), a.human); leg.position.set(s * 8, 42, 0); leg.castShadow = true; g.add(leg); }
  const torso = new THREE.Mesh(new THREE.CapsuleGeometry(15, 40, 8, 20), a.human); torso.scale.set(1, 1, 0.62); torso.position.y = 112; torso.castShadow = true; g.add(torso);
  for (const s of [-1, 1]) { const arm = new THREE.Mesh(new THREE.CapsuleGeometry(4.6, 52, 6, 12), a.human); arm.position.set(s * 21, 108, 4); arm.rotation.x = -0.25; arm.castShadow = true; g.add(arm); }
  const head = new THREE.Mesh(new THREE.SphereGeometry(10.5, 24, 18), a.human); head.position.y = 158; head.castShadow = true; g.add(head);
  return g;
}
function table(g, x0, z0, x1, z1, opts = {}) {
  const a = amat(); const h = 73;
  g.add(bx(x0, h - 3, z0, x1, h, z1, a.wood));
  for (const [x, z] of [[x0 + 5, z0 + 5], [x1 - 5, z0 + 5], [x0 + 5, z1 - 5], [x1 - 5, z1 - 5]]) g.add(bx(x - 2, 0, z - 2, x + 2, h - 3, z + 2, a.wood));
  if (opts.chairs !== false) {
    const cw = 42; const n = Math.max(1, Math.floor((x1 - x0) / 75));
    for (let i = 0; i < n; i++) { const cx = x0 + (i + 0.5) * (x1 - x0) / n;
      for (const [zz, s] of [[z0 - 22, -1], [z1 + 22, 1]]) { g.add(bx(cx - cw / 2, 43, zz - 20, cx + cw / 2, 46, zz + 20, a.chair)); g.add(bx(cx - cw / 2, 46, zz + s * 18, cx + cw / 2, 88, zz + s * 21, a.chair));
        for (const [ox, oz] of [[-17, -16], [17, -16], [-17, 16], [17, 16]]) g.add(bx(cx + ox - 1.2, 0, zz + oz - 1.2, cx + ox + 1.2, 43, zz + oz + 1.2, a.chair)); } }
  }
}
function zone(g, kind, x0, z0, x1, z1, y = 0.6) {
  const a = amat();
  if (kind === 'robot') { g.add(plane(x0, z0, x1, z1, y, a.zoneRobot)); outline(g, x0, z0, x1, z1, y + 0.2, 1.6, a.path, false); }
  else if (kind === 'human') { g.add(plane(x0, z0, x1, z1, y, a.zoneHuman)); outline(g, x0, z0, x1, z1, y + 0.2, 1.6, new THREE.MeshBasicMaterial({ color: 0x5c6670 }), true); }
  else { const m = a.zoneNoGo.clone(); m.map = a.hatch.clone(); m.map.needsUpdate = true; m.map.repeat.set((x1 - x0) / 60, (z1 - z0) / 60);
    g.add(plane(x0, z0, x1, z1, y + 0.1, m)); outline(g, x0, z0, x1, z1, y + 0.3, 1.6, new THREE.MeshBasicMaterial({ color: 0x3a3f46 }), false); }
}
function reachVolume(g, x0, x1, z0, z1, y0, y1) {
  const a = amat(); const m = bx(x0, y0, z0, x1, y1, z1, a.reach); m.castShadow = false; m.receiveShadow = false; g.add(m);
  const e = edges(m, a.edgeOrange); g.add(e);
  return m;
}
function pathCurve(g, pts, y = null, dash = 6, gap = 4, r = 0.7) {
  const a = amat(); const curve = new THREE.CatmullRomCurve3(pts.map(p => p.clone())); const L = curve.getLength();
  let s = 0;
  while (s < L) { const s1 = Math.min(L, s + dash); const sub = []; for (let k = 0; k <= 6; k++) sub.push(curve.getPointAt((s + (s1 - s) * k / 6) / L));
    const tube = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(sub), 6, r, 8, false), a.path); g.add(tube); s = s1 + gap; }
  const end = curve.getPointAt(1), tan = curve.getTangentAt(1);
  const head = new THREE.Mesh(new THREE.ConeGeometry(2.4, 6, 16), a.path); head.position.copy(end); head.quaternion.setFromUnitVectors(V(0, 1, 0), tan); g.add(head);
}
function visionCone(g, apex, target, radius = 30) {
  const a = amat(); const dir = target.clone().sub(apex); const L = dir.length();
  const cone = new THREE.Mesh(new THREE.ConeGeometry(radius, L, 4, 1, true), a.cone);
  cone.position.copy(apex.clone().add(dir.clone().multiplyScalar(0.5)));
  cone.quaternion.setFromUnitVectors(V(0, -1, 0), dir.clone().normalize()); cone.rotateY(Math.PI / 4); g.add(cone);
  const e = new THREE.LineSegments(new THREE.EdgesGeometry(cone.geometry), a.edgeOrange); e.position.copy(cone.position); e.quaternion.copy(cone.quaternion); g.add(e);
}
function detectBox(g, center, w, h, d) {
  const a = amat(); const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d)); m.position.copy(center);
  const e = edges(m, a.edgeOrange); g.add(e);
}

// ---------------------------------------------------------------- ARKI linear kitchen (3Bay standard: Rail architecture)
// Back wall z = 0, run from x0, total 360 cm: garage tall 44 | counter | sink 80 | counter | IH 60 | tall DW+storage 60
export function arkiLinearKitchen(g, x0 = 0, opts = {}) {
  const a = amat();
  const xg = x0, xc0 = x0 + 44, xs = x0 + 170, xi = x0 + 268, xt = x0 + 300, xe = x0 + 360;
  const gar = garageTall(g, xg);
  baseRun(g, xc0, xt, { doorW: 64 });
  const sk = sink(g, xs, { w: 80 });
  counter(g, xc0, xt, { holes: [[sk.x0, sk.x1, 10, 52]] });
  // cooktop stays off the robot run (heat source = No-go); opts.ihOnRun only for the ordinary 'before' style
  let ih = opts.ihOnRun ? induction(g, xi, { w: 56 }) : null;
  backsplash(g, xc0, xt);
  upperRun(g, xc0, xt, { doorW: 64 });
  const tall = tallDW(g, xt, opts.tall || {});
  const rl = rail(g, xg + 4, xt - 2);
  // ㄱ return along the left wall carrying the cooktop + hood (human zone, beyond the rail end)
  let ret = null;
  if (opts.ret) {
    const wx = opts.ret.wallX ?? (x0 - 40), z0 = 62, L = opts.ret.len ?? 180;
    const sg = new THREE.Group(); sg.rotation.y = Math.PI / 2; sg.position.set(wx, 0, z0 + L); g.add(sg);   // local x -> world -z, local z -> world +x
    baseRun(sg, 0, L, { doorW: 60 }); counter(sg, 0, L, {}); induction(sg, L / 2, { w: 56 }); backsplash(sg, 0, L);
    sg.add(bx(L / 2 - 32, 158, 0, L / 2 + 32, 170, 46, a.cabTall)); sg.add(bx(L / 2 - 14, 170, 0, L / 2 + 14, 240, 26, a.cabTall));   // hood
    if (wx < x0) g.add(bx(wx, 0, 0, x0, 225, 60, a.cabTall));                                       // filler tall between wall and garage
    ih = { center: V(wx + 30, 88.2, z0 + L / 2) };
    ret = { x0: wx, x1: wx + 62, z0, z1: z0 + L, ihz0: z0 + L / 2 - 30, ihz1: z0 + L / 2 + 30 };
  }
  // dishes: dirty ones on the counter next to the sink, clean ones in the racks / storage
  const dishes = [];
  if (opts.dirty !== false) {
    const p1 = plate(12.5); p1.position.set(xc0 + 34, 88.2, 32); g.add(p1); dishes.push(p1);
    const p2 = plate(12.5, a.ceramicB); p2.position.set(xc0 + 34, 90.6, 32); g.add(p2); dishes.push(p2);
    const b1 = bowl(6.5, 6, a.ceramic); b1.position.set(xc0 + 63, 88.2, 22); g.add(b1); dishes.push(b1);
    const b2 = bowl(8, 7, a.ceramicG); b2.position.set(xc0 + 66, 88.2, 44); g.add(b2); dishes.push(b2);
    const c1 = cup(); c1.position.set(xc0 + 12, 88.2, 18); g.add(c1); dishes.push(c1);
  }
  // clean plates standing in the lower rack + bowls in the upper rack + storage contents
  const lr = tall.racks[0];
  for (let i = 0; i < (opts.rackPlates ?? 5); i++) { const p = plate(11); p.rotation.set(0, 0, Math.PI / 2); p.position.set(-14 + i * 4, 11, 4); lr.add(p); }
  const ur = tall.racks[1];
  for (let i = 0; i < 3; i++) { const b = bowl(6, 5.5); b.rotation.x = Math.PI; b.position.set(-12 + i * 12, 6.5, -2); ur.add(b); }
  const st = tall.storage;
  for (let i = 0; i < (opts.stPlates ?? 4); i++) { const p = plate(11); p.rotation.set(Math.PI / 2, 0, 0); p.position.set(-12, 12.4, -14 + i * 5); st.add(p); }
  for (let i = 0; i < 2; i++) { const b = bowl(6, 5.5); b.position.set(10, 1.2 + i * 2.2, -6); st.add(b); }
  return { gar, sk, ih, tall, rl, dishes, ret, xg, xc0, xs, xi, xt, xe };
}

// ---------------------------------------------------------------- ARKI robot run v2 (collision-checked layout)
// Back wall z = 0. Left -> right: robot garage on the counter | drop zone | sink | dish drawer | dishwasher (under counter, optional raise)
// The robot hangs from a rail under the upper cabinets and only ever works IN FRONT of / ABOVE the units it serves,
// so no link has to cross a cabinet side panel (the failure mode of the v1 tall-unit layout).
function _underDW(g, x0, opts = {}) {
  const a = amat(); const w = 60, d = 57, raise = opts.raise ?? 0;
  const x1 = x0 + w, y0 = 10 + raise, y1 = 82 + raise;          // DW body
  const open = opts.open ?? 1, rackL = opts.rackL ?? 1, rackU = opts.rackU ?? 0.85;
  // carcass + cavity
  g.add(bx(x0, 0, 0, x1, 10, d - 5, a.dark));
  if (raise > 0) g.add(bx(x0 + 0.5, 10, 0, x1 - 0.5, y0, d - 1, a.cabLower));   // raise plinth / drawer front
  g.add(bx(x0, y0, 0, x0 + 1.5, y1, d, a.dwIn)); g.add(bx(x1 - 1.5, y0, 0, x1, y1, d, a.dwIn));
  g.add(bx(x0, y1 - 1.5, 0, x1, y1, d, a.dwIn)); g.add(bx(x0, y0, 0, x1, y0 + 1.2, d, a.dwIn)); g.add(bx(x0, y0, 0, x1, y1, 1.2, a.dwIn));
  // door hinged at the bottom front, opened down to horizontal
  const door = new THREE.Group(); door.position.set((x0 + x1) / 2, y0 + 0.5, d); door.rotation.x = open * 88 * D; g.add(door);
  door.add(bx(-(w / 2 - 0.4), 0, -1.6, w / 2 - 0.4, y1 - y0 + 2, 0.6, a.cabLower));
  door.add(bx(-(w / 2 - 4), 3, 0.6, w / 2 - 4, y1 - y0 - 3, 1.6, a.dwIn));
  // racks (not obstacles: they are the target)
  const obPrev = OB.on; OB.on = false;
  const racks = [];
  for (const [ry, out] of [[y0 + 4, rackL * (opts.rackOutL ?? 44)], [y0 + 38, rackU * (opts.rackOutU ?? 44)]]) {
    const r = new THREE.Group(); r.position.set((x0 + x1) / 2, ry, d / 2 + out); g.add(r);
    const rw = w - 8, rd = d - 8;
    for (const [p, q, s2, t] of [[-rw / 2, -rd / 2, rw / 2, -rd / 2], [rw / 2, -rd / 2, rw / 2, rd / 2], [rw / 2, rd / 2, -rw / 2, rd / 2], [-rw / 2, rd / 2, -rw / 2, -rd / 2]]) {
      const L = Math.hypot(s2 - p, t - q); const bar = cyl(0.35, L, a.rack, 8); bar.rotation.z = Math.PI / 2; bar.rotation.y = -Math.atan2(t - q, s2 - p);
      bar.position.set((p + s2) / 2, 0, (q + t) / 2); r.add(bar); const b2 = bar.clone(); b2.position.y = 9; r.add(b2); }
    for (let i = -rw / 2 + 4; i <= rw / 2 - 4; i += 4) { const tine = cyl(0.25, rd, a.rack, 6); tine.rotation.x = Math.PI / 2; tine.position.set(i, 0, 0); r.add(tine); }
    racks.push(r);
  }
  OB.on = obPrev;
  return { x0, x1, d, y0, y1, racks, door, raise };
}
function underDW(...a) { return obst('dw', () => _underDW(...a)); }

// deep dish drawer (motorised push-to-open), front 60 wide, pulled out by `out`
function _dishDrawer(g, x0, w = 60, opts = {}) {
  const a = amat(); const y0 = opts.y0 ?? 40, y1 = opts.y1 ?? 70, out = opts.out ?? 1;
  const dr = new THREE.Group(); dr.position.set(x0 + w / 2, 0, out * 48); g.add(dr);
  const obPrev = OB.on; OB.on = false;          // the open drawer box is the target, its front panel stays an obstacle
  dr.add(bx(-(w / 2 - 3), y0, 6, w / 2 - 3, y0 + 1.2, 56, a.cabInside));
  dr.add(bx(-(w / 2 - 3), y0, 6, -(w / 2 - 4.4), y1 - 4, 56, a.cabInside)); dr.add(bx(w / 2 - 4.4, y0, 6, w / 2 - 3, y1 - 4, 56, a.cabInside));
  dr.add(bx(-(w / 2 - 3), y0, 6, w / 2 - 3, y1 - 4, 7.4, a.cabInside));
  for (let i = 0; i < 6; i++) { const peg = cyl(0.6, 9, a.steelDark, 8); peg.position.set(-18 + i * 7.2, y0 + 5, 30); dr.add(peg); }
  OB.on = obPrev;
  dr.add(bx(-(w / 2 - 0.3), y0 - 2, 56, w / 2 - 0.3, y1 + 1, 58, a.cabLower));
  return { group: dr, x0, x1: x0 + w, y0, y1, out };
}
function dishDrawer(...a) { return obst('drawer', () => _dishDrawer(...a)); }

// robot garage standing on the counter (appliance-garage type), W45 x D62, counter top to the top of the upper cabinets.
// Right side below the upper-cabinet line (passY = 145) is the robot's passage onto the rail.
// Door: one hinged wrap-around door (front leaf + 15 cm return covering the front of the passage), hinge on the
// front-left edge, opens out to 105 deg. It opens for every exit/entry: the folded arm needs the room in front of the
// garage to swing down below the rail level before it turns toward the run.
function _counterGarage(g, x0, w = 45, opts = {}) {
  const a = amat(); const x1 = x0 + w, d = opts.d ?? 62, y0 = 88.2, y1 = 225, open = opts.open ?? 0;
  const pY = opts.passY ?? 145, ret = opts.ret ?? 15, t = 1.8;
  g.add(bx(x0, y0, 0, x0 + t, y1, d - t, a.cabTall));                         // left side
  g.add(bx(x1 - t, pY, 0, x1, y1, d - t - ret, a.cabTall));                   // right side above the passage
  g.add(bx(x0, y1 - 2, 0, x1, y1, d - t, a.cabTall));                         // top
  g.add(bx(x0, y0, 0, x1, y1, 1.2, a.homeBack));                              // back
  const door = new THREE.Group(); door.position.set(x0, y0, d); door.rotation.y = -open * 105 * D; g.add(door);
  door.add(bx(0.2, 0.3, -t, w, y1 - y0 - 0.3, 0, a.cabTall));                 // front leaf
  door.add(bx(w - t, 0.3, -t - ret, w, y1 - y0 - 0.3, -t, a.cabTall));        // return leaf (right side, front 15 cm)
  return { x0, x1, d, y0, y1, passY: pY, ret, door, home: V((x0 + x1) / 2, 125, 26) };
}
function counterGarage(...a) { return obst('garage', () => _counterGarage(...a)); }

export function arkiRunV2(g, x0 = 0, opts = {}) {
  const a = amat();
  const GW = opts.gw ?? 45;
  const DZ = opts.drop ?? 80;      // drop-zone width (cm)
  const xg = x0, xz = x0 + GW, xs = xz + DZ + 40, xd = xz + DZ + 80, xw = xz + DZ + 140, xe = xz + DZ + 200;   // garage | drop | sink 80 | drawer 60 | DW 60
  const raise = opts.raise ?? 0;
  baseRun(g, xg, xz, { doorW: GW });
  baseRun(g, xz, xd, { doorW: 60 });
  // drawer cabinet: carcass with the deep drawer opening
  obst('base', () => { g.add(bx(xd, 0, 0, xd + 60, 10, 53, a.dark)); g.add(bx(xd, 10, 0, xd + 60, 38, 56, a.cabLower)); g.add(bx(xd, 72, 0, xd + 60, 85, 56, a.cabLower));
    g.add(bx(xd, 38, 0, xd + 1.5, 72, 56, a.cabLower)); g.add(bx(xd + 58.5, 38, 0, xd + 60, 72, 56, a.cabLower)); g.add(bx(xd, 38, 0, xd + 60, 72, 2, a.cabLower)); });
  const dr = dishDrawer(g, xd, 60, { y0: 40, y1: 70, out: opts.drawerOut ?? 1 });
  const dw = underDW(g, xw, { raise, open: opts.dwOpen ?? 1, rackL: opts.rackL ?? 1, rackU: opts.rackU ?? 0.85 });
  const sk = sink(g, xs, { w: 76 });
  const ctop = raise > 0 ? xw : xe;
  counter(g, xg, ctop, { holes: [[sk.x0, sk.x1, 10, 52]] });
  if (raise > 0) counter(g, xw, xe, { y: 85 + raise });
  backsplash(g, xz, xe); upperRun(g, xz, xe, { doorW: 60 });
  const gar = counterGarage(g, xg, GW, { open: (opts.garageOpen ?? 0) * (opts.garageAngle ?? 105) / 105 });
  const rl = rail(g, xg + 6, xe - 4, { z: opts.railZ ?? 24 });
  const dishes = [];
  if (opts.dirty !== false) {
    const p1 = plate(12.5); p1.position.set(xz + 30, 88.2, 32); g.add(p1); dishes.push(p1);
    const p2 = plate(12.5, a.ceramicB); p2.position.set(xz + 30, 90.6, 32); g.add(p2); dishes.push(p2);
    const b1 = bowl(6.5, 6, a.ceramic); b1.position.set(xz + 58, 88.2, 22); g.add(b1); dishes.push(b1);
    const b2 = bowl(8, 7, a.ceramicG); b2.position.set(xz + 62, 88.2, 44); g.add(b2); dishes.push(b2);
    const c1 = cup(); c1.position.set(xz + 10, 88.2, 18); g.add(c1); dishes.push(c1);
  }
  let ret = null, ih = null;
  if (opts.ret) {
    const wx = opts.ret.wallX ?? (x0 - 40), z0 = 64, L = opts.ret.len ?? 180;
    const sg = new THREE.Group(); sg.rotation.y = Math.PI / 2; sg.position.set(wx, 0, z0 + L); g.add(sg);
    baseRun(sg, 0, L, { doorW: 60 }); counter(sg, 0, L, {}); induction(sg, L / 2, { w: 56 }); backsplash(sg, 0, L);
    sg.add(bx(L / 2 - 32, 158, 0, L / 2 + 32, 170, 46, a.cabTall)); sg.add(bx(L / 2 - 14, 170, 0, L / 2 + 14, 240, 26, a.cabTall));
    if (wx < x0) g.add(bx(wx, 0, 0, x0, 225, 62, a.cabTall));
    ih = { center: V(wx + 30, 88.2, z0 + L / 2) };
    ret = { x0: wx, x1: wx + 62, z0, z1: z0 + L, ihz0: z0 + L / 2 - 30, ihz1: z0 + L / 2 + 30 };
  }
  const [lr, ur] = dw.racks;
  for (let i = 0; i < (opts.rackPlates ?? 5); i++) { const p = plate(11); p.rotation.set(0, 0, Math.PI / 2); p.position.set(-14 + i * 4, 11, 4); lr.add(p); }
  for (let i = 0; i < 3; i++) { const b = bowl(6, 5.5); b.rotation.x = Math.PI; b.position.set(-12 + i * 12, 6.5, -2); ur.add(b); }
  for (let i = 0; i < (opts.drawerPlates ?? 4); i++) { const p = plate(11); p.rotation.set(Math.PI / 2, 0, 0); p.position.set(-8, 40 + 11.5, 22 + i * 4.6); dr.group.add(p); }
  return { v2: true, gar, sk, dw, dr, rl, dishes, ret, ih, xg, xz, xs, xd, xw, xe, xc0: xz, xt: xw, raise, drop: DZ };
}

// task poses for the v2 run (local frame of the run group)
function taskPoseV2(k, task) {
  const dn = V(0, -1, 0), dw = k.dw, dr = k.dr;
  const dwx = (dw.x0 + dw.x1) / 2, rl = dw.racks[0].position, ru = dw.racks[1].position;
  switch (task) {
    case 'detect': return { car: k.xz + 70, tcp: V(k.xz + 40, 122, 44), dir: V(-0.35, -1, 0.1), side: V(0, 0, 1) };
    case 'pick': return { car: k.xz + 60, tcp: V(k.xz + 30 + 12.5, 95.5, 32), dir: dn, side: V(0, 0, 1), hold: null };
    case 'load': return { car: dwx, tcp: V(dwx + 2, rl.y + 11 + 12, rl.z + 4), dir: dn, side: V(1, 0, 0), hold: 'plateV' };
    case 'unload': return { car: dwx - 6, tcp: V(dwx - 6, ru.y + 15, ru.z - 2), dir: V(0.1, -1, 0.15), side: V(1, 0, 0), hold: 'bowl' };
    case 'store': return { car: (dr.x0 + dr.x1) / 2, tcp: V((dr.x0 + dr.x1) / 2 - 8, dr.y0 + 11.5 + 13, dr.out * 48 + 22 + 2 * 4.6), dir: V(0, -1, 0), side: V(1, 0, 0), hold: 'plateV' };
    case 'hero': return { car: k.xs + 20, tcp: V(k.xs + 70, 104, 64), dir: V(0.25, -1, 0.3), side: V(1, 0, 0), hold: 'plateV' };
    case 'park': { const gx = (k.gar.x0 + k.gar.x1) / 2; return { car: gx, parkCands: [
      [V(gx, 182, 45), V(0, 1, 0), V(1, 0, 0)], [V(gx + 8, 176, 46), V(0, 1, 0), V(0, 0, 1)], [V(gx - 8, 178, 44), V(0, 1, 0), V(1, 0, 0)],
      [V(gx, 168, 47), V(0, 0, -1), V(1, 0, 0)], [V(gx, 190, 40), V(0, 1, 0), V(0, 0, -1)], [V(gx + 6, 160, 48), V(-1, 0, 0), V(0, 1, 0)],
      [V(gx + 14, 104, 34), V(-1, 0, 0), V(0, 1, 0)], [V(gx - 14, 104, 34), V(1, 0, 0), V(0, 1, 0)], [V(gx, 100, 40), V(0, 0, -1), V(1, 0, 0)],
      [V(gx + 10, 98, 30), V(0, 1, 0), V(1, 0, 0)], [V(gx, 104, 24), V(0, 0, 1), V(1, 0, 0)], [V(gx - 10, 98, 34), V(0, 1, 0), V(0, 0, 1)]] }; }
    case 'travel': { const cx = k.gar.x1 + 34; return { car: cx, parkCands: [
      [V(cx + 4, 104, 52), V(0, -1, 0), V(1, 0, 0)], [V(cx + 10, 108, 50), V(0, -1, 0.3), V(1, 0, 0)], [V(cx - 6, 106, 54), V(0, -1, 0), V(0, 0, 1)],
      [V(cx + 14, 112, 48), V(1, -1, 0), V(0, 0, 1)], [V(cx, 110, 56), V(0, -0.6, 1), V(1, 0, 0)]] }; }
    default: return { car: k.xs + 40, tcp: V(k.xs + 62, 118, 52), dir: V(0.1, -1, 0.2), side: V(1, 0, 0), hold: 'plateV' };
  }
}

// ---------------------------------------------------------------- stow / deploy planning (v2 run)
// Park pose inside the garage (door closed) -> door opens -> collision-free joint path (RRT-Connect + shortcut)
// to a compact travel pose under the rail -> carriage runs out through the side passage.
// Every configuration is checked against the furniture boxes, the rail + carriage, robot self-collision and the
// dishes left on the drop zone.
function lcg(seed) { let r = seed >>> 0; return () => { r = (r * 1103515245 + 12345) % 2147483648; return r / 2147483648; }; }
const JW = [1.5, 1.5, 1.2, 0.7, 0.6, 0.2];
const jdist = (p, q) => { let s = 0; for (let i = 0; i < 6; i++) { const d = (p[i] - q[i]) * JW[i]; s += d * d; } return Math.sqrt(s); };
function edgeValid(p, q, valid, res = 0.03) {
  const n = Math.max(1, Math.ceil(Math.max(...p.map((v, i) => Math.abs(q[i] - v))) / res));
  for (let s = 1; s <= n; s++) { const t = s / n; if (!valid(p.map((v, i) => v + (q[i] - v) * t))) return false; }
  return true;
}
function rrtConnect(qa, qb, valid, rnd, lo, hi, opts = {}) {
  const step = opts.step ?? 0.14, maxIt = opts.maxIt ?? 5000;
  const steer = (p, q) => { const m = Math.max(...p.map((v, i) => Math.abs(q[i] - v))); if (m <= step) return q.slice(); return p.map((v, i) => v + (q[i] - v) * step / m); };
  const nearest = (T, q) => { let bi = 0, bd = 1e9; for (let i = 0; i < T.length; i++) { const d = jdist(T[i].q, q); if (d < bd) { bd = d; bi = i; } } return bi; };
  const A = [{ q: qa.slice(), p: -1 }], B = [{ q: qb.slice(), p: -1 }];
  const extend = (T, q) => { const i = nearest(T, q); const qn = steer(T[i].q, q); if (!edgeValid(T[i].q, qn, valid)) return -1; T.push({ q: qn, p: i }); return T.length - 1; };
  const connect = (T, q) => { for (let k = 0; k < 400; k++) { const i = nearest(T, q); const qn = steer(T[i].q, q); if (!edgeValid(T[i].q, qn, valid)) return -1; T.push({ q: qn, p: i }); if (Math.max(...qn.map((v, j) => Math.abs(q[j] - v))) < 1e-9) return T.length - 1; } return -1; };
  let Ta = A, Tb = B, swapped = false;
  for (let it = 0; it < maxIt; it++) {
    const qr = rnd() < 0.08 ? (swapped ? qa : qb).slice() : lo.map((l, i) => l + rnd() * (hi[i] - l));
    const ia = extend(Ta, qr);
    if (ia >= 0) {
      const ib = connect(Tb, Ta[ia].q);
      if (ib >= 0) {
        const pa = []; for (let i = ia; i >= 0; i = Ta[i].p) pa.unshift(Ta[i].q);
        const pb = []; for (let i = ib; i >= 0; i = Tb[i].p) pb.push(Tb[i].q);
        const path = pa.concat(pb.slice(1)); if (swapped) path.reverse();
        return { path, nodes: A.length + B.length, it };
      }
    }
    [Ta, Tb] = [Tb, Ta]; swapped = !swapped;
  }
  return null;
}
function shortcut(path, valid, rnd, iters = 300) {
  let P = path.map(q => q.slice());
  for (let k = 0; k < iters && P.length > 2; k++) {
    const i = Math.floor(rnd() * (P.length - 2)), j = i + 2 + Math.floor(rnd() * (P.length - i - 2));
    if (j >= P.length) continue;
    if (edgeValid(P[i], P[j], valid)) P = P.slice(0, i + 1).concat(P.slice(j));
  }
  return P;
}
// gC/kC: run with the garage door closed; gO/kO: the same run with the door open
export function planStow(gC, kC, gO, kO, opts = {}) {
  const t0 = performance.now();
  gC.updateMatrixWorld(true); gO.updateMatrixWorld(true);
  const k = kO, gar = k.gar, gx = (gar.x0 + gar.x1) / 2 + (opts.parkDx ?? 0), yb = k.rl.y - 6, rz = k.rl.z;
  const xEnd = opts.xEnd ?? (gar.x1 + 12);                    // robot fully out of the passage
  const obsOf = (g, kk) => { const o = collectObstacles(g).filter(b => b.max.x > gar.x0 - 10 && b.min.x < xEnd + 90);
    for (const d of (kk.dishes || [])) { const b = new THREE.Box3().setFromObject(d); b.userData = { name: 'dish' }; o.push(b); } return o; };
  const obsC = obsOf(gC, kC), obsO = obsOf(gO, kO);
  const robot = makeRobot(1.0); robot.rotation.x = Math.PI;
  const railBox = new THREE.Box3(V(k.rl.x0, k.rl.y, rz - 4), V(k.rl.x1, k.rl.y + 6, rz + 4.4));
  const carBox = (cx) => new THREE.Box3(V(cx - 13, k.rl.y - 6, rz - 7), V(cx + 13, k.rl.y, rz + 7));
  const put = (cx, q) => { robot.position.set(cx, yb, rz); setJoints(robot, q); return robotCapsules(robot); };
  const cost = (obs, cx, q, detail = false) => {
    const caps = put(cx, q);
    const P = penetration(caps, obs);
    const R = penetration(caps.filter(c => c.link !== -1 && c.link !== 0), [railBox, carBox(cx)]);
    const S = selfPenetration(caps);
    const tot = P.total + R.total + S.total;
    return detail ? { tot: +tot.toFixed(3), hits: P.hits, rail: R.hits, self: S.hits, b: capsuleBounds(caps) } : tot;
  };
  const rnd = lcg(opts.seed ?? 4242);
  const lo = [-1.25 * Math.PI, -3.8, -2.8, -1.1 * Math.PI, -1.1 * Math.PI, 0], hi = [1.25 * Math.PI, 3.8, 2.8, 1.1 * Math.PI, 1.1 * Math.PI, 0];
  const sample = () => lo.map((l, i) => l + rnd() * (hi[i] - l));
  const boundsOf = (cx, q) => capsuleBounds(put(cx, q));
  // admissibility measures (cm, 0 = admissible)
  const overPark = (b) => Math.max(0, gar.x0 + 2.2 - b.xmin) + Math.max(0, b.xmax - (gar.x1 - 2.2)) + Math.max(0, b.zmax - (gar.d - 2.4 - (gar.ret ?? 0) * 0)) + Math.max(0, 1.6 - b.zmin) + Math.max(0, b.ymax - (gar.y1 - 2.5));
  const yMin = opts.yMin ?? 98.2, yCap = gar.passY - 0.8, zCap = opts.zCap ?? 56, xLen = opts.xLen ?? 62;
  const overTrav = (b) => Math.max(0, 2.5 - b.zmin) + Math.max(0, b.zmax - zCap) + Math.max(0, yMin - b.ymin) + Math.max(0, b.ymax - yCap) + Math.max(0, b.xmax - b.xmin - xLen);
  const xsQuick = [gx, gar.x1 - 6, gar.x1 + 4, xEnd];
  const fPark = (q) => { const o = overPark(boundsOf(gx, q)); return o > 6 ? 6 + o : o + cost(obsC, gx, q); };
  const fTrav = (q) => { const o = overTrav(boundsOf(gx, q)); if (o > 6) return 6 + o; let c = o; for (const cx of xsQuick) c += cost(obsO, cx, q); return c; };
  const climb = (q0, f, iters, amp0) => {
    let q = q0.slice(), fq = f(q);
    for (let t = 0; t < iters && fq > 0.01; t++) {
      const amp = amp0 * (1 - t / iters) + 0.04;
      const q1 = q.map((v, i) => i === 5 ? 0 : Math.max(lo[i], Math.min(hi[i], v + (rnd() * 2 - 1) * amp)));
      const f1 = f(q1); if (f1 < fq) { q = q1; fq = f1; }
    }
    return { q, f: fq };
  };
  const biased = (q0s) => { const q = sample(); if (rnd() < 0.7) q[0] = q0s[Math.floor(rnd() * q0s.length)] + (rnd() * 2 - 1) * 0.35; return q; };
  const parkScore = (b) => (b.xmax - b.xmin) * 0.3 + (b.zmax - b.zmin) * 0.6 - b.ymin * 0.8;
  const travScore = (b) => (b.zmax - b.zmin) + (b.ymax - b.ymin) * 0.5 + (b.xmax - b.xmin) * 0.25;
  const parks = [], travs = [];
  for (let r = 0; r < (opts.nPark ?? 60) && parks.length < (opts.wantPark ?? 8); r++) {
    const R = climb(biased([0, Math.PI, -Math.PI, Math.PI / 2, -Math.PI / 2]), fPark, opts.iters ?? 500, 0.8);
    if (R.f <= 0.01 && cost(obsO, gx, R.q) <= 0.01) { const b = boundsOf(gx, R.q); parks.push({ q: R.q, b, score: parkScore(b) }); }
  }
  for (let r = 0; r < (opts.nTravel ?? 80) && travs.length < (opts.wantTravel ?? 8); r++) {
    const R = climb(biased([Math.PI / 2, -Math.PI / 2]), fTrav, opts.iters ?? 500, 0.8);
    if (R.f <= 0.01) { const b = boundsOf(gx, R.q); travs.push({ q: R.q, b, score: travScore(b) }); }
  }
  parks.sort((p, q) => p.score - q.score); travs.sort((p, q) => p.score - q.score);
  const valid = (q) => cost(obsO, gx, q) <= 0.01;
  const transitWorst = (q, step = 1) => { let w = 0; for (let cx = gx; cx <= xEnd + 0.01; cx += step) { const c = cost(obsO, cx, q); if (c > w) w = c; } return w; };
  const out = { tried: { parks: parks.length, travels: travs.length, rrt: [] }, gx, xEnd };
  let best = null;
  for (const P of parks.slice(0, opts.topPark ?? 4)) { if (best) break;
    for (const T of travs.slice(0, opts.topTravel ?? 4)) {
      if (transitWorst(T.q, 2) > 0.01) continue;
      const R = rrtConnect(P.q, T.q, valid, rnd, lo, hi, { maxIt: opts.maxIt ?? 4000 });
      out.tried.rrt.push(R ? { ok: 1, nodes: R.nodes, it: R.it } : { ok: 0 });
      if (R) { best = { P, T, path: shortcut(R.path, valid, rnd, 400) }; break; }
    }
  }
  if (best) {
    const r4 = (q) => q.map(v => +v.toFixed(4));
    out.qPark = r4(best.P.q); out.qTravel = r4(best.T.q); out.path = best.path.map(r4);
    out.parkBounds = best.P.b; out.travelBounds = best.T.b;
    // independent re-check at finer resolution
    let wPath = 0; for (let i = 1; i < best.path.length; i++) { const a = best.path[i - 1], b2 = best.path[i];
      const n = Math.max(1, Math.ceil(Math.max(...a.map((v, j) => Math.abs(b2[j] - v))) / 0.015));
      for (let s = 0; s <= n; s++) { const c = cost(obsO, gx, a.map((v, j) => v + (b2[j] - v) * s / n)); if (c > wPath) wPath = c; } }
    out.check = { parkDoorClosed: cost(obsC, gx, best.P.q, true), parkDoorOpen: cost(obsO, gx, best.P.q).toFixed(3), pathWorst: +wPath.toFixed(3),
      transitWorst: +transitWorst(best.T.q, 1).toFixed(3), travelAtPassage: cost(obsO, gar.x1, best.T.q, true) };
    // how far the arm reaches out of the garage front while deploying (z of the swept envelope)
    let zMax = -1e9, yMinPath = 1e9; for (const q of best.path) { const bb = boundsOf(gx, q); zMax = Math.max(zMax, bb.zmax); yMinPath = Math.min(yMinPath, bb.ymin); }
    out.sweep = { zMax: +zMax.toFixed(1), yMin: +yMinPath.toFixed(1) };
  } else { out.parks = parks.slice(0, 3).map(p => ({ q: p.q, b: p.b })); out.travels = travs.slice(0, 3).map(p => ({ q: p.q, b: p.b })); }
  out.ms = Math.round(performance.now() - t0);
  return out;
}

// ---------------------------------------------------------------- scenes
function camPersp(W, H, fov, pos, look) {
  const c = new THREE.PerspectiveCamera(fov, W / H, 5, 5000); c.position.copy(pos); c.lookAt(look); c.updateMatrixWorld(); return c;
}
function camOrtho(W, H, span, pos, look) {
  const h = span * H / W; const c = new THREE.OrthographicCamera(-span / 2, span / 2, h / 2, -h / 2, 1, 10000);
  c.position.copy(pos); c.lookAt(look); c.updateMatrixWorld(); return c;
}
// fit an orthographic camera to a world box (keeps the view direction, recentres, pads by `pad` of the frame)
function fitOrtho(cam, box, W, H, pad = 0.06) {
  cam.updateMatrixWorld(); const inv = cam.matrixWorldInverse;
  let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
  for (const x of [box.min.x, box.max.x]) for (const y of [box.min.y, box.max.y]) for (const z of [box.min.z, box.max.z]) {
    const v = V(x, y, z).applyMatrix4(inv); x0 = Math.min(x0, v.x); x1 = Math.max(x1, v.x); y0 = Math.min(y0, v.y); y1 = Math.max(y1, v.y); }
  let w = x1 - x0, h = y1 - y0; const ar = W / H;
  if (w / h > ar) h = w / ar; else w = h * ar;
  w *= 1 + 2 * pad; h *= 1 + 2 * pad;
  const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
  cam.left = cx - w / 2; cam.right = cx + w / 2; cam.top = cy + h / 2; cam.bottom = cy - h / 2; cam.updateProjectionMatrix();
  return cam;
}
function project(cam, W, H, pts) {
  const out = {};
  for (const [k, p] of Object.entries(pts)) { const v = p.clone().project(cam); out[k] = [Math.round((v.x + 1) / 2 * W), Math.round((1 - v.y) / 2 * H)]; }
  return out;
}
function room(...a) { return obst('wall', () => _room(...a)); }
function _room(g, x0, x1, depth, h = 240, opts = {}) {
  const a = amat();
  g.add(plane(x0 - 40, -2, x1 + 40, depth, 0, a.floor));
  g.add(bx(x0 - (opts.left === false ? 0 : 40), 0, -22, x1 + 40, h, -1.2, a.wall));
  if (opts.left !== false) g.add(bx(x0 - 60, 0, -22, x0 - 40, h, depth, a.wall));
}
function lights(scene, opts = {}) {
  const L = addLights(scene, { key: opts.key ?? 2.1, keyPos: opts.keyPos ?? [260, 520, 520], rim: 0.2, hemi: 0.32, shadowSize: opts.shadowSize ?? 420, target: opts.target ?? [180, 60, 60] });
  L.key.color.set(0xfff4e6); L.key.shadow.radius = 7; L.key.shadow.bias = -0.0006;
  const fill = new THREE.DirectionalLight(0xe8f0ff, 0.35); fill.position.set(-300, 200, 400); scene.add(fill);
  return L;
}
const RB_Q0 = [[0.2, 0.7, 1.4, 0.4, 0.1, 0], [-0.4, 0.9, 1.1, 0.6, -0.3, 0.2], [0.8, 0.5, 1.6, 0.2, 0.4, 0], [0, 0.3, 1.8, 0.9, 0, 0.5], [1.4, 0.8, 1.2, 0.5, 0.6, -0.3], [-1.2, 0.6, 1.5, 0.3, -0.6, 0.3]];

// task poses for the linear kitchen (k = arkiLinearKitchen result)
function taskPose(k, task) {
  const xs = k.xs, tl = k.tall, dn = V(0, -1, 0);
  switch (task) {
    case 'detect': return { car: k.xc0 + 108, tcp: V(k.xc0 + 66, 122, 46), dir: V(-0.35, -1, 0.1), side: V(0, 0, 1) };
    case 'pick': return { car: k.xc0 + 112, tcp: V(k.xc0 + 34 + 12.5, 95.5, 32), dir: dn, side: V(0, 0, 1), hold: null };
    case 'load': return { car: tl.x0 - 18, tcp: V((tl.x0 + tl.x1) / 2 + 2, tl.dwY0 + 8 + 22, 30 + 34 + 4), dir: dn, side: V(1, 0, 0), hold: 'plateV' };
    case 'unload': return { car: tl.x0 - 20, tcp: V((tl.x0 + tl.x1) / 2 - 6, tl.dwY0 + 44 + 16, 30 + 18), dir: V(0.15, -1, 0.25), side: V(1, 0, 0), hold: 'bowl' };
    case 'store': return { car: tl.x0 - 16, tcp: V((tl.x0 + tl.x1) / 2 - 12, tl.stY0 + 26, 30 + 38 + 4), dir: dn, side: V(1, 0, 0), hold: 'plateV' };
    case 'hero': return { car: xs + 30, tcp: V(xs + 92, 104, 64), dir: V(0.25, -1, 0.3), side: V(1, 0, 0), hold: 'plateV' };
    case 'carry': default: return { car: xs + 70, tcp: V(xs + 62, 118, 52), dir: V(0.1, -1, 0.2), side: V(1, 0, 0), hold: 'plateV' };
  }
}
function attachHeld(robot, kind) {
  if (!kind) return;
  const tcp = robot.userData.tcp; let o;
  if (kind === 'plateV') { o = plate(11); o.rotation.set(0, 0, 0); o.rotation.x = Math.PI / 2; o.position.set(0, 9, -1.2); }
  else if (kind === 'bowl') { o = bowl(6, 5.5); o.rotation.x = Math.PI; o.position.set(0, 4.5, 0); }
  o.scale.setScalar(1 / robot.scale.x); tcp.add(o);
}
// carriage search along the rail (+ optional lift), collision-aware IK; returns the best collision-free pose found
function placeRobot(g, k, task, scale = 1.0, opts = {}) {
  const tp = k.v2 ? taskPoseV2(k, task) : taskPose(k, task);
  const root = opts.root || g; root.updateMatrixWorld(true);
  const obstacles = collectObstacles(root);
  const robot = makeRobot(scale); robot.rotation.x = Math.PI; g.add(robot);
  attachHeld(robot, tp.hold);
  const lift = opts.lift ?? tp.lift ?? k.lift ?? 0;
  const lifts = opts.lifts || [lift];
  const offs = opts.offsets || [0, -8, 8, -16, 16, -26, 26, -36, 36];
  const x0 = k.rl.x0 + 12, x1 = k.rl.x1 - 12;
  let best = null;
  const cands = tp.parkCands || [[tp.tcp, tp.dir, tp.side]];
  for (const [tcp, dir, side] of cands) for (const lf of lifts) for (const dx of (tp.parkCands ? [0] : offs)) {
    const cx = tp.car + dx; if (!tp.parkCands && (cx < x0 || cx > x1)) continue;
    robot.position.set(cx, k.rl.y - 6 - lf, k.rl.z); g.updateMatrixWorld(true);
    const r = reach(robot, g.localToWorld(tcp.clone()), dir, side, RB_Q0, { obstacles });
    const score = r.score + Math.abs(dx) * 0.01 + lf * 0.002;
    if (!best || score < best.score) best = { r, cx, lf, score };
    if (r.posErr < 0.6 && r.rotErr < 0.02 && r.pen < 0.05) break;
  }
  robot.position.set(best.cx, k.rl.y - 6 - best.lf, k.rl.z);
  setJoints(robot, best.r.q); g.updateMatrixWorld(true);
  if (tp.parkCands) { const bb = new THREE.Box3().setFromObject(robot); best.envelope = [bb.min.x, bb.min.y, bb.min.z, bb.max.x, bb.max.y, bb.max.z].map(v => +v.toFixed(1)); }
  g.add(carriage(best.cx, k.rl.y, k.rl.z, best.lf));
  const P = penetration(robotCapsules(robot), obstacles);
  return { robot, ik: { posErr: +best.r.posErr.toFixed(2), rotErr: +best.r.rotErr.toFixed(3), pen: +P.total.toFixed(2), hits: P.hits, car: +best.cx.toFixed(1), lift: best.lf, envelope: best.envelope }, tp };
}

export const ARKI_SCENES = {
  // Cover / product shots on the linear kitchen. q: task, view(hero|seq|after), zones=1, human=1, path=1
  async linear(W, H, p) {
    const renderer = makeRenderer(W, H); const scene = makeScene(renderer, 0.42); amat();
    const g = new THREE.Group(); scene.add(g);
    const task = p.get('task') || 'load';
    const closed = task === 'detect' || task === 'pick';
    const withRet = p.get('ret') === '1';
    const k = arkiLinearKitchen(g, 0, { tall: { dwOpen: closed ? 0.0 : 1, rackOut: closed ? 0 : 1, stOut: task === 'store' ? 1 : (task === 'hero' ? 0.75 : 0.0) }, dirty: !['store', 'unload'].includes(task), ret: withRet ? {} : null });
    room(g, 0, 360, 330, 240, { left: p.get('leftwall') !== '0' });
    if (p.get('table') === '1') table(g, 110, 215, 260, 300);
    if (p.get('zones') === '1') {
      zone(g, 'robot', 44, 1, 300, 62, 88.9); zone(g, 'human', withRet ? 30 : 0, 76, 360, 200);
      if (withRet) zone(g, 'nogo', k.ret.x0 + 1, k.ret.ihz0 - 10, k.ret.x1 - 1, k.ret.ihz1 + 10, 89.6);
      else if (p.get('table') === '1') zone(g, 'nogo', 80, 194, 290, 326);
      reachVolume(g, 44, 300, 0, 68, 89, 139);
    }
    const lifts = p.get('lifts') ? p.get('lifts').split(',').map(Number) : null;
    const { robot, ik } = placeRobot(g, k, task, 1.0, lifts ? { lifts } : {});
    if (p.get('path') === '1') pathCurve(g, [V(k.xc0 + 46, 100, 40), V(k.xs - 10, 128, 58), V(k.xi - 10, 132, 70), V(k.tall.x0 - 6, 110, 78), V((k.tall.x0 + k.tall.x1) / 2, 84, 74)]);
    if (task === 'detect') { visionCone(g, V(k.xc0 + 64, 118, 52), V(k.xc0 + 44, 89, 30), 30); for (const d of k.dishes) { const b = new THREE.Box3().setFromObject(d); const c = b.getCenter(V(0, 0, 0)); const s = b.getSize(V(0, 0, 0)); detectBox(g, c, s.x + 3, s.y + 3, s.z + 3); } }
    if (p.get('human') === '1') g.add(human(+(p.get('hx') || 300), +(p.get('hz') || 150), +(p.get('hr') || -0.5)));
    const view = p.get('view') || 'hero';
    let cam;
    const qv = (k) => p.get(k) ? p.get(k).split(',').map(Number) : null;
    if (view === 'hero') cam = camPersp(W, H, 33, V(470, 230, 520), V(185, 100, 40));
    else if (view === 'seq') {
      const left = task === 'detect' || task === 'pick';
      const look = left ? V(112, 100, 34) : V(300, 104, 46);
      const off = left ? V(150, 62, 230) : V(-150, 70, 250);
      cam = camPersp(W, H, 36, look.clone().add(off), look);
    }
    else if (view === 'after') cam = camPersp(W, H, 38, V(460, 330, 560), V(180, 70, 80));
    else cam = camPersp(W, H, 34, V(420, 260, 430), V(180, 90, 40));
    if (qv('cam')) cam = camPersp(W, H, +(p.get('fov') || 34), V(...qv('cam')), V(...qv('look')));
    lights(scene, { keyPos: [300, 520, 600], target: [180, 60, 60] });
    renderer.render(scene, cam);
    const anchors = project(cam, W, H, { home: k.gar.home, rail: V((k.xg + k.xt) / 2, 140, 24), sink: k.sk.center, dw: V((k.tall.x0 + k.tall.x1) / 2, k.tall.dwY0 + 40, 60), storage: V((k.tall.x0 + k.tall.x1) / 2, k.tall.stY0 + 10, 60), ih: k.ih ? k.ih.center : V(k.xi, 88, 30),
      robotZone: V(200, 89, 40), humanZone: V(200, 0, 140), counter: V(k.xc0 + 40, 90, 40), nogo: k.ret ? V((k.ret.x0 + k.ret.x1) / 2, 89, (k.ret.ihz0 + k.ret.ihz1) / 2) : V(180, 0, 260), reach: V(120, 135, 66) });
    return { ik, anchors };
  },

  // stow/deploy planner run (no image): returns park / travel joint sets, the deploy path and a collision report
  async stowsearch(W, H, p) {
    amat();
    const mk = (open) => { const g = new THREE.Group(); const k = arkiRunV2(g, 0, { railZ: +(p.get('railz') || 30), garageOpen: open, dwOpen: 0, rackL: 0, rackU: 0, drawerOut: 0, dirty: true }); room(g, 0, k.xe, 330, 240, {}); return [g, k]; };
    const [gC, kC] = mk(0), [gO, kO] = mk(1);
    const num = (key, d) => p.get(key) ? +p.get(key) : d;
    return planStow(gC, kC, gO, kO, { seed: num('seed', 4242), nPark: num('npark', 60), nTravel: num('ntravel', 80), yMin: num('ymin', 98.2), maxIt: num('maxit', 4000), topPark: num('toppark', 4), topTravel: num('toptravel', 4) });
  },

  // v2 robot run (collision-checked): task=detect|pick|load|unload|store|hero|park, view=seq|hero|front
  async run2(W, H, p) {
    const renderer = makeRenderer(W, H); const scene = makeScene(renderer, 0.42); amat();
    const g = new THREE.Group(); scene.add(g);
    const task = p.get('task') || 'load';
    const STOW = ['park', 'deploy', 'exit', 'out'];
    const doorOpen = p.get('door') !== null ? +p.get('door') : (['deploy', 'exit'].includes(task) ? 1 : 0);
    const k = arkiRunV2(g, 0, { raise: +(p.get('raise') || 0), railZ: +(p.get('railz') || 24), dwOpen: ['load', 'unload', 'hero'].includes(task) ? 1 : 0,
      rackL: ['load', 'hero'].includes(task) ? 1 : 0, rackU: task === 'unload' ? 1 : 0, drawerOut: task === 'store' ? 1 : 0,
      rackOutL: +(p.get('outl') || 44), rackOutU: +(p.get('outu') || 44), ret: p.get('ret') === '1' ? {} : null,
      garageOpen: doorOpen, dirty: !['store', 'unload'].includes(task) });
    room(g, 0, k.xe, 330, 240, { left: p.get('leftwall') !== '0' });
    if (p.get('zones') === '1') {
      zone(g, 'robot', k.xz, 1, k.xe, 62, 89.2); zone(g, 'human', k.ret ? 30 : 0, 76, k.xe, 200);
      if (k.ret) zone(g, 'nogo', k.ret.x0 + 1, k.ret.ihz0 - 10, k.ret.x1 - 1, k.ret.ihz1 + 10, 89.6);
      reachVolume(g, k.xz, k.xe, 0, 68, 89, 139);
    }
    if (p.get('human') === '1') g.add(human(+(p.get('hx') || 64), +(p.get('hz') || 168), +(p.get('hr') || -1.57)));
    if (p.get('path') === '1') { const dx = (k.dw.x0 + k.dw.x1) / 2;
      pathCurve(g, [V(k.xz + 36, 100, 40), V(k.xs - 20, 126, 60), V(k.xs + 30, 130, 68), V(k.xw - 20, 116, 78), V(dx, 66, 80)]); }
    let ik = null, stowA = {};
    if (STOW.includes(task)) {
      // stored, collision-checked stow/deploy poses (planStow -> web/stow_poses.json)
      const SP = await (await fetch('stow_poses.json')).json();
      const lens = [0]; for (let i = 1; i < SP.path.length; i++) lens.push(lens[i - 1] + jdist(SP.path[i - 1], SP.path[i]));
      const along = (t) => { const L = lens[lens.length - 1] * Math.max(0, Math.min(1, t)); let i = 1; while (i < lens.length - 1 && lens[i] < L) i++;
        const u = (L - lens[i - 1]) / ((lens[i] - lens[i - 1]) || 1); return SP.path[i - 1].map((v, j) => v + (SP.path[i][j] - v) * u); };
      const pose = (q, cx, ghost = false) => { const r = makeRobot(1.0); r.rotation.x = Math.PI; r.position.set(cx, k.rl.y - 6, k.rl.z); setJoints(r, q);
        if (ghost) r.traverse(o => { if (o.isMesh) { o.material = o.material.clone(); o.material.transparent = true; o.material.opacity = 0.22; o.material.depthWrite = false; o.castShadow = false; } });
        g.add(r); return r; };
      let q, cx;
      if (task === 'park') { q = SP.qPark; cx = SP.gx; }
      else if (task === 'deploy') { q = along(+(p.get('t') ?? 0.5)); cx = SP.gx; }
      else if (task === 'exit') { q = SP.qTravel; cx = k.gar.x1 + +(p.get('dx') || 0); }
      else { q = SP.qTravel; cx = +(p.get('cx') || (k.xz + 60)); }
      const robot = pose(q, cx); g.add(carriage(cx, k.rl.y, k.rl.z, 0));
      if (p.get('ghosts')) for (const t of p.get('ghosts').split(',').map(Number)) pose(along(t), SP.gx, true);
      if (p.get('tcppath') === '1') { const tmp = makeRobot(1.0); tmp.rotation.x = Math.PI; tmp.position.set(SP.gx, k.rl.y - 6, k.rl.z); g.add(tmp); const pts = [];
        for (let i = 0; i <= 40; i++) { setJoints(tmp, along(i / 40)); tmp.updateMatrixWorld(true); pts.push(tmp.userData.tcp.getWorldPosition(V(0, 0, 0))); } g.remove(tmp); pathCurve(g, pts, null, 5, 3, 0.6); }
      if (p.get('arrow') === '1') pathCurve(g, [V(k.gar.x1 + 4, 96.5, 58), V(k.xz + 95, 96.5, 58)], null, 7, 4, 0.8);
      // collision report for this frame: furniture + dishes + rail/carriage + self-collision
      g.updateMatrixWorld(true);
      const obs = collectObstacles(g); for (const d of k.dishes) obs.push(new THREE.Box3().setFromObject(d));
      const caps = robotCapsules(robot);
      const railBox = new THREE.Box3(V(k.rl.x0, k.rl.y, k.rl.z - 4), V(k.rl.x1, k.rl.y + 6, k.rl.z + 4.4)), carBox = new THREE.Box3(V(cx - 13, k.rl.y - 6, k.rl.z - 7), V(cx + 13, k.rl.y, k.rl.z + 7));
      const pen = penetration(caps, obs).total + penetration(caps.filter(c => c.link !== -1 && c.link !== 0), [railBox, carBox]).total + selfPenetration(caps).total;
      const bb = capsuleBounds(caps);
      ik = { pen: +pen.toFixed(2), car: +cx.toFixed(1), envelope: [bb.xmin, bb.ymin, bb.zmin, bb.xmax, bb.ymax, bb.zmax].map(v => +v.toFixed(1)), stored: SP.check ? { pathWorst: SP.check.pathWorst, transitWorst: SP.check.transitWorst } : null };
      if (p.get('sweep') === '1') {   // envelope of the whole deploy path (fine sampling), for the 'how far does it reach out' number
        const tmp = makeRobot(1.0); tmp.rotation.x = Math.PI; tmp.position.set(SP.gx, k.rl.y - 6, k.rl.z); g.add(tmp); const e = { xmax: -1e9, zmax: -1e9, ymin: 1e9, ymax: -1e9 };
        for (let i = 0; i <= 400; i++) { setJoints(tmp, along(i / 400)); const b2 = capsuleBounds(robotCapsules(tmp)); e.xmax = Math.max(e.xmax, b2.xmax); e.zmax = Math.max(e.zmax, b2.zmax); e.ymin = Math.min(e.ymin, b2.ymin); e.ymax = Math.max(e.ymax, b2.ymax); }
        g.remove(tmp); ik.sweep = Object.fromEntries(Object.entries(e).map(([kk, v]) => [kk, +v.toFixed(1)])); }
      stowA = { robot: V((bb.xmin + bb.xmax) / 2, (bb.ymin + bb.ymax) / 2, (bb.zmin + bb.zmax) / 2), passage: V(k.gar.x1, 116, 26), door: V(k.gar.x0 + 4, 160, k.gar.d + 30), garageTop: V((k.gar.x0 + k.gar.x1) / 2, 210, k.gar.d) };
    }
    else if (task !== 'none') { const R = placeRobot(g, k, task, 1.0, p.get('lifts') ? { lifts: p.get('lifts').split(',').map(Number) } : {}); ik = R.ik; }
    const look = V(+(p.get('lx') || 200), +(p.get('ly') || 95), +(p.get('lz') || 40));
    let cam = p.get('cam') ? camPersp(W, H, +(p.get('fov') || 36), V(...p.get('cam').split(',').map(Number)), look)
      : camPersp(W, H, 36, look.clone().add(V(150, 70, 260)), look);
    let secA = {};
    if (p.get('section') === '1') {
      // true section through the dishwasher: clip everything left of X, look from -x (wall on the left, room on the right)
      const X = k.dw.x0 + 2;
      renderer.clippingPlanes = [new THREE.Plane(V(1, 0, 0), -X)];
      g.traverse(o => { if (o.isMesh) { const ms = Array.isArray(o.material) ? o.material : [o.material]; ms.forEach(m => { m.side = THREE.DoubleSide; }); } });
      const span = +(p.get('span') || 300);
      cam = camOrtho(W, H, span, V(X - 600, 118, 70), V(X, 118, 70));
      const lv = (y, z = -6) => V(X, y, z);
      secA = { y0: lv(0), y37: lv(37), y85: lv(85), y88: lv(88.2), ysh: lv(112.4), y139: lv(139), y145: lv(145), y225: lv(225), y240: lv(240),
        z0: V(X, -12, 0), z62: V(X, -12, 62), zRack: V(X, -12, 98), tcp: V(X, 37, 72) };
    }
    lights(scene, { keyPos: [300, 520, 600], target: [180, 60, 60] });
    renderer.render(scene, cam);
    const dwc = V((k.dw.x0 + k.dw.x1) / 2, 40, 70), drc = V((k.dr.x0 + k.dr.x1) / 2, 58, k.dr.out * 48 + 58);
    const anchors = project(cam, W, H, { garage: V((k.gar.x0 + k.gar.x1) / 2, 170, 60), rail: V((k.xz + k.xs) / 2, 140, k.rl.z + 4), sink: k.sk.center,
      drop: V(k.xz + 40, 89, 40), drawer: drc, dw: dwc, dwBody: V((k.dw.x0 + k.dw.x1) / 2, 60, 57), robotZone: V((k.xz + k.xe) / 2, 89, 30),
      humanZone: V(200, 0, 150), nogo: k.ret ? V((k.ret.x0 + k.ret.x1) / 2, 89, (k.ret.ihz0 + k.ret.ihz1) / 2) : V(0, 0, 0), reach: V(k.xz + 60, 135, 66), ...stowA, ...secA });
    return { ik, anchors };
  },

  // Before: ordinary kitchen + robot added on a mobile pedestal (dishwasher under the counter, storage high, robot in the aisle)
  async before(W, H, p) {
    const renderer = makeRenderer(W, H); const scene = makeScene(renderer, 0.42); const a = amat();
    const g = new THREE.Group(); scene.add(g);
    baseRun(g, 0, 360, { doorW: 60 });
    const sk = sink(g, 150, { w: 80 });
    counter(g, 0, 360, { holes: [[sk.x0, sk.x1, 10, 52]] });
    const ih = induction(g, 300, { w: 56 });
    backsplash(g, 0, 360); upperRun(g, 0, 360, { doorW: 60 });
    // under-counter dishwasher at floor level (door open, rack out)
    const dx0 = 210, dx1 = 270;
    g.add(bx(dx0, 10, 0, dx1, 85, 2, a.dwIn));
    const door = new THREE.Group(); door.position.set((dx0 + dx1) / 2, 10, 57); door.rotation.x = 88 * D; g.add(door);
    door.add(bx(-29, 0, -1.2, 29, 74, 1.2, a.cabLower));
    const rk = new THREE.Group(); rk.position.set((dx0 + dx1) / 2, 18, 62); g.add(rk);
    rk.add(bx(-25, 0, -22, 25, 9, 22, new THREE.MeshStandardMaterial({ color: 0x8d939b, metalness: 0.5, roughness: 0.4, transparent: true, opacity: 0.85 })));
    // dirty dishes
    const p1 = plate(12.5); p1.position.set(70, 88.2, 32); g.add(p1);
    const b1 = bowl(6.5, 6); b1.position.set(98, 88.2, 24); g.add(b1);
    room(g, 0, 360, 330);
    // robot on a cart in the aisle
    const cart = new THREE.Group(); cart.position.set(150, 0, 112); g.add(cart);
    cart.add(bx(-26, 6, -26, 26, 72, 26, new THREE.MeshPhysicalMaterial({ color: 0x3a3e45, roughness: 0.5, clearcoat: 0.2 }), 2.5));
    for (const [x, z] of [[-20, -20], [20, -20], [-20, 20], [20, 20]]) { const w = cyl(3, 3, a.dark, 16); w.rotation.z = Math.PI / 2; w.position.set(x, 3, z); cart.add(w); }
    const robot = makeRobot(1.0); robot.position.set(150, 72, 112); g.add(robot); g.updateMatrixWorld(true);
    const r = reach(robot, V(128, 108, 46), V(0, -1, 0), V(1, 0, 0), [[0.3, 0.6, 1.2, 0.6, 0, 0], [-0.3, 0.9, 0.9, 0.9, 0, 0], [0.0, 1.0, 1.0, 0.8, 0.2, 0], [2.6, 0.7, 1.1, 0.6, 0, 0], [-2.6, 0.7, 1.1, 0.6, 0, 0]]);
    attachHeld(robot, 'plateV');
    g.add(human(+(p.get('hx') || 292), +(p.get('hz') || 122), -0.35));
    const cam = camPersp(W, H, 38, V(460, 330, 560), V(180, 70, 80));
    lights(scene, { keyPos: [300, 520, 600], target: [180, 60, 60] });
    renderer.render(scene, cam);
    const anchors = project(cam, W, H, { robot: V(150, 130, 112), cart: V(150, 40, 140), dw: V(240, 25, 85), storage: V(60, 200, 30), human: V(292, 165, 122), sink: V(150, 80, 30), conflict: V(220, 0, 120) });
    return { ik: { posErr: +r.posErr.toFixed(2) }, anchors };
  },

  // Real plans digitized from the client's drawings: id=old2a|old2b|new2|new3|new4, mode=unit|orig, arki=0|1
  async plan(W, H, p) {
    const renderer = makeRenderer(W, H); const scene = makeScene(renderer, 0.45); const a = amat();
    const g = new THREE.Group(); scene.add(g);
    const id = p.get('id'); const mode = p.get('mode') || 'unit';
    const P = await (await fetch(`/${p.get('dir') || 'plans'}/${id}.json`)).json();
    const M = planMats();
    const { W: PW, D: PD } = planBounds(P);
    buildFloors(g, P, M);
    const K = P.kitchen || {};
    const backEdges = (K.counters || []).filter(c => c.back && c.back !== 'none').map(c => ({
      horiz: c.back === 'top' || c.back === 'bottom', c: { top: c.y0, bottom: c.y1, left: c.x0, right: c.x1 }[c.back],
      a0: (c.back === 'top' || c.back === 'bottom') ? c.x0 : c.y0, a1: (c.back === 'top' || c.back === 'bottom') ? c.x1 : c.y1 }));
    const kitchenWalls = (w) => {      // full-height only along the counters that sit against this wall (+ 30 cm)
      if (p.get('kfull') === '0') return [];
      const horiz = Math.abs(w.y1 - w.y2) < 1, wc = horiz ? w.y1 : w.x1;
      const lo = horiz ? Math.min(w.x1, w.x2) : Math.min(w.y1, w.y2), hi = horiz ? Math.max(w.x1, w.x2) : Math.max(w.y1, w.y2);
      return backEdges.filter(e => e.horiz === horiz && Math.abs(e.c - wc) < (w.t || 150) / 2 + 80 && Math.min(hi, e.a1) - Math.max(lo, e.a0) > 100)
        .map(e => [Math.max(lo - 200, e.a0 - 300), Math.min(hi + 200, e.a1 + 300)]);
    };
    const FIT = p.get('arki') === '1' ? ARKI_FIT[id] : null;
    if (FIT) {       // full-height walls behind the ARKI run and the side run instead of the original counters
      const runLen = 45 + FIT.drop + 200;
      backEdges.length = 0;
      backEdges.push({ horiz: true, c: FIT.pos[1] * 10, a0: FIT.pos[0] * 10, a1: (FIT.pos[0] + runLen) * 10 });
      if (FIT.side) backEdges.push({ horiz: false, c: FIT.side.pos[0] * 10, a0: (FIT.side.pos[1] - FIT.side.len) * 10, a1: FIT.side.pos[1] * 10 });
    }
    buildWalls(g, P, M, { cut: +(p.get('cut') || 110), fullRanges: kitchenWalls });
    buildFixtures(g, P, M, { tallCap: +(p.get('cut') || 110) - 5 });
    let ik = null, extraA = {};
    if (!FIT) buildKitchenOriginal(g, P, M);
    else {
      const task = p.get('task') || 'none';
      const doorOpen = ['deploy', 'exit'].includes(task) ? 1 : +(p.get('door') || 0);
      const dwT = ['load', 'unload', 'hero'].includes(task);
      const { gk, k } = arkiInPlan(g, FIT, { garageOpen: doorOpen, dwOpen: dwT ? 1 : 0, rackL: ['load', 'hero'].includes(task) ? 1 : 0, rackU: task === 'unload' ? 1 : 0,
        drawerOut: task === 'store' ? 1 : 0, dirty: !['store', 'unload'].includes(task) });
      if (p.get('zones') === '1') { zone(gk, 'robot', k.xz, 1, k.xe, 62, 89.2); reachVolume(gk, k.xz, k.xe, 0, 68, 89, 139); }
      g.updateMatrixWorld(true);
      if (['detect', 'pick', 'load', 'unload', 'store', 'hero'].includes(task)) { const R = placeRobot(gk, k, task, 1.0, { root: g }); ik = R.ik; }
      else if (task === 'park' || task === 'deploy' || task === 'exit') {
        const SP = await (await fetch('stow_poses.json')).json();
        const lens = [0]; for (let i = 1; i < SP.path.length; i++) lens.push(lens[i - 1] + jdist(SP.path[i - 1], SP.path[i]));
        const along = (t) => { const L = lens[lens.length - 1] * Math.max(0, Math.min(1, t)); let i = 1; while (i < lens.length - 1 && lens[i] < L) i++;
          const u = (L - lens[i - 1]) / ((lens[i] - lens[i - 1]) || 1); return SP.path[i - 1].map((v, j) => v + (SP.path[i][j] - v) * u); };
        const q = task === 'park' ? SP.qPark : task === 'exit' ? SP.qTravel : along(+(p.get('t') ?? 0.6));
        const cx = task === 'exit' ? k.gar.x1 : SP.gx;
        const r = makeRobot(1.0); r.rotation.x = Math.PI; r.position.set(cx, k.rl.y - 6, k.rl.z); setJoints(r, q); gk.add(r); gk.add(carriage(cx, k.rl.y, k.rl.z, 0));
        if (p.get('verify') === '1') {   // whole stored deploy path + transit, in this plan (walls, side run, door at this plan's angle, dishes)
          g.updateMatrixWorld(true);
          const obs = collectObstacles(g); for (const d of k.dishes) obs.push(new THREE.Box3().setFromObject(d));
          const inv = new THREE.Matrix4().copy(gk.matrixWorld).invert();
          const obsL = obs.map(b => { const c = b.clone().applyMatrix4(inv); c.userData = b.userData; return c; });   // run frame (rot is a multiple of 90 deg, so boxes stay exact)
          const tmp = makeRobot(1.0); tmp.rotation.x = Math.PI;
          const railBox = new THREE.Box3(V(k.rl.x0, k.rl.y, k.rl.z - 4), V(k.rl.x1, k.rl.y + 6, k.rl.z + 4.4));
          const penAt = (q2, cx2) => { tmp.position.set(cx2, k.rl.y - 6, k.rl.z); setJoints(tmp, q2); const caps = robotCapsules(tmp);
            const carBox = new THREE.Box3(V(cx2 - 13, k.rl.y - 6, k.rl.z - 7), V(cx2 + 13, k.rl.y, k.rl.z + 7));
            return penetration(caps, obsL).total + penetration(caps.filter(c => c.link !== -1 && c.link !== 0), [railBox, carBox]).total + selfPenetration(caps).total; };
          const hitsAt = (q2, cx2) => { tmp.position.set(cx2, k.rl.y - 6, k.rl.z); setJoints(tmp, q2); const caps = robotCapsules(tmp); return penetration(caps, obsL).hits.map(h => h.box + ':' + h.link + ':' + h.depth); };
          let wPark = penAt(SP.qPark, SP.gx), wPath = 0, wTr = 0, tPath = 0, xTr = 0;
          for (let i = 0; i <= 400; i++) { const c = penAt(along(i / 400), SP.gx); if (c > wPath) { wPath = c; tPath = i / 400; } }
          for (let x = SP.gx; x <= k.gar.x1 + 12; x += 1) { const c = penAt(SP.qTravel, x); if (c > wTr) { wTr = c; xTr = x; } }
          ik = { verify: { park: +wPark.toFixed(3), path: +wPath.toFixed(3), transit: +wTr.toFixed(3), doorDeg: FIT.doorDeg, obstacles: obsL.length,
            pathHits: wPath > 0 ? { t: tPath, hits: hitsAt(along(tPath), SP.gx) } : null, transitHits: wTr > 0 ? { x: xTr, hits: hitsAt(SP.qTravel, xTr) } : null } };
        }
      }
      const toW = (v) => gk.localToWorld(v.clone());
      extraA = { garage: toW(V((k.gar.x0 + k.gar.x1) / 2, 170, 62)), sink: toW(k.sk.center), dw: toW(V((k.dw.x0 + k.dw.x1) / 2, 50, 60)), rail: toW(V((k.xz + k.xs) / 2, 142, 30)),
        drop: toW(V(k.xz + 35, 89, 40)), drawer: toW(V((k.dr.x0 + k.dr.x1) / 2, 60, 58)), runMid: toW(V((k.xg + k.xe) / 2, 110, 40)),
        cooktop: FIT.side ? V(FIT.side.pos[0] + 30, 89, FIT.side.pos[1] - FIT.side.cooktop) : V(0, 0, 0) };
    }
    // camera from the front side
    const fs = P.front_side || 'bottom';
    const cx = PW / 2, cz = PD / 2, span = (+(p.get('span') || 0)) || Math.max(PW, PD) * 1.32;
    const dirs = { bottom: [0.62, 1.0, 1.0], top: [-0.62, 1.0, -1.0], left: [-1.0, 1.0, 0.62], right: [1.0, 1.0, -0.62] };
    const d = p.get('dir3') ? p.get('dir3').split(',').map(Number) : dirs[fs]; const L = 2600;
    let cam;
    if (p.get('view') === 'persp') cam = camPersp(W, H, +(p.get('fov') || 40), V(...p.get('cam').split(',').map(Number)), V(...p.get('look').split(',').map(Number)));
    else if (p.get('view') === 'top') { cam = camOrtho(W, H, span, V(cx, 3000, cz + 0.01), V(cx, 0, cz)); fitOrtho(cam, new THREE.Box3().setFromObject(g), W, H, +(p.get('pad') || 0.04)); }
    else { cam = camOrtho(W, H, span, V(cx + d[0] * L, d[1] * L * 0.95, cz + d[2] * L), V(cx, 0, cz)); fitOrtho(cam, new THREE.Box3().setFromObject(g), W, H, +(p.get('pad') || 0.04)); }
    lights(scene, { keyPos: [cx + d[0] * 600, 1100, cz + d[2] * 900], target: [cx, 0, cz], shadowSize: Math.max(PW, PD) * 0.8 });
    renderer.render(scene, cam);
    const anchors = { ...roomAnchors(P), ...extraA };
    return { ik, anchors: project(cam, W, H, anchors), W: PW, D: PD, front: fs };
  },

  // 84㎡ representative apartment concept models. type=2|3|4, mode=unit|kitchen
  async apt(W, H, p) {
    const renderer = makeRenderer(W, H); const scene = makeScene(renderer, 0.45); amat();
    const g = new THREE.Group(); scene.add(g);
    const type = p.get('type') || '3'; const mode = p.get('mode') || 'unit';
    const U = buildUnit(g, type, mode);
    let cam;
    const c = U.camera[mode];
    if (mode === 'unit') cam = camOrtho(W, H, c.span, V(...c.pos), V(...c.look));
    else cam = camPersp(W, H, c.fov, V(...c.pos), V(...c.look));
    lights(scene, { keyPos: c.key || [U.W * 0.6, 900, U.D + 700], target: [U.W / 2, 0, U.D / 2], shadowSize: Math.max(U.W, U.D) * 0.75 });
    renderer.render(scene, cam);
    return { ik: U.ik, anchors: project(cam, W, H, U.anchors), rooms: U.rooms, W: U.W, D: U.D, kitchen: U.kitchen };
  },
};

// ---------------------------------------------------------------- ARKI kitchen fitted into a digitized plan
// pos = world (cm) of the run's local origin, rot = rotation about +Y (local x along the wall, local z out of the wall).
// The v2 run keeps its verified geometry; only the drop-zone width and the door's maximum angle change per plan.
const ARKI_FIT = {
  // 구축 2Bay A: kitchen north wall (face y = 3290 mm) from the west wall face (100 mm) to the bedroom-2 door (3355 mm).
  // Run 315 cm starts 4 cm off the west wall; the garage door stops at 90 deg (west wall). Cooktop moves to the west wall, south part.
  old2a: { pos: [14, 329], rot: 0, drop: 70, doorDeg: 90, wallObst: [[-30, -40, -4, 700]],
    side: { pos: [10, 611], rot: Math.PI / 2, len: 171, depth: 60, cooktop: 86 } },
};
function sideRun(g, sd) {
  const a = amat(); const sg = new THREE.Group(); sg.position.set(sd.pos[0], 0, sd.pos[1]); sg.rotation.y = sd.rot; g.add(sg);
  obst('side', () => {
    baseRun(sg, 0, sd.len, { doorW: 57 }); counter(sg, 0, sd.len, { depth: sd.depth + 2 }); backsplash(sg, 0, sd.len);
    const c = sd.cooktop; induction(sg, c, { w: 58 });
    upperRun(sg, 0, Math.max(0, c - 34), { doorW: 52 }); upperRun(sg, Math.min(sd.len, c + 34), sd.len, { doorW: 52 });
    sg.add(bx(c - 34, 158, 0, c + 34, 170, 50, a.cabTall)); sg.add(bx(c - 14, 170, 0, c + 14, 240, 26, a.cabTall));
  });
  return sg;
}
function arkiInPlan(g, fit, opts = {}) {
  const gk = new THREE.Group(); gk.position.set(fit.pos[0], 0, fit.pos[1]); gk.rotation.y = fit.rot; g.add(gk);
  const k = arkiRunV2(gk, 0, { railZ: 30, drop: fit.drop, garageAngle: fit.doorDeg, ...opts });
  if (fit.side) sideRun(g, fit.side);
  // walls next to the run as collision boxes in the run frame (the plan walls themselves are drawn by buildWalls)
  for (const [x0, z0, x1, z1] of fit.wallObst || []) obst('wall', () => gk.add(Object.assign(bx(x0, 0, z0, x1, 240, z1, amat().wall), { visible: false })));
  return { gk, k };
}

// ---------------------------------------------------------------- original kitchen of a digitized plan (as drawn)
function buildKitchenOriginal(g, P, M) {
  const a = amat(); const K = P.kitchen || {}; const S = 0.1;
  for (const c of K.counters || []) {
    const x0 = c.x0 * S, z0 = c.y0 * S, x1 = c.x1 * S, z1 = c.y1 * S;
    g.add(bx(x0, 0, z0, x1, 10, z1, a.dark));
    g.add(bx(x0 + 0.3, 10, z0 + 0.3, x1 - 0.3, 85, z1 - 0.3, a.cabLower));
    g.add(bx(x0, 85, z0, x1, 88.2, z1, a.quartz));
  }
  if (K.sink) { const x = K.sink.x * S, z = K.sink.y * S; g.add(bx(x - 38, 88.25, z - 21, x + 38, 88.5, z + 21, a.sinkIn)); }
  if (K.cooktop) { const x = K.cooktop.x * S, z = K.cooktop.y * S; const hob = rbox(56, 0.7, 50, 0.3, a.hob, 2); hob.position.set(x, 88.6, z); g.add(hob); }
  if (K.fridge) { const f = K.fridge; g.add(bx(f.x0 * S + 1, 0, f.y0 * S + 1, f.x1 * S - 1, 180, f.y1 * S - 1, a.fridge)); }
  for (const u of K.upper_cabinets || []) g.add(bx(u.x0 * S, 145, u.y0 * S, u.x1 * S, 225, u.y1 * S, a.cabUpper));
}

// ---------------------------------------------------------------- 84㎡ unit plans (representative concept models, not real complexes)
// Rooms: [name, x0, z0, x1, z1]; front facade (living/balcony side) at z = D.  Walls listed as [x0, z0, x1, z1] centre lines.
const PLANS = {
  '2': { W: 780, D: 1090,
    rooms: [['거실', 0, 640, 430, 1090], ['침실1', 430, 620, 780, 1090], ['주방', 0, 0, 330, 380], ['식당', 0, 380, 430, 640],
            ['침실2', 480, 0, 780, 310], ['침실3', 480, 310, 780, 620], ['욕실', 330, 0, 480, 200], ['현관', 330, 200, 480, 380]],
    walls: [[0, 0, 780, 0], [0, 0, 0, 1090], [780, 0, 780, 1090], [0, 1090, 780, 1090], [430, 620, 430, 1090], [430, 620, 780, 620],
            [480, 0, 480, 620], [480, 310, 780, 310], [330, 0, 330, 200], [330, 200, 480, 200], [330, 380, 430, 380]],
    fullWalls: [[0, 0, 330, 0], [0, 0, 0, 380]],
    camera: { unit: { span: 1300, pos: [1650, 1500, 2350], look: [400, 60, 545] }, kitchen: { fov: 34, pos: [610, 430, 600], look: [190, 92, 160] } } },
  '3': { W: 1020, D: 830,
    rooms: [['침실2', 0, 450, 300, 830], ['거실', 300, 400, 700, 830], ['침실1', 700, 430, 1020, 830], ['주방·식당', 300, 0, 700, 400],
            ['침실3', 0, 0, 300, 330], ['욕실2', 0, 330, 180, 450], ['현관', 180, 330, 300, 450], ['다용도', 700, 0, 860, 220], ['드레스룸', 700, 220, 1020, 430], ['욕실1', 860, 0, 1020, 220]],
    walls: [[0, 0, 1020, 0], [0, 0, 0, 830], [1020, 0, 1020, 830], [0, 830, 1020, 830], [300, 0, 300, 830], [700, 0, 700, 830],
            [0, 330, 300, 330], [0, 450, 300, 450], [180, 330, 180, 450], [700, 220, 1020, 220], [700, 430, 1020, 430], [860, 0, 860, 220]],
    fullWalls: [[300, 0, 700, 0]],
    camera: { unit: { span: 1420, pos: [1900, 1500, 2150], look: [510, 60, 415] }, kitchen: { fov: 34, pos: [890, 470, 690], look: [495, 85, 145] } } },
  '4': { W: 1140, D: 740,
    rooms: [['침실2', 0, 400, 270, 740], ['침실3', 270, 400, 540, 740], ['거실', 540, 360, 900, 740], ['침실1', 900, 380, 1140, 740],
            ['주방·식당', 520, 0, 920, 360], ['욕실2', 0, 0, 220, 280], ['현관', 220, 0, 400, 200], ['다용도', 400, 0, 520, 200], ['복도', 0, 280, 520, 400], ['드레스·욕실1', 920, 0, 1140, 380]],
    walls: [[0, 0, 1140, 0], [0, 0, 0, 740], [1140, 0, 1140, 740], [0, 740, 1140, 740], [270, 400, 270, 740], [540, 400, 540, 740],
            [900, 380, 900, 740], [0, 400, 540, 400], [920, 0, 920, 380], [900, 380, 1140, 380], [220, 0, 220, 280], [0, 280, 220, 280], [400, 0, 400, 200], [520, 0, 520, 200], [220, 200, 520, 200]],
    fullWalls: [[520, 0, 920, 0]],
    camera: { unit: { span: 1520, pos: [2050, 1450, 2000], look: [570, 60, 370] }, kitchen: { fov: 34, pos: [1100, 560, 720], look: [712, 80, 165] } } },
};

function buildUnit(g, type, mode) {
  const a = amat(); const P = PLANS[type]; const Wd = P.W, Dp = P.D;
  const wallH = mode === 'unit' ? 105 : 40;
  // floors
  P.rooms.forEach(([name, x0, z0, x1, z1], i) => {
    const wet = /욕실|다용도/.test(name);
    const m = wet ? a.floorWet : (/주방|식당/.test(name) ? a.floor : new THREE.MeshStandardMaterial({ color: a.roomFloor[i % 4], roughness: 0.85 }));
    g.add(plane(x0, z0, x1, z1, 0.05 + (wet ? 0 : 0.02), m));
  });
  // walls (low cut, dark section cap); kitchen back walls full height
  const mats = [a.wall, a.wall, a.wallCap, a.wall, a.wall, a.wall];
  for (const [x0, z0, x1, z1] of P.walls) {
    const horiz = z0 === z1;
    const ext = horiz ? (z0 === 0 || z0 === Dp) : (x0 === 0 || x0 === Wd);
    const t = ext ? 20 : 12;
    for (const [sx0, sz0, sx1, sz1, isFull] of splitFull(horiz, x0, z0, x1, z1, P.fullWalls)) {
      const h = isFull ? 240 : wallH;
      const len = horiz ? (sx1 - sx0) : (sz1 - sz0);
      const geo = horiz ? new THREE.BoxGeometry(len + t, h, t) : new THREE.BoxGeometry(t, h, len + t);
      const m = new THREE.Mesh(geo, isFull ? [a.wall, a.wall, a.wall, a.wall, a.wall, a.wall] : mats);
      m.position.set(horiz ? (sx0 + sx1) / 2 : sx0, h / 2, horiz ? sz0 : (sz0 + sz1) / 2);
      m.castShadow = true; m.receiveShadow = true; g.add(m);
    }
  }
  // context furniture
  const fur = (x0, z0, x1, z1, h, mat) => g.add(bx(x0, 0, z0, x1, h, z1, mat, 3));
  const anchors = {}; let ik = null; let kitchen = null;
  if (type === '3') {
    fur(360, 700, 640, 790, 42, a.sofa); fur(740, 560, 900, 770, 45, a.bed); fur(40, 560, 200, 760, 45, a.bed); fur(40, 60, 200, 260, 45, a.bed);
    // kitchen: linear run on the back wall x 320..680, robot rail; dining table; zones
    const kg = new THREE.Group(); kg.position.set(320, 0, 10); g.add(kg);
    const k = arkiLinearKitchen(kg, 0, { tall: { dwOpen: 1, rackOut: 1, stOut: 0 }, ret: { wallX: -14 } });
    table(g, 440, 230, 600, 310);
    const zg = new THREE.Group(); g.add(zg);
    zone(zg, 'robot', 364, 11, 620, 72, 88.9); zone(zg, 'human', 378, 86, 680, 200); zone(zg, 'nogo', 307, k.ret.ihz0, 367, k.ret.ihz1 + 20, 89.6);
    reachVolume(zg, 364, 620, 10, 78, 89, 139);
    const R = placeRobot(kg, k, 'load', 1.0); ik = R.ik;
    Object.assign(anchors, { home: V(342, 160, 40), rail: V(470, 145, 34), sink: V(490, 80, 40), dw: V(650, 90, 70), storage: V(650, 150, 40), ih: V(336, 92, 162),
      robotZone: V(400, 89, 46), humanZone: V(520, 0, 140), nogo: V(336, 89, 162), reach: V(560, 134, 76) });
    kitchen = [300, 0, 700, 400];
  } else if (type === '2') {
    fur(60, 950, 360, 1040, 42, a.sofa); fur(500, 760, 700, 990, 45, a.bed); fur(520, 40, 700, 220, 45, a.bed); fur(520, 360, 700, 560, 45, a.bed);
    k2(g, anchors); ik = anchors.__ik; delete anchors.__ik;
    kitchen = [0, 0, 330, 380];
  } else {
    fur(600, 640, 860, 720, 42, a.sofa); fur(940, 520, 1100, 720, 45, a.bed); fur(40, 540, 230, 720, 45, a.bed); fur(310, 540, 500, 720, 45, a.bed);
    k4(g, anchors); ik = anchors.__ik; delete anchors.__ik;
    kitchen = [520, 0, 920, 360];
  }
  if (mode === 'unit' && kitchen) { const [x0, z0, x1, z1] = kitchen; outline(g, x0 + 6, z0 + 6, x1 - 6, z1 - 6, 1.2, 9, a.path, false); }
  // room label anchors (floor centres)
  for (const [name, x0, z0, x1, z1] of P.rooms) anchors['room:' + name] = V((x0 + x1) / 2, 0, (z0 + z1) / 2);
  return { W: Wd, D: Dp, camera: P.camera, anchors, ik, rooms: P.rooms, kitchen };
}
function splitFull(horiz, x0, z0, x1, z1, fulls) {
  // split a wall into [full-height part(s)] and low parts
  const segs = []; const a0 = horiz ? x0 : z0, a1 = horiz ? x1 : z1;
  let cuts = [];
  for (const [p0, q0, p1, q1] of fulls) { if (horiz && q0 === z0 && q1 === z0) cuts.push([p0, p1]); if (!horiz && p0 === x0 && p1 === x0) cuts.push([q0, q1]); }
  cuts.sort((u, v) => u[0] - v[0]); let s = a0;
  for (const [c0, c1] of cuts) { if (c0 > s) segs.push(horiz ? [s, z0, c0, z0, false] : [x0, s, x0, c0, false]); segs.push(horiz ? [c0, z0, c1, z0, true] : [x0, c0, x0, c1, true]); s = c1; }
  if (s < a1) segs.push(horiz ? [s, z0, a1, z0, false] : [x0, s, x0, a1, false]);
  return segs;
}

// 2Bay: compact ㄱ-shaped kitchen in the back-left corner, robot docked in a tall cabinet (Dock / Fold-out)
function k2(g, anchors) {
  const a = amat(); const kg = new THREE.Group(); kg.position.set(10, 0, 10); g.add(kg);
  // back run x 0..260 (z 0..60), side run along x = 0 (z 60..240), tall dock+DW unit at x 260..320
  baseRun(kg, 0, 260, { doorW: 60 });
  const sk = sink(kg, 200, { w: 76 });
  counter(kg, 0, 260, { holes: [[sk.x0, sk.x1, 10, 52]] });
  backsplash(kg, 0, 260); upperRun(kg, 0, 238, { doorW: 60 });
  // side run (rotated): build in a sub-group rotated -90° about Y so its back wall is x = 0
  const sg = new THREE.Group(); sg.rotation.y = Math.PI / 2; sg.position.set(0, 0, 240); kg.add(sg);   // local x -> world -z
  baseRun(sg, 0, 180, { doorW: 60 }); counter(sg, 0, 180, {}); const ih = induction(sg, 92, { w: 56 }); backsplash(sg, 0, 180); upperRun(sg, 0, 180, { doorW: 60 });
  // tall unit: elevated DW (bottom) + robot home niche (top); robot base on a fold-out swing plate
  const t = tallDW(kg, 260, { w: 60, dwOpen: 1, rackOut: 1, stOut: 0, homeTop: true });
  const dock = new THREE.Group(); dock.position.set(290, 150, 30); kg.add(dock);
  dock.add(bx(-14, 0, -24, 14, 4, 36, a.rail, 1.0));
  dock.add(bx(-14, 1, 36, 14, 3, 36.6, a.railAccent));
  const robot = makeRobot(0.95); robot.rotation.x = Math.PI; robot.position.set(290, 150, 54); kg.add(robot); kg.updateMatrixWorld(true);
  const r = reach(robot, kg.localToWorld(V(226, 100, 38)), V(0, -1, 0), V(0, 0, 1), RB_Q0);
  attachHeld(robot, 'plateV');
  const p1 = plate(12.5); p1.position.set(120, 88.2, 32); kg.add(p1);
  const b1 = bowl(6.5, 6); b1.position.set(150, 88.2, 22); kg.add(b1);
  table(g, 70, 450, 250, 540);
  const zg = new THREE.Group(); g.add(zg);
  zone(zg, 'robot', 150, 11, 270, 72, 88.9); zone(zg, 'human', 82, 86, 330, 250); zone(zg, 'nogo', 11, 118, 71, 198, 89.6);
  reachVolume(zg, 150, 330, 10, 82, 89, 150);
  Object.assign(anchors, { home: V(300, 170, 50), rail: V(282, 150, 60), sink: V(210, 80, 40), dw: V(300, 90, 80), storage: V(226, 183, 42), ih: V(40, 92, 158),
    robotZone: V(180, 89, 46), humanZone: V(200, 0, 180), nogo: V(40, 89, 158), reach: V(200, 150, 92), __ik: { posErr: +r.posErr.toFixed(2), rotErr: +r.rotErr.toFixed(3) } });
}

// 4Bay: open kitchen with island; wall-side run carries the rail robot, the island (IH) is the human zone
function k4(g, anchors) {
  const a = amat(); const kg = new THREE.Group(); kg.position.set(540, 0, 10); g.add(kg);
  const k = arkiLinearKitchen(kg, 0, { tall: { dwOpen: 1, rackOut: 1, stOut: 0 } });
  // island with induction (human zone), x 60..300 (local), z 190..280
  const ig = new THREE.Group(); ig.position.set(540, 0, 10); g.add(ig);
  ig.add(bx(70, 0, 190, 290, 10, 276, a.dark)); ig.add(bx(70, 10, 188, 290, 85, 278, a.cabLower)); ig.add(bx(62, 85, 182, 298, 88.2, 284, a.quartz));
  const hob = rbox(56, 0.7, 50, 0.3, a.hob, 2); hob.position.set(180, 88.6, 233); ig.add(hob);
  for (let i = 0; i < 3; i++) { const st = new THREE.Group(); st.position.set(110 + i * 70, 0, 318); ig.add(st);
    st.add(bx(-17, 62, -17, 17, 66, 17, a.chair)); st.add(bx(-1.5, 0, -1.5, 1.5, 62, 1.5, a.chair)); }
  const R = placeRobot(kg, k, 'pick', 1.0);
  const zg = new THREE.Group(); g.add(zg);
  zone(zg, 'robot', 584, 11, 840, 72, 88.9); zone(zg, 'human', 540, 86, 900, 360); zone(zg, 'nogo', 602, 192, 838, 294, 88.9);
  reachVolume(zg, 584, 840, 10, 78, 89, 139);
  Object.assign(anchors, { home: V(562, 160, 40), rail: V(690, 145, 34), sink: V(710, 80, 40), dw: V(870, 90, 70), storage: V(870, 150, 40), ih: V(720, 92, 243),
    robotZone: V(620, 89, 46), humanZone: V(700, 0, 140), nogo: V(800, 89, 243), reach: V(780, 134, 76), __ik: R.ik });
}

// ---------------------------------------------------------------- building blocks for add-on scene modules (web/fig_flow.js). Export list only: no behaviour change.
export { bx, obst, baseRun, counter, sink, induction, upperRun, backsplash, underDW, table, zone, pathCurve, room, lights, camPersp, project,
  placeRobot, attachHeld, RB_Q0 };
