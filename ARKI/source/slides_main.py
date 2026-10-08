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
FOOT_LEFT = 'ARKI Robotics  ·  Seed 투자 제안서  ·  Draft v3'

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

def mfoot(s, no, note=None):
    footer(s, no, left=FOOT_LEFT, note=note)

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
        kicker='SEED 투자 제안서  ·  2026.10  ·  DRAFT v3',
        title='설거지 정리를 맡는\n로봇 주방',
        sub='로봇이 일할 자리를 주방 설계 단계에서 만듭니다',
        body=['첫 기능: 식사 후 식기 정리 (식기세척기 넣기 · 꺼내기 · 수납)', '첫 시장: 구축 아파트 주방 리모델링'],
        note=('ARKI Robotics는 식사 후 설거지 정리를 맡는 로봇 주방을 만듭니다. 로봇을 사서 기존 주방에 두는 방식이 아니라, 레일과 보관함, 식기세척기와 서랍을 로봇이 쓰기 좋게 처음부터 같이 설계합니다. '
              '첫 기능은 식사 후 식기를 식기세척기에 넣고, 세척이 끝나면 꺼내서 서랍에 정리하는 일입니다. 첫 시장은 주방을 새로 시공하는 구축 아파트 리모델링입니다. '
              '현재는 Concept 단계로 시제품, 고객, 계약, LOI, 파트너, 매출이 없습니다. 오늘 자료는 Seed 자금으로 무엇을 검증할지에 대한 제안입니다.')))
    s = start(prs, 'm01', 1, c['title'].replace('\n', ' '), note=c['note'],
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
    text(s, lx, 6.5, lw, 0.5, ['Concept 단계 · 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT)',
                               '숫자는 FACT · ASSUMPTION · TARGET 등으로 구분 표기'], size=8.5, color=GREY)


# ================================================================= 02 problem
def m02(prs):
    v = M['value']
    c = cp('m02', dict(
        kicker='01  문제',
        title='식사 후 정리는 아직 사람이 합니다',
        sub='식기세척기는 씻기만 합니다. 옮기고, 넣고, 꺼내서 제자리에 두는 일은 사람 몫입니다.',
        body=['정리 시간은 아직 가정입니다. 첫 3개월에 30세대 시간 기록으로 실제 시간과 빈도를 잽니다.'],
        numbers=[{'value': '약 40분', 'label': '하루 식사 후 정리 시간', 'tag': 'ASSUMPTION'},
                 {'value': f"월 약 {v['hours']:.0f}시간", 'label': '40분 × 30일', 'tag': 'DERIVED'},
                 {'value': '1.5만원', 'label': '가사서비스 시간당 요금', 'tag': 'FACT'}],
        note=('식기세척기와 인덕션은 기기 안의 일을 자동으로 합니다. 하지만 식사 후 식기를 싱크로 옮기고, 식기세척기에 넣고, 끝나면 꺼내서 수납장에 넣는 일은 여전히 사람이 합니다. '
              'ARKI가 맡는 범위는 조리대에 놓인 식기를 집는 일부터 서랍에 정리하는 일까지입니다. 식탁에서 조리대로 옮기는 일은 첫 제품에서도 사람이 합니다. '
              '하루 40분은 가정입니다. Seed 첫 3개월에 30세대의 시간 기록으로 확인합니다.')))
    s = start(prs, 'm02', 2, c['title'], note=c['note'],
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
    mfoot(s, 2, note='시간당 1.5만원: 가사서비스 플랫폼 공개 요금 (4시간 59,900~64,900원) → 부록 F2')


# ================================================================= 03 solution
def m03(prs):
    c = cp('m03', dict(
        kicker='02  해결 방법',
        title='로봇을 들이는 대신, 로봇 자리를 주방에 만듭니다',
        sub='레일 · 보관함 · 식기세척기 · 서랍을 로봇이 쓰기 좋은 위치와 높이로 함께 설계합니다',
        body=['집마다 다른 위치 · 높이 · 동선을 로봇이 현장에서 알아내는 대신, 설계 단계에서 정해 둡니다.', '그만큼 집마다 새로 풀 문제가 줄어듭니다 (실물 미검증). 식기 인식 · 집기는 따로 검증합니다.'],
        note=('왼쪽은 기존 주방에 이동형 로봇을 들여놓은 경우입니다. 로봇이 통로를 막고, 식기세척기는 무릎 높이에, 수납은 손이 닿지 않는 위치에 있으며, 사람과 동선이 겹칩니다. '
              '이런 조건을 집마다 로봇이 현장에서 풀어야 합니다. 오른쪽은 ARKI 방식입니다. 로봇은 상부장 아래 레일에 매달려 바닥을 쓰지 않고, 식기세척기와 서랍은 로봇이 위에서 넣을 수 있게 배치합니다. '
              '로봇 작업 구역과 사람 구역을 나누고, 인덕션 같은 조리기구 구역은 로봇이 들어가지 않습니다.')))
    s = start(prs, 'm03', 3, c['title'], note=c['note'],
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
    mfoot(s, 3)


# ================================================================= 04 how it works
def m04(prs):
    c = cp('m04', dict(
        kicker='03  제품',
        title='식사 후 정리를 다섯 단계로 끝냅니다',
        sub='사람은 식기를 조리대 한쪽에 두기만 합니다. 조리 · 칼 · 불 쓰는 일은 하지 않습니다.',
        labels=['인식', '집기', '넣기', '꺼내기', '서랍 정리'],
        body=['카메라로 식기 종류 · 위치 확인', '식기 모양에 맞게 집기', '식기세척기 랙에 세워 넣기', '세척 끝난 식기 꺼내기', '로봇용 서랍에 정리'],
        numbers=[{'value': '3개 이상', 'label': '승인된 작업 수 (M12)', 'tag': 'TARGET'},
                 {'value': '70%', 'label': '정리 성공률 판단 기준 (M9)', 'tag': 'TARGET'}],
        note=('첫 제품의 일은 하나입니다. 조리대 한쪽에 놓인 식기를 인식하고, 모양에 맞게 집어서, 식기세척기 랙에 넣고, 세척이 끝나면 꺼내서 로봇용 서랍에 정리합니다. '
              '조리, 칼, 불을 쓰는 일은 범위에서 뺐습니다. 범위를 좁혀야 가정에서 믿을 수 있는 수준을 만들 수 있기 때문입니다. '
              '9개월에 정리 성공률 70%, 12개월에 승인된 작업 3개 이상이 판단 기준입니다.'),
        _lock=('labels', 'body')))
    s = start(prs, 'm04', 4, c['title'], note=c['note'],
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
    mfoot(s, 4)


# ================================================================= 05 stow / deploy / low reach
def m05(prs):
    SP = json.load(open(os.path.join(RD, 'v2_stow_3_deploy.json'), encoding='utf-8'))['ik'].get('sweep', {})
    out_cm = max(0, SP.get('zmax', 88) - 62)
    c = cp('m05', dict(
        kicker='04  보관 · 전개 · 낮은 곳',
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
              '모든 자세와 이동 경로는 3D 모델에서 충돌검사를 했고 관통은 0센티미터입니다. 실물 검증은 Seed 기간의 실물 크기 목업에서 합니다.'),
        _lock=('labels',)))
    s = start(prs, 'm05', 5, c['title'], note=c['note'],
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
    mfoot(s, 5, note='3D 모델 기준 (실물 미검증) · 로봇 링크 = 캡슐, 가구 = 상자로 충돌검사 · 경로는 관절 보간 0.015rad · 레일 이동 1cm 간격')


# ================================================================= 06 real plan
def m06(prs):
    c = cp('m06', dict(
        kicker='05  실제 평면 적용',
        title='받은 평면 그대로 3D로 옮겨, 주방 한 벽에 넣었습니다',
        sub='구축 2Bay A (코어 포함 12,390 × 11,670mm) · 주방 윗벽 3,255mm에 ARKI 한 줄 3,150mm',
        body=['인덕션은 옆 벽 아래쪽으로 옮겨 로봇 구역과 분리 · 싱크 중심 약 21cm 이동',
              '벽 3,255mm에 한 줄 3,150mm (내려놓는 곳 70cm) → 여유 10.5cm, 현장 실측 필요',
              '보관함 문은 옆 벽 때문에 90°까지만 열림 → 이 조건으로 충돌검사 다시 수행 · 나머지 평면 4종은 작업 중'],
        numbers=[{'value': '3,150mm', 'label': 'ARKI 한 줄 (벽 길이 3,255mm)', 'tag': 'CONCEPT'},
                 {'value': '0cm', 'label': '작업 · 보관 · 이동 경로 관통 (3D 단순 모델)', 'tag': 'CONCEPT'}],
        note=('받은 평면 중 구축 2Bay 평면 하나를 치수 그대로 3D로 만들었습니다. 오른쪽 그림이 그 주방입니다. '
              '주방 윗벽은 왼쪽 벽에서 침실 문까지 3,255밀리미터이고, 여기에 보관함, 내려놓는 곳, 싱크, 서랍, 식기세척기로 된 ARKI 한 줄 3,150밀리미터를 넣었습니다. '
              '원래 왼쪽 벽에 있던 조리대는 아래쪽으로 줄이고 인덕션을 옮겨 로봇 구역과 분리했습니다. 싱크 중심은 약 21센티미터 옮겨집니다. '
              '보관함 문은 옆 벽 때문에 90도까지만 열리는데, 이 조건으로 작업 자세와 보관, 이동 경로를 다시 충돌검사했고 관통은 0센티미터입니다. '
              '나머지 평면 4종은 같은 방법으로 작업 중이며 부록에 정리합니다.')))
    s = start(prs, 'm06', 6, c['title'], note=c['note'],
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
    mfoot(s, 6, note='평면: 사용자 제공 도면을 치수선 기준으로 디지털화 (특정 단지명 표기 안 함) · 부록 B6~B10')


# ================================================================= 07 standard module
def m07(prs):
    smr = inp('smr'); kc = B('kit_unit_cost')
    c = cp('m07', dict(
        kicker='06  표준화',
        title='평면이 달라도 같은 한 줄 모듈을 쓰는 것이 목표입니다',
        sub='순서와 치수는 고정하고 폭 · 문 열림각 · 조리기구 위치만 맞춥니다. 지금은 평면 1종에 적용, 30개 분석으로 확인합니다.',
        table=[['바뀌는 것', '범위', '예: 구축 2Bay A'], ['내려놓는 곳 폭', '70 ~ 80cm', '70cm'], ['보관함 문 열림각', '90 ~ 105°', '90° (옆 벽)'],
               ['조리기구 위치', '옆 벽 · 아일랜드', '옆 벽 아래쪽'], ['마감재 · 상부장', '현장 선택', '기존 톤']],
        numbers=[{'value': '30개 → 3~5개', 'label': '평면 분석 → 주방 표준안', 'tag': 'TARGET'},
                 {'value': f"{kc[0]:.0f} → {kc[4]:.0f}만원", 'label': f"세대당 주방 모듈 원가 (표준 모듈 사용률 {pct(smr[0])} → {pct(smr[4])})", 'tag': 'DERIVED'},
                 {'value': '60%', 'label': 'M18 표준 모듈 사용률 기준', 'tag': 'TARGET'}],
        note=('집마다 주방이 다르면 결국 인테리어 회사가 아니냐는 질문에 대한 답입니다. ARKI는 보관함, 내려놓는 곳, 싱크, 서랍, 식기세척기의 순서와 치수를 고정한 한 줄 모듈을 씁니다. '
              '평면마다 바뀌는 것은 내려놓는 곳의 폭, 보관함 문이 열리는 각도, 조리기구 위치, 마감재 정도입니다. 앞 장의 구축 2Bay 평면도 이 범위 안에서 맞췄습니다. '
              'Seed 기간에 평면 30개를 분석해 주방 표준안 3~5개로 묶는 것이 목표입니다. 표준 모듈 사용률이 40%에서 80%로 오르면 세대당 주방 모듈 원가가 332만원에서 244만원으로 내려가도록 재무모델에 연결했습니다. '
              '18개월에 사용률 60%를 못 넘으면 표준화 방식을 다시 봅니다.'),
        _lock=('table',)))
    s = start(prs, 'm07', 7, c['title'], note=c['note'],
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
    mfoot(s, 7)


# ================================================================= 08 market
def m08(prs):
    mk = M['market']['B']
    c = cp('m08', dict(
        kicker='07  시장',
        title='첫 시장은 주방을 새로 하는 구축 아파트입니다',
        sub='해마다 약 30만 세대가 주방을 바꾸고, 그중 연 1.8만 세대를 적용 가능 시장으로 봅니다',
        numbers=[{'value': f"연 약 {mk['sam']:,.0f}억원", 'label': f"적용 가능 시장 (구축 {mk['sam_remodel']:,.0f} + 신축 {mk['sam_new']:,.0f})", 'tag': 'DERIVED'},
                 {'value': f"약 {mk['som_share_hh'] * 100:.0f}%", 'label': f"Y5 계획 물량 / 적용 가능 세대 (Y5 매출 {mk['som']:.1f}억원 기준)", 'tag': 'TARGET'}],
        body=['비율(교체 30만 · 프리미엄 10% · 적용 60%)은 가정 → Seed 기간 조사로 확인', '대중 시장 진입은 계획에 넣지 않음'],
        note=('시장은 큰 숫자보다 실제로 살 수 있는 세대 수부터 셉니다. 아파트는 약 1,328만호이고, 준공 20년 이상 주택이 56%입니다. '
              '해마다 주방을 바꾸는 아파트는 두 가지 방법으로 추정해 약 30만 세대로 봤습니다. 그중 주방 예산 2천만원 이상인 프리미엄 10%, 다시 구조상 적용이 가능한 60%를 가정하면 연 1.8만 세대입니다. '
              '금액으로는 구축 약 3,212억원에 신축 약 184억원을 더해 연 약 3,396억원입니다. 신축은 세대당 옵션 220만원에 입주자 25%가 로봇을 사는 것으로 가정했습니다. 5년차 계획 물량은 적용 가능 세대의 약 2%입니다. 비율은 모두 가정이고 Seed 기간에 확인합니다. 참고로 준공 20년 이상 주택 56%는 전체 주택 기준이라 깔때기 단계로 쓰지 않았습니다.')))
    s = start(prs, 'm08', 8, c['title'], note=c['note'],
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
    mfoot(s, 8)


# ================================================================= 09 business model
def m09(prs):
    a = {d['key']: d['vals']['B'] for d in M['inputs']}; hh = M['household']['purchase_direct_Y3']; rn = M['rental']; v = M['value']
    c = cp('m09', dict(
        kicker='08  수익 구조',
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
    s = start(prs, 'm09', 9, c['title'], note=c['note'],
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
    mfoot(s, 9)


# ================================================================= 10 go to market
def m10(prs):
    rd, rp, ni = inp('rd'), inp('rp'), B('ni'); bl = B('backlog')
    c = cp('m10', dict(
        kicker='09  판매 방법',
        title='직접 팔며 배우고, 파트너로 늘리고, 신축 옵션으로 키웁니다',
        sub='직접판매로 가격 · 설치 · 사용을 확인하고, 파트너 판매와 신축 옵션으로 물량을 늘립니다',
        numbers=[{'value': '9.7%', 'label': '신축 유상옵션 / 분양가 (공개 7개 단지 평균, 보도 인용)', 'tag': 'FACT'},
                 {'value': '약 2년', 'label': '옵션 계약 → 입주', 'tag': 'ASSUMPTION'},
                 {'value': f"{bl[4]:.0f}세대", 'label': 'Y5 말 신축 대기 물량', 'tag': 'DERIVED'}],
        note=('판매는 세 단계입니다. 처음 2년은 직접 판매로 리모델링 고객을 만나 가격, 설치, 실제 사용을 배웁니다. 직접 판매의 고객 획득비는 세대당 150만원으로 가정했습니다. '
              '3년차부터는 인테리어와 주방가구 회사를 통해 판매하고 패키지의 10%를 수수료로 줍니다. 신축은 건설사 설계 단계에 옵션으로 들어가는데, 계약에서 입주까지 약 2년이 걸려 5년차부터 설치가 반영되고, 5년차 말 대기 물량은 400세대입니다. '
              '그래서 Seed와 Series A 기간의 매출과 검증은 구축이 맡습니다.')))
    s = start(prs, 'm10', 10, c['title'], note=c['note'],
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
    mfoot(s, 10, note='Y2 5세대는 실증 할인 50% · 렌탈 30% 가정 → Y2 매출 0.4억원 (산식: 재무모델 xlsx · 부록 D9)')


# ================================================================= 11 competition
def m11(prs):
    c = cp('m11', dict(
        kicker='10  경쟁 · 차별점',
        title='가전은 기기 안만, 범용 로봇은 집마다 새로 배워야 합니다',
        sub='ARKI는 공간과 로봇을 같이 설계합니다. 이 방식이 더 낫다는 것은 아직 검증 전입니다.',
        table=[['공개 사례', '방식', '공개 내용 (보도 기준)'],
               ['1X NEO', '가정용 휴머노이드', '2만 달러 또는 월 499달러 · 2026 출하 발표'],
               ['LG CLOiD', '가정용 로봇', 'CES 2026 식기세척기 비우기 시연'],
               ['Moley Robotic Kitchen', '로봇 주방 (조리)', '팔 포함 £248,000'],
               ['Samsung Bot Chef', '레일형 로봇 팔', 'CES 2020 콘셉트'],
               ['Sunday Memo', '가정용 로봇', '2026 베타']],
        body=['평면 데이터 → 주방 표준안 3~5개', '설치비 · 설치 시간 검증 데이터', '가구 · 인테리어 파트너 실증 협의', '특허 출원 5~8건 (등록 미정)'],
        note=('경쟁은 접근 방식으로 봅니다. 가전 회사는 식기세척기와 인덕션 안의 일을 자동화하지만, 기기 사이에서 식기를 옮기고 정리하는 일은 남습니다. '
              '범용 로봇과 휴머노이드는 기존 집에 로봇이 적응하는 방식입니다. 1X는 NEO를 2만 달러 또는 월 499달러에 내놓겠다고 발표했고, LG는 CES 2026에서 식기세척기를 비우는 로봇을 시연했습니다. '
              'LG CLOiD가 시연한 식기세척기 비우기는 저희 첫 기능과 같은 작업입니다. 같은 작업에서 저희 방식이 나은지는 아직 검증하지 않았습니다. ARKI는 공간과 로봇을 같이 설계해 로봇이 집마다 풀어야 할 문제를 줄이는 쪽입니다. 다만 이 방식이 더 낫다는 것은 아직 검증 전이고, 주방가구 회사가 같은 일을 직접 할 위험도 있습니다. '
              '진입장벽은 지금 있는 것이 아니라 쌓아야 할 것입니다. 평면 데이터와 표준안, 설치 데이터, 파트너, 특허 출원입니다.'),
        _lock=('table',)))
    s = start(prs, 'm11', 11, c['title'], note=c['note'],
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
    mfoot(s, 11)


# ================================================================= 12 financials
def m12(prs):
    sc = M['scenarios']; Bv = sc['B']
    rev = [v / 10000 for v in Bv['rev']]; op = [v / 10000 for v in Bv['op']]; gm = Bv['gm']
    c = cp('m12', dict(
        kicker='11  재무 계획',
        title='5년차 매출 77.6억원, 손익분기는 6년차 이후입니다',
        sub='5년 누적 현금 최저 약 -128억원 → 단계마다 검증 후 다음 투자를 받는 계획입니다',
        numbers=[{'value': f"연 약 {M['breakeven_kitchens']:,.0f}세대", 'label': '손익분기 설치 물량 (Y5 단가 · 원가)', 'tag': 'DERIVED'},
                 {'value': f"약 {min(Bv['cum_cash']) / 10000:.0f}억원", 'label': '5년 누적 현금 최저', 'tag': 'DERIVED'},
                 {'value': f"{gm[4]:.0%}", 'label': 'Y5 매출총이익률 (Y2 -75%)', 'tag': 'DERIVED'}],
        note=('기본 시나리오의 매출은 1년차 0, 2년차 0.4억, 3년차 7.5억, 4년차 32.5억, 5년차 77.6억원입니다. 영업이익은 5년 내내 적자이고, 5년 누적 현금은 최저 약 마이너스 128억원입니다. '
              '연간 약 1,340세대를 설치해야 손익분기에 도달하므로 6년차 이후입니다. 보수 시나리오의 5년차 매출은 27.8억, 상향은 134억원입니다. '
              '즉 이 사업은 단계마다 검증을 통과해야 다음 투자를 받을 수 있는 구조이고, Seed는 그 첫 검증 비용입니다.')))
    s = start(prs, 'm12', 12, c['title'], note=c['note'],
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
    mfoot(s, 12, note='Y2 매출 0.4억원 = 5세대 (실증 할인 50% · 렌탈 30% 가정) · 산식은 재무모델 xlsx · 부록 D9')


# ================================================================= 13 milestones / stop rules
def m13(prs):
    c = cp('m13', dict(
        kicker='12  일정 · 중단 기준',
        title='24개월 동안 다섯 번 점검하고, 기준에 못 미치면 바꾸거나 멈춥니다',
        sub='자금을 다 쓰기 전에 실패를 확인할 수 있게 점검 시점과 기준을 미리 정했습니다',
        table=[['M6', '실물 크기 목업', '사람 동선과 로봇 동작범위가 함께 성립', '구조 변경'],
               ['M9', '정리 성공률', '70% 이상', '작업 범위 축소'],
               ['M12', '지불의사', '중앙값이 목표가의 60% 이상', 'B2C 재검토'],
               ['M18', '표준 모듈', '사용률 60% 이상', '표준화 재검토'],
               ['M24', '유료 실증 · 파트너', '유료 실증 · 파트너 협의 성사', '확장 투자 보류']],
        body=['실물 크기 목업 2식', '평면 30개 분석 → 주방 표준안 3~5개', '승인된 작업 3개 이상', '인터뷰 50명 · 지불의사 조사 n ≥ 300',
              '가정 실증 3~5세대 (유료 포함)', '검증된 BOM · 설치비 · 설치 시간', '관리 · 소모품 원가 실측', '주방가구 · 인테리어 파트너 실증 협의', '특허 출원 5~8건'],
        note=('Seed 24개월의 목표는 완성품이 아니라 Series A가 판단할 수 있는 증거입니다. 6개월에 실물 크기 목업에서 사람 동선과 로봇 동작범위가 함께 성립하는지, 9개월에 정리 성공률, 12개월에 지불의사, 18개월에 표준 모듈 사용률, 24개월에 유료 실증과 파트너를 봅니다. '
              '각 시점에 기준을 넘지 못하면 구조를 바꾸거나, 범위를 줄이거나, 확장 투자를 보류합니다. 오른쪽은 24개월 뒤에 남길 결과물 목록입니다.'),
        _lock=('table', 'body')))
    s = start(prs, 'm13', 13, c['title'], note=c['note'],
              visual='M0~M24 시간축에 점검 5개 (위: 무엇을 보나 / 기준, 아래: 못 넘으면). 오른쪽: 24개월 결과물 9개.',
              chart='시간축 + 중단 기준')
    mhead(s, c['kicker'], c['title'], c['sub'])
    lw = 8.4; n = 5; cw = (lw - (n - 1) * 0.12) / n; top = 2.0; ay = 3.95
    seg(s, MX, ay, MX + lw, ay, color=T['text'], lw=1.5)
    for i, (m_, a, crit, kill) in enumerate(c['table'][:5]):
        cx = MX + i * (cw + 0.12); mid = cx + cw / 2
        rect(s, cx, top, cw, 1.6, fill=T['soft'])
        text(s, cx + 0.12, top + 0.08, cw - 0.24, 0.3, m_, size=14, bold=True, color=T['accent'])
        text(s, cx + 0.12, top + 0.42, cw - 0.24, 0.3, a, size=11, bold=True)
        text(s, cx + 0.12, top + 0.74, cw - 0.24, 0.8, crit, size=9.5, color=T['text2'], line=1.0)
        seg(s, mid, top + 1.6, mid, ay, color=GREY, lw=0.75); dot(s, mid, ay, 0.16, fill=T['text'])
        seg(s, mid, ay, mid, ay + 0.25, color=GREY, lw=0.75)
        rect(s, cx, ay + 0.25, cw, 0.92, line=T['text'], lw=0.9)
        text(s, cx + 0.12, ay + 0.31, cw - 0.24, 0.24, '못 넘으면', size=8.5, bold=True, color=GREY)
        text(s, cx + 0.12, ay + 0.55, cw - 0.24, 0.56, kill, size=10.5, bold=True, line=1.0)
    mts(s, MX, ay + 1.3, ['TARGET'])
    text(s, MX + 0.7, ay + 1.27, lw - 0.8, 0.24, '모든 기준 = Seed 투자 후 측정할 목표', size=8.5, color=GREY, check=False)
    rx = MX + lw + 0.4; rw = W - MX - rx
    rect(s, rx, top, rw, 3.6, fill=T['text'])
    text(s, rx + 0.2, top + 0.12, rw - 0.4, 0.3, '24개월 결과물 → Series A', size=12, bold=True, color='FFFFFF')
    text(s, rx + 0.2, top + 0.52, rw - 0.4, 3.0, c['body'][:9], size=9.5, color='E2E4E7', bullet='–', bullet_color='8C9198', space_after=2, line=1.0)
    band(s, 6.2, [('자금 기간  ', {'bold': True}), ('24개월 계획은 재산정 25.8억원 기준 · 20억원만으로는 약 19개월 → M18 이후 점검은 TIPS 연계 또는 브리지 전제 (DERIVED)', {})], size=10.5)
    mfoot(s, 13, note='M12 목표가 = 설치 시점 약 2,020만원 또는 렌탈 월 33만원 (ASSUMPTION) · 지금: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음')


# ================================================================= 14 team
def m14(prs):
    c = cp('m14', dict(
        kicker='13  팀',
        title='Seed 판단의 첫 질문은 팀이고, 그 칸은 아직 비어 있습니다',
        sub='필요한 역량은 로봇 조작, 주방 · 건축 시공, 고객 · 파트너 영업 세 가지입니다',
        note=('창업자 정보는 받지 못해 비워 두었습니다. 투자 판단에서 가장 중요한 칸이 비어 있다는 점을 그대로 보여드립니다. '
              'ARKI에 필요한 역량은 세 가지입니다. 식기를 집고 옮기는 로봇 조작, 주방가구와 건축 시공을 함께 설계하는 능력, 리모델링 고객과 가구 회사, 건설사를 상대하는 영업입니다. '
              '창업팀이 이 세 가지를 직접 갖고 있는지가 첫 질문이고, 부족한 역량은 첫 6개월 채용과 자문으로 보완합니다.')))
    s = start(prs, 'm14', 14, c['title'], note=c['note'],
              visual='3열 역량 카드 (로봇 조작 · 주방/건축 시공 · 고객/파트너 영업), 각 카드 창업팀 보유 = [Founder 정보 필요]. 아래 창업자 7항목 (미입력) + 채용 순서.',
              chart='역량 카드 + 채용 순서')
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
    ty = 4.2; lw = 5.0
    text(s, MX, ty, lw, 0.28, '창업자 확인 항목 (7) — 모두 미입력', size=11.5, bold=True)
    fi = ['학력 · 경력', '엔지니어링 경험', '제품 개발 경험', '건설 · 주방 이해', '로봇 경험', '고객 · 파트너 네트워크', '전업 여부']
    for j, f in enumerate(fi):
        fx = MX + (j % 2) * (lw / 2); fy = ty + 0.4 + (j // 2) * 0.38
        text(s, fx, fy, lw / 2 - 0.1, 0.32, [[('□  ', {'color': GREY}), (f, {})]], size=10, anchor='m')
    mt(s, MX, ty + 2.0, 'TBV', label='[Founder 정보 필요]')
    rx = MX + lw + 0.4; rw = W - MX - rx
    text(s, rx, ty, rw, 0.28, '채용 순서 (평균 인원 Y1 6명 → Y2 9명)', size=11.5, bold=True)
    mts(s, rx + 4.0, ty + 0.05, ['ASSUMPTION'])
    hires = [('M0', '로봇 리드 · 주방/건축 통합 리드'), ('M0~M3', '비전 · ML · 메카트로닉스 (레일 · 그리퍼)'), ('M3~M6', '임베디드 · 전기 · 안전'),
             ('M6', '사업개발 · 고객 조사'), ('M12', '현장 설치 엔지니어')]
    for j, (when, who) in enumerate(hires):
        hy = ty + 0.42 + j * 0.36
        text(s, rx, hy, 0.85, 0.32, when, size=10, bold=True, anchor='m')
        text(s, rx + 0.9, hy, rw - 0.9, 0.32, who, size=10, color=T['text2'], anchor='m')
        hline(s, rx, hy + 0.34, rw)
    text(s, rx, ty + 2.3, rw, 0.5, '자문: 주방가구 제조 · 시공 / 건설사 유상옵션 / 로봇 안전인증 (ISO 10218 · ISO 13482 · KC) / 렌탈 금융', size=9.5, color=T['text2'])
    mfoot(s, 14)


# ================================================================= 15 ask
def m15(prs):
    F = M['funds']; rev = dict(F['revised'])
    c = cp('m15', dict(
        kicker='14  투자 요청',
        title='Seed 20억원을 요청합니다. 24개월 검증에는 25.8억원이 필요합니다',
        sub=f"20억원만으로는 약 {F['months_equity_only']:.0f}개월 → 부족분 {F['gap_vs_seed'] / 10000:.1f}억원은 TIPS 연계 또는 증액으로 채웁니다",
        numbers=[{'value': '20억원', 'label': 'Seed 요청액', 'tag': 'ASSUMPTION'},
                 {'value': f"{F['revised_total'] / 10000:.1f}억원", 'label': f"재산정 필요액 (부족 {F['gap_vs_seed'] / 10000:.1f}억원)", 'tag': 'DERIVED'},
                 {'value': f"약 {F['months_equity_only']:.0f}개월", 'label': '20억원만으로 운영 가능한 기간', 'tag': 'DERIVED'}],
        body=['부족분 5.8억원을 채우는 방법', '안 A  TIPS R&D 최대 8억원 연계 (선정 미확정)', '안 B  Seed 25억원 (예비비 일부 조정) 또는 M18 브리지'],
        note=(f"요청 금액은 Seed 20억원, 기간은 24개월입니다. 이 자금은 완성된 로봇 주방을 파는 데가 아니라, 앞에서 말씀드린 가설을 검증하는 데 씁니다. "
              f"실제 인건비와 시제품, 목업 공간, 인증 비용으로 다시 계산하면 약 {F['revised_total'] / 10000:.1f}억원이 필요하고, 20억원만으로는 약 {F['months_equity_only']:.0f}개월을 버팁니다. "
              '그래서 TIPS R&D 최대 8억원 연계를 기본안으로 제안하고, 선정되지 않으면 Seed 증액이나 18개월 시점 브리지가 필요합니다. '
              '현재는 Concept 단계로 시제품, 고객, 파트너, 매출이 없습니다.')))
    s = start(prs, 'm15', 15, c['title'], note=c['note'],
              visual='왼쪽: 20억원 · 24개월 + 재산정 25.8억원 · 부족분 · 대안 2개. 오른쪽: 자금 용도 가로 막대 (재산정 기준) + 항목 목록.',
              chart='핵심 숫자 + 자금 용도 막대')
    mhead(s, c['kicker'], c['title'], c['sub'])
    ly = 2.05
    n0 = c['numbers'][0]
    text(s, MX, ly - 0.05, 3.2, 1.0, n0['value'], size=50, bold=True, color=T['accent'])
    text(s, MX + 3.2, ly + 0.42, 2.6, 0.4, n0['label'], size=16, bold=True)
    text(s, MX + 3.2, ly + 0.82, 2.6, 0.22, '당초 24개월 계획 기준', size=9, color=GREY, check=False)
    mts(s, MX + 3.2, ly + 1.06, [n0['tag']])
    items = [(n['value'], n['label'], n['tag']) for n in c['numbers'][1:3]]
    nums_row(s, MX, ly + 1.35, 5.6, items, vsize=20, lsize=9.5)
    text(s, MX, ly + 2.5, 5.6, 1.0, [[(c['body'][0], {'color': GREY, 'size': 9.5})]] + c['body'][1:3], size=11, bold=True, space_after=4)
    rx = MX + 6.2; rw = W - MX - rx
    text(s, rx, ly, rw, 0.28, f"자금 용도 — 재산정 {F['revised_total'] / 10000:.1f}억원 기준 (DERIVED)", size=11.5, bold=True)
    parts = [('핵심 개발팀', rev['Core Development Team']), ('로봇 · 주방 시제품', rev['Robot / Kitchen Prototype']), ('목업 · 설치 개발', rev['Mock-up / Installation Development']),
             ('실증 · 고객 검증', rev['Pilot / Customer Validation']), ('비전 · SW · 데이터', rev['Vision / Software / Data']), ('안전 · 인증 · 특허', rev['Safety / Certification / IP']),
             ('운영 (관리비)', rev['Operations (G&A)']), ('예비비 (10%)', rev['Contingency (10%)'])]
    tot = sum(v for _, v in parts); x = rx; bh = 0.46; yb = ly + 0.4
    fills = ['15171A', '3A3F46', '5A5F67', '7A7F87', '9AA0A7', 'B4B8BE', 'CDD1D5', 'E2E4E7']
    for i, (lab, v) in enumerate(parts):
        ww = rw * v / tot
        rect(s, x, yb, ww, bh, fill=fills[i])
        if ww > 0.5: text(s, x, yb, ww, bh, f"{v / 10000:.1f}", size=9, bold=True, color='FFFFFF' if i < 4 else T['text'], align='c', anchor='m', check=False)
        x += ww
    for i, (lab, v) in enumerate(parts):
        lx_ = rx + (i % 2) * (rw / 2); ly_ = yb + bh + 0.18 + (i // 2) * 0.34
        rect(s, lx_, ly_ + 0.08, 0.15, 0.15, fill=fills[i])
        text(s, lx_ + 0.22, ly_, rw / 2 - 0.3, 0.3, f"{lab}  {v / 10000:.1f}억", size=10, anchor='m', check=False)
    band(s, 6.2, [('지금  ', {'bold': True}), ('Concept 단계 · 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음', {}), ('      →      M24  ', {'bold': True}), ('Series A 판단 자료 (13쪽 결과물)', {})], size=11)
    mfoot(s, 15, note='투자 조건 (형태 · 기업가치 · 지분) · 연락처: [입력 필요]')


MAIN = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, m12, m13, m14, m15]

# legacy constants still used by the appendix concept-model slides (slides_apx2._apt_detail)
APT = [('2', '2Bay', '후면 측부 · ㄱ자', '작은 ㄱ자 주방\n→ 키큰장 · 접이식 중심'),
       ('3', '3Bay', '후면 중앙 · 일자 + ㄱ자', '일자 작업대\n→ 레일 표준형'),
       ('4', '4Bay', '후면 중앙 · 개방형 + 아일랜드', '개방형 + 아일랜드\n→ 벽면 로봇 구역 + 아일랜드 사람 구역')]
NUDGE = {'2': {'rail': (-0.16, 0.06), 'home': (0.1, -0.1)}}
MARKS = [('sink', '싱크'), ('dw', '식기세척기'), ('ih', '인덕션'), ('storage', '수납'), ('home', '로봇 보관함'), ('rail', '레일')]
