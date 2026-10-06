# -*- coding: utf-8 -*-
# python3 source/deck/make_report.py OUT.md OUT.docx
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from report_content import *
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT_MD = sys.argv[1]; OUT_DOCX = sys.argv[2]
A = M['assumptions']

def base_rows():
    f = lambda v: f'{v:.1f}'.replace('-', '−')
    rows = [['항목 (억 원)', '1년', '2년', '3년', '4년', '5년']]
    rows.append(['유료 PoC / 통합 (건)'] + [f'{a} / {b}' for a, b in zip(A['poc_n'], A['int_n'])])
    rows.append(['신규 핸드 (대) 직판 / 파트너'] + [f'{a} / {b}' for a, b in zip(A['hand_direct'], A['hand_partner'])])
    rows.append(['매출: 유료 PoC·통합'] + [f(v) for v in B['poc_int']])
    rows.append(['매출: SoftHand 하드웨어'] + [f(v) for v in B['hw']])
    rows.append(['매출: 작업 스킬'] + [f(v) for v in B['skill']])
    rows.append(['매출: 런타임·유지보수'] + [f(v) for v in B['runtime']])
    rows.append(['매출: 파트너 판매'] + [f(v) for v in B['partner']])
    rows.append(['총매출'] + [f(v) for v in B['rev']])
    rows.append(['매출총이익 (이익률)'] + [f'{f(g)} ({m*100:.0f}%)' for g, m in zip(B['gp'], B['gm'])])
    rows.append(['운영비'] + [f(v) for v in B['opex']])
    rows.append(['영업손익'] + [f(v) for v in B['op']])
    rows.append(['재사용 매출 비중'] + [f'{v*100:.0f}%' for v in B['reuse_share']])
    return rows

ASSUMP = ('가정: 유료 PoC 건당 5,000만 원 · 통합 프로젝트 4,000만 원 · 핸드 1,500만 원 (SI 파트너 순매출 1,200만 원) · 핸드 원가 950만 → 750만 원 · '
          '스킬 300만 원 (파트너 240만 원, 핸드당 1.0 → 1.6개) · 런타임 설치 핸드당 연 150만 원 · 매출총이익률: PoC·통합 40%, 스킬 85%, 런타임 70% · '
          '운영비 1·2년차는 Seed 집행 계획과 동일, 3~5년차는 평균 인원 14·19·23명 기준')
FUND = [f"18개월 핵심 운영 {S['core18']:.1f}억 원 + 6개월 연장 {S['ext6']:.1f}억 원 (M18 점검 통과 시) + 예비비 {CONT:.1f}억 원 = 20.0억 원",
        f"손익 연결: 운영비 1년차 {S['opex_y1']:.1f}억 + 2년차 {S['opex_y2']:.1f}억 = 집행 계획 − 예비비 (매출원가는 매출로 충당)",
        f'매출이 없어도 24개월 뒤 예비비 {CONT:.1f}억 원 잔존, 정부지원금·공동개발비는 확정 전이라 기본 재원에서 제외']
REDTEAM_NOTE = '실제 투자 심의에서 나올 질문 17개에 2차 수정본 본문만으로 답할 수 있는지 점검한 결과. 1차에서 덱 부록에 있던 목록을 투자자 배포 자료가 아니므로 이 보고서로 이동'

# ---------------------------------------------------------------- Markdown
def md_table(rows):
    out = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '|'.join(['---'] * len(rows[0])) + '|']
    for r in rows[1:]: out.append('| ' + ' | '.join(str(c).replace('|', '/') for c in r) + ' |')
    return '\n'.join(out)

md = [f'# {TITLE}', f'_{SUBTITLE}_', '']
md.append(md_table([['구분', '내용']] + [list(r) for r in META]))
md += ['', '## 0. 요약', '']
md += [f'- {t}' for t in SUMMARY]
md += ['', '### 1차 → 2차 수치 비교 (본문 16장)', '']
md.append(md_table([['항목', '1차 수정본', '2차 수정본']] + [list(r) for r in METRICS]))
md += ['', '### 투자자가 이렇게 설명할 수 있는가', '']
md.append(md_table([['투자자가 설명해야 하는 내용', '답하는 장']] + [list(r) for r in JUDGMENT]))
md += ['', '## 1. 2차 수정 상세: 기존 → 수정 → 이유 → 투자자 효과', '']
for i, (t, before, after, why, eff) in enumerate(CHANGES2):
    md += [f'### 1.{i+1} {t}', '']
    md.append(md_table([['구분', '내용'], ['기존', before], ['수정', after], ['이유', why], ['투자자 효과', eff]]))
    md.append('')
md += ['## 2. 1차 필수 변경 14항목의 2차 반영 위치', '']
md.append(md_table([['#', '변경', '2차 반영 내용', '위치']] + [[str(i + 1)] + list(r) for i, r in enumerate(CHANGES1)]))
md += ['', '## 3. 2차 수정본 장표 구성', '']
md.append(md_table([['장', '제목', '역할']] + [list(r) for r in SLIDES]))
md += ['', '## 4. 재무 계획과 Seed 집행 (1차와 동일)', '', '### 4.1 5개년 기본 시나리오 (주방·OEM 매출 0원)', '']
md.append(md_table(base_rows()))
md += ['', ASSUMP, '', '### 4.2 민감도', '']
md.append(md_table([['시나리오', '결과']] + [list(r) for r in SENS]))
md += ['', '### 4.3 Seed 20억 원 자금 사용: 원본 vs 수정 (억 원)', '']
md.append(md_table([['항목', '원본', '수정', '근거']] + [list(r) for r in UOF_COMPARE]))
md += [''] + [f'- {t}' for t in FUND] + ['']
md += ['## 5. VC 예상 질문 17개와 답변 위치', '', REDTEAM_NOTE, '']
md.append(md_table([['#', '질문', '위치', '판정', '근거']] + [[str(i + 1), q, sl, v, n] for i, (q, sl, v, n) in enumerate(REDTEAM)]))
md += ['', '## 6. 외부 제출 전 입력할 정보', '']
md.append(md_table([['항목', '위치', '내용']] + [list(r) for r in TODO]))
md += ['', '## 7. 사실·가정 구분 원칙', ''] + [f'- {t}' for t in PRINCIPLES]
md += ['', '## 8. 이미지 기준: SoftHand-4 디자인', '']
md.append(md_table([['요소', '고정 기준']] + [list(r) for r in DESIGN_LANG]))
md += ['', DESIGN_NOTE, '', '## 9. 다음 단계', ''] + [f'{i + 1}. {t}' for i, t in enumerate(NEXT)] + ['']
open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(md))

# ---------------------------------------------------------------- DOCX
doc = Document()
sec = doc.sections[0]
sec.page_width = Cm(21.0); sec.page_height = Cm(29.7)
for side in ('left_margin', 'right_margin'): setattr(sec, side, Cm(2.0))
sec.top_margin = Cm(2.0); sec.bottom_margin = Cm(1.8)
FONT_KO = '맑은 고딕'; FONT_EN = 'Malgun Gothic'
ORANGE = RGBColor(0xE2, 0x57, 0x1B); DARK = RGBColor(0x15, 0x17, 0x1A); GRAY = RGBColor(0x4A, 0x4F, 0x57)

def set_font(run, size=10, bold=False, color=DARK):
    run.font.size = Pt(size); run.font.bold = bold; run.font.color.rgb = color
    run.font.name = FONT_EN
    rPr = run._element.get_or_add_rPr(); rf = rPr.find(qn('w:rFonts'))
    if rf is None: rf = OxmlElement('w:rFonts'); rPr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs'): rf.set(qn(a), FONT_EN)
    rf.set(qn('w:eastAsia'), FONT_KO)

st = doc.styles['Normal']; st.font.name = FONT_EN; st.font.size = Pt(10)
st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT_KO)
pf = st.paragraph_format; pf.space_after = Pt(4); pf.line_spacing = 1.25
# no automatic extra space between Hangul and Latin letters / digits (Word default is on)
_pPr = st.element.get_or_add_pPr()
_succ = ('w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind', 'w:contextualSpacing', 'w:mirrorIndents',
         'w:suppressOverlap', 'w:jc', 'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap', 'w:outlineLvl', 'w:divId', 'w:cnfStyle', 'w:rPr')
for _tag in ('w:autoSpaceDE', 'w:autoSpaceDN'):
    _e = OxmlElement(_tag); _e.set(qn('w:val'), '0')
    _nxt = next((_pPr.find(qn(t)) for t in _succ if _pPr.find(qn(t)) is not None), None)
    if _nxt is not None: _nxt.addprevious(_e)
    else: _pPr.append(_e)

def para(text, size=10, bold=False, color=DARK, after=4, align=None, before=0):
    p = doc.add_paragraph(); r = p.add_run(text); set_font(r, size, bold, color)
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(before)
    if align: p.alignment = align
    return p

def heading(text, level=1):
    h = doc.add_heading(level=level)
    r = h.add_run(text); set_font(r, {1: 15, 2: 12, 3: 11}[level], True, ORANGE if level == 1 else DARK)
    h.paragraph_format.space_before = Pt(14 if level == 1 else 10); h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    return h

def bullet(text, style='List Bullet'):
    p = doc.add_paragraph(style=style); r = p.add_run(text); set_font(r, 10)
    p.paragraph_format.space_after = Pt(3)
    return p

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexcolor); tcPr.append(shd)

def table(rows, widths_cm, head=True, first_col_bold=False, size=9):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.autofit = False
    for i, wcm in enumerate(widths_cm): t.columns[i].width = Cm(wcm)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = t.cell(ri, ci); c.width = Cm(widths_cm[ci])
            c.text = ''
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(1); p.paragraph_format.line_spacing = 1.15
            r = p.add_run(str(val))
            hb = (head and ri == 0) or (first_col_bold and ci == 0)
            set_font(r, size, hb, DARK)
            if head and ri == 0: shade(c, 'E9EBEE')
    tblPr = t._tbl.tblPr; borders = OxmlElement('w:tblBorders')
    for b in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{b}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), 'D5D8DC'); borders.append(e)
    anchor = None
    for tag in ('w:shd', 'w:tblLayout', 'w:tblCellMar', 'w:tblLook', 'w:tblCaption', 'w:tblDescription'):
        anchor = tblPr.find(qn(tag))
        if anchor is not None: break
    if anchor is not None: anchor.addprevious(borders)
    else: tblPr.append(borders)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

para(TITLE, 20, True, DARK, after=2)
para(SUBTITLE, 10.5, False, ORANGE, after=10)
table([['구분', '내용']] + [list(r) for r in META], [3.2, 13.8], first_col_bold=True)
heading('0. 요약')
for t_ in SUMMARY: bullet(t_)
heading('1차 → 2차 수치 비교 (본문 16장)', 3)
table([['항목', '1차 수정본', '2차 수정본']] + [list(r) for r in METRICS], [5.0, 6.0, 6.0], first_col_bold=True)
heading('투자자가 이렇게 설명할 수 있는가', 3)
table([['투자자가 설명해야 하는 내용', '답하는 장']] + [list(r) for r in JUDGMENT], [13.0, 4.0])
heading('1. 2차 수정 상세: 기존 → 수정 → 이유 → 투자자 효과')
for i, (t_, before, after, why, eff) in enumerate(CHANGES2):
    heading(f'1.{i+1}  {t_}', 2)
    table([['구분', '내용'], ['기존', before], ['수정', after], ['이유', why], ['투자자 효과', eff]], [3.0, 14.0], first_col_bold=True)
heading('2. 1차 필수 변경 14항목의 2차 반영 위치')
table([['#', '변경', '2차 반영 내용', '위치']] + [[str(i + 1)] + list(r) for i, r in enumerate(CHANGES1)], [0.8, 5.0, 8.6, 2.6], size=8.5)
heading('3. 2차 수정본 장표 구성')
table([['장', '제목', '역할']] + [list(r) for r in SLIDES], [1.2, 8.3, 7.5], size=8.5)
heading('4. 재무 계획과 Seed 집행 (1차와 동일)')
heading('4.1 5개년 기본 시나리오 (주방·OEM 매출 0원)', 2)
table(base_rows(), [5.0, 2.4, 2.4, 2.4, 2.4, 2.4], first_col_bold=True, size=8.5)
para(ASSUMP, 9, color=GRAY)
heading('4.2 민감도', 2)
table([['시나리오', '결과']] + [list(r) for r in SENS], [6.0, 11.0], first_col_bold=True)
heading('4.3 Seed 20억 원 자금 사용: 원본 vs 수정 (억 원)', 2)
table([['항목', '원본', '수정', '근거']] + [list(r) for r in UOF_COMPARE], [3.8, 3.2, 2.6, 7.4], first_col_bold=True, size=8.5)
for t_ in FUND: bullet(t_)
heading('5. VC 예상 질문 17개와 답변 위치')
para(REDTEAM_NOTE, 9.5, color=GRAY)
table([['#', '질문', '위치', '판정', '근거']] + [[str(i + 1), q, sl, v, n] for i, (q, sl, v, n) in enumerate(REDTEAM)], [0.8, 5.4, 2.0, 1.8, 7.0], size=8.5)
heading('6. 외부 제출 전 입력할 정보')
table([['항목', '위치', '내용']] + [list(r) for r in TODO], [3.6, 2.6, 10.8], first_col_bold=True)
heading('7. 사실·가정 구분 원칙')
for t_ in PRINCIPLES: bullet(t_)
heading('8. 이미지 기준: SoftHand-4 디자인')
table([['요소', '고정 기준']] + [list(r) for r in DESIGN_LANG], [4.0, 13.0], first_col_bold=True)
para(DESIGN_NOTE, 9, color=GRAY)
heading('9. 다음 단계')
for t_ in NEXT: bullet(t_, style='List Number')
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = fp.add_run('SoftHand IR Deck 수정 보고서  ·  대외비  ·  '); set_font(r, 8, False, GRAY)
fld1 = OxmlElement('w:fldSimple'); fld1.set(qn('w:instr'), 'PAGE'); rr = OxmlElement('w:r'); t = OxmlElement('w:t'); t.text = '1'; rr.append(t); fld1.append(rr); fp._p.append(fld1)
z = doc.settings.element.find(qn('w:zoom'))
if z is not None and z.get(qn('w:percent')) is None: z.set(qn('w:percent'), '100')
doc.save(OUT_DOCX)
print('ok')
