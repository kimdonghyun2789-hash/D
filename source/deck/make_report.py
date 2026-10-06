# -*- coding: utf-8 -*-
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
    f = lambda v: f'{v:.1f}'
    rows = [['항목 (억원)', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5']]
    rows.append(['유료 PoC / 통합 (건)'] + [f'{a} / {b}' for a, b in zip(A['poc_n'], A['int_n'])])
    rows.append(['신규 Hand (대) 직판 / 파트너'] + [f'{a} / {b}' for a, b in zip(A['hand_direct'], A['hand_partner'])])
    rows.append(['매출 — 유료 PoC · 통합'] + [f(v) for v in B['poc_int']])
    rows.append(['매출 — SoftHand 하드웨어'] + [f(v) for v in B['hw']])
    rows.append(['매출 — ToolSkill 패키지'] + [f(v) for v in B['skill']])
    rows.append(['매출 — Runtime · 유지보수'] + [f(v) for v in B['runtime']])
    rows.append(['매출 — Partner Sales'] + [f(v) for v in B['partner']])
    rows.append(['총매출'] + [f(v) for v in B['rev']])
    rows.append(['매출총이익 (GM)'] + [f'{f(g)} ({m*100:.0f}%)' for g, m in zip(B['gp'], B['gm'])])
    rows.append(['운영비'] + [f(v) for v in B['opex']])
    rows.append(['영업손익'] + [f(v) for v in B['op']])
    rows.append(['재사용 매출 비중'] + [f'{v*100:.0f}%' for v in B['reuse_share']])
    return rows

SENS = [('판매량 −30% (Y3~Y5)', 'Y5 매출 31.4억 · 영업손익 −7.1억'), ('Hand 원가 절감 지연 (₩900만 유지)', 'Y5 영업손익 −3.1억'),
        ('SI 파트너 채널 1년 지연', 'Y5 매출 32.3억 · 영업손익 −6.4억'), ('판매량 −50%', 'Y5 매출 22.4억 · 영업손익 −11.9억'),
        ('기존 Deck', 'Y5 매출 112억 (Kitchen 셀 50억 = 45%) → 수정 Y5 44.7억 (Kitchen 0 · OEM 0)')]

# ---------------------------------------------------------------- Markdown
def md_table(rows):
    out = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '|'.join(['---'] * len(rows[0])) + '|']
    for r in rows[1:]: out.append('| ' + ' | '.join(str(c).replace('|', '/') for c in r) + ' |')
    return '\n'.join(out)

md = [f'# {TITLE}', f'_{SUBTITLE}_', '']
md.append(md_table([['구분', '내용']] + [list(r) for r in META]))
md += ['', '## 0. 요약', '']
md += [f'- {t}' for t in SUMMARY]
md += ['', '### 최종 판단기준 — 투자자가 이렇게 설명할 수 있는가', '']
md.append(md_table([['투자자가 설명해야 하는 내용', '답하는 Slide']] + [list(r) for r in JUDGMENT]))
md += ['', '## 1. 필수 변경 14항목 — 기존 → 수정 → 이유 → 투자자 효과', '']
for i, (t, before, after, why, eff, sl) in enumerate(CHANGES):
    md += [f'### 1.{i+1} {t}', '']
    md.append(md_table([['구분', '내용'], ['기존 내용', before], ['수정 내용', after], ['수정 이유', why], ['투자자 관점의 효과', eff], ['반영 Slide', sl]]))
    md.append('')
md += ['## 2. 추가 변경', '']
md.append(md_table([['항목', '기존', '수정', 'Slide']] + [list(r) for r in EXTRA]))
md += ['', '## 3. 장표 매핑 (기존 → 최종)', '']
md.append(md_table([['기존', '기존 제목', '최종', '처리']] + [list(r) for r in SLIDEMAP]))
md += ['', '## 4. 재무 모델과 Seed 집행 계획', '', '### 4.1 Base Case 5개년 (Kitchen · OEM 매출 0원, Management Forecast)', '']
md.append(md_table(base_rows()))
md += ['', '가정: 유료 PoC 건당 ₩5,000만 · 통합 프로젝트 ₩4,000만 · Hand 패키지 ₩1,500만(파트너 순매출 ₩1,200만) · Hand 원가 ₩950만 → ₩750만 · Skill 패키지 ₩300만(파트너 ₩240만, Hand당 1.0 → 1.6개) · Runtime 설치 Hand당 연 ₩150만 · GM: PoC/통합 40%, Skill 85%, Runtime 70%. 운영비 Y1 · Y2는 Seed 집행 계획과 동일, Y3~Y5는 평균 인원 14 / 19 / 23명 기준.', '', '### 4.2 Sensitivity', '']
md.append(md_table([['시나리오', '결과']] + [list(r) for r in SENS]))
md += ['', '### 4.3 Seed ₩20억 Use of Funds — 기존 vs 수정 (억원)', '']
md.append(md_table([['항목', '기존', '수정', '근거']] + [list(r) for r in UOF_COMPARE]))
md += ['', f"- 18개월 Core Runway ₩{S['core18']:.1f}억 + 6개월 Milestone Extension ₩{S['ext6']:.1f}억(M18 Gate 통과 시) + 예비비 ₩1.7억 = ₩20.0억",
       f"- P&L 운영비 Y1 ₩{S['opex_y1']:.1f}억 + Y2 ₩{S['opex_y2']:.1f}억 = Use of Funds − 예비비 (매출원가는 매출로 충당)",
       '- 매출이 0원이어도 M24 잔액 ₩1.7억 — 24개월 집행 가능. 정부지원금 · 공동개발비는 확정 전이므로 기본 재원에서 제외', '']
md += ['## 5. VC Red-Team Review 결과', '', '실제 투자심의 질문 17개를 본문만으로 답할 수 있는지 점검했다. "보완"은 이번 점검에서 본문을 다시 수정한 항목이다.', '']
md.append(md_table([['#', '질문', 'Slide', '판정', '근거 · 보완 내용']] + [[str(i + 1), q, sl, v, n] for i, (q, sl, v, n) in enumerate(REDTEAM)]))
md += ['', '## 6. 외부 제출 전 반드시 입력할 정보', '']
md.append(md_table([['항목', '위치', '내용']] + [list(r) for r in TODO]))
md += ['', '## 7. 사실 · 가정 구분 원칙 (유지)', '',
       '- 확인되지 않은 고객 · Design Partner · 실적 · 특허 · 성능은 만들지 않았다. Design Partner는 모두 TARGET · 미확보, 성능은 Target, 가격 · 원가 · 매출은 가정으로 표기했다.',
       '- 유지한 외부 수치는 재확인했다: IFR World Robotics 2026(2026-09-24, 가동 약 500만 대 · 2025년 60만 대+ 설치 · 2026F 65.5만 · 2029F 80.6만), IFR Robot Density(2026-04, 한국 1,220대/직원 1만 명 · 2025년 3.0만 대 설치), BCG(2026-04, TCO의 약 75%가 초기 셋업 · 재설계, Software-defined 접근의 절감 잠재력 최대 50%). BCG 50%는 우리 제품의 효과로 쓰지 않았다.',
       '- 기존 Deck의 "사람 개입 −30%", OEM 매출 302억~1,810억, 초기 기회 ₩75억 계산은 검증 근거가 없어 삭제했다.', '',
       '## 8. Concept Rendering 통일 기준 — SoftHand-4 Design Language', '']
md.append(md_table([['요소', '고정 기준']] + [list(r) for r in DESIGN_LANG]))
md += ['', '적용: 표지(설비 문 손잡이를 잡은 SoftHand-4) · 03 제품 · 04 Cutaway · 05 머신텐딩 Cell · 06 6단계 Workflow · 10 Robot A/B · 12 공장/주방 벤치 · 16 Closing · A9 Screwdriver Demo를 모두 같은 3D 모델로 재렌더링. 문제 장표의 전용 그리퍼 이미지(손이 아님)와 A14의 천장형 주방 Future Vision 이미지만 원본 유지.', '',
       '## 9. 다음 단계 권고', '',
       '1. Founder 정보(14) 입력 — 외부 제출 전 필수. 가장 약한 질문(Q17)이 이 장표에 달려 있다.',
       '2. 창업 후 90일 내 고객 인터뷰 30곳으로 첫 구매자 가설(05)과 지불의사(07)를 검증하고, Design Partner 후보를 실명 · 상태(MOU/LOI)로 갱신.',
       '3. 가격 · 원가 가정(A10)을 공급사 견적 · BOM으로 갱신하고 Base Case(A11)를 재계산.',
       '4. 실물 Prototype 사진 · 무편집 시험 영상이 생기면 Concept Rendering을 순서대로 교체.', '']
open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(md))

# ---------------------------------------------------------------- DOCX
doc = Document()
sec = doc.sections[0]
sec.page_width = Cm(21.0); sec.page_height = Cm(29.7)
for side in ('left_margin', 'right_margin'): setattr(sec, side, Cm(2.0))
sec.top_margin = Cm(2.0); sec.bottom_margin = Cm(1.8)
FONT_KO = '맑은 고딕'; FONT_EN = 'Malgun Gothic'
ORANGE = RGBColor(0xEC, 0x7A, 0x3C); DARK = RGBColor(0x16, 0x18, 0x1B); GRAY = RGBColor(0x51, 0x56, 0x5E)

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

def para(text, size=10, bold=False, color=DARK, after=4, align=None, before=0):
    p = doc.add_paragraph(); r = p.add_run(text); set_font(r, size, bold, color)
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(before)
    if align: p.alignment = align
    return p

def heading(text, level=1):
    h = doc.add_heading(level=level)
    r = h.add_run(text); set_font(r, {1: 15, 2: 12.5, 3: 11}[level], True, ORANGE if level == 1 else DARK)
    h.paragraph_format.space_before = Pt(14 if level == 1 else 10); h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    return h

def bullet(text):
    p = doc.add_paragraph(style='List Bullet'); r = p.add_run(text); set_font(r, 10)
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
            set_font(r, size, hb, RGBColor(0xFF, 0xFF, 0xFF) if (head and ri == 0) else DARK)
            if head and ri == 0: shade(c, '16181B')
            elif first_col_bold and ci == 0: shade(c, 'F2F1EE')
    # borders color
    tblPr = t._tbl.tblPr; borders = OxmlElement('w:tblBorders')
    for b in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{b}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), 'CFCCC6'); borders.append(e)
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
heading('최종 판단기준 — 투자자가 이렇게 설명할 수 있는가', 3)
table([['투자자가 설명해야 하는 내용', '답하는 Slide']] + [list(r) for r in JUDGMENT], [13.0, 4.0])
heading('1. 필수 변경 14항목 — 기존 → 수정 → 이유 → 투자자 효과')
for i, (t_, before, after, why, eff, sl) in enumerate(CHANGES):
    heading(f'1.{i+1}  {t_}', 2)
    table([['구분', '내용'], ['기존 내용', before], ['수정 내용', after], ['수정 이유', why], ['투자자 관점의 효과', eff], ['반영 Slide', sl]], [3.2, 13.8], first_col_bold=True)
heading('2. 추가 변경')
table([['항목', '기존', '수정', 'Slide']] + [list(r) for r in EXTRA], [3.0, 4.0, 8.0, 2.0], first_col_bold=True, size=8.5)
heading('3. 장표 매핑 (기존 → 최종)')
table([['기존', '기존 제목', '최종', '처리']] + [list(r) for r in SLIDEMAP], [1.6, 6.0, 3.0, 6.4], size=8.5)
heading('4. 재무 모델과 Seed 집행 계획')
heading('4.1 Base Case 5개년 (Kitchen · OEM 매출 0원)', 2)
table(base_rows(), [5.0, 2.4, 2.4, 2.4, 2.4, 2.4], first_col_bold=True, size=8.5)
para('가정: 유료 PoC 건당 ₩5,000만 · 통합 프로젝트 ₩4,000만 · Hand 패키지 ₩1,500만(파트너 순매출 ₩1,200만) · Hand 원가 ₩950만 → ₩750만 · Skill 패키지 ₩300만(파트너 ₩240만, Hand당 1.0 → 1.6개) · Runtime 설치 Hand당 연 ₩150만 · GM: PoC/통합 40%, Skill 85%, Runtime 70%. 운영비 Y1·Y2는 Seed 집행 계획과 동일, Y3~Y5는 평균 인원 14 / 19 / 23명 기준.', 9, color=GRAY)
heading('4.2 Sensitivity', 2)
table([['시나리오', '결과']] + [list(r) for r in SENS], [6.0, 11.0], first_col_bold=True)
heading('4.3 Seed ₩20억 Use of Funds — 기존 vs 수정 (억원)', 2)
table([['항목', '기존', '수정', '근거']] + [list(r) for r in UOF_COMPARE], [3.8, 3.2, 2.6, 7.4], first_col_bold=True, size=8.5)
bullet(f"18개월 Core Runway ₩{S['core18']:.1f}억 + 6개월 Milestone Extension ₩{S['ext6']:.1f}억(M18 Gate 통과 시) + 예비비 ₩1.7억 = ₩20.0억")
bullet(f"P&L 운영비 Y1 ₩{S['opex_y1']:.1f}억 + Y2 ₩{S['opex_y2']:.1f}억 = Use of Funds − 예비비 (매출원가는 매출로 충당)")
bullet('매출이 0원이어도 M24 잔액 ₩1.7억 — 24개월 집행 가능. 정부지원금 · 공동개발비는 확정 전이므로 기본 재원에서 제외')
heading('5. VC Red-Team Review 결과')
para('실제 투자심의 질문 17개를 본문만으로 답할 수 있는지 점검했다. "보완"은 이번 점검에서 본문을 다시 수정한 항목이다.', 9.5, color=GRAY)
table([['#', '질문', 'Slide', '판정', '근거 · 보완 내용']] + [[str(i + 1), q, sl, v, n] for i, (q, sl, v, n) in enumerate(REDTEAM)], [0.8, 5.4, 1.8, 1.8, 7.2], size=8.5)
heading('6. 외부 제출 전 반드시 입력할 정보')
table([['항목', '위치', '내용']] + [list(r) for r in TODO], [3.6, 2.4, 11.0], first_col_bold=True)
heading('7. 사실 · 가정 구분 원칙 (유지)')
for t_ in ['확인되지 않은 고객 · Design Partner · 실적 · 특허 · 성능은 만들지 않았다. Design Partner는 모두 TARGET · 미확보, 성능은 Target, 가격 · 원가 · 매출은 가정으로 표기했다.',
           '유지한 외부 수치는 재확인했다: IFR World Robotics 2026(2026-09-24, 가동 약 500만 대 · 2025년 60만 대+ 설치 · 2026F 65.5만 · 2029F 80.6만), IFR Robot Density(2026-04, 한국 1,220대/직원 1만 명 · 2025년 3.0만 대 설치), BCG(2026-04, TCO의 약 75%가 초기 셋업 · 재설계, Software-defined 접근의 절감 잠재력 최대 50%). BCG 50%는 우리 제품의 효과로 쓰지 않았다.',
           '기존 Deck의 "사람 개입 −30%", OEM 매출 302억~1,810억, 초기 기회 ₩75억 계산은 검증 근거가 없어 삭제했다.']: bullet(t_)
heading('8. Concept Rendering 통일 기준 — SoftHand-4 Design Language')
table([['요소', '고정 기준']] + [list(r) for r in DESIGN_LANG], [4.0, 13.0], first_col_bold=True)
para('적용: 표지 · 03 제품 · 04 Cutaway · 05 머신텐딩 Cell · 06 6단계 Workflow · 10 Robot A/B · 12 공장/주방 벤치 · 16 Closing · A9 Screwdriver Demo를 모두 같은 3D 모델로 재렌더링. 문제 장표의 전용 그리퍼 이미지와 A14의 천장형 주방 Future Vision 이미지만 원본 유지.', 9, color=GRAY)
heading('9. 다음 단계 권고')
for t_ in ['Founder 정보(14) 입력 — 외부 제출 전 필수. 가장 약한 질문(Q17)이 이 장표에 달려 있다.',
           '창업 후 90일 내 고객 인터뷰 30곳으로 첫 구매자 가설(05)과 지불의사(07)를 검증하고, Design Partner 후보를 실명 · 상태(MOU/LOI)로 갱신.',
           '가격 · 원가 가정(A10)을 공급사 견적 · BOM으로 갱신하고 Base Case(A11)를 재계산.',
           '실물 Prototype 사진 · 무편집 시험 영상이 생기면 Concept Rendering을 순서대로 교체.']: bullet(t_)
# footer page numbers
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = fp.add_run('SoftHand IR Deck Revision Report  ·  대외비  ·  '); set_font(r, 8, False, GRAY)
fld1 = OxmlElement('w:fldSimple'); fld1.set(qn('w:instr'), 'PAGE'); rr = OxmlElement('w:r'); t = OxmlElement('w:t'); t.text = '1'; rr.append(t); fld1.append(rr); fp._p.append(fld1)
z = doc.settings.element.find(qn('w:zoom'))
if z is not None and z.get(qn('w:percent')) is None: z.set(qn('w:percent'), '100')
doc.save(OUT_DOCX)
print('ok')
