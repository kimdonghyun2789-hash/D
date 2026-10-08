# Shared helpers for the MH Robotics deck slides (layout idioms, number formats, slide metadata for the docs).
import os, json
import kit
from kit import (T, W, H, MX, CW, text, rect, hline, vline, table, chip, arrow, dashed_rect, tag, tags, alpha,
                 text_h, notes, new_slide, footer, header, ttxt, column_chart, bar_chart, dot)
from pptx.enum.shapes import MSO_SHAPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
OUTPUT = os.path.join(ROOT, 'MH_Robotics_Seed_TIPS_IR_Final.pptx')            # 제출용: 본문 + 부록
PREVIEW = os.path.join(ROOT, 'MH_Robotics_Seed_TIPS_IR_Final.pdf')
MAIN_PDF = os.path.join(ROOT, 'MH_Robotics_Seed_TIPS_IR_Final_Main.pdf')       # 본문만
INTERNAL = os.path.join(ROOT, 'MH_Robotics_IR_Internal_QA.pptx')              # 내부 검토용 (제출 제외)
INTERNAL_PDF = os.path.join(ROOT, 'MH_Robotics_IR_Internal_QA.pdf')
M = {}
META = []          # one dict per slide, in deck order

def load():
    M.update(json.load(open(os.path.join(HERE, 'model.json'), encoding='utf-8')))
    M['src'] = json.load(open(os.path.join(HERE, 'sources.json'), encoding='utf-8'))
    return M

# ---------------------------------------------------------------- numbers
def eok(v, d=1):          # 만원 -> 억원
    return f"{v / 10000:,.{d}f}억원"

def eokn(v, d=1):
    return f"{v / 10000:,.{d}f}"

def man(v, d=0):
    return f"{v:,.{d}f}만원"

def mann(v, d=0):
    return f"{v:,.{d}f}"

def pct(v, d=0):
    return f"{v * 100:.{d}f}%"

def B(k):
    return M['scenarios']['B'][k]

def inp(key, s='B'):
    for d in M['inputs']:
        if d['key'] == key: return d['vals'][s]
    raise KeyError(key)

# ---------------------------------------------------------------- slide scaffolding
# ---------------------------------------------------------------- appendix mode (v2 deck: legacy slides re-coded A~F)
APX = {'on': False, 'pack': 'main'}      # pack: main | appendix | internal
SECTION = {'A': 'TIPS 과제 상세', 'B': '제품 · 기술', 'C': '시장 · 경쟁', 'D': '경제성 · 재무',
           'E': 'IP · 리스크', 'F': '출처', 'I': '내부 검토용 (제출 제외)'}
SID2CODE = {   # legacy main-slide ids and old appendix codes -> v2 appendix codes
    'thesis': 'A1', 'proof': 'A2', 'integration': 'B1', 'system': 'B2', 'product': 'B3', 'architecture': 'B4',
    'layouts': 'B7', 'housing': 'B8', 'standard': 'B9', 'robotready': 'B11', 'channels': 'C4', 'market': 'C3',
    'gtm': 'C5', 'competition': 'C6', 'pricing': 'D1', 'household': 'D2', 'bm': 'D3', 'unit': 'D4', 'moat': 'E1',
    'milestone': 'E3',
    'A1': 'F1', 'A2': 'C1', 'A3': 'C2', 'A4': 'D5', 'A5': 'B10', 'A6': 'B12', 'A7': 'B13', 'A8': 'B14', 'A9': 'C7',
    'A10': 'E2', 'A11': 'D6', 'A12': 'D7', 'A13': 'D8', 'A14': 'D9', 'A15': 'D10', 'A16': 'D11', 'A17': 'C8',
    'A18': 'A3', 'A19': 'E4', 'A20': 'E5', 'A21': 'E6', 'A22': 'A4', 'A23': 'F2'}
OLD_MAIN = {1: '01', 2: 'A1', 3: 'A2', 4: '02', 5: 'B1', 6: 'B8', 7: 'B2', 8: 'B3', 9: 'B4', 10: 'B7', 11: 'B9',
            12: 'C4', 13: 'B11', 14: 'D1', 15: 'D2', 16: 'D3', 17: 'D4', 18: 'C3', 19: 'C5', 20: 'C6', 21: 'E1',
            22: 'E3', 23: '14', 24: '15'}

def remap(t):
    """Rewrite v1 cross-references ("A16", "(16·19장)", "09장 #07") to v2 codes."""
    import re
    def a_sub(m):
        a = SID2CODE.get('A' + m.group(1), 'A' + m.group(1))
        return a + ('~' + SID2CODE.get('A' + m.group(2), m.group(2)) if m.group(2) else '')
    t = re.sub(r'(?<![A-Za-z0-9#])A(\d{1,2})(?:~(\d{1,2}))?(?![0-9A-Fa-f]{3}|\d)', a_sub, t)
    def ch_sub(m):
        outs = [OLD_MAIN.get(int(n), n) for n in m.group(1).split('·')]
        return ' · '.join(o + '장' if o.isdigit() else o for o in outs)
    return re.sub(r'(?<!\d)(\d{1,2}(?:·\d{1,2})*)장', ch_sub, t)

def _legacy_text(t):
    from glossary import plain
    return plain(remap(t))

def start(prs, sid, no, title, q=None, visual='', chart='', note='', bg=None):
    """New slide + metadata record. q = list of investor questions (1..6) the slide answers."""
    legacy = APX['on'] and sid in SID2CODE
    if APX['on']:
        no = SID2CODE.get(sid, no); q = []
    kit.XFORM['fn'] = _legacy_text if legacy else None
    if legacy: note, visual, title = _legacy_text(note), _legacy_text(visual), _legacy_text(title)
    s = new_slide(prs, sid, bg=bg)
    META.append(dict(id=sid, no=no, title=title, q=q or [], visual=visual, chart=chart, note=note, pack=APX.get('pack', 'main')))
    if note: notes(s, note)
    return s

def head(s, section, title, sub=None, q=None, size=26):
    """Section label (+ question chips) + headline. Returns y below."""
    if q is None and META: q = META[-1]['q']
    y = 0.55
    if APX['on']:
        code = str(META[-1]['no']); q = []
        lab = 'INTERNAL' if APX.get('pack') == 'internal' else 'APPENDIX'
        sec_code = len(code) > 1 and code[0] in SECTION and code[1].isdigit()     # 'A1' · 'I0' (not 'Index')
        section = f"{lab} {code}  ·  {SECTION[code[0]]}" if sec_code else section
    text(s, MX, y, 7.5, 0.28, section, size=11, bold=True, color=T['muted'] if APX['on'] else T['accent'], label='section')
    if q:
        x = W - MX
        labs = [f'Q{n}' for n in q]
        for lab in reversed(labs):
            w = 0.42; x -= w
            rect(s, x, y + 0.02, w - 0.06, 0.24, line=T['grey_bar'], lw=0.5)
            text(s, x, y + 0.02, w - 0.06, 0.24, lab, size=9, bold=True, color=T['text2'], align='c', anchor='m', check=False)
    y += 0.38
    nl = title.count('\n') + 1
    th = nl * size * kit.LH * 0.95 / 72
    text(s, MX, y, CW, th + 0.02, title, size=size, bold=True, line=0.95, label='title:' + title[:12])
    y += th + 0.1
    if sub:
        sh = text_h(sub, 13, CW)
        text(s, MX, y, CW, sh + 0.02, sub, size=13, color=T['text2'], label='sub:' + sub[:12])
        y += sh + 0.05
    return y + 0.12

def foot(s, page, note=None):
    if APX['on']:
        left = 'MH Robotics  ·  내부 검토용 (제출 제외)' if APX.get('pack') == 'internal' else 'MH Robotics  ·  Seed · TIPS IR  ·  부록'
        footer(s, META[-1]['no'], left=left, note=note)
    else:
        footer(s, page, note=note)

def note_line(s, txt, y=None, size=10, color=None):
    hh = text_h(txt, size, CW)
    yy = y if y is not None else H - 0.62 - hh
    text(s, MX, yy, CW, hh + 0.02, txt, size=size, color=color or T['muted'], label='footnote')
    return yy

def statement(s, x, y, w, txt, size=15, h=None, fill=None, color=None, bold=True):
    """Accent-bar statement block (single key message)."""
    hh = h or text_h(txt, size, w - 0.35, bold=bold) + 0.24
    rect(s, x, y, w, hh, fill=fill or T['soft'])
    rect(s, x, y, 0.06, hh, fill=T['text'])      # ink bar: orange is reserved for robot zone · path · key numbers
    text(s, x + 0.22, y, w - 0.32, hh, txt, size=size, bold=bold, color=color or T['text'], anchor='m', label='stmt')
    return hh

def card(s, x, y, w, h, title, body, tag_kinds=None, size=11, title_size=13, fill=None, line=None, body_color=None,
         bullet=None, accent_top=False):
    rect(s, x, y, w, h, fill=fill or T['soft'], line=line)
    if accent_top: rect(s, x, y, w, 0.05, fill=T['accent'])
    yy = y + 0.14
    th = text_h(title, title_size, w - 0.3, bold=True)
    text(s, x + 0.15, yy, w - 0.3, th + 0.02, title, size=title_size, bold=True, label='card:' + title[:10])
    yy += th + 0.06
    if tag_kinds:
        tags(s, x + 0.15, yy, tag_kinds); yy += 0.28
    if body:
        bh = y + h - yy - 0.08
        text(s, x + 0.15, yy, w - 0.3, bh, body, size=size, color=body_color or T['text2'], line=1.0,
             bullet=bullet, space_after=2, label='cardbody:' + title[:10])

def flow(s, x, y, w, items, h=0.62, gap=0.28, size=11, fills=None, colors=None, bold=True):
    """Horizontal chain of equal boxes with arrows."""
    n = len(items); bw = (w - gap * (n - 1)) / n
    for i, it in enumerate(items):
        bx = x + i * (bw + gap)
        fill = (fills[i] if fills else T['soft'])
        col = (colors[i] if colors else T['text'])
        chip(s, bx, y, bw, h, it, fill=fill, color=col, size=size, bold=bold)
        if i < n - 1:
            arrow(s, bx + bw + 0.03, y + h / 2, bx + bw + gap - 0.03, y + h / 2, color=T['muted'])
    return bw

def tag_legend(s, x, y, kinds=('FACT', 'DERIVED', 'ASSUMPTION', 'TARGET')):
    return tags(s, x, y, kinds)

def kpi(s, x, y, w, value, label, tag_kind=None, vsize=24, lsize=10, vcolor=None):
    text(s, x, y, w, 0.45, value, size=vsize, bold=True, color=vcolor or T['text'], label='kpi ' + value)
    text(s, x, y + vsize / 72 * 1.45, w, 0.5, label, size=lsize, color=T['text2'], label='kpil ' + label[:10])
    if tag_kind:
        tag(s, x, y + vsize / 72 * 1.45 + text_h(label, lsize, w) + 0.04, tag_kind)

def table_slide(prs, sid, no, section, title, header_row, rows, col_w, sub=None, q=None, size=10, note='', visual='',
                chart='', foot_note=None, takeaway=None, align=None, max_h=None, pad=0.06):
    s = start(prs, sid, no, title, q=q, visual=visual or '표 중심 Appendix', chart=chart, note=note)
    y = head(s, section, title, sub=sub, q=q)
    th = table(s, MX, y, CW, header_row, rows, col_w=col_w, size=size, header_size=size, align=align, pad=pad,
               label=sid, max_h=max_h or (H - y - (1.25 if takeaway else 0.85)))
    if takeaway:
        statement(s, MX, min(y + th + 0.18, H - 1.2), CW, takeaway, size=12)
    foot(s, no, foot_note)
    return s
