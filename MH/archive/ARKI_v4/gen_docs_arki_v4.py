# Generate the ARKI IR documents (docs/*.md) from model.json, sources.json and the deck text log.
#   python3 ARKI/source/gen_docs.py      (run after model.py and build.py)
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DOCS = os.path.join(ROOT, 'docs')
os.makedirs(DOCS, exist_ok=True)
M = json.load(open(os.path.join(HERE, 'model.json'), encoding='utf-8'))
SRC = json.load(open(os.path.join(HERE, 'sources.json'), encoding='utf-8'))
DT = json.load(open(os.path.join(HERE, '_deck_text.json'), encoding='utf-8'))
import common; common.load()
import slides_appx as SA            # QA list, scorecard (single source with the deck)

S = M['scenarios']; B = S['B']; Y = M['years']
IN = {d['key']: d for d in M['inputs']}
def v(k, s='B'): return IN[k]['vals'][s]
def eok(x, d=1): return f"{x / 1e4:,.{d}f}"
def man(x, d=0): return f"{x:,.{d}f}"
def pct(x, d=0): return f"{x * 100:.{d}f}%"
HH = M['household']; h3, h5 = HH['purchase_direct_Y3'], HH['purchase_direct_Y5']; r3h, r5h = HH['rental_direct_Y3'], HH['rental_direct_Y5']
R3, R5 = M['rental']['Y3'], M['rental']['Y5']; C3, C5 = M['care']['Y3'], M['care']['Y5']; CO = M['cons']
MK = M['market']['B']; TP = M['tips']; VA = M['value']; PI = M['partner_irr']
HEADER = '> ARKI Robotics (가칭) · TIPS 창업기업 IR · Draft v4 · 2026-10-08 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·파트너·투자유치 없음.\n'

TIPSIFY = [('내가 실제 Seed VC라면', 'TIPS 운영사 심사역이라면'), ('현재 자료로 20억원을 집행하면', '현재 자료로 운영사 투자 · TIPS 추천을 하면'),
           ('Robotics Hardware Seed의 일반 기준', '로봇 하드웨어 초기 투자의 일반 기준'), ('Seed Close 또는 범위 수정', '운영사 투자 · TIPS 신청 또는 범위 수정'),
           ('실제 Seed 심사역 관점의', '운영사 심사역 · TIPS 평가위원 관점의'), ('Seed 판단의 핵심 4요소', '투자 판단의 핵심 4요소'),
           ('Seed 판단의 1순위', '투자 · TIPS 판단의 1순위'), ('Seed 판단 1순위', '투자 · TIPS 판단 1순위'), ('Seed 자금이 끝까지 소진되기 전', '자금이 끝까지 소진되기 전'),
           ('Seed 자본이 "Option 매입"으로', '초기 자금이 "Option 매입"으로'), ('Seed 90일', '과제 첫 90일'), ('(Seed 범위)', '(TIPS 기간)'), ('Seed M0~M3', '과제 M0~M3'),
           ('Seed 기간 또는 이후 목표', 'TIPS 기간 또는 이후 목표'), ('Seed 기간', 'TIPS 기간'), ('Seed에는', 'TIPS 기간에는'), ('Seed는', '초기에는'),
           ('84㎡ Full-scale Mock-up', '실물 크기 목업 (대표 평면 기준)'), ('84㎡ 11자 Full-scale Mock-up', '대표 평면 기준 실물 크기 목업'),
           ('Seed', '초기')]

def tipsify(t):
    for a, b in TIPSIFY:
        t = t.replace(a, b)
    return t

def write(name, body):
    if name[:2] not in ('00', '01', '02'):      # hand-written docs still cite v1 slide numbers -> current locations (본문 쪽 / 부록 코드)
        body = common.remap(body)
    if name[:2] not in ('00', '01', '02', '07'):
        body = tipsify(body)
    with open(os.path.join(DOCS, name), 'w', encoding='utf-8') as f:
        f.write(body.strip() + '\n')
    print('wrote', name)

def md_table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '|'.join(['---'] * len(header)) + '|']
    for r in rows:
        out.append('| ' + ' | '.join(str(c).replace('\n', ' ').replace('|', '/') for c in r) + ' |')
    return '\n'.join(out)

# ---------------------------------------------------------------- 01 / 02 deck scripts
def deck_script(appendix):
    meta = [m for m in DT['meta'] if ((not isinstance(m['no'], int)) == appendix)]
    out = []
    for m in meta:
        no = m['no'] if appendix else f"{m['no']:02d}"
        out.append(f"## {no}. {m['title']}\n")
        if m['q']:
            out.append('**답하는 투자 질문**: ' + ' · '.join(f"Q{q}" for q in m['q']) + '\n')
        lines = [t for t in DT['log'].get(m['id'], []) if not re.fullmatch(r'Q\d', t.strip())]
        out.append('**화면 문구** (표기 순서)\n')
        out.append('```text')
        out.extend(lines)
        out.append('```\n')
        out.append(f"**그림 구성**: {m['visual']}\n")
        out.append(f"**도표**: {m['chart']}\n")
        out.append(f"**발표 메모**: {m['note']}\n")
    return '\n'.join(out)

Q6 = '\n'.join(f"{i}. {q}" for i, q in enumerate(['누가 가장 먼저 돈을 내는가?', '고객이 얼마까지 지불할 가능성이 있는가?', '한 세대 설치 시 회사가 얼마를 버는가?',
                                                   '집마다 다른 주방을 얼마나 표준화할 수 있는가?', '설치대수가 늘어날수록 반복매출과 Gross Margin이 개선되는가?',
                                                   'TIPS 24개월 뒤 어떤 핵심 위험이 제거되는가?'], 1))
_NM = sum(1 for m in DT['meta'] if isinstance(m['no'], int))
write('01_Main_Deck_Script.md', f"""# 01. 본문 IR 덱 — 장별 문구 · 그림 · 발표 메모 ({_NM}장)

{HEADER}
- 파일: `ARKI/ARKI_Robotics_TIPS_IR_Deck.pptx` (본문 1~{_NM}쪽 + 부록 A~F, 16:9) · 본문만 PDF `ARKI_Robotics_TIPS_IR_Deck_Main.pdf` · 전체 검토용 PDF `ARKI_Robotics_TIPS_IR_Deck_preview.pdf`
- 구성: 1~14쪽 = IR (TIPS 연구개발계획서 별첨 6항목: 문제 · 솔루션 / 시장 / 경쟁 / 비즈니스 모델 / 팀 / 사업화 로드맵 · 매출 목표) · 15~{_NM}쪽 = TIPS 과제 요약 (본문1 항목: 목표 · 성과지표 / 연차 목표 · 일정 / 개발 방법 · 선행 개발 / 추진 체계 · 지식재산 · 안전 / 연구개발비 · 자금)
- 아래 "화면 문구"는 덱 생성 코드가 화면에 그린 텍스트를 그대로 추출한 것 (표는 `|`로 열 구분, `[TAG]`는 숫자 태그).
- 3D 그림은 `ARKI/render3d`에서 생성 (충돌검사 결과는 각 PNG 옆 JSON의 `ik.pen`, 관통 cm).

---

{deck_script(False)}""")

write('02_Appendix_Script.md', f"""# 02. 부록 — 장별 문구 · 그림 · 발표 메모 (A~F)

{HEADER}
---

{deck_script(True)}""")

# ---------------------------------------------------------------- 03 sources
rows = [[d['id'], d['item'], d['value'], d['basis'], d['source'], d['used_in']] for d in SRC]
write('03_Market_Data_and_Sources.md', f"""# 03. 사용한 시장 데이터와 Source

{HEADER}
## 조사 방법과 한계

- 조사일: 2026-10-07. 웹 검색 결과(보도·공개자료·공식 발표 인용)를 기준으로 수집. 이 실행 환경에서는 국가데이터처·국토부·KOSIS 원문 사이트에 직접 접속할 수 없어, **공식 통계는 해당 기관 발표를 인용한 보도로 확인**함.
- 외부 제출 전 필수: S1~S6 (주택·공급 통계)는 국가데이터처 「2025 인구주택총조사 결과」(2026.7.28) 및 국토교통부 「'25년 12월 주택통계」(2026.1.30) 보도자료 원문과 대조.
- 블로그·홍보성 기사만으로 핵심 시장숫자를 판단하지 않음. Kitchen 단독 Remodeling 가격처럼 공식 자료가 없는 항목은 FACT로 쓰지 않고 ASSUMPTION / TO BE VALIDATED로 표기.
- 가격 Benchmark(USD)는 공개 판매가·유통가. 환율 1,400원/USD는 환산용 ASSUMPTION.

## Source 목록

{md_table(['ID', '항목', '값', '기준', 'Source (URL)', '사용 위치 (Slide)'], rows)}

## 확인하지 못한 데이터 (Data Gap)

{md_table(['항목', '상태', '대체 방법 (Seed 90일)'], [
    ['Kitchen 단독 Remodeling 가격대 (일반 / Premium)', '공식 통계 없음 → ASSUMPTION (600~1,500만원 / 2,000~4,000만원)', '한샘·리바트·LX·지역 인테리어 견적 20건 수집'],
    ['연간 Kitchen 교체 세대 수', '공식 통계 없음 → 교차검증 DERIVED (29.0만·30.3만) + ASSUMPTION 30만', 'Partner 판매 Data · 업계 인터뷰로 보정'],
    ['식기세척기 가구 보급률 (최신)', '2019~2020 업계 추정 10%대만 확인 → TBV', 'Premium 상담 고객 조사 문항으로 직접 측정'],
    ['Clean-up 소요시간', '생활시간조사 세부 항목(설거지) 미확인 → ASSUMPTION 40분/일', 'Time-diary 30세대 · 7일'],
    ['아파트 매매거래 중 아파트 비중 (2025 연간)', '월별 수치만 확인 → ASSUMPTION 70%', '부동산원 R-ONE 연간 아파트 거래량 확인'],
    ['협동로봇 국내 OEM 견적', '공개가 없음', 'OEM 3곳 RFQ (100대 기준)'],
    ['로봇 안전·KC 인증 비용', '공개 자료 없음 → ASSUMPTION 0.7억원 (Seed 범위)', '인증기관 사전상담 견적'],
    ['신축 Robot-ready Option 선택률', '선례 없음 → ASSUMPTION 10%', '신축 계약자 10명 Interview · 옵션 박람회 Test'],
])}
""")

# ---------------------------------------------------------------- 04 tag register
inrows = []
for d in M['inputs']:
    vals = d['vals']
    f = lambda x: (', '.join(f"{y:g}" for y in x) if isinstance(x, list) else f"{x:g}")
    same = vals['C'] == vals['B'] == vals['U']
    inrows.append([d['tag'], d['key'], d['desc'], d['unit'], f(vals['B']) if same else f"C: {f(vals['C'])} / B: {f(vals['B'])} / U: {f(vals['U'])}", d['src']])
outrows = [
    ['DERIVED', '아파트 수 (2025)', f"{MK['apt'] / 10:,.0f}만호", '총주택 2,018.1만 × 65.8%'],
    ['DERIVED', 'Kitchen 교체 세대 교차검증 ①·②', f"{MK['tri1'] / 10:.1f}만 · {MK['tri2'] / 10:.1f}만/년", 'A2'],
    ['DERIVED', 'TAM / SAM / SOM(Y5)', f"{MK['tam'] / 1e4:.2f}조 / {MK['sam']:,.0f}억 / {MK['som']:.1f}억원", 'A2·18장'],
    ['DERIVED', '가치 Anchor (월)', f"{VA['value']:.0f}만원 (Range {VA['lo']:.0f}~{VA['hi']:.0f})", '14장'],
    ['DERIVED', '세대 5년 매출 / Contribution (구매, Y3·Y5)', f"{man(h3['rev5'])}만원 / {man(h3['contrib5'])}·{man(h5['contrib5'])}만원", '15장'],
    ['DERIVED', 'Rental 월 Contribution · Payback (Y3·Y5)', f"{R3['contrib_m']:.1f}·{R5['contrib_m']:.1f}만원 · {R3['payback']:.0f}·{R5['payback']:.0f}개월", 'A12'],
    ['DERIVED', 'Rental Partner IRR (Base)', f"{PI['B']['irr_y'] * 100:.1f}% (연체·해지 미반영)", 'A12'],
    ['DERIVED', 'Care Margin (Y3·Y5)', f"{pct(C3['margin'])} · {pct(C5['margin'])}", 'A13'],
    ['DERIVED', 'Consumables 연 매출 · Contribution / Robot', f"{CO['rev']:.1f} · {CO['contrib']:.1f}만원", 'A13'],
    ['DERIVED', 'Y5 매출 C / B / U', f"{eok(S['C']['rev'][4])} / {eok(B['rev'][4])} / {eok(S['U']['rev'][4])}억원", 'A14'],
    ['DERIVED', 'Y5 영업이익 C / B / U', f"{eok(S['C']['op'][4])} / {eok(B['op'][4])} / {eok(S['U']['op'][4])}억원", 'A14'],
    ['DERIVED', '5년 누적 현금흐름 최저 (Base)', f"{eok(B['min_cum_cash'])}억원", 'A14'],
    ['DERIVED', '손익분기 Kitchen (연, Y5 단가·원가)', f"{M['breakeven_kitchens']:,.0f}세대", '24장'],
    ['DERIVED', 'TIPS 24개월 회사 전체 지출 / 후속 투자 없을 때 자금 지속', f"{eok(TP['spend_total'])}억원 / {TP['runway_no_followon']:.1f}개월", 'A16'],
    ['ASSUMPTION', 'TIPS 과제 예산 (정부 · 민간 현금 · 현물)', f"{eok(TP['total'])}억원 ({eok(TP['gov'])} · {eok(TP['private_cash'], 2)} · {eok(TP['inkind'], 2)})", '본문 19쪽'],
    ['DERIVED', '정상상태 Recurring / Upgrade 비중', f"{pct(M['steady']['rec_share'])} / {pct(M['steady']['upg_share'])}", '19장'],
]
tgt = [['TARGET', '평면 분석', '30개 이상 (신축 15 · 구축 15)'], ['TARGET', 'Layout Family / Robot Architecture', '3~5 / 2~3'],
       ['TARGET', 'Standard Module 사용률', '65% (Y3) · 80% (Y5) · Kill: M18 60% 미만'], ['TARGET', '식기 정리 성공률 (사람 개입 없이)', '70% (M9 목업) · 90% (M24 가정 실증)'],
       ['TARGET', '특허 출원', '24개월 5건 (Y1 2 · Y2 3, 등록 미정)'], ['TARGET', 'Consumer Interview / Conjoint', '50명 / n≥300'],
       ['TARGET', 'Home Pilot', '3세대 (TIPS 가정 실증, 유료 목표)'], ['TARGET', 'Installation · Calibration Time', '1일·2인 · 2시간 (M24)'],
       ['TARGET', 'Patent 출원', '5~8건 (선행기술조사 후)'], ['TARGET', 'Volume (Base)', f"구축 직접 {v('rd')} · Partner {v('rp')} · 신축 Project {v('projects')}"]]
write('04_Number_Tag_Register.md', f"""# 04. FACT / DERIVED / ASSUMPTION / TARGET 구분표

{HEADER}
## Tag 정의

{md_table(['Tag', '정의', '사용 원칙'], [
    ['FACT', '공식 통계 또는 공개자료로 확인된 값', '출처 ID(S1~S32) 병기. 보도 인용은 원문 대조 필요'],
    ['DERIVED', 'FACT 또는 가정을 ARKI가 계산한 값', '산식 병기. 가정 기반 계산은 "DERIVED (from ASSUMPTION)"'],
    ['ASSUMPTION', '현재 사업가설', '검증 방법·시점 병기'],
    ['TARGET', 'Seed 기간 또는 이후 목표', 'Kill Criteria와 연결'],
    ['CONCEPT', '실물 없는 설계 개념', 'Concept Layout·단면·Module 구성'],
    ['TO BE VALIDATED (TBV)', '미확인 사실, 검증 방법 확정', '본문 각주'],
    ['FUTURE CONCEPT', '현재 존재하지 않는 제품', 'V2 ASSIST · V3 COOK · Tool 확장'],
])}

## 입력값 전체 ({len(M['inputs'])}개, 재무모델 `Inputs` · `Inputs_Yearly` 시트와 동일)

연도별 값은 Y1~Y5 순서. C = Conservative, B = Base, U = Upside. 금액 단위 만원.

{md_table(['Tag', 'Key', '항목', '단위', '값', 'Source / Note'], inrows)}

## 주요 산출값 (DERIVED)

{md_table(['Tag', '항목', '값', '위치'], outrows)}

## 주요 목표값 (TARGET)

{md_table(['Tag', '항목', '목표'], tgt)}
""")

# ---------------------------------------------------------------- 05 financial model
def fm_table(s):
    L = S[s]
    lines = [('구축 직접판매 Kitchen (세대)', 'rd', 0), ('구축 Partner Kitchen (세대)', 'rp', 0), ('신축 Robot-ready 설치 (세대)', 'ni', 0),
             ('Robot 설치 (대)', 'pl', 0), ('Installed Robot 기말 (대)', 'base_end', 0), ('신축 Backlog (세대)', 'backlog', 0),
             ('Kitchen Build', 'rev_kitchen', 1), ('설치·Calibration', 'rev_comm', 1), ('Robot Hardware', 'rev_robot', 1),
             ('Rental (ARKI 보유)', 'rev_rental', 1), ('Care', 'rev_care', 1), ('Consumables', 'rev_cons', 1), ('Upgrade', 'rev_upg', 1),
             ('**매출**', 'rev', 1), ('COGS', 'cogs', 1), ('**매출총이익**', 'gp', 1), ('매출총이익률', 'gm', 2),
             ('채널·변동판매비 (Partner·CAC·신축 BD)', None, 3), ('**Contribution**', 'contrib', 1), ('Opex', 'opex', 1),
             ('**영업이익 (근사)**', 'op', 1), ('Rental 자산 취득', 'capex', 1), ('누적 현금흐름', 'cum_cash', 1)]
    rows = []
    for lab, k, kind in lines:
        if kind == 0: vals = [f"{L[k][t]:,.0f}" for t in range(5)]
        elif kind == 1: vals = [eok(L[k][t]) for t in range(5)]
        elif kind == 2: vals = [pct(L[k][t]) if L['rev'][t] else '—' for t in range(5)]
        else: vals = [eok(L['ch_partner'][t] + L['ch_cac'][t] + L['ch_bd'][t]) for t in range(5)]
        rows.append([lab] + vals)
    return md_table(['억원 / 수량', *Y], rows)

write('05_Financial_Model_5Y.md', f"""# 05. 5-Year Financial Model (Bottom-up · 3 Scenario)

{HEADER}
- 수식 모델: `ARKI/ARKI_Robotics_Financial_Model.xlsx` (Inputs → FM_Conservative / FM_Base / FM_Upside → Scenario_Summary). 1,778개 수식, LibreOffice 재계산 오류 0, `model.py`와 836개 값 교차검증 일치.
- 단위: 억원 (수량 제외). Year 정의: Y1 = TIPS 과제 M1~M12, Y2 = M13~M24 (TIPS 기간, 대표 + 연구원 4~5명), Y3 = 후속 투자 이후 첫 해.
- 전부 DERIVED (from ASSUMPTION · TARGET). 실적 아님.

## Driver 구조

{md_table(['Driver', '산식', '주요 가정 (Base)'], [
    ['Kitchen Project', '구축 직접 + 구축 Partner + 신축 설치', f"직접 {v('rd')} · Partner {v('rp')}"],
    ['Robot Unit', '구축 Kitchen × Attach + 신축 설치 × 입주 Attach + Robot-ready Only Pool × 후속 Attach', f"Attach {pct(v('attach')[2])} · 후속 {pct(v('later_attach'))}/년 · 신축 {pct(v('new_attach'))}"],
    ['Robot-ready Only', '(1 − Attach) 누적 Pool', '후속 Attach 대상'],
    ['Rental Unit', 'Robot × Rental 비중; Y2~Y3 ARKI 보유, Y4~ Rental Partner 보유', f"Rental 비중 {', '.join(pct(x) for x in v('rental_share'))}"],
    ['Care / Consumables Base', '평균 가동 대수 × 가입·구매율 × 요금', f"Care 가입 {pct(v('care_attach'))} · Kit 구매 {pct(v('cons_attach'))}"],
    ['Upgrade', '전년 설치 × SW 구매율 × 60만 + 2년 전 설치 × Tool 구매율 × 80만', f"SW {pct(v('sw_attach'))} · Tool {pct(v('tool_attach'))}"],
    ['신축', 'Project 계약 → 2년 후 입주 설치, Project당 800세대 × Option 선택률', f"계약 {v('projects')} · 선택률 {pct(v('option_rate'))}"],
    ['Cost', 'Robot BOM · Kitchen Module (Standard Module 사용률 연동) · 설치 · 물류 · Warranty · Care · Consumables COGS · Partner 수수료 · CAC · R&D·Opex', f"BOM {v('bom')} · SMR {[pct(x) for x in v('smr')]}"],
])}

## 시나리오 정의

{md_table(['변수', 'Conservative', 'Base', 'Upside', '원칙'], [
    ['Robot ASP (만원)', v('p_robot', 'C'), v('p_robot'), v('p_robot', 'U'), 'Upside 가격 인상 없음'],
    ['Rental 월 요금 (만원)', v('p_rent', 'C'), v('p_rent'), v('p_rent', 'U'), ''],
    ['Robot BOM Y5 (만원)', v('bom', 'C')[4], v('bom')[4], v('bom', 'U')[4], '물량·OEM'],
    ['Standard Module 사용률 Y5', pct(v('smr', 'C')[4]), pct(v('smr')[4]), pct(v('smr', 'U')[4]), '표준화'],
    ['설치원가 Y5 (만원/대)', v('comm_cost', 'C')[4], v('comm_cost')[4], v('comm_cost', 'U')[4], 'Installation Cost 하락'],
    ['Partner Kitchen Y5', v('rp', 'C')[4], v('rp')[4], v('rp', 'U')[4], 'Partner Distribution 확대'],
    ['신축 Project 계약 (Y3~Y5)', v('projects', 'C'), v('projects'), v('projects', 'U'), ''],
    ['Robot Attach (구축)', pct(v('attach', 'C')[2]), pct(v('attach')[2]), pct(v('attach', 'U')[2]), ''],
    ['Failure (고장 방문/년)', v('corrective', 'C'), v('corrective'), v('corrective', 'U'), ''],
    ['Opex', '동일', '동일', '동일', '고정 계획 (인원 6→9→20→32→42명)'],
])}

## Base

{fm_table('B')}

## Conservative

{fm_table('C')}

## Upside

{fm_table('U')}

## 해석

- Base Y5 매출 {eok(B['rev'][4])}억원, 매출총이익률 {pct(B['gm'][4])}, Contribution {eok(B['contrib'][4])}억원, 영업이익 {eok(B['op'][4])}억원 → **5년 내 흑자 전환 없음** (Hardware 회사의 일반 경로). 손익분기는 Y5 단가·원가 기준 연 약 {M['breakeven_kitchens']:,.0f}세대 (Y6 이후, 신축 Backlog 설치 시점).
- 5년 누적 현금흐름 최저점 (Base): {eok(B['min_cum_cash'])}억원 → 필요 외부자본 = TIPS 24개월 (정부지원 {eok(TP['gov'], 0)}억 + 운영사 투자 {eok(v('op_invest'), 0)}억 + 후속 투자 {eok(v('followon'), 0)}억) + Series A 약 80~100억 (Y3~Y4 영업손실 {eok(-(B['op'][2] + B['op'][3]))}억원 + Buffer) + Series B.
- Conservative: Y5 Contribution {eok(S['C']['contrib'][4])}억원 ≈ 0 → 가격·BOM 가정이 깨지면 물량을 늘려도 가치가 생기지 않음 → **Kill Criteria M24 (Scale 투자 보류)** 시나리오.
- Upside: 가격 동일, Partner 물량·표준화·설치원가 차이만으로 Y5 매출 {eok(S['U']['rev'][4])}억원, 영업이익 {eok(S['U']['op'][4])}억원.
- 신축은 계약 후 2년 Lag로 5년 매출 기여가 Y5에 한정 (Base Y5 {B['ni'][4]:.0f}세대). Y5 말 Backlog {B['backlog'][4]:.0f}세대가 Y6~Y7 매출로 이어짐.
- Revenue Mix (Base Y5): Build {pct(B['build'][4] / B['rev'][4])} · Robot {pct(B['rev_robot'][4] / B['rev'][4])} · Recurring {pct(B['recurring'][4] / B['rev'][4])} · Upgrade {pct(B['rev_upg'][4] / B['rev'][4])}. 정상상태(DERIVED) Recurring 약 {pct(M['steady']['rec_share'])} + Upgrade 약 {pct(M['steady']['upg_share'])}.
""")

# ---------------------------------------------------------------- 06 unit economics
def hh_rows():
    keys = [('Robot-ready Kitchen 증분', 'R', 'kitchen'), ('설치·Calibration', 'R', 'comm'), ('Robot (구매)', 'R', 'robot'),
            ('Rental 60개월', 'R', 'rental'), ('Care Basic 5년', 'R', 'care'), ('Consumables 5년', 'R', 'cons'),
            ('Software Skill (기대값)', 'R', 'sw'), ('Tool (기대값)', 'R', 'tool'), ('**5년 매출**', None, 'rev5'),
            ('Kitchen Module 원가', 'C', 'kitchen'), ('Robot BOM (Rental: 순감가)', 'C', 'robot'), ('Rental 금융비용', 'C', 'finance'),
            ('설치·Calibration 원가', 'C', 'comm'), ('물류', 'C', 'log'), ('Warranty Reserve', 'C', 'warranty'),
            ('Care 원가 5년', 'C', 'care'), ('Consumables 원가', 'C', 'cons'), ('Upgrade 원가', 'C', 'sw+tool'),
            ('획득비용 (CAC)', 'C', 'channel'), ('**5년 매출총이익 (CAC 전)**', None, 'gp5'), ('**Lifetime Contribution**', None, 'contrib5'),
            ('Contribution Margin', None, 'cm5')]
    rows = []
    for lab, part, k in keys:
        vals = []
        for h in (h3, h5, r3h, r5h):
            if part is None: x = h[k]
            elif k == 'sw+tool': x = h['C'].get('sw', 0) + h['C'].get('tool', 0)
            else: x = h[part].get(k, 0)
            vals.append(pct(x, 1) if k == 'cm5' else man(x))
        rows.append([lab] + vals)
    return md_table(['만원', '구매 · Y3 원가', '구매 · Y5 원가', 'Rental · Y3 원가', 'Rental · Y5 원가'], rows)

sh, scn = M['sens_household'], M['sens_company']
write('06_Unit_Economics_Household_Rental_Care.md', f"""# 06. Household · Rental · Care · Consumables Economics

{HEADER}
수식: xlsx `Household` · `Unit_Economics` · `Sensitivity` 시트. 전부 DERIVED (from ASSUMPTION). 단위 만원.

## 1. 가격 가설 (Purchase · Rental)

{md_table(['근거', '내용', 'Tag'], [
    ['Cost Floor', f"Robot BOM {v('bom')[2]:,} (Y3) / {v('bom')[4]:,} (Y5) → GM 30% Robot 가격 {v('bom')[2] / 0.7:,.0f} / {v('bom')[4] / 0.7:,.0f}만원 · Rental 마진 20% 요금 월 {R3['fee_at_20']:.1f} / {R5['fee_at_20']:.1f}만원", 'DERIVED'],
    ['Market Reference', '1X NEO $20,000 또는 월 $499 · Sunday Memo 양산 $10k 미만 목표 · Moley £248,000 · 신축 유상옵션 분양가의 9.7% · 30평대 전체 리모델링 약 3,000만원(2019)', 'FACT'],
    ['Value Anchor', f"Clean-up 40분/일 (A) × 30일 × 가사서비스 1.5만원/h (F) × 자동화 60% (A) = 월 {VA['value']:.0f}만원 (Range {VA['lo']:.0f}~{VA['hi']:.0f})", 'DERIVED'],
    ['가격 가설 (구매)', f"Robot-ready {v('p_rr')} + Robot {v('p_robot'):,} + 설치 {v('p_comm')} = ARKI {v('p_rr') + v('p_robot') + v('p_comm'):,}만원 (Kitchen 공사비 별도)", 'ASSUMPTION'],
    ['가격 가설 (Rental)', f"Robot-ready {v('p_rr')} + 설치 {v('p_comm')} + 월 {v('p_rent')}만원 × 60개월 (Care Basic · Grip Kit 포함)", 'ASSUMPTION'],
    ['WTP Test Point', 'Robot 990 / 1,290 / 1,490 / 1,790만원 · Rental 월 19 / 25 / 29 / 33 / 39만원', 'TARGET (조사 설계)'],
])}

**핵심 Gap**: 가치 Anchor(월 {VA['lo']:.0f}~{VA['hi']:.0f}만원) < 원가 기반 Rental(월 {R5['fee_at_20']:.0f}~{R3['fee_at_20']:.0f}만원). V1 단일 Task의 "가사 대체 가치"만으로는 가격 정당화가 어려움 → (1) Premium Kitchen Amenity로서의 가치 (2) V2 Task 확장 (3) BOM 절감이 필요하며, WTP 검증이 Seed 1순위.

## 2. Household Economics — 구축 Premium 1세대 · 5년 · 직접판매

구매 모델은 Care 가입 세대 기준, Software·Tool은 구매율 반영 기대값. Rental은 ARKI 자산 보유 가정 (잔존가치 15% 회수, 금융비용 8%).

{hh_rows()}

- 구매 · Y3 원가: Year 0 매출 {man(h3['y0'])}만원이 5년 매출의 {pct(h3['y0'] / h3['rev5'])} → 세대 경제성은 **Robot ASP(WTP) × BOM**이 결정.
- Recurring(Care+Consumables) 5년 {man(h3['recurring5'])}만원 → 보완 역할, 핵심 Value Driver 아님.
- Partner 경유 시 Contribution 약 {man(h3['contrib5'] - HH['purchase_partner_Y3']['contrib5'])}만원 감소 (수수료 {pct(v('partner_margin'))}).

## 3. Unit Economics 요약

{md_table(['Unit', 'Y3 원가', 'Y5 원가', '조건 / 해석'], [
    ['Purchase Year-0 Contribution (CAC 포함)', man(h3['y0'] - (h3['C']['robot'] + h3['C']['kitchen'] + h3['C']['comm'] + h3['C']['log'] + h3['C']['warranty'] + h3['C']['channel'])),
     man(h5['y0'] - (h5['C']['robot'] + h5['C']['kitchen'] + h5['C']['comm'] + h5['C']['log'] + h5['C']['warranty'] + h5['C']['channel'])), 'BOM 하락이 핵심'],
    ['Rental 월 Contribution · Margin', f"{R3['contrib_m']:.1f} · {pct(R3['margin'])}", f"{R5['contrib_m']:.1f} · {pct(R5['margin'])}", '월 33만원 기준'],
    ['Rental Payback (개월)', f"{R3['payback']:.0f}", f"{R5['payback']:.0f}", f"Partner 허들 36개월 → BOM ≤ {R3['bom_max']:,.0f}만원"],
    ['Care Contribution · Margin (연)', f"{C3['contrib']:.1f} · {pct(C3['margin'])}", f"{C5['contrib']:.1f} · {pct(C5['margin'])}", '방문 1.5회 이하 · 방문원가 9만원 이하'],
    ['Consumables Contribution · Margin (연)', f"{CO['contrib']:.1f} · {pct(CO['margin'])}", f"{CO['contrib']:.1f} · {pct(CO['margin'])}", '교체주기 미실측'],
])}

## 4. Rental Economics

{md_table(['월 원가 Build-up (Robot 1대)', 'Y3', 'Y5'], [
    ['감가 (BOM × 85% ÷ 60)', f"{R3['lines']['dep']:.2f}", f"{R5['lines']['dep']:.2f}"],
    ['금융비용 (평균잔액 × 8% ÷ 12)', f"{R3['lines']['fin']:.2f}", f"{R5['lines']['fin']:.2f}"],
    ['Care 원가 ÷ 12', f"{R3['lines']['care']:.2f}", f"{R5['lines']['care']:.2f}"],
    ['Grip Kit 원가 ÷ 12', f"{R3['lines']['grip']:.2f}", f"{R5['lines']['grip']:.2f}"],
    ['Failure Reserve (BOM × 4% ÷ 60)', f"{R3['lines']['reserve']:.2f}", f"{R5['lines']['reserve']:.2f}"],
    ['**월 원가**', f"{R3['cost_m']:.2f}", f"{R5['cost_m']:.2f}"],
    ['월 요금 (가정)', f"{R3['fee']:.1f}", f"{R5['fee']:.1f}"],
    ['**월 Contribution**', f"{R3['contrib_m']:.2f}", f"{R5['contrib_m']:.2f}"],
    ['마진 20% 확보 요금', f"{R3['fee_at_20']:.1f}", f"{R5['fee_at_20']:.1f}"],
    ['Payback (개월, 금융 제외)', f"{R3['payback']:.1f}", f"{R5['payback']:.1f}"],
    ['36개월 Payback 최대 BOM', f"{R3['bom_max']:,.0f}", f"{R5['bom_max']:,.0f}"],
])}

- 구조: Seed = ARKI 직접 Rental Pilot (소량) · Scale(Y4~) = Rental / Capital Partner가 Robot을 ASP의 {pct(v('wholesale'))}({PI['B']['price']:,.0f}만원)에 매입하고 월 {v('p_rent') - v('partner_fee'):.0f}만원 순유입 · 잔존 {PI['B']['resid']:,.0f}만원 → Partner IRR 약 {PI['B']['irr_y'] * 100:.1f}% (Conservative {PI['C']['irr_y'] * 100:.1f}%). 연체·중도해지·회수비용 미반영.
- 결론: Y3 원가로는 Payback {R3['payback']:.0f}개월 > 36개월 → **Rental은 BOM ≤ {R3['bom_max']:,.0f}만원 달성 전까지 Pilot 규모로 제한**.

## 5. Care Economics

{md_table(['Care Basic (Robot 1대·년)', 'Y3', 'Y5', 'Tag'], [
    ['요금', f"{C3['fee']:.0f}", f"{C5['fee']:.0f}", 'ASSUMPTION'],
    ['정기 방문 (횟수 × 원가)', f"{C3['visits']:.1f}", f"{C5['visits']:.1f}", 'ASSUMPTION (Y3 2회×11만, Y5 1.5회×8만)'],
    ['고장 방문 (0.6회 × 18만원)', f"{C3['corrective']:.1f}", f"{C5['corrective']:.1f}", 'ASSUMPTION'],
    ['Cloud·Software', f"{C3['cloud']:.1f}", f"{C5['cloud']:.1f}", 'ASSUMPTION'],
    ['**Contribution · Margin**', f"{C3['contrib']:.1f} · {pct(C3['margin'])}", f"{C5['contrib']:.1f} · {pct(C5['margin'])}", 'DERIVED'],
])}

- 포함: 정기 안전점검 · Calibration · Remote Diagnosis · Joint / Rail / Vision 상태 · Consumables Check · Software Update · A/S 공임.
- 참고 (FACT): 삼성·LG 가전 A/S 출장비 2.8만원 (2026, 소비자 부과분) — ARKI 실제 방문 원가(인건비·이동)와 다름.
- Care가 Profit Center가 되는 조건: 원격진단으로 정기방문 1.5회 이하 + Route Density로 방문원가 9만원 이하 → Y5 Margin {pct(C5['margin'])}. Y3에는 Profit Center 아님.

## 6. Consumables Economics

{md_table(['Kit', '구성', '가격(만원)', '교체/년', '연 List'], [[k, {'Grip Kit': 'Finger Pad · Food-contact Tip · Suction Cup', 'Cleaning Kit': 'Brush · Wiper · Cleaning Pad', 'Protection Kit': 'Sensor Cover · Protective Sleeve · Seal'}[k], f"{p:g}", f"{n:g}", f"{p * n:g}"] for k, p, n in CO['kits']] + [['합계', '', '', '', f"{CO['list_y']:g}"]])}

- 구매율 {pct(CO['attach'])} → 연 매출 {CO['rev']:.1f}만원 · 원가 {pct(v('cons_cogs'))} → Contribution {CO['contrib']:.1f}만원/Robot.
- 설계 원칙: 억지 Lock-in이 아니라 위생 · 마모 · Grip 성능 유지 · 식품접촉부 교체 · 안전성 유지. Care Plus(연 72만원)에 정기 교체 포함 가능.
- 검증 KPI: Replacement Cycle · Cost per Kit · Annual Consumables Revenue per Robot · Gross Margin · Care Attach Rate.

## 7. 5-Year Household Economics 요약 (대표 1세대)

{md_table(['', '구매 · Y3 원가', '구매 · Y5 원가', 'Rental · Y3 원가', 'Rental · Y5 원가'], [
    ['Initial (Kitchen Module + Robot / 설치)', man(h3['y0']), man(h5['y0']), man(r3h['y0']), man(r5h['y0'])],
    ['Recurring (Rental 또는 Care + Consumables)', man(h3['recurring5']), man(h5['recurring5']), man(r3h['R']['rental'] + r3h['R']['cons']), man(r5h['R']['rental'] + r5h['R']['cons'])],
    ['Expansion (Tool · Software 기대값)', man(h3['R']['sw'] + h3['R']['tool']), man(h5['R']['sw'] + h5['R']['tool']), man(r3h['R']['sw'] + r3h['R']['tool']), man(r5h['R']['sw'] + r5h['R']['tool'])],
    ['5-Year Revenue', man(h3['rev5']), man(h5['rev5']), man(r3h['rev5']), man(r5h['rev5'])],
    ['5-Year Gross Profit', man(h3['gp5']), man(h5['gp5']), man(r3h['gp5']), man(r5h['gp5'])],
    ['Expected Service Cost (Care 원가 5년)', man(h3['C']['care']), man(h5['C']['care']), man(r3h['C']['care']), man(r5h['C']['care'])],
    ['Lifetime Contribution', man(h3['contrib5']), man(h5['contrib5']), man(r3h['contrib5']), man(r5h['contrib5'])],
])}

## 8. Sensitivity (Top 3 Critical Variable = Customer WTP · Robot BOM · Partner Distribution)

세대 5년 Contribution (구매·Y3, Base {sh['base']:,.0f}만원):

{md_table(['변수', '불리 Δ (만원)', '유리 Δ (만원)'], [[d['name'], f"{d['lo']:,.0f}", f"+{d['hi']:,.0f}"] for d in sh['items']])}

회사 Y5 Contribution (Base {scn['base'] / 1e4:,.1f}억원):

{md_table(['변수', '불리 Δ (억원)', '유리 Δ (억원)'], [[d['name'], f"{d['lo'] / 1e4:,.1f}", f"+{d['hi'] / 1e4:,.1f}"] for d in scn['items']])}
""")

# ---------------------------------------------------------------- 07 TIPS budget plan
_a = {d['key']: d['vals']['B'] for d in M['inputs']}
_ppl = [_a['fte'][t] * _a['loaded'] for t in (0, 1)]
_sp = [('인건비', _ppl, f"평균 {_a['fte'][0]:.1f}명 · {_a['fte'][1]:.0f}명 × 연 {_a['loaded']:,}만원"),
       ('시제품 (로봇 · 주방)', [_a['proto'][0], _a['proto'][1]], '1차 2식 + 목업 주방 2식 (Y1) · 2차 개선 부품 (Y2)'),
       ('목업 공간', [_a['space'][0], _a['space'][1]], '약 30평 임차 + 목업 시공'),
       ('비전 · SW · 데이터', [_a['swdata'][0], _a['swdata'][1]], 'GPU · 클라우드 · 데이터 라벨링'),
       ('안전 · 시험 · 특허', [_a['cert_ip'][0], _a['cert_ip'][1]], '선행기술조사 · 출원 5건 · 공인기관 사전시험'),
       ('관리비', [_a['ga'][0], _a['ga'][1]], '법무 · 회계 · 보험 · 사무')]
_known = [sum(x[1][t] for x in _sp) for t in (0, 1)]
_sp.append(('고객 검증 · 실증', [TP['spend'][t] - _known[t] for t in (0, 1)], f"인터뷰 · 지불의사 조사 · 가정 실증 {_a['rd'][1]}세대 (실증 매출 차감)"))
write('07_TIPS_Budget_Plan.md', f"""# 07. TIPS 기간 (24개월) 연구개발비 · 자금 계획

{HEADER}
## 결론

- TIPS 과제 예산 **{TP['total'] / 1e4:.1f}억원** = 정부지원금 {TP['gov'] / 1e4:.0f}억원 (2026 일반 트랙 최대, 선정 미확정) + 민간부담 {TP['private'] / 1e4:.1f}억원 (현금 {TP['private_cash'] / 1e4:.2f} · 현물 {TP['inkind'] / 1e4:.2f}억원).
- 과제 밖 비용까지 더한 **24개월 회사 전체 지출은 약 {TP['spend_total'] / 1e4:.1f}억원** (Y1 {TP['spend'][0] / 1e4:.1f} · Y2 {TP['spend'][1] / 1e4:.1f}억원).
- 재원: TIPS {TP['gov'] / 1e4:.0f} + 운영사 투자 {_a['op_invest'] / 1e4:.0f} (요청, ASSUMPTION) + 후속 투자 {_a['followon'] / 1e4:.0f}억원 (M12 점검 뒤, TARGET) = {TP['src_total'] / 1e4:.0f}억원 → 여유 {TP['buffer'] / 1e4:.1f}억원.
- 후속 투자가 없으면 약 **{TP['runway_no_followon']:.0f}개월**까지 → 2차 시제품 · 가정 실증 범위를 줄여야 함. 창업사업화 연계 (최대 {TP['biz_link'] / 1e4:.0f}억원, 선정 뒤 별도 신청)는 미반영.
- 이전 Seed 안 (20억원 · 24개월, 재산정 25.8억원)은 TIPS 계획으로 대체: 팀을 평균 6 → 9명에서 {_a['fte'][0]:.1f} → {_a['fte'][1]:.0f}명으로 줄이고, 판매 · 파트너 확장과 본인증은 후속 투자 단계 (3년차~)로 넘김.

## TIPS 과제 예산 (비목별, 억원)

{md_table(['비목', '내용', '구분', '1차년도', '2차년도', '합계'],
          [[r['cat'], r['item'], r['kind'], f"{r['y1'] / 1e4:.2f}", f"{r['y2'] / 1e4:.2f}", f"{r['total'] / 1e4:.2f}"] for r in TP['rows']]
          + [['**합계**', f"정부 {TP['gov'] / 1e4:.0f} · 민간 {TP['private'] / 1e4:.2f}", '', f"**{TP['year_total'][0] / 1e4:.2f}**", f"**{TP['year_total'][1] / 1e4:.2f}**", f"**{TP['total'] / 1e4:.2f}**"]])}

- 가정 (ASSUMPTION): 정부지원 비율 {_a['tips_gov_ratio']:.0%} 이내 · 민간 현금 {_a['tips_cash_ratio']:.0%} 이상 — 2026 공고 원문으로 최종 확인 필요. 간접비는 직접비 대비 약 {TP['indirect_rate']:.1%}.
- 인건비: 연 {_a['loaded']:,}만원/인 (평균 연봉 약 7,100만원 × 1.2, 4대보험 · 퇴직급여 포함) × 참여 개월 × 과제 참여율.

## TIPS 기간 팀 (채용 계획, ASSUMPTION)

{md_table(['역할', '시작', '인건비 구분', '과제 참여율', 'Y1 인·월', 'Y2 인·월'],
          [[t['role'], f"M{t['start']}", t['kind'], (f"{t['part']:.0%}" if t['part'] else '과제 외'), t['pm_y1'], t['pm_y2']] for t in TP['team']])}

대표 외 인원은 모두 신규 채용 계획. 창업팀 정보는 `[Founder 정보 필요]`.

## 회사 전체 지출 (24개월, 억원) — 재무모델 Base Y1 + Y2

{md_table(['항목', 'Y1', 'Y2', '합계', '근거'], [[lab, f"{x[0] / 1e4:.2f}", f"{x[1] / 1e4:.2f}", f"{(x[0] + x[1]) / 1e4:.2f}", why] for lab, x, why in _sp]
          + [['**합계**', f"**{TP['spend'][0] / 1e4:.2f}**", f"**{TP['spend'][1] / 1e4:.2f}**", f"**{TP['spend_total'] / 1e4:.2f}**", '= −현금흐름 (FM_Base)']])}

## 점검과 범위 조정

- M9 목업 정리 성공률 70% · M12 지불의사 (중앙값 ≥ 목표가 60%)가 후속 투자 판단 자료. 미달 시 작업 범위 축소 · B2C 재검토 (본문 16쪽).
- 절감 옵션 (일정 위험 증가): 로봇 팔 구매형 시제품 유지 · 목업 공간 공유 (가구 파트너 공장 · 쇼룸) · 채용 3개월 순연.
- xlsx `TIPS_Budget` 시트에서 정부지원 비율 · 민간 현금 비율 충족 여부를 수식으로 확인.
""")

# ---------------------------------------------------------------- 08 IP
pat = [
    ('1', '주방가구 일체형 Robot Rail · Dock · Storage 구조', '상부장 하단 Rail과 Robot Garage의 일체 구조 · 가구가 아닌 구조체로의 하중 전달 경로', '높음 — 모든 Rail형 제품의 기반', '높음 — 천장 Rail 양팔 로봇주방(Moley 계열), 상부장 하단 Rail 양팔(삼성 Bot Chef Concept) 등 선례 존재 → 청구범위를 "가구 일체 Garage + 구조체 정착 Frame" 조합으로 좁혀야 할 가능성', 'B25J 5/02, A47B 77/00 (확인 필요)'),
    ('2', 'Robot-ready Kitchen Interface Module', 'Mount · 전원 · 통신 · Sensor · Tool Dock을 한 Module로 표준화한 주방가구 Interface 규격', '높음 — Land 상품(신축 Option)의 핵심', '중간 — 가전 Built-in 규격·가구 Interface 일반 기술', 'A47B 77/00 · H02J (확인 필요)'),
    ('3', 'Fold / Deploy Robot Storage System', '키큰장 내부 수납 Robot의 전개·복귀 기구, 문 Interlock', '중간 — Compact 평형 (Case A)', '중간 — 가전 Lift 기구 · 수납형 Robot', 'B25J 5/00 · A47B (확인 필요)'),
    ('4', 'Human Zone / Robot Zone 기반 Safety Control', '주방 Zone Map 기반 감속·정지 · 통로 위 운반 금지 Logic', '높음 — 안전 인증·고객 수용성', '높음 — 산업용 Speed & Separation Monitoring · 협동로봇 안전 특허 다수', 'B25J 9/16 · B25J 19/06 · F16P 3/14 (확인 필요)'),
    ('5', 'Kitchen End-effector', '한식 식기(밥공기·국그릇·접시) 형상 대응 Gripper + Suction 복합', '중간', '중간 — 식품·물류 Gripper', 'B25J 15/00 (확인 필요)'),
    ('6', 'Food-contact Consumable Cartridge', '교체형 식품접촉 Tip·Pad 체결 구조 · 교체주기 인식', '중간 — 반복매출 근거', '중간 — 교체형 Gripper Pad', 'B25J 15/00 (확인 필요)'),
    ('7', 'Installation Auto Calibration', '설치 후 Kitchen 기준점 Target 기반 자동 좌표 보정 · Template 좌표 불러오기', '높음 — 설치시간·설치원가', '중간 — Robot Calibration 일반 기술', 'B25J 9/16 · G05B (확인 필요)'),
    ('8', 'Dishwasher Robot Interface', '상향 Housing 식세기의 Door·Rack 위치 표준 · Robot 투입·인출 연동', '높음 — 첫 제품 핵심 Task', '중간 — 가전사의 Robot 연동 특허 가능성', 'A47L 15/00 · A47L 15/50 (확인 필요)'),
    ('9', 'Robot Cleaning / Sanitizing Dock', 'Garage 내 End-effector 세척·건조·위생 관리', '중간 — 위생·식품접촉', '낮음~중간', 'A47L · B08B (확인 필요)'),
    ('10', 'Kitchen Layout 기반 Robot Module Selection', '평면·치수 입력 → Layout Family 분류 → Architecture·Module 자동 선택 Software', '중간 — 표준화·Design Lead Time', '낮음~중간 — 설계 자동화 SW (SW 특허 적격성 검토 필요)', 'G06F 30 · G06Q (확인 필요)'),
]
write('08_IP_Patent_Portfolio.md', f"""# 08. IP / Patent Portfolio (후보)

{HEADER}
> 등록 가능성을 주장하지 않음. 아래 10개 Family는 **출원 후보**이며 전부 TO BE VALIDATED (선행기술조사 필요). 특정 특허번호는 조사 전이므로 기재하지 않음.

## Patent Family 후보

{md_table(['#', 'Family', 'Protectable Core', 'Business Relevance', 'Possible Prior Art Risk', '분류 후보'], pat)}

## 선행기술조사 계획 (Seed M0~M3)

1. 검색 DB: KIPRIS · Google Patents · Espacenet · USPTO.
2. 검색 축: (a) Kitchen + Robot Arm + Rail/Gantry/Ceiling (b) Robot + Dishwasher Loading/Unloading (c) Cabinet-integrated / Retractable Robot (d) Zone-based Safety + Domestic Robot (e) Robot Installation Calibration + Furniture.
3. 우선 확인 대상 (선례가 공개된 주체): Moley Robotics 로봇 주방 특허 Family · Samsung (Bot Chef · Bot Handy) · LG (CLOiD 관련) · Sunday Robotics · 주방가구·빌트인 가전사의 Robot 연동 출원.
4. 산출: Family별 FTO 위험 (High/Medium/Low) · 청구범위 차별 포인트 · 출원 우선순위.

## 출원 우선순위 가설

- 1순위 (사업 핵심 + 선행 위험 상대적 낮음 추정): ② Interface Module · ⑦ Auto Calibration · ⑧ Dishwasher Interface.
- 2순위: ① Rail·Dock·Storage 일체 구조 (선행 위험 높음 → 구조체 정착 Frame·Garage 조합으로 범위 설계) · ④ Zone Safety.
- 3순위: ③ · ⑤ · ⑥ · ⑨ · ⑩ (Prototype 이후 실제 구조 확정 시).
- TIPS 24개월 목표: KR 출원 5건 (Y1 2 · Y2 3) + PCT는 후속 투자 단계에서 검토 (비용은 TIPS 과제 연구활동비 · 안전 · 시험 · 특허 항목에 포함, ASSUMPTION).

## Moat에서 IP의 위치

IP는 7개 Moat Layer 중 L5. 경쟁사가 Hardware를 확보해도 복제하기 어려운 것은 **Kitchen Template Library (L2) · Installation Standard (L3) · Care/Service Data (L6) · Installed Base (L7)**라는 가설이며, 특허는 이를 보완하는 수단 (21장).
""")

# ---------------------------------------------------------------- 09 VC Q&A
strength = {1: '보통', 2: '보통', 3: '강함', 4: '약함', 5: '보통', 6: '약함', 7: '보통', 8: '보통', 9: '약함', 10: '보통', 11: '보통', 12: '약함',
            13: '강함', 14: '보통', 15: '강함', 16: '보통', 17: '보통', 18: '약함', 19: '보통', 20: '보통', 21: '보통', 22: '보통', 23: '약함', 24: '보통', 25: '약함'}
fix = {4: 'Time-diary 30세대 + PSM/Conjoint + 예약금', 6: 'Kitchen 견적 20건 + 총비용 기준 WTP 문항', 9: 'Pilot 세대 Kit 교체주기 실측',
       12: '평면 30개 분석 결과', 18: '가구사 2~3곳 Partner 조건 탐색 · 독점/비독점 구조', 23: 'TIPS 운영사 접촉 · Plan B 확정', 25: 'Founder 정보 입력'}
qarows = [[str(i + 1), q, a, strength[i + 1], fix.get(i + 1, '—')] for i, (q, a) in enumerate(SA.qa())]
write('09_VC_RedTeam_QA.md', f"""# 09. VC 예상질문 · Red-Team 답변

{HEADER}
실제 Seed 심사역 관점의 25개 질문. "답의 강도"가 약한 항목은 본문에서 숨기지 않고 표기했고, Investment Memo의 Reasons Not to Invest와 연결됨.

{md_table(['#', '질문', '답 (근거 Slide)', '답의 강도', '보완 Evidence'], qarows)}

## Red-Team 결과 본문 반영 내역

| 약점 | 반영 위치 |
|---|---|
| 가치 Anchor(월 11~24만원) < 원가 기반 Rental(월 24~31만원) | 14장 Gap Statement · 02장 Q2 |
| Rental Payback Y3 39개월 > 36개월 | 17장 하단 · A12 결론 |
| Care는 Y3에 Profit Center 아님 | 17장 · A13 |
| TIPS 이후 후속 투자 의존 (후속 없으면 약 18개월) | 본문 19쪽 · D11 |
| 신축 매출 2년 Lag | 12장 Timing |
| Founder 정보 공백 | 03장 · 23장 · A22 |
| 범용 Humanoid의 월 $499 구독가 | 20장 · A9 시사점 |
""")

# ---------------------------------------------------------------- 10 investment memo
SC = SA.score()
tot_c = sum(c for _, c, _, _ in SC); tot_t = sum((t or c) for _, c, t, _ in SC)
write('10_Investment_Memo.md', f"""# 10. Investment Memo — ARKI Robotics (가칭) · TIPS 운영사 검토용

{HEADER}
| 항목 | 내용 |
|---|---|
| 회사 | ARKI Robotics (아키로보틱스, 가칭) — Residential Built-in Robotics |
| 제품 | ARKI Kitchen System (Robot-ready Kitchen + Robot Module + Software + Installation + Care/Consumables) · 첫 제품 ARKI Kitchen Assist V1 (Kitchen Clean-up) |
| 첫 시장 | 구축 아파트 Premium Kitchen Remodeling (Validation) → 신축 Robot-ready Option (Scale) |
| 요청 | 운영사 투자 {v('op_invest') / 1e4:.0f}억원 (가설) + TIPS R&D 최대 {TP['gov'] / 1e4:.0f}억원 · 24개월 (회사 전체 지출 약 {TP['spend_total'] / 1e4:.1f}억원, 후속 투자 {v('followon') / 1e4:.0f}억원 목표) |
| 단계 | Concept. Prototype · 고객 · Partner · 특허 · 매출 없음. Founder 정보 미입력 |
| **판단** | **WATCH** (아래 근거) |

## 1. Investment Highlights

1. **문제 정의가 구체적**: "가전 사이 Physical Task"라는 좁고 반복적인 공백 (식기 투입·인출·수납). 완전자율 요리가 아닌 Clean-up부터 시작해 검증 가능한 범위로 제한.
2. **AI가 아닌 공간으로 난이도를 낮추는 접근**: Robot Home · Rail/Dock · Human Zone 분리 · 식세기 상향 배치 등 공간 설계 규칙으로 Task 조건을 고정 → 범용 Mobile/Humanoid와 다른 경로.
3. **한국 공동주택이라는 Test Market**: 아파트 65.8% (FACT) · 준공 20년 이상 주택 56.0% (FACT) · 반복 평면 → Template 표준화 가설에 유리.
4. **채널 순서가 논리적**: 구축 Premium Remodeling으로 WTP·설치를 직접 검증하고, 신축 유상옵션(분양가의 9.7%가 옵션인 시장, FACT)으로 Project 단위 Scale.
5. **공사업체화를 피하는 역할 분담과 Kill Criteria가 사전에 설계됨**: M6·M9·M12·M18·M24 판정 기준 → Seed 자금이 끝까지 소진되기 전 실패 확인 가능.

## 2. Investment Risks

1. **Team 공백**: Founder 정보 없음 — Seed 판단의 1순위 항목이 비어 있음.
2. **WTP Gap**: 가치 Anchor 월 {VA['lo']:.0f}~{VA['hi']:.0f}만원 (DERIVED) < 원가 기반 Rental 월 {R5['fee_at_20']:.0f}~{R3['fee_at_20']:.0f}만원. Clean-up 단일 Task로 Robot 1,490만원을 정당화할 수 있는지 불명확.
3. **Hardware 원가 의존**: Y3 BOM 1,150만원 기준 세대 Contribution Margin {pct(h3['cm5'], 1)} — BOM 하락(Y5 900만원)이 전제. Arm 450만원은 공격적 가정.
4. **경쟁 속도**: 1X NEO ($20k 또는 월 $499), Sunday Memo, LG CLOiD가 식세기 작업을 시연 (FACT). 범용 Robot 가격이 빠르게 내려오면 Built-in 고정형의 가치가 희석될 수 있음.
5. **자본 집약**: Base 5년 누적 현금 최저 {eok(B['min_cum_cash'])}억원, 5년 내 흑자 없음. 신축 매출 2년 Lag. 가구사·가전사의 직접 진입 위험.

## 3. Key Assumptions

{md_table(['가정', 'Base 값', 'Tag', '검증'], [
    ['Robot ASP / Robot-ready 증분가', f"{v('p_robot'):,} / {v('p_rr')}만원", 'ASSUMPTION', 'PSM·Conjoint·예약금 (M12)'],
    ['Rental 월 요금', f"{v('p_rent')}만원 (60개월)", 'ASSUMPTION', '가격 Test'],
    ['Robot BOM', f"{v('bom')[0]:,} → {v('bom')[2]:,} → {v('bom')[4]:,}만원 (Y1→Y3→Y5)", 'ASSUMPTION', 'OEM RFQ · BOM v2'],
    ['Robot Attach (구축)', pct(v('attach')[2]), 'ASSUMPTION', 'Pilot 전환율'],
    ['Standard Module 사용률', f"{pct(v('smr')[2])} (Y3) → {pct(v('smr')[4])} (Y5)", 'TARGET', '평면 30개 · Pilot'],
    ['Kitchen 교체 세대 · Premium · 적용가능률', '30만/년 · 10% · 60%', 'ASSUMPTION', '견적·Partner Data·평면 분석'],
    ['신축 Option 선택률 · 입주 Attach', f"{pct(v('option_rate'))} · {pct(v('new_attach'))}", 'ASSUMPTION', '신축 계약자 Interview'],
    ['Care 가입 · Kit 구매율', f"{pct(v('care_attach'))} · {pct(v('cons_attach'))}", 'ASSUMPTION', 'Pilot 실측'],
    ['인당 인건비', f"{v('loaded'):,}만원/년", 'ASSUMPTION', '채용 시장 Data'],
])}

## 4. Key Numbers

{md_table(['지표', '값', 'Tag'], [
    ['총주택 / 아파트 비중 (2025)', '2,018.1만호 / 65.8%', 'FACT'],
    ['준공 20년 이상 주택 비중', '56.0%', 'FACT'],
    ['2025 주택 준공 / 아파트 입주 2025→2026E', '34.2만호 / 23.6만 → 18.3만', 'FACT'],
    ['TAM / SAM / SOM (Y5)', f"{MK['tam'] / 1e4:.2f}조 / {MK['sam']:,.0f}억 / {MK['som']:.0f}억원 (연)", 'DERIVED'],
    ['세대 5년 매출 / Contribution (구매·Y3 → Y5 원가)', f"{man(h3['rev5'])}만원 / {man(h3['contrib5'])} → {man(h5['contrib5'])}만원", 'DERIVED'],
    ['Rental Payback (Y3 → Y5)', f"{R3['payback']:.0f} → {R5['payback']:.0f}개월", 'DERIVED'],
    ['Care Margin (Y3 → Y5)', f"{pct(C3['margin'])} → {pct(C5['margin'])}", 'DERIVED'],
    ['Base 매출 Y3 / Y5', f"{eok(B['rev'][2])} / {eok(B['rev'][4])}억원", 'DERIVED'],
    ['Base 매출총이익률 Y3 / Y5', f"{pct(B['gm'][2])} / {pct(B['gm'][4])}", 'DERIVED'],
    ['Base 영업이익 Y5 · 5년 누적현금 최저', f"{eok(B['op'][4])}억원 · {eok(B['min_cum_cash'])}억원", 'DERIVED'],
    ['TIPS 24개월 지출 · 후속 투자 없을 때 자금 지속', f"{eok(TP['spend_total'])}억원 · {TP['runway_no_followon']:.1f}개월", 'DERIVED'],
    ['손익분기 (연 Kitchen)', f"약 {M['breakeven_kitchens']:,.0f}세대", 'DERIVED'],
])}

## 5. Critical Milestones

{md_table(['시점', 'Milestone (TARGET)', 'Kill Criteria'], [
    ['M3', '평면 30개 수집 · Interview 30 · Time-diary 30 · 선행기술조사', '—'],
    ['M6', '84㎡ Full-scale Mock-up · Robot Architecture 선정 · Dish Handling Test', '주거동선과 Robot Reach 양립 실패 → Architecture 변경'],
    ['M9', 'Dishwasher Integration · 성공률 측정 (200 cycle)', 'Clean-up 성공률 70% 미만 → Task Scope 축소'],
    ['M12', 'Clean-up Integrated Demo · Template 3개 · PSM/Conjoint · BOM v1', 'WTP 중앙값 < 목표가 60% → B2C 전략 재검토'],
    ['M18', 'Real-home Pilot 3세대 (M13~M24) · 설치시간·Service 원가 실측', 'Standard Module 사용률 60% 미만 → Productization 재검토'],
    ['M24', 'Paid Pilot · Partner Pilot 협의 · Series A Evidence Pack', 'Paid Pilot·Partner 확보 실패 → Scale 투자 보류'],
])}

## 6. What Must Be True

{md_table(['#', '전제', '현재 Evidence', '향후 검증', 'Failure Condition'], [
    ['1', 'Kitchen Remodeling 고객이 Robot Integration Premium을 지불', '없음', 'PSM·Conjoint·예약금·Paid Pilot', 'WTP 중앙값 < 목표가 60% (M12)'],
    ['2', '주요 Kitchen Layout이 소수 Template으로 분류', '없음', '평면 30개 · Coverage', '상위 3 Template Cover < 70%'],
    ['3', 'Single Robot Architecture가 반복설치 가능', '없음', 'Mock-up 2식 · Pilot 설치시간', '세대별 Custom 설계 · 설치 > 2일'],
    ['4', 'Robot + Installation GM이 장기적으로 개선', '공개가 기반 BOM 추정', 'BOM v2 · OEM 견적 · 설치원가 실측', 'Y3 BOM > 1,300만원 전망'],
    ['5', 'Care + Consumables가 실제 반복매출 형성', '없음', 'Pilot Care 가입 · Kit 교체주기', 'Care 가입 < 40% · 교체주기 > 2배'],
    ['6', 'Partner Distribution이 Direct보다 빠르게 Scale', '없음', 'Partner Pilot · 수수료 조건', 'M24 Partner Pilot 0건'],
    ['7', 'Service Cost가 Recurring Revenue를 초과하지 않음', '없음', '방문원가·고장률 실측', '방문 원가 > Care 요금'],
])}

## 7. Reasons to Invest

1. 문제·첫 Task·채널 순서가 좁고 검증 가능하게 정의됨 (과도한 TAM·완전자율 Cooking 주장 없음).
2. 공간 설계로 Robot 난이도를 낮추는 접근은 한국 공동주택의 반복 평면과 유상옵션 관행에 맞물림.
3. Robot-ready Kitchen을 독립 상품으로 두어 Robot 구매 없이도 설치기반(Land)을 확보하는 구조.
4. Kill Criteria가 사전 정의되어 Seed 자본이 "Option 매입"으로 작동 — 실패를 일찍 확인 가능.
5. 성공 시 Template Library · 설치 Standard · Care Network가 Laundry · Storage 등 Residential Robotics Infrastructure로 확장될 수 있는 구조 (장기 Option, 현재 미검증).

## 8. Reasons Not to Invest

1. Founder·Team 정보 없음 → 실행 역량 판단 불가.
2. 고객 Evidence 전무, 가치 Anchor와 가격 사이 Gap.
3. 범용 가정용 Robot의 가격 하락·기능 확장 속도가 빠름 (월 $499 구독 등장).
4. Hardware BOM·인증·설치 Risk가 겹치는 자본집약 사업, 5년 내 흑자 없음.
5. 가구사·가전사가 동일 Integration을 직접 수행할 가능성 — 방어력(Template·설치 Data)은 설치 경험 이후에만 생김.

## 9. 90-Day Action Plan

`11_Evidence_Gaps_Founder_Inputs_90Day.md` 상세. 요약: ① Founder·공동창업자 확정 ② Kitchen 견적 20건 · 평면 30개 · Time-diary 30 · Interview 30 ③ 구매형 Arm Desktop Rig로 식기 20종 Pick·식세기 Loading 시연 + 로그 ④ 선행기술조사 · 우선 출원 2건 ⑤ 주방가구·인테리어 사업자 10곳 미팅 → Pilot 협력 1곳 ⑥ TIPS 운영사 접촉.

## 10. Investment Scorecard

{md_table(['항목', '현재 (1~5)', '24개월 Target', '핵심 Evidence'], [[k, c, (t if t else 'TBV'), e] for k, c, t, e in SC] + [['합계', f"{tot_c}/50", f"{tot_t}/50", '']])}

## 11. 판단: 내가 실제 Seed VC라면 — **WATCH**

**근거**
- 진입 방식(구축 Validation → 신축 Scale), Kill Criteria, BM 구조, 역할 분담은 IC에 올릴 만큼 명확함. 접근의 차별점(공간으로 Task 조건 고정)도 논리적임.
- 그러나 Seed 판단의 핵심 4요소 — **Team · Customer Demand · Standardization · Channel** — 의 Evidence가 모두 0. 현재 자료로 20억원을 집행하면 "아이디어와 가설"에 투자하는 것이며, Robotics Hardware Seed의 일반 기준(Founder 역량 + 최소 기술 Proof)에 미달.
- PASS가 아닌 이유: 문제 정의·검증 설계가 구체적이어서 **90일 안에 아래 5개 Evidence를 만들 수 있는 구조**이고, 이 Evidence가 나오면 판단이 바뀔 수 있음.

**INVEST로 바뀌기 위해 반드시 필요한 Evidence (최대 5개)**

1. **Founder-Market Fit**: Robot Manipulation × 주방·건축 Integration × 고객/Partner 영업 역량을 가진 Full-time Founding Team 2인 이상 (경력·결과물 증빙).
2. **Mock-up Proof**: 실제 크기 주방(또는 Rig)에서 식기 → 식세기 Loading 연속 시연 — 영상 + 성공률·개입 Log (측정 프로토콜 공개).
3. **WTP 행동 신호**: Premium Remodeling 상담 고객 30명 Interview + 실명 예약금(환불가능) 또는 유료 Pilot 의향 3건 이상 (Robot ≥ 1,000만원 또는 Rental ≥ 월 25만원 수준).
4. **표준화 신호**: 실제 평면 30개 분석에서 상위 3개 Template이 70% 이상 Cover.
5. **Channel 신호**: 주방가구·Interior 사업자 1곳 이상과 Pilot 시공 협력 합의 (실재 · 조건 명시).
""")

# ---------------------------------------------------------------- 11 gaps / founder / 90 days / top5
write('11_Evidence_Gaps_Founder_Inputs_90Day.md', f"""# 11. 현재 부족한 Evidence · Founder 입력 필요정보 · 90일 실행계획 · Top 5 Evidence

{HEADER}
## 1. 현재 부족한 Evidence

{md_table(['영역', '부족한 Evidence', '영향 (Slide)', '확보 시점'], [
    ['Team', 'Founder 경력 · 역할 · Full-time 여부 · 공동창업자', '23 · A22 (Team 1점)', 'D+14'],
    ['Customer', 'Interview · Time-diary · WTP · 예약금', '02 · 14 · 15 · A17', 'D+30~M12'],
    ['Price', 'Kitchen 단독 Remodeling 견적 (일반·Premium)', '14 · A3', 'D+30'],
    ['Space', '실제 평면 30개 · 실측 · 벽체 구조', '06 · 10 · 11 · A5 · A6 · A8', 'D+60~M3'],
    ['Technology', 'Pick·Loading 성공률 · Cycle Time · Recovery', '08 · A17', 'D+60 (Rig) · M12 (Mock-up)'],
    ['Cost', 'Arm OEM 견적 · Rail·EE·Vision 견적 → BOM v1', '17 · A4', 'D+60'],
    ['Installation', '설치·Calibration 시간 · Partner 시공비', '11 · A8', 'M12~M18'],
    ['Service', '방문원가 · 고장률 · Kit 교체주기', '17 · A13', 'M18~M24'],
    ['Channel', '주방가구·Interior·건설사 협력 의향 (실재)', '19 · 20', 'D+90~M24'],
    ['IP', '선행기술조사 · 출원', '21 · A10', 'D+60~M18'],
    ['Safety', 'Risk Assessment · 인증기관 사전상담', 'A7', 'D+90~M12'],
    ['Market', '공식 통계 원문 대조 · 연간 Kitchen 교체 세대 보정', 'A2', 'D+30'],
])}

## 2. Founder 입력 필요정보

덱에서 `[Founder 정보 필요]` 또는 `[입력 필요]`로 남긴 항목. 임의 생성하지 않음.

{md_table(['항목', '내용', '위치'], [
    ['Founder Background', '학력·주요 경력 (기간·조직·역할)', '본문 14쪽'],
    ['Relevant Engineering Experience', 'Robot 제어·Manipulation·Vision·Mechatronics 실적 (논문·제품·특허·코드)', '본문 14쪽'],
    ['Product Development Experience', '하드웨어 제품 출시·양산·인증 경험', '본문 14쪽'],
    ['Construction / Kitchen Understanding', '주방가구·인테리어·건설 설계/시공 경험 (공동주택 Kitchen 이해)', '본문 14쪽'],
    ['Robot Experience', 'Cobot·Service Robot 개발/운영 경험', '본문 14쪽'],
    ['Customer / Partner Network', '인테리어·가구사·건설사·렌탈사 접점 (실명 가능 범위)', '본문 14 · 12쪽'],
    ['Full-time Commitment', 'Full-time 전환 시점 · 지분 구조 · Vesting', '본문 14쪽'],
    ['회사 정보', '법인 설립 여부 · 상호(ARKI 가칭) 상표 검색 결과 · 소재지', '본문 1쪽'],
    ['투자 조건', '투자 형태 (보통주·RCPS·SAFE 등) · Pre-money · 지분율 · 라운드 구성 · TIPS 운영사', '본문 19쪽'],
    ['현재 Evidence', '보유 설계자료 · Prototype · 인터뷰 · Partner 미팅 · 특허 (있으면 03장 CURRENT EVIDENCE 갱신)', '03장'],
    ['연락처', 'IR 담당자 연락처', '본문 1 · 19쪽'],
])}

## 3. 90일 실행계획 (Evidence Pack v1)

{md_table(['주차', '실행', '산출물 (Evidence)', '담당 역량'], [
    ['W1~W2', 'Founding Team 확정 · 역할·지분 · Founder 정보 정리 · ARKI 상표 선행 검색', '팀 슬라이드 완성 (본문 14쪽)', 'CEO'],
    ['W1~W4', 'Kitchen 견적 20건 (한샘·리바트·LX·지역 인테리어, 일반/Premium/빌트인 포함)', 'A3 ASSUMPTION → 견적 Data 대체', 'BD'],
    ['W1~W6', '입주자모집공고 평면 30개 수집 · 분석 Template (치수·설비·Robot Home 후보)', 'Layout Family 초안 · Coverage %', 'Kitchen·건축'],
    ['W2~W6', 'Time-diary 30세대 (7일) · Interview 30명 (Premium 상담 고객, 인테리어 업체 협조)', 'Pain 크기 · 수용성 · 우려 Top 5', 'BD·Research'],
    ['W3~W8', '구매형 Arm(5kg급) + 저가 Gripper Desktop Rig · 한식 식기 20종 Pick · 식세기 Rack Loading 실험', '시연 영상 + 성공률·Cycle Time Log', 'Robotics'],
    ['W3~W8', 'Case A~D CAD Reach Study · 식세기 상향 배치 검증', 'Reach Coverage 표 (A6 갱신)', 'Robotics·Kitchen'],
    ['W4~W8', '선행기술조사 10 Family (KIPRIS·Google Patents) → 우선 출원 2건 명세서 초안', 'FTO 위험표 · 출원 2건', 'CEO·변리사'],
    ['W4~W10', 'Arm OEM 3곳·Rail·Gripper·Vision RFQ (100대 기준)', 'BOM v1 (A4 갱신)', 'Mechatronics'],
    ['W6~W10', '주방가구·인테리어 사업자 10곳 미팅', 'Pilot 협력 합의 1곳 (실재)', 'BD'],
    ['W8~W12', '84㎡ 11자 Full-scale Mock-up 설계·발주 · Risk Assessment 초안 · 인증기관 사전상담', 'Mock-up 설계도 · 안전 요구사항 목록', 'Kitchen·Safety'],
    ['W10~W12', 'PSM 1차 (n≈300 Panel) · TIPS 운영사 접촉 · IR 덱 v5 (Evidence 반영)', 'WTP Range · 운영사 투자 · TIPS 추천 구조 확정', 'CEO'],
])}

**Day 90 판정**: Evidence Pack v1 (견적 20 · 평면 30 · Interview 30 · Time-diary 30 · Rig Log · BOM v1 · 선행조사 · Partner 1) → Seed Close 또는 범위 수정.

## 4. 투자매력도를 가장 크게 올릴 Top 5 Evidence

| 순위 | Evidence | 왜 가장 큰가 | 해소되는 질문 |
|---|---|---|---|
| 1 | **Founder-Market Fit** (Robot × 주방/건축 × 영업 Founding Team) | Seed 판단 1순위, 현재 공백 | Q6 · Red-Team #25 |
| 2 | **Mock-up / Rig 시연 + 성공률 Log** (식기 → 식세기 Loading 연속) | 기술 실현성의 최소 Proof | Q4 · Technology |
| 3 | **WTP 행동 신호** (실명 예약금·유료 Pilot 의향 3건+, 목표가 근처) | Sensitivity 1순위 변수 (WTP) | Q1 · Q2 · Q3 |
| 4 | **평면 30개 → 상위 3 Template 70%+ Cover** | "Custom Interior 아닌가" 질문의 직접 답 | Q4 |
| 5 | **주방가구·Interior Partner Pilot 합의 (실재)** | Sensitivity 3순위 (Partner 물량) · 공사업체화 Risk 해소 | Q1 · Q5 |

다음 순위: Arm OEM 견적 (Sensitivity 2순위 BOM) · 선행기술조사 결과 · 인증기관 사전상담 결과.
""")

# ---------------------------------------------------------------- 00 index
write('00_Index.md', f"""# ARKI Robotics — TIPS IR Package Index

{HEADER}
| # | 요청 산출물 | 위치 |
|---|---|---|
| 1 | 본문 IR 덱 (TIPS) | `ARKI_Robotics_TIPS_IR_Deck.pptx` 1~{_NM}쪽 (1~14 IR · 15~{_NM} TIPS 과제 요약) · 본문만 `..._Main.pdf` (전체 검토용 `..._preview.pdf`) |
| 2 | 부록 | 같은 파일 부록 A~F (목차 포함, v1 본문 · 부록 전체 유지) |
| 3 | 장별 화면 문구 | `docs/01_Main_Deck_Script.md` · `docs/02_Appendix_Script.md` |
| 4 | 장별 그림 구성 | 같은 문서 "그림 구성" · 3D는 `ARKI/render3d` (README 참고) |
| 5 | 도표 | 같은 문서 "도표" |
| 6 | 발표 메모 | 같은 문서 "발표 메모" + pptx 발표자 노트 |
| 7 | 시장 데이터와 출처 | `docs/03_Market_Data_and_Sources.md` · xlsx `Sources` · 덱 부록 F2 |
| 8 | FACT / DERIVED / ASSUMPTION / TARGET 구분표 | `docs/04_Number_Tag_Register.md` · xlsx `Inputs` · 덱 부록 F1 |
| 9 | 5개년 재무모델 | `ARKI_Robotics_Financial_Model.xlsx` · `docs/05_Financial_Model_5Y.md` · 덱 본문 13쪽 · 부록 D9 |
| 10 | 세대당 경제성 | `docs/06_...` §2·§7 · xlsx `Household` · 덱 본문 11쪽 · 부록 D2 · D6 |
| 11 | 렌탈 경제성 | `docs/06_...` §4 · xlsx `Unit_Economics` · 덱 부록 D7 |
| 12 | 관리 · 소모품 경제성 | `docs/06_...` §5·§6 · 덱 부록 D8 |
| 13 | TIPS 연구개발비 · 자금 계획 | `docs/07_TIPS_Budget_Plan.md` · xlsx `TIPS_Budget` · 덱 본문 19쪽 · 부록 D11 |
| 14 | 특허 후보 | `docs/08_IP_Patent_Portfolio.md` · 덱 부록 E1 · E2 |
| 15 | 예상 질문과 답 | `docs/09_VC_RedTeam_QA.md` · 덱 부록 E5~E6 |
| 16 | Investment Memo | `docs/10_Investment_Memo.md` |
| 17 | 현재 부족한 Evidence | `docs/11_...` §1 |
| 18 | Founder 입력 필요정보 | `docs/11_...` §2 |
| 19 | 90일 실행계획 | `docs/11_...` §3 |
| 20 | Top 5 Evidence | `docs/11_...` §4 · 덱 부록 A4 |
""")

# ---------------------------------------------------------------- facts sheet: TIPS / 재무 / 팀 sections regenerated from model.json
def _facts_sections():
    a = {d['key']: d['vals']['B'] for d in M['inputs']}; Bf = M['scenarios']['B']; Sf = M['scenarios']
    eo = lambda x, d=1: f"{x / 1e4:.{d}f}"
    fin = (f"## 재무 (Base, 억원)\n- 매출 Y1 {eo(Bf['rev'][0])} / Y2 {eo(Bf['rev'][1])} / Y3 {eo(Bf['rev'][2])} / Y4 {eo(Bf['rev'][3])} / Y5 {eo(Bf['rev'][4])} [DERIVED from ASSUMPTION/TARGET]\n"
           f"- 매출총이익률 Y1 0% / Y2 {Bf['gm'][1]:.0%} / Y3 {Bf['gm'][2]:.0%} / Y4 {Bf['gm'][3]:.0%} / Y5 {Bf['gm'][4]:.0%}\n"
           f"- 영업이익 Y1 {eo(Bf['op'][0])} / Y2 {eo(Bf['op'][1])} / Y3 {eo(Bf['op'][2])} / Y4 {eo(Bf['op'][3])} / Y5 {eo(Bf['op'][4])}\n"
           f"- 5년 누적 현금 최저 약 {eo(Bf['min_cum_cash'], 0)}억원; 손익분기 연 약 {M['breakeven_kitchens']:,.0f}세대 (Y5 단가·원가, Y6 이후)\n"
           f"- 시나리오 Y5 매출: 보수 {eo(Sf['C']['rev'][4])} / 기본 {eo(Bf['rev'][4])} / 상향 {eo(Sf['U']['rev'][4])}억원\n"
           f"- Y1~Y2 = TIPS 과제 기간 (평균 인원 {a['fte'][0]}명 → {a['fte'][1]}명), Y2 가정 실증 {a['rd'][1]}세대 (실증 할인 50%) [ASSUMPTION/TARGET]\n"
           f"## TIPS 요청 · 자금 (2026 팁스 창업기업 일반 트랙)\n"
           f"- TIPS R&D 정부지원금 최대 {eo(a['tips'], 0)}억원 · 최대 {a['tips_months']}개월 [FACT, 2026 공고] · 선정 미확정. 정부지원 비율 {a['tips_gov_ratio']:.0%} 이내 · 민간 현금 {a['tips_cash_ratio']:.0%} 이상 (inputs 출처 참조)\n"
           f"- TIPS 과제 예산 {eo(TP['total'])}억원 = 정부 {eo(TP['gov'], 0)} + 민간 {eo(TP['private'], 2)} (현금 {eo(TP['private_cash'], 2)} · 현물 {eo(TP['inkind'], 2)} = 대표 인건비 참여 50%) [ASSUMPTION]\n"
           f"- 비목 (억원, 1차년도/2차년도/합계): " + ' · '.join(f"{r['cat']}({r['kind']}) {eo(r['y1'], 2)}/{eo(r['y2'], 2)}/{eo(r['total'], 2)}" for r in TP['rows']) + f" · 간접비율 직접비 대비 {TP['indirect_rate']:.1%}\n"
           f"- 24개월 회사 전체 지출 약 {eo(TP['spend_total'])}억원 (Y1 {eo(TP['spend'][0])} · Y2 {eo(TP['spend'][1])}) = TIPS 과제 {eo(TP['total'])} + 과제 밖 {eo(TP['non_rnd'])} [DERIVED]\n"
           f"- 재원: TIPS {eo(TP['gov'], 0)} + 운영사 투자 {eo(a['op_invest'], 0)} (요청, ASSUMPTION) + 후속 투자 {eo(a['followon'], 0)} (M12 점검 뒤, TARGET) = {eo(TP['src_total'], 0)}억원 → 여유 {eo(TP['buffer'])}억원; 후속 투자 없으면 약 {TP['runway_no_followon']:.0f}개월 [DERIVED]\n"
           f"- 창업사업화 연계 최대 {eo(TP['biz_link'], 0)}억원 (선정 뒤 별도 신청) 미반영. 투자유치 실적 없음 [FACT]. 운영사 · 투자 조건 미정 ([운영사 협의 후 기재])\n"
           "- 이전 Seed 안 (20억원 · 재산정 25.8억원)은 TIPS 계획으로 대체됨\n"
           "- 24개월 목표 [TARGET]: 실물 크기 목업 주방 2식 · 시제품 1차 2식 → 2차 · 가정 실증 3세대 (유료 목표) · 성과지표는 본문 TIPS 과제 ① 표 (slides_main.TIPS['kpi']) · 평면 30개 분석 → 표준형 · 단축형 한 줄, 적용 60% (M18) · 인터뷰 50명 · 지불의사 n≥300 · 특허 출원 5건 (Y1 2 · Y2 3, 등록 미정) · 공인기관 성능 · 안전 사전시험\n"
           "- 점검 · 중단 기준 [TARGET]: M6 목업에서 사람 동선과 로봇 동작범위 양립 실패→구조 변경 / M9 정리 성공률 70% 미만→작업 범위 축소 / M12 지불의사 중앙값 < 목표가 60%→B2C 재검토 / M18 표준 한 줄 적용 60% 미만→표준화 재검토 / M24 가정 실증 · 공인시험 실패→확장 투자 보류\n")
    team = ("## 팀\n- Founder 정보 미제공 → 창업자 · R&D 역량 8항목 (학력·경력 / 엔지니어링·제품 개발 / 로봇 / 건설·주방 / 보유 특허 / 논문·수상 / 고객·파트너 네트워크 / 전업 여부) 모두 [Founder 정보 필요]. TIPS 기간 팀 [ASSUMPTION]: "
            + ' · '.join(f"{t['role']} M{t['start']}~ ({'과제 외' if not t['part'] else format(t['part'], '.0%')})" for t in TP['team'])
            + f". 평균 인원 Y1 {a['fte'][0]}명 → Y2 {a['fte'][1]}명. 대표 외 전원 신규 채용 계획.\n")
    p_ = os.path.join(HERE, '_facts_sheet.md'); s_ = open(p_, encoding='utf-8').read()
    i0 = s_.index('## 재무 (Base, 억원)'); i1 = s_.index('## 경쟁·사례'); s_ = s_[:i0] + fin + s_[i1:]
    i0 = s_.index('## 팀'); i1 = s_.index('## 금지'); s_ = s_[:i0] + team + s_[i1:]
    s_ = re.sub(r'- Y5 계획 매출 [0-9.]+억원 = SAM', f"- Y5 계획 매출 {eo(Bf['rev'][4])}억원 = SAM", s_)
    open(p_, 'w', encoding='utf-8').write(s_); print('wrote _facts_sheet.md (TIPS · 재무 · 팀)')
_facts_sections()

# ---------------------------------------------------------------- README (deck table generated from the deck text log)
_main = [m for m in DT['meta'] if isinstance(m['no'], int)]
_deck_rows = '\n'.join(f"| {m['no']:02d} | {m['title']} |" for m in _main)
_h3 = M['household']['purchase_direct_Y3']; _h5 = M['household']['purchase_direct_Y5']; B5r = M['scenarios']['B']; _av = {d['key']: d['vals']['B'] for d in M['inputs']}
README = f"""# ARKI Robotics — TIPS IR Package (Draft v4, 2026.10)

**설거지 정리를 맡는 로봇 주방 · 첫 시장 구축 아파트 주방 리모델링 → 신축 옵션**

> Concept 단계 자료. 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 · 투자유치 없음. 2026 TIPS 창업기업 (일반 트랙) 지원용 IR. 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET (+ CONCEPT · TO BE VALIDATED · FUTURE)로 구분. Founder 정보는 `[Founder 정보 필요]`로 비워 둠. 평면은 사용자 제공 도면이며 단지명은 표기하지 않음.

## 산출물

| 파일 | 내용 |
|---|---|
| `ARKI_Robotics_TIPS_IR_Deck.pptx` | TIPS IR 덱 (본문 {len(_main)}쪽 = IR 14쪽 + TIPS 과제 요약 {len(_main) - 14}쪽, 부록 A~F), 16:9, 발표자 노트 포함 |
| `ARKI_Robotics_TIPS_IR_Deck_Main.pdf` | 본문만 (TIPS 연구개발계획서 IR 별첨 · 운영사 공유용) |
| `ARKI_Robotics_TIPS_IR_Deck_preview.pdf` | 전체 검토용 PDF |
| `ARKI_Robotics_Financial_Model.xlsx` | 수식 기반 5개년 모델 (Inputs → 3개 시나리오 · Household · Unit_Economics · Market · Sensitivity · TIPS_Budget · Sources) |
| `docs/00~11` | 장별 문구 · 그림 · 발표 메모, 시장 데이터 · 출처, 숫자 태그 구분표, 재무 · 세대 경제성, TIPS 연구개발비 · 자금 계획, 특허 후보, 예상 질문, 투자 메모 (WATCH), Evidence 공백 |
| `render3d/` | 3D 그림 생성기 (three.js + Playwright) · 충돌검사 · 보관/전개 경로 계획 · 평면 JSON |
| `assets/renders/` | 덱에 들어간 3D 그림 PNG + 앵커 · 충돌검사 결과 JSON |

## 본문 구성 ({len(_main)}쪽: 1~14 IR · 15~{len(_main)} TIPS 과제 요약)

| 쪽 | 메시지 |
|---|---|
{_deck_rows}

부록: A 투자 판단 요약 · B 제품 · 표준화 (B5 받은 평면 5종 상태, B6 구축 2Bay A 원래 평면 → ARKI) · C 시장 · 사업화 · D 경제성 · 재무 (D11 TIPS 기간 자금 계획 상세) · E 진입장벽 · 리스크 · 예상 질문 · F 숫자 표기 원칙 · 출처. 그림은 대표 평면 1종 (구축 2Bay A)만 사용. v1 본문 · 부록은 삭제 없이 부록으로 옮김.

## 로봇 주방 설계 (3D 모델 기준, CONCEPT)

- 한 줄 모듈: 로봇 보관함 45 · 내려놓는 곳 70~80 · 싱크 80 · 로봇용 서랍 60 · 식기세척기 60cm. 조리기구는 이 줄에 두지 않음 (로봇 금지 구역).
- 레일: 상부장 바로 아래 (높이 139cm). 로봇은 레일에 매달려 이동, 바닥을 쓰지 않음.
- 보관함: 조리대 위 끝 (W45 × D62 × H137cm), 앞판 + 15cm 꺾인 판으로 된 여닫이 문 1짝 (왼쪽 경첩). 오른쪽 아래(상부장 하단선 아래)는 레일 통로. 평소 로봇은 위로 접혀 안에 있음.
- 나오는 순서: 문 열림 → 팔이 문 앞쪽으로 펴지며 레일 아래로 → 레일 방향 이동 자세 → 통로로 이동. 경로는 RRT-Connect로 찾고 짧게 다듬음. 펼칠 때 팔이 조리대 앞으로 최대 약 26cm 나옴.
- 낮은 곳: 일반 빌트인 식기세척기 하단 랙을 44cm 당겨 위에서 넣음 (집게 끝 최저 약 37cm). 서랍도 열어서 위에서 넣음.
- 충돌검사: 로봇 링크 = 캡슐, 가구 = 상자. 모든 작업 자세 · 보관 · 전개 경로 (관절 보간 0.015rad) · 레일 이동 (1cm 간격) · 레일/캐리지 · 로봇 자기충돌 · 조리대 위 식기까지 검사, 관통 0cm. 결과는 `assets/renders/*.json`의 `ik`.

## 실제 평면 (사용자 제공 5종)

| 평면 | 상태 |
|---|---|
| 구축 2Bay A (12,390 × 11,670, 코어 포함) | 3D 완료 · 원본과 겹쳐 확인 · ARKI 한 줄 3,150mm 배치 · 문 90° 조건 충돌검사 0cm (본문 7쪽 · 부록 B6) — 덱 대표 평면 |
| 구축 2Bay B (10,940 × 8,500) | 3D 완료 · 원본과 겹쳐 확인 · 싱크 줄 약 2.6m (냉장고 이전 시 약 3.3m) → 미적용 |
| 신축 3Bay (12,400 × 10,550) | 3D 완료 · 원본과 겹쳐 확인 · 싱크 줄 약 2.6m → 단축형 한 줄 검토 |
| 신축 4Bay (14,700 × 9,780) | 3D 완료 · 원본과 겹쳐 확인 · 싱크 줄 약 2.8m → 단축형 한 줄 검토 |
| 신축 2Bay 탑상형 (15,120 × 10,730) | 미착수 (TIPS 1차년도 평면 30개 분석에 포함) |

## 핵심 결과 (기본 시나리오, 전부 DERIVED from ASSUMPTION)

- 세대 경제성 (구축 · 구매 · 5년): 매출 {_h3['rev5']:,.0f}만원, 기여이익 {_h3['contrib5']:,.0f}만원 (Y3 원가) → {_h5['contrib5']:,.0f}만원 (Y5 원가). 설치 시점 매출 {_h3['y0'] / _h3['rev5']:.0%}.
- 가격 위험: 가치 기준 월 약 11~24만원 < 렌탈 원가 하한 월 24~31만원 → 지불의사 검증이 1순위 (M12 점검).
- 5개년: Y5 매출 {B5r['rev'][4] / 1e4:.1f}억원 · 매출총이익률 {B5r['gm'][4]:.0%} · 영업이익 {B5r['op'][4] / 1e4:.1f}억원 · 5년 누적 현금 최저 약 {B5r['min_cum_cash'] / 1e4:.0f}억원 · 손익분기 연 약 {M['breakeven_kitchens']:,.0f}세대 (6년차 이후).
- TIPS 24개월: 과제 예산 {TP['total'] / 1e4:.1f}억원 (정부 {TP['gov'] / 1e4:.0f} · 민간 {TP['private'] / 1e4:.1f}) ⊂ 회사 전체 지출 약 {TP['spend_total'] / 1e4:.1f}억원 ← TIPS {TP['gov'] / 1e4:.0f} + 운영사 투자 {_av['op_invest'] / 1e4:.0f} + 후속 투자 {_av['followon'] / 1e4:.0f}억원 (후속 없으면 약 {TP['runway_no_followon']:.0f}개월).
- 운영사 관점 판단: **WATCH** — 조건: 창업팀 역량 · 목업 검증 · 지불의사 신호 · 평면 표준안 · 실제 파트너 실증 합의.

## 다시 만들기

```bash
pip install python-pptx openpyxl pillow lxml pypdf      # LibreOffice: PDF · xlsx 재계산
python3 ARKI/source/model.py          # 가정 · 계산 → model.json
python3 ARKI/source/xlsx_model.py     # 수식 기반 xlsx
python3 /mnt/skills/public/xlsx/scripts/recalc.py ARKI/ARKI_Robotics_Financial_Model.xlsx 120   # LibreOffice 재계산
python3 ARKI/source/check_xlsx.py     # xlsx 값 ↔ model.py 교차검증
cd ARKI/render3d && npm install three@0.170.0 && bash render_v2.sh && bash render_plans.sh   # 3D 그림 + 충돌검사 (Playwright Chromium)
node shot.js stowsearch out/stow.png 64 64 "railz=30"    # 보관/전개 경로 다시 계획 → 결과를 web/stow_poses.json으로
python3 ARKI/source/build.py --pdf    # 덱 + 본문 PDF + 전체 PDF (--png: 미리보기)
python3 ARKI/source/gen_docs.py       # docs/*.md + 이 README
```

- 단일 원천: `source/model.py` 입력 (태그 · 출처 포함)과 `tips_plan()`이 덱 · xlsx · 문서의 숫자를 만듦. 덱 문구와 TIPS 과제 내용 (성과지표 · 일정 · 기술 · 지식재산)은 `slides_main.py`의 `TIPS`.
- 평면 JSON: `render3d/plans/*.json` (mm, 치수선 기준). 원본 겹침 확인 스크립트는 작업 메모 참고.

## 외부 제출 전 입력 · 확인

| 항목 | 위치 |
|---|---|
| Founder · R&D 역량 8항목 · 회사 정보 · 연락처 | 본문 1 · 14쪽 |
| 운영사명 · 투자 조건 (형태 · 기업가치 · 지분) · 운영사 연계 계획 | 본문 19쪽 · 부록 D11 |
| TIPS 공고 원문 대조 (정부지원 비율 · 민간 현금 비율 · 간접비 · 운영사 투자 요건) | 본문 19쪽 · docs/07 |
| 성과지표 세계 최고 수준 출처 · 평가 기관 확정 | 본문 15쪽 |
| 공식 통계 원문 대조 | 부록 C1 · F2 |
"""
with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(README)
print('wrote README.md')
