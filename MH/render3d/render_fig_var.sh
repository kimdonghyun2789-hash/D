# Kitchen Variation figures (m04 · B2): secured plans AS DRAWN (arki=0, no robot) -> MH/assets/renders/fig_var_*
#  fig_var_k_<id>   m04 strip: kitchen of each plan, orthographic axonometric from the room side (corner diagonal, elevation 43.5 deg),
#                   same scale for all 4 (window 520 cm wide = 800 px), cropped from a 3200x2400 full-unit render
#  fig_var_top_<id> B2 thumbnails: existing top views (plan_<id>_top_orig) trimmed + rescaled to one scale (0.8 px/cm),
#                   JSON 'kitchen' = 주방/식당 outline (union of room rects, inset 30 cm) in image px
set -e
cd "$(dirname "$0")"
O=../assets/renders
T=out/fig_var
mkdir -p $T
N="node shot.js plan"
# camera direction = from the inside corner of the two counter back walls toward the room (horizontal), dir3 y = 1
$N $T/k_old2a.png 3200 2400 "id=old2a&arki=0&dir3=0.7071,1,0.7071&pad=0.02" > /dev/null
$N $T/k_old2b.png 3200 2400 "id=old2b&arki=0&dir3=-0.7071,1,-0.7071&pad=0.02" > /dev/null
$N $T/k_new3.png 3200 2400 "id=new3&arki=0&dir3=-0.7071,1,0.7071&pad=0.02" > /dev/null
$N $T/k_new4.png 3200 2400 "id=new4&arki=0&dir3=-0.7071,1,0.7071&pad=0.02" > /dev/null
python3 - <<'PY'
import json, math
from PIL import Image
O, T, PL = '../assets/renders', 'out/fig_var', 'plans'
IDS = ['old2a', 'old2b', 'new3', 'new4']


def solve3(A, b):
    det = lambda m: (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                     + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    D = det(A); out = []
    for i in range(3):
        m = [row[:] for row in A]
        for r in range(3): m[r][i] = b[r]
        out.append(det(m) / D)
    return out


def affine(P, anchors):
    """Floor-level room centres (largest rect, y = 1 cm) -> image px: p = a X + b Z + c (orthographic camera). Returns rows x, y and max error."""
    pts = []
    for r in P['rooms']:
        k = 'room:' + r['name']
        if k not in anchors: continue
        best = max(r['rects'], key=lambda rc: (rc[2] - rc[0]) * (rc[3] - rc[1]))
        pts.append(((best[0] + best[2]) / 20, (best[1] + best[3]) / 20, anchors[k]))
    res = []
    for j in (0, 1):
        A = [[0.0] * 3 for _ in range(3)]; b = [0.0] * 3
        for X, Z, p in pts:
            v = (X, Z, 1.0)
            for r in range(3):
                b[r] += v[r] * p[j]
                for c in range(3): A[r][c] += v[r] * v[c]
        res.append(solve3(A, b))
    err = max(abs(res[j][0] * X + res[j][1] * Z + res[j][2] - p[j]) for X, Z, p in pts for j in (0, 1))
    return res[0], res[1], err


def outline(rects, inset):
    """Outline of a union of axis-aligned rects (clockwise, y down), each edge moved `inset` inward."""
    xs = sorted({v for r in rects for v in (r[0], r[2])}); ys = sorted({v for r in rects for v in (r[1], r[3])})
    def cov(i, j):
        if i < 0 or j < 0 or i >= len(xs) - 1 or j >= len(ys) - 1: return False
        cx, cy = (xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2
        return any(r[0] <= cx <= r[2] and r[1] <= cy <= r[3] for r in rects)
    nxt = {}
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            if not cov(i, j): continue
            x0, x1, y0, y1 = xs[i], xs[i + 1], ys[j], ys[j + 1]
            if not cov(i, j - 1): nxt[(x0, y0)] = (x1, y0)
            if not cov(i + 1, j): nxt[(x1, y0)] = (x1, y1)
            if not cov(i, j + 1): nxt[(x1, y1)] = (x0, y1)
            if not cov(i - 1, j): nxt[(x0, y1)] = (x0, y0)
    st = min(nxt); poly = [st]; cur = nxt[st]
    while cur != st: poly.append(cur); cur = nxt[cur]
    n = len(poly)
    poly = [poly[k] for k in range(n) if (poly[k][0] - poly[k - 1][0]) * (poly[(k + 1) % n][1] - poly[k][1])
            - (poly[k][1] - poly[k - 1][1]) * (poly[(k + 1) % n][0] - poly[k][0]) != 0]
    n = len(poly); out = []
    for k in range(n):
        a, b, c = poly[k - 1], poly[k], poly[(k + 1) % n]
        e1, e2 = (b[0] - a[0], b[1] - a[1]), (c[0] - b[0], c[1] - b[1])
        hz, vt = (e1, e2) if e1[1] == 0 else (e2, e1)              # one horizontal, one vertical edge per corner
        ny = inset if hz[0] > 0 else -inset                        # interior is right of travel (clockwise, y down)
        nx = -inset if vt[1] > 0 else inset
        out.append((b[0] + nx, b[1] + ny))
    return out


# ---- m04: same-scale kitchen windows from the full-unit axonometric renders
WIN, OW, ASP, UP = 520.0, 800, 1.0921, 105.0          # window width cm, output px, aspect w/h (m04 tile 1.66 x 1.52 in), window centre height cm
COSE = math.cos(math.atan(0.95))                      # dir3 y = 1 -> elevation atan(0.95)
for id in IDS:
    P = json.load(open(f'{PL}/{id}.json')); J = json.load(open(f'{T}/k_{id}.json'))
    ax, ay, err = affine(P, J['anchors']); s = math.hypot(ax[0], ax[1])
    K = P['kitchen']
    bx = [(c['x0'], c['y0'], c['x1'], c['y1']) for c in K['counters']]
    if K.get('fridge'): f = K['fridge']; bx.append((f['x0'], f['y0'], f['x1'], f['y1']))
    X = (min(b[0] for b in bx) + max(b[2] for b in bx)) / 20; Z = (min(b[1] for b in bx) + max(b[3] for b in bx)) / 20
    cx = ax[0] * X + ax[1] * Z + ax[2]; cy = ay[0] * X + ay[1] * Z + ay[2] - UP * COSE * s
    w = WIN * s; h = w / ASP
    box = (round(cx - w / 2), round(cy - h / 2), round(cx + w / 2), round(cy + h / 2))
    Image.open(f'{T}/k_{id}.png').crop(box).resize((OW, round(OW / ASP)), Image.LANCZOS).save(f'{O}/fig_var_k_{id}.png', optimize=True)
    sc = OW / w
    def proj(Xc, Zc, Y=0.0):
        return [round((ax[0] * Xc + ax[1] * Zc + ax[2] - box[0]) * sc), round((ay[0] * Xc + ay[1] * Zc + ay[2] - Y * COSE * s - box[1]) * sc)]
    A = {}
    if K.get('sink'): A['sink'] = proj(K['sink']['x'] / 10, K['sink']['y'] / 10, 88)
    if K.get('cooktop'): A['cooktop'] = proj(K['cooktop']['x'] / 10, K['cooktop']['y'] / 10, 88)
    if K.get('fridge'): A['fridge'] = proj((f['x0'] + f['x1']) / 20, (f['y0'] + f['y1']) / 20, 180)
    for c in K['counters']: A[c['role']] = proj((c['x0'] + c['x1']) / 20, (c['y0'] + c['y1']) / 20, 88)
    json.dump({'anchors': A, 'px_per_cm': round(OW / WIN, 4), 'window_cm': WIN, 'fit_err_px': round(err, 2),
               'source': f'plans/{id}.json as drawn (arki=0), orthographic, camera from the counter corner toward the room'},
              open(f'{O}/fig_var_k_{id}.json', 'w'), ensure_ascii=False)
    print('k', id, 'src px/cm', round(s, 3), 'fit err px', round(err, 2))

# ---- B2: existing top views, trimmed and rescaled to one scale + kitchen outline
Q, M, INSET = 0.8, 6, 300                              # px per cm, margin px, outline inset mm
for id in IDS:
    P = json.load(open(f'{PL}/{id}.json')); src = f'{O}/plan_{id}_top_orig'
    J = json.load(open(src + '.json')); im = Image.open(src + '.png')
    ax, ay, err = affine(P, J['anchors']); s = (ax[0] + ay[1]) / 2       # top view: px = s X + a, py = s Z + b
    l, t, r, b = im.getchannel('A').getbbox(); l, t, r, b = max(0, l - M), max(0, t - M), min(im.width, r + M), min(im.height, b + M)
    k = Q / s
    im.crop((l, t, r, b)).resize((round((r - l) * k), round((b - t) * k)), Image.LANCZOS).save(f'{O}/fig_var_top_{id}.png', optimize=True)
    to = lambda Xc, Zc: [round((ax[0] * Xc + ax[1] * Zc + ax[2] - l) * k, 1), round((ay[0] * Xc + ay[1] * Zc + ay[2] - t) * k, 1)]
    room = next(rr for rr in P['rooms'] if rr['name'] == '주방/식당')
    poly = [to(x / 10, y / 10) for x, y in outline(room['rects'], INSET)]
    A = {kk: [round((p[0] - l) * k, 1), round((p[1] - t) * k, 1)] for kk, p in J['anchors'].items()}
    json.dump({'anchors': A, 'kitchen': poly, 'px_per_cm': Q, 'fit_err_px': round(err, 2), 'plan_mm': [P['overall']['width'], P['overall']['depth']],
               'source': f'plan_{id}_top_orig.png (as drawn) trimmed + rescaled'}, open(f'{O}/fig_var_top_{id}.json', 'w'), ensure_ascii=False)
    print('top', id, 'src px/cm', round(s, 4), 'fit err px', round(err, 2), 'size', round((r - l) * k), round((b - t) * k))
PY
