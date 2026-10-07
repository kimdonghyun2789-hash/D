// Real apartment plans (digitized JSON, mm, plan y down) -> 3D (cm, world x right, y up, z = plan y).
// Walls are cut at `cut` height (dollhouse view); window glass is shown as a light band; doors are gaps.
import * as THREE from 'three';

const S = 0.1;                       // mm -> cm
const V = (x, y, z) => new THREE.Vector3(x, y, z);

export function planMats() {
  const tex = (draw) => { const c = document.createElement('canvas'); c.width = c.height = 512; draw(c.getContext('2d'), 512, 512);
    const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t; };
  const wood = tex((g, w, h) => { g.fillStyle = '#d2b48e'; g.fillRect(0, 0, w, h); for (let r = 0; r < 8; r++) { let x = (r % 2) * 120;
      while (x < w + 260) { const len = 210 + ((r * 37 + x) % 3) * 45; const s = 186 + ((r * 13 + x * 7) % 18);
        g.fillStyle = `rgb(${s + 22},${s + 4},${s - 22})`; g.fillRect(x - 260, r * 64 + 1, len - 2, 62); x += len; } } });
  const tile = tex((g, w, h) => { g.fillStyle = '#d9dcdf'; g.fillRect(0, 0, w, h); g.strokeStyle = '#c3c7cc'; g.lineWidth = 3;
    for (let i = 0; i <= 512; i += 64) { g.beginPath(); g.moveTo(i, 0); g.lineTo(i, 512); g.stroke(); g.beginPath(); g.moveTo(0, i); g.lineTo(512, i); g.stroke(); } });
  const m = (o) => new THREE.MeshStandardMaterial(o);
  return {
    wood, tile,
    floorWood: m({ color: 0xffffff, map: wood, roughness: 0.75 }),
    floorWood2: m({ color: 0xf2ece4, map: wood, roughness: 0.75 }),
    floorTile: m({ color: 0xffffff, map: tile, roughness: 0.6 }),
    floorBalc: m({ color: 0xe6e2da, map: tile, roughness: 0.7 }),
    floorCore: m({ color: 0xc9c9c6, roughness: 0.9 }),
    wall: m({ color: 0xf1eee8, roughness: 0.92 }),
    wallCut: m({ color: 0x2e3136, roughness: 0.8 }),
    glass: new THREE.MeshPhysicalMaterial({ color: 0xa9c4d6, roughness: 0.05, transparent: true, opacity: 0.45 }),
    frame: m({ color: 0x9aa1a9, roughness: 0.5, metalness: 0.3 }),
    sanitary: new THREE.MeshPhysicalMaterial({ color: 0xf6f6f4, roughness: 0.25, clearcoat: 0.5 }),
    wardrobe: m({ color: 0xe4ddd2, roughness: 0.7 }),
    bed: m({ color: 0xd8d2c7, roughness: 0.9 }), sofa: m({ color: 0xa79f94, roughness: 0.9 }), table: m({ color: 0xb48c64, roughness: 0.6 }),
  };
}

const FLOOR_KIND = { living: 'floorWood', kitchen: 'floorWood', dining: 'floorWood', corridor: 'floorWood', bedroom: 'floorWood2', dress: 'floorWood2',
  closet: 'floorWood2', pantry: 'floorWood', bath: 'floorTile', utility: 'floorBalc', balcony: 'floorBalc', evac: 'floorBalc', outdoor_unit: 'floorBalc',
  entry: 'floorTile', core: 'floorCore' };

function box(x0, y0, z0, x1, y1, z1, mat) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(Math.max(0.1, x1 - x0), Math.max(0.1, y1 - y0), Math.max(0.1, z1 - z0)), mat);
  m.position.set((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2); m.castShadow = true; m.receiveShadow = true; return m;
}
function floorRect(g, r, y, mat) {
  const [x0, z0, x1, z1] = r.map(v => v * S);
  const geo = new THREE.PlaneGeometry(x1 - x0, z1 - z0);
  const uv = geo.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * (x1 - x0) / 120, uv.getY(i) * (z1 - z0) / 120);
  const m = new THREE.Mesh(geo, mat); m.rotation.x = -Math.PI / 2; m.position.set((x0 + x1) / 2, y, (z0 + z1) / 2); m.receiveShadow = true; g.add(m);
}

// openings lying on a wall: returns [[a0,a1,kind], ...] in mm along the wall axis
function openingsOn(w, P) {
  const horiz = Math.abs(w.y1 - w.y2) < 1;
  const lo = horiz ? Math.min(w.x1, w.x2) : Math.min(w.y1, w.y2), hi = horiz ? Math.max(w.x1, w.x2) : Math.max(w.y1, w.y2);
  const c = horiz ? w.y1 : w.x1, tol = Math.max(80, (w.t || 150));
  const out = [];
  const take = (o, kind) => {
    const oh = Math.abs(o.y1 - o.y2) < 1, ov = Math.abs(o.x1 - o.x2) < 1;
    if (horiz && !oh) return; if (!horiz && !ov) return;
    const oc = horiz ? o.y1 : o.x1; if (Math.abs(oc - c) > tol) return;
    let a0 = horiz ? Math.min(o.x1, o.x2) : Math.min(o.y1, o.y2), a1 = horiz ? Math.max(o.x1, o.x2) : Math.max(o.y1, o.y2);
    a0 = Math.max(a0, lo); a1 = Math.min(a1, hi); if (a1 - a0 > 20) out.push([a0, a1, kind]);
  };
  (P.doors || []).forEach(o => take(o, 'door'));
  (P.windows || []).forEach(o => take(o, 'window'));
  out.sort((p, q) => p[0] - q[0]);
  return { horiz, lo, hi, c, ops: out };
}

export function buildWalls(g, P, M, opts = {}) {
  const cut = opts.cut ?? 110, full = opts.full ?? 240, sill = opts.sill ?? 90, head = opts.head ?? 210;
  const fullRanges = opts.fullRanges || (() => []);     // (wall) -> [[a0, a1], ...] (mm along the wall) shown full height
  for (const w of P.walls || []) {
    const { horiz, lo, hi, c, ops } = openingsOn(w, P);
    const t = (w.t || (w.exterior ? 200 : 120)) * S;
    const FR = fullRanges(w);
    const hAt = (a) => FR.some(([r0, r1]) => a >= r0 - 1 && a <= r1 + 1) ? full : cut;
    // split [a0,a1] at full-range boundaries -> [[s0,s1,H], ...]
    const spans = (a0, a1) => {
      const cuts = [a0, a1]; for (const [r0, r1] of FR) { if (r0 > a0 && r0 < a1) cuts.push(r0); if (r1 > a0 && r1 < a1) cuts.push(r1); }
      cuts.sort((p, q) => p - q); const out = [];
      for (let i = 0; i < cuts.length - 1; i++) if (cuts[i + 1] - cuts[i] > 1) out.push([cuts[i], cuts[i + 1], hAt((cuts[i] + cuts[i + 1]) / 2)]);
      return out;
    };
    const piece = (a0, a1, y0, y1, mat, H) => {
      if (a1 - a0 < 1 || y1 - y0 < 0.5) return;
      const A0 = a0 * S, A1 = a1 * S, C = c * S;
      g.add(horiz ? box(A0, y0, C - t / 2, A1, y1, C + t / 2, mat) : box(C - t / 2, y0, A0, C + t / 2, y1, A1, mat));
      if (y1 >= H - 0.01 && H < full) {
        const cap = horiz ? box(A0, y1, C - t / 2, A1, y1 + 0.6, C + t / 2, M.wallCut) : box(C - t / 2, y1, A0, C + t / 2, y1 + 0.6, A1, M.wallCut);
        cap.castShadow = false; g.add(cap);
      }
    };
    const solid = (a0, a1) => { for (const [s0, s1, H] of spans(a0, a1)) piece(s0, s1, 0, H, M.wall, H); };
    let cur = lo - (w.t || 150) / 2; const e0 = hi + (w.t || 150) / 2;
    for (const [a0, a1, kind] of ops) {
      solid(cur, a0);
      for (const [s0, s1, H] of spans(a0, a1)) {
        if (kind === 'window') {
          piece(s0, s1, 0, Math.min(sill, H), M.wall, H);
          if (H > sill) {
            const gt = 2.4, C = c * S, A0 = s0 * S, A1 = s1 * S, top = Math.min(head, H);
            const gl = horiz ? box(A0, sill, C - gt / 2, A1, top, C + gt / 2, M.glass) : box(C - gt / 2, sill, A0, C + gt / 2, top, A1, M.glass);
            gl.castShadow = false; g.add(gl);
            if (H > head) piece(s0, s1, head, H, M.wall, H);
          }
        } else if (H > head) piece(s0, s1, head, H, M.wall, H);
      }
      cur = a1;
    }
    solid(cur, e0);
  }
}

export function buildFloors(g, P, M) {
  for (const r of P.rooms || []) {
    const mat = M[FLOOR_KIND[r.kind] || 'floorWood'];
    const lift = ['bath', 'balcony', 'utility', 'evac', 'outdoor_unit', 'entry'].includes(r.kind) ? 0.02 : 0.06;
    for (const rc of r.rects || []) floorRect(g, rc, lift, mat);
  }
}

export function buildFixtures(g, P, M, opts = {}) {
  const H = { bathtub: 55, toilet: 42, washbasin: 82, shower: 4, wardrobe: opts.tallCap ?? 105, shoe_cabinet: opts.tallCap ?? 105, utility_sink: 80, washer: 85,
    bed: 45, sofa: 42, table: 73 };
  const MAT = { bathtub: 'sanitary', toilet: 'sanitary', washbasin: 'sanitary', shower: 'sanitary', utility_sink: 'sanitary', washer: 'sanitary',
    wardrobe: 'wardrobe', shoe_cabinet: 'wardrobe', bed: 'bed', sofa: 'sofa', table: 'table' };
  for (const f of P.fixtures || []) {
    const h = H[f.kind]; if (!h) continue;
    g.add(box(f.x0 * S, 0, f.y0 * S, f.x1 * S, h, f.y1 * S, M[MAT[f.kind]]));
  }
}

// room centre anchors (largest rect of each room)
export function roomAnchors(P) {
  const out = {};
  for (const r of P.rooms || []) {
    let best = null, ba = -1;
    for (const rc of r.rects || []) { const a = (rc[2] - rc[0]) * (rc[3] - rc[1]); if (a > ba) { ba = a; best = rc; } }
    if (best) out['room:' + r.name] = V((best[0] + best[2]) / 2 * S, 1, (best[1] + best[3]) / 2 * S);
  }
  return out;
}

export function planBounds(P) {
  return { W: P.overall.width * S, D: P.overall.depth * S };
}
