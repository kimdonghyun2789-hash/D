# Main deck v3 (15 slides). One message per slide: a big visual, 1-3 key numbers, short plain-Korean text.
# Number Tags stay but as small low-contrast chips; orange only for Robot Zone / Robot Path / Key Numbers.
# Visuals: three.js concept renders in ARKI/assets/renders (PNG + projected label anchors, built by ARKI/render3d).
import os, json
from PIL import Image
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.dml import MSO_LINE, MSO_PATTERN_TYPE
from common import *
from common import M

RD = os.path.join(ROOT, 'assets', 'renders')
GREY = '8C9198'
EDGE = 'C9CDD2'
FOOT_LEFT = 'ARKI Robotics  ·  TIPS 창업기업 IR  ·  Draft v4'

def N():
    return dict(hh=M['household']['purchase_direct_Y3'], hh5=M['household']['purchase_direct_Y5'], mk=M['market']['B'],
                v=M['value'], F=M['funds'])

# ---------------------------------------------------------------- main-deck idioms
MT_LABEL = {'TBV': 'TO BE VALIDATED', 'FUTURE': 'FUTURE CONCEPT'}

def mt(s, x, y, kind, size=6.5, h=0.17, label=None, fill=None):
    """Low-priority Number Tag: outlined, grey text, no fill (fill only when placed over an image)."""
    lab = label or MT_LABEL.get(kind, kind)
    w = kit.text_w(lab, size, True) + 0.12
    rect(s, x, y, w, h, fill=fill, line=EDGE, lw=0.5)
    kit.NOLOG['on'] = True
    text(s, x, y, w, h, lab, size=size, bold=True, color=GREY, align='c', anchor='m', check=False)
    kit.NOLOG['on'] = False
    kit._log(f'[{lab}]')
    return w

def mts(s, x, y, kinds, gap=0.05, **kw):
    for k in kinds:
        x += mt(s, x, y, k, **kw) + gap
    return x

def mhead(s, kicker, title, sub=None, size=26):
    import re
    kicker = re.sub(r'^\s*\d+\s+', '', kicker or '')
    text(s, MX, 0.46, 9.5, 0.24, kicker, size=10, bold=True, color=GREY, label='kicker')
    th = kit.text_h(title, size, CW, line=0.95, bold=True)
    text(s, MX, 0.74, CW, th + 0.04, title, size=size, bold=True, line=0.95, label='title:' + title[:12])
    y = 0.74 + th + 0.1
    if sub:
        sh = kit.text_h(sub, 12.5, CW)
        text(s, MX, y, CW, sh + 0.02, sub, size=12.5, color=T['text2'], label='sub:' + sub[:12])
        y += sh + 0.04
    return y + 0.12

PAGE = {'n': 0}

def pg(prs):
    """Page number of the slide about to be created (main deck order = MAIN)."""
    PAGE['n'] = len(prs.slides) + 1
    return PAGE['n']

def mfoot(s, no=None, note=None):
    footer(s, PAGE['n'], left=FOOT_LEFT, note=note)

def seg(s, x1, y1, x2, y2, color=None, lw=0.75, dash=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = RGBColor.from_string(color or T['text2']); c.line.width = Pt(lw)
    kit._nostyle(c)
    if dash: c.line.dash_style = MSO_LINE.DASH
    return c

def render(s, name, x, y, w, h, focus=(0.5, 0.5), zoom=1.0, bg=(255, 255, 255), border=False, src=None):
    """Cover-fit a render into the box (same crop as kit.image). Returns at(key | (px, py)) -> slide inches."""
    path = src or os.path.join(RD, name + '.png')
    iw, ih = Image.open(path).size; ar = w / h
    cw, ch = (int(ih * ar), ih) if iw / ih > ar else (iw, int(iw / ar))
    cw, ch = int(cw / zoom), int(ch / zoom)
    cx = min(max(int(focus[0] * iw - cw / 2), 0), iw - cw); cy = min(max(int(focus[1] * ih - ch / 2), 0), ih - ch)
    kit.image(s, path, x, y, w, h, focus=focus, bg=bg, zoom=zoom)
    if border: rect(s, x, y, w, h, line=T['line'], lw=0.75)
    A = json.load(open(os.path.join(RD, name + '.json'), encoding='utf-8')).get('anchors', {})
    def at(key, dx=0.0, dy=0.0):
        px, py = A[key] if isinstance(key, str) else key
        return x + (px - cx) / cw * w + dx, y + (py - cy) / ch * h + dy
    return at

def faded(name, left=0.0, bottom=0.0, bg=(255, 255, 255)):
    """Render composited on bg with a soft fade to bg along the left / bottom edges (for full-bleed placement)."""
    im = Image.open(os.path.join(RD, name + '.png')).convert('RGBA')
    base = Image.new('RGBA', im.size, bg + (255,)); base.alpha_composite(im)
    iw, ih = im.size
    mask = Image.new('L', im.size, 255); px = mask.load()
    lw_, bh = int(iw * left), int(ih * bottom)
    for xx in range(lw_):
        a = int(255 * (xx / lw_) ** 1.6)
        for yy in range(ih): px[xx, yy] = min(px[xx, yy], a)
    for yy in range(ih - bh, ih):
        a = int(255 * ((ih - yy) / bh) ** 1.6)
        for xx in range(iw): px[xx, yy] = min(px[xx, yy], a)
    out = Image.new('RGBA', im.size, bg + (255,)); out.paste(base, (0, 0), mask)
    os.makedirs(kit.IMG_CACHE, exist_ok=True)
    p = os.path.join(kit.IMG_CACHE, f'{name}_fade.png'); out.convert('RGB').save(p)
    return p

def chipl(s, x, y, txt, size=9, side='r', fill='FFFFFF', color=None, line=None, bold=True):
    """Label chip vertically centred on y; side='r' extends right of x, 'l' left of x, 'c' centred."""
    w = kit.text_w(txt, size, bold) + 0.18; h = size * kit.LH / 72 + 0.08
    x0 = {'r': x, 'l': x - w, 'c': x - w / 2}[side]
    rect(s, x0, y - h / 2, w, h, fill=fill, line=line or EDGE, lw=0.5)
    text(s, x0, y - h / 2, w, h, txt, size=size, bold=bold, color=color or T['text'], align='c', anchor='m', check=False)
    return x0, w, h

def callout(s, at, key, txt, dx, dy, size=9, color=None, side=None):
    ax, ay = at(key); lx, ly = ax + dx, ay + dy
    seg(s, ax, ay, lx, ly, color='5C6169', lw=0.6)
    dot(s, ax, ay, 0.07, fill=T['text'])
    chipl(s, lx, ly, txt, size=size, side=side or ('r' if dx >= 0 else 'l'), color=color)

def marker(s, cx, cy, n, d=0.22, fill=None, color='FFFFFF', size=8.5, ring=True):
    if ring: rect(s, cx - d / 2 - 0.025, cy - d / 2 - 0.025, d + 0.05, d + 0.05, fill='FFFFFF', shape=MSO_SHAPE.OVAL)
    rect(s, cx - d / 2, cy - d / 2, d, d, fill=fill or T['text'], shape=MSO_SHAPE.OVAL)
    text(s, cx - d / 2, cy - d / 2, d, d, str(n), size=size, bold=True, color=color, align='c', anchor='m', check=False)

def knum(s, x, y, w, value, label, tag=None, vsize=30, color=None, lsize=10.5, tag_y=None):
    vh = vsize * kit.LH / 72
    text(s, x, y, w, vh, value, size=vsize, bold=True, color=color or T['accent'], label='knum ' + value)
    lh = kit.text_h(label, lsize, w)
    text(s, x, y + vh - 0.02, w, lh + 0.02, label, size=lsize, color=T['text2'], label='knuml ' + label[:10])
    yy = tag_y if tag_y is not None else y + vh + lh + 0.02
    if tag:
        mts(s, x, yy, [tag] if isinstance(tag, str) else tag); yy += 0.2
    return yy

def hatch(s, x, y, w, h):
    sh = rect(s, x, y, w, h, line='3A3F46', lw=0.75)
    sh.fill.patterned(); sh.fill.pattern = MSO_PATTERN_TYPE.WIDE_UPWARD_DIAGONAL
    sh.fill.fore_color.rgb = RGBColor.from_string('3A3F46'); sh.fill.back_color.rgb = RGBColor.from_string('FFFFFF')
    return sh

def swatch(s, x, y, kind, w=0.34, h=0.2):
    if kind == 'robot': alpha(rect(s, x, y, w, h, fill=T['accent'], line=T['accent'], lw=1.0), 40)
    elif kind == 'reach': alpha(rect(s, x, y, w, h, fill=T['accent'], line=T['accent'], lw=0.5), 8)
    elif kind == 'human': alpha(rect(s, x, y, w, h, fill='7F8A96'), 28); dashed_rect(s, x, y, w, h, color='5C6670', lw=1.0)
    elif kind == 'nogo': hatch(s, x, y, w, h)
    elif kind == 'path': seg(s, x, y + h / 2, x + w, y + h / 2, color=T['accent'], lw=2.0, dash=True)


import viz
from viz import module_strip, level_marks

# ---------------------------------------------------------------- copy (plain-Korean IR text)
# Defaults are written here; ARKI/source/_copy_v3.json (reviewed copy) overrides kicker/title/sub/note/body/numbers per slide.
COPY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_copy_v3.json')
try:
    _CP = {d['id']: d for d in json.load(open(COPY_PATH, encoding='utf-8'))['slides']}
except Exception:
    _CP = {}

def cp(sid, D):
    """Merge reviewed copy over the defaults; keys missing / empty in the reviewed copy fall back to D."""
    out = dict(D)
    for k, v in _CP.get(sid, {}).items():
        if k in out and v not in (None, '', []) and (k not in D.get('_lock', ())):
            out[k] = v
    return out

def nums(s, x, y, w, items, vsize=26, lsize=10, gap=0.28, tag_y=None):
    """Key numbers stacked vertically: items = [(value, label, tag)]."""
    yy = y
    for v, lab, tg in items:
        yy = knum(s, x, yy, w, v, lab, tg, vsize=vsize, lsize=lsize) + gap
    return yy

def nums_row(s, x, y, w, items, vsize=24, lsize=9.5, gap=0.25):
    n = len(items); cw = (w - gap * (n - 1)) / n
    ty = y + vsize * kit.LH / 72 + max(kit.text_h(it[1], lsize, cw) for it in items) + 0.02
    for i, (v, lab, tg) in enumerate(items):
        knum(s, x + i * (cw + gap), y, cw, v, lab, tg, vsize=vsize, lsize=lsize, tag_y=ty)
    return ty + 0.2

def band(s, y, runs, h=0.46, size=11):
    rect(s, MX, y, CW, h, fill=T['soft'])
    text(s, MX + 0.2, y, CW - 0.4, h, [runs], size=size, anchor='m')

def caption(s, x, y, w, txt, size=10.5, bold=True, color=None):
    text(s, x, y, w, 0.3, txt, size=size, bold=bold, color=color or T['text'], check=False)


# ================================================================= 01 cover
def m01(prs):
    c = cp('m01', dict(
        kicker='TIPS 창업기업 IR  ·  2026.10  ·  DRAFT v4',
        title='설거지 정리를 맡는\n로봇 주방',
        sub='로봇이 일할 자리를 주방 설계 단계에서 만듭니다',
        body=['첫 기능: 식사 후 식기 정리 (식기세척기 넣기 · 꺼내기 · 수납)', '첫 시장: 구축 아파트 주방 리모델링',
              'TIPS 과제 (안): 레일 로봇 기반 식기 정리 자동화 · 24개월'],
        note=('ARKI Robotics는 식사 후 설거지 정리를 맡는 로봇 주방을 만듭니다. 로봇을 사서 기존 주방에 두는 방식이 아니라, 레일과 보관함, 식기세척기와 서랍을 로봇이 쓰기 좋게 처음부터 같이 설계합니다. '
              '첫 기능은 식사 후 식기를 식기세척기에 넣고, 세척이 끝나면 꺼내서 서랍에 정리하는 일입니다. 첫 시장은 주방을 새로 시공하는 구축 아파트 리모델링입니다. '
              '현재는 Concept 단계로 시제품, 고객, 계약, LOI, 파트너, 매출, 투자유치가 없습니다. 오늘 자료는 TIPS 24개월 동안 무엇을 만들고 어떻게 검증할지에 대한 계획입니다.')))
    s = start(prs, 'm01', pg(prs), c['title'].replace('\n', ' '), note=c['note'],
              visual='우측 대형 3D: 레일에 매달린 로봇이 싱크 옆에서 접시를 들고 식기세척기로 이동 (주황 점선 = 로봇 경로), 왼쪽 끝 로봇 보관함. 좌측 회사명 · 한 줄 소개.',
              chart='3D 콘셉트 렌더 1개 (CONCEPT)')
    x, y, w, h = 13.333 - 8.4, 0.5, 8.4, 7.0
    at = render(s, 'v2_cover', x, y, w, h, src=faded('v2_cover', left=0.16), focus=(0.5, 0.5))
    callout(s, at, 'garage', '로봇 보관함', -0.55, -0.5)
    callout(s, at, 'rail', '레일 (상부장 아래)', -0.2, -0.75, side='l')
    callout(s, at, 'sink', '싱크', 0.05, 0.75)
    callout(s, at, 'dw', '식기세척기', 0.75, 0.15)
    callout(s, at, 'drawer', '로봇용 서랍', 0.6, 0.6)
    mt(s, W - MX - 1.15, 7.12, 'CONCEPT', label='CONCEPT RENDERING')
    lx, lw = MX, 4.3
    text(s, lx, 0.95, lw + 1, 0.26, c['kicker'], size=9.5, bold=True, color=GREY)
    text(s, lx, 1.42, lw, 0.82, 'ARKI Robotics', size=40, bold=True)
    text(s, lx, 2.28, lw, 0.3, '아키로보틱스 (가칭)', size=12, color=T['text2'])
    th = kit.text_h(c['title'], 30, lw, line=1.0, bold=True)
    text(s, lx, 3.0, lw, th + 0.05, c['title'], size=30, bold=True, line=1.0)
    yy = 3.0 + th + 0.22
    hline(s, lx, yy, 3.6, color=T['line'])
    sh = kit.text_h(c['sub'], 13, lw, bold=True)
    text(s, lx, yy + 0.18, lw, sh + 0.04, c['sub'], size=13, bold=True)
    bh = kit.text_h(c['body'], 11.5, lw, space_after=3)
    text(s, lx, yy + 0.3 + sh, lw, bh + 0.05, c['body'], size=11.5, color=T['text2'], space_after=3)
    text(s, lx, 6.5, lw, 0.5, ['Concept 단계 · 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 · 투자유치 없음 (FACT)',
                               '숫자는 FACT · ASSUMPTION · TARGET 등으로 구분 표기'], size=8.5, color=GREY)


# ================================================================= 02 problem
def m02(prs):
    v = M['value']
    c = cp('m02', dict(
        kicker='IR ① 문제 정의',
        title='식사 후 정리는 아직 사람이 합니다',
        sub='식기세척기는 씻기만 합니다. 옮기고, 넣고, 꺼내서 제자리에 두는 일은 사람 몫입니다.',
        body=['정리 시간은 아직 가정입니다. 과제 첫 3개월에 30세대 시간 기록으로 실제 시간과 빈도를 잽니다.'],
        numbers=[{'value': '약 40분', 'label': '하루 식사 후 정리 시간', 'tag': 'ASSUMPTION'},
                 {'value': f"월 약 {v['hours']:.0f}시간", 'label': '40분 × 30일', 'tag': 'DERIVED'},
                 {'value': '1.5만원', 'label': '가사서비스 시간당 요금', 'tag': 'FACT'}],
        note=('식기세척기와 인덕션은 기기 안의 일을 자동으로 합니다. 하지만 식사 후 식기를 싱크로 옮기고, 식기세척기에 넣고, 끝나면 꺼내서 수납장에 넣는 일은 여전히 사람이 합니다. '
              'ARKI가 맡는 범위는 조리대에 놓인 식기를 집는 일부터 서랍에 정리하는 일까지입니다. 식탁에서 조리대로 옮기는 일은 첫 제품에서도 사람이 합니다. '
              '하루 40분은 가정입니다. 과제 첫 3개월에 30세대의 시간 기록으로 확인합니다.')))
    s = start(prs, 'm02', pg(prs), c['title'], note=c['note'],
              visual='흐름도: 식탁 → 싱크대 → 식기세척기(기기가 하는 일, 검정) → 수납장. 사이의 옮기기 · 넣기 · 꺼내서 수납 = 사람. 주황 괄호 = ARKI가 맡는 범위.',
              chart='흐름도 + 핵심 숫자 3개')
    mhead(s, c['kicker'], c['title'], c['sub'])
    nodes = [('식탁', '식사 후 식기'), ('싱크대', '잔반 정리 · 헹굼'), ('식기세척기', '세척 · 건조'), ('수납장', '보관')]
    nw, nh = 2.05, 1.25; gap = (CW - 4 * nw) / 3; ny = 2.55
    xs = [MX + i * (nw + gap) for i in range(4)]
    for i, (a, b) in enumerate(nodes):
        dark = i == 2
        rect(s, xs[i], ny, nw, nh, fill=T['text'] if dark else T['soft'])
        text(s, xs[i], ny + 0.25, nw, 0.4, a, size=16, bold=True, color='FFFFFF' if dark else T['text'], align='c')
        text(s, xs[i], ny + 0.7, nw, 0.3, b, size=11, color='C9CDD2' if dark else T['text2'], align='c')
    chipl(s, xs[2] + nw / 2, ny - 0.02, '기기가 하는 일', size=8.5, side='c', fill=T['text'], color='FFFFFF', line=T['text'])
    for i, t in enumerate(['옮기기', '넣기', '꺼내서 수납']):
        x1 = xs[i] + nw + 0.08; x2 = xs[i + 1] - 0.08; cy = ny + nh / 2
        arrow(s, x1, cy, x2, cy, color=T['text2'], lw=2.25)
        text(s, (x1 + x2) / 2 - 1.0, ny - 0.42, 2.0, 0.3, t, size=11.5, bold=True, align='c')
        chipl(s, (x1 + x2) / 2, cy + 0.3, '사람', size=8.5, side='c', color=T['text2'])
    by = ny + nh + 0.3
    bx0 = xs[1] + nw * 0.35; bx1 = xs[3] + nw * 0.5
    seg(s, bx0, by, bx1, by, color=T['accent'], lw=2.0)
    seg(s, bx0, by - 0.12, bx0, by, color=T['accent'], lw=2.0); seg(s, bx1, by - 0.12, bx1, by, color=T['accent'], lw=2.0)
    text(s, bx0, by + 0.08, bx1 - bx0, 0.3, 'ARKI가 맡는 범위: 집기 → 넣기 → 꺼내기 → 서랍 정리', size=11.5, bold=True, color=T['accent'], align='c')
    gx0 = xs[0] + nw * 0.5; gx1 = xs[1] + nw * 0.3
    seg(s, gx0, by, gx1, by, color=GREY, lw=1.25, dash=True)
    text(s, gx0 - 0.4, by + 0.08, gx1 - gx0 + 0.8, 0.3, '식탁 → 조리대는 사람', size=9.5, color=GREY, align='c')
    ky = 5.25
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:3]]
    nums_row(s, MX, ky, 7.4, items, vsize=24)
    rx = MX + 7.8; rw = W - MX - rx
    rect(s, rx, ky + 0.02, rw, 1.1, fill=T['soft'])
    text(s, rx + 0.22, ky + 0.14, rw - 0.4, 0.86, c['body'][:2], size=10.5, color=T['text2'], line=1.05, space_after=3)
    mfoot(s, note='시간당 1.5만원: 가사서비스 플랫폼 공개 요금 (4시간 59,900~64,900원) → 부록 F2')


# ================================================================= 03 solution
def m03(prs):
    c = cp('m03', dict(
        kicker='IR ① 솔루션',
        title='로봇을 들이는 대신, 로봇 자리를 주방에 만듭니다',
        sub='레일 · 보관함 · 식기세척기 · 서랍을 로봇이 쓰기 좋은 위치와 높이로 함께 설계합니다',
        body=['집마다 다른 위치 · 높이 · 동선을 로봇이 현장에서 알아내는 대신, 설계 단계에서 정해 둡니다.', '그만큼 집마다 새로 풀 문제가 줄어듭니다 (실물 미검증). 식기 인식 · 집기는 따로 검증합니다.'],
        note=('왼쪽은 기존 주방에 이동형 로봇을 들여놓은 경우입니다. 로봇이 통로를 막고, 식기세척기는 무릎 높이에, 수납은 손이 닿지 않는 위치에 있으며, 사람과 동선이 겹칩니다. '
              '이런 조건을 집마다 로봇이 현장에서 풀어야 합니다. 오른쪽은 ARKI 방식입니다. 로봇은 상부장 아래 레일에 매달려 바닥을 쓰지 않고, 식기세척기와 서랍은 로봇이 위에서 넣을 수 있게 배치합니다. '
              '로봇 작업 구역과 사람 구역을 나누고, 인덕션 같은 조리기구 구역은 로봇이 들어가지 않습니다.')))
    s = start(prs, 'm03', pg(prs), c['title'], note=c['note'],
              visual='3D 비교 2장. 왼쪽: 일반 주방 + 이동형 로봇 (통로 · 무릎 높이 식세기 · 동선 겹침). 오른쪽: ARKI 주방 (레일 · 보관함 · 로봇 구역(주황) · 사람 구역 · 조리기구 금지 구역).',
              chart='비교 렌더 2장')
    mhead(s, c['kicker'], c['title'], c['sub'])
    pw = 5.72; ph = pw / (1500 / 1075); py = 2.25
    for i, (name, head_) in enumerate([('before', '기존 주방에 이동형 로봇을 들이는 경우 (개념도)'), ('v2_after', 'ARKI 주방 (개념도)')]):
        px = MX + i * (pw + CW - 2 * pw)
        text(s, px, py - 0.38, pw, 0.3, head_, size=12.5, bold=True, color=GREY if i == 0 else T['text'])
        at = render(s, name, px, py, pw, ph, border=True)
        if i == 0:
            callout(s, at, 'cart', '통로에 선 이동형 로봇', -0.3, -0.75, side='l')
            callout(s, at, 'dw', '무릎 높이 식기세척기', -0.15, 0.6, side='l')
            callout(s, at, 'human', '사람 동선과 겹칠 수 있음', 0.42, 0.62)
        else:
            callout(s, at, 'rail', '상부장 아래 레일 · 바닥 안 씀', -0.35, -0.45, side='l')
            callout(s, at, 'garage', '로봇 보관함', 0.1, -0.62, side='l')
            callout(s, at, 'robotZone', '로봇 작업 구역', 0.32, 0.72, color=T['accent'])
            callout(s, at, 'nogo', '조리기구 = 로봇 금지', 0.25, -0.62)
            callout(s, at, 'humanZone', '사람 구역', -0.2, 0.6, side='l')
    by = py + ph + 0.22
    text(s, MX, by, CW, 0.6, c['body'][:2], size=12, line=1.05)
    mfoot(s)


# ================================================================= 04 how it works
def m04(prs):
    c = cp('m04', dict(
        kicker='IR ① 솔루션 · 제품',
        title='식사 후 정리를 다섯 단계로 끝냅니다',
        sub='사람은 식기를 조리대 한쪽에 두기만 합니다. 조리 · 칼 · 불 쓰는 일은 하지 않습니다.',
        labels=['인식', '집기', '넣기', '꺼내기', '서랍 정리'],
        body=['카메라로 식기 종류 · 위치 확인', '식기 모양에 맞게 집기', '식기세척기 랙에 세워 넣기', '세척 끝난 식기 꺼내기', '로봇용 서랍에 정리'],
        numbers=[{'value': '70%', 'label': '목업 정리 성공률 (M9 점검)', 'tag': 'TARGET'},
                 {'value': '90%', 'label': '가정 실증 정리 성공률 (최종)', 'tag': 'TARGET'}],
        note=('첫 제품의 일은 하나입니다. 조리대 한쪽에 놓인 식기를 인식하고, 모양에 맞게 집어서, 식기세척기 랙에 넣고, 세척이 끝나면 꺼내서 로봇용 서랍에 정리합니다. '
              '조리, 칼, 불을 쓰는 일은 범위에서 뺐습니다. 범위를 좁혀야 가정에서 믿을 수 있는 수준을 만들 수 있기 때문입니다. '
              '성공률은 사람 개입 없이 다섯 단계를 끝낸 비율로 재며, 9개월에 목업에서 70%, 과제 끝에 가정 실증에서 90%가 목표입니다.'),
        _lock=('labels', 'body')))
    s = start(prs, 'm04', pg(prs), c['title'], note=c['note'],
              visual='3D 장면 5장 (인식 → 집기 → 넣기 → 꺼내기 → 서랍 정리), 주황 번호와 점선. 하단 판단 기준 숫자 2개.',
              chart='5단계 3D 시퀀스')
    mhead(s, c['kicker'], c['title'], c['sub'])
    steps = ['v2_seq_1_detect', 'v2_seq_2_pick', 'v2_seq_3_load', 'v2_seq_4_unload', 'v2_seq_5_store']
    fw = (CW - 4 * 0.15) / 5; fh = fw / (1100 / 840); fy = 2.35; ny = 2.02
    seg(s, MX + fw / 2, ny, MX + 4 * (fw + 0.15) + fw / 2, ny, color=T['accent'], lw=2.0, dash=True)
    for i, img in enumerate(steps):
        fx = MX + i * (fw + 0.15)
        render(s, img, fx, fy, fw, fh, border=True, focus=(0.5, 0.5))
        marker(s, fx + fw / 2, ny, i + 1, d=0.34, fill=T['accent'], size=12)
        text(s, fx, fy + fh + 0.1, fw, 0.32, c['labels'][i], size=14, bold=True)
        text(s, fx, fy + fh + 0.44, fw, 0.5, c['body'][i], size=10.5, color=T['text2'], line=1.0)
    mt(s, W - MX - 1.2, fy + fh - 0.24, 'CONCEPT', label='CONCEPT RENDERING', fill='FFFFFF')
    by = 5.45
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:2]]
    nums_row(s, MX, by, 5.2, items, vsize=24)
    rx = MX + 5.6; rw = W - MX - rx
    rect(s, rx, by + 0.02, rw, 0.95, fill=T['soft'])
    text(s, rx + 0.22, by + 0.1, rw - 0.4, 0.8, [[('범위 밖  ', {'bold': True}), ('조리 · 칼 · 불 쓰는 작업 · 식탁에서 조리대로 옮기기 (사람)', {})],
                                                 [('다음 단계  ', {'bold': True, 'color': GREY}), ('재료 옮기기 · 조리 보조는 이후 검토 (FUTURE)', {'color': T['text2']})]],
         size=10.5, line=1.05, space_after=4)
    mfoot(s)


# ================================================================= 05 stow / deploy / low reach
def m05(prs):
    SP = json.load(open(os.path.join(RD, 'v2_stow_3_deploy.json'), encoding='utf-8'))['ik'].get('sweep', {})
    out_cm = max(0, SP.get('zmax', 88) - 62)
    c = cp('m05', dict(
        kicker='IR ① 솔루션 · 보관 · 전개 · 낮은 곳',
        title='평소엔 보관함에 숨고, 낮은 곳은 랙을 당겨 위에서 넣습니다',
        sub='로봇은 조리대 끝 폭 45cm 보관함에 접혀 있다가, 여닫이 문이 열리면 레일로 나옵니다',
        labels=['① 평소: 문 닫힘', '② 문 열면: 접힌 로봇', '③ 펼침: 레일 아래로', '④ 레일 따라 이동'],
        body=[f'펼칠 때 팔이 조리대 앞으로 최대 {out_cm:.0f}cm 나옴 → 사람이 가까우면 멈춤',
              '식기세척기는 일반 빌트인 그대로, 하단 랙을 44cm 당겨 위에서 넣음'],
        numbers=[{'value': '45 × 62cm', 'label': '보관함 폭 × 깊이 (조리대 위)', 'tag': 'CONCEPT'},
                 {'value': '약 37cm', 'label': '집게가 내려가는 최저 높이', 'tag': 'CONCEPT'},
                 {'value': '0cm', 'label': '3D 충돌검사 관통 (단순 모델, 실물 미검증)', 'tag': 'CONCEPT'}],
        note=('로봇은 쓰지 않을 때 조리대 끝의 폭 45센티미터 보관함에 위로 접혀 들어가 있습니다. 보관함은 일반 수납장처럼 여닫이 문이 달려 있고, 오른쪽 아래는 레일이 지나가는 통로입니다. '
              f'작업을 시작하면 문이 열리고, 팔이 문 앞쪽으로 펴지면서 레일 아래로 내려온 뒤 레일 방향으로 접혀 이동합니다. 이때 팔이 조리대 앞으로 최대 {out_cm:.0f}센티미터 나오므로 사람이 가까이 있으면 멈춰야 합니다. '
              '낮은 곳은 식기세척기 하단 랙을 앞으로 당겨 랙이 조리대 앞에 오게 한 뒤 위에서 수직으로 넣습니다. 로봇이 가구 옆판을 뚫고 들어가지 않습니다. '
              '모든 자세와 이동 경로는 3D 모델에서 충돌검사를 했고 관통은 0센티미터입니다. 실물 검증은 TIPS 1차년도의 실물 크기 목업에서 합니다.'),
        _lock=('labels',)))
    s = start(prs, 'm05', pg(prs), c['title'], note=c['note'],
              visual='상단 3D 4장: 문 닫힘 → 문 열고 접힌 로봇 → 펼침(주황 점선 = 집게 끝 경로) → 레일 이동(주황 화살표). 하단 왼쪽: 식기세척기 위치 단면 (높이 표시). 하단 오른쪽: 핵심 숫자 3개.',
              chart='3D 4장 + 단면 1장')
    mhead(s, c['kicker'], c['title'], c['sub'])
    names = ['v2_stow_1_closed', 'v2_stow_2_open', 'v2_stow_3_deploy', 'v2_stow_4_exit']
    fw = (CW - 3 * 0.14) / 4; fh = fw * 0.58; fy = 1.98
    for i, nm in enumerate(names):
        fx = MX + i * (fw + 0.14)
        render(s, nm, fx, fy, fw, fh, border=True, focus=(0.45, 0.42), zoom=1.12)
        caption(s, fx, fy + fh + 0.06, fw, c['labels'][i], size=10.5)
    # section through the dishwasher with height marks
    sy = fy + fh + 0.44; sh_ = H - 0.5 - sy; sw_ = sh_ * (1000 / 1150)
    sx = MX + 1.45
    at = render(s, 'v2_section_low', sx, sy, sw_, sh_, bg=(255, 255, 255))
    pts = []
    for key, lab, hi in [('y225', '225  상부장 위', False), ('y139', '139  레일 (상부장 145 아래)', True),
                         ('y88', '88  조리대', False), ('y37', '37  집게 최저', True), ('y0', '0  바닥', False)]:
        px, py = at(key); pts.append((px, py, lab, hi))
    level_marks(s, pts, MX - 0.3, w_text=1.55, size=9)
    text(s, MX - 0.3, sy - 0.02, 1.7, 0.24, '높이 (cm)', size=8.5, bold=True, color=GREY, align='r', check=False)
    ax, ay = at('zRack')
    chipl(s, ax - 0.1, ay - 0.42, '랙 44cm 당김', size=8.5, side='c')
    # right: numbers + notes
    rx = sx + sw_ + 0.45; rw = W - MX - rx
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:3]]
    nums_row(s, rx, sy + 0.05, rw, items, vsize=22, lsize=9.5)
    text(s, rx, sy + 1.3, rw, 1.2, c['body'][:3], size=10.5, color=T['text2'], bullet='–', space_after=4, line=1.05)
    mfoot(s, note='3D 모델 기준 (실물 미검증) · 로봇 링크 = 캡슐, 가구 = 상자로 충돌검사 · 경로는 관절 보간 0.015rad · 레일 이동 1cm 간격')


# ================================================================= 06 real plan
def m06(prs):
    c = cp('m06', dict(
        kicker='IR ① 솔루션 · 실제 평면 적용',
        title='받은 평면 그대로 3D로 옮겨, 주방 한 벽에 넣었습니다',
        sub='구축 2Bay A (코어 포함 12,390 × 11,670mm) · 주방 윗벽 3,255mm에 ARKI 한 줄 3,150mm',
        body=['인덕션은 옆 벽 아래쪽으로 옮겨 로봇 구역과 분리 · 싱크 중심 약 21cm 이동',
              '벽 3,255mm에 한 줄 3,150mm (내려놓는 곳 70cm) → 여유 10.5cm, 현장 실측 필요',
              '보관함 문은 옆 벽 때문에 90°까지만 열림 → 이 조건으로 작업 · 보관 · 이동 경로 충돌검사 다시 수행'],
        numbers=[{'value': '3,150mm', 'label': 'ARKI 한 줄 (벽 길이 3,255mm)', 'tag': 'CONCEPT'},
                 {'value': '0cm', 'label': '작업 · 보관 · 이동 경로 관통 (3D 단순 모델)', 'tag': 'CONCEPT'}],
        note=('받은 평면 중 구축 2Bay 평면 하나를 치수 그대로 3D로 만들었습니다. 오른쪽 그림이 그 주방입니다. '
              '주방 윗벽은 왼쪽 벽에서 침실 문까지 3,255밀리미터이고, 여기에 보관함, 내려놓는 곳, 싱크, 서랍, 식기세척기로 된 ARKI 한 줄 3,150밀리미터를 넣었습니다. '
              '원래 왼쪽 벽에 있던 조리대는 아래쪽으로 줄이고 인덕션을 옮겨 로봇 구역과 분리했습니다. 싱크 중심은 약 21센티미터 옮겨집니다. '
              '보관함 문은 옆 벽 때문에 90도까지만 열리는데, 이 조건으로 작업 자세와 보관, 이동 경로를 다시 충돌검사했고 관통은 0센티미터입니다. '
              '같은 방법으로 평면 30개를 분석하는 일은 TIPS 1차년도 과제에 넣었습니다.')))
    s = start(prs, 'm06', pg(prs), c['title'], note=c['note'],
              visual='왼쪽: 받은 평면을 치수 그대로 옮긴 평면도 (ARKI 구역 주황) + 원래 주방 작은 그림. 오른쪽: 같은 평면의 주방 3D (보관함 · 레일 · 싱크 · 서랍 · 식기세척기 · 옮긴 인덕션).',
              chart='평면도 + 주방 3D')
    mhead(s, c['kicker'], c['title'], c['sub'])
    py = 1.98; ph = 3.85; pw = ph * (1400 / 1320)
    at = render(s, 'plan_old2a_top_arki', MX, py, pw, ph, bg=(255, 255, 255))
    for key, lab in [('room:주방/식당', '주방 · 식당'), ('room:거실', '거실'), ('room:침실1(안방)', '침실1'), ('room:침실2', '침실2'), ('room:침실3', '침실3')]:
        try:
            x_, y_ = at(key); text(s, x_ - 0.5, y_ - 0.11, 1.0, 0.22, lab, size=8.5, bold=True, color=T['text2'], align='c', check=False)
        except KeyError:
            pass
    gx, gy = at('drop')
    chipl(s, gx + 0.55, gy - 0.36, 'ARKI 한 줄', size=8.5, side='c', color=T['accent'], line=T['accent'])
    text(s, MX, py + ph + 0.04, pw, 0.24, '받은 평면 (치수 그대로) + ARKI 배치', size=9, color=GREY, check=False)
    rw = 5.6; rh = rw / (1600 / 1100); rx = W - MX - rw
    at2 = render(s, 'plan_old2a_kitchen', rx, py, rw, rh, border=True)
    callout(s, at2, 'garage', '로봇 보관함', -0.35, -0.35, side='l')
    callout(s, at2, 'rail', '레일', 0.25, -0.5)
    callout(s, at2, 'sink', '싱크', 0.15, -0.55)
    callout(s, at2, 'dw', '식기세척기', 0.35, 0.3)
    callout(s, at2, 'cooktop', '인덕션 (옆 벽으로 이동)', 0.1, 0.5)
    mt(s, rx + rw - 1.2, py + rh - 0.24, 'CONCEPT', label='CONCEPT RENDERING', fill='FFFFFF')
    mx0 = MX + pw + 0.25; mw = rx - 0.25 - mx0
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:2]]
    nums(s, mx0, py + 0.05, mw, items, vsize=20, lsize=9, gap=0.2)
    text(s, MX, py + rh + 0.3, CW, 0.75, c['body'][:3], size=10, color=T['text2'], bullet='–', space_after=2, line=1.0)
    mfoot(s, note='평면: 받은 도면을 치수선 기준으로 디지털화 (특정 단지명 표기 안 함) · 받은 평면 5종 분류는 부록 B5')


# ================================================================= 07 standard module
def m07(prs):
    smr = inp('smr'); kc = B('kit_unit_cost')
    c = cp('m07', dict(
        kicker='IR ① 솔루션 · 표준화',
        title='평면이 달라도 같은 한 줄 모듈을 쓰는 것이 목표입니다',
        sub='순서와 치수는 고정하고 폭 · 문 열림각 · 조리기구 위치만 맞춥니다. 받은 5종 중 3종은 싱크 벽이 2.6~2.8m라 짧은 벽용 한 줄도 필요합니다.',
        table=[['바뀌는 것', '범위', '예: 구축 2Bay A'], ['한 줄 길이', '표준 315~325 · 단축 약 255cm (검토)', '표준 315cm'], ['내려놓는 곳 폭', '70 ~ 80cm', '70cm'],
               ['보관함 문 열림각', '90 ~ 105°', '90° (옆 벽)'], ['조리기구 위치', '옆 벽 · 아일랜드', '옆 벽 아래쪽'], ['마감재 · 상부장', '현장 선택', '기존 톤']],
        numbers=[{'value': '30개 → 3~5개', 'label': '평면 분석 → 주방 표준안', 'tag': 'TARGET'},
                 {'value': f"{kc[0]:.0f} → {kc[4]:.0f}만원", 'label': f"세대당 주방 모듈 원가 (표준 모듈 사용률 {pct(smr[0])} → {pct(smr[4])})", 'tag': 'DERIVED'},
                 {'value': '60%', 'label': 'M18 표준 모듈 사용률 기준', 'tag': 'TARGET'}],
        note=('집마다 주방이 다르면 결국 인테리어 회사가 아니냐는 질문에 대한 답입니다. ARKI는 보관함, 내려놓는 곳, 싱크, 서랍, 식기세척기의 순서와 치수를 고정한 한 줄 모듈을 씁니다. '
              '평면마다 바뀌는 것은 내려놓는 곳의 폭, 보관함 문이 열리는 각도, 조리기구 위치, 마감재 정도입니다. 앞 장의 구축 2Bay 평면도 이 범위 안에서 맞췄습니다. '
              '다만 받은 평면 5종 중 3종은 싱크 벽이 2.6~2.8미터라, 내려놓는 곳 아래에 서랍을 넣은 약 255센티미터 단축형을 따로 검토합니다. TIPS 1차년도에 평면 30개를 분석해 주방 표준안 3~5개로 묶는 것이 목표입니다. 표준 모듈 사용률이 40%에서 80%로 오르면 세대당 주방 모듈 원가가 332만원에서 244만원으로 내려가도록 재무모델에 연결했습니다. '
              '18개월에 사용률 60%를 못 넘으면 표준화 방식을 다시 봅니다.'),
        _lock=('table',)))
    s = start(prs, 'm07', pg(prs), c['title'], note=c['note'],
              visual='위: 한 줄 모듈 띠 (보관함 45 · 내려놓는 곳 70~80 · 싱크 80 · 서랍 60 · 식기세척기 60cm, 폭 비례). 아래 왼쪽: 평면마다 바뀌는 것 표. 아래 오른쪽: 숫자 3개.',
              chart='모듈 띠 + 표')
    mhead(s, c['kicker'], c['title'], c['sub'])
    text(s, MX, 2.0, 6, 0.26, '고정 — 한 줄 모듈 (위에서 본 그림, cm)', size=11, bold=True)
    parts = [('보관함', 45, '15171A'), ('내려놓는 곳', 75, None), ('싱크', 80, None), ('서랍', 60, None), ('식기세척기', 60, None)]
    xs = module_strip(s, MX, 2.4, CW, 0.82, parts, label_size=12, dim_size=10, sub='315 ~ 325cm  (내려놓는 곳 70 ~ 80)')
    rail_y = 2.4 - 0.1
    seg(s, xs[0][0] + 0.1, rail_y, xs[-1][1] - 0.1, rail_y, color=T['accent'], lw=3.0)
    text(s, xs[-1][1] - 2.4, rail_y - 0.3, 2.3, 0.24, '레일 (상부장 아래)', size=9, bold=True, color=T['accent'], align='r', check=False)
    ty = 3.95
    text(s, MX, ty, 6, 0.26, '평면마다 바뀌는 것', size=11, bold=True)
    tb = c['table']
    kit.table(s, MX, ty + 0.36, 6.6, tb[0], tb[1:], col_w=[2.0, 2.0, 2.6], size=10.5, header_size=9.5)
    rx = MX + 7.1; rw = W - MX - rx
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:3]]
    nums(s, rx, ty, rw, items, vsize=20, lsize=9.5, gap=0.18)
    mfoot(s)


# ================================================================= 08 market
def m08(prs):
    mk = M['market']['B']
    c = cp('m08', dict(
        kicker='IR ② 시장 규모 · 목표 시장',
        title='첫 시장은 주방을 새로 하는 구축 아파트입니다',
        sub='해마다 약 30만 세대가 주방을 바꾸고, 그중 연 1.8만 세대를 적용 가능 시장으로 봅니다',
        numbers=[{'value': f"연 약 {mk['sam']:,.0f}억원", 'label': f"적용 가능 시장 (구축 {mk['sam_remodel']:,.0f} + 신축 {mk['sam_new']:,.0f})", 'tag': 'DERIVED'},
                 {'value': f"약 {mk['som_share_hh'] * 100:.0f}%", 'label': f"Y5 계획 물량 / 적용 가능 세대 (Y5 매출 {mk['som']:.1f}억원 기준)", 'tag': 'TARGET'}],
        body=['비율(교체 30만 · 프리미엄 10% · 적용 60%)은 가정 → TIPS 기간 인터뷰 · 평면 분석으로 확인', '대중 시장 진입은 계획에 넣지 않음'],
        note=('시장은 큰 숫자보다 실제로 살 수 있는 세대 수부터 셉니다. 아파트는 약 1,328만호이고, 준공 20년 이상 주택이 56%입니다. '
              '해마다 주방을 바꾸는 아파트는 두 가지 방법으로 추정해 약 30만 세대로 봤습니다. 그중 주방 예산 2천만원 이상인 프리미엄 10%, 다시 구조상 적용이 가능한 60%를 가정하면 연 1.8만 세대입니다. '
              '금액으로는 구축 약 3,212억원에 신축 약 184억원을 더해 연 약 3,396억원입니다. 신축은 세대당 옵션 220만원에 입주자 25%가 로봇을 사는 것으로 가정했습니다. 5년차 계획 물량은 적용 가능 세대의 약 2%입니다. 비율은 모두 가정이고 TIPS 기간에 확인합니다. 참고로 준공 20년 이상 주택 56%는 전체 주택 기준이라 깔때기 단계로 쓰지 않았습니다.')))
    s = start(prs, 'm08', pg(prs), c['title'], note=c['note'],
              visual='왼쪽 깔때기 5단 (아파트 → 20년 이상 → 주방 교체 → 프리미엄 → 적용 가능). 오른쪽 숫자 2개.',
              chart='깔때기')
    mhead(s, c['kicker'], c['title'], c['sub'])
    rows = [(f"{mk['apt'] / 10:,.0f}만호", '아파트 (총주택 2,018만 × 아파트 65.8%)', 'DERIVED'),
            (f"연 약 {mk['rep'] / 10:,.0f}만 세대", f"주방 교체 (두 방식 추정 {mk['tri1'] / 10:.1f}만 · {mk['tri2'] / 10:.1f}만)", 'ASSUMPTION'),
            (f"연 {mk['prem'] / 10:,.0f}만 세대", '그중 프리미엄 (주방 예산 2,000만원 이상) 10%', 'ASSUMPTION'),
            (f"연 {mk['fit'] / 10:,.1f}만 세대", '그중 로봇 맞춤 주방 적용 가능 60%', 'ASSUMPTION')]
    lw = 7.5; fy = 2.05; rh = 0.8
    for i, (v, lab, tg) in enumerate(rows):
        ww = lw * (1 - i * 0.13); yy = fy + i * (rh + 0.1)
        hi = i == 3
        rect(s, MX, yy, ww, rh, fill=T['text'] if hi else ['EEEFF1', 'E6E8EB', 'DDE0E4', None][i])
        text(s, MX + 0.18, yy + 0.05, ww - 0.36, 0.4, v, size=17, bold=True, color=T['accent'] if hi else T['text'], check=False)
        text(s, MX + 0.18, yy + 0.42, ww - 1.3, 0.28, lab, size=9.5, color='C9CDD2' if hi else T['text2'], check=False)
        mt(s, MX + ww - 1.02, yy + 0.47, tg, fill='FFFFFF' if hi else None)
    text(s, MX, fy + 4 * (rh + 0.1) + 0.05, lw, 0.5, ['참고: 준공 20년 이상 주택 56.0% · 30년 이상 30.6% (전체 주택 기준, FACT) — 주방 교체 30만 세대는 이 비율에서 나온 값이 아님',
                                                       '출처: 국가데이터처 2025 인구주택총조사 (2026.7 발표) · 국토부 주택 통계 → 부록 C1 · F2'], size=8.5, color=GREY, check=False)
    rx = MX + lw + 0.6; rw = W - MX - rx
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:2]]
    yy = nums(s, rx, 2.05, rw, items, vsize=26, lsize=10, gap=0.32)
    text(s, rx, yy + 0.1, rw, 1.2, c['body'][:2], size=10.5, color=T['text2'], bullet='–', space_after=4, line=1.05)
    mfoot(s)


# ================================================================= 09 business model
def m09(prs):
    a = {d['key']: d['vals']['B'] for d in M['inputs']}; hh = M['household']['purchase_direct_Y3']; rn = M['rental']; v = M['value']
    c = cp('m09', dict(
        kicker='IR ④ 비즈니스 모델',
        title='설치할 때 한 번 크게, 쓰는 동안 매년 받습니다',
        sub=f"구축 1세대 기준: 설치 시점 약 {hh['y0']:,.0f}만원, 이후 관리 연 {a['p_care']}만원 + 소모품 연 약 {M['cons']['list_y']:.0f}만원",
        table=[['누가', '무엇에', '얼마 (가설)', '언제'],
               ['집주인 (구축 리모델링)', '로봇 맞춤 주방 (레일 · 보관함 · 서랍 등)', f"{a['p_rr']}만원 (주방 공사비 별도)", '설치할 때'],
               ['집주인', '로봇 + 설치 · 조정', f"{a['p_robot']:,}만원 + {a['p_comm']}만원", '설치할 때'],
               ['집주인 (구매 대신)', '로봇 렌탈 (관리 · 소모품 포함)', f"월 {a['p_rent']}만원 × {a['rent_months']}개월", '매월'],
               ['집주인', '관리 (점검 · 수리)', f"연 {a['p_care']}만원", '매년'],
               ['집주인', '소모품 (그리퍼 패드 등)', f"연 약 {M['cons']['list_y']:.0f}만원", '매년'],
               ['건설사 (신축)', '로봇 맞춤 주방 옵션', f"세대당 {a['p_rr_new']}만원 (공급가)", '분양 옵션 계약'],
               ['신축 입주자 (25% 가정)', '로봇 + 설치 · 조정', f"{a['p_robot']:,}만원 + {a['p_comm']}만원", '입주 후'],
               ['파트너 (인테리어 · 가구)', '판매 수수료를 받음 (ARKI가 지급)', '패키지의 10%', '판매할 때']],
        numbers=[{'value': f"{hh['rev5']:,.0f}만원", 'label': '1세대 5년 매출 (구매 · 직접판매)', 'tag': 'DERIVED'},
                 {'value': f"{hh['y0'] / hh['rev5']:.0%}", 'label': '그중 설치 시점 매출', 'tag': 'DERIVED'},
                 {'value': f"{hh['contrib5']:,.0f}만원", 'label': '1세대 5년 기여이익 (Y3 원가)', 'tag': 'DERIVED'}],
        body=['모든 가격은 가설 · VAT 별도 · 주방 공사비 별도',
              f"시간 가치 월 약 {v['value']:.0f}만원 (범위 {v['lo']:.0f}~{v['hi']:.0f}만원) < 원가 기준 렌탈 하한 월 {rn['Y3']['fee_at_20']:.0f}만원 (Y3, 마진 20%) → {rn['Y5']['fee_at_20']:.0f}만원 (Y5) · 모두 DERIVED → 지불의사 검증이 1순위"],
        note=('돈을 내는 사람과 시점을 표로 정리했습니다. 아래 가격은 모두 가정한 값이며, 부가세와 주방 공사비는 별도입니다. 구축 리모델링 세대는 설치할 때 로봇 맞춤 주방 증분 450만원과 로봇 1,490만원, 설치와 조정 80만원을 냅니다. 합치면 약 2,020만원입니다. '
              '구매가 부담스러운 고객은 월 33만원에 60개월 렌탈을 고를 수 있고, 관리와 소모품이 포함됩니다. 구매 고객은 매년 관리비 48만원과 소모품을 냅니다. '
              '신축은 건설사가 세대당 220만원에 주방 옵션을 사고, 입주자 중 25%가 로봇을 산다고 가정했습니다. 인테리어와 가구 파트너에게는 판매 수수료 10%를 줍니다. 렌탈은 투자회수 기간이 3년차 39개월, 5년차 30개월로 계산되어, 렌탈 회사가 요구하는 36개월을 맞추려면 로봇 원가가 약 1,059만원 이하여야 합니다. '
              '한 세대의 5년 매출은 약 2,418만원이고 84%가 설치 시점에 나옵니다. 가장 큰 위험은 가격입니다. 정리 시간을 돈으로 환산한 가치는 월 약 18만원, 범위로는 11~24만원인데, 3년차 원가에 마진 20%를 붙인 렌탈 하한은 월 31만원이고 5년차에도 24만원입니다. 그래서 지불의사 검증을 1순위로 둡니다.'),
        _lock=('table',)))
    s = start(prs, 'm09', pg(prs), c['title'], note=c['note'],
              visual='왼쪽 표: 누가 / 무엇에 / 얼마 / 언제 (7행). 오른쪽: 1세대 5년 매출 막대 (설치 시점 vs 이후) + 숫자 3개 + 가격 위험 1줄.',
              chart='수익 구조 표 + 1세대 매출 막대')
    mhead(s, c['kicker'], c['title'], c['sub'])
    tb = c['table']
    lw = 7.9
    rows = []
    for r in tb[1:]:
        when = r[3]
        hi = when.startswith('설치')
        rows.append([r[0], r[1], (r[2], {'bold': True}), (when, {'bold': hi, 'color': T['accent'] if hi else T['text2']})])
    th_ = kit.table(s, MX, 2.05, lw, tb[0], rows, col_w=[1.75, 2.85, 2.1, 1.2], size=10.5, header_size=9.5)
    mts(s, MX, 2.05 + th_ + 0.14, ['ASSUMPTION'])
    text(s, MX + 0.95, 2.05 + th_ + 0.11, lw - 1.0, 0.24, c['body'][0], size=9, color=GREY, check=False)
    rx = MX + lw + 0.45; rw = W - MX - rx
    # one-household 5-year revenue split
    R = hh['R']; y0 = hh['y0']; later = hh['rev5'] - y0
    text(s, rx, 2.02, rw, 0.26, '1세대 5년 매출 구성 (만원)', size=10.5, bold=True)
    bw_ = rw; bx = rx; by_ = 2.36
    w1 = bw_ * y0 / hh['rev5']
    rect(s, bx, by_, w1, 0.42, fill=T['text']); rect(s, bx + w1, by_, bw_ - w1, 0.42, fill='C9CDD2')
    text(s, bx, by_, w1, 0.42, f"설치 시점 {y0:,.0f}", size=9.5, bold=True, color='FFFFFF', align='c', anchor='m', check=False)
    text(s, bx + w1 - 0.1, by_ + 0.46, bw_ - w1 + 0.1, 0.22, f"이후 {later:,.0f}", size=9, color=T['text2'], align='r', check=False)
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:3]]
    yy = nums(s, rx, 3.05, rw, items, vsize=20, lsize=9.5, gap=0.12)
    rect(s, MX, 6.2, CW, 0.5, fill=T['soft']); rect(s, MX, 6.2, 0.06, 0.5, fill=T['accent'])
    text(s, MX + 0.22, 6.2, CW - 0.3, 0.5, [[('가장 큰 위험 = 가격   ', {'bold': True}), (c['body'][1] if len(c['body']) > 1 else '', {})]], size=10.5, anchor='m')
    mfoot(s)


# ================================================================= 10 go to market
def m10(prs):
    rd, rp, ni = inp('rd'), inp('rp'), B('ni'); bl = B('backlog')
    c = cp('m10', dict(
        kicker='IR ⑥ 사업화 로드맵',
        title='직접 팔며 배우고, 파트너로 늘리고, 신축 옵션으로 키웁니다',
        sub='직접판매로 가격 · 설치 · 사용을 확인하고, 파트너 판매와 신축 옵션으로 물량을 늘립니다',
        numbers=[{'value': '9.7%', 'label': '신축 유상옵션 / 분양가 (공개 7개 단지 평균, 보도 인용)', 'tag': 'FACT'},
                 {'value': '약 2년', 'label': '옵션 계약 → 입주', 'tag': 'ASSUMPTION'},
                 {'value': f"{bl[4]:.0f}세대", 'label': 'Y5 말 신축 대기 물량', 'tag': 'DERIVED'}],
        note=('판매는 세 단계입니다. 처음 2년은 직접 판매로 리모델링 고객을 만나 가격, 설치, 실제 사용을 배웁니다. 직접 판매의 고객 획득비는 세대당 150만원으로 가정했습니다. '
              '3년차부터는 인테리어와 주방가구 회사를 통해 판매하고 패키지의 10%를 수수료로 줍니다. 신축은 건설사 설계 단계에 옵션으로 들어가는데, 계약에서 입주까지 약 2년이 걸려 5년차부터 설치가 반영되고, 5년차 말 대기 물량은 400세대입니다. '
              '그래서 TIPS와 후속 투자 기간의 매출과 검증은 구축이 맡습니다. 해외는 국내에서 표준 한 줄과 설치 데이터를 쌓은 뒤 3년차 이후에 빌트인 주방 비중이 높은 시장부터 검토하며, 아직 계획 수치는 넣지 않았습니다.')))
    s = start(prs, 'm10', pg(prs), c['title'], note=c['note'],
              visual='왼쪽 3단 채널 (직접판매 → 파트너 → 신축 옵션) 시작 연도 · 조건. 오른쪽 연도별 설치 세대 누적 막대 (Base). 아래 숫자 3개.',
              chart='누적 막대 (설치 세대)')
    mhead(s, c['kicker'], c['title'], c['sub'])
    lanes = [('1', '직접 판매', 'Y1~', ['구축 리모델링 고객 · 학습용', f"설치 {rd[1]} → {rd[2]} → {rd[4]}세대 (Y2 · Y3 · Y5)", '고객 획득비 세대당 150만원 (가정)']),
             ('2', '인테리어 · 주방가구 파트너', 'Y3~', ['파트너가 팔고 ARKI가 설치', f"설치 {rp[2]} → {rp[3]} → {rp[4]}세대 (Y3 · Y4 · Y5)", '수수료 패키지의 10% (가정)']),
             ('3', '신축 옵션', 'Y3 계약~', ['건설사 설계 단계에 옵션으로', '프로젝트 1 → 2 → 3개 (800세대 × 옵션 10%)', 'Y5 설치 80세대 · 대기 400세대'])]
    lw = 5.6; ly = 2.02; lh = 1.14
    for i, (n_, a, when, lines) in enumerate(lanes):
        yy = ly + i * (lh + 0.12)
        rect(s, MX, yy, lw, lh, fill=T['text'] if i == 0 else T['soft'])
        c1 = 'FFFFFF' if i == 0 else T['text']; c2 = 'C9CDD2' if i == 0 else T['text2']
        text(s, MX + 0.18, yy + 0.1, lw - 1.6, 0.32, a, size=13, bold=True, color=c1)
        text(s, MX + lw - 1.35, yy + 0.12, 1.2, 0.28, when, size=10, bold=True, color=c2, align='r')
        text(s, MX + 0.18, yy + 0.46, lw - 0.36, 0.7, lines, size=9.5, color=c2, line=1.0, space_after=1)
    rx = MX + lw + 0.45; rw = W - MX - rx
    text(s, rx, ly, rw, 0.28, '연도별 설치 세대 (기본 시나리오)', size=11.5, bold=True)
    mts(s, rx + 3.15, ly + 0.05, ['TARGET'])
    cats = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']; ch_h = 2.55
    tot = [rd[i] + rp[i] + ni[i] for i in range(5)]; vmax = max(tot) * 1.2; cwid = rw * 0.72; pl = (0.02, 0.04, 0.96, 0.84)
    column_chart(s, rx, ly + 0.35, cwid, ch_h, cats, [('직접', [float(x) for x in rd]), ('파트너', [float(x) for x in rp]), ('신축', [float(x) for x in ni])],
                 ['15171A', 'A9AEB5', 'D3D7DC'], stacked=True, show_labels=False, size=10, gap=55, vmax=vmax, plot=pl)
    for i, tv in enumerate(tot):
        bx_ = rx + cwid * (pl[0] + pl[2] * (i + 0.5) / 5); by_ = ly + 0.35 + ch_h * (pl[1] + pl[3] * (1 - tv / vmax))
        text(s, bx_ - 0.5, by_ - 0.3, 1.0, 0.26, f"{tv:.0f}", size=11, bold=True, align='c', check=False)
    lx = rx + rw * 0.75
    for j, (lab, col) in enumerate([('신축', 'D3D7DC'), ('파트너', 'A9AEB5'), ('직접', '15171A')]):
        rect(s, lx, ly + 0.75 + j * 0.34, 0.18, 0.18, fill=col)
        text(s, lx + 0.26, ly + 0.7 + j * 0.34, rw * 0.25, 0.28, lab, size=9.5, anchor='m')
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:3]]
    nums_row(s, rx, 5.25, rw, items, vsize=20, lsize=9)
    text(s, MX, 6.0, lw, 0.24, '현재 협의 중인 파트너 · 건설사 없음 (FACT) · 세대 수 · 계약 수는 모두 목표 (TARGET)', size=9, bold=True, color=T['text2'], check=False)
    text(s, MX, 6.28, lw, 0.42, [[('해외 (FUTURE)  ', {'bold': True}), ('국내 표준 한 줄 · 설치 데이터로 3년차 이후 빌트인 주방 · 아파트 비중이 높은 해외 시장 검토 (검증 전, 계획 수치 없음)', {'color': T['text2']})]], size=9, check=False)
    mfoot(s, note=f"Y2 {rd[1]}세대 = TIPS 가정 실증 (실증 할인 50% · 렌탈 30% 가정) → Y2 매출 {B('rev')[1] / 1e4:.1f}억원 (산식: 재무모델 xlsx · 부록 D9)")


# ================================================================= 11 competition
def m11(prs):
    c = cp('m11', dict(
        kicker='IR ③ 경쟁 현황 · 차별성',
        title='가전은 기기 안만, 범용 로봇은 집마다 새로 배워야 합니다',
        sub='ARKI는 공간과 로봇을 같이 설계합니다. 이 방식이 더 낫다는 것은 아직 검증 전입니다.',
        table=[['공개 사례', '방식', '공개 내용 (보도 기준)'],
               ['1X NEO', '가정용 휴머노이드', '2만 달러 또는 월 499달러 · 2026 출하 발표'],
               ['LG CLOiD', '가정용 로봇', 'CES 2026 식기세척기 비우기 시연'],
               ['Moley Robotic Kitchen', '로봇 주방 (조리)', '팔 포함 £248,000'],
               ['Samsung Bot Chef', '레일형 로봇 팔', 'CES 2020 콘셉트'],
               ['Sunday Memo', '가정용 로봇', '2026 베타']],
        body=['평면 데이터 → 주방 표준안 3~5개', '설치비 · 설치 시간 검증 데이터', '가구 · 인테리어 파트너 실증 협의', '특허 출원 5건 (24개월 목표, 등록 미정)'],
        note=('경쟁은 접근 방식으로 봅니다. 가전 회사는 식기세척기와 인덕션 안의 일을 자동화하지만, 기기 사이에서 식기를 옮기고 정리하는 일은 남습니다. '
              '범용 로봇과 휴머노이드는 기존 집에 로봇이 적응하는 방식입니다. 1X는 NEO를 2만 달러 또는 월 499달러에 내놓겠다고 발표했고, LG는 CES 2026에서 식기세척기를 비우는 로봇을 시연했습니다. '
              'LG CLOiD가 시연한 식기세척기 비우기는 저희 첫 기능과 같은 작업입니다. 같은 작업에서 저희 방식이 나은지는 아직 검증하지 않았습니다. ARKI는 공간과 로봇을 같이 설계해 로봇이 집마다 풀어야 할 문제를 줄이는 쪽입니다. 다만 이 방식이 더 낫다는 것은 아직 검증 전이고, 주방가구 회사가 같은 일을 직접 할 위험도 있습니다. '
              '진입장벽은 지금 있는 것이 아니라 쌓아야 할 것입니다. 평면 데이터와 표준안, 설치 데이터, 파트너, 특허 출원입니다.'),
        _lock=('table',)))
    s = start(prs, 'm11', pg(prs), c['title'], note=c['note'],
              visual='왼쪽: 공개 사례 5개 표 (FACT). 가운데: 3가지 접근 비교 (가전 · 범용 로봇 · ARKI). 오른쪽: 쌓아야 할 진입장벽 4개.',
              chart='비교 표 + 접근 3열')
    mhead(s, c['kicker'], c['title'], c['sub'])
    tb = c['table']
    lw = 5.9
    kit.table(s, MX, 2.05, lw, tb[0], tb[1:], col_w=[1.75, 1.45, 2.7], size=9.5, header_size=9)
    mts(s, MX, 4.75, ['FACT'])
    text(s, MX + 0.55, 4.72, lw - 0.6, 0.24, '공개 보도 기준 · 출처 부록', size=8.5, color=GREY, check=False)
    cx0 = MX + lw + 0.35; cwid = 3.45
    cols = [('가전 회사', '기기 안 공정만 자동화', '기기 사이 옮기기 · 정리는 사람', False),
            ('범용 로봇', '기존 집에 로봇이 적응', '집마다 다른 공간을 현장에서 풀어야 함', False),
            ('ARKI', '공간과 로봇을 같이 설계', '공사 시점(리모델링 · 신축)에만 들어갈 수 있음', True)]
    for i, (a, b, d, hi) in enumerate(cols):
        yy = 2.05 + i * 0.98
        rect(s, cx0, yy, cwid, 0.88, fill=T['text'] if hi else T['soft'])
        text(s, cx0 + 0.16, yy + 0.08, cwid - 0.3, 0.3, a, size=12.5, bold=True, color='FFFFFF' if hi else T['text'])
        text(s, cx0 + 0.16, yy + 0.38, cwid - 0.3, 0.24, b, size=10, color='FFFFFF' if hi else T['text'], check=False)
        text(s, cx0 + 0.16, yy + 0.6, cwid - 0.3, 0.24, ('한계: ' if hi else '남는 일: ') + d, size=9, color='C9CDD2' if hi else T['text2'], check=False)
    mt(s, cx0 + cwid - 0.95, 2.05 + 2 * 0.98 + 0.1, 'TBV', fill=None)
    rx = cx0 + cwid + 0.35; rw = W - MX - rx
    text(s, rx, 2.05, rw, 0.28, '앞으로 쌓을 진입장벽', size=11.5, bold=True)
    text(s, rx, 2.33, rw, 0.22, '지금은 없음 · 모두 24개월 목표', size=8.5, color=GREY, check=False)
    for i, b in enumerate(c['body'][:4]):
        yy = 2.62 + i * 0.6
        marker(s, rx + 0.14, yy + 0.2, i + 1, d=0.26, fill=T['text'], size=9, ring=False)
        text(s, rx + 0.38, yy, rw - 0.38, 0.5, b, size=10.5, anchor='m', line=1.0)
    mts(s, rx, 5.05, ['TARGET'])
    band(s, 6.2, [('위험  ', {'bold': True}), ('주방가구 · 가전 회사가 같은 방식에 직접 들어올 수 있음 → 표준안 · 설치 데이터 · 파트너를 먼저 확보 (검증 전)', {})], size=10.5)
    mfoot(s)


# ================================================================= 12 financials
def m12(prs):
    sc = M['scenarios']; Bv = sc['B']
    rev = [v / 10000 for v in Bv['rev']]; op = [v / 10000 for v in Bv['op']]; gm = Bv['gm']
    c = cp('m12', dict(
        kicker='IR ⑥ 매출 목표 · 재무',
        title=f"5년차 매출 {rev[4]:.1f}억원, 손익분기는 6년차 이후입니다",
        sub=f"5년 누적 현금 최저 약 {min(Bv['cum_cash']) / 10000:.0f}억원 → TIPS로 기술을 확인한 뒤, 단계마다 검증하고 다음 투자를 받는 계획입니다",
        numbers=[{'value': f"연 약 {M['breakeven_kitchens']:,.0f}세대", 'label': '손익분기 설치 물량 (Y5 단가 · 원가)', 'tag': 'DERIVED'},
                 {'value': f"약 {min(Bv['cum_cash']) / 10000:.0f}억원", 'label': '5년 누적 현금 최저', 'tag': 'DERIVED'},
                 {'value': f"{gm[4]:.0%}", 'label': f"Y5 매출총이익률 (Y2 {gm[1]:.0%})", 'tag': 'DERIVED'}],
        note=(f"기본 시나리오의 매출은 1년차 0, 2년차 {rev[1]:.1f}억, 3년차 {rev[2]:.1f}억, 4년차 {rev[3]:.1f}억, 5년차 {rev[4]:.1f}억원입니다. 1~2년차는 TIPS 과제 기간이라 가정 실증 {inp('rd')[1]}세대 매출만 있습니다. "
              f"영업이익은 5년 내내 적자이고, 5년 누적 현금은 최저 약 마이너스 {-min(Bv['cum_cash']) / 10000:.0f}억원입니다. "
              f"연간 약 {M['breakeven_kitchens']:,.0f}세대를 설치해야 손익분기에 도달하므로 6년차 이후입니다. 보수 시나리오의 5년차 매출은 {sc['C']['rev'][4] / 1e4:.1f}억, 상향은 {sc['U']['rev'][4] / 1e4:.1f}억원입니다. "
              '즉 이 사업은 단계마다 검증을 통과해야 다음 투자를 받을 수 있는 구조이고, TIPS 24개월은 그 첫 기술 검증 단계입니다.')))
    s = start(prs, 'm12', pg(prs), c['title'], note=c['note'],
              visual='왼쪽: 연도별 매출 · 영업이익 막대 (억원, 기본). 오른쪽: 시나리오 3개 Y5 매출 + 숫자 3개.',
              chart='막대 2개 + 시나리오')
    mhead(s, c['kicker'], c['title'], c['sub'])
    lw = 7.3
    text(s, MX, 2.0, 3.0, 0.26, '매출 (억원)', size=11, bold=True)
    viz.bars(s, MX, 2.6, lw * 0.48, 2.2, rev, ['Y1', 'Y2', 'Y3', 'Y4', 'Y5'], lambda v: f"{v:.1f}", accent_idx=4)
    text(s, MX + lw * 0.52, 2.0, 3.0, 0.26, '영업이익 (억원)', size=11, bold=True)
    viz.bars(s, MX + lw * 0.52, 2.6, lw * 0.48, 2.2, op, ['Y1', 'Y2', 'Y3', 'Y4', 'Y5'], lambda v: f"{v:.1f}", vmax=5, vmin=min(op) * 1.15)
    mts(s, MX, 5.45, ['DERIVED'])
    text(s, MX + 0.75, 5.42, lw - 0.8, 0.24, '기본 시나리오 · 가격 · 물량 · 원가 가정에서 계산 (재무모델 xlsx)', size=8.5, color=GREY, check=False)
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, 2.0, rw, 0.26, 'Y5 매출 시나리오 (억원)', size=11, bold=True)
    scs = [('보수', sc['C']['rev'][4] / 10000), ('기본', sc['B']['rev'][4] / 10000), ('상향', sc['U']['rev'][4] / 10000)]
    mx_ = max(v for _, v in scs)
    for i, (lab, v) in enumerate(scs):
        yy = 2.38 + i * 0.4
        text(s, rx, yy, 0.6, 0.3, lab, size=10, anchor='m', check=False)
        rect(s, rx + 0.62, yy + 0.05, (rw - 1.5) * v / mx_, 0.2, fill=T['accent'] if lab == '기본' else 'C9CDD2')
        text(s, rx + 0.7 + (rw - 1.5) * v / mx_, yy, 0.8, 0.3, f"{v:.1f}", size=10, bold=lab == '기본', anchor='m', check=False)
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][:3]]
    nums(s, rx, 3.7, rw, items, vsize=20, lsize=9, gap=0.14)
    mfoot(s, note=f"Y2 매출 {rev[1]:.1f}억원 = TIPS 가정 실증 {inp('rd')[1]}세대 (실증 할인 50% · 렌탈 30% 가정) · 산식은 재무모델 xlsx · 부록 D9")


# ================================================================= 14 team
def m14(prs):
    TP = M['tips']
    c = cp('m14', dict(
        kicker='IR ⑤ 팀 · R&D 역량',
        title='TIPS 판단의 첫 질문은 팀이고, 그 칸은 아직 비어 있습니다',
        sub='필요한 역량은 로봇 조작, 주방 · 건축 시공, 고객 · 파트너 영업 세 가지입니다',
        note=('창업자 정보는 받지 못해 비워 두었습니다. 투자와 과제 평가에서 가장 중요한 칸이 비어 있다는 점을 그대로 보여드립니다. '
              'ARKI에 필요한 역량은 세 가지입니다. 식기를 집고 옮기는 로봇 조작, 주방가구와 건축 시공을 함께 설계하는 능력, 리모델링 고객과 가구 회사, 건설사를 상대하는 영업입니다. '
              f"TIPS 기간에는 대표가 과제책임자로 참여하고, 연구원 4명을 첫 6개월 안에 채용하며, 2차년도에 설치 · 실증 엔지니어와 사업개발 인력을 더해 평균 {TP['fte'][0]:.1f}명에서 {TP['fte'][1]:.0f}명으로 갑니다.")))
    s = start(prs, 'm14', pg(prs), c['title'], note=c['note'],
              visual='3열 역량 카드 (로봇 조작 · 주방/건축 시공 · 고객/파트너 영업), 각 카드 창업팀 보유 = [Founder 정보 필요]. 아래 왼쪽: 창업자 · R&D 역량 8항목 (미입력). 아래 오른쪽: TIPS 기간 채용 계획.',
              chart='역량 카드 + 채용 계획')
    mhead(s, c['kicker'], c['title'], c['sub'])
    caps = [('로봇 조작', '인식 · 집기 · 제어\n레일 · 그리퍼'), ('주방 · 건축 시공', '주방가구 설계 · 시공 표준\n벽체 고정 · 전원 · 설비'), ('고객 · 파트너 영업', '리모델링 고객 · 가구 회사\n인테리어 · 건설사 옵션')]
    cw = (CW - 0.5) / 3; cy = 2.0
    for i, (a, b) in enumerate(caps):
        cx = MX + i * (cw + 0.25)
        rect(s, cx, cy, cw, 1.85, fill=T['soft'])
        text(s, cx + 0.22, cy + 0.16, cw - 0.44, 0.36, a, size=15, bold=True)
        text(s, cx + 0.22, cy + 0.56, cw - 0.44, 0.6, b, size=10.5, color=T['text2'], line=1.05)
        dashed_rect(s, cx + 0.22, cy + 1.27, cw - 0.44, 0.42, color=T['text2'], lw=0.9)
        text(s, cx + 0.32, cy + 1.27, cw - 0.64, 0.42, [[('창업팀 보유  ', {'size': 9, 'color': GREY}), ('[Founder 정보 필요]', {'bold': True})]], size=10.5, anchor='m')
    ty = 4.15; lw = 5.0
    text(s, MX, ty, lw, 0.28, '창업자 · R&D 역량 확인 항목 (8) — 모두 미입력', size=11.5, bold=True)
    fi = ['학력 · 경력', '엔지니어링 · 제품 개발 경험', '로봇 경험', '건설 · 주방 이해', '보유 특허', '논문 · 수상 실적', '고객 · 파트너 네트워크', '전업 여부']
    for j, f in enumerate(fi):
        fx = MX + (j % 2) * (lw / 2); fy = ty + 0.4 + (j // 2) * 0.36
        text(s, fx, fy, lw / 2 - 0.1, 0.32, [[('□  ', {'color': GREY}), (f, {})]], size=10, anchor='m')
    mt(s, MX, ty + 1.9, 'TBV', label='[Founder 정보 필요]')
    text(s, MX + 1.35, ty + 1.86, lw - 1.35, 0.5, 'TIPS 요건: 대표 포함 창업팀 2인 이상 · 지분 60% 이상 · 운영사 30% 이하', size=8.5, bold=True, color=T['text2'], check=False)
    rx = MX + lw + 0.4; rw = W - MX - rx
    text(s, rx, ty, rw, 0.28, f"TIPS 기간 채용 계획 (평균 {TP['fte'][0]:.1f}명 → {TP['fte'][1]:.0f}명)", size=11.5, bold=True)
    mts(s, rx + rw - 0.95, ty + 0.05, ['ASSUMPTION'])
    for j, m_ in enumerate(TP['team']):
        hy = ty + 0.38 + j * 0.27
        part = f"과제 참여 {m_['part']:.0%}" if m_['part'] else '과제 외'
        text(s, rx, hy, 0.8, 0.26, f"M{m_['start']}~", size=9.5, bold=True, anchor='m', check=False)
        text(s, rx + 0.8, hy, rw - 2.2, 0.26, m_['role'], size=9.5, anchor='m', check=False)
        text(s, rx + rw - 1.4, hy, 1.4, 0.26, part, size=9, color=T['text2'], align='r', anchor='m', check=False)
        hline(s, rx, hy + 0.26, rw, color='E2E4E7', lw=0.5)
    text(s, rx, ty + 0.42 + len(TP['team']) * 0.27, rw, 0.45, '자문: 주방가구 제조 · 시공 / 건설사 유상옵션 / 로봇 안전인증 (ISO 10218 · ISO 13482 · KC) / 렌탈 금융', size=9, color=T['text2'])
    mfoot(s)


# ================================================================= TIPS R&D part (본문1 항목 요약)
# 과제 내용은 한 곳(TIPS)에 모아 두고, 슬라이드는 이 값만 읽는다. 숫자 Tag: 목표 = TARGET, 3D 검증 = CONCEPT.
TIPS = dict(
    name='주방 일체형 레일 로봇 기반 식사 후 식기 정리 자동화 시스템 개발',
    output='실물 크기 로봇 주방 시제품 2식 (레일 3.2m · 6축 협동로봇 · 보관함 · 식기세척기 · 서랍 연동) + 가정 실증 3세대',
    use='구축 아파트 주방 리모델링 패키지 (직접 판매 → 인테리어 · 주방가구 파트너) → 신축 아파트 유상 옵션 · 표준 한 줄 설계 데이터는 설치 표준으로 재사용',
    # 성과지표: name 지표 · unit 단위 · w 비중(%) · best 세계 최고 수준 (출처 요약, sources S36~S39) · now 개발 전 · y1 1차년도 (목업) · goal 최종 · basis 목표 설정 근거
    kpi=[dict(name='식기 정리 성공률\n(인식 → 넣기 → 꺼내기 → 수납, 사람 개입 없이)', unit='%', w=30,
              best='81: 가정 단순 과제 평균 (Dobb-E, 2023)\n59: 식기세척기 적재 연구 (2021)', now='실물 없음\n(3D 검증만)',
              y1='70 (M9 목업)', goal='90 이상', basis='로봇 자리 · 높이 · 랙을 고정한 조건이라\n범용 로봇 연구보다 높게 설정 (도전 목표)'),
         dict(name='식기 1점당 처리 시간', unit='초/점', w=15, best='비교 가능한 공개 수치 없음', now='–', y1='30 이하', goal='20 이하',
              basis='식사 1회 약 30점 → 10분 안에 넣기\n(사용자 요구 가설, 인터뷰로 확인)'),
         dict(name='파지 중 식기 파손 · 낙하', unit='건/1,000회', w=15, best='공개 수치 없음', now='–', y1='5 이하', goal='0',
              basis='파손은 고객이 받아들이기 어려운 실패'),
         dict(name='식기 인식 정확도', unit='%', w=10, best='비교 가능한 공개 수치 없음', now='–', y1='90 이상', goal='95 이상',
              basis='성공률 90%를 위한 인식 단계 여유'),
         dict(name='사람 접근 시 감속 · 접촉력', unit='mm/s · N', w=15, best='기준: 250mm/s 이하 · 손 140N 이하\n(ISO 10218-2:2025)', now='–',
              y1='설계 반영 · 사전 측정', goal='기준 이하', basis='협동로봇 안전 기준 충족\n(가정용은 ISO 13482 함께 검토)'),
         dict(name='설치 시간 (주방 설치 후 로봇)', unit='시간/세대', w=10, best='공개 자료 없음', now='–', y1='목업 설치 측정', goal='8 이하',
              basis='1일 · 2인 설치 → 설치비 80만원 가격 가설'),
         dict(name='표준 한 줄 적용 평면 비율', unit='%', w=5, best='공개 자료 없음', now='20\n(받은 5종 중 1종)', y1='평면 30개 분석', goal='60 이상',
              basis='M18 점검 기준 · 주방 모듈 원가\n332 → 244만원 전제')],
    kpi_how='평가: ①~④ 공인 시험기관 입회 시험 (표준 식기 20종 · 연속 200회, 파손은 1,000회 반복) · ⑤ 공인기관 안전 시험 · ⑥ 가정 실증 3세대 평균 · ⑦ 평면 30개 분석 보고서 (시험기관은 1차년도에 확정)',
    y1=['실물 크기 목업 주방 2식 (대표 평면)', '시제품 1차 2식 (레일 · 팔 · 보관함)', '식기 20종 데이터 · 인식 · 집기 1차',
        '목업 정리 성공률 70% (M9 점검)', '평면 30개 → 표준형 · 단축형 한 줄', '특허 출원 2건 · 정리 시간 기록 30세대'],
    y2=['시제품 2차 (설치 시간 · 안전 기능 보완)', '가정 실증 3세대 (유료 목표)', '성공률 90% · 처리 20초/점 · 파손 0',
        '공인기관 성능 · 안전 사전시험', '지불의사 조사 n ≥ 300', '특허 출원 누적 5건'],
    # (작업, [(시작 월, 끝 월), ...])
    wp=[('보관 · 전개 · 레일 구조', [(1, 9), (13, 18)]), ('식기 인식 · 집기', [(2, 12), (13, 21)]), ('식기세척기 · 서랍 연동', [(3, 10), (13, 18)]),
        ('평면 분석 · 표준 한 줄', [(1, 6), (7, 18)]), ('안전 · 시험 · 인증', [(4, 12), (15, 24)]), ('실증 · 고객 검증', [(1, 3), (13, 24)])],
    gates=[(6, '목업', '사람 동선과 로봇 동작범위 양립', '구조 변경'), (9, '성공률', '목업 정리 70% 이상', '작업 범위 축소'),
           (12, '지불의사', '중앙값 ≥ 목표가의 60%', 'B2C 재검토'), (18, '표준화', '표준 한 줄 적용 60% 이상', '표준화 재검토'),
           (24, '실증', '가정 3세대 · 공인시험 통과', '확장 투자 보류')],
    tech=[('① 보관 · 전개 구조', '보관함 45 × 62cm + 여닫이 문 + 레일 통로. 접힌 자세 ↔ 작업 자세 경로를 미리 계산', '3D 충돌검사 관통 0cm', '목업에서 전개 시간 · 간섭 실측'),
          ('② 낮은 곳 적재', '식기세척기 하단 랙을 44cm 당겨 위에서 수직으로 넣음. 집게 최저 37cm', '3D 단면 검증', '랙 당김 반복 · 적재 위치 오차 측정'),
          ('③ 식기 인식 · 집기', '깊이 카메라 2대 + 그리퍼 · 흡착 겸용. 식기 20종 데이터로 집는 방법 학습', '미착수', '성공률 · 파손 · 처리 시간 시험'),
          ('④ 평면 → 한 줄 배치', '도면 치수선으로 3D 변환 → 표준 한 줄 배치 → 충돌검사까지 자동화', '평면 4종 3D화 · 1종 적용', '평면 30개 적용률')],
    ip=['로봇 보관함 · 레일 통로 일체형 주방가구 구조', '식기세척기 하단 랙 당김과 상부 적재 연동', '주방 사람 · 로봇 구역 기반 정지 · 감속 제어',
        '설치 후 자동 좌표 보정', '평면 기반 로봇 주방 한 줄 배치 · 검증 방법'],
    std=[('ISO 10218-1/-2:2025', '협동로봇 안전 (설계 기준)'), ('ISO 13482', '개인케어로봇 안전 (가정용 적용 검토)'), ('KC · 전파법', '전기 안전 · EMC (해당 여부 확인)'),
         ('식품용 기구 기준', '식기에 닿는 집게 · 흡착컵 재질')],
)


def _tag_cell(v, tag):
    return [(v + '  ', {'bold': True}), (tag, {'size': 7, 'color': GREY, 'bold': True})]


# ================================================================= 02 one-page summary
def m_sum(prs):
    a = {d['key']: d['vals']['B'] for d in M['inputs']}; mk = M['market']['B']; hh = M['household']['purchase_direct_Y3']; TP = M['tips']
    c = cp('m_sum', dict(
        kicker='요약',
        title='식기 정리를 맡는 로봇 주방을, TIPS 24개월 동안 가정 실증까지 만듭니다',
        note=('한 장으로 요약하면 이렇습니다. 식기세척기는 씻기만 하고, 옮기고 넣고 꺼내서 정리하는 일은 아직 사람이 합니다. ARKI는 로봇을 기존 주방에 들이는 대신, 로봇이 일할 자리를 주방 설계 단계에서 만듭니다. '
              f"TIPS 24개월 동안 시제품과 실물 크기 목업을 만들고, 가정 3세대에서 실증하며, 정리 성공률 90%를 목표로 공인기관 시험을 받습니다. 첫 시장은 구축 아파트 주방 리모델링이고, 적용 가능 시장은 연 약 {mk['sam']:,.0f}억원으로 봅니다. "
              f"요청은 TIPS R&D {TP['gov'] / 1e4:.0f}억원과 운영사 투자 {a['op_invest'] / 1e4:.0f}억원입니다. 현재는 Concept 단계로 시제품, 고객, 계약, 파트너, 매출, 투자유치가 없습니다.")))
    s = start(prs, 'm_sum', pg(prs), c['title'], note=c['note'],
              visual='3열 × 2행 카드: 문제 · 해결 · TIPS 과제 / 시장 · 수익 · 요청. 카드마다 한 줄 설명 + 핵심 숫자 1개 (Tag). 아래 띠: 지금 → 24개월 뒤.',
              chart='요약 카드 6개')
    mhead(s, c['kicker'], c['title'])
    cards = [('문제', '식기세척기는 씻기만 합니다', '옮기고 · 넣고 · 꺼내서 · 정리하는 일은 사람 몫', '약 40분', '하루 식사 후 정리 시간', 'ASSUMPTION'),
             ('해결', '로봇 자리를 주방에 먼저 만듭니다', '상부장 아래 레일 · 로봇 보관함 · 식기세척기 · 서랍을 한 줄로 설계', '3,150mm', '대표 평면에 넣은 한 줄 (3D 충돌 0cm)', 'CONCEPT'),
             ('TIPS 과제', '시제품 → 목업 → 가정 실증 3세대', '성공률 · 처리 시간 · 파손 · 안전을 공인기관 시험으로 확인', '90%', '최종 식기 정리 성공률 목표', 'TARGET'),
             ('시장', '첫 시장은 구축 아파트 주방 리모델링', f"주방 교체 연 약 {mk['rep'] / 10:.0f}만 세대 중 적용 가능 연 {mk['fit'] / 10:.1f}만 세대", f"연 약 {mk['sam']:,.0f}억원", '적용 가능 시장 (구축 + 신축)', 'DERIVED'),
             ('수익', '설치 때 한 번, 쓰는 동안 매년', f"로봇 주방 {a['p_rr']} + 로봇 {a['p_robot']:,} + 설치 {a['p_comm']}만원 · 이후 관리 · 소모품", f"약 {hh['y0']:,.0f}만원", '구축 1세대 설치 시점 매출 (가설)', 'ASSUMPTION'),
             ('요청', f"TIPS R&D {TP['gov'] / 1e4:.0f}억원 + 운영사 투자 {a['op_invest'] / 1e4:.0f}억원", f"24개월 지출 약 {TP['spend_total'] / 1e4:.1f}억원 · M12 점검 뒤 후속 {a['followon'] / 1e4:.0f}억원 목표", f"{(TP['gov'] + a['op_invest']) / 1e4:.0f}억원", 'TIPS R&D + 운영사 투자', 'ASSUMPTION')]
    cw = (CW - 2 * 0.25) / 3; ch = 2.0; y0 = 1.62
    for i, (lab, head_, body, val, vlab, tg) in enumerate(cards):
        cx = MX + (i % 3) * (cw + 0.25); cy = y0 + (i // 3) * (ch + 0.22)
        hi = lab in ('TIPS 과제', '요청')
        rect(s, cx, cy, cw, ch, fill=T['text'] if hi else T['soft'])
        c1 = 'FFFFFF' if hi else T['text']; c2 = 'C9CDD2' if hi else T['text2']
        text(s, cx + 0.2, cy + 0.14, cw - 0.4, 0.24, lab, size=9.5, bold=True, color='8C9198' if hi else GREY, check=False)
        text(s, cx + 0.2, cy + 0.38, cw - 0.4, 0.34, head_, size=13, bold=True, color=c1, label='sum:' + lab)
        text(s, cx + 0.2, cy + 0.74, cw - 0.4, 0.46, body, size=9.5, color=c2, line=1.0, label='sumb:' + lab)
        text(s, cx + 0.2, cy + 1.2, cw - 0.4, 0.44, val, size=21, bold=True, color=T['accent'], label='sumv:' + lab)
        text(s, cx + 0.2, cy + 1.62, cw - 1.5, 0.24, vlab, size=8.5, color=c2, check=False)
        mt(s, cx + cw - 0.2 - (kit.text_w(MT_LABEL.get(tg, tg), 6.5, True) + 0.12), cy + 1.66, tg, fill='FFFFFF' if hi else None)
    band(s, y0 + 2 * ch + 0.22 + 0.2, [('지금  ', {'bold': True}), ('Concept 단계 · 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 · 투자유치 없음 (FACT)', {}),
                                       ('     →     24개월 뒤  ', {'bold': True}), ('공인시험 성적 · 가정 실증 3세대 · 특허 출원 5건 · 후속 투자 판단 자료', {})], size=10.5)
    mfoot(s)


# ================================================================= TIPS ① goal + KPIs
def m_kpi(prs):
    c = cp('m_kpi', dict(
        kicker='TIPS 과제 ①  기술개발 목표 · 성과지표',
        title='최종 목표: 실제 주방에서 식기 정리를 90% 이상 혼자 끝내는 시제품',
        sub=f"과제명 (안): {TIPS['name']} · 24개월",
        note=('TIPS 과제의 최종 목표와 성과지표입니다. 결과물은 실물 크기 로봇 주방 시제품 2식과 가정 실증 3세대입니다. '
              '가장 비중이 큰 지표는 사람 개입 없이 식기를 인식해서 식기세척기에 넣고, 꺼내서 서랍에 정리까지 끝내는 비율이며 최종 90% 이상이 목표입니다. '
              '공개 연구에서는 가정 단순 과제 평균 81%, 식기세척기 적재 연구 약 59%가 보고되어 있어 90%는 도전 목표입니다. 다만 ARKI는 로봇 자리와 높이, 랙 위치를 고정한 조건이라 범용 로봇보다 높게 잡았습니다. 측정 조건이 달라 직접 비교는 어렵다는 점도 표시했습니다. 처리 시간, 파손, 인식 정확도, 사람 접근 시 감속과 접촉력, 설치 시간, 표준 한 줄 적용 평면 비율을 함께 봅니다. '
              '개발 전 수준은 실물이 없고 3D 검증만 한 상태입니다. 평가는 가능한 한 공인기관 입회 시험으로 합니다.')))
    s = start(prs, 'm_kpi', pg(prs), c['title'], note=c['note'],
              visual='상단: 최종 결과물 한 줄. 본문: 성과지표 표 7행 (지표 · 단위 · 비중 · 세계 최고 수준 · 개발 전 · 최종 목표 · 평가 방법). 비중 합 100%.',
              chart='성과지표 표')
    y = mhead(s, c['kicker'], c['title'], c['sub'])
    rect(s, MX, y - 0.02, CW, 0.66, fill=T['soft'])
    text(s, MX + 0.18, y + 0.02, CW - 0.3, 0.3, [[('최종 결과물  ', {'bold': True, 'color': GREY, 'size': 9.5}), (TIPS['output'], {'bold': True})]], size=11, anchor='m')
    text(s, MX + 0.18, y + 0.31, CW - 0.3, 0.3, [[('용도 · 적용  ', {'bold': True, 'color': GREY, 'size': 9.5}), (TIPS['use'], {})]], size=10.5, anchor='m')
    y += 0.78
    rows = []
    for k in TIPS['kpi']:
        rows.append([(k['name'], {'bold': True}), k['unit'], f"{k['w']}", k['best'], k['now'], (k['goal'], {'bold': True, 'color': T['accent']}), k['basis']])
    tot = sum(k['w'] for k in TIPS['kpi'])
    rows.append([('합계', {'bold': True}), '', (f"{tot}", {'bold': True}), '', '', '', ''])
    th = kit.table(s, MX, y, CW, ['성과지표', '단위', '비중(%)', '세계 최고 수준', '개발 전', '최종 목표', '목표 설정 근거'], rows,
                   col_w=[2.6, 0.85, 0.6, 2.6, 1.1, 0.95, 3.133], size=8.5, header_size=8, label='kpi', max_h=H - y - 1.05, pad=0.04,
                   align=['l', 'c', 'c', 'l', 'c', 'c', 'l'])
    text(s, MX, max(y + th + 0.3, H - 1.15), CW, 0.26, TIPS['kpi_how'], size=8.5, color=T['text2'], label='kpi_how')
    mts(s, MX, H - 0.78, ['TARGET'])
    text(s, MX + 0.7, H - 0.81, CW - 0.8, 0.24, '목표 = TIPS 과제 목표 · 세계 최고 수준 = 공개 연구 자료 (측정 조건이 달라 직접 비교 어려움) · 출처 부록 F2', size=8.5, color=GREY, check=False)
    mfoot(s)


# ================================================================= TIPS ② yearly goals + schedule + gates
def m_plan(prs):
    c = cp('m_plan', dict(
        kicker='TIPS 과제 ②  연차별 목표 · 수행 일정',
        title='1차년도엔 목업에서 70%, 2차년도엔 실제 집에서 90%를 확인합니다',
        note=('1차년도에는 대표 평면 기준의 실물 크기 목업 주방 2식과 1차 시제품 2식을 만들고, 식기 20종으로 인식과 집기를 개발합니다. 9개월에 목업 정리 성공률 70%가 첫 기술 점검입니다. '
              '같은 기간에 평면 30개를 분석해 표준형과 단축형 한 줄을 정합니다. 2차년도에는 설치 시간과 안전 기능을 보완한 2차 시제품으로 가정 3세대에서 실증하고, 공인기관 시험을 받습니다. '
              '6, 9, 12, 18, 24개월에 점검하고 기준에 못 미치면 구조를 바꾸거나 범위를 줄이거나 확장 투자를 보류합니다.')))
    s = start(prs, 'm_plan', pg(prs), c['title'], note=c['note'],
              visual='위: 1차년도 · 2차년도 목표 2칸. 아래: 6개 작업 × 24개월 일정 막대 + 점검 5개 (M6 · M9 · M12 · M18 · M24, 주황) 기준 · 못 넘으면.',
              chart='일정 막대 (Gantt) + 점검')
    y = mhead(s, c['kicker'], c['title'])
    bw = (CW - 0.25) / 2
    for i, (lab, items) in enumerate([('1차년도  M1 ~ M12', TIPS['y1']), ('2차년도  M13 ~ M24', TIPS['y2'])]):
        bx = MX + i * (bw + 0.25)
        rect(s, bx, y, bw, 1.42, fill=T['text'] if i else T['soft'])
        text(s, bx + 0.2, y + 0.1, bw - 0.4, 0.28, lab, size=12, bold=True, color='FFFFFF' if i else T['text'])
        half = (len(items) + 1) // 2
        for j, it in enumerate(items):
            cx = bx + 0.2 + (j // half) * ((bw - 0.4) / 2); cy = y + 0.46 + (j % half) * 0.3
            text(s, cx, cy, (bw - 0.4) / 2 - 0.05, 0.28, [[('· ', {'color': '8C9198'}), (it, {})]], size=9.5, color='E2E4E7' if i else T['text'], label='yr:' + it[:8])
    # Gantt
    gy = y + 1.62; lw = 2.3; gx = MX + lw; gw = CW - lw; mw = gw / 24; rh = 0.27
    for m in range(24):
        text(s, gx + m * mw, gy, mw, 0.2, f"{m + 1}", size=7, color=GREY, align='c', check=False)
    rect(s, gx + 12 * mw - 0.005, gy, 0.01, 0.24 + len(TIPS['wp']) * rh, fill=T['line'])
    for k, (nm, spans) in enumerate(TIPS['wp']):
        ry = gy + 0.24 + k * rh
        text(s, MX, ry, lw - 0.1, rh, nm, size=9.5, anchor='m', check=False)
        hline(s, MX, ry + rh, CW, color='E2E4E7', lw=0.5)
        for a0, a1 in spans:
            rect(s, gx + (a0 - 1) * mw + 0.02, ry + 0.06, (a1 - a0 + 1) * mw - 0.04, rh - 0.12, fill='3A3F46' if a0 > 12 else '9AA0A7')
    gy2 = gy + 0.24 + len(TIPS['wp']) * rh + 0.06
    for m_, nm, crit, kill in TIPS['gates']:
        gxm = gx + (m_ - 0.5) * mw
        seg(s, gxm, gy + 0.22, gxm, gy2, color=T['accent'], lw=1.25, dash=True)
        marker(s, gxm, gy2 + 0.13, f"{m_}", d=0.26, fill=T['accent'], size=7.5)
    # gate criteria row
    ty = gy2 + 0.36; n = len(TIPS['gates']); gwid = (CW - 0.12 * (n - 1)) / n
    for i, (m_, nm, crit, kill) in enumerate(TIPS['gates']):
        cx = MX + i * (gwid + 0.12)
        rect(s, cx, ty, gwid, 0.86, line=T['line'], lw=0.75)
        text(s, cx + 0.12, ty + 0.06, gwid - 0.24, 0.24, [[(f"M{m_}  ", {'bold': True, 'color': T['accent']}), (nm, {'bold': True})]], size=10, check=False)
        text(s, cx + 0.12, ty + 0.3, gwid - 0.24, 0.26, crit, size=8.5, color=T['text2'], label='gate:' + nm)
        text(s, cx + 0.12, ty + 0.56, gwid - 0.24, 0.26, [[('못 넘으면 ', {'color': GREY}), (kill, {'bold': True})]], size=8.5, check=False)
    mts(s, MX, ty + 0.94, ['TARGET'])
    text(s, MX + 0.7, ty + 0.91, CW - 0.8, 0.24, '모든 목표 · 기준 = TIPS 과제 목표 (측정 전) · 막대: 회색 1차년도, 검정 2차년도', size=8.5, color=GREY, check=False)
    mfoot(s)


# ================================================================= TIPS ③ core tech + prior work + difference
def m_tech(prs):
    c = cp('m_tech', dict(
        kicker='TIPS 과제 ③  핵심기술 개발 방법 · 선행 개발',
        title='공간을 먼저 맞추고, 로봇은 정해진 자리에서만 일하게 만듭니다',
        note=('개발할 핵심기술은 네 가지입니다. 첫째, 로봇을 보관함에 접어 두었다가 꺼내는 구조와 경로. 둘째, 식기세척기 하단 랙을 당겨 위에서 넣는 낮은 곳 적재. 셋째, 식기 인식과 집기. 넷째, 받은 평면을 3D로 옮겨 표준 한 줄을 배치하고 충돌검사까지 하는 작업입니다. '
              '첫째, 둘째, 넷째는 3D 모델에서 먼저 검증했고, 식기 인식과 집기는 아직 시작하지 않았습니다. 국가 R&D 수행 이력과 특허 출원은 없습니다. '
              '범용 로봇은 집마다 다른 주방을 현장에서 풀어야 하지만, ARKI는 로봇의 자리와 높이, 동선을 설계 단계에서 정해 로봇이 풀어야 할 문제를 줄입니다. 이 방식이 실제로 더 나은지는 이번 과제에서 검증합니다.')))
    s = start(prs, 'm_tech', pg(prs), c['title'], note=c['note'],
              visual='왼쪽 2 × 2 기술 카드 (방법 · 지금 상태 · 검증 방법). 오른쪽: 선행 개발 이력 표. 아래 띠: 기존 기술 대비 차이 (검증 전).',
              chart='기술 카드 4개 + 이력 표')
    y = mhead(s, c['kicker'], c['title'])
    lw = 7.65; cw = (lw - 0.2) / 2; ch = 1.95
    for i, (nm, how, now, ver) in enumerate(TIPS['tech']):
        cx = MX + (i % 2) * (cw + 0.2); cy = y + (i // 2) * (ch + 0.18)
        rect(s, cx, cy, cw, ch, fill=T['soft'])
        text(s, cx + 0.18, cy + 0.14, cw - 0.36, 0.3, nm, size=13.5, bold=True)
        text(s, cx + 0.18, cy + 0.52, cw - 0.36, 0.72, how, size=10, color=T['text2'], line=1.0, label='tech:' + nm)
        done = now not in ('미착수',)
        chipl(s, cx + 0.18, cy + 1.42, ('지금  ' + now), size=9, color=T['text'] if done else GREY, line=EDGE)
        text(s, cx + 0.18, cy + 1.64, cw - 0.36, 0.26, [[('검증  ', {'bold': True, 'color': GREY}), (ver, {})]], size=9.5, check=False)
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y, rw, 0.28, '선행 개발 이력', size=12, bold=True)
    rows = [['자체 설계 · 3D 검증', '보관 · 전개 · 레일 이동 경로 충돌검사 (관통 0cm) · 낮은 곳 단면', '2026.10'],
            ['평면 적용', '받은 평면 5종 중 4종 3D화, 대표 1종에 한 줄 배치 (충돌 0cm)', '2026.10'],
            ['국가 R&D 수행', '없음 (중기부 · 타 부처 모두)', '–'],
            ['특허', '출원 없음 · 후보 10건 정리 (부록 E2)', '–']]
    th = kit.table(s, rx, y + 0.36, rw, ['구분', '내용', '시기'], rows, col_w=[1.15, rw - 1.85, 0.7], size=9, header_size=8.5, label='prior')
    mts(s, rx, y + 0.36 + th + 0.1, ['CONCEPT'])
    text(s, rx + 0.82, y + 0.36 + th + 0.07, rw - 0.85, 0.24, '3D 단순 모델 결과 · 실물 미검증', size=8.5, color=GREY, check=False)
    band(s, y + 2 * ch + 0.18 + 0.22, [('기존 기술과 다른 점  ', {'bold': True}), ('범용 로봇은 집마다 다른 주방을 현장에서 풀어야 함 · 가전은 기기 안만 자동화 → ARKI는 로봇 자리 · 높이 · 동선을 설계 단계에서 고정 (더 나은지는 이번 과제에서 검증)', {})], size=10)
    mfoot(s)


# ================================================================= TIPS ④ organisation + IP + safety
def m_org(prs):
    TP = M['tips']
    c = cp('m_org', dict(
        kicker='TIPS 과제 ④  추진 체계 · 지식재산 · 안전',
        title='개발은 주관기관이 직접 하고, 특허와 안전 기준은 처음부터 같이 챙깁니다',
        note=('과제는 주관기관이 전부 수행합니다. 공동기관과 위탁기관은 두지 않고, 공인 시험과 인증은 시험기관에 의뢰합니다. '
              '대표가 과제책임자로 참여하고, 연구원 4명을 첫 6개월 안에 채용하며, 2차년도에 설치 · 실증 엔지니어와 사업개발 인력을 더합니다. 정부지원금 5억원당 청년 1명을 새로 뽑아야 하므로 신규 연구원 중 2명 이상을 청년으로 채용합니다. TIPS는 대표를 포함한 창업팀 2인 이상이 지분 60% 이상을 가져야 하는데, 창업팀 정보는 아직 받지 못했습니다. '
              '특허는 3개월 안에 선행기술조사를 마치고 24개월 동안 5건 출원을 목표로 합니다. 등록 여부는 알 수 없습니다. '
              '안전은 협동로봇 안전 표준과 개인케어로봇 표준을 설계 기준으로 쓰고, 전기 안전과 전자파, 식기에 닿는 부품의 재질 기준을 확인합니다.')))
    s = start(prs, 'm_org', pg(prs), c['title'], note=c['note'],
              visual='왼쪽: 추진 체계 (주관 100%) + TIPS 기간 팀 구성. 가운데: 특허 출원 목표 5건. 오른쪽: 안전 · 인증 기준. 아래 띠: 결과 검증 방법.',
              chart='3열 (체계 · 지식재산 · 안전)')
    y = mhead(s, c['kicker'], c['title'])
    c1 = 4.15; c2 = 3.75; gap = 0.3; c3 = CW - c1 - c2 - 2 * gap
    x1 = MX; x2 = x1 + c1 + gap; x3 = x2 + c2 + gap
    text(s, x1, y, c1, 0.28, '추진 체계', size=12, bold=True)
    kit.table(s, x1, y + 0.36, c1, ['기관', '맡는 일', '비중'], [['주관 (ARKI)', '설계 · 시제품 · SW · 실증 전부', '100%'], ['공동 · 위탁', '없음 (시험 · 인증은 공인기관 의뢰)', '–']],
              col_w=[1.05, c1 - 1.65, 0.6], size=9, header_size=8.5, label='org')
    text(s, x1, y + 1.4, c1, 0.26, 'TIPS 기간 팀 (채용 계획)', size=10.5, bold=True)
    tr = []
    for m_ in TP['team']:
        when = f"M{m_['start']}~"
        part = f"{m_['part']:.0%}" if m_['part'] else '과제 외'
        tr.append([m_['role'], when, part])
    kit.table(s, x1, y + 1.7, c1, ['역할', '시작', '과제 참여'], tr, col_w=[c1 - 1.5, 0.65, 0.85], size=8.5, header_size=8, label='team', pad=0.035)
    mts(s, x1, y + 3.78, ['ASSUMPTION'])
    text(s, x1, y + 4.02, c1, 0.5, ['청년 고용 의무 (정부지원 5억원당 1명) → 신규 연구원 중 2명 이상 청년',
                                   'TIPS 요건: 창업팀 2인 이상 · 지분 60% 이상 → [Founder 정보 필요]'], size=8.5, color=T['text2'], label='orgreq')
    text(s, x2, y, c2, 0.28, '지식재산: 24개월 출원 목표 5건', size=12, bold=True)
    for i, t in enumerate(TIPS['ip']):
        yy = y + 0.42 + i * 0.5
        marker(s, x2 + 0.13, yy + 0.18, i + 1, d=0.26, fill=T['text'], size=9, ring=False)
        text(s, x2 + 0.38, yy, c2 - 0.4, 0.42, t, size=10, anchor='m', line=1.0, label='ip')
    mts(s, x2, y + 3.0, ['TARGET'])
    text(s, x2 + 0.7, y + 2.97, c2 - 0.75, 0.5, 'M3까지 선행기술조사 (KIPRIS · USPTO · EPO) 후 확정 · 등록 여부 미정', size=8.5, color=GREY)
    text(s, x3, y, c3, 0.28, '안전 · 인증 기준', size=12, bold=True)
    kit.table(s, x3, y + 0.36, c3, ['기준', '쓰는 곳'], [[(a_, {'bold': True}), b_] for a_, b_ in TIPS['std']], col_w=[1.45, c3 - 1.45], size=9, header_size=8.5, label='std')
    text(s, x3, y + 2.3, c3, 0.9, ['2차년도: 공인기관 성능 · 안전 사전시험', '본인증은 후속 투자 단계 (3년차)'], size=9.5, color=T['text2'], bullet='–', space_after=2)
    band(s, y + 4.62, [('결과 검증  ', {'bold': True}), ('공인기관 시험성적서 (성능 · 안전) · 가정 실증 기록 (사용 로그 · 설문) · 평면 30개 분석 보고서 · 특허 출원서', {})], size=10.5)
    mfoot(s)


# ================================================================= TIPS ⑤ R&D budget + funding (ask)
def m_fund(prs):
    a = {d['key']: d['vals']['B'] for d in M['inputs']}; TP = M['tips']
    eo = lambda v: f"{v / 1e4:.2f}"
    c = cp('m_fund', dict(
        kicker='TIPS 과제 ⑤  연구개발비 · 자금 계획',
        title=f"TIPS R&D {TP['gov'] / 1e4:.0f}억원과 운영사 투자 {a['op_invest'] / 1e4:.0f}억원으로 24개월을 시작합니다",
        sub=f"24개월 회사 전체 지출 약 {TP['spend_total'] / 1e4:.1f}억원 = TIPS 과제 {TP['total'] / 1e4:.1f}억원 + 과제 밖 비용 {TP['non_rnd'] / 1e4:.1f}억원 (인건비 일부 · 관리 · 고객 조사 등)",
        note=(f"TIPS 과제 예산은 총 {TP['total'] / 1e4:.1f}억원입니다. 2026 공고에 따라 정부지원금은 총 연구개발비의 {a['tips_gov_ratio']:.0%} 이내라, 정부지원금 {TP['gov'] / 1e4:.0f}억원에 기관부담 {TP['private'] / 1e4:.1f}억원을 더했습니다. 기관부담은 현금 {TP['private_cash'] / 1e4:.2f}억원과 대표 인건비 현물 {TP['inkind'] / 1e4:.2f}억원입니다. "
              f"과제 밖에서도 연구원 인건비 일부와 관리비, 고객 조사 비용이 들어 24개월 회사 전체 지출은 약 {TP['spend_total'] / 1e4:.1f}억원입니다. "
              f"재원은 TIPS {TP['gov'] / 1e4:.0f}억원, 운영사 투자 {a['op_invest'] / 1e4:.0f}억원, 그리고 12개월 점검 뒤 후속 투자 {a['followon'] / 1e4:.0f}억원을 목표로 합니다. 후속 투자가 없으면 약 {TP['runway_no_followon']:.0f}개월까지 갈 수 있어 2차 시제품과 실증 범위를 줄여야 합니다. "
              f"운영사 투자 3억원은 수도권 기준 요건 2억원을 넘는 금액입니다. 선정 뒤 별도로 신청하는 창업사업화 · 해외마케팅 연계 자금 (각 최대 {TP['biz_link'] / 1e4:.1f}억원)은 계획에 넣지 않았습니다. 현재 투자유치 실적은 없습니다.")))
    s = start(prs, 'm_fund', pg(prs), c['title'], note=c['note'],
              visual='왼쪽: TIPS 과제 예산 비목 표 (1차년도 · 2차년도 · 합계, 현금/현물). 오른쪽: 재원 vs 지출 막대 2개 + 숫자. 아래 띠: 투자유치 현황 · 운영사 연계.',
              chart='비목 표 + 재원 · 지출 막대')
    y = mhead(s, c['kicker'], c['title'], c['sub'])
    lw = 6.9
    text(s, lw + MX - 2.2, y - 0.02, 2.2, 0.24, '단위: 억원', size=8.5, color=GREY, align='r', check=False)
    text(s, MX, y - 0.02, 4.0, 0.26, 'TIPS 과제 예산 (24개월)', size=11.5, bold=True)
    rows = []
    for r in TP['rows']:
        rows.append([(r['cat'], {'bold': True}), r['item'], r['kind'], eo(r['y1']), eo(r['y2']), (eo(r['total']), {'bold': True})])
    yt = TP['year_total']
    rows.append([('합계', {'bold': True}), f"정부 {TP['gov'] / 1e4:.0f} · 기관부담 {TP['private'] / 1e4:.2f} (현금 {TP['private_cash'] / 1e4:.2f} · 현물 {TP['inkind'] / 1e4:.2f})", '',
                 (eo(yt[0]), {'bold': True}), (eo(yt[1]), {'bold': True}), (eo(TP['total']), {'bold': True, 'color': T['accent']})])
    th = kit.table(s, MX, y + 0.3, lw, ['비목', '내용', '구분', '1차년도', '2차년도', '합계'], rows, col_w=[0.95, 3.45, 0.55, 0.65, 0.65, 0.65],
                   size=8.5, header_size=8, label='budget', align=['l', 'l', 'c', 'r', 'r', 'r'], pad=0.04)
    mts(s, MX, y + 0.3 + th + 0.12, ['ASSUMPTION'])
    text(s, MX + 0.95, y + 0.3 + th + 0.09, lw - 1.0, 0.24, f"2026 공고: 정부지원 {a['tips_gov_ratio']:.0%} 이내 · 기관부담 중 현금 {a['tips_cash_ratio']:.0%} 이상 · 인건비 연 {a['loaded']:,}만원/인 가정", size=8.5, color=GREY, check=False)
    # sources vs uses bars
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, y - 0.02, rw, 0.26, '재원 vs 지출 (24개월, 억원)', size=11.5, bold=True)
    srcs = [(d['name'], d['value'], d['tag']) for d in TP['sources']]
    uses = [('TIPS 과제', TP['total']), ('과제 밖 비용', TP['non_rnd'])]
    vmax = max(TP['src_total'], TP['spend_total']); bwid = rw - 1.2; by = y + 0.42
    for row_i, (lab, parts, fills) in enumerate([('재원', [(n, v) for n, v, _ in srcs], [T['accent'], '3A3F46', 'A9AEB5']),
                                                  ('지출', uses, ['15171A', 'C9CDD2'])]):
        yy = by + row_i * 1.05
        text(s, rx, yy, 0.6, 0.42, lab, size=11, bold=True, anchor='m')
        x = rx + 0.65
        for j, (n_, v_) in enumerate(parts):
            ww = bwid * v_ / vmax
            rect(s, x, yy, ww, 0.42, fill=fills[j])
            if ww > 0.45: text(s, x, yy, ww, 0.42, f"{v_ / 1e4:.1f}", size=9.5, bold=True, color='FFFFFF' if j < (len(parts) - 1 if row_i == 0 else 1) else T['text'], align='c', anchor='m', check=False)
            text(s, x, yy + 0.45, max(ww, 0.9), 0.22, n_.replace(' (요청)', '').replace(' (M12 목표)', ''), size=7.5, color=T['text2'], check=False)
            x += ww
        tot = sum(v for _, v in parts)
        text(s, x + 0.08, yy, 0.6, 0.42, f"{tot / 1e4:.1f}", size=10.5, bold=True, anchor='m', check=False)
    ny = by + 2.25
    items = [(f"약 {TP['runway_no_followon']:.0f}개월", '후속 투자 없을 때 자금 지속', 'DERIVED'),
             (f"{a['followon'] / 1e4:.0f}억원", '후속 투자 (M12 점검 뒤)', 'TARGET')]
    nums_row(s, rx, ny, rw, items, vsize=18, lsize=9)
    text(s, rx, ny + 1.0, rw, 0.62, [f"운영사 투자 요건 (2026): 수도권 2억원 이상 · 비수도권 1억원 이상 → 요청 {a['op_invest'] / 1e4:.0f}억원",
                                      f"창업사업화 · 해외마케팅 연계 (각 최대 {TP['biz_link'] / 1e4:.1f}억원, 선정 뒤 별도 신청)는 미반영"], size=8.5, color=GREY)
    band(s, H - 1.2, [('투자유치 현황  ', {'bold': True}), ('없음 (FACT)', {}), ('     운영사 연계 계획  ', {'bold': True}), ('[운영사 협의 후 기재]', {}),
                      ('     투자 조건  ', {'bold': True}), ('[협의]', {})], size=10.5)
    mfoot(s)


MAIN = [m01, m_sum, m02, m03, m04, m05, m06, m07, m08, m11, m09, m14, m10, m12,     # IR (TIPS 별첨 6항목 순서: 문제·솔루션 / 시장 / 경쟁 / BM / 팀 / 로드맵·매출)
        m_kpi, m_plan, m_tech, m_org, m_fund]                                              # TIPS R&D 과제 요약 (본문1 항목)

# legacy constants still used by the appendix concept-model slides (slides_apx2._apt_detail)
APT = [('2', '2Bay', '후면 측부 · ㄱ자', '작은 ㄱ자 주방\n→ 키큰장 · 접이식 중심'),
       ('3', '3Bay', '후면 중앙 · 일자 + ㄱ자', '일자 작업대\n→ 레일 표준형'),
       ('4', '4Bay', '후면 중앙 · 개방형 + 아일랜드', '개방형 + 아일랜드\n→ 벽면 로봇 구역 + 아일랜드 사람 구역')]
NUDGE = {'2': {'rail': (-0.16, 0.06), 'home': (0.1, -0.1)}}
MARKS = [('sink', '싱크'), ('dw', '식기세척기'), ('ih', '인덕션'), ('storage', '수납'), ('home', '로봇 보관함'), ('rail', '레일')]
