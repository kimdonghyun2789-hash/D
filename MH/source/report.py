# Detailed Word report: MH Robotics · Seed · TIPS 사업계획 상세 보고서.
# Numbers come from model.json / content.py only. Prose is 개조식 (□ ○ - ·). Internal Q&A and the investment memo are not included.
# usage: python3 report.py [--pdf]      (writes ../MH_Robotics_Seed_TIPS_Report.docx, and the PDF preview with --pdf)
import json, os, re, shutil, subprocess, sys, tempfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageChops, ImageDraw, ImageFont

import content as C
import model

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
RD = os.path.join(ROOT, 'assets', 'renders')
FIG = os.path.join(HERE, '_report_fig')
OUT = os.path.join(ROOT, 'MH_Robotics_Seed_TIPS_Report.docx')
PDF = os.path.join(ROOT, 'MH_Robotics_Seed_TIPS_Report.pdf')
SPEC = os.path.join(FIG, 'report_spec.json')
FONT_DIR = '/root/.fonts'

M = C.M; F = C.F; TP = C.TP; KL = C.KL; MK = C.MK; A = C.A; H3 = C.H3; H5 = C.H5
HH = M['household']; SC = M['scenarios']; B = SC['B']
VA = M['value']; PI = M['partner_irr']['B']; CONS = M['cons']; CARE = M['care']; RENT = M['rental']
IN = {d['key']: d for d in M['inputs']}
SRC = {s['id']: s for s in json.load(open(os.path.join(HERE, 'sources.json'), encoding='utf-8'))}

INK, INK2, GREY, EDGE, SOFT, ACC = '#15171A', '#4A4F57', '#8C9198', '#C9CDD2', '#F4F5F6', '#E2571B'
TITLE = 'MH Robotics — Kitchen Manipulation Robotics System'
HEADER = 'MH Robotics · Seed · TIPS 사업계획 상세 보고서'


def v(k, s='B'):
    return IN[k]['vals'][s]


def nf(x, d=0):
    return f"{x:,.{d}f}"


def man(x, d=0):
    return f"{x:,.{d}f}만원"


def eok(x, d=1):                      # x in 만원
    return f"{x / 1e4:,.{d}f}억원"


def pct(x, d=0):
    return f"{x * 100:.{d}f}%"


# ================================================================ blocks
BL, TOC = [], []
NT, NF = [0], [0]


def h1(t, newpage=True):
    TOC.append((1, t)); BL.append({'t': 'h1', 'text': t, 'newpage': newpage})


def h2(t):
    TOC.append((2, t)); BL.append({'t': 'h2', 'text': t})


def h3(t):
    BL.append({'t': 'h3', 'text': t})


LV = {'□': 0, '○': 1, '-': 2, '·': 3}


def gj(*lines):
    """개조식 lines: '□ ' lv0 · '○ ' lv1 · '- ' lv2 · '· ' lv3."""
    for ln in lines:
        mk, txt = ln.split(' ', 1)
        assert mk in LV, ln
        assert not re.search(r'(습니다|합니다|입니다)', txt), txt
        BL.append({'t': 'b', 'lv': LV[mk], 'text': txt})


def table(caption, header, rows, widths, align=None, note=None, **k):
    NT[0] += 1
    assert abs(sum(widths) - 100) < 0.01 and all(len(r) == len(header) for r in rows), caption
    BL.append({'t': 'table', 'caption': f'<표 {NT[0]}> {caption}', 'header': header,
               'rows': [['' if c is None else str(c) for c in r] for r in rows], 'widths': widths,
               'align': align or ['l'] * len(header), 'note': note, **k})


def fig(f, caption, w_pct=100, note=None):
    NF[0] += 1
    BL.append({'t': 'fig', 'path': f['path'], 'w_px': f['w'], 'h_px': f['h'], 'w_pct': w_pct,
               'caption': f'[그림 {NF[0]}] {caption}', 'note': note})


def box(title, items):
    BL.append({'t': 'box', 'title': title, 'items': [{'lv': LV[s.split(' ', 1)[0]], 'text': s.split(' ', 1)[1]} for s in items]})


def tiles(items):
    BL.append({'t': 'tiles', 'items': [{'value': a, 'label': b, 'accent': c} for a, b, c in items]})


# ================================================================ charts (matplotlib, deck palette: greys + orange for key numbers)
for _f in ('NotoSansKR-400.ttf', 'NotoSansKR-700.ttf'):
    font_manager.fontManager.addfont(os.path.join(FONT_DIR, _f))
plt.rcParams.update({'font.family': 'Noto Sans KR', 'font.size': 8.5, 'axes.edgecolor': EDGE, 'axes.labelcolor': INK2,
                     'xtick.color': INK2, 'ytick.color': INK2, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.unicode_minus': False, 'axes.titlesize': 9, 'axes.titleweight': 'bold', 'axes.titlecolor': INK,
                     'legend.frameon': False, 'legend.fontsize': 8, 'xtick.major.size': 0, 'ytick.major.size': 0})


def _save(fg, name):
    p = os.path.join(FIG, name + '.png')
    fg.savefig(p, dpi=220, facecolor='white', bbox_inches='tight', pad_inches=0.06)
    plt.close(fg)
    w, h = Image.open(p).size
    return {'path': p, 'w': w, 'h': h}


def _grid(ax, axis='y'):
    ax.grid(axis=axis, color='#E6E8EB', lw=0.6)
    ax.set_axisbelow(True)


def ch_waterfall():
    h = H3; c = h['C']
    steps = [('Robot BOM', c['robot']), ('Interface Kit\n· 설치 · 물류', c['kitchen'] + c['comm'] + c['log']),
             ('Care · 소모품\n· Warranty', c['care'] + c['cons'] + c['warranty']), ('채널비용\n(획득)', c['channel']),
             ('Skill · Tool\n원가', c['sw'] + c['tool'])]
    assert abs(sum(x for _, x in steps) - h['cost5']) < 0.05
    fg, ax = plt.subplots(figsize=(6.6, 2.75))
    labels = ['5년 매출'] + [s for s, _ in steps] + ['누적\n공헌이익']
    top = h['rev5']
    ax.bar(0, top, width=0.62, color='#4A4F57')
    ax.text(0, top + 40, nf(top), ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=INK)
    for i, (_, x) in enumerate(steps, 1):
        ax.bar(i, x, bottom=top - x, width=0.62, color='#B4B8BE')
        ax.plot([i - 1 + 0.31, i - 0.31], [top, top], color=GREY, lw=0.6)
        ax.text(i, top + 40, f"−{nf(x)}", ha='center', va='bottom', fontsize=8, color=INK2)
        top -= x
    n = len(labels) - 1
    ax.plot([n - 1 + 0.31, n - 0.31], [top, top], color=GREY, lw=0.6)
    ax.bar(n, h['contrib5'], width=0.62, color=ACC)
    ax.text(n, h['contrib5'] + 40, f"{nf(h['contrib5'])} ({pct(h['cm5'])})", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=ACC)
    ax.set_xticks(range(len(labels)), labels, fontsize=7.8)
    ax.set_ylim(0, h['rev5'] * 1.13); ax.set_ylabel('만원 (5년 누적)')
    _grid(ax)
    return _save(fg, 'ch_waterfall')


PATHS = [('purchase_direct', 'Remodeling 구매 (직접)'), ('purchase_partner', 'Remodeling 구매 (Partner)'),
         ('rental_direct', 'Remodeling Rental (MH 보유)'), ('rental_partner', 'Remodeling Rental (Partner 경유)'),
         ('retrofit_purchase', 'Retrofit 구매'), ('newbuild_purchase', 'New-build 구매')]


def ch_paths():
    fg, ax = plt.subplots(figsize=(6.6, 2.9))
    ys = list(range(len(PATHS)))[::-1]
    for (k, lab), y in zip(PATHS, ys):
        a3, a5 = HH[k + '_Y3'], HH[k + '_Y5']
        ax.barh(y + 0.19, a3['contrib5'], height=0.36, color='#B4B8BE', label='Y3 원가 기준' if y == ys[0] else None)
        ax.barh(y - 0.19, a5['contrib5'], height=0.36, color='#4A4F57', label='Y5 원가 기준' if y == ys[0] else None)
        ax.text(a3['contrib5'] + 12, y + 0.19, f"{nf(a3['contrib5'])} ({pct(a3['cm5'])})", va='center', fontsize=7.6, color=INK2)
        ax.text(a5['contrib5'] + 12, y - 0.19, f"{nf(a5['contrib5'])} ({pct(a5['cm5'])})", va='center', fontsize=7.6, color=INK, fontweight='bold')
    ax.set_yticks(ys, [lab for _, lab in PATHS])
    ax.set_xlim(0, max(HH[k + '_Y5']['contrib5'] for k, _ in PATHS) * 1.28)
    ax.set_xlabel('세대당 5년 누적 공헌이익 (만원, 괄호 = 공헌이익률)')
    ax.legend(loc='lower left', bbox_to_anchor=(0, 1.0), ncol=2)
    _grid(ax, 'x')
    return _save(fg, 'ch_paths')


def ch_tornado(sens, name, unit_div=1, unit='만원', base_lab=''):
    items = sens['items']
    fg, ax = plt.subplots(figsize=(6.6, 0.3 * len(items) + 0.75))
    ys = list(range(len(items)))[::-1]
    mx = max(max(abs(d['lo']), abs(d['hi'])) for d in items) / unit_div
    for d, y in zip(items, ys):
        lo, hi = d['lo'] / unit_div, d['hi'] / unit_div
        ax.barh(y, lo, height=0.58, color='#B4B8BE', label='불리' if y == ys[0] else None)
        ax.barh(y, hi, height=0.58, color='#4A4F57', label='유리' if y == ys[0] else None)
        ax.text(lo - mx * 0.02, y, f"{lo:+,.0f}".replace('-', '−'), va='center', ha='right', fontsize=7.5, color=INK2)
        ax.text(hi + mx * 0.02, y, f"{hi:+,.0f}", va='center', ha='left', fontsize=7.5, color=INK)
    ax.axvline(0, color=INK, lw=0.9)
    ax.set_yticks(ys, [d['name'] for d in items], fontsize=7.8)
    ax.set_xlim(-mx * 1.28, mx * 1.28)
    ax.set_xlabel(f'{base_lab} 대비 변화 ({unit})')
    ax.legend(loc='lower right', ncol=2)
    _grid(ax, 'x')
    return _save(fg, name)


CH_COL = ['#5C6169', '#9DA2A9', '#D5D8DC']


def ch_market():
    labs = ['① Remodeling', '② Retrofit', '③ New-build']
    hh = [MK['fit'] * 1000, MK['retro_annual'] * 1000, MK['new_opt'] * 1000]
    am = [MK['sam_remodel'], MK['sam_retro'], MK['sam_new']]
    fg, axs = plt.subplots(1, 2, figsize=(6.6, 1.75))
    for ax, vals, ttl, fmt in ((axs[0], hh, '연 대상 세대 (세대)', '{:,.0f}'), (axs[1], am, '연 규모 (억원)', '{:,.0f}')):
        ys = [2, 1, 0]
        ax.barh(ys, vals, height=0.6, color=CH_COL)
        for y, val in zip(ys, vals):
            ax.text(val + max(vals) * 0.02, y, fmt.format(val), va='center', fontsize=8, color=INK, fontweight='bold' if y == 2 else 'normal')
        ax.set_yticks(ys, labs); ax.set_xlim(0, max(vals) * 1.25); ax.set_xticks([])
        ax.spines['bottom'].set_visible(False); ax.set_title(ttl, loc='left')
    axs[1].set_yticklabels([])
    fg.tight_layout(w_pad=1.5)
    return _save(fg, 'ch_market')


def ch_installs():
    yrs = M['years']
    ser = [('Remodeling 직접', B['rd'], '#3A3F47'), ('Remodeling Partner', B['rp'], '#6B7078'),
           ('Retrofit', B['rt'], '#A3A8AF'), ('New-build 입주', B['ni'], '#D5D8DC')]
    fg, ax = plt.subplots(figsize=(6.6, 2.5))
    bot = [0.0] * 5
    for lab, vals, col in ser:
        ax.bar(range(5), vals, bottom=bot, width=0.56, color=col, label=lab, edgecolor='white', linewidth=0.8)
        bot = [a + b for a, b in zip(bot, vals)]
    for i, t in enumerate(bot):
        ax.text(i, t + 8, f"{t:,.0f}세대", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=ACC if i == 4 else INK)
    assert abs(bot[4] - B['kitchens'][4]) < 1e-6
    ax.set_xticks(range(5), yrs); ax.set_ylim(0, bot[4] * 1.18); ax.set_ylabel('연간 설치 세대')
    ax.legend(loc='upper left', ncol=2)
    _grid(ax)
    return _save(fg, 'ch_installs')


def ch_rev_layers():
    lay = [('INSTALL (Robot · Interface · 설치)', [a / 1e4 for a in B['install']], INK),
           ('OPERATE (Rental · Care · 소모품)', [a / 1e4 for a in B['recurring']], '#6B7078'),
           ('EXPAND (Skill · Tool)', [a / 1e4 for a in B['expand']], '#B4B8BE')]
    fg, ax = plt.subplots(figsize=(6.6, 2.5))
    bot = [0.0] * 5
    for lab, vals, col in lay:
        ax.bar(range(5), vals, bottom=bot, width=0.56, color=col, label=lab, edgecolor='white', linewidth=0.8)
        bot = [a + b for a, b in zip(bot, vals)]
    for i, t in enumerate(bot):
        assert abs(t - B['rev'][i] / 1e4) < 1e-6
        ax.text(i, t + 1.2, f"{t:,.1f}억원", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=ACC if i == 4 else INK)
    ax.set_xticks(range(5), M['years']); ax.set_ylim(0, bot[4] * 1.18); ax.set_ylabel('매출 (억원)')
    ax.legend(loc='upper left')
    _grid(ax)
    return _save(fg, 'ch_rev_layers')


def ch_scen():
    fg, ax = plt.subplots(figsize=(6.6, 2.4))
    sty = [('C', 'Conservative', '#A3A8AF', '--'), ('B', 'Base', INK, '-'), ('U', 'Upside', '#6B7078', '-')]
    for k, lab, col, ls in sty:
        vals = [a / 1e4 for a in SC[k]['rev']]
        ax.plot(range(5), vals, color=col, ls=ls, lw=2, marker='o', ms=4.5, label=lab)
        ax.text(4.12, vals[4], f"{vals[4]:,.1f}", va='center', fontsize=8.5, color=ACC if k == 'B' else INK2, fontweight='bold' if k == 'B' else 'normal')
    ax.set_xticks(range(5), M['years']); ax.set_xlim(-0.2, 4.6); ax.set_ylabel('매출 (억원)')
    ax.legend(loc='upper left')
    _grid(ax)
    return _save(fg, 'ch_scen')


def ch_cash():
    op = [a / 1e4 for a in B['op']]; cum = [a / 1e4 for a in B['cum_cash']]
    fg, ax = plt.subplots(figsize=(6.6, 2.5))
    ax.bar(range(5), op, width=0.36, color='#C9CDD2', label='영업이익 (연)')
    ax.plot(range(5), cum, color=INK, lw=2, marker='o', ms=4.5, label='누적 현금흐름')
    for i, x in enumerate(cum):
        ax.text(i + 0.21, x + 2, f"{x:,.1f}", ha='left', va='bottom', fontsize=8, color=ACC if i == 4 else INK, fontweight='bold')
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_xticks(range(5), [f"{y}\n영업이익 {x:,.1f}" for y, x in zip(M['years'], op)], fontsize=7.8)
    ax.set_ylim(min(cum) * 1.15, 8); ax.set_xlim(-0.5, 4.75); ax.set_ylabel('억원')
    ax.legend(loc='lower left')
    _grid(ax)
    return _save(fg, 'ch_cash')


def ch_uses():
    rows = sorted(F['uses'], key=lambda u: -sum(u['y']))
    fg, ax = plt.subplots(figsize=(6.6, 3.2))
    ys = list(range(len(rows)))[::-1]
    for u, y in zip(rows, ys):
        tot = sum(u['y']) / 1e4; tp = sum(u['tips']) / 1e4
        ax.barh(y, tp, height=0.6, color='#5C6169', label='TIPS 과제 편성' if y == ys[0] else None)
        ax.barh(y, tot - tp, left=tp, height=0.6, color='#C9CDD2', label='Seed (과제 외)' if y == ys[0] else None)
        ax.text(tot + 0.15, y, f"{tot:,.2f}", va='center', fontsize=7.6, color=INK)
    ax.set_yticks(ys, [u['cat'] for u in rows], fontsize=7.8)
    ax.set_xlabel('24개월 지출 (억원)'); ax.set_xlim(0, max(sum(u['y']) for u in rows) / 1e4 * 1.12)
    ax.legend(loc='lower right')
    _grid(ax, 'x')
    return _save(fg, 'ch_uses')


def fte_monthly():
    kinds = {'founder': 'Founder', 'rnd': 'R&D', 'biz': '사업 · 경영지원', 'ops': '사업 · 경영지원', 'field': '현장 (설치 · 서비스)'}
    out = {k: [0.0] * 24 for k in ('Founder', 'R&D', '사업 · 경영지원', '현장 (설치 · 서비스)')}
    for t in F['team']:
        for m in range(t['start'], 25):
            out[kinds[t['kind']]][m - 1] += t['frac']
    y1 = sum(sum(v[:12]) for v in out.values()) / 12; y2 = sum(sum(v[12:]) for v in out.values()) / 12
    assert abs(y1 - F['fte'][0]) < 1e-6 and abs(y2 - F['fte'][1]) < 1e-6, (y1, y2)
    return out


def ch_fte():
    out = fte_monthly()
    cols = ['#3A3F47', '#6B7078', '#A3A8AF', '#D5D8DC']
    fg, ax = plt.subplots(figsize=(6.6, 2.4))
    bot = [0.0] * 24
    for (lab, vals), col in zip(out.items(), cols):
        ax.bar(range(1, 25), vals, bottom=bot, width=0.78, color=col, label=lab, edgecolor='white', linewidth=0.5)
        bot = [a + b for a, b in zip(bot, vals)]
    ax.text(6.5, max(bot) * 1.02, f"Y1 평균 {F['fte'][0]:.1f}명", ha='center', fontsize=8, color=INK)
    ax.text(18.5, max(bot) * 1.02, f"Y2 평균 {F['fte'][1]:.1f}명", ha='center', fontsize=8, color=INK)
    ax.axvline(12.5, color=GREY, lw=0.7, ls='--')
    ax.set_xticks([1, 6, 12, 18, 24], ['M1', 'M6', 'M12', 'M18', 'M24']); ax.set_xlim(0.3, 24.7)
    ax.set_ylim(0, max(bot) * 1.12); ax.set_ylabel('인원 (FTE)')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=4, fontsize=7.6)
    _grid(ax)
    return _save(fg, 'ch_fte')


def ch_gantt():
    wps = [(w[0], w[1], *[int(x) for x in re.findall(r'\d+', w[2])]) for w in C.WP]
    fg, ax = plt.subplots(figsize=(6.6, 2.55))
    ys = list(range(len(wps)))[::-1]
    for (k, nm, s, e), y in zip(wps, ys):
        ax.barh(y, e - s + 1, left=s - 0.5, height=0.5, color='#B4B8BE')
        ax.text(-0.01, y, f"{k}  {nm}", va='center', ha='right', fontsize=7.6, color=INK, transform=ax.get_yaxis_transform())
    ms = {'WP1': [(4, 'v1'), (10, 'v2'), (18, 'v3')]}
    for k, pts in ms.items():
        y = ys[[w[0] for w in wps].index(k)]
        for m, t in pts:
            ax.plot(m, y, marker='D', ms=4.5, color=INK)
            ax.text(m - (0.7 if m % 6 == 0 else 0), y - 0.3, f"Hand {t}", ha='center', va='top', fontsize=6.8, color=INK2)
    y6 = ys[[w[0] for w in wps].index('WP6')]
    for a, b_, t in [(9, 12, '목업'), (13, 18, '주방 3종'), (19, 24, '실거주 3세대')]:
        ax.barh(y6, b_ - a + 1, left=a - 0.5, height=0.5, color='#6B7078', edgecolor='white', linewidth=1)
        ax.text((a + b_) / 2, y6, t, ha='center', va='center', fontsize=6.8, color='white', fontweight='bold')
    for g in (6, 12, 18, 24):
        ax.plot([g + 0.5, g + 0.5], [-0.6, ys[0] + 0.38], color=INK, lw=0.8, ls='--')
        ax.text(g + 0.5, ys[0] + 0.45, f"M{g} Gate", ha='center', va='bottom', fontsize=7.4, fontweight='bold', color=INK)
    ax.set_yticks([]); ax.set_xticks([1, 6, 12, 18, 24], ['M1', 'M6', 'M12', 'M18', 'M24'])
    ax.set_xlim(0.5, 24.9); ax.set_ylim(-0.6, ys[0] + 0.95)
    ax.spines['left'].set_visible(False)
    _grid(ax, 'x')
    return _save(fg, 'ch_gantt')


def ch_bom():
    bom = v('bom'); asp = v('p_robot')
    fg, ax = plt.subplots(figsize=(6.6, 2.3))
    ax.bar(range(5), bom, width=0.52, color=['#B4B8BE', '#B4B8BE', '#6B7078', '#B4B8BE', '#6B7078'])
    for i, x in enumerate(bom):
        ax.text(i, x + 25, f"{x:,}", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=INK)
    ax.axhline(asp, color=INK, lw=1.1, ls='--')
    ax.text(4.42, asp + 25, f"Robot ASP {asp:,}만원", ha='right', va='bottom', fontsize=8, color=INK)
    ax.set_xticks(range(5), [f"{y}\nHW 마진 {(1 - b / asp) * 100:+.0f}%".replace('-', '−') for y, b in zip(M['years'], bom)], fontsize=7.8)
    ax.set_ylim(0, max(bom) * 1.18); ax.set_ylabel('만원 / 대')
    _grid(ax)
    return _save(fg, 'ch_bom')


# ================================================================ render composites (PIL) — every product render carries a CONCEPT tag
FB, FR = os.path.join(FONT_DIR, 'NotoSansKR-700.ttf'), os.path.join(FONT_DIR, 'NotoSansKR-400.ttf')


def _font(px, bold=False):
    return ImageFont.truetype(FB if bold else FR, int(px))


class R:
    def __init__(self, name):
        im = Image.open(os.path.join(RD, name + '.png')).convert('RGBA')
        bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
        self.im = bg.convert('RGB')
        j = os.path.join(RD, name + '.json')
        self.a = {k: tuple(p) for k, p in json.load(open(j, encoding='utf-8')).get('anchors', {}).items()} if os.path.exists(j) else {}

    def crop(self, l, t, r, b):          # fractions of the current image
        W, H = self.im.size
        box = (int(l * W), int(t * H), int(r * W), int(b * H))
        self.im = self.im.crop(box)
        self.a = {k: (x - box[0], y - box[1]) for k, (x, y) in self.a.items()}
        return self

    def trim(self, pad=0.02):
        d = ImageChops.difference(self.im, Image.new('RGB', self.im.size, 'white')).convert('L').point(lambda p: 255 if p > 10 else 0)
        l, t, r, b = d.getbbox()
        W, H = self.im.size; p = int(pad * max(W, H))
        return self.crop(max(0, l - p) / W, max(0, t - p) / H, min(W, r + p) / W, min(H, b + p) / H)

    def width(self, w):
        s = w / self.im.width
        self.im = self.im.resize((int(w), int(round(self.im.height * s))), Image.LANCZOS)
        self.a = {k: (x * s, y * s) for k, (x, y) in self.a.items()}
        return self

    def fit(self, w, h):                 # contain into w×h on white
        s = min(w / self.im.width, h / self.im.height)
        nw, nh = int(self.im.width * s), int(self.im.height * s)
        im = self.im.resize((nw, nh), Image.LANCZOS)
        c = Image.new('RGB', (int(w), int(h)), 'white'); ox, oy = (int(w) - nw) // 2, (int(h) - nh) // 2
        c.paste(im, (ox, oy))
        self.im = c; self.a = {k: (x * s + ox, y * s + oy) for k, (x, y) in self.a.items()}
        return self


def concept_tag(im, x, y, u):
    d = ImageDraw.Draw(im); f = _font(15 * u, True)
    tw = d.textlength('CONCEPT', font=f); p = 7 * u
    d.rectangle([x, y, x + tw + 2 * p, y + 26 * u], fill='white', outline=EDGE, width=max(1, int(1.5 * u)))
    d.text((x + p, y + 3.5 * u), 'CONCEPT', fill=GREY, font=f)


def callouts(r, items, u, absolute=False):
    """items: (anchor key or (x, y), text, a, b) — absolute: label centre at (a·W, b·H); else offset (a·W, b·W) from the anchor."""
    d = ImageDraw.Draw(r.im); f = _font(17 * u, True); W, H = r.im.size
    for key, txt, a, b in items:
        ax, ay = r.a[key] if isinstance(key, str) else key
        lx, ly = (a * W, b * H) if absolute else (ax + a * W, ay + b * W)
        d.line([(ax, ay), (lx, ly)], fill=INK2, width=max(2, int(2 * u)))
        rr = 4.5 * u
        d.ellipse([ax - rr, ay - rr, ax + rr, ay + rr], fill=INK, outline='white', width=max(1, int(1.5 * u)))
        tw = d.textlength(txt, font=f); p = 8 * u; hh = 30 * u
        x0 = min(max(lx - tw / 2 - p, 2), W - tw - 2 * p - 2); y0 = min(max(ly - hh / 2, 2), H - hh - 2)
        d.rounded_rectangle([x0, y0, x0 + tw + 2 * p, y0 + hh], radius=4 * u, fill='white', outline=INK2, width=max(1, int(1.5 * u)))
        d.text((x0 + p, y0 + 4 * u), txt, fill=INK, font=f)


def _save_im(im, name, q=90):
    p = os.path.join(FIG, name + '.jpg')
    im.save(p, quality=q, optimize=True)
    return {'path': p, 'w': im.width, 'h': im.height}


def panel(cells, cols, cw, ch, name, gap=24, lab=None, sub=None, tag=True, u=1.6, tu=None):
    """cells: list of R (already cropped) · lab/sub: per-cell caption lines under each image · tu = CONCEPT tag scale."""
    tu = tu or min(u, 1.3)
    rows = (len(cells) + cols - 1) // cols
    lh = (21 * u + 14 if lab else 0) + (17 * u + 12 if sub else 0) + 6
    W = cols * cw + (cols - 1) * gap; H = rows * (ch + lh) + (rows - 1) * gap
    out = Image.new('RGB', (int(W), int(H)), 'white'); d = ImageDraw.Draw(out)
    for i, r in enumerate(cells):
        row, col = divmod(i, cols)
        n_row = min(cols, len(cells) - row * cols)
        cx = col * (cw + gap) + (cols - n_row) * (cw + gap) / 2; cy = row * (ch + lh + gap)
        r.fit(cw, ch); out.paste(r.im, (int(cx), int(cy)))
        d.rectangle([cx, cy, cx + cw - 1, cy + ch - 1], outline='#E1E3E6', width=2)
        if tag if isinstance(tag, bool) else tag[i]:
            concept_tag(out, cx + 10 * tu, cy + 10 * tu, tu)
        ty = cy + ch + 8
        if lab:
            f = _font(21 * u, True); t = lab[i]
            assert d.textlength(t, font=f) < cw, ('label too wide', t)
            d.text((cx + cw / 2 - d.textlength(t, font=f) / 2, ty), t, fill=INK, font=f); ty += 21 * u + 14
        if sub:
            f = _font(17 * u); t = sub[i]
            assert d.textlength(t, font=f) < cw, ('sub too wide', t)
            d.text((cx + cw / 2 - d.textlength(t, font=f) / 2, ty), t, fill=INK2, font=f)
    return _save_im(out, name)


def single(r, name, w=1900, tag=True, items=None, u=2.0, legend=None):
    r.width(w)
    if items: callouts(r, items, u)
    if tag: concept_tag(r.im, 14 * u, 14 * u, min(u, 1.6))
    if legend:
        d = ImageDraw.Draw(r.im); f = _font(16 * u); x = r.im.width - 14 * u; y = r.im.height - 14 * u
        for sw, txt in reversed(legend):
            tw = d.textlength(txt, font=f); y -= 32 * u
            d.rectangle([x - tw - 46 * u, y - 4 * u, x + 4 * u, y + 26 * u], fill='white')
            d.text((x - tw, y), txt, fill=INK, font=f)
            sx = x - tw - 38 * u
            if sw == 'robot': d.rectangle([sx, y + 4 * u, sx + 28 * u, y + 20 * u], fill='#F3B08F', outline=ACC, width=int(2 * u))
            elif sw == 'human': d.rectangle([sx, y + 4 * u, sx + 28 * u, y + 20 * u], fill='#E6E8EB', outline=INK2, width=int(1.5 * u))
            else:
                d.rectangle([sx, y + 4 * u, sx + 28 * u, y + 20 * u], fill='white', outline=INK2, width=int(1.5 * u))
                for k in range(0, 40, 8):
                    d.line([(sx + k * u, y + 20 * u), (sx + min(28, k + 16) * u, y + (20 - min(16, 28 - k)) * u)], fill=INK2, width=int(1.2 * u))
    return _save_im(r.im, name)


def make_figures():
    os.makedirs(FIG, exist_ok=True)
    G = {}
    G['cover'] = single(R('v2_cover').trim(0.01), 'f_cover', w=1900, u=2.0)
    # labels sized for A4: final width Wc px shown at ~642 px → 8 pt ≈ Wc / 60 px
    r = R('fig_flow_kitchen').trim(0.01).width(1900)
    callouts(r, [('p1', '① 식기 이동', 0.33, 0.10), ('p4', '④ 수납', 0.50, 0.06), ('p2', '② 식세기 적재', 0.68, 0.09),
                 ('p3', '③ 식세기 꺼내기', 0.86, 0.33), ('ih', '인덕션', 0.15, 0.25), ('oven', '오븐', 0.13, 0.64),
                 ('fridge', '냉장고', 0.90, 0.66), ('dw', '식기세척기', 0.70, 0.90)], 2.1, absolute=True)
    G['flow'] = _save_im(r.im, 'f_flow')
    names = [('old2a', '구축 2Bay A'), ('old2b', '구축 2Bay B'), ('new3', '신축 3Bay'), ('new4', '신축 4Bay')]
    pl = {p[0]: p for p in C.PLANS}
    subs = []
    for k, nm in names:
        row = pl[nm]
        subs.append(f"{row[3].split(' (')[0]} · {'기본 일자 배치 가능' if row[5].startswith('가능') else '기본 일자 배치 불가'}")
    G['kitchens'] = panel([R('fig_var_k_' + k).trim(0.02) for k, _ in names], 2, 900, 640, 'f_kitchens', lab=[n for _, n in names], sub=subs, tag=False, u=1.7)
    r = R('fig_tech_m03_kitchen').trim(0.01)
    G['m03'] = single(r, 'f_m03', w=1500, u=2.1, items=[
        ('garage', 'Robot Home', -0.16, -0.02), ('rail', 'Rail', 0.12, -0.1), ('drop', 'Drop Zone', -0.18, 0.06),
        ('sink', '싱크', 0.15, -0.06), ('drawer', '수납 Dock', 0.16, 0.02), ('dw', '식기세척기 Interface', 0.1, 0.08),
        ('cooktop', '인덕션 (측면 · 진입 금지)', 0.06, 0.2)])
    hero = R('hand_hero').trim(0.04)
    hero.fit(1000, 1240)
    callouts(hero, [('pad', '교체형 Food-contact Pad', 0.58, 0.05), ('suction', 'Palm Suction', 0.17, 0.30), ('cam', 'Wrist Camera', 0.15, 0.62),
                    ('ft', '힘/토크 센서', 0.80, 0.80), ('qc', 'Quick Changer', 0.21, 0.95)], 2.1, absolute=True)
    concept_tag(hero.im, 14, 14, 1.4)
    grasps = [('hand_plate', '접시', '가장자리 Pinch 파지'), ('hand_cup', '컵', '몸통 감싸쥐기'), ('hand_bowl', '그릇', '테두리 Pinch 파지'), ('hand_tool', '국자', '손잡이 파지')]
    gp = Image.open(panel([R(n).trim(0.03) for n, _, _ in grasps], 2, 560, 470, 'f_hand_grid', gap=22, lab=[a for _, a, _ in grasps],
                          sub=[b for _, _, b in grasps], u=1.75, tu=1.3)['path'])
    W = hero.im.width + 40 + gp.width; Hh = max(hero.im.height, gp.height)
    comp = Image.new('RGB', (W, Hh), 'white'); comp.paste(hero.im, (0, (Hh - hero.im.height) // 2)); comp.paste(gp, (hero.im.width + 40, (Hh - gp.height) // 2))
    G['hand'] = _save_im(comp, 'f_hand')
    r = R('v2_after').trim(0.01).width(1900)
    callouts(r, [('garage', 'D · Robot Home', 0.20, 0.10), ('rail', 'D · Rail', 0.53, 0.12), ('robotZone', 'E · 로봇 작업 영역', 0.74, 0.22),
                 ('drop', 'D · Drop Zone', 0.53, 0.47), ('nogo', 'E · 진입 금지 (쿡탑)', 0.17, 0.70), ('humanZone', 'E · 사람 작업 영역', 0.40, 0.91),
                 ('dw', 'D · 식기세척기 Interface', 0.85, 0.74)], 2.1, absolute=True)
    concept_tag(r.im, 24, 24, 2.0)
    G['after'] = _save_im(r.im, 'f_after')
    r = R('fig_tech_b5_zones').trim(0.01)
    G['zones'] = single(r, 'f_zones', u=2.0, legend=[('robot', '로봇 작업 영역 (싱크대 벽 일자 구간)'), ('human', '사람 작업 영역 (진입 시 감속 · 정지)'), ('nogo', '진입 금지 (쿡탑 구역)')])
    seq = [('v2_seq_1_detect', '① 식기 인식'), ('v2_seq_2_pick', '② 집기'), ('v2_seq_3_load', '③ 식세기 적재'), ('v2_seq_4_unload', '④ 식세기 꺼내기'), ('v2_seq_5_store', '⑤ 제자리 수납')]
    G['clean'] = panel([R(n).crop(0.04, 0.04, 0.96, 0.96) for n, _ in seq], 3, 640, 490, 'f_clean', gap=20, lab=[t for _, t in seq], u=1.65)
    ins = [('fig_flow_retrofit', 'Retrofit · 기존 주방'), ('fig_flow_remodel', 'Remodeling · 주방 공사 연계'), ('fig_flow_newbuild', 'New-build · 설계 반영')]
    isub = ['Compact Mount · Dock · Vision 기준점', 'Rail · Robot Home · 식세기 Interface', 'Tool Dock · 점검 공간 · 전원 · 통신']
    G['install'] = panel([R(n).trim(0.01) for n, _ in ins], 3, 640, 360, 'f_install', gap=18, lab=[t for _, t in ins], sub=isub, u=1.6)
    stow = [('v2_stow_1_closed', '① 문 닫힘'), ('v2_stow_2_open', '② 문 열림'), ('v2_stow_3_deploy', '③ 팔 펼침'), ('v2_stow_4_exit', '④ Rail 이동'), ('v2_stow_5_low', '⑤ 하단 랙 적재')]
    G['stow'] = panel([R(n).crop(0.04, 0.04, 0.96, 0.96) for n, _ in stow], 3, 640, 490, 'f_stow', gap=20, lab=[t for _, t in stow], u=1.65)
    G['plan'] = panel([R('plan_old2a_top_orig').trim(0.01), R('plan_old2a_top_arki').trim(0.01)],
                      2, 900, 850, 'f_plan', lab=['기존 평면 (ㄱ자 주방)', 'Interface 적용 (싱크대 벽 로봇 구간)'], tag=[False, True], u=1.7)
    G['section'] = panel([R('plan_old2a_kitchen').trim(0.01), R('v2_section_low').trim(0.02)], 2, 1000, 760, 'f_section',
                         lab=['구축 2Bay A 주방 · Interface 적용 3D', '단면: 식세기 하단 랙 적재 (하단 작업)'], u=1.7)
    return G


# ================================================================ content
def build_content(G, CH):
    BL.clear(); TOC.clear(); NT[0] = 0; NF[0] = 0
    hr, hrt, hnb = H3, HH['retrofit_purchase_Y3'], HH['newbuild_purchase_Y3']
    rent3 = HH['rental_direct_Y3']
    hw3, hw5 = 1 - v('bom')[2] / v('p_robot'), 1 - v('bom')[4] / v('p_robot')
    tips_people = sum(F['uses'][0]['tips']); people = sum(F['people'])

    # ---------------------------------------------------------------- cover · toc
    BL.append({'t': 'cover', 'kicker': 'MH Robotics · Seed · TIPS', 'title': TITLE, 'subtitle': 'Seed · TIPS 사업계획 상세 보고서',
               'image': {'path': G['cover']['path'], 'w_px': G['cover']['w'], 'h_px': G['cover']['h'],
                         'caption': '[CONCEPT] 구축 아파트 주방 한 벽 적용 예 — Robot Home · Rail · 식기세척기 Interface (설계 개념 · 실제 제품 아님)'},
               'lines': ['2026. 10', '현재 단계: Concept (시제품 개발 전 · 고객 · 계약 · 매출 없음)', '대표자: [Founder 정보 필요]']})
    BL.append({'t': 'toc'})

    # ---------------------------------------------------------------- 요약
    h1('요약')
    box('사업 정의', [
        '□ Adaptive Robot Hand · Manipulation Skill · Calibration · Environment Interface 결합 → 다양한 실제 주방에서 식기 정리부터 조리까지 단계적으로 확장하는 **Kitchen Manipulation Robotics System** 개발',
        '○ 첫 검증 Workflow = CLEAN (식기 정리) → 같은 Platform에 ASSIST · COOK 단계적 추가',
        '○ 기존 주방 · Remodeling · 신축에 설치 유형별 시공 범위만 달리해 적용',
        '○ Robot · 설치 매출 이후 Rental · Care · 소모품 · Skill · Tool로 Installed Base 기반 반복매출 확보',
        '○ 현재 단계 = Concept (시제품 · 고객 · 계약 · 매출 없음) → Seed · TIPS 24개월로 기술 · 사업 Evidence 확보'])
    tiles([(eok(F['spend_total']), '24개월 지출 (Bottom-up)', False),
           (f"{F['seed_range'][0]}~{F['seed_range'][1]}억원", 'Seed 요청 범위 (Lean ~ Base)', True),
           ('8억원', 'TIPS R&D 정부지원 (선정 시)', False),
           (f"{MK['sam']:,.0f}억원", '연 SAM (Bottom-up, 3개 채널)', False)])
    table('사업 요약', ['항목', '핵심 내용', '근거 · 구분'], [
        ['문제', '가전 = 내부 기능만 자동화 · 가전 사이 식기 이동 · 식세기 적재/꺼내기 · 수납 · 재료 투입 · 도구 조작 = 사람 작업', '가정관리 무급노동 459.5조원 (2024) [[FACT]] · 식사 후 정리 40분/일 [[ASSUMPTION]]'],
        ['왜 주방', '동작 종류 적고 반복 · 작업영역 고정 · 물체 종류 한정 (기술) · 매일 사용 · Remodeling · 입주 = 구매 계기 (사업)', 'WTP n ≥ 300 · 예약금 테스트로 검증 (M18)'],
        ['구조적 한계', '주방마다 형태 · 가전 · 수납 · 치수 · 시공 오차 상이 → 범용 로봇 = 집마다 인식 · 티칭 · Calibration 반복', '확보 평면 5종 중 3종 기본 배치 불가 [[DERIVED]]'],
        ['접근', 'Object → Adaptive Hand · Task → Skill Library · Kitchen → Perception + Calibration · 반복 작업 위치 → 최소 Interface (주방 전체 표준화 없음)', '[[CONCEPT]]'],
        ['제품', '5개 Layer 통합 (Robot Module · Manipulation · Calibration · Environment Interface · Safety) · CLEAN → ASSIST → COOK', '[[CONCEPT]] · COOK [[FUTURE]]'],
        ['설치 유형', f"Retrofit {man(hrt['y0'])} · Remodeling {man(hr['y0'])} · New-build Option {v('p_rr_new')}만원 (B2B) + 입주 시 로봇 구매", '[[ASSUMPTION]] · VAT 별도'],
        ['사업모델', f"INSTALL → OPERATE (Rental 월 {v('p_rent')}만 · Care 연 {v('p_care')}만 · 소모품 연 {CONS['list_y']:.0f}만) → EXPAND (Skill {v('p_sw')}만 · Tool {v('p_tool')}만) · 세대당 5년 공헌이익 {man(H3['contrib5'])} (Y3 원가) → {man(H5['contrib5'])} (Y5 원가)", '[[DERIVED]]'],
        ['시장', f"Bottom-up SAM 연 {MK['sam']:,.0f}억원 (Remodeling {MK['sam_remodel']:,.0f} · Retrofit {MK['sam_retro']:,.0f} · New-build {MK['sam_new']:,.0f}) · Y5 계획 매출 {B['rev'][4] / 1e4:.1f}억원 = 대상 세대의 {pct(MK['som_share_hh'], 1)}", '[[DERIVED]] · [[TARGET]]'],
        ['사업화', 'Phase 1 Premium Remodeling (검증) → Phase 2 호환 주방 Retrofit → Phase 3 신축 B2B2C (Scale) · 인테리어 시공 = Partner', 'Partner 조건 협의 (M18~M24)'],
        ['자금', f"24개월 지출 {eok(F['spend_total'])} = TIPS 정부지원 8억원 (기술 검증, 선정 시) + Seed {F['seed_range'][0]}~{F['seed_range'][1]}억원 (사업 검증 · 과제 외 개발)", '[[DERIVED]] · TIPS 규정 [[FACT]]'],
        ['24개월 Evidence', '실거주 3세대 CLEAN ≥ 90% · 주방 3종 적용 하락 ≤ 10%p · Calibration ≤ 4시간 · 원가 실측 · WTP n ≥ 300 · 유료 전환 ≥ 2세대 · 출원 5건', '[[TARGET]]'],
    ], [14, 62, 24], size=16, fill_first=True, bold_first=True)
    table('핵심 숫자', ['항목', '값', '산식 · 구분'], [
        ['국내 아파트 (잠재 대상, 실구매 시장 아님)', f"약 {MK['apt'] / 10:,.0f}만호", '총주택 2,018.1만 × 65.8% [[DERIVED]]'],
        ['연간 주방 교체 (아파트)', '30만 세대', f"교차검증 {MK['tri1'] / 10:.1f}만 · {MK['tri2'] / 10:.1f}만 [[ASSUMPTION]]"],
        ['Remodeling 첫 시장 (Beachhead)', f"{MK['fit'] * 1000:,.0f}세대/년 · {MK['sam_remodel']:,.0f}억원", '30만 × Premium 10% × 적용 60% [[DERIVED]]'],
        ['Robot System ASP', man(v('p_robot')), 'WTP 검증 1순위 [[ASSUMPTION]]'],
        ['Robot BOM (Y1 시제품 → Y3 → Y5)', f"{v('bom')[0]:,} → {v('bom')[2]:,} → {v('bom')[4]:,}만원", '공개가 Benchmark 기반 [[ASSUMPTION]]'],
        ['Remodeling 세대당 설치 시점 매출', man(hr['y0']), f"Interface {v('p_rr')} + Robot {v('p_robot'):,} + 설치 {v('p_comm')} [[DERIVED]]"],
        ['세대당 5년 누적 공헌이익', f"{man(H3['contrib5'])} (Y3) · {man(H5['contrib5'])} (Y5)", '[[DERIVED]]'],
        ['Y5 매출 · 설치 (Base Plan)', f"{B['rev'][4] / 1e4:.1f}억원 · {B['kitchens'][4]:,.0f}세대", '[[TARGET]]'],
        ['24개월 지출', eok(F['spend_total']), 'Bottom-up [[DERIVED]]'],
        ['Seed 범위', f"{F['seed_range'][0]}~{F['seed_range'][1]}억원 (Lean {eok(F['seed_lean'])} · Base {eok(F['seed_base'])})", '[[DERIVED]]'],
        ['TIPS 정부지원 (일반트랙 상한)', '8억원 · 24개월 · 정부 75% 이내', '상한 [[FACT]] · 수령 = 선정 시'],
    ], [38, 30, 32], align=['l', 'r', 'l'], size=16)

    # ---------------------------------------------------------------- Ⅰ
    h1('Ⅰ. 사업 개요')
    h2('1. 사업 정의')
    gj('□ 제품: 주거용 **Kitchen Manipulation Robotics System**',
       '○ 5개 Layer 통합: A Robot Module · B Manipulation Layer · C Calibration Layer · D Environment Interface · E Human-Robot Safety',
       '○ Robot Arm = 상용 구매 · MH = Hand · Skill · Calibration · Interface · Safety · Care로 주방 System 구성',
       '□ 기능 확장 경로: CLEAN → ASSIST → COOK',
       '○ CLEAN (초기 · 기술 검증): 식기 인식 · 집기 · 식세기 적재 · 꺼내기 · 제자리 수납',
       '○ ASSIST (중기 · 기능 확장): 재료 이동 · 재료 투입 · 젓기 · 뚜껑 조작 · 도구 조작',
       '○ COOK (장기 · R&D 방향): Recipe Workflow · 복수 Skill 연결 · 가전 연동 [[FUTURE]]',
       '□ 적용 경로: 기존 주방 (Retrofit) · 주방 Remodeling · 신축 (New-build)',
       '○ 제품 1개 · 설치 유형 3개 → 설치 유형별 시공 범위만 다름',
       '○ 첫 검증 채널 = Premium 주방 Remodeling (주방 교체 시 Interface 동시 시공)',
       '□ 수익 구조: 설치 매출 (INSTALL) → 사용 기간 반복매출 (OPERATE) → 기능 확장매출 (EXPAND)',
       f"○ INSTALL: Robot System {v('p_robot'):,}만원 · Interface {v('p_rt_if')}~{v('p_rr')}만원 · 설치 · Calibration {v('p_comm')}~{v('p_comm_rt')}만원",
       f"○ OPERATE: Rental 월 {v('p_rent')}만원 · Care 연 {v('p_care')}만원 · 소모품 연 {CONS['list_y']:.0f}만원 (정가)",
       f"○ EXPAND: ASSIST Skill Pack {v('p_sw')}만원 · Tool {v('p_tool')}만원 · COOK Skill · Upgrade [[FUTURE]]")
    h2('2. 현재 단계 및 작성 기준')
    gj('□ 현재 단계: **Concept** (시제품 개발 전)',
       '○ 시제품 · 고객 · 계약 · LOI · 매출 없음',
       '○ Founder · 핵심 팀: [Founder 정보 필요] (Ⅹ장)',
       '○ 특허 출원 0건 · 출원 후보 12개 묶음 도출 · 등록 가능성 미정 (Ⅷ장)',
       '□ 수치 기준',
       '○ 금액 = 만원 또는 억원 · VAT 별도 · 주방 공사비 별도',
       '○ 연차 = 사업 연차 (Y1 = Seed · TIPS 1차년도) · 월 = 과제 시작 기준 (M1~M24)',
       '○ 수치 구분 = FACT · DERIVED · ASSUMPTION · TARGET · CONCEPT · FUTURE (부록 B)',
       '○ 재무 수치 = 재무모델 (MH_Robotics_Financial_Model.xlsx)과 동일 값',
       '□ 그림 기준',
       '○ 제품 3D 그림 = 전부 설계 개념 [[CONCEPT]] · 실제 제품 · 시공 사례 아님',
       '○ 평면 = 확보 평면 유형별 재작도 · 특정 단지 표기 없음',
       '○ 주황 = 로봇 작업 영역 · 로봇 경로 · 핵심 숫자에만 사용')
    h2('3. 투자 요청 개요')
    table('투자 요청 개요', ['구분', '금액', '용도', '구분'], [
        ['24개월 지출', eok(F['spend_total']), '인건비 중심 Bottom-up (팀 14명 · 목업 · 시제품 · 실증 · 인증 · IP)', '[[DERIVED]]'],
        ['TIPS R&D 정부지원 (선정 시)', '8억원', '기술 검증 (WP1~WP6) · 과제 총액 ' + eok(TP['total'], 2), '상한 [[FACT]]'],
        ['Seed 요청', f"{F['seed_range'][0]}~{F['seed_range'][1]}억원", f"사업 검증 · 과제 외 개발 · 기관부담금 · Buffer 3개월 (Lean {eok(F['seed_lean'])} · Base {eok(F['seed_base'])})", '[[DERIVED]]'],
        ['TIPS 미선정 시', eok(F['seed_no_tips']), 'Lean 범위 · 일정 연장 또는 비R&D 과제로 보완', '[[DERIVED]]'],
    ], [22, 15, 51, 12], align=['l', 'r', 'l', 'l'], size=16)
    gj('□ 24개월 목표 Evidence [[TARGET]]',
       '○ 기술: 실거주 3세대 CLEAN 성공률 ≥ 90% · 주방 3종 적용 하락 ≤ 10%p · 현장 Calibration ≤ 4시간',
       '○ 경제성: Robot BOM (100대/년 견적) · 설치 · Service 원가 실측',
       '○ 시장: WTP n ≥ 300 · 예약금 테스트 · 유료 전환 ≥ 2세대 · Partner 조건 (리모델링 1 · 렌탈/캐피탈 1)',
       '○ IP: 국내 출원 5건 + PCT 1건 (등록 가능성 미정)')

    # ---------------------------------------------------------------- Ⅱ
    h1('Ⅱ. 문제 정의 및 기회')
    h2('1. 가전 자동화 이후에도 남은 주방 Physical Workflow')
    fig(G['flow'], '현재 주방 작업 흐름 — 가전 내부 자동화 vs 가전 사이 사람 작업 ①~④ (로봇 없음 · 개념도)')
    gj('□ 가전 = 내부 기능만 자동화',
       '○ 식기세척기 = 세척 · 인덕션 = 가열 · 냉장고 = 보관 · 오븐 = 조리',
       '○ 가전 사이 식기 · 재료 · 도구 이동 = 여전히 사람 작업',
       '□ 사람 작업으로 남은 Physical Task 10개',
       '○ CLEAN 범위 (①~④): 식기 이동 · 식세기 적재 · 식세기 꺼내기 · 수납',
       '○ ASSIST · COOK 범위: 식재료 이동 · 재료 투입 · 조리도구 조작 · 젓기 · 뚜껑 조작 · 조리 후 정리',
       '□ 문제 정의: 개별 가전 기능이 아닌 주방 Workflow 전체의 Physical Manipulation 미자동화',
       '○ Appliance Automation ≠ Physical Workflow Automation',
       '□ 규모 근거',
       '○ 2024 무급 가사노동 가치 582.4조원 · 그중 가정관리 459.5조원 (78.9%) · 1인당 132분/일 [[FACT]]',
       '- 국가데이터처 가계생산 위성계정 (2026.4) [S40]',
       f"○ 식사 후 정리 시간 하루 약 {v('a_cleanup_min')}분 [[ASSUMPTION]] → 시간일지 조사 30세대로 검증 (M3)",
       f"○ CLEAN 가사노동 대체 가치 = {v('a_cleanup_min')}분/일 × 30일 × 자동화 {pct(v('a_auto_share'))} × 가사서비스 {v('f_helper_rate')}만원/h ≈ 월 약 {VA['value']:.0f}만원 (범위 {VA['lo']:.0f}~{VA['hi']:.0f}만원) [[DERIVED]]",
       f"- 가사서비스 시간당 요금 {v('f_helper_rate')}만원 = 플랫폼 4시간 59,900~64,900원 [[FACT]]")
    h2('2. 왜 주방인가')
    fig(G['m03'], '확보 평면 (구축 2Bay A) 주방 Interface 적용 예 — 주황 = 로봇 작업 영역 (싱크대 벽 일자 구간) [CONCEPT]', w_pct=78)
    table('주방 선택 기준', ['구분', '기준', '내용'], [
        ['Robot Engineering', '집기 · 이동 · 놓기 · 넣기 · 꺼내기 중심', '동작 종류 적고 반복 → Skill Library화 용이'],
        ['', '작업영역 고정', '싱크 · 조리대 · 식세기 · 수납장 → Calibration 대상 명확'],
        ['', '물체는 다양 · 종류는 한정', '접시 · 컵 · 그릇 · 수저 · 뚜껑 · 집게 · 국자 → 이후 식재료'],
        ['', '가전 사이 이동 반복', '식세기 · 수납장 · 조리대 사이 물리적 이동'],
        ['Business', '높은 일일 사용빈도', '매일 식사 후 반복 → 사용 Data · 빠른 가치 체감'],
        ['', '구매 계기 존재', '주방 Remodeling · 신축 입주 시 공사 · 설치 동시 결정'],
        ['', 'CLEAN → ASSIST → COOK', '같은 Platform + Skill · Tool 추가로 기능 확장'],
        ['', '설치 이후 반복매출', 'Installed Base 기반 Care · 소모품 · Skill'],
    ], [20, 32, 48], size=16, bold_first=True)
    gj('□ Why now',
       '○ 6축 Arm 가격 하락: FAIRINO FR5 $6,999 · UFACTORY xArm 6 $8,399 (UR3e $23k~33k 대비) [[FACT]] [S15]',
       '○ 공개 범용 모델 (π0.5) 공개 → Manipulation 학습 기반 활용 가능 [[FACT]] [S46]',
       '○ 안전기준 정비: ISO 10218-1/-2:2025 발행 · 가정용 IEC 63682 2026 CDV 단계 [[FACT]] [S39 · S47]',
       '□ 검증 과제: 지불의사 미검증 → WTP 조사 n ≥ 300 · 예약금 테스트 (M18)')
    h2('3. 구조적 한계: 주방마다 다른 환경')
    gj('□ 가정용 로봇의 한계 = 로봇 지능 부족만이 아닌 주방 간 환경 차이 (Environment Variation)',
       '○ 주방마다 다른 9개 변수: 주방 형태 (일자 · ㄱ자 · ㄷ자 · 아일랜드) · 가전 위치 · 가전 모델 · 수납 위치 · 조리대 치수 · 물건 위치 · 동선 · 조명 · 시공 오차',
       '□ 범용 로봇 적용 시 집마다 반복되는 6단계',
       '○ 인식 (Perception) → Mapping → 티칭 (Teaching) → Programming → Calibration → 검증 (Validation)',
       '○ 반복 공정 = 설치시간 · 비용 · 신뢰성 좌우 → 반복 설치형 사업 구조의 핵심 장애')
    fig(G['kitchens'], '확보 평면 4종 주방 재작도 (로봇 없음 · 동일 축척)')
    table('확보 평면 5종 분석', ['평면', '유형', '외곽 치수 (mm)', '주방 형태', '3D 모델링', '기본 배치 (Remodeling 일자)'],
          [list(p) for p in C.PLANS], [12, 17, 14, 23, 13, 21], size=15, bold_first=True,
          note='주: 확보 평면 = 유형별 재작도 · 특정 단지 표기 없음 · 기본 배치 = 싱크대 벽 일자 구간 3.15m 이상 (Robot Home · Drop Zone · 싱크 · 서랍 · 식세기) [[DERIVED]]')
    gj('□ 분석 결과 [[DERIVED]]',
       '○ 5종 모두 싱크 · 쿡탑이 다른 벽 → 로봇 작업 구역 분리 가능',
       '○ 싱크대 벽 길이 약 2.6~3.3m · 기본 일자 배치 가능 1종 · 불가 3종 · 미검토 1종',
       '○ 불가 3종 = 싱크대 벽 2.6~2.8m → Compact Mount 또는 냉장고 위치 변경 검토',
       '□ 시사점',
       '○ 같은 로봇의 반복 설치 조건 = 로봇의 주방 적응 (Calibration) + 반복 작업 위치 최소 Interface',
       f"○ Remodeling 적용 가능률 {pct(v('a_fit_rate'))} [[ASSUMPTION]] = 확보 평면 결과 (5종 중 1종)보다 높은 가정 → 평면 30개 분석 (M6)으로 검증")

    # ---------------------------------------------------------------- Ⅲ
    h1('Ⅲ. 기술 개발 전략')
    h2('1. 접근: 로봇의 주방 적응 + 최소 Interface')
    gj('□ 주방 전체를 로봇에 맞게 바꾸는 방식이 아님',
       '○ 변동 요인별 MH 기술 대응 → 같은 Robot · Skill의 여러 주방 반복 적용',
       '○ 표준화 범위 = 매일 반복되는 작업 위치만 (Robot 대기 자리 · 도구 거치대 · 식세기 랙) → 신뢰성 · 설치 시간 확보')
    table('변동 요인별 MH 기술 대응', ['변동 요인', 'MH 기술', '내용', '검증 지표 (M24)'], [
        ['물체 다양성 (Object)', 'Adaptive Robot Hand', '접시 · 컵 · 그릇 · 수저 · 뚜껑 · 도구를 Tool 교체 없이 하나의 Hand로', 'Object Coverage ≥ 27/30'],
        ['작업 다양성 (Task)', 'Manipulation Skill Library', 'Pick · Place · Insert · Remove · Open/Close · 실패 복구 Template', 'Task Success ≥ 90% (실거주)'],
        ['주방 차이 (Kitchen)', 'Perception + Calibration', '주방 Mapping · 좌표계 Calibration · 가전 · 수납 위치 등록', 'Calibration ≤ 4시간 · 하락 ≤ 10%p'],
        ['반복 작업 위치', 'Minimal Environment Interface', 'Robot Home · Tool Dock · 수납 Dock · 식세기 Interface · Vision 기준점', '설치 2인 1일 (Remodeling)'],
    ], [17, 22, 39, 22], size=15, bold_first=True)
    h2('2. 핵심 Hardware: Adaptive Robot Hand')
    fig(G['hand'], 'Adaptive Robot Hand 구성과 식기 · 도구 파지 예 [CONCEPT]')
    gj('□ 식기 · 도구 파지의 어려움',
       '○ 얇은 접시 가장자리 · 젖은 유리 · 미끄러운 도자기 · 크기 편차 · 겹친 식기 · 식세기 랙 사이 좁은 공간',
       '○ 공개 연구: 식세기 적재 성공률 58.7% (실험실) · 단순 가사 81% · 정리 85% 수준 [S36~S38]',
       '□ 설계 목표 = 손가락 수 · 자유도 경쟁이 아닌 작업 완료율 · 가격 · 위생 · 유지관리 · 내구성',
       '○ 2+1 손가락 부족구동 + 교체형 Food-contact Pad · Edge Lip · 미끄럼 감지 · Palm Suction · Quick Changer · Wrist Camera · 힘/토크 센서',
       '○ 파지 방식: 접시 = 가장자리 Pinch 파지 · 컵 = 몸통 감싸쥐기 · 그릇 = 테두리 Pinch 파지 · 국자 = 손잡이 파지',
       '○ 식품 접촉 Pad · Tip = 교체형 Module → 위생 관리 + 소모품 (Grip Kit) 매출 연결',
       '□ Buy vs Build Gate (M6)',
       '○ 상용 Gripper (Robotiq 2F-85 등) 비교 기준으로 30종 식기 비교',
       '○ Coverage +15%p 이상 또는 Tool 교체 횟수 50% 감소 시에만 자체 Hand 채택',
       '○ 미달 시 상용 Gripper + 교체형 Pad (Buy) · WP1 예산 재배분')
    table('Hand 시험 계획 (M1~M24)', ['항목', '내용', '구분'], [list(r) for r in C.HAND_TEST], [17, 68, 15], size=15, bold_first=True)
    table('핵심 부품 공개가 Benchmark', ['부품', '공개가 (USD)', f"환산 (만원, {C.FX:,}원/USD)"], [list(r) for r in C.BENCH], [44, 28, 28],
          align=['l', 'r', 'r'], size=15, note='주: 공개가 [[FACT]] (2026, 판매처 · 보도 기준) · 환산 = [[ASSUMPTION]] · 출처 [S15 · S16 · S42]')
    h2('3. 핵심 기술: Manipulation Skill과 Calibration')
    gj('□ Skill = Software 구독이 아닌 로봇이 수행 가능한 작업을 늘리는 Layer',
       '□ Skill 실행 5단계: 인식 → 파지 → 조작 → 확인 → 복구',
       '○ 인식 = 물체 · 위치 인식 · 파지 = 파지점 · 파지력 결정 · 조작 = 이동 · 삽입',
       '○ 확인 = 완료 확인 · 복구 = 실패 감지 시 다시 잡기 · 내려놓기',
       '○ 모든 Skill이 같은 구조 → Template화 · 주방마다 재사용',
       '□ Calibration = Skill의 타 주방 적용 핵심',
       '○ 주방 Mapping · 기준점 좌표계 Calibration (Robot Home · 가전 기준점) · 가전 · 수납 위치 등록 · 작업 Parameter 조정',
       '○ 현장 Custom 코드 0 · 티칭 ≤ 1시간 · 현장 Calibration ≤ 4시간 (M18 목표)',
       '□ 타 주방 적용 시험 (M18)',
       '○ 주방 A 일자 3.2m · 빌트인 식세기 / 주방 B ㄱ자 · 짧은 싱크대 벽 / 주방 C Retrofit · 프리스탠딩 식세기',
       '○ 같은 Skill 설치 후 성공률 하락 ≤ 10%p → Platform 반복 적용 증거',
       '□ 공개 범용 모델 (π0 계열) Fine-tune 검토 → MH Manipulation Layer로 활용')
    h2('4. 제품 Architecture: 5개 Layer 통합')
    fig(G['after'], 'MH Kitchen Robotics System 5개 Layer 배치 예 — 주황 = 로봇 작업 영역 · 회색 점선 = 사람 작업 영역 [CONCEPT]')
    table('제품 Layer 구성', ['Layer', '구성', '개발 방식'], [
        ['A · Robot Module', 'Robot Arm · Adaptive Hand · Vision · 힘 · 안전 센서 · 필요 시 Rail · Dock', 'Arm 상용 구매 · Hand M6 Build/Buy 판정'],
        ['B · Manipulation Layer', '물체 인식 · 파지 계획 · 경로 계획 · 작업 실행 · 실패 감지 · 복구', '자체 개발 (공개 범용 모델 활용 검토)'],
        ['C · Calibration Layer', '주방 Mapping · 좌표계 Calibration · 가전 · 수납 위치 등록 · 작업 Parameter', '자체 개발'],
        ['D · Environment Interface', 'Robot Home · Tool Dock · 수납 Dock · 가전 Interface · Vision 기준점 · 필요 시 작업면 Guide', '자체 표준 · 가구 Partner 생산'],
        ['E · Human-Robot Safety', '사람 감지 · 감속 · 충돌 감지 · 비상정지 · Robot Home 자동 복귀', '자체 설계 · 인증기관 상담'],
    ], [24, 50, 26], size=15, bold_first=True)
    gj('□ 왜 Robot Arm인가',
       '○ 식세기 랙 · 서랍 · 상부장 작업 = 6축 위치 · 자세 제어 필요',
       '○ 전용 기계 = 식기 · 주방마다 재설계 · 이동형 = 하단 작업 · 가격 · 안전 부담',
       '○ Arm + Skill · Tool 추가 → ASSIST · COOK 확장',
       '□ Robot OEM과의 차이: Arm = 상용 구매 · MH = Hand · Skill · Calibration · Interface · Safety · Care로 주방 System 구성')
    bb = M['bom_breakdown']
    table('Robot System BOM 구성 (만원/대)', ['구성', 'Y1 시제품', 'Y3', 'Y5', '근거'],
          [[r[0], nf(r[1]), nf(r[2]), nf(r[3]), r[4] or '-'] for r in bb] +
          [['합계', nf(sum(r[1] for r in bb)), nf(sum(r[2] for r in bb)), nf(sum(r[3] for r in bb)), f"Robot ASP {v('p_robot'):,}만원 대비 HW 마진 Y3 {pct(hw3)} · Y5 {pct(hw5)}"]],
          [33, 10, 8, 8, 41], align=['l', 'r', 'r', 'r', 'l'], size=14, bold_rows=[len(bb)],
          note='주: [[ASSUMPTION]] · 공개가 Benchmark 기반 추정 → 100대/년 견적으로 확정 (M18)')
    assert sum(r[1] for r in bb) == v('bom')[0] and sum(r[2] for r in bb) == v('bom')[2] and sum(r[3] for r in bb) == v('bom')[4]
    fig(CH['bom'], 'Robot BOM 하락 경로와 Hardware 마진 (Robot ASP 대비)', w_pct=92, note='Y1 = 시제품 · HW 마진 = 1 − BOM ÷ ASP [[ASSUMPTION]]')
    h2('5. 안전 · 인증')
    fig(G['zones'], '주방 Zoning — 로봇 작업 영역 · 사람 작업 영역 · 진입 금지 구역 [CONCEPT]', w_pct=86)
    table('안전 · 인증 경로', ['항목', '내용', '구분', '출처'], [list(r) for r in C.SAFETY], [16, 62, 10, 12], size=15, bold_first=True)
    gj('□ MH 안전 원칙 [[CONCEPT]]',
       '○ 사람 위로 운반 금지 · Zone 진입 시 감속 · 정지 · 저가반하중 Arm',
       '○ 쿡탑 구역 진입 금지 · 고장 시 Robot Home 자동 복귀 · 로봇 없이 일반 주방 사용 가능',
       '□ 인증 경로 미확정 → M9 인증기관 사전상담 · M18 전기 · EMC 사전시험 · Series A 이후 본인증')
    h2('6. 기술 KPI')
    table('기술 KPI 정의 · Benchmark', ['구분', '지표', '정의', 'Benchmark'],
          [[k[0], k[1], k[2], k[3]] for k in C.KPI], [12, 20, 36, 32], size=13)
    table('기술 KPI 단계별 목표', ['지표', 'M6', 'M12', 'M18', 'M24', '구분'],
          [[k[1], k[4], k[5], k[6], k[7], k[9]] for k in C.KPI], [26, 15, 16, 16, 16, 11], size=13,
          note='주: [[TARGET]] = 목표 · [[DERIVED]] = 원가 가정에서 역산 · [[ASSUMPTION]] = 가정 검증 항목 · 근거 = 재무모델 KPI Link')

    # ---------------------------------------------------------------- Ⅳ
    h1('Ⅳ. 제품 및 설치 유형')
    h2('1. CLEAN Workflow (첫 검증)')
    fig(G['clean'], 'CLEAN 5단계 — 식기 인식 → 집기 → 식세기 적재 → 꺼내기 → 제자리 수납 [CONCEPT]')
    gj('□ CLEAN 범위: 조리대 한쪽 식기 인식 → 집기 → 식세기 적재 → 세척 후 꺼내기 → 수납장 정리',
       '□ CLEAN 목적 = 식기 정리 시장이 아닌 Platform 전체의 첫 End-to-End 검증',
       '○ 검증 기술 9개: 적응 파지 · 물체 인식 · 경로 계획 · 가전 조작 · 수납장 조작 · Calibration · 안전 · 실패 복구 · 연속 운전',
       '○ 단계별 새 로봇 개발이 아닌 같은 Platform에 Skill · Tool 추가')
    table('단계별 기능 확장', ['단계', '시기', '작업', '추가 항목'], [
        ['CLEAN', '초기 · 기술 검증', '식기 이동 · 식세기 적재 · 꺼내기 · 제자리 수납', '기본 Skill 4종 · 식세기 Interface · 수납 Dock'],
        ['ASSIST', '중기 · 기능 확장', '재료 이동 · 재료 투입 · 젓기 · 뚜껑 조작 · 도구 조작', 'ASSIST Skill Pack · 집게 · 국자 · 뚜껑 Tool'],
        ['COOK', '장기 · R&D 방향 [[FUTURE]]', 'Recipe Workflow · 복수 Skill 연결 · 가전 연동 · 조리 · 조리 후 정리', 'Recipe Skill · 식재료 Tool · 열 · 액체 안전'],
    ], [11, 19, 38, 32], size=15, bold_first=True)
    box('가치 Gap', [
        f"□ CLEAN 단독 가사노동 대체 가치 월 약 {VA['value']:.0f}만원 (범위 {VA['lo']:.0f}~{VA['hi']:.0f}) < Rental 월 {v('p_rent')}만원 [[DERIVED]]",
        '○ CLEAN 단독 가치만으로 가격 정당화 어려울 수 있음 = 핵심 미검증 가설',
        '○ 대응: Premium Remodeling 고객부터 · ASSIST 확장 · 위생 · 편의 가치 묶음으로 WTP 검증 (n ≥ 300 · 예약금, M18)'])
    h2('2. 설치 유형 3종')
    fig(G['install'], '단일 제품 · 3가지 설치 유형 (같은 주방 · 같은 시점) [CONCEPT]')
    table('설치 유형별 비교', ['구분', 'Retrofit (기존 주방)', 'Remodeling (주방 공사 연계)', 'New-build (설계 반영)'], [
        ['고객 상황', '주방 유지 · 호환 주방', '주방 교체 시점 (Premium)', '분양 · 입주 전 (건설사 · 가구사)'],
        ['공사 범위', '최소 시공 (Mount · Dock)', '주방 공사와 동시 (Partner 시공)', '설계 단계에서 반영'],
        ['Interface', 'Compact Mount · Dock · Vision 기준점 · Drop Zone', 'Rail · Robot Home · 식세기 Interface · 수납 Dock', 'Mount · 전원 · 통신 · Tool Dock · 가전 Interface · 점검 공간'],
        ['설치 · Calibration', f"현장 Calibration 중심 · Y3 원가 {v('comm_cost_rt')[2]}만원 (약 {KL['inst_h_rt'][2]:.0f}인시)", f"Y3 원가 {v('comm_cost')[2]}만원 (약 {KL['inst_h'][2]:.0f}인시 = 2인 약 1일)", '입주 시 설치 또는 Robot 후설치 (Option 세대)'],
        ['MH 매출 (가설)', f"Kit {v('p_rt_if')} + Robot {v('p_robot'):,} + 설치 {v('p_comm_rt')} = {hrt['y0']:,.0f}만원", f"Interface {v('p_rr')} + Robot {v('p_robot'):,} + 설치 {v('p_comm')} = {hr['y0']:,.0f}만원", f"Option {v('p_rr_new')}만원 (B2B) + 입주 시 로봇 구매 {pct(v('new_attach'))} × (Robot + 설치)"],
        ['역할', 'Phase 2 · 고객 확대', 'Phase 1 · 검증 채널', 'Phase 3 · Scale 채널'],
    ], [16, 28, 28, 28], size=15, fill_first=True, bold_first=True, bold_rows=[5],
          note='주: 가격 · 원가 = [[ASSUMPTION]] · VAT · 주방 공사비 별도 · 인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 약 ' + f"{KL['hour']:.1f}만원")
    gj('□ MH Core vs Partner',
       '○ MH Core = Robot · Hand · Skill · Calibration · Interface 표준 · Safety · 시운전 · QA',
       '○ Partner = 철거 · 가구 · 전기 · 설비 · 마감 · (신축) 건설사 · 주방가구사 · (Rental) 렌탈 · 캐피탈사',
       '○ 현재 Partner 계약 · LOI 없음 → 조건 협의 (M18~M24)')
    h2('3. Remodeling Interface 상세 (대표 평면 적용 예)')
    fig(G['stow'], 'Robot Home 보관 · 펼침 · Rail 이동 · 하단 작업 순서 [CONCEPT]')
    table('Robot Home · Rail · 하단 작업 설계 개념', ['항목', '내용', '구분'], [
        ['Robot Home (Dock)', '상판 위 끝단 W450 × D620 × H1,370mm · 여닫이 문 1짝 · 평소 로봇 수납 (보이지 않음)', '[[CONCEPT]]'],
        ['Rail', '상부장 하단 (바닥에서 약 1,390mm) · 바닥 레일 없음 · Retrofit은 Compact Mount로 대체', '[[CONCEPT]]'],
        ['하단 작업', '식세기 하단 랙 440mm 당김 → 위에서 적재 (Gripper 최저 도달 높이 약 370mm) · 서랍도 열어서 위에서 넣음', '[[CONCEPT]]'],
        ['검증 방법', '캡슐 (로봇) · 상자 (가구) 간섭 검토: 작업 자세 · 보관 · 펼침 · Rail 이동 경로 간섭 없음 (3D 모델 기준)', '[[DERIVED]]'],
    ], [18, 70, 12], size=15, bold_first=True)
    fig(G['plan'], '구축 2Bay A 평면 (12,390 × 11,670mm, 코어 포함) — 기존 주방 vs Interface 적용 [CONCEPT]')
    vv = json.load(open(os.path.join(RD, 'plan_old2a_verify.json'), encoding='utf-8'))['ik']['verify']
    gap_cm = [vv['park'], vv['path'], vv['transit']]
    chk = (f"보관 · 펼침 경로 · Rail 이동 간섭 없음 (가구 {vv['obstacles']}개)" if max(gap_cm) < 0.5
           else f"보관 {vv['park'] * 10:.0f}mm · 경로 {vv['path'] * 10:.0f}mm · 이동 {vv['transit'] * 10:.0f}mm 간섭 (가구 {vv['obstacles']}개)")
    table('대표 평면 변경 사항', ['항목', '내용'], [
        ['싱크대 벽 길이', '3,255mm'],
        ['로봇 작업 구간', '3,150mm (Robot Home 450 · Drop Zone 700 · 싱크 800 · 서랍 600 · 식세기 600)'],
        ['싱크볼 중심 이동', '약 210mm'], ['인덕션', '측면 조리대 끝으로 이동 (로봇 진입 금지)'],
        ['Robot Home 문 열림각', f"최대 {vv['doorDeg']}° (측면 벽 간섭)"], ['간섭 검토', chk],
    ], [24, 76], size=15, bold_first=True, note='주: 3D 모델 기준 검토 [[DERIVED]] · 실제 기구 · 시공 검증 예정')
    fig(G['section'], '대표 평면 주방 3D와 하단 작업 단면 [CONCEPT]')

    # ---------------------------------------------------------------- Ⅴ
    h1('Ⅴ. 사업모델 및 경제성')
    h2('1. 3단계 사업모델')
    gj('□ INSTALL → OPERATE → EXPAND · Hardware 외 매출 = 실제 유지관리 · 기능 가치 기반 (억지 Lock-in 없음)',
       f"□ Installed Base 증가 → 반복 · 확장 매출 비중 확대 구조 (Y5 매출 중 OPERATE + EXPAND {pct(B['oe_share'][4])} = 설치 초기 구조) [[DERIVED]]")
    table('3단계 사업모델 · 가격 가설 (VAT 별도)', ['단계', '항목', '가격 가설', '근거 · 비고'], [
        ['INSTALL', 'Robot System (Arm · Adaptive Hand · Vision · Safety)', man(v('p_robot')), f"BOM Y3 {v('bom')[2]:,} → Y5 {v('bom')[4]:,}만원 · HW 마진 {pct(hw3)} → {pct(hw5)}"],
        ['', 'Interface · Integration', f"Retrofit {v('p_rt_if')} · Remodeling {v('p_rr')} · New-build Option {v('p_rr_new')}만원", 'Robot Home · Rail · 식세기 Interface · Dock · Vision 기준점'],
        ['', 'Installation · Calibration · Safety Check', f"{v('p_comm')}만원 (Retrofit {v('p_comm_rt')})", f"원가 Y3 {v('comm_cost')[2]}만원 (약 {KL['inst_h'][2]:.0f}인시)"],
        ['OPERATE', 'Robot Rental (60개월, Care Basic · Grip Kit 포함)', f"월 {v('p_rent')}만원", f"월 원가 Y3 {RENT['Y3']['cost_m']:.1f} → Y5 {RENT['Y5']['cost_m']:.1f}만원"],
        ['', 'Care (Robot Lifecycle Maintenance)', f"연 {v('p_care')}만원", f"원가 Y3 {CARE['Y3']['cost']:.1f} → Y5 {CARE['Y5']['cost']:.1f}만원 · 가입률 {pct(v('care_attach'))}"],
        ['', 'Consumables (Grip · Cleaning · Protection Kit)', f"연 {CONS['list_y']:.0f}만원 (정가)", f"구매율 {pct(v('cons_attach'))} · 원가율 {pct(v('cons_cogs'))}"],
        ['EXPAND', 'ASSIST Skill Pack (설치 다음 해)', man(v('p_sw')), f"구매율 {pct(v('sw_attach'))} (ASSIST 출시 전제 [[FUTURE]])"],
        ['', 'Tool · End-effector (설치 2년 후)', man(v('p_tool')), f"구매율 {pct(v('tool_attach'))}"],
        ['', 'COOK Skill · Robot Upgrade', '[[FUTURE]]', '5년 Base 매출 미반영'],
    ], [12, 36, 22, 30], size=15, bold_first=True, note='주: 가격 = [[ASSUMPTION]] · 실측 가격 없음 → WTP 조사 (M18) · 유료 전환 (M24)으로 검증')
    h2('2. 가격 가설의 범위')
    table('원가 Floor · 시장 Reference · 가치 Anchor', ['항목', '가격 가설', '원가 Floor', '시장 Reference', '가치 Anchor'],
          [list(r) for r in C.PRICE], [16, 14, 24, 26, 20], size=13, bold_first=True,
          note='주: 원가 Floor = [[DERIVED]] · 시장 Reference = 공개 자료 [[FACT]] · 가치 Anchor = 가사노동 대체 가치 [[DERIVED]]')
    h2('3. 대표 세대 5년 경제성')
    gj('□ 대표 세대 정의: Premium 주방 Remodeling 시점에 MH System 함께 설치 · 직접 판매 · 구매 · Care 가입',
       '○ 5년 기대값 (Skill · Tool = 구매율 반영) · 원가 = 해당 연도 수준 5년 적용 (Y3 원가 = 첫 상용 단계 · Y5 원가 = BOM · 설치 · 방문 개선 후)',
       '○ 모든 값 만원 · VAT · 주방 공사비 별도 [[DERIVED]] (from [[ASSUMPTION]])')
    R_ = H3['R']; C_ = H3['C']
    rev_rows = [['Interface · Integration', nf(R_['kitchen'])], ['Installation · Calibration', nf(R_['comm'])], ['Robot System', nf(R_['robot'])],
                ['Care (5년)', nf(R_['care'])], ['Consumables (5년, 구매율 반영)', nf(R_['cons'])], ['ASSIST Skill (기대값)', nf(R_['sw'])],
                ['Tool · End-effector (기대값)', nf(R_['tool'])], ['5년 매출 합계', nf(H3['rev5'])]]
    cost_names = {'kitchen': 'Interface Kit 원가', 'comm': '설치 · Calibration 원가', 'log': '물류', 'sw': 'Skill 원가', 'tool': 'Tool 원가', 'robot': 'Robot BOM',
                  'warranty': 'Warranty Reserve', 'care': 'Care 원가 (5년)', 'cons': 'Consumables 원가', 'channel': '채널비용 (직접판매 획득)'}
    cost_rows = [[cost_names[k], f"{x:,.1f}".rstrip('0').rstrip('.')] for k, x in C_.items()] + [['총원가', f"{H3['cost5']:,.1f}"]]
    n = max(len(rev_rows), len(cost_rows))
    rev_rows += [['', '']] * (n - len(rev_rows)); cost_rows += [['', '']] * (n - len(cost_rows))
    rr = [a + b for a, b in zip(rev_rows, cost_rows)]
    table('대표 세대 5년 매출 · 원가 (Remodeling 구매 · Y3 원가, 만원)', ['매출 항목', '5년', '원가 항목', '5년'], rr, [32, 14, 38, 16],
          align=['l', 'r', 'l', 'r'], size=15)
    table('대표 세대 5년 산출 결과', ['산출 항목', '값', '정의'], [
        ['Initial (INSTALL)', man(H3['layers']['install']), f"Interface {v('p_rr')} + 설치 {v('p_comm')} + Robot {v('p_robot'):,}"],
        ['Recurring (OPERATE, 5년)', man(H3['layers']['operate']), f"Care 5 × {v('p_care')} + 소모품 5 × {pct(v('cons_attach'))} × {CONS['list_y']:.0f}"],
        ['Expansion (EXPAND, 5년)', man(H3['layers']['expand']), f"ASSIST Skill {pct(v('sw_attach'))} × {v('p_sw')} + Tool {pct(v('tool_attach'))} × {v('p_tool')} · COOK = [[FUTURE]] (0)"],
        ['5년 매출', man(H3['rev5']), '합계'],
        ['Gross Profit (채널비용 전)', f"{man(H3['gp5'])} ({pct(H3['gm5'])})", '매출 − 제품 · 설치 · 서비스 원가'],
        ['Expected Service Cost', man(H3['service_cost5'], 1), 'Care 원가 + 소모품 원가 + Warranty'],
        ['누적 공헌이익', f"{man(H3['contrib5'])} ({pct(H3['cm5'], 1)})", f"Gross Profit − 채널비용 (직접판매 획득비용 {v('cac')})"],
        ['누적 공헌이익 (Y5 원가)', f"{man(H5['contrib5'])} ({pct(H5['cm5'])})", f"Robot BOM {H5['C']['robot']:,.0f} · 설치 {H5['C']['comm']} · Care 원가 {H5['C']['care']:,.0f}"],
    ], [26, 22, 52], align=['l', 'r', 'l'], size=15, bold_rows=[6, 7])
    fig(CH['waterfall'], '대표 세대 5년 매출 → 원가 → 누적 공헌이익 (Remodeling 구매 · Y3 원가, 만원)', w_pct=95)
    h2('4. 설치 경로 · 판매 방식별 경제성')
    table('설치 경로 · 판매 방식별 세대당 5년 (만원)', ['경로', '설치 시점 매출', '5년 매출', 'Gross Profit', 'Service Cost', '공헌이익 (Y3 원가)', '공헌이익 (Y5 원가)'],
          [[lab, nf(HH[k + '_Y3']['y0']), nf(HH[k + '_Y3']['rev5']), nf(HH[k + '_Y3']['gp5']), nf(HH[k + '_Y3']['service_cost5']),
            f"{nf(HH[k + '_Y3']['contrib5'])} ({pct(HH[k + '_Y3']['cm5'])})", f"{nf(HH[k + '_Y5']['contrib5'])} ({pct(HH[k + '_Y5']['cm5'])})"] for k, lab in PATHS],
          [24, 12, 11, 12, 12, 15, 14], align=['l', 'r', 'r', 'r', 'r', 'r', 'r'], size=14, bold_first=True,
          note='주: Rental (MH 보유) = 금융비용 포함 · 잔존가치 15% 회수 기준 · Scale 단계는 Partner 자산 보유')
    fig(CH['paths'], '설치 경로 · 판매 방식별 세대당 5년 누적 공헌이익', w_pct=95)
    gj('□ Retrofit = Partner 수수료 · 현장 Calibration 비용으로 공헌이익 낮음',
       '□ New-build = Project 수주비용의 세대당 배분이 작아 공헌이익률 높음',
       '□ Rental (MH 보유) = 5년 총지불 증가 · 금융비용 · 자산 부담 → Scale 단계는 Partner 보유 구조')
    h2('5. 가정 범위 (Scenario)')
    rng = []
    for s, lab in (('C', 'Conservative'), ('B', 'Base'), ('U', 'Upside')):
        a3, a5 = model.household(s, 2), model.household(s, 4)
        rng.append([lab, f"{v('p_robot', s):,}", f"{v('bom', s)[2]:,} / {v('bom', s)[4]:,}", nf(a3['y0']), nf(a3['rev5']),
                    f"{nf(a3['contrib5'])} ({pct(a3['cm5'])})", f"{nf(a5['contrib5'])} ({pct(a5['cm5'])})"])
    assert abs(model.household('B', 2)['contrib5'] - H3['contrib5']) < 1e-6
    table('Scenario별 세대당 5년 (Remodeling 구매 · 직접, 만원)', ['Scenario', 'Robot ASP', 'BOM Y3 / Y5', '설치 시점', '5년 매출', '공헌이익 (Y3 원가)', '공헌이익 (Y5 원가)'],
          rng, [16, 12, 15, 12, 12, 17, 16], align=['l', 'r', 'r', 'r', 'r', 'r', 'r'], size=14, bold_rows=[1])
    gj(f"□ Conservative (ASP {v('p_robot', 'C'):,} · Interface {v('p_rr', 'C')} · Care {v('p_care', 'C')}만원 · BOM 높음 · 고장 {v('corrective', 'C')}회/년 · 획득비용 {v('cac', 'C')}만원) = Y3 원가 기준 적자",
       '○ 가격 (WTP) · BOM = 사업성 1 · 2순위 변수 → 24개월 검증 우선순위')
    h2('6. Rental 구조')
    gj('□ Rental = 고객 초기 부담 완화 수단',
       '○ Pilot (Y2~Y3): MH 직접 보유 · 운영 (실증 3세대 + 초기 고객)',
       f"○ Scale (Y4~): Rental · Capital Partner가 Robot 자산을 ASP의 {pct(v('wholesale'))}에 매입 · 보유 → 고객은 Partner에 월 {v('p_rent')}만원 · MH는 제품 · SW · Care 담당 + 서비스료 월 {v('partner_fee'):.0f}만원",
       '○ MH Balance Sheet의 Rental 자산 누적 지양',
       f"□ Partner 관점: 매입가 {nf(PI['price'], 1)}만원 · 월 순유입 {PI['inflow']:.0f}만원 · 60개월 · 잔존 {pct(v('residual'))} → 연 IRR 약 {pct(PI['irr_y'], 1)} · 단순 회수기간 약 {PI['payback']:.0f}개월 [[DERIVED]]",
       f"○ 회수 약 {PI['payback']:.0f}개월 > Partner 요구 {PI['hurdle']}개월 [[ASSUMPTION]] → 매입가율 · 서비스료 · 계약기간 조건 협의 필요 (M24)")
    rl = [('dep', '감가 (잔존 15%)'), ('fin', '금융비용 (연 8%)'), ('care', 'Care 원가'), ('grip', 'Grip Kit 원가'), ('reserve', 'Failure Reserve')]
    table('Rental 월 단위 경제성 (만원/월)', ['항목', 'Y3', 'Y5'],
          [[lab, f"{RENT['Y3']['lines'][k]:.1f}", f"{RENT['Y5']['lines'][k]:.1f}"] for k, lab in rl] +
          [['월 원가 합계', f"{RENT['Y3']['cost_m']:.1f}", f"{RENT['Y5']['cost_m']:.1f}"], ['월 요금', f"{RENT['Y3']['fee']}", f"{RENT['Y5']['fee']}"],
           ['월 공헌이익', f"{RENT['Y3']['contrib_m']:.1f}", f"{RENT['Y5']['contrib_m']:.1f}"], ['Payback (개월)', f"{RENT['Y3']['payback']:.0f}", f"{RENT['Y5']['payback']:.0f}"]],
          [50, 25, 25], align=['l', 'r', 'r'], size=15, width_pct=70, bold_rows=[5, 7])
    h2('7. Care · 소모품')
    gj('□ Care = Robot Lifecycle Maintenance (Software 구독 아님)',
       '○ 정기 안전점검 · Calibration · 원격진단 · Robot / Rail 상태점검 · Vision Calibration · SW Update · 소모품 점검 · A/S',
       '○ 선례: 코웨이 국내 렌탈 계정 748만 (2026 1Q) · LG 가전 구독 매출 2조원+ · 케어매니저 약 4,000명 (2025) [[FACT]] [S12 · S41]',
       '□ 소모품 = 실제 마모 · 위생 기반 (억지 Lock-in 아님)',
       '○ 후보: Grip Pad · Finger Pad · Food-contact Tip · Suction Seal · Cleaning Pad · Protective Cover',
       f"○ 교체주기 = Pad 수명 가속시험 (목표 ≥ {KL['pad_life']:,.0f}회 파지, M18~M24)으로 확정 · 식품 접촉 부품 = 「기구 및 용기 · 포장의 기준 및 규격」 대응 [S48]")
    table('Care 연 단위 경제성 (만원/대 · 년)', ['항목', 'Y3', 'Y5'], [
        ['요금', f"{CARE['Y3']['fee']}", f"{CARE['Y5']['fee']}"], ['정기 방문 원가', f"{CARE['Y3']['visits']:.1f}", f"{CARE['Y5']['visits']:.1f}"],
        ['고장 방문 원가', f"{CARE['Y3']['corrective']:.1f}", f"{CARE['Y5']['corrective']:.1f}"], ['Cloud · SW', f"{CARE['Y3']['cloud']}", f"{CARE['Y5']['cloud']}"],
        ['원가 합계', f"{CARE['Y3']['cost']:.1f}", f"{CARE['Y5']['cost']:.1f}"], ['마진', pct(CARE['Y3']['margin']), pct(CARE['Y5']['margin'])],
    ], [50, 25, 25], align=['l', 'r', 'r'], size=15, width_pct=70, bold_rows=[4, 5])
    table('소모품 Kit 구성 (정가)', ['Kit', '단가 (만원)', '교체 (회/년)', '연 (만원)'],
          [[k, f"{p:.1f}", f"{n_}", f"{p * n_:.0f}"] for k, p, n_ in CONS['kits']] + [['정가 합계', '', '', f"{CONS['list_y']:.0f}"]],
          [40, 20, 20, 20], align=['l', 'r', 'r', 'r'], size=15, width_pct=70, bold_rows=[len(CONS['kits'])],
          note=f"주: 구매율 {pct(CONS['attach'])} · 원가율 {pct(v('cons_cogs'))} 가정 [[ASSUMPTION]]")
    h2('8. 민감도')
    fig(CH['tornado_hh'], f"세대당 5년 공헌이익 민감도 (Remodeling 구매 · Y3 원가 · 기준 {H3['contrib5']:,.0f}만원)", w_pct=95)
    gj('□ 최대 변수 = 고객 지불의사 (Robot ASP) · Robot BOM',
       '○ ASP ±20% → ±286만원 · BOM ±20% → ±236만원 (기준 428만원 대비)',
       '○ 대응: WTP n ≥ 300 · 예약금 테스트 (M18) · 100대/년 BOM 견적 (M18) · 원가 실측 (M24)')

    # ---------------------------------------------------------------- Ⅵ
    h1('Ⅵ. 시장 분석')
    h2('1. 시장 기초 통계')
    table('주택 · 가사노동 기초 통계', ['항목', '값', '구분', '출처 · 산식'], [list(r) for r in C.HOUSING], [30, 26, 12, 32], size=14, bold_first=True)
    gj(f"□ 국내 아파트 약 {MK['apt'] / 10:,.0f}만호 = 잠재 대상 (실구매 시장 아님)",
       '□ 준공 20년 이상 주택 56.0% · 30년 이상 30.6% → 주방 교체 수요 기반 [[FACT]]',
       f"□ 연간 주방 교체 30만 세대 [[ASSUMPTION]] = 교차검증 ① {MK['tri1'] / 10:.1f}만 (20년+ 아파트 ÷ 교체주기 22년) · ② {MK['tri2'] / 10:.1f}만 (매매 × 아파트 70% × 교체 40% + 비거래 노후 10만)")
    h2('2. Bottom-up 시장 산정')
    gj('□ 산정 원칙 = 큰 TAM이 아닌 세대 수 × 적용률 × 단가',
       '○ 비율 = 전부 가정 → 견적 20건 · 평면 30개 분석 · 소비자 조사로 검증')
    table('채널별 시장 산정 (연간)', ['시장', '산식 (세대 × 적용률)', '대상 세대', '패키지 단가', '연 규모'], [
        ['① Remodeling (Beachhead)', f"주방 교체 30만 × Premium 10% × 적용 60% · 로봇 동시 구매 {pct(v('attach')[2])}", f"{MK['fit'] * 1000:,.0f}/년", man(MK['pkg_remodel'], 1), f"{MK['sam_remodel']:,.0f}억원"],
        ['② Retrofit', f"{MK['apt'] / 10:,.0f}만 × Premium 10% × 식세기 60% × 호환 40% = {MK['retro_pool'] / 10:.1f}만 (재고) × 연 0.5%", f"{MK['retro_annual'] * 1000:,.0f}/년", man(MK['pkg_retro']), f"{MK['sam_retro']:,.0f}억원"],
        ['③ New-build', '입주 20만 × Premium 단지 15% × Option 10%', f"{MK['new_opt'] * 1000:,.0f}/년", man(MK['pkg_new'], 1), f"{MK['sam_new']:,.0f}억원"],
        ['SAM 합계', '① + ② + ③', f"{(MK['fit'] + MK['retro_annual'] + MK['new_opt']) * 1000:,.0f}/년", '-', f"{MK['sam']:,.0f}억원"],
        ['④ Recurring', f"Installed Base × 구매 고객 ARPU {MK['arpu']:.1f}만원/년 (Care · 소모품)", '1,000대당', '-', f"{MK['recurring_per_1000']:.1f}억원"],
        ['Y5 계획 (SOM)', f"설치 {MK['som_hh']:,.0f}세대 = 대상 세대의 {pct(MK['som_share_hh'], 1)}", f"{MK['som_hh']:,.0f}", '-', f"{MK['som']:.1f}억원"],
    ], [20, 40, 12, 14, 14], align=['l', 'l', 'r', 'r', 'r'], size=14, bold_first=True, bold_rows=[3, 5],
          note='주: Remodeling 패키지 = Interface 450 + 로봇 동시 구매율 × (Robot 1,490 + 설치 80) · New-build = Option 220 + 입주 시 로봇 구매 25% × (Robot + 설치) [[DERIVED]]')
    fig(CH['market'], f"채널별 연 대상 세대와 연 규모 — SAM 연 {MK['sam']:,.0f}억원 · Y5 계획 {MK['som_hh']:,.0f}세대 (대상 세대의 {pct(MK['som_share_hh'], 1)})", w_pct=95)
    gj('□ Remodeling = 대상 세대 · 연 규모 모두 최대 → 첫 시장 (Beachhead)',
       f"□ New-build = Option 단가 {nf(MK['pkg_new'], 1)}만원 → 세대 대비 연 규모 비중 작음 · 단지 단위 Scale 채널",
       f"□ 적용 60% = 확보 평면 5종 (기본 배치 가능 1)보다 높은 가정 → 평면 30개 분석으로 검증 (M6)")
    h2('3. 연관 시장 · 참고 지표')
    table('리모델링 · 렌탈 · Care 참고 지표', ['항목', '값', '구분', '비고'], [list(r) for r in C.REFS], [28, 34, 12, 26], size=14, bold_first=True)
    h2('4. 시장 가정 검증 계획')
    table('시장 가정 검증 계획', ['가정', '현재 상태', '검증 방법', '시점'], [list(r) for r in C.MKT_VALID], [30, 22, 38, 10], size=14, bold_first=True)

    # ---------------------------------------------------------------- Ⅶ
    h1('Ⅶ. 사업화 전략')
    h2('1. 단계별 진입 전략')
    gj('□ 초기 Mass Market 진입 없음 → 검증 채널에서 Reference · 고객 Data 확보 후 확장')
    table('단계별 진입 전략', ['단계', '시장', '시기', '목적', '채널', '역할'], [
        ['Phase 1', 'Premium Kitchen Remodeling', 'Y2 실증 → Y3~', '제품 · 가격 수용성 · 설치 · 사용성 검증 · 초기 Reference · 고객 Data', '직접 판매 + 주방 · 인테리어 Partner', '검증 채널'],
        ['Phase 2', 'Compatible Existing Retrofit', 'Y4~', '전체 Remodeling 없이 적용 가능한 고객 확대 · 호환성 Check 표준화', '설치 Partner 경유', '고객 확대'],
        ['Phase 3', 'New-build Apartment', 'Y3 계약 → Y5 입주', '건설사 · 주방가구사 B2B2C · 단지 단위 Scale', 'Interface Option + Robot 후설치', 'Scale 채널'],
    ], [10, 20, 14, 30, 16, 10], size=14, bold_first=True)
    h2('2. 연도별 설치 계획')
    fig(CH['installs'], '채널별 연간 설치 세대 (Base Plan) [TARGET]', w_pct=95)
    yrs = M['years']
    table('채널별 설치 세대 · Installed Base (Base Plan)', ['구분'] + yrs, [
        ['Remodeling 직접'] + [nf(x) for x in B['rd']], ['Remodeling Partner'] + [nf(x) for x in B['rp']],
        ['Retrofit'] + [nf(x) for x in B['rt']], ['New-build 입주 (로봇 설치)'] + [nf(x) for x in B['ni']],
        ['연간 설치 합계'] + [nf(x) for x in B['kitchens']], ['Installed Base (연말, 로봇)'] + [nf(x) for x in B['base_end']],
    ], [30, 14, 14, 14, 14, 14], align=['l'] + ['r'] * 5, size=15, bold_rows=[4],
          note=f"주: [[TARGET]] · 신축 Interface Option 계약 Project {v('projects')[2]}→{v('projects')[4]}개 (Project당 {v('hh_project')}세대 · Option {pct(v('option_rate'))}) · Rental 비중 {pct(v('rental_share')[4])} (Y5) [[ASSUMPTION]]")
    h2('3. 운영 구조: MH Core vs Partner')
    table('MH Core vs Partner 역할 분담', ['MH Core', 'Partner'], [
        ['Robot · Robot Hand', '철거 · 가구'], ['Manipulation Skill', '전기 · 설비'], ['Calibration', '마감 공사'],
        ['Interface 표준', '(신축) 건설사 · 주방가구사'], ['Safety · 시운전 · QA', '(Rental) 렌탈 · 캐피탈사'],
    ], [50, 50], size=15, width_pct=80)
    gj('□ 설치 물량 증가 ≠ 본사 현장인력 비례 증가',
       '○ 현장 인력 = 설치 · 서비스 엔지니어 중심 (24개월 차 2명)',
       f"○ 설치 인시 = Calibration 기술로 Y2 약 {KL['inst_h'][1]:.0f} → Y5 약 {KL['inst_h'][4]:.0f}인시 목표 [[TARGET]]",
       '□ Partner 조건 = M18~M24 협의 · 확보 예정 (현재 계약 · LOI 없음)')
    h2('4. 매출 구성 전망')
    fig(CH['rev_layers'], '연도별 매출 구성 (Base Plan, 억원) [TARGET]', w_pct=95)
    table('사업 단계별 매출 (Base Plan, 억원)', ['구분'] + yrs, [
        ['INSTALL (Interface · 설치 · Robot)'] + [f"{x / 1e4:.1f}" for x in B['install']],
        ['OPERATE (Rental · Care · 소모품)'] + [f"{x / 1e4:.1f}" for x in B['recurring']],
        ['EXPAND (Skill · Tool)'] + [f"{x / 1e4:.1f}" for x in B['expand']],
        ['매출 합계'] + [f"{x / 1e4:.1f}" for x in B['rev']],
        ['OPERATE + EXPAND 비중'] + [pct(x) for x in B['oe_share']],
    ], [30, 14, 14, 14, 14, 14], align=['l'] + ['r'] * 5, size=15, bold_rows=[3])
    gj(f"□ 반복매출 (OPERATE) Y3 {B['recurring'][2] / 1e4:.1f} → Y5 {B['recurring'][4] / 1e4:.1f}억원 (Installed Base {B['base_end'][4]:,.0f}대) [[DERIVED]]",
       f"□ Y5 매출 중 OPERATE + EXPAND {pct(B['oe_share'][4])} = 설치 초기 구조 → Installed Base 누적 후 비중 확대")

    # ---------------------------------------------------------------- Ⅷ
    h1('Ⅷ. 경쟁 및 지식재산')
    h2('1. 경쟁 구도')
    table('경쟁 · 인접 기업 (공개 자료 기준)', ['기업 · 제품', '유형', '범위', '가격 · 일정', '특징', '출처'], [list(r) for r in C.COMP],
          [16, 14, 22, 22, 18, 8], size=13, bold_first=True, note='주: 회사 발표 · 보도 기준 [[FACT]] · 출시 · 가격 미확인 항목 표기 · 2026.10 기준')
    gj('□ 경쟁 Category',
       '○ 가전사 (가전 내부 자동화 · 구독) · 조리 로봇 (전용 주방 · 조리대 기기) · Humanoid · 이동형 (범용 손 · 모델 학습) · 협동로봇 + Gripper (부품) · 주방가구사 (시공)',
       '□ MH 목표 Position',
       '○ 식기 · 도구용 Hand · CLEAN → COOK Skill 확장 · Calibration + 최소 Interface · 주방 공사 연계 설치 · Care · 소모품',
       '○ 우위 = 신규 주방 적용 시간 · 경제성 → 실증으로 입증 필요',
       '□ 대응 방향',
       '○ 가전사 · 가구사 직접 진입 가능 (LG CLOiD 2028 상용화 목표) → Interface · 시공 Partner 후보로 설계',
       '○ Humanoid = 위협만이 아님: 공개 범용 모델 → MH Manipulation Layer 활용 · MH Interface · Skill → 다른 Robot에도 적용',
       '○ 방어력 = 단일 특허가 아닌 축적: 식기 · 도구 Grasp Data · Skill Library · Calibration 절차 · Interface 표준 · Installed Base · Care Data [[TARGET]]')
    h2('2. 지식재산 전략')
    gj('□ 현재 출원 0건 · 선행기술조사 M3 · 청구항 변리사 검토 예정 · 등록 가능성 미정',
       '□ 식기 로봇 · 주방 Rail Arm · 수납장 로봇 · 교체형 Gripper 부품 선행특허 존재 → 넓은 청구 대신 구체 구조 · 방법 청구')
    table('출원 후보 12개 묶음', ['영역', '출원 후보 (Family)', '사업 중요도', '차별성', 'Prior Art Risk (참고)', '순위', '시점'],
          [[*r[:5], str(r[5]), r[6]] for r in C.IP], [11, 30, 10, 8, 27, 6, 8], size=13, bold_first=True,
          note='주: 선행특허 = 참고 검색 결과 · FTO 판단 아님 · 출원 전 변리사 검토 [[TARGET]]')
    table('출원 일정', ['시점', '내용'], [
        ['M3', '선행기술조사 (KIPRIS · USPTO · EPO · Google Patents) · 예비 FTO'],
        ['M6~M9', '1순위 2건 출원 (Replaceable Food-contact Module · Task Coordinate Calibration) → M12 Gate 확인 항목'],
        ['M12~M18', '2순위 5개 후보 중 3건 출원 (Robot Home · Appliance Interface · Kitchen Object Handling · Kitchen Mapping · Adaptive Finger 중, 실시예 확보 순)'],
        ['M18', 'PCT 1건 (1순위 중 1건)'],
    ], [14, 86], size=15, bold_first=True, note=f"주: 24개월 IP 예산 {sum(v('ip')[:2]):,}만원 (선행조사 · 국내 5건 · PCT 1건) [[ASSUMPTION]] — TIPS 연구활동비 편성 대상")

    # ---------------------------------------------------------------- Ⅸ
    h1('Ⅸ. TIPS R&D 계획')
    h2('1. TIPS 과제와 Seed의 역할 분담')
    table('TIPS 과제 vs 민간 Seed', ['구분', 'TIPS 과제', '민간 Seed'], [
        ['목적', '기술 검증 (Technology De-risking)', '사업 검증 (Commercial Validation) · 과제 외 개발'],
        ['범위', 'Adaptive Robot Hand · Manipulation · Calibration · Safety · Reliability · Integrated Workflow',
         f"기관부담금 · 과제 외 인건비 {(people - tips_people) / 1e4:.2f}억원 (참여율 외 R&D · 사업 · 현장 · 경영지원) · 목업 운영 · 고객 검증 · 실증 · WTP · Partner 개발"],
        ['결과물', 'Hand v3 · CLEAN Skill Library · Calibration Tool · Interface 표준 · Safety Architecture · 실증 보고서', 'WTP 조사 · 예약금 · 유료 전환 · Partner 조건 · BOM · 설치 · Service 원가'],
        ['판단 Gate', 'M6 Hand Buy/Build · M12 목업 CLEAN · M18 타 주방 적용', 'M18 WTP · M24 유료 전환 · 원가'],
        ['금액', f"과제 {eok(TP['total'], 2)} (정부 8억원 + 기관부담 {eok(TP['private'], 2)})", f"Seed {F['seed_range'][0]}~{F['seed_range'][1]}억원 (Lean ~ Base)"],
    ], [14, 43, 43], size=15, fill_first=True, bold_first=True)
    h2('2. TIPS 2026 주요 규정')
    table('TIPS 2026 주요 규정 (일반트랙)', ['항목', '내용', '구분'], [
        ['정부지원 R&D', '최대 8억원 · 최대 24개월', '[[FACT]] [S33]'],
        ['정부지원 비율', '총 연구개발비의 75% 이내 · 기관부담 25% 이상 (그중 현금 10% 이상)', '[[FACT]] [S33]'],
        ['운영사 선투자', '수도권 2억원 이상 · 비수도권 1억원 이상 (Seed 라운드에 포함)', '[[FACT]] [S33]'],
        ['창업팀 요건', '대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 지분 30% 이하', '[[FACT]] [S33]'],
        ['고용', '정부지원 5억원당 청년 1명 신규 채용', '[[FACT]] [S33]'],
        ['비R&D 연계', f"창업사업화 · 해외마케팅 각 최대 {v('biz_link') / 1e4:.1f}억원 (선정 뒤 별도 신청, 본 계획 미반영)", '[[FACT]] [S33]'],
        ['접수', '분기별 접수 (운영사 추천)', '[[FACT]] [S52]'],
    ], [18, 66, 16], size=15, bold_first=True)
    h2('3. 세부 연구개발 과제 (WP1~WP6)')
    for w in C.WP:
        h3(f"{w[0]}. {w[1]} ({w[2]})")
        gj(f"□ 목표: {w[3]}", '□ 주요 내용', *[f"○ {x}" for x in w[4]], f"□ 산출물: {w[5]}", f"□ KPI: {w[6]}", f"□ 담당 (채용 계획): {w[7]}")
    h2('4. 24개월 추진 일정')
    fig(CH['gantt'], 'Work Package 일정과 Gate (M6 · M12 · M18 · M24)', w_pct=95)
    table('구간별 실행 계획', ['구간', '기술 (TIPS WP)', '사업 검증 (Seed)', 'Gate'], [
        ['0~6M', 'Kitchen Task 분석 · Robot Architecture · Hand v1 (M4) · Object Grasp Test (30종, 상용 Gripper 비교) · 초기 Calibration', '리드 3명 채용 · 시간일지 조사 30세대 · 인터뷰 50명 · 평면 30개 분석 · 견적 20건 · 선행기술조사 (M3)', 'M6'],
        ['7~12M', 'CLEAN Skill · 식세기 Interaction · Hand v2 (M10) · Safety 기능 · 1:1 Kitchen Mock-up · 목업 CLEAN 전 과정', '인증기관 사전상담 (M9) · 1순위 특허 2건 출원 · 리모델링 · 렌탈 Partner 탐색 · 사업개발 합류 (M7)', 'M12'],
        ['13~18M', '주방 3종 적용 시험 · 실패 복구 · Hand v3 (M18) · Pilot 착수', 'WTP 조사 n ≥ 300 · 예약금 테스트 · 전기 · EMC 사전시험 · BOM 100대/년 견적 · PCT 1건', 'M18'],
        ['19~24M', '연속 운전 신뢰성 · 설치 표준 · 실거주 3세대 실증 · BOM · 설치 · Service 원가 실측', '유료 실증 전환 · Partner 조건 (리모델링 1 · 렌탈/캐피탈 1) · 출원 누적 5건 · Series A 준비', 'M24'],
    ], [10, 42, 40, 8], size=14, bold_first=True)
    h2('5. 단계별 Gate')
    table('Gate 판단 기준', ['Gate', '확인할 Evidence', '통과 기준', '미달 시 조치'], [list(g) for g in C.GATES], [8, 36, 28, 28], size=14, bold_first=True,
          note='주: 통과 기준 = [[TARGET]] · Gate별 판단 = 계속 · 범위 축소 · 전환')
    h2('6. TIPS 과제 사업비 편성')
    table('TIPS 과제 사업비 편성 (Base, 만원)', ['비목', '내용', '1차년도', '2차년도', '합계', '구분'],
          [[r['cat'], r['item'], nf(r['y1']), nf(r['y2']), nf(r['total']), r['kind']] for r in TP['rows']] +
          [['합계', '', nf(TP['year_total'][0]), nf(TP['year_total'][1]), nf(TP['total']), '']],
          [16, 38, 12, 12, 12, 10], align=['l', 'l', 'r', 'r', 'r', 'c'], size=14, bold_rows=[len(TP['rows'])], note='주: [[ASSUMPTION]] · 협약 시 비목 기준 재확인')
    table('편성 점검', ['점검', '값 (만원)', '판단'], [
        ['정부지원 (75%)', nf(TP['gov']), '상한 충족'], ['기관부담 (25%)', nf(TP['private']), '현금 + 현물'],
        ['기관부담 현금', nf(TP['private_cash']), f"현금 ≥ 10% 충족 (기관부담의 {pct(TP['private_cash'] / TP['private'])})"],
        ['기관부담 현물', nf(TP['inkind']), 'Founder 인건비 참여분'], ['간접비율', pct(TP['indirect_rate'], 1), '협약 기준 확인 필요'],
    ], [30, 25, 45], align=['l', 'r', 'l'], size=15, width_pct=85)

    # ---------------------------------------------------------------- Ⅹ
    h1('Ⅹ. 조직 및 인력')
    h2('1. 필요 핵심 역량')
    gj('□ 필요 핵심 역량 3개',
       '○ 로봇 조작 (Hand · Skill): Manipulation · 제어 · Hand 기구 · 센싱',
       '○ 주방 · 건축 시공 (Interface · 시공 Partner): 주방 가구 · 설비 · 설치 표준',
       '○ 고객 · Partner 영업: 리모델링 · 렌탈 · 건설사 · 가구사 접점',
       '□ 리드 3명 (Manipulation · Perception · Hand) 우선 채용 → M6 미충원 시 일정 재편')
    h2('2. Founder 정보')
    table('Founder 확인 항목', ['항목', 'Founder 1 (대표 · 사업 총괄)', 'Founder 2 (기술 총괄)', '확인 내용'], [
        [a, '[Founder 정보 필요]', '[Founder 정보 필요]', b] for a, b in C.FOUNDER_INPUTS[:10]
    ], [24, 18, 18, 40], size=14, bold_first=True, note='주: 사실 확인 전 공란 유지 · 추정 · 가공 정보 기재 없음')
    h2('3. 24개월 채용 계획')
    kind_k = {'founder': 'Founder', 'rnd': 'R&D', 'biz': '사업', 'ops': '경영지원', 'field': '현장'}
    table('채용 계획 · 인건비 (ASSUMPTION, 만원)', ['역할', '구분', '시작', 'Y1 인건비', 'Y2 인건비', 'TIPS 참여율'],
          [[t['role'], kind_k[t['kind']], f"M{t['start']}", nf(t['cost'][0]), nf(t['cost'][1]), pct(t['part']) if t['part'] else '-'] for t in F['team']] +
          [['합계', '', '', nf(F['people'][0]), nf(F['people'][1]), '']],
          [38, 11, 9, 14, 14, 14], align=['l', 'c', 'c', 'r', 'r', 'r'], size=14, bold_rows=[len(F['team'])],
          note=f"주: 연 인건비 = 연봉 × 1.2 (4대보험 · 퇴직급여) · Founder 인건비 = TIPS 현물 편성 · Lean안 = Hand 센싱 · Skill/Data · 현장 서비스 엔지니어 제외 · 시험 인력 M19 (24개월 차 약 {F['heads_m24_lean']:.0f}명)")
    fig(CH['fte'], f"월별 인원 (FTE) — Y1 평균 {F['fte'][0]:.1f}명 → Y2 평균 {F['fte'][1]:.1f}명 · 24개월 차 약 {round(F['heads_m24'] + 0.5):.0f}명", w_pct=95)
    h2('4. TIPS 창업팀 요건 대응')
    gj('□ 대표 포함 창업팀 2인 이상 지분 60% 이상 → Founder 2인 지분 · 역할 확정 필요 [Founder 정보 필요]',
       '□ 정부지원 5억원당 청년 1명 신규 채용 → 신규 채용 12명 계획 중 청년 해당 인원 확인 (적용 인원 = 협약 시점 공고 기준)',
       '□ 운영사 선투자 (수도권 2억원 이상) → Seed 라운드에 포함 · 법인 소재지 확인 필요')

    # ---------------------------------------------------------------- Ⅺ
    h1('Ⅺ. 재무 계획 및 투자 요청')
    h2('1. 24개월 자금 사용 계획')
    table('24개월 사용처 (Base, 만원)', ['구분', '내용', 'Y1', 'Y2', '24개월', 'TIPS 편성', 'Seed'],
          [[u['cat'], u['item'], nf(u['y'][0]), nf(u['y'][1]), nf(sum(u['y'])), nf(sum(u['tips'])) if sum(u['tips']) else '-', nf(sum(u['y']) - sum(u['tips']))] for u in F['uses']] +
          [['합계', '', nf(F['spend'][0]), nf(F['spend'][1]), nf(F['spend_total']), nf(TP['total']), nf(F['spend_total'] - TP['total'])]],
          [12, 40, 9, 9, 10, 10, 10], align=['l', 'l', 'r', 'r', 'r', 'r', 'r'], size=12, bold_rows=[len(F['uses'])],
          note='주: 인건비 = 팀 14명 (Founder 2 + 신규 12) · 예비비 = 인건비 외 지출의 10% · 실증 순비용 = 실증 3세대 하드웨어 · 설치 원가 − 실증 매출 (50% 할인) [[DERIVED]]')
    assert abs(sum(sum(u['y']) for u in F['uses']) - F['spend_total']) < 1
    fig(CH['uses'], f"24개월 사용처 — 인건비 {sum(F['uses'][0]['y']) / 1e4:.1f}억원 ({pct(sum(F['uses'][0]['y']) / F['spend_total'])}) 중심", w_pct=95)
    h2('2. 재원 구성 및 Seed 산정')
    table('Seed 범위 산식 (만원)', ['안', '24개월 지출', 'TIPS 정부지원', 'Buffer (3개월)', 'Seed 필요액', '차이'], [
        ['Base (기술 + 사업 검증)', nf(F['spend_total']), nf(TP['gov']), nf(F['buffer']), nf(F['seed_base']), '-'],
        ['Lean (팀 · 목업 · 실증 축소)', nf(F['lean_total']), nf(TP['gov']), nf(F['seed_lean'] - F['lean_total'] + TP['gov']), nf(F['seed_lean']), 'Hand 센싱 · Skill/Data · 서비스 엔지니어 제외 · 시험 인력 M19 · 비용 축소'],
        ['TIPS 미선정 (Lean 범위)', nf(sum(F['no_tips_spend'])), '0', nf(F['seed_no_tips'] - sum(F['no_tips_spend'])), nf(F['seed_no_tips']), '연구수당 없음 · 일정 연장 또는 비R&D 과제로 보완'],
    ], [22, 12, 12, 12, 12, 30], align=['l', 'r', 'r', 'r', 'r', 'l'], size=13, bold_first=True)
    gj(f"□ Seed Base = 지출 {eok(F['spend_total'])} − TIPS 8억원 + Buffer {eok(F['buffer'], 2)} (Y2 월평균 지출 × {F['buffer_months']}개월) = 약 {eok(F['seed_base'])}",
       f"□ Seed 범위 = {F['seed_range'][0]}~{F['seed_range'][1]}억원 (Lean {eok(F['seed_lean'])} ~ Base {eok(F['seed_base'])}) · Runway (Base, TIPS 포함) 약 {F['runway_base']:.0f}개월",
       f"□ 운영사 선투자 요건 (수도권 {v('op_invest_min') / 1e4:.0f}억원 이상) = Seed 라운드에 포함 [[FACT]]",
       '□ 투자 조건 · 기업가치 = 협의 · 비R&D 연계 (창업사업화 · 해외마케팅) = 선정 후 별도 신청 (계획 미반영)')
    h2('3. 5개년 손익 · 현금흐름')
    fl = lambda xs: [f"{x / 1e4:.1f}" for x in xs]
    table('5개년 계획 (Base, 억원)', ['항목'] + yrs, [
        ['매출'] + fl(B['rev']), ['매출총이익'] + fl(B['gp']), ['공헌이익'] + fl(B['contrib']), ['Opex'] + fl(B['opex']),
        ['영업이익 (근사)'] + fl(B['op']), ['연간 현금흐름'] + fl(B['cash']), ['누적 현금'] + fl(B['cum_cash']),
        ['설치 세대 [[TARGET]]'] + [nf(x) for x in B['kitchens']], ['평균 인원 (FTE)'] + [f"{x:.1f}" for x in v('fte')],
    ], [28, 14.4, 14.4, 14.4, 14.4, 14.4], align=['l'] + ['r'] * 5, size=15, bold_rows=[0, 6],
          note='주: Y1~Y2 = Seed + TIPS 24개월 · Y3~ = Series A 전제 · 영업이익 = 공헌이익 − Opex (감가 · 세금 근사) [[DERIVED]]')
    fig(CH['cash'], f"영업이익과 누적 현금흐름 (Base, 억원) — 누적 최저 {B['cum_cash'][4] / 1e4:,.1f}억원", w_pct=95)
    gj(f"□ Base 누적 현금 최저 {B['cum_cash'][4] / 1e4:,.0f}억원 → Series A 이후에도 추가 자금이 필요한 하드웨어 사업 구조",
       f"□ Series A 이후 2년 (Y3~Y4) 현금 소요 약 {M['post_seed_burn']['y3_y4'] / 1e4:.0f}억원 [[DERIVED]]",
       f"□ 손익분기 설치 물량 연 약 {M['breakeven_kitchens']:,.0f}세대 (Y5 단가 · 원가 · Opex 기준, 세대당 공헌이익 약 {M['contrib_per_kitchen_y5']:.0f}만원)",
       '□ 24개월 Evidence (WTP · 원가 실측 · 유료 전환) = Series A 규모와 가능성 결정')
    h2('4. Scenario 비교')
    table('Scenario별 매출 / 영업이익 (억원)', ['Scenario'] + yrs,
          [[n] + [f"{a / 1e4:.1f} / {b / 1e4:.1f}" for a, b in zip(SC[k]['rev'], SC[k]['op'])] for k, n in (('C', 'Conservative'), ('B', 'Base'), ('U', 'Upside'))],
          [20, 16, 16, 16, 16, 16], align=['l'] + ['r'] * 5, size=14, bold_rows=[1])
    fig(CH['scen'], 'Scenario별 매출 (억원)', w_pct=95)
    h2('5. 회사 단위 민감도')
    sc_ = M['sens_company']
    table(f"Y5 공헌이익 민감도 (기준 {sc_['base'] / 1e4:.1f}억원)", ['변수', '불리 (억원)', '유리 (억원)'],
          [[d['name'], f"{d['lo'] / 1e4:+.1f}".replace('-', '−'), f"{d['hi'] / 1e4:+.1f}"] for d in sc_['items']],
          [56, 22, 22], align=['l', 'r', 'r'], size=15, width_pct=85)
    gj('□ 회사 단위 1순위 변수 = Customer WTP (Robot ASP · Interface) · 2순위 = Robot BOM → 세대당 민감도와 동일 순서')
    h2('6. 24개월 Value Creation과 후속 투자 기준')
    table('24개월 Value Creation', ['단계', '내용'], [
        ['TODAY', 'Concept · Technology Hypothesis · Business Hypothesis (시제품 · 고객 · 매출 없음)'],
        ['Seed + TIPS (24개월)', f"{eok(F['spend_total'])} 지출 · 24개월 차 약 {round(F['heads_m24'] + 0.5):.0f}명"],
        ['24M TARGET — 기술', 'Working Kitchen Prototype · Adaptive Robot Hand · Manipulation Skill Library · Calibration System · Safety Architecture · 주방 3종 적용 검증'],
        ['24M TARGET — 경제성', 'Robot BOM (100대/년 견적) · Installation Cost · Service Cost (실거주 3세대 실측)'],
        ['24M TARGET — 시장', 'Customer WTP (n ≥ 300) · Pilot · Paid Pilot (≥ 2세대) · Partner Evidence · 출원 5건 + PCT 1건'],
        ['NEXT ROUND', 'Productization · Production · Distribution · Scale (Series A 판단 기준 = 기술 성공 + 유료 전환 + 원가 실측)'],
    ], [24, 76], size=15, fill_first=True, bold_first=True)

    # ---------------------------------------------------------------- Ⅻ
    h1('Ⅻ. 리스크 및 대응')
    h2('1. 리스크 관리표')
    table('리스크 관리표', ['구분', 'Risk', '확인 시점', '대응', '중단 · 재편 기준'], [list(r) for r in C.RISKS], [10, 26, 18, 26, 20], size=13, bold_first=True)
    h2('2. 핵심 리스크 대응')
    gj('□ 기술: 자체 Hand 우위 미검증',
       '○ M6 30종 비교 → 열위 시 상용 Gripper + 교체형 Pad (Buy) · Skill · Calibration에 집중',
       '□ 기술: 타 주방 적용 시 성능 급락 (Calibration 과다)',
       '○ M18 주방 3종 시험 → Calibration > 8시간이면 Retrofit 보류 · Remodeling 집중 · Interface 보강',
       '□ 시장: CLEAN 가치 대비 가격 부담 (WTP 부족)',
       '○ M18 WTP n ≥ 300 · 예약금 → WTP < 15%면 Rental 중심 · 구성 · 가격 재설계 · ASSIST 묶음 · Seed 범위 재편',
       '□ 사업: 설치 · A/S 원가 과다',
       '○ M24 실거주 3세대 실측 → 원격진단 · Partner 교육 · 설치 표준 · 설치 > 2인 2일이면 채널 재검토',
       '□ 안전 · 인증: 가정용 로봇 기준 불확실 (IEC 63682 발행 전)',
       '○ M9 인증기관 사전상담 · M18 사전시험 → 저속 · Zone 분리 · 사람 감지 시 정지 · 인증 경로 미확정 시 판매 보류',
       '□ 자금: TIPS 미선정',
       f"○ Lean 범위 · 비R&D 과제 · 일정 연장 (TIPS 없이 Seed 약 {F['seed_no_tips'] / 1e4:.1f}억원)",
       '□ 팀: Founder 공백 · 핵심 리드 채용 지연',
       '○ M3 리드 3명 채용 · 지분 보상 → M6 리드 미충원 시 일정 재편')

    # ---------------------------------------------------------------- ⅩⅢ
    h1('ⅩⅢ. 확인 필요 사항 및 향후 과제')
    h2('1. Evidence 확보 계획')
    table('Evidence 현황과 확보 계획', ['항목', '현재', '필요 Evidence', '방법', '시점'], [list(r) for r in C.EVIDENCE], [16, 18, 30, 22, 14], size=13, bold_first=True)
    h2('2. 제출 전 확인 사항')
    table('Founder · 법인 입력 항목', ['항목', '필요 내용'], [list(r) for r in C.FOUNDER_INPUTS], [28, 72], size=14, bold_first=True,
          note='주: 입력 전 [Founder 정보 필요] 표기 유지 · 제출 전 전 항목 사실 확인')
    gj('□ 수치 확인',
       f"○ 가격 · 원가 · 비율 = 전부 [[ASSUMPTION]] → 견적 20건 · 평면 30개 · 소비자 조사 결과로 갱신",
       '○ TIPS 규정 = 2026 공고 기준 → 접수 시점 공고 재확인 (간접비율 · 비목 기준 포함)',
       '□ 표현 확인',
       '○ 고객 · 계약 · Partner · 매출 = 없음 (가상 사례 기재 없음)',
       '○ 특허 = 출원 예정 (등록 가능성 미정) · 제품 그림 = [[CONCEPT]]')

    # ---------------------------------------------------------------- 부록
    h1('부록')
    h2('A. 용어 정리')
    table('주요 용어', ['용어', '의미'], [
        ['CLEAN · ASSIST · COOK', '식기 정리 (첫 검증) · 조리 보조 (중기) · 조리 Workflow (장기 R&D) 단계'],
        ['Adaptive Robot Hand', '식기 · 도구를 Tool 교체 없이 다루는 로봇 손 (교체형 Food-contact Pad 포함)'],
        ['Manipulation Skill', '로봇이 수행하는 작업 단위 (집기 · 놓기 · 넣기 · 꺼내기 · 열기/닫기 · 실패 복구)'],
        ['Calibration', '새 주방에 설치 시 주방 Mapping · 좌표계 설정 · 가전 · 수납 위치 등록 · 작업 Parameter 조정'],
        ['타 주방 적용', '한 주방에서 만든 Skill을 다른 주방에 설치해 같은 성능으로 실행'],
        ['Environment Interface', '반복 작업 위치에만 두는 최소 장치 (Robot Home · Rail · Dock · 식세기 Interface · Vision 기준점)'],
        ['Robot Home', '로봇 보관함 겸 대기 위치 (평소 로봇 수납 · 고장 시 자동 복귀)'],
        ['Drop Zone', '사용자가 식기를 내려놓는 조리대 위 지정 구역'],
        ['Vision 기준점', 'Calibration용 카메라 인식 표식 (주방 좌표계 기준)'],
        ['Retrofit · Remodeling · New-build', '기존 주방 최소 시공 · 주방 공사 연계 · 신축 설계 반영 설치 유형'],
        ['INSTALL · OPERATE · EXPAND', '설치 매출 · 사용 기간 반복매출 · 기능 확장매출'],
        ['Installed Base', '설치되어 사용 중인 로봇 누적 대수'],
        ['공헌이익', '매출 − 제품 · 설치 · 서비스 원가 − 채널비용 (본사 고정비 차감 전)'],
        ['WTP', 'Willingness to Pay · 고객 지불의사'],
        ['BOM', 'Bill of Materials · 로봇 1대 부품 · 조립 원가'],
        ['SAM · SOM', '채널별 실제 접근 가능한 연간 시장 · 계획 매출 기준 점유'],
        ['인시', '설치 엔지니어 투입 시간 (원가 ÷ 시간당 원가)'],
        ['WP · Gate', 'R&D Work Package · 6개월 단위 계속 · 축소 · 전환 판단 시점'],
    ], [28, 72], size=15, bold_first=True)
    h2('B. 수치 구분 기준')
    table('Number Tag 기준', ['구분', '의미', '사용 예'], [
        ['FACT', '공개 통계 · 규정 · 공개가 (출처 표기)', '총주택 2,018.1만호 · TIPS 8억원 상한'],
        ['DERIVED', 'FACT · ASSUMPTION에서 계산한 값', 'SAM 3,676억원 · 세대당 공헌이익'],
        ['ASSUMPTION', '검증 전 가정 (검증 계획 병기)', '연 주방 교체 30만 · Robot ASP 1,490만원'],
        ['TARGET', '24개월 · 5개년 목표', 'CLEAN ≥ 90% · Y5 560세대'],
        ['CONCEPT', '설계 개념 그림 · 구조 (실제 제품 아님)', '3D 렌더 · Robot Home 치수'],
        ['FUTURE', '장기 방향 (계획 수치 미반영)', 'COOK Skill · Robot Upgrade'],
        ['TBV', '확인 필요 (To Be Verified)', '식기세척기 보급률 · KC 적용 범위'],
    ], [16, 44, 40], size=15, bold_first=True)
    h2('C. 주요 출처')
    used = sorted({int(x) for x in re.findall(r'S(\d+)', json.dumps(BL, ensure_ascii=False))})
    srows = []
    for i in used:
        s = SRC.get(f'S{i}')
        if not s: continue
        urls = re.findall(r'https?://[^\s,]+', s['source'])
        head = re.sub(r'\s*(—\s*)?(보도:|인용 보도:)?\s*https?://\S+', '', s['source']).strip(' ,:—-')
        doms = []
        for u in urls:
            d = re.sub(r'^(www\.|m\.)', '', u.split('/')[2])
            if d not in doms: doms.append(d)
        label = head or s.get('basis', '')
        srows.append([s['id'], s['item'], f"{label} ({' · '.join(doms[:2])})" if doms else label])
    table('본문 인용 출처', ['ID', '항목', '출처'], srows, [7, 43, 50], size=13, note='주: 전체 출처 · URL = docs/07_Market_Data_Sources.md')
    h2('D. 관련 산출 파일')
    table('관련 파일', ['파일', '내용'], [
        ['MH_Robotics_Seed_TIPS_IR_Final.pptx / .pdf', 'IR Deck 본문 18장 + 부록'],
        ['MH_Robotics_Seed_TIPS_IR_Final_Main.pdf', '본문 18장'],
        ['MH_Robotics_Financial_Model.xlsx', '재무모델 (가정 · 세대 경제성 · 시장 · 5개년 · 24개월 자금 · TIPS 편성)'],
        ['docs/00~20', '세부 문서 20종 (사업모델 · 세대 경제성 · TIPS WP · KPI · 특허 · Roadmap · 자금 등)'],
        ['MH_Robotics_Seed_TIPS_Report.docx', '본 보고서'],
    ], [42, 58], size=15, bold_first=True)


# ================================================================ build · pagination
def node_render(entries):
    spec = {'title': 'MH Robotics Seed · TIPS 사업계획 상세 보고서', 'subject': TITLE, 'header': HEADER, 'blocks': []}
    for b in BL:
        spec['blocks'].append({**b, 'entries': entries} if b['t'] == 'toc' else b)
    json.dump(spec, open(SPEC, 'w', encoding='utf-8'), ensure_ascii=False)
    env = dict(os.environ, NODE_PATH=subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip())
    subprocess.run(['node', os.path.join(HERE, 'report_docx.js'), SPEC, OUT], check=True, env=env)


def to_pdf(docx, pdf):
    tmp = tempfile.mkdtemp(prefix='rep_', dir=FIG)
    try:
        conf = os.path.join(tmp, 'fonts.conf')
        open(conf, 'w').write('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig>'
                              '<include ignore_missing="yes">/etc/fonts/fonts.conf</include><dir>' + FONT_DIR + '</dir>'
                              '<alias binding="same"><family>맑은 고딕</family><prefer><family>Noto Sans KR</family></prefer></alias>'
                              '<alias binding="same"><family>Malgun Gothic</family><prefer><family>Noto Sans KR</family></prefer></alias></fontconfig>')
        env = dict(os.environ, FONTCONFIG_FILE=conf)
        subprocess.run(['soffice', f'-env:UserInstallation=file://{tmp}/prof', '--headless', '--convert-to', 'pdf', '--outdir', tmp, docx],
                       check=True, capture_output=True, timeout=600, env=env)
        shutil.move(os.path.join(tmp, os.path.splitext(os.path.basename(docx))[0] + '.pdf'), pdf)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def heading_pages(pdf):
    pages = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True, check=True).stdout.split('\f')
    norm = lambda s: re.sub(r'\s+', '', s)
    lines = [[norm(l) for l in p.splitlines()] for p in pages]
    out, pg = [], 0
    for lv, t in TOC:
        nt = norm(t)
        while pg < len(lines) and nt not in lines[pg]:
            pg += 1
        assert pg < len(lines), f'heading not found in PDF: {t}'
        out.append({'title': t, 'level': lv, 'page': pg + 1})
    return out


def main():
    os.makedirs(FIG, exist_ok=True)
    G = make_figures()
    CH = {'waterfall': ch_waterfall(), 'paths': ch_paths(), 'market': ch_market(), 'installs': ch_installs(), 'rev_layers': ch_rev_layers(),
          'scen': ch_scen(), 'cash': ch_cash(), 'uses': ch_uses(), 'fte': ch_fte(), 'gantt': ch_gantt(), 'bom': ch_bom(),
          'tornado_hh': ch_tornado(M['sens_household'], 'ch_tornado_hh', base_lab=f"기준 {H3['contrib5']:,.0f}만원")}
    build_content(G, CH)
    entries = [{'title': t, 'level': lv, 'page': 0} for lv, t in TOC]
    node_render(entries)
    if '--pdf' in sys.argv or '--toc' in sys.argv:
        tmp_pdf = os.path.join(FIG, 'pass.pdf')
        for it in range(3):
            to_pdf(OUT, tmp_pdf)
            new = heading_pages(tmp_pdf)
            if [e['page'] for e in new] == [e['page'] for e in entries]:
                break
            entries = new
            node_render(entries)
        if '--pdf' in sys.argv:
            shutil.copy(tmp_pdf, PDF)
            print('pdf', PDF)
    print('tables', NT[0], 'figures', NF[0], 'headings', len(TOC))


if __name__ == '__main__':
    main()
