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


def tone_metrics():
    """Korean share of words and '아니라' count over the main slides of the built deck."""
    import re
    from pptx import Presentation
    from paths import OUTPUT
    prs = Presentation(OUTPUT)
    txt = []
    for i, sl in enumerate(prs.slides):
        if i >= 17: break
        for sh in sl.shapes:
            if sh.has_text_frame: txt.append(sh.text_frame.text)
            if sh.has_table:
                for row in sh.table.rows:
                    for c in row.cells: txt.append(c.text)
    t = '\n'.join(txt)
    ko = len(re.findall(r'[가-힣]+', t)); en = len(re.findall(r'[A-Za-z]+', t))
    return dict(ko_ratio=f'{ko / (ko + en) * 100:.0f}%', anira=f'{t.count("아니라")}곳')


TM = tone_metrics()
TONE_ROWS = [(a, b, c.format(**TM)) for a, b, c in TONE]


def base_rows():
    f = f2
    rows = [['항목 (억 원)', '1년차', '2년차', '3년차', '4년차', '5년차']]
    rows.append(['핸드 단품 판매 (대)'] + [str(v) for v in A['hands']])
    rows.append(['주방 셀 판매 (대)'] + [str(v) for v in A['cells']])
    rows.append(['SW 유효 계약 (건)'] + [str(v) for v in A['sw']])
    rows.append(['매출: 핸드 (대수 × 0.15)'] + [f(v) for v in B['rev_hand']])
    rows.append(['매출: 주방 셀 (셀 × 2.0)'] + [f(v) for v in B['rev_cell']])
    rows.append(['매출: SW (계약 × 0.03)'] + [f(v) for v in B['rev_sw']])
    rows.append(['매출: 유료 실증·개발'] + [f(v) for v in B['rev_pilot']])
    rows.append(['총매출'] + [f(v) for v in B['rev']])
    rows.append(['매출총이익 (이익률)'] + [f'{f(g)} ({m * 100:.0f}%)' for g, m in zip(B['gp'], B['gm'])])
    rows.append(['운영비'] + [f(v) for v in B['opex']])
    rows.append(['영업손익'] + [f(v) for v in B['op']])
    rows.append(['누적 영업손익'] + [f(v) for v in B['cum_op']])
    return rows


ASSUMP = ('가정 (사업계획서 09장과 동일): 핸드 매출 = 단품 대수 × 0.15억 원, 주방 매출 = 셀 수 × 2억 원, SW 매출 = 유효 연간 계약 수 × 0.03억 원 · '
          '매출총이익: 핸드 46.7%, 주방 셀 30%, SW 70%, 유료 실증·개발 40% · 주방 셀에 포함한 핸드는 단품 매출에서 제외 · '
          '운영비는 연구개발·영업·관리·감가상각을 포함하는 계획값 · SW 계약 수는 당해 매출 인식 가능한 연간 계약 환산치')
SENS_ROWS = [('기준 시나리오', f'5년차 매출 {f2(B["rev"][4])}억 원 · 영업이익 {f2(B["op"][4])}억 원 · 4년차 흑자 전환'),
             ('3년차 판매량·계약·실증 매출 50% (동일 마진·운영비)', f'3년차 매출 {f2(S["y3_50"]["rev"])}억 원 · 영업손실 {f2(-S["y3_50"]["op"])}억 원'),
             ('4년차 모든 부문 매출 80%', f'매출총이익 {f2(S["y4_80"]["gp"])}억 원 < 운영비 {A["opex"][3]:.0f}억 원 (영업손실 {f2(-S["y4_80"]["op"])}억 원)')]
UOF_ROWS = [(k, f'{v:.1f}', f'{v / M["seed"] * 100:.1f}%', d) for k, v, d in U]
FUND = [f'1~2년차 운영비 {A["opex"][0] + A["opex"][1]:.0f}억 원, 매출총이익 {B["gp"][0] + B["gp"][1]:.2f}억 원 → 누적 영업손실 {f2(-B["cum_op"][1])}억 원',
        '자금 사용표는 현금 집행 예산이며 손익계산서 운영비와 일대일로 일치하지 않음 (사업계획서 원칙)',
        '재고·설비·보증금·매출채권·세금에 따라 현금 소요가 커지므로 18~24개월에 후속 자금 조달 필요, 보조금은 기본 재원에서 제외',
        '4차의 9항목·18 + 6개월 집행 구조·예비비 1.7억 원은 사업계획서 6항목으로 대체']
AVG = sum(sc for _, sc, _ in SCORES) / len(SCORES)

# ---------------------------------------------------------------- Markdown
def md_table(rows):
    clean = lambda c: str(c).replace('|', '/').replace('\n', '<br>')
    out = ['| ' + ' | '.join(clean(c) for c in rows[0]) + ' |', '|' + '|'.join(['---'] * len(rows[0])) + '|']
    for r in rows[1:]: out.append('| ' + ' | '.join(clean(c) for c in r) + ' |')
    return '\n'.join(out)

md = [f'# {TITLE}', f'_{SUBTITLE}_', '']
md.append(md_table([['구분', '내용']] + [list(r) for r in META]))
md += ['', '## 0. 요약', ''] + [f'- {t}' for t in SUMMARY]
md += ['', '### 4차 → 5차 비교', '']
md.append(md_table([['항목', '4차', '5차 (사업계획서 기준)']] + [list(r) for r in METRICS]))
md += ['', '## 1. 통합 원칙: 4차에만 있던 내용의 처리', '',
       '수치·사업 순서·제품 정의·일정·팀·자금 사용은 사업계획서를 따르고, 사업계획서 형식·문체·표 중심 구성은 4차를 유지. 4차에만 있던 내용은 아래와 같이 처리.', '']
md.append(md_table([['4차 내용', '처리', '이유']] + [list(r) for r in MERGE]))
md += ['', '## 2. 슬라이드별 변경 (5차 본문 17장 기준)', '']
md.append(md_table([['5차 장', '항목', '근거 (4차 / 사업계획서)', '변경 내용', '이유']] + [list(r) for r in CHANGES]))
md += ['', '### 부록 변경', '']
md.append(md_table([['4차 부록', '5차 위치', '내용']] + [list(r) for r in APPX_CHANGES]))
md += ['', '## 3. 5차 구성', '']
md.append(md_table([['장', '항목', '제목']] + [list(r) for r in SLIDES]))
md += ['', '## 4. 사업계획서와 수치 대조', '', '재무 모델(source/deck/model.py)이 사업계획서 수치를 그대로 재현하는지 assert로 검사한 뒤 덱·보고서를 생성.', '']
md.append(md_table([['항목', '사업계획서', '덱 위치', '결과']] + [list(r) for r in CHECK]))
md += ['', '## 5. 문체·디자인 점검 결과', '']
md.append(md_table([['점검 항목', '4차', '5차']] + [list(r) for r in TONE_ROWS]))
md += ['', '## 6. 투자 심사 관점 점검', '']
md.append(md_table([['질문', '5차 근거', '판정']] + [list(r) for r in REVIEW]))
md += ['', '### 투자심의 평가 (10점 만점)', '']
md.append(md_table([['항목', '점수', '근거']] + [[a, str(b), c] for a, b, c in SCORES]))
md += ['', f'평균 {AVG:.1f}점. 사업 구조와 재무 산식은 투명해졌고, 팀·실물·고객 항목이 낮은 시제품 이전 Seed 상태', '',
       '### 사업계획서 수치에 대한 검토 의견 (수치는 바꾸지 않음, 실사 전 보완 권장)', '']
md.append(md_table([['항목', '현재 수치', '보완 권장']] + [list(r) for r in REDFLAGS]))
md += ['', '### 현재 상태에서 투자를 보류한다면 가장 큰 이유 3개', ''] + [f'{i + 1}. **{a}**: {b}' for i, (a, b) in enumerate(HOLD)]
md += ['', '### 이 3가지가 확보되면 투자 결정 가능성이 크게 높아지는 증거 3개', ''] + [f'{i + 1}. **{a}**: {b}' for i, (a, b) in enumerate(EVIDENCE)]
md += ['', '## 7. 재무와 자금 (사업계획서 기준 시나리오)', '', '### 7.1 5개년 기준 시나리오', '']
md.append(md_table(base_rows()))
md += ['', ASSUMP, '', '### 7.2 민감도 (사업계획서)', '']
md.append(md_table([['시나리오', '결과']] + [list(r) for r in SENS_ROWS]))
md += ['', '### 7.3 Seed 20억 원 사용 계획 (사업계획서 제안안)', '']
md.append(md_table([['항목', '금액 (억 원)', '비중', '사용 목적']] + [list(r) for r in UOF_ROWS]))
md += [''] + [f'- {t}' for t in FUND] + ['']
md += ['## 8. 출처 확인 결과', '']
md.append(md_table([['항목', '확인 내용']] + [list(r) for r in FACTS]))
md += ['', '## 9. 사실·가정 구분 원칙', ''] + [f'- {t}' for t in PRINCIPLES]
md += ['', '## 10. 외부 제출 전 입력할 정보', '']
md.append(md_table([['항목', '위치', '내용']] + [list(r) for r in TODO]))
md += ['', '## 11. 출처 (열람 2026-10-06)', '']
md.append(md_table([['번호', '출처', 'URL']] + [list(r) for r in SOURCES_FULL]))
md += ['', '## 12. 다음 단계', ''] + [f'{i + 1}. {t}' for i, t in enumerate(NEXT)] + ['']
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
heading('4차 → 5차 비교', 3)
table([['항목', '4차', '5차 (사업계획서 기준)']] + [list(r) for r in METRICS], [3.2, 6.4, 7.4], first_col_bold=True, size=8.5)
heading('1. 통합 원칙: 4차에만 있던 내용의 처리')
para('수치·사업 순서·제품 정의·일정·팀·자금 사용은 사업계획서를 따르고, 사업계획서 형식·문체·표 중심 구성은 4차를 유지. 4차에만 있던 내용은 아래와 같이 처리.', 10, after=6)
table([['4차 내용', '처리', '이유']] + [list(r) for r in MERGE], [5.4, 5.0, 6.6], first_col_bold=True, size=8.5)
heading('2. 슬라이드별 변경 (5차 본문 17장 기준)')
table([['5차 장', '항목', '근거 (4차 / 사업계획서)', '변경 내용', '이유']] + [list(r) for r in CHANGES], [1.1, 3.2, 2.8, 6.2, 3.7], size=8)
heading('부록 변경', 2)
table([['4차 부록', '5차 위치', '내용']] + [list(r) for r in APPX_CHANGES], [4.8, 4.6, 7.6], size=8.5)
heading('3. 5차 구성')
table([['장', '항목', '제목']] + [list(r) for r in SLIDES], [1.6, 4.4, 11.0], size=9)
heading('4. 사업계획서와 수치 대조')
para('재무 모델(source/deck/model.py)이 사업계획서 수치를 그대로 재현하는지 assert로 검사한 뒤 덱·보고서를 생성.', 10, after=6)
table([['항목', '사업계획서', '덱 위치', '결과']] + [list(r) for r in CHECK], [3.4, 8.6, 3.2, 1.8], first_col_bold=True, size=8.5)
heading('5. 문체·디자인 점검 결과')
table([['점검 항목', '4차', '5차']] + [list(r) for r in TONE_ROWS], [5.0, 4.6, 7.4], first_col_bold=True, size=9)
heading('6. 투자 심사 관점 점검')
table([['질문', '5차 근거', '판정']] + [list(r) for r in REVIEW], [5.0, 9.0, 3.0], size=9)
heading('투자심의 평가 (10점 만점)', 2)
table([['항목', '점수', '근거']] + [[a, str(b), c] for a, b, c in SCORES], [3.6, 1.4, 12.0], first_col_bold=True, size=9)
para(f'평균 {AVG:.1f}점. 사업 구조와 재무 산식은 투명해졌고, 팀·실물·고객 항목이 낮은 시제품 이전 Seed 상태', 10, True, DARK, after=6)
heading('사업계획서 수치에 대한 검토 의견 (수치는 바꾸지 않음, 실사 전 보완 권장)', 3)
table([['항목', '현재 수치', '보완 권장']] + [list(r) for r in REDFLAGS], [3.4, 6.4, 7.2], first_col_bold=True, size=8.5)
heading('현재 상태에서 투자를 보류한다면 가장 큰 이유 3개', 3)
for i, (a, b) in enumerate(HOLD): para(f'{i + 1}. {a}: {b}', 10, after=3)
heading('이 3가지가 확보되면 투자 결정 가능성이 크게 높아지는 증거 3개', 3)
for i, (a, b) in enumerate(EVIDENCE): para(f'{i + 1}. {a}: {b}', 10, after=3)
heading('7. 재무와 자금 (사업계획서 기준 시나리오)')
heading('7.1 5개년 기준 시나리오', 2)
table(base_rows(), [5.0, 2.4, 2.4, 2.4, 2.4, 2.4], first_col_bold=True, size=8.5)
para(ASSUMP, 9, color=GRAY)
heading('7.2 민감도 (사업계획서)', 2)
table([['시나리오', '결과']] + [list(r) for r in SENS_ROWS], [7.0, 10.0], first_col_bold=True)
heading('7.3 Seed 20억 원 사용 계획 (사업계획서 제안안)', 2)
table([['항목', '금액 (억 원)', '비중', '사용 목적']] + [list(r) for r in UOF_ROWS], [4.0, 2.4, 2.0, 8.6], size=9)
for t_ in FUND: bullet(t_)
heading('8. 출처 확인 결과')
table([['항목', '확인 내용']] + [list(r) for r in FACTS], [3.8, 13.2], first_col_bold=True, size=9)
heading('9. 사실·가정 구분 원칙')
for t_ in PRINCIPLES: bullet(t_)
heading('10. 외부 제출 전 입력할 정보')
table([['항목', '위치', '내용']] + [list(r) for r in TODO], [3.4, 2.8, 10.8], first_col_bold=True, size=9)
heading('11. 출처 (열람 2026-10-06)')
table([['번호', '출처', 'URL']] + [list(r) for r in SOURCES_FULL], [1.2, 7.4, 8.4], size=8)
heading('12. 다음 단계')
for i, t_ in enumerate(NEXT): para(f'{i + 1}. {t_}', 10, after=3)
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = fp.add_run('SoftHand 사업계획서 최종본 수정 보고서 (5차)  ·  대외비  ·  '); set_font(r, 8, False, GRAY)
fld1 = OxmlElement('w:fldSimple'); fld1.set(qn('w:instr'), 'PAGE'); rr = OxmlElement('w:r'); t = OxmlElement('w:t'); t.text = '1'; rr.append(t); fld1.append(rr); fp._p.append(fld1)
z = doc.settings.element.find(qn('w:zoom'))
if z is not None and z.get(qn('w:percent')) is None: z.set(qn('w:percent'), '100')
doc.save(OUT_DOCX)
print('ok')
