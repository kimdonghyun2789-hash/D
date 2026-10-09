# Generate the 20 MH Robotics IR deliverables (docs/*.md, Spec 38 order) from model.json, content.py, sources.json and the deck text log.
#   python3 MH/source/gen_docs.py      (run after model.py and build.py)
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DOCS = os.path.join(ROOT, 'docs')
os.makedirs(DOCS, exist_ok=True)
M = json.load(open(os.path.join(HERE, 'model.json'), encoding='utf-8'))
SRC = json.load(open(os.path.join(HERE, 'sources.json'), encoding='utf-8'))
DT = json.load(open(os.path.join(HERE, '_deck_text.json'), encoding='utf-8'))
import content as C
import model

IN = {d['key']: d for d in M['inputs']}
SC = M['scenarios']; B = SC['B']
HH = M['household']; H3, H5 = HH['purchase_direct_Y3'], HH['purchase_direct_Y5']
MK = M['market']['B']; F = M['funding']; TP = M['tips']; KL = M['kpi_links']
R3, R5 = M['rental']['Y3'], M['rental']['Y5']; C3, C5 = M['care']['Y3'], M['care']['Y5']; CO = M['cons']
PI = M['partner_irr']['B']; VA = M['value']
MAIN = [m for m in DT['meta'] if m.get('pack', 'main') == 'main']
APX = [m for m in DT['meta'] if m.get('pack') == 'appendix']
INT = [m for m in DT['meta'] if m.get('pack') == 'internal']
N_MAIN = len(MAIN)
DATE = '2026-10-08'
HEADER = "> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10\n"
HEADER_INT = "> MH Robotics · IR 내부 검토용 (제출 제외) · 2026.10\n"


def v(k, s='B'):
    return IN[k]['vals'][s]


def eok(x, d=1):
    return f"{x / 1e4:,.{d}f}억원"


def man(x, d=0):
    return f"{x:,.{d}f}만원"


def pct(x, d=0):
    return f"{x * 100:.{d}f}%"


def cell(c):
    return str(c).replace('\n', ' ').replace('|', '/')


def md_table(header, rows, align=None):
    al = align or ['l'] * len(header)
    sep = {'l': '---', 'r': '---:', 'c': ':---:'}
    out = ['| ' + ' | '.join(header) + ' |', '|' + '|'.join(sep[a] for a in al) + '|']
    for r in rows:
        out.append('| ' + ' | '.join(cell(c) for c in r) + ' |')
    return '\n'.join(out)


def gaejo(body):
    # 개조식: drop the sentence period at the end of prose / bullet lines (tables and code blocks untouched)
    out, code = [], False
    for l in body.split('\n'):
        if l.startswith('```'): code = not code
        elif not code and not l.startswith('|'):
            l = re.sub(r'(?<=[가-힣0-9A-Za-z\)\]%*])\.\s*$', '', l)
        out.append(l)
    return '\n'.join(out)


def write(name, body):
    with open(os.path.join(DOCS, name), 'w', encoding='utf-8') as f:
        f.write(gaejo(body.strip()) + '\n')
    print('wrote', name)


def ylist(x, f=lambda z: f"{z:,.0f}"):
    return ' / '.join(f(z) for z in x) if isinstance(x, list) else f(x)


def slide_log(sid):
    return DT['log'].get(sid, [])


def slide_sub(m):
    """Main-slide sub headline (third logged string after kicker and title)."""
    lg = slide_log(m['id'])
    return lg[2] if m['id'] != 'm01' and len(lg) > 2 else lg[3] if len(lg) > 3 else ''


def refs_to_slides(ref):
    return [int(x) for x in re.findall(r'\b(\d{2})\b', ref)]


QA_BY_SLIDE = {}
for i, q in enumerate(C.QA, 1):
    for n in refs_to_slides(q[4]):
        QA_BY_SLIDE.setdefault(n, []).append(i)

SPEC35 = ['MH Robotics · Kitchen Manipulation Robotics System', '가전 자동화 이후 남은 Physical Workflow', '왜 Kitchen인가',
          '가정용 Robot 적용의 구조적 한계', 'MH Robotics Technology Strategy', 'Adaptive Kitchen Robot Hand', 'Manipulation Skill / Calibration',
          'MH Kitchen Robotics System', '첫 검증 Workflow: CLEAN → ASSIST → COOK', 'Existing / Remodeling / New-build 적용', 'Business Model',
          'Market / Beachhead', 'GTM / Partner Distribution', 'Technology-to-Economics / Moat', 'IP / Competition', 'TIPS R&D / 24개월 Roadmap',
          'Founder / Team', 'Investment Ask / 24M Value Creation']
assert len(SPEC35) == N_MAIN == 18


# ---------------------------------------------------------------- assets per main slide (parsed from slides_mh.py)
def slide_assets():
    src = open(os.path.join(HERE, 'slides_mh.py'), encoding='utf-8').read()
    have = {os.path.splitext(f)[0] for f in os.listdir(os.path.join(ROOT, 'assets', 'renders')) if f.endswith('.png')}
    out = {}
    parts = re.split(r'\ndef (m\d\d)\(', src)
    for i in range(1, len(parts), 2):
        names = []
        for q in re.findall(r"'([a-z0-9_]+)'", parts[i + 1]):
            if q in have and q not in names:
                names.append(q)
        for q in re.findall(r"f'v2_seq_\{", parts[i + 1]):
            names += [n for n in sorted(have) if n.startswith('v2_seq_') and n not in names]
        out[parts[i]] = names
    return out


ASSETS = slide_assets()


# ================================================================ 00 index
DELIV = [
    ('01', 'Executive Summary', '01_Executive_Summary.md', '회사 정의 · 문제 · 접근 · 제품 · BM · 시장 · 자금 · 24개월 Gate', '제출 · 공유'),
    ('02', 'Main IR Deck', '02_Main_IR_Deck.md', f'본문 {N_MAIN}장 구성 · 장별 핵심 메시지 · 부록 {len(APX) - 1}장 + 목차', '제출 · 공유'),
    ('03', '각 Slide 실제 화면 문구', '03_Slide_Text.md', '본문 화면 문구 전체 (표기 순서)', '제출 · 공유'),
    ('04', '각 Slide Visual 구성', '04_Slide_Visual.md', '장별 레이아웃 · 사용 이미지 · CONCEPT 표기', '제출 · 공유'),
    ('05', 'Diagram / Chart', '05_Diagram_Chart.md', '필수 Visual 8종 위치 · 도표별 Data 출처 · 3D 렌더 재생성', '제출 · 공유'),
    ('06', 'Speaker Note', '06_Speaker_Notes.md', '장별 발표 요지 · 예상 발표 시간', '발표자용'),
    ('07', '시장 Data 및 Source', '07_Market_Data_Sources.md', '주택 · 리모델링 · 렌탈 · Care · Robot Arm · Hand Benchmark · 경쟁 · 기준 · 출처 전체', '제출 · 공유'),
    ('08', 'FACT / DERIVED / ASSUMPTION / TARGET 구분표', '08_Tag_Register.md', f"재무모델 입력 {len(M['inputs'])}개 전체 · 주요 계산값 · CONCEPT 목록", '제출 · 공유'),
    ('09', 'Business Model', '09_Business_Model.md', 'INSTALL → OPERATE → EXPAND · 가격 가설 · Rental · Care · Consumables · MH Core vs Partner', '제출 · 공유'),
    ('10', '5-Year Household Economics', '10_Household_Economics_5Y.md', '대표 1세대 5년 매출 · 매출총이익 · 서비스 원가 · Lifetime Contribution · 범위 · 민감도', '제출 · 공유'),
    ('11', 'TIPS R&D Work Package', '11_TIPS_RnD_Work_Package.md', 'TIPS 과제 (기술 검증) vs Seed (사업 검증 · 과제 외 개발) · WP1~WP6 · 과제 편성', '제출 · 공유'),
    ('12', 'Technical KPI', '12_Technical_KPI.md', 'Manipulation · Application · Business KPI 20개 · Benchmark · 목표 근거 · Hand 시험 계획', '제출 · 공유'),
    ('13', 'Patent Portfolio', '13_Patent_Portfolio.md', '출원 후보 12개 묶음 · 사업 중요도 · 차별성 · Prior Art Risk · 우선순위', '제출 · 공유'),
    ('14', '24개월 Roadmap', '14_Roadmap_24M.md', '0~6 · 7~12 · 13~18 · 19~24M 실행 · Gate · 채용 · 24M Value Creation', '제출 · 공유'),
    ('15', 'Funding Plan', '15_Funding_Plan.md', '24개월 사용처 · TIPS 과제 편성 · Seed 범위 산식 · 5개년 계획', '제출 · 공유'),
    ('16', '투자심사 예상질문 20개', '16_Investor_Questions_20.md', '질문 · 확인 포인트 · 답하는 위치', '내부 검토용'),
    ('17', '각 질문의 방어논리', '17_Defense_Logic.md', '방어논리 · 근거 (Tag) · 약한 부분 · 보강 Evidence', '내부 검토용'),
    ('18', '현재 부족한 Evidence', '18_Evidence_Gaps.md', 'Evidence Gap · Risk Register · 첫 90일 실행 목록', '내부 검토용'),
    ('19', 'Founder 입력 필요정보', '19_Founder_Inputs.md', 'Founder 입력 항목 · TIPS 요건 · 증빙 · 입력 양식', '내부 검토용'),
    ('20', '투자심사 Memo', '20_Investment_Memo.md', f'심사 의견 · Scorecard · 판단 {C.VERDICT} · 판단을 바꿀 Evidence 5개', '내부 검토용'),
]
FILES = [
    ('`MH/MH_Robotics_Seed_TIPS_IR_Final.pptx`', f'제출용 IR: 본문 {N_MAIN}장 + 부록 {len(APX) - 1}장 + 목차 (A TIPS 과제 · B 제품 · 기술 · C 시장 · 경쟁 · D 경제성 · 재무 · E IP · Risk · F 출처), 16:9'),
    ('`MH/MH_Robotics_Seed_TIPS_IR_Final_Main.pdf`', f'본문 {N_MAIN}장 (발표 · 송부용)'),
    ('`MH/MH_Robotics_Seed_TIPS_IR_Final.pdf`', '본문 + 부록 전체'),
    ('`MH/MH_Robotics_IR_Internal_QA.pptx` · `.pdf`', f'내부 검토용 {len(INT)}장 (예상질문 · 방어논리 · Evidence · Founder 입력 · 투자심사 Memo · Tag 원칙, 제출 제외)'),
    ('`MH/MH_Robotics_Financial_Model.xlsx`', '수식 재무모델: Inputs (Tag · 출처) · 5Y FM (3 Scenario) · Household · Unit Economics · Market · Budget_24M · Sensitivity'),
]
write('00_README_Index.md', f"""# MH Robotics — Seed · TIPS IR 산출물 Index

{HEADER}
## 결과물 20종

{md_table(['No', '산출물', '파일', '내용', '용도'], [(a, b, f'[{c}]({c})', d, e) for a, b, c, d, e in DELIV])}

## 파일

{md_table(['파일', '내용'], FILES)}
""")


# ================================================================ 01 executive summary
GOAL = ('Adaptive Robot Hand · Manipulation Skill · Calibration · Environment Integration 결합 → 다양한 실제 주방에서 '
        '식기 정리부터 조리까지 단계적으로 확장하는 Kitchen Manipulation Robotics System 개발  \n'
        '- 초기 CLEAN Workflow로 기술 검증 → 같은 Platform에서 ASSIST · COOK으로 Capability 확장  \n'
        '- 기존 주방 · Remodeling · New-build에 서로 다른 Integration 수준으로 적용  \n'
        '- Robot · 설치 매출 이후 Rental · Care · Consumables · Skill · Tool · Upgrade로 Installed Base 기반 반복매출 확보')
ROWS01 = [
    ('문제', '가전은 기기 안의 일을 자동화했지만, 가전 사이의 Physical Workflow (식기 이동 · 식세기 적재/인출 · 수납 · 재료 투입 · 도구)는 사람 몫. Appliance Automation ≠ Physical Workflow Automation',
     '무급 가사노동 582.4조원 중 가정관리 459.5조원 (2024) FACT · 식사 후 정리 40분/일 ASSUMPTION'),
    ('왜 Kitchen', '동작 종류가 적고 반복 (Pick · Place · Insert · Remove) · 작업영역 고정 · 물체 범위가 닫혀 있음 (기술). 매일 사용 · Remodeling / 입주라는 구매 계기 (사업)', '사업 가설 → WTP n ≥ 300 (M18)'),
    ('구조적 한계', '주방마다 형태 · 가전 · 수납 · 치수 · 설치오차가 달라 범용 Robot은 집마다 인식 · 교시 · Calibration을 반복 → 설치시간 · 비용 · 신뢰성 문제', '받은 평면 5종 중 3종 기본 배치 불가 (DERIVED)'),
    ('접근', 'Object → Adaptive Hand · Task → Skill Library · Kitchen → Perception + Calibration · 반복 작업점 → Minimal Interface. 주방 전체 표준화는 하지 않음', 'CONCEPT'),
    ('제품', 'A Robot Module · B Manipulation Layer · C Calibration Layer · D Environment Interface · E Human-Robot Safety. CLEAN (첫 검증) → ASSIST (중기) → COOK (장기 R&D)', 'CONCEPT · FUTURE'),
    ('설치 경로', f"제품 하나 · 경로 셋: Retrofit {man(HH['retrofit_purchase_Y3']['y0'])} · Remodeling {man(H3['y0'])} · New-build Option {v('p_rr_new')}만원 (B2B) + 입주 후 Robot", 'ASSUMPTION (VAT 별도)'),
    ('BM', f"INSTALL → OPERATE (Rental 월 {v('p_rent')}만 · Care 연 {v('p_care')}만 · 소모품 연 {CO['list_y']:.0f}만) → EXPAND (Skill {v('p_sw')}만 · Tool {v('p_tool')}만). 1세대 5년 매출 {man(H3['rev5'])} · 기여이익 {man(H3['contrib5'])} (Y3 원가) → {man(H5['contrib5'])} (Y5 원가)", 'DERIVED (from ASSUMPTION)'),
    ('시장', f"Bottom-up SAM 연 {MK['sam']:,.0f}억원 (Remodeling {MK['sam_remodel']:,.0f} · Retrofit {MK['sam_retro']:,.0f} · New-build {MK['sam_new']:,.0f}). Y5 계획 매출 {B['rev'][4] / 1e4:.1f}억원 = 대상 세대의 {MK['som_share_hh'] * 100:.1f}%", 'DERIVED · TARGET'),
    ('GTM', 'Phase 1 Premium Kitchen Remodeling (검증) → Phase 2 호환 주방 Retrofit → Phase 3 신축 B2B2C (Scale). 일반 시공은 Partner, MH는 Robot · Hand · Skill · Calibration · Interface 표준 · Safety · Commissioning', 'Partner 조건 협의 (M18~M24)'),
    ('자금', f"24개월 지출 {eok(F['spend_total'])} = TIPS 정부지원 8억원 (Technology De-risking, 선정 시) + Seed {F['seed_range'][0]}~{F['seed_range'][1]}억원 (Commercial Validation, Lean ~ Base). TIPS 미선정 시 Lean 범위 {eok(F['seed_no_tips'])}", 'DERIVED · TIPS 규정 FACT'),
    ('24개월 Evidence', '가정 3세대 CLEAN ≥ 90% · 주방 3종 Transfer 하락 ≤ 10%p · Calibration ≤ 4시간 · BOM · 설치 · Service 원가 실측 · WTP n ≥ 300 · 유료 전환 ≥ 2세대 · Partner 조건 · 출원 5건', 'TARGET'),
]
KEYNUM = [
    ('국내 아파트 (기회 기반, 구매시장 아님)', f"약 {MK['apt'] / 10:,.0f}만호", 'DERIVED (총주택 2,018.1만 × 65.8%, FACT)'),
    ('연간 주방 교체 (아파트)', '30만 세대', f"ASSUMPTION (교차검증 {MK['tri1'] / 10:.1f}만 · {MK['tri2'] / 10:.1f}만)"),
    ('Remodeling Beachhead', f"{MK['fit'] * 1000:,.0f}세대/년 · {MK['sam_remodel']:,.0f}억원", 'DERIVED (30만 × Premium 10% × 적용 60%)'),
    ('Robot System ASP', man(v('p_robot')), 'ASSUMPTION (WTP 검증 1순위)'),
    ('Robot BOM Y1 시제품 → Y3 → Y5', f"{v('bom')[0]:,} → {v('bom')[2]:,} → {v('bom')[4]:,}만원", 'ASSUMPTION (공개가 Benchmark 기반)'),
    ('Remodeling 1세대 설치 시점 매출', man(H3['y0']), 'DERIVED (Interface 450 + Robot 1,490 + 설치 80)'),
    ('1세대 5년 Lifetime Contribution', f"{man(H3['contrib5'])} (Y3) · {man(H5['contrib5'])} (Y5)", 'DERIVED'),
    ('Y5 매출 · 설치 (Base Plan)', f"{B['rev'][4] / 1e4:.1f}억원 · {B['kitchens'][4]:,.0f}세대", 'TARGET'),
    ('24개월 지출', eok(F['spend_total']), 'DERIVED (Bottom-up)'),
    ('Seed 범위', f"{F['seed_range'][0]}~{F['seed_range'][1]}억원 (Lean {eok(F['seed_lean'])} · Base {eok(F['seed_base'])})", 'DERIVED'),
    ('TIPS 정부지원 (일반트랙 상한)', '8억원 · 24개월 · 정부 75% 이내', 'FACT (상한) · 수령 = 선정 시'),
]
write('01_Executive_Summary.md', f"""# 01. Executive Summary

{HEADER}
## 한 문장 정의

> {GOAL}

현재 단계: **Concept** (시제품 개발 전).

## 요약

{md_table(['항목', '내용', '근거 · Tag'], ROWS01)}

## 핵심 숫자

{md_table(['항목', '값', 'Tag · 산식'], KEYNUM)}

## TIPS와 Seed의 역할 분담

{md_table(['재원', '목적', '쓰는 곳'], [
    (f"TIPS 과제 {TP['total'] / 1e4:.2f}억원 (정부 8억원 + 기관부담 {TP['private'] / 1e4:.2f}억원)", '기술 검증 (Technology De-risking)', 'WP1 Adaptive Hand · WP2 Skill · WP3 Perception / Calibration · WP4 Minimal Interface · WP5 Safety · WP6 Integrated CLEAN 실증'),
    ('민간 Seed', '사업 검증 · 과제 외 개발 (Commercial Validation)', f"기관부담금 · 과제 외 인건비 {(sum(F['people']) - sum(F['uses'][0]['tips'])) / 1e4:.2f}억원 (참여율 외 R&D · 사업 · 현장 · 경영지원) · 목업 운영 · 고객 검증 · WTP · 실증 · Partner 개발 · 운영사 선투자 요건"),
])}

## 24개월 Gate (판단 기준)

{md_table(['Gate', '확인할 Evidence', '통과 기준 (TARGET)', '미달 시'], C.GATES)}

## 가장 큰 Risk 5개

{md_table(['구분', 'Risk', '확인 시점', '대응', '중단 · 재편 기준'], C.RISKS[:5])}

""")


# ================================================================ 02 main deck structure
GROUPS = [('Why: 문제와 첫 적용 공간', 2, 4), ('How: 기술 전략과 제품', 5, 9), ('Business: 적용 경로 · BM · 시장 · GTM', 10, 13),
          ('Proof: 경제성 연결 · 경쟁 · 실행 계획', 14, 16), ('Ask: 팀과 투자 요청', 17, 18)]
rows02 = []
for m in MAIN:
    qs = QA_BY_SLIDE.get(m['no'], [])
    rows02.append((f"{m['no']:02d}", SPEC35[m['no'] - 1], m['title'], slide_sub(m), ', '.join(f'Q{q}' for q in qs) or '-'))
apx_rows = [(m['no'], m['title']) for m in APX if m['id'] != 'xIDX']
write('02_Main_IR_Deck.md', f"""# 02. Main IR Deck — 구성

{HEADER}
- 제출용: `MH/MH_Robotics_Seed_TIPS_IR_Final.pptx` (본문 {N_MAIN}장 + 부록 {len(APX) - 1}장 + 목차, 16:9) · 본문 PDF `MH_Robotics_Seed_TIPS_IR_Final_Main.pdf` · 전체 PDF `MH_Robotics_Seed_TIPS_IR_Final.pdf`
- 내부 검토용 (제출 제외): `MH/MH_Robotics_IR_Internal_QA.pptx` · `.pdf` ({len(INT)}장)
- 화면 문구 [03](03_Slide_Text.md) · Visual [04](04_Slide_Visual.md) · Diagram / Chart [05](05_Diagram_Chart.md) · 발표 요지 [06](06_Speaker_Notes.md)

## 흐름

""" + '\n'.join(f"- **{g}**: {a:02d}~{b:02d}쪽" for g, a, b in GROUPS) + f"""

## 본문 {N_MAIN}장

{md_table(['No', '구성', '화면 제목', '부제', '예상 질문 (내부 Q#)'], rows02)}

## 부록 (근거 · 계산 · 검증 계획)

{md_table(['Code', '제목'], apx_rows)}

## 내부 검토용 (제출 제외)

{md_table(['Code', '제목'], [(m['no'], m['title']) for m in INT])}
""")


# ================================================================ 03 screen text
out = []
for m in MAIN:
    out.append(f"## {m['no']:02d}. {m['title']}\n")
    out.append('```text')
    out.extend(slide_log(m['id']))
    out.append('```\n')
write('03_Slide_Text.md', f"""# 03. 각 Slide 실제 화면 문구 (본문 {N_MAIN}장)

{HEADER}
- 표 = `셀 | 셀` · 대괄호 = 화면의 작은 Tag

""" + '\n'.join(out))


# ================================================================ 04 visual composition
CONCEPT_NOTE = {'m01': '렌더 우하단 [CONCEPT RENDERING]', 'm06': 'Hand 확대 렌더 · 파지 렌더 4컷 각각 [CONCEPT]', 'm08': '렌더 좌상단 [CONCEPT]',
                'm09': '렌더 5컷 각각 [CONCEPT] · COOK 카드 [FUTURE CONCEPT]', 'm07': '평면 도식 범례 (CONCEPT)'}
out = []
for m in MAIN:
    a = ASSETS.get(m['id'], [])
    out.append(f"## {m['no']:02d}. {m['title']}\n")
    out.append(f"- **구성**: {m['visual']}")
    out.append(f"- **도표 유형**: {m['chart']}")
    out.append(f"- **사용 이미지**: {', '.join(f'`assets/renders/{n}.png`' for n in a) if a else '없음 (도형 · 표 · 텍스트)'}")
    if m['id'] in CONCEPT_NOTE:
        out.append(f"- **CONCEPT 표기**: {CONCEPT_NOTE[m['id']]}")
    out.append('')
write('04_Slide_Visual.md', f"""# 04. 각 Slide Visual 구성

{HEADER}
공통: 16:9 · 흰 배경 · 짙은 회색 글자 · 주황은 Robot Zone / Path / Key Number만 · 상단 Kicker (번호 · 구성명) → 결론형 제목 → 부제 → 본문 → 하단 출처 · 각주 → Footer.

""" + '\n'.join(out))


# ================================================================ 05 diagram / chart
REQ = [
    ('1', '실제 한국 Apartment 느낌의 MH Kitchen Robotics System Concept Rendering', '01 · 08 (부록 B3 · B4)', 'v2_cover · v2_after · v2_stow_1~5 · plan_old2a_*', '구축 2Bay 대표 평면 비율 · 상부장 하단 Rail · Robot Home · 식세기 Interface. 특정 단지 표기 없음'),
    ('2', 'Adaptive Robot Hand 확대도', '06', 'hand_hero', 'Quick Changer · 힘/토크 센서 · Wrist Camera · 교체형 Food-contact Pad · Palm Suction'),
    ('3', 'Plate · Cup · Bowl · Tool Handling', '06', 'hand_plate · hand_cup · hand_bowl · hand_tool', '접시 가장자리 Pinch · 컵 외벽 감싸기 · 그릇 테두리 Pinch · 국자 손잡이 Power Grasp (손가락 각도를 접촉점에 맞춰 계산)'),
    ('4', '다양한 Kitchen → Calibration → 동일 Skill', '07', '도형 (평면 도식 3)', 'Kitchen A ㅡ자 · B ㄱ자 · C Retrofit → Mapping · 기준점 · 가전/수납 위치 · Task Parameter → 같은 CLEAN Skill Library'),
    ('5', 'Kitchen CLEAN Workflow', '09', 'v2_seq_1~5', '식기 인식 → Pick → Dishwasher Loading → Unloading → Storage Return'),
    ('6', 'Existing / Remodeling / New-build 비교', '10', 'fig_flow_retrofit · fig_flow_remodel · fig_flow_newbuild + 표', '같은 주방 · 같은 시점 3D 3컷 (Compact Mount · Rail · 설계 반영, CONCEPT) + Integration 수준 막대 + 6행 비교표 (고객 상황 · 공사 범위 · Interface · 설치 · 매출 가설 · 역할)'),
    ('7', 'Robot + Skill + Calibration + Environment Interface Architecture', '08', 'v2_after + A~E 층 카드', 'A Robot Module · B Manipulation · C Calibration · D Environment Interface · E Safety'),
    ('8', 'Business Model: Install → Operate → Expand', '11', '도형 · 막대', '3층 항목 · 가격 가설 + 1세대 5년 층별 막대 + Rental 3자 구조'),
]
DATA = {
    'm01': '렌더 v2_cover (CONCEPT)',
    'm03': '렌더 fig_tech_m03_kitchen (구축 2Bay A 주방 · Interface 적용 예, CONCEPT) · 정성 기준 (사업 가설) → WTP n ≥ 300 (M18)',
    'm05': '렌더 fig_tech_m05_hand · v2_seq_3_load · v2_seq_1_detect · v2_stow_2_open (CONCEPT) · 대응 관계 = CONCEPT (기술 개발 전)',
    'm08': '렌더 v2_after (CONCEPT) · 안전 기준 [S39 · S47]',
    'm09': '렌더 v2_seq_1~5 (CONCEPT) · 가치 Anchor value.value · p_rent',
    'm02': '렌더 fig_flow_kitchen (로봇 없음 · 가전 사이 사람 작업 ①~④) · 가계생산 위성계정 [S40] (FACT) · 정리 시간 a_cleanup_min (ASSUMPTION)',
    'm04': '렌더 fig_var_k_old2a · old2b · new3 · new4 (확보 평면 주방 재작도 · 동일 축척) · content.PLANS · LG CLOiD 보도 [S21]',
    'm06': 'Robotiq · Inspire 공개가 [S16 · S42] · 식품 접촉 규격 [S48]',
    'm07': 'KPI 목표 (content.KPI, TARGET)',
    'm10': '렌더 fig_flow_retrofit · remodel · newbuild (CONCEPT) · inputs p_rt_if · p_rr · p_rr_new · p_robot · p_comm · p_comm_rt · comm_cost · comm_cost_rt · kpi_links.inst_h',
    'm11': '렌더 v2_seq_3_load · hand_hero · hand_tool (CONCEPT) · household.purchase_direct_Y3 / _Y5 · partner_irr.B · scenarios.B recurring · oe_share · inputs p_* (xlsx Household · Unit_Economics 시트)',
    'm12': 'market.B 채널별 대상 세대 · 패키지 · 연 규모 → 채널 구성 막대 · Y5 계획 세대 (xlsx Market 시트) · [S1~S6]',
    'm13': 'scenarios.B rd · rp · rt · ni · kitchens (xlsx FM 시트, TARGET)',
    'm14': 'kpi_links (inst_h · care_unit · bom · pad_life) · sens_household (xlsx Sensitivity)',
    'm15': 'content.COMP · content.IP · [S19~S25 · S41 · S45 · S46 · S49~S51]',
    'm16': '렌더 hand_* · v2_cover · apt2/3/4_kitchen · v2_after (CONCEPT) · content.WP · content.GATES · TIPS 규정 [S33 · S52]',
    'm17': 'model.TEAM · funding.team (시작월 × FTE → 월별 인원 막대 · Y1 · Y2 평균 FTE) (xlsx Budget_24M)',
    'm18': 'funding.uses · tips.rows · funding.seed_* · post_seed_burn · breakeven_kitchens (xlsx Budget_24M · FM)',
}
import glob as _glob
FIG_DESC = {'render_fig_flow.sh': 'fig_flow_kitchen (02 · 로봇 없음) · fig_flow_retrofit · remodel · newbuild (10 · CONCEPT)',
            'render_fig_var.sh': 'fig_var_k_* (04 · 확보 평면 주방 재작도 · 동일 축척) · fig_var_top_* (부록 B2)',
            'render_fig_tech.sh': 'fig_tech_* (03 · 05 · 부록 B5 · CONCEPT)',
            'render_fig_bm.sh': 'fig_bm_* (11 · 16 · CONCEPT)'}
FIG_SH = ''.join(f"bash {os.path.basename(f):<23}# {FIG_DESC.get(os.path.basename(f)) or open(f, encoding='utf-8').readline().lstrip('#').strip()}\n"
                 for f in sorted(_glob.glob(os.path.join(ROOT, 'render3d', 'render_fig_*.sh'))))
rows05 = [(f"{m['no']:02d}", m['title'][:40] + ('…' if len(m['title']) > 40 else ''), m['chart'], DATA.get(m['id'], '-')) for m in MAIN]
write('05_Diagram_Chart.md', f"""# 05. Diagram / Chart

{HEADER}
## 핵심 Visual 8종 → 반영 위치

{md_table(['#', '필수 Visual', '본문 (부록)', '이미지 · 도형', '내용'], REQ)}

표기: 제품 콘셉트 이미지 = `CONCEPT` · COOK · Robot Upgrade = `FUTURE CONCEPT`.

## 장별 도표와 Data 출처

{md_table(['No', '장', '도표', 'Data 출처 (model.json key · xlsx 시트 · Source ID)'], rows05)}

도표 숫자 원천 = `model.json` (xlsx 수식 재계산값과 대조 완료).

## 3D 콘셉트 렌더 재생성

three.js + Playwright (Chromium) 기반. `MH/render3d`에서:

```bash
npm install                 # three 0.170 · playwright
bash render_v2.sh           # v2_cover · v2_after · v2_seq_1~5 · v2_stow_1~5 (충돌검사 포함)
bash render_plans.sh        # 대표 평면 (구축 2Bay A) 원본 · Interface 적용 · 충돌검사
bash render_hand.sh         # hand_hero · hand_plate · hand_cup · hand_bowl · hand_tool
{FIG_SH}```

PNG 옆 JSON = Callout 위치 (Anchor) · 충돌검사 결과.
""")


# ================================================================ 06 speaker notes
TIME = [('표지 · Why (01~04)', 1, 4, 3.0), ('How (05~09)', 5, 9, 4.5), ('Business (10~13)', 10, 13, 3.5), ('Proof (14~16)', 14, 16, 2.5), ('Ask (17~18)', 17, 18, 1.5)]
out = []
for m in MAIN:
    out.append(f"## {m['no']:02d}. {m['title']}\n")
    out.append(m['note'] + '\n')
write('06_Speaker_Notes.md', f"""# 06. Speaker Note (본문 {N_MAIN}장)

{HEADER}
발표 시간 배분 (15분 기준, 질의응답 별도)

{md_table(['구간', '쪽', '분'], [(a, f'{b:02d}~{c:02d}', d) for a, b, c, d in TIME], ['l', 'c', 'r'])}

""" + '\n'.join(out))


# ================================================================ 07 market data & sources
FACT_IN = [d for d in M['inputs'] if d['tag'] == 'FACT']
src_rows = [(d['id'], d['item'], d['value'], d.get('basis', ''), d['source'], d.get('used_in', '')) for d in SRC]
write('07_Market_Data_Sources.md', f"""# 07. 시장 Data 및 Source

{HEADER}
조회일 2026-10-07~08 · 국가데이터처 (통계청) · 국토교통부 · 한국부동산원 · 중소벤처기업부 · 기업 공식자료 · 학술자료 · 보도 인용 포함

## 1. 주택 · Apartment Stock · 노후 · 거래 · 입주

{md_table(['항목', '값', 'Tag', '출처 / 산식'], C.HOUSING)}

## 2. Remodeling · Premium Kitchen · Rental · Care 사례

{md_table(['항목', '값', 'Tag', '비고'], C.REFS)}

## 3. Robot Arm · Hand · Sensor Benchmark (공개 판매가)

{md_table(['Benchmark', 'USD (FACT)', f"만원 (환율 {C.FX:,}원/USD, ASSUMPTION)"], C.BENCH, ['l', 'r', 'r'])}

## 4. 경쟁 · 인접 Player (공개 자료)

{md_table(['Player', '구분', '공개 내용', '가격 · 상태', '접근', '출처'], [(a, b, c, d, e, f'[{s}]') for a, b, c, d, e, s in C.COMP])}

## 5. 안전 · 인증 · 식품 접촉 기준

{md_table(['항목', '내용', 'Tag', '출처'], C.SAFETY)}

## 6. 재무모델에 쓰인 FACT 입력 ({len(FACT_IN)}개)

{md_table(['Key', '항목', '값', '단위', '출처'], [(d['key'], d['desc'], ylist(d['vals']['B'], lambda z: f'{z:,}' if isinstance(z, (int, float)) else str(z)), d['unit'], d['src']) for d in FACT_IN])}

## 7. 공식 통계가 없는 항목 → ASSUMPTION + 검증 계획

{md_table(['가정', 'Tag', '검증 방법', '시점'], C.MKT_VALID)}

- 공식 통계 미확인 항목: 식기세척기 보급률 · 연간 주방 교체 세대 수 · Premium Kitchen 시장 규모 → 견적 20건 · 평면 30개 · 소비자 조사 n ≥ 300으로 대체 예정.

## 8. 전체 출처 ({len(SRC)}건, sources.json)

{md_table(['ID', '항목', '값', '기준', '출처', '사용처'], src_rows)}
""")


# ================================================================ 08 tag register
GROUP_NAME = {'market': '시장', 'value': '고객 가치', 'price': '가격', 'cost': '원가', 'volume': '물량', 'opex': '운영비', 'funding': '자금 · TIPS'}
cnt = {}
for d in M['inputs']:
    cnt[d['tag']] = cnt.get(d['tag'], 0) + 1


def fmtv(x, unit=''):
    if isinstance(x, list):
        return ' / '.join(fmtv(z, unit) for z in x)
    if unit.startswith('%') and isinstance(x, (int, float)):
        return f'{x * 100:.1f}'.rstrip('0').rstrip('.') + '%'
    if isinstance(x, float):
        return f'{x:,.3f}'.rstrip('0').rstrip('.') if abs(x) < 10 else f'{x:,.2f}'.rstrip('0').rstrip('.')
    return f'{x:,}' if isinstance(x, int) else str(x)


inp_sections = []
for g in ['market', 'value', 'price', 'cost', 'volume', 'opex', 'funding']:
    rows = []
    for d in M['inputs']:
        if d['group'] != g:
            continue
        cv, bv, uv = (d['vals'][s] for s in 'CBU')
        u = d['unit']
        rows.append((f"`{d['key']}`", d['desc'], u, d['tag'], fmtv(cv, u) if cv != bv else '=', fmtv(bv, u), fmtv(uv, u) if uv != bv else '=', d['src'] or '-'))
    inp_sections.append(f"### {GROUP_NAME[g]} ({len(rows)})\n\n" + md_table(['Key', '항목', '단위', 'Tag', 'Conservative', 'Base', 'Upside', '출처 · 근거'], rows))
DERIVED_ROWS = [
    ('국내 아파트 수', f"약 {MK['apt'] / 10:,.0f}만호", '총주택 2,018.1만 × 65.8%', 'market.B.apt'),
    ('연간 주방 교체 교차검증 ① · ②', f"{MK['tri1'] / 10:.1f}만 · {MK['tri2'] / 10:.1f}만", '20년+ 아파트 ÷ 교체주기 22년 · 매매 × 70% × 40% + 비거래 10만', 'market.B.tri1 · tri2'),
    ('Remodeling SAM', f"{MK['sam_remodel']:,.0f}억원/년", '30만 × 10% × 60% × 패키지 1,784.5만원', 'market.B.sam_remodel'),
    ('Retrofit SAM', f"{MK['sam_retro']:,.0f}억원/년", f"{MK['retro_pool'] / 10:.1f}만 (재고) × 0.5% × 1,760만원", 'market.B.sam_retro'),
    ('New-build SAM', f"{MK['sam_new']:,.0f}억원/년", '20만 × 15% × 10% × 612.5만원', 'market.B.sam_new'),
    ('Recurring (1,000대당)', f"{MK['recurring_per_1000']:.1f}억원/년", f"ARPU {MK['arpu']:.1f}만원 (Care 70% × 48 + 소모품 70% × 36)", 'market.B.recurring_per_1000'),
    ('Y5 매출 / 대상 세대 비중', f"{B['rev'][4] / 1e4:.1f}억원 · {MK['som_share_hh'] * 100:.1f}%", '560세대 ÷ 대상 세대 합', 'market.B.som · som_share_hh'),
    ('1세대 5년 매출 · 기여이익 (Y3 원가)', f"{man(H3['rev5'])} · {man(H3['contrib5'])} ({pct(H3['cm5'], 1)})", '부록 D2 · 10번 문서', 'household.purchase_direct_Y3'),
    ('1세대 5년 기여이익 (Y5 원가)', f"{man(H5['contrib5'])} ({pct(H5['cm5'], 1)})", 'BOM 915 · 설치 38 · Care 26.8만원', 'household.purchase_direct_Y5'),
    ('Rental 월 원가 · Payback (Y3)', f"{R3['cost_m']:.1f}만원 · {R3['payback']:.0f}개월", '감가 + 금융 + Care + Grip + Reserve', 'rental.Y3'),
    ('Partner IRR (연)', pct(PI['irr_y'], 1), f"Robot을 ASP의 88% ({PI['price']:,.0f}만원)에 매입, 월 {PI['inflow']:.0f}만원 순유입, 잔존 15%", 'partner_irr.B'),
    ('Care 마진 Y3 → Y5', f"{pct(C3['margin'])} → {pct(C5['margin'])}", '요금 48만원 − (방문 + 고장 + Cloud)', 'care.Y3 · Y5'),
    ('설치 인시 (Remodeling) Y2 · Y3 · Y5', f"{KL['inst_h'][1]:.0f} · {KL['inst_h'][2]:.0f} · {KL['inst_h'][4]:.0f}인시", f"설치 원가 ÷ 시간당 {KL['hour']:.1f}만원", 'kpi_links.inst_h'),
    ('Pad 수명 목표', f"{KL['pad_life']:,.0f}회", '하루 60회 × 365 ÷ 4 (분기 교체)', 'kpi_links.pad_life'),
    ('24개월 지출', eok(F['spend_total']), '팀 계획 + 비용 + 예비비 10% + 연구수당', 'funding.spend_total'),
    ('TIPS 과제 총액', f"{TP['total'] / 1e4:.2f}억원", '정부 8억원 ÷ 75%', 'tips.total'),
    ('Seed Base · Lean · TIPS 미선정', f"{eok(F['seed_base'])} · {eok(F['seed_lean'])} · {eok(F['seed_no_tips'])}", '지출 − TIPS 정부지원 + Y2 월지출 × 3개월', 'funding.seed_*'),
    ('손익분기 설치 물량 (Y5 단가 · 원가)', f"연 약 {M['breakeven_kitchens']:,.0f}세대", 'Y5 Opex ÷ 세대당 기여이익', 'breakeven_kitchens'),
    ('Series A 이후 2년 (Y3~Y4) 현금 소요', eok(M['post_seed_burn']['y3_y4'], 0), 'Base 계획 기준', 'post_seed_burn.y3_y4'),
]
TARGET_ROWS = [(f"`{d['key']}`", d['desc'], fmtv(d['vals']['B'], d['unit']), d['src'] or '-') for d in M['inputs'] if d['tag'] == 'TARGET']
CONCEPT_ROWS = [
    ('Adaptive Robot Hand 형상 · 구성', '06 · 부록 B1', 'CONCEPT (v1~v3 설계 전)'),
    ('Robot Home · Rail · 식세기 Interface · Storage Dock', '01 · 08 · 10 · 부록 B3 · B4', 'CONCEPT (3D 충돌검사 = 모델 기준)'),
    ('CLEAN 5단계 동작 장면', '09', 'CONCEPT'),
    ('Kitchen A~C 평면 도식', '07', 'CONCEPT (개념 예시)'),
    ('Calibration 4요소 · Skill 실행 구조', '07 · 08', 'CONCEPT (개발 전)'),
    ('ASSIST Skill Pack · Tool', '09 · 11', 'FUTURE (출시 전제, Y3~)'),
    ('COOK · Robot Upgrade', '09 · 11', 'FUTURE CONCEPT (5년 Base 매출 미반영)'),
    ('MH 안전 원칙 (Zone · 감속 · Safe Home Return)', '08 · 부록 B5', 'CONCEPT'),
]
write('08_Tag_Register.md', f"""# 08. FACT / DERIVED / ASSUMPTION / TARGET 구분표

{HEADER}
## Tag 정의

{md_table(['Tag', '정의', '예'], [
    ('FACT', '공식 통계 · 공개자료로 확인된 값', '총주택 2,018.1만호 · TIPS 8억원 · Robotiq 2F-85 약 $5,825'),
    ('DERIVED', 'FACT 또는 가정으로 계산한 값 (산식 공개)', '아파트 약 1,328만호 · 1세대 5년 기여이익 · Seed 범위'),
    ('ASSUMPTION', '현재 사업 가설 (검증 전)', 'Robot ASP 1,490만원 · Premium 10% · 적용률 60%'),
    ('TARGET', '24개월 · 이후 목표', '가정 실증 ≥ 90% · 출원 5건 · 설치 물량'),
    ('CONCEPT', '실물 없는 설계 개념 (그림 · 도식)', 'Hand 렌더 · Robot Home'),
    ('TBV (To Be Validated)', '검증 방법이 정해진 미확인 사실', '식세기 보급률 · 인증 적용 범위'),
    ('FUTURE', '현재 없는 제품 · 기능', 'COOK · Upgrade'),
])}

재무모델 입력 {len(M['inputs'])}개: {' · '.join(f'{k} {n}개' for k, n in sorted(cnt.items(), key=lambda z: -z[1]))}. 같은 표가 xlsx `Inputs` 시트에 있음 (Tag · 출처 포함).

## 1. 재무모델 입력 전체 (Scenario별 값, `=`은 Base와 같음)

연도별 값은 Y1 / Y2 / Y3 / Y4 / Y5 순서.

""" + '\n\n'.join(inp_sections) + f"""

## 2. 주요 계산값 (DERIVED)

{md_table(['항목', '값', '산식', 'model.json key'], DERIVED_ROWS)}

## 3. TARGET (물량 · 표준화 목표)

{md_table(['Key', '항목', 'Base (Y1~Y5)', '근거'], TARGET_ROWS)}

기술 KPI 목표 (M6~M24)는 [12_Technical_KPI.md](12_Technical_KPI.md).

## 4. CONCEPT · FUTURE

{md_table(['대상', '위치 (본문 · 부록)', 'Tag'], CONCEPT_ROWS)}
""")


# ================================================================ 09 business model
lay = lambda k: [B[k][i] for i in range(5)]
rev_mix = [('INSTALL (Interface · 설치 · Robot)', lay('install')), ('OPERATE (Rental · Care · 소모품)', lay('recurring')), ('EXPAND (Skill · Tool)', lay('expand'))]
mix_rows = [(n, *[f"{x / 1e4:.1f}" for x in xs]) for n, xs in rev_mix]
mix_rows.append(('매출 합계', *[f"{x / 1e4:.1f}" for x in B['rev']]))
mix_rows.append(('OPERATE + EXPAND 비중', *[pct(x) for x in B['oe_share']]))
ch_rows = []
for k, lab in [('retrofit_purchase', 'Existing Retrofit'), ('purchase_direct', 'Remodeling (직접)'), ('purchase_partner', 'Remodeling (Partner 경유)'),
               ('newbuild_purchase', 'New-build (Option 세대 · 입주 후 Robot)'), ('rental_direct', 'Remodeling Rental (MH 보유)')]:
    a3, a5 = HH[k + '_Y3'], HH[k + '_Y5']
    ch_rows.append((lab, man(a3['y0']), man(a3['rev5']), f"{man(a3['contrib5'])} ({pct(a3['cm5'])})", f"{man(a5['contrib5'])} ({pct(a5['cm5'])})"))
write('09_Business_Model.md', f"""# 09. Business Model

{HEADER}
## 한 줄 정의

INSTALL (Robot System · Interface · 설치) → OPERATE (Rental · Care · 소모품 반복매출) → EXPAND (같은 Platform에 Skill · Tool 추가). Installed Base 증가 → 반복 · 확장 매출 비중 확대 구조 (가설).

## 3층 구조 (가격 = ASSUMPTION, VAT 별도)

{md_table(['층', '항목', '가격 가설', '근거 · 비고'], [
    ('INSTALL', 'Robot System (Arm · Adaptive Hand · Vision · Safety)', man(v('p_robot')), f"BOM Y3 {v('bom')[2]:,} → Y5 {v('bom')[4]:,}만원 · Hardware 마진 {pct(1 - v('bom')[2] / v('p_robot'))} → {pct(1 - v('bom')[4] / v('p_robot'))}"),
    ('INSTALL', 'Interface · Integration', f"Retrofit {v('p_rt_if')} · Remodeling {v('p_rr')} · New-build Option {v('p_rr_new')}만원", 'Robot Home · Rail · 식세기 Interface · Dock · Vision Reference (경로별 수준 다름)'),
    ('INSTALL', 'Installation · Calibration · Safety Check', f"{v('p_comm')}만원 (Retrofit {v('p_comm_rt')})", f"원가 Y3 {v('comm_cost')[2]}만원 (약 {KL['inst_h'][2]:.0f}인시)"),
    ('OPERATE', 'Robot Rental (60개월, Care Basic · Grip Kit 포함)', f"월 {v('p_rent')}만원", f"월 원가 Y3 {R3['cost_m']:.1f} → Y5 {R5['cost_m']:.1f}만원"),
    ('OPERATE', 'Care (Robot Lifecycle Maintenance)', f"연 {v('p_care')}만원", f"원가 Y3 {C3['cost']:.1f} → Y5 {C5['cost']:.1f}만원 · 가입률 {pct(v('care_attach'))}"),
    ('OPERATE', 'Consumables (Grip · Cleaning · Protection Kit)', f"연 {CO['list_y']:.0f}만원 (List)", f"구매율 {pct(v('cons_attach'))} · 원가율 {pct(v('cons_cogs'))}"),
    ('EXPAND', 'ASSIST Skill Pack (설치 다음 해)', f"{v('p_sw')}만원", f"구매율 {pct(v('sw_attach'))} (FUTURE: ASSIST 출시 전제)"),
    ('EXPAND', 'Tool · End-effector (설치 2년 후)', f"{v('p_tool')}만원", f"구매율 {pct(v('tool_attach'))}"),
    ('EXPAND', 'COOK Skill · Robot Upgrade', 'FUTURE', '5년 Base 매출 미반영'),
])}

## 가격 가설의 범위 (원가 Floor · 시장 Reference · 가치 Anchor)

{md_table(['항목', '가격 가설', '원가 Floor (DERIVED)', '시장 Reference (FACT)', '가치 Anchor'], C.PRICE)}

**가치 Gap**: CLEAN만의 가사 대체 가치 = 월 약 {VA['value']:.0f}만원 (정리 {v('a_cleanup_min')}분/일 × {pct(v('a_auto_share'))} 자동화 × 가사서비스 {v('f_helper_rate')}만원/h, 범위 {VA['lo']:.0f}~{VA['hi']:.0f}만원) < Rental 월 {v('p_rent')}만원. → Premium Remodeling 고객부터, ASSIST 확장 · 위생 · 편의 가치를 묶어 WTP 조사 (n ≥ 300 · 예약금, M18).

## 설치 경로별 1세대 경제성 (구매, 5년, 만원)

{md_table(['경로', '설치 시점 매출', '5년 매출', '5년 기여이익 (Y3 원가)', '5년 기여이익 (Y5 원가)'], ch_rows, ['l', 'r', 'r', 'r', 'r'])}

Retrofit은 Partner 수수료 · 현장 Calibration 비용 때문에 낮고, New-build는 Project 수주비용이 세대당 작아 높음. 상세: [10_Household_Economics_5Y.md](10_Household_Economics_5Y.md)

## Rental 구조 (초기 부담 완화 수단)

- **Pilot (Y2~Y3)**: MH가 직접 보유 · 운영 (실증 3세대 + 초기 고객).
- **Scale (Y4~)**: Rental · Capital Partner가 Robot 자산을 ASP의 {pct(v('wholesale'))}에 매입 · 보유, 고객은 Partner에 월 {v('p_rent')}만원, MH는 Product · SW · Care 담당 + 서비스료 월 {v('partner_fee'):.0f}만원.
- Partner 관점: 매입가 {PI['price']:,.0f}만원 · 월 순유입 {PI['inflow']:.0f}만원 · 60개월 · 잔존 15% → 연 IRR 약 {pct(PI['irr_y'], 1)} · 단순 회수 약 {PI['payback']:.0f}개월 (DERIVED).
- 회수 약 {PI['payback']:.0f}개월 > Partner 요구 {PI['hurdle']}개월 (ASSUMPTION) → 매입가율 · 서비스료 · 계약기간 조건 협의 필요 (M24 Partner 조건).
- MH Balance Sheet의 Rental 자산 누적 지양 (Scale 단계 Partner 보유).

{md_table(['Rental 월 단위 (만원)', 'Y3', 'Y5'], [
    ('감가 (잔존 15%)', f"{R3['lines']['dep']:.1f}", f"{R5['lines']['dep']:.1f}"), ('금융비용 (연 8%)', f"{R3['lines']['fin']:.1f}", f"{R5['lines']['fin']:.1f}"),
    ('Care 원가', f"{R3['lines']['care']:.1f}", f"{R5['lines']['care']:.1f}"), ('Grip Kit 원가', f"{R3['lines']['grip']:.1f}", f"{R5['lines']['grip']:.1f}"),
    ('Failure Reserve', f"{R3['lines']['reserve']:.1f}", f"{R5['lines']['reserve']:.1f}"), ('**월 원가 합계**', f"{R3['cost_m']:.1f}", f"{R5['cost_m']:.1f}"),
    ('월 요금', f"{R3['fee']}", f"{R5['fee']}"), ('**월 Contribution**', f"{R3['contrib_m']:.1f}", f"{R5['contrib_m']:.1f}"), ('Payback (개월)', f"{R3['payback']:.0f}", f"{R5['payback']:.0f}"),
], ['l', 'r', 'r'])}

## Care = Robot Lifecycle Maintenance (Software 구독 아님)

포함: 정기 안전점검 · Calibration · 원격진단 · Robot / Rail 상태점검 · Vision Calibration · SW Update · Consumables Check · A/S.

{md_table(['Care (만원/대 · 년)', 'Y3', 'Y5'], [
    ('요금', f"{C3['fee']}", f"{C5['fee']}"), ('정기 방문 원가', f"{C3['visits']:.1f}", f"{C5['visits']:.1f}"), ('고장 방문 원가', f"{C3['corrective']:.1f}", f"{C5['corrective']:.1f}"),
    ('Cloud · SW', f"{C3['cloud']}", f"{C5['cloud']}"), ('**원가 합계**', f"{C3['cost']:.1f}", f"{C5['cost']:.1f}"), ('**마진**', pct(C3['margin']), pct(C5['margin'])),
], ['l', 'r', 'r'])}

선례: 코웨이 국내 렌탈 계정 748만 (2026 1Q) · LG 가전 구독 매출 2조원+ · 케어매니저 약 4,000명 (2025) [S12 · S41].

## Consumables = 실제 마모 · 위생 기반 (억지 Lock-in 아님)

{md_table(['Kit', '단가 (만원)', '교체 (회/년)', '연 (만원)'], [(k, p, n, f'{p * n:.0f}') for k, p, n in CO['kits']] + [('List 합계', '', '', f"{CO['list_y']:.0f}")], ['l', 'r', 'r', 'r'])}

후보: Grip Pad · Finger Pad · Food-contact Tip · Suction Seal · Cleaning Pad · Protective Cover. 교체주기는 Pad 수명 가속시험 (목표 ≥ {KL['pad_life']:,.0f}회 파지, M18~M24)으로 확정. 식품 접촉 부품은 「기구 및 용기 · 포장의 기준 및 규격」 대응 [S48].

## 회사 매출 구성 (Base Plan, 억원, TARGET / ASSUMPTION)

{md_table(['층', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'], mix_rows, ['l', 'r', 'r', 'r', 'r', 'r'])}

반복매출 (OPERATE) Y3 {B['recurring'][2] / 1e4:.1f} → Y5 {B['recurring'][4] / 1e4:.1f}억원 (Installed Base {B['base_end'][4]:,.0f}대) · Y5 매출 중 OPERATE + EXPAND {pct(B['oe_share'][4])} = 설치 초기 구조 (Installed Base 누적 후 비중 확대, DERIVED).

## MH Core vs Partner (Product Company 구조)

{md_table(['MH Core', 'Partner'], [
    ('Robot · Robot Hand', '철거 · 가구'), ('Manipulation Skill', '전기 · 배관'), ('Calibration', '일반 시공'), ('Interface Standard', '(신축) 건설사 · 주방가구사'),
    ('Safety · Commissioning · QA', '(Rental) 렌탈 · 캐피탈사'),
])}

Installation Volume 증가 ≠ 본사 현장인력 동일비율 증가. 현장 인력은 설치 엔지니어 · Technician (24개월 차 2명) 중심, 설치 인시는 Calibration 기술로 Y2 약 {KL['inst_h'][1]:.0f} → Y5 약 {KL['inst_h'][4]:.0f}인시 목표 (TARGET).
""")


# ================================================================ 10 household economics
def hh_lines(h):
    R, Cc = h['R'], h['C']
    rows = []
    for k, lab in [('kitchen', 'Interface · Integration'), ('comm', 'Installation · Calibration'), ('robot', 'Robot System'), ('rental', 'Rental (60개월)'),
                   ('care', 'Care (5년)'), ('cons', 'Consumables (5년, 구매율 반영)'), ('sw', 'ASSIST Skill (기대값)'), ('tool', 'Tool · End-effector (기대값)')]:
        if k in R:
            rows.append((lab, f"{R[k]:,.1f}".rstrip('0').rstrip('.')))
    return rows


def cost_lines(h):
    Cc = h['C']
    names = {'kitchen': 'Interface Kit 원가', 'comm': '설치 · Calibration 원가', 'log': '물류', 'robot': 'Robot BOM' if h['mode'] == 'purchase' else 'Robot 순감가 (잔존 15% 회수)', 'finance': 'Rental 금융비용',
             'warranty': 'Warranty Reserve', 'care': 'Care 원가 (5년)', 'cons': 'Consumables 원가', 'sw': 'Skill 원가', 'tool': 'Tool 원가', 'channel': '채널비용 (획득 · Partner · 수주)'}
    return [(names[k], f"{x:,.1f}".rstrip('0').rstrip('.')) for k, x in Cc.items()]


rng = []
for s, lab in (('C', 'Conservative'), ('B', 'Base'), ('U', 'Upside')):
    h3, h5 = model.household(s, 2), model.household(s, 4)
    rng.append((lab, f"{v('p_robot', s):,}", f"{v('bom', s)[2]:,} / {v('bom', s)[4]:,}", man(h3['y0']), man(h3['rev5']), f"{man(h3['contrib5'])} ({pct(h3['cm5'])})", f"{man(h5['contrib5'])} ({pct(h5['cm5'])})"))
var_keys = [('purchase_direct', 'Remodeling 구매 (직접)'), ('purchase_partner', 'Remodeling 구매 (Partner)'), ('rental_direct', 'Remodeling Rental (MH 보유)'),
            ('rental_partner', 'Remodeling Rental (Partner 경유 판매)'), ('retrofit_purchase', 'Retrofit 구매'), ('newbuild_purchase', 'New-build 구매')]
var_rows = []
for k, lab in var_keys:
    a3, a5 = HH[k + '_Y3'], HH[k + '_Y5']
    var_rows.append((lab, f"{a3['y0']:,.0f}", f"{a3['rev5']:,.0f}", f"{a3['gp5']:,.0f}", f"{a3['service_cost5']:,.0f}", f"{a3['contrib5']:,.0f} ({pct(a3['cm5'])})", f"{a5['contrib5']:,.0f} ({pct(a5['cm5'])})"))
sh = M['sens_household']
write('10_Household_Economics_5Y.md', f"""# 10. 5-Year Household Economics

{HEADER}
## 대표 고객 1세대 정의

- Premium 주방 Remodeling 시점에 MH System을 함께 설치하는 아파트 1세대, **직접 판매 · 구매 · Care 가입**.
- 5년 기대값 (Skill · Tool은 구매율 반영). 원가는 해당 연도 수준을 5년간 적용: **Y3 원가** (첫 상용 단계) · **Y5 원가** (BOM · 설치 · 방문 개선 후).
- 모든 값 만원 · VAT 별도 · 주방 공사비 별도 · DERIVED (from ASSUMPTION). 가격 실측 없음 → 공개가격 · Component Benchmark 기반 ASSUMPTION 범위 (아래 3).

## 1. 대표 1세대 5년 (Remodeling 구매, Y3 원가)

{md_table(['매출 (만원)', '5년'], hh_lines(H3) + [('**5-Year Revenue**', f"**{H3['rev5']:,.0f}**")], ['l', 'r'])}

{md_table(['원가 (만원)', '5년'], cost_lines(H3) + [('**총원가**', f"**{H3['cost5']:,.1f}**")], ['l', 'r'])}

{md_table(['산출 항목', '값', '정의'], [
    ('Initial (INSTALL)', man(H3['layers']['install']), 'Interface 450 + 설치 80 + Robot 1,490'),
    ('Recurring (OPERATE, 5년)', man(H3['layers']['operate']), 'Care 5 × 48 + 소모품 5 × 70% × 36'),
    ('Expansion (EXPAND, 5년)', man(H3['layers']['expand']), 'ASSIST Skill 20% × 60 + Tool 25% × 80. COOK Skill · Upgrade = FUTURE (0)'),
    ('5-Year Revenue', man(H3['rev5']), '합계'),
    ('Gross Profit (채널비용 전)', f"{man(H3['gp5'])} ({pct(H3['gm5'])})", '매출 − 제품 · 설치 · 서비스 원가'),
    ('Expected Service Cost', man(H3['service_cost5'], 1), 'Care 원가 + 소모품 원가 + Warranty'),
    ('**Lifetime Contribution**', f"**{man(H3['contrib5'])} ({pct(H3['cm5'], 1)})**", 'Gross Profit − 채널비용 (직접판매 획득비용 150)'),
])}

같은 1세대를 **Y5 원가**로 보면: Robot BOM {H5['C']['robot']:,.0f} · 설치 {H5['C']['comm']} · Care 원가 {H5['C']['care']:,.0f} → Lifetime Contribution **{man(H5['contrib5'])} ({pct(H5['cm5'])})**.

## 2. 고객 지불 구조

{md_table(['구분', '구매', 'Rental'], [
    ('설치 시점', man(H3['y0']), f"{man(HH['rental_direct_Y3']['y0'])} (Interface + 설치)"),
    ('매월', '-', f"{v('p_rent')}만원 × 60개월 (Care Basic · Grip Kit 포함)"),
    ('매년', f"Care {v('p_care')}만원 (선택) · 소모품 약 {CO['list_y']:.0f}만원 (List)", '추가 소모품 (Cleaning · Protection)'),
    ('5년 총지불 (기대값)', man(H3['rev5']), man(HH['rental_direct_Y3']['rev5'])),
])}

가치 Anchor: CLEAN만의 가사 대체 가치 월 약 {VA['value']:.0f}만원 (범위 {VA['lo']:.0f}~{VA['hi']:.0f}) × 60개월 ≈ {VA['value'] * 60:,.0f}만원 → 구매가보다 낮음. **CLEAN 단독 가치로는 가격을 정당화하지 못할 수 있음** (핵심 미검증 가설 · WTP M18).

## 3. ASSUMPTION 범위 (Scenario, 구매 · Remodeling 직접)

{md_table(['Scenario', 'Robot ASP', 'BOM Y3 / Y5', '설치 시점', '5년 매출', 'Contribution (Y3 원가)', 'Contribution (Y5 원가)'], rng, ['l', 'r', 'r', 'r', 'r', 'r', 'r'])}

Conservative (ASP {v('p_robot', 'C'):,} · Interface {v('p_rr', 'C')} · Care {v('p_care', 'C')}만원 · BOM 높음 · 고장 {v('corrective', 'C')}회/년 · 획득비용 {v('cac', 'C')}만원)에서는 Y3 원가 기준 **적자**. → 가격 · BOM이 사업성의 1 · 2순위 변수.

## 4. 설치 경로 · 판매 방식별 (만원)

{md_table(['경로', '설치 시점 매출', '5년 매출', 'Gross Profit', 'Service Cost', 'Contribution (Y3 원가)', 'Contribution (Y5 원가)'], var_rows, ['l', 'r', 'r', 'r', 'r', 'r', 'r'])}

Rental (MH 보유)은 금융비용을 포함하고 잔존가치 15%를 회수하는 기준. Scale 단계에서는 Partner가 자산을 보유 (09 문서).

## 5. 민감도 (Remodeling 구매 1세대 · Y3 원가 · 기준 {sh['base']:,.0f}만원)

{md_table(['변수', '불리', '유리'], [(d['name'], f"{d['lo']:+,.0f}", f"{d['hi']:+,.0f}") for d in sh['items']], ['l', 'r', 'r'])}

## 6. 검증 계획

- Robot ASP · Interface 가격: WTP 조사 n ≥ 300 + 예약금 Test (M18) · 유료 전환 ≥ 2세대 (M24).
- BOM: 100대/년 견적 (M18). 설치 · Care · 고장 원가: 가정 3세대 실측 (M24).
- 소모품 교체주기: Pad 수명 가속시험 (M18~M24).
""")


# ================================================================ 11 TIPS R&D work packages
TIPS_RULES = [
    ('정부지원 R&D (일반트랙)', '최대 8억원 · 최대 24개월', 'FACT [S33]'),
    ('정부지원 비율', '총 연구개발비의 75% 이내 · 기관부담 25% 이상 (그중 현금 10% 이상)', 'FACT [S33]'),
    ('운영사 선투자', '수도권 2억원 이상 · 비수도권 1억원 이상 (Seed 라운드에 포함)', 'FACT [S33]'),
    ('창업팀 요건', '대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 지분 30% 이하', 'FACT [S33]'),
    ('고용', '정부지원 5억원당 청년 1명 신규 채용', 'FACT [S33]'),
    ('비R&D 연계', f"창업사업화 · 해외마케팅 각 최대 {v('biz_link') / 1e4:.1f}억원 (선정 뒤 별도 신청, 본 계획 미반영)", 'FACT [S33]'),
    ('접수', '분기별 접수 (운영사 추천)', 'FACT [S52]'),
]
wp_rows = [(a, b, c, d, ' · '.join(e), f, g, h) for a, b, c, d, e, f, g, h in C.WP]
tips_rows = [(r['cat'], r['item'], f"{r['y1']:,.0f}", f"{r['y2']:,.0f}", f"{r['total']:,.0f}", r['kind']) for r in TP['rows']]
tips_rows.append(('**합계**', '', f"{TP['year_total'][0]:,.0f}", f"{TP['year_total'][1]:,.0f}", f"**{TP['total']:,.0f}**", ''))
write('11_TIPS_RnD_Work_Package.md', f"""# 11. TIPS R&D Work Package

{HEADER}
## TIPS 과제 = 기술 검증 (Technology De-risking) · Seed = 사업 검증 + 과제 외 개발

{md_table(['구분', 'TIPS 과제', '민간 Seed'], [
    ('목적', '기술 검증 (Technology De-risking)', '사업 검증 (Commercial Validation) · 과제 외 개발'),
    ('범위', 'Adaptive Robot Hand · Manipulation · Calibration · Safety · Reliability · Integrated Workflow', f"기관부담금 · 과제 외 인건비 {(sum(F['people']) - sum(F['uses'][0]['tips'])) / 1e4:.2f}억원 (참여율 외 R&D · 사업 · 현장 · 경영지원) · Full-scale Mock-up 운영 · Customer Validation · Pilot · WTP · Partner Development · BM Validation"),
    ('결과물', 'Hand v3 · CLEAN Skill Library · Calibration Tool · Interface 표준 · Safety Architecture · 실증 보고서', 'WTP 조사 · 예약금 · 유료 전환 · Partner 조건 · BOM · 설치 · Service 원가'),
    ('판단 Gate', 'M6 Hand Buy/Build · M12 목업 CLEAN · M18 Transfer', 'M18 WTP · M24 유료 전환 · 원가'),
])}

TIPS 편성 = R&D 인력 (참여율분) · 연구재료 · 시험 · 인증 사전시험 · IP · 간접비 / Seed = 기관부담금 · 과제 외 인건비 · 고객 검증 · 실증 운영 · 사업개발 · 운영비.

## TIPS 2026 규정

{md_table(['항목', '내용', 'Tag'], TIPS_RULES)}

## Work Package (WP1~WP6)

{md_table(['WP', '이름', '기간', '목표', '주요 내용', '산출물', 'KPI', '담당 (채용 계획)'], wp_rows)}

KPI 정의 · 목표 근거: [12_Technical_KPI.md](12_Technical_KPI.md). Gate: [14_Roadmap_24M.md](14_Roadmap_24M.md).

## TIPS 과제 편성 (Base, 만원, ASSUMPTION)

{md_table(['비목', '내용', '1차년도', '2차년도', '합계', '구분'], tips_rows, ['l', 'l', 'r', 'r', 'r', 'c'])}

{md_table(['점검', '값', '판단'], [
    ('정부지원 (75%)', f"{TP['gov']:,.0f}", '상한 충족'),
    ('기관부담 (25%)', f"{TP['private']:,.0f}", '현금 + 현물'),
    ('기관부담 현금', f"{TP['private_cash']:,.0f}", f"현금 ≥ 10% 충족 ({TP['private_cash'] / TP['private'] * 100:.0f}% of 기관부담)"),
    ('기관부담 현물', f"{TP['inkind']:,.0f}", 'Founder 인건비 참여분'),
    ('간접비율', pct(TP['indirect_rate'], 1), '협약 기준 확인 필요'),
])}

- 인건비는 R&D 인원 8명 (참여율 40~60%) 현금 + Founder 2인 현물. 연구수당 = 현금 인건비 × 5%.
- 회사 전체 24개월 지출 {eok(F['spend_total'])} 중 TIPS 과제 {TP['total'] / 1e4:.2f}억원, 나머지는 Seed ([15_Funding_Plan.md](15_Funding_Plan.md)).
""")


# ================================================================ 12 technical KPI
kpi_sections = []
for g, lab in (('Manipulation', 'Manipulation'), ('Application', 'Application (설치 · 반복 적용)'), ('Business', 'Business')):
    rows = [(n, d, b, m6, m12, m18, m24, basis, t) for grp, n, d, b, m6, m12, m18, m24, basis, t in C.KPI if grp == g]
    kpi_sections.append(f"## {lab} ({len(rows)})\n\n" + md_table(['KPI', '정의', 'Benchmark (출처)', 'M6', 'M12', 'M18', 'M24', '목표 근거', 'Tag'], rows))
write('12_Technical_KPI.md', f"""# 12. Technical KPI

{HEADER}
목표 설정 기준: 선행 Benchmark · Prototype 결과 · 경제성 가정 → Benchmark 없는 KPI = Baseline 측정 후 다음 Gate에서 설정 · 공개 연구값 = 참고선 (실험 조건 상이).

""" + '\n\n'.join(kpi_sections) + f"""

## KPI ↔ 원가 연결 (Base · 원가 ASSUMPTION, 인시 DERIVED)

{md_table(['연결 지표', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'], [
    ('설치 · Calibration 인시 (Remodeling)', *[f'{x:.1f}' for x in KL['inst_h']]),
    ('설치 · Calibration 인시 (Retrofit)', *[f'{x:.1f}' for x in KL['inst_h_rt']]),
    ('Care 방문 1회 인시', *[f'{x:.1f}' for x in KL['visit_h']]),
    ('Care 원가 (만원/대 · 년)', *[f'{x:.1f}' for x in KL['care_unit']]),
    ('Robot BOM (만원)', *[f'{x:,}' for x in KL['bom']]),
], ['l', 'r', 'r', 'r', 'r', 'r'])}

인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 약 {KL['hour']:.1f}만원 (연 6,600만원 기준). Pad 수명 요구치 {KL['pad_life']:,.0f}회 = 하루 {KL['grasps_day']:.0f}회 파지 × 365 ÷ 4 (분기 교체 가정 충족 조건).

## Adaptive Hand 시험 계획 (Buy vs Build, WP1)

{md_table(['항목', '내용', 'Tag'], C.HAND_TEST)}

자체 Hand 채택 조건 = Coverage +15%p 또는 Tool 교체 50% 감소 (성공률 · 교체 · 원가 중 명확한 우위) · 미달 시 상용 Gripper + 교체형 Pad (Buy) 전환 → Skill · Calibration 집중.
""")


# ================================================================ 13 patent portfolio
ip_rows = [(a, f, i, d, r, p, t) for a, f, i, d, r, p, t in C.IP]
prior = [d for d in SRC if d['id'] in ('S16', 'S43', 'S49', 'S50')]
write('13_Patent_Portfolio.md', f"""# 13. Patent Portfolio (출원 후보)

{HEADER}
## 출원 전략

- 현재 출원 0건 · 선행기술조사 M3 · 청구항 변리사 검토 예정 · 등록 가능성 미정.
- 식기 로봇 · 주방 Rail Arm · 수납장 로봇 · 교체형 Gripper 부품 선행특허 존재 → 넓은 청구 대신 구체 구조 · 방법 청구.
- 방어력 = 특허 + Grasp Data · Skill Library · Calibration 절차 · Interface 표준 · Installed Base Data 축적 (TARGET).

## 출원 후보 12개 묶음 (기술 영역별)

{md_table(['영역', '출원 후보 (Family)', '사업 중요도', '차별성', 'Prior Art Risk (참고)', '우선순위', '시점'], ip_rows)}

## 출원 계획

{C.IP_PLAN}

{md_table(['시점', '내용'], [
    ('M3', '선행기술조사 (KIPRIS · USPTO · EPO · Google Patents) · 예비 FTO'),
    ('M6~M9', '1순위 2건 출원 (Replaceable Food-contact Module · Task Coordinate Calibration) → M12 Gate 확인 항목'),
    ('M12~M18', '2순위 5개 후보 중 3건 출원 (Robot Home · Appliance Interface · Kitchen Object Handling · Kitchen Mapping · Adaptive Finger 중, 실시예 확보 순)'),
    ('M18', 'PCT 1건 (1순위 중 1건)'),
])}

24개월 IP 예산 {v('ip')[0] + v('ip')[1]:,}만원 (선행조사 · 국내 5건 · PCT 1건, ASSUMPTION) — TIPS 연구활동비 편성 대상.

## 참고 선행기술 (청구항 미검토)

{md_table(['ID', '항목', '내용', '출처'], [(d['id'], d['item'], d['value'], d['source']) for d in prior])}

## 우선순위 판단 기준

1. **사업 중요도**: 소모품 매출 · 설치시간 · 반복설치에 직접 연결되는가 (Food-contact Module · Coordinate Calibration · Robot Home).
2. **차별성**: 주방 · 식기 · 가전 기준점이라는 구체 조건에서만 성립하는 구조 · 절차인가.
3. **Prior Art Risk**: 일반 Gripper · Tool Changer · 협동로봇 안전 기술과 겹치는 정도.
4. **시점**: Hand v1 (M4) · 목업 CLEAN (M12) 결과로 실시예가 생긴 뒤 출원.
""")


# ================================================================ 14 roadmap
PERIODS = [
    ('0~6M', 'Kitchen Task 분석 · Robot Architecture · Hand v1 (M4) · Object Grasp Test (30종, 상용 Gripper 비교) · 초기 Calibration',
     '리드 3명 채용 · Time-diary 30세대 · 인터뷰 50명 · 평면 30개 분석 · 견적 20건 · 선행기술조사 (M3)', 'M6'),
    ('7~12M', 'CLEAN Skill · Dishwasher Interaction · Hand v2 (M10) · Safety 기능 · 1:1 Kitchen Mock-up · 목업 CLEAN 전 과정',
     '인증기관 사전상담 (M9) · 1순위 특허 2건 출원 · 리모델링 · 렌탈 Partner 탐색 · 사업개발 합류 (M7)', 'M12'),
    ('13~18M', '다양한 Kitchen 적용 (주방 3종) · Task Transfer Test · Failure Recovery · Hand v3 (M18) · Pilot 착수',
     'WTP 조사 n ≥ 300 · 예약금 Test · 전기 · EMC 사전시험 · BOM 100대/년 견적 · PCT 1건', 'M18'),
    ('19~24M', 'Reliability (연속 운전) · Installation Standard · Real-home Pilot 3세대 · BOM · 설치 · Service 원가 실측',
     'Paid Pilot 전환 · Partner 조건 (리모델링 1 · 렌탈/캐피탈 1) · 출원 누적 5건 · Series A 준비', 'M24'),
]
team_rows = [(t['role'], M['team_kind'][t['kind']], f"M{t['start']}", f"{t['cost'][0]:,.0f}", f"{t['cost'][1]:,.0f}") for t in F['team']]
VC = [('TODAY', 'Concept · Technology Hypothesis · Business Hypothesis (시제품 · 고객 · 매출 없음)'),
      ('Seed + TIPS (24개월)', f"{eok(F['spend_total'])} 지출 · 24개월 차 약 {F['heads_m24']:.0f}명"),
      ('24M TARGET — 기술', 'Working Kitchen Prototype · Adaptive Robot Hand · Manipulation Skill Library · Calibration System · Safety Architecture · Multiple Kitchen Test · Task Transfer Evidence'),
      ('24M TARGET — 경제성', 'Robot BOM (100대/년 견적) · Installation Cost · Service Cost (가정 3세대 실측)'),
      ('24M TARGET — 시장', 'Customer WTP (n ≥ 300) · Pilot · Paid Pilot (≥ 2세대) · Partner Evidence · Patent 출원 5건 + PCT 1건'),
      ('NEXT ROUND', 'Productization · Production · Distribution · Scale (Series A 판단 기준 = 기술 성공 + 유료 전환 + 원가 실측)')]
write('14_Roadmap_24M.md', f"""# 14. 24개월 Roadmap

{HEADER}
## 구간별 실행 (TARGET)

{md_table(['구간', '기술 (TIPS WP)', '사업 검증 (Seed)', 'Gate'], PERIODS)}

## Gate · 중단 기준

{md_table(['Gate', '확인할 Evidence', '통과 기준 (TARGET)', '미달 시 조치'], C.GATES)}

Gate별 판단: 계속 · 범위 축소 · 전환.

## WP 일정

{md_table(['WP', '이름', '기간'], [(a, b, c) for a, b, c, *_ in C.WP])}

## 채용 계획 (ASSUMPTION)

{md_table(['역할', '구분', '시작', 'Y1 인건비 (만원)', 'Y2 인건비 (만원)'], team_rows, ['l', 'l', 'c', 'r', 'r'])}

평균 FTE {F['fte'][0]:.1f} (Y1) → {F['fte'][1]:.1f} (Y2) · 24개월 차 약 {F['heads_m24']:.0f}명. Lean안: Hand 센싱 · Skill/Data · 현장 Technician 제외, 시험 인력 M19로 연기 (24개월 차 약 {F['heads_m24_lean']:.0f}명).

## 24개월 Value Creation

{md_table(['단계', '내용'], VC)}
""")


# ================================================================ 15 funding plan
use_rows = []
for u in F['uses']:
    tv = sum(u['tips'])
    use_rows.append((u['cat'], u['item'], f"{u['y'][0]:,.0f}", f"{u['y'][1]:,.0f}", f"{sum(u['y']):,.0f}", f"{tv:,.0f}" if tv else '-', f"{sum(u['y']) - tv:,.0f}"))
use_rows.append(('**합계**', '', f"{F['spend'][0]:,.0f}", f"{F['spend'][1]:,.0f}", f"**{F['spend_total']:,.0f}**", f"{TP['total']:,.0f}", f"{F['spend_total'] - TP['total']:,.0f}"))
fm_rows = []
for k, lab in [('rev', '매출'), ('gp', '매출총이익'), ('contrib', 'Contribution'), ('opex', 'Opex'), ('op', '영업이익 (근사)'), ('cash', '연간 현금흐름'), ('cum_cash', '누적 현금')]:
    fm_rows.append((lab, *[f"{x / 1e4:.1f}" for x in B[k]]))
fm_rows.append(('설치 세대 (TARGET)', *[f"{x:,.0f}" for x in B['kitchens']]))
fm_rows.append(('평균 인원 (FTE)', *[f"{x:.1f}" for x in v('fte')]))
sc_rows = [(n, *[f"{a / 1e4:.1f} / {b / 1e4:.1f}" for a, b in zip(SC[k]['rev'], SC[k]['op'])]) for k, n in (('C', 'Conservative'), ('B', 'Base'), ('U', 'Upside'))]
write('15_Funding_Plan.md', f"""# 15. Funding Plan

{HEADER}
## 요약

{md_table(['항목', '값', 'Tag'], [
    ('24개월 지출 (Bottom-up)', eok(F['spend_total']), 'DERIVED'),
    ('TIPS 정부지원 (선정 시)', '8.0억원', 'FACT (상한)'),
    ('TIPS 기관부담 (현금 · 현물)', f"{TP['private'] / 1e4:.2f}억원 (현금 {TP['private_cash'] / 1e4:.2f} · 현물 {TP['inkind'] / 1e4:.2f})", 'DERIVED'),
    ('Buffer (Series A 협상 기간)', f"{eok(F['buffer'])} = Y2 월평균 지출 × {F['buffer_months']}개월", 'ASSUMPTION'),
    ('**Seed Base**', f"**{eok(F['seed_base'])}** = 지출 {eok(F['spend_total'])} − TIPS 8억원 + Buffer {eok(F['buffer'])}", 'DERIVED'),
    ('Seed Lean (팀 축소 · 범위 축소)', eok(F['seed_lean']), 'DERIVED'),
    ('**Seed 범위**', f"**{F['seed_range'][0]}~{F['seed_range'][1]}억원**", 'DERIVED'),
    ('TIPS 미선정 시 (Lean 범위)', eok(F['seed_no_tips']), 'DERIVED'),
    ('Runway (Base, TIPS 포함)', f"약 {F['runway_base']:.0f}개월", 'DERIVED'),
    ('운영사 선투자 요건 (수도권)', f"{v('op_invest_min') / 1e4:.0f}억원 이상 → Seed 라운드에 포함", 'FACT'),
])}

투자 조건 · 기업가치: 협의 · 비R&D 연계 (창업사업화 · 해외마케팅 각 최대 1.5억원): 선정 후 별도 신청 (계획 미반영).

## 24개월 사용처 (만원, Base)

{md_table(['구분', '내용', 'Y1', 'Y2', '24개월', 'TIPS 편성', '그 외 (Seed)'], use_rows, ['l', 'l', 'r', 'r', 'r', 'r', 'r'])}

- 인건비: 팀 {len(F['team'])}명 (Founder 2 + 신규 {len(F['team']) - 2}), 연 인건비 = 연봉 × 1.2. Founder 인건비는 TIPS 현물로 편성.
- 예비비 = 인건비 외 지출의 10%. 실증 순비용 = 실증 3세대 하드웨어 · 설치 원가 − 실증 매출 (50% 할인).

## Seed 범위 산식

{md_table(['안', '24개월 지출', 'TIPS 정부지원', 'Buffer (3개월)', 'Seed 필요액', '차이'], [
    ('Base (기술 + 사업 검증)', f"{F['spend_total']:,.0f}", '80,000', f"{F['buffer']:,.0f}", f"**{F['seed_base']:,.0f}**", '-'),
    ('Lean (팀 · 목업 · 실증 축소)', f"{F['lean_total']:,.0f}", '80,000', f"{F['seed_lean'] - F['lean_total'] + 80000:,.0f}", f"**{F['seed_lean']:,.0f}**", 'Hand 센싱 · Skill/Data · Technician 제외, 시험 인력 M19, 비용 축소'),
    ('TIPS 미선정 (Lean 범위)', f"{sum(F['no_tips_spend']):,.0f}", '0', f"{F['seed_no_tips'] - sum(F['no_tips_spend']):,.0f}", f"**{F['seed_no_tips']:,.0f}**", '연구수당 없음 · 일정 연장 또는 비R&D 과제로 보완'),
], ['l', 'r', 'r', 'r', 'r', 'l'])}

## TIPS 과제 편성

{md_table(['비목', '1차년도', '2차년도', '합계', '구분'], [(r['cat'], f"{r['y1']:,.0f}", f"{r['y2']:,.0f}", f"{r['total']:,.0f}", r['kind']) for r in TP['rows']] + [('합계', f"{TP['year_total'][0]:,.0f}", f"{TP['year_total'][1]:,.0f}", f"{TP['total']:,.0f}", '')], ['l', 'r', 'r', 'r', 'c'])}

## 5개년 계획 맥락 (Base, 억원, TARGET / ASSUMPTION)

{md_table(['항목', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'], fm_rows, ['l', 'r', 'r', 'r', 'r', 'r'])}

{md_table(['Scenario (매출 / 영업이익, 억원)', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'], sc_rows, ['l', 'r', 'r', 'r', 'r', 'r'])}

- Y1~Y2 = Seed + TIPS 24개월. Y3~ = Series A 전제. Base 누적 현금 최저 {eok(M['post_seed_burn']['min_cum'], 0)} → Series A 이후에도 추가 자금이 필요한 하드웨어 사업 구조.
- Series A 이후 2년 (Y3~Y4) 현금 소요 약 {eok(M['post_seed_burn']['y3_y4'], 0)} (DERIVED). 손익분기 설치 물량 연 약 {M['breakeven_kitchens']:,.0f}세대 (Y5 단가 · 원가 기준).
- 그래서 24개월 Evidence (WTP · 원가 실측 · 유료 전환)가 Series A 규모와 가능성을 결정.
""")


# ================================================================ 16 questions
q_rows = []
for i, (q, a, ev, wk, where) in enumerate(C.QA, 1):
    spec = ' + '.join(C.QA_SPEC_MERGED.get(i - 1, [q]))
    q_rows.append((f'Q{i}', q, C.QA_INTENT[i - 1], where, spec if (i - 1) in C.QA_SPEC_MERGED else '-'))
write('16_Investor_Questions_20.md', f"""# 16. 투자심사 예상질문 20개

{HEADER_INT}
- Q6 = 상용 Gripper 비교 · 자체 Hand 필요성 병합 (같은 Buy vs Build 판단)

{md_table(['#', '질문', '확인 포인트', '답하는 위치 (본문 쪽 · 부록)', '병합 질문 원문'], q_rows)}

방어논리: [17_Defense_Logic.md](17_Defense_Logic.md) · 내부 검토 자료 I1~I3.
""")


# ================================================================ 17 defense logic
out = []
for i, (q, a, ev, wk, where) in enumerate(C.QA, 1):
    out.append(f"## Q{i}. {q}\n")
    out.append(f"- **방어논리**: {a}")
    out.append(f"- **근거 (Tag)**: {ev}")
    out.append(f"- **약한 부분**: {wk}")
    out.append(f"- **위치**: 본문 · 부록 {where}\n")
write('17_Defense_Logic.md', f"""# 17. 각 질문의 방어논리

{HEADER_INT}
답변 기준: 미검증 항목 = "미검증" 명시 + 확인 Gate · Evidence 제시.

""" + '\n'.join(out))


# ================================================================ 18 evidence gaps
first90 = [r for r in C.EVIDENCE if any(t in r[4] for t in ('즉시', 'M3'))]
write('18_Evidence_Gaps.md', f"""# 18. 현재 부족한 Evidence

{HEADER_INT}
현재 없음: 고객 · 계약 · LOI · 파트너 · 매출 · 시제품 Data.

## Evidence Gap

{md_table(['Evidence', '현재', '필요한 Evidence', '확보 방법', '시점'], C.EVIDENCE)}

## 투자 판단 기준 우선순위

1. **Founder · 핵심 팀** — 다른 모든 판단의 전제 (현재 공백).
2. **기술 Baseline** — 상용 Arm + Gripper로 30종 식기 파지 · 식세기 적재 영상과 성공률 (M3 이내 가능).
3. **고객 행동** — 인터뷰가 아니라 예약금 · 유료 실증 의향서.
4. **설치 경제성** — 서로 다른 주방에서 Calibration · 설치 시간.
5. **Partner 조건** — 리모델링 시공 · 렌탈/캐피탈의 조건부 협력 의사.

## 첫 90일 실행 목록 (즉시 ~ M3)

{md_table(['Evidence', '현재', '필요한 Evidence', '확보 방법', '시점'], first90)}

## Risk Register

{md_table(['구분', 'Risk', '확인 Evidence (시점)', '대응', '중단 · 재편 기준'], C.RISKS)}
""")


# ================================================================ 19 founder inputs
slide17 = ['Why This Problem', 'Relevant Engineering Experience', 'Hardware / Product Development', 'Robot / Mechanical / AI Capability',
           'Construction / Kitchen / Manufacturing Knowledge', 'Customer / Partner Network', 'Full-time Commitment']
form = '\n'.join(f"- **{s}**: [Founder 정보 필요]" for s in slide17)
write('19_Founder_Inputs.md', f"""# 19. Founder 입력 필요정보

{HEADER_INT}
입력 전 Founder 칸 = `[Founder 정보 필요]` (본문 17쪽 · 내부 검토 자료 I4).

## 입력 항목

{md_table(['항목', '필요한 내용'], C.FOUNDER_INPUTS)}

## 본문 17쪽 Founder Slide 항목 (Founder 1 · Founder 2 각각)

{form}

## TIPS 관련 확인 사항

{md_table(['요건', '확인할 것', 'Tag'], [
    ('창업팀 지분', '대표 포함 2인 이상 합산 60% 이상 · 운영사 30% 이하 (주주명부)', 'FACT [S33] · 원문 확인'),
    ('소재지', '수도권 여부 → 운영사 선투자 요건 (수도권 2억원 이상 / 비수도권 1억원 이상)', 'FACT [S33]'),
    ('업력 · 기업 규모', '공고상 창업기업 요건 (업력 · 매출 · 중복지원 제한) 원문 대조', 'TBV'),
    ('청년 채용', '정부지원 5억원당 청년 1명 신규 채용 계획', 'FACT [S33] · 원문 확인'),
    ('IP 권리귀속', '전 직장 · 연구실 직무발명 · 공동연구 권리 · 경업금지', 'TBV'),
])}

## 증빙 자료 (예)

경력증명서 · 학위증명 · 논문 · 특허 · 코드 저장소 · 수상 · 개발 제품 자료 · 주주명부 · 법인등기부등본 · 4대보험 가입자 명부 · 겸직 여부 확인서.

## 입력 양식 (복사해서 사용)

```text
[Founder 1 — 대표]
이름 / 학력 / 경력 (연도 · 회사 · 역할 · 성과):
Why This Problem:
Relevant Engineering Experience:
Hardware / Product Development:
Robot / Mechanical / AI Capability (증빙):
Construction / Kitchen / Manufacturing Knowledge:
Customer / Partner Network (실명 · 관계 수준, 없으면 "없음"):
Full-time Commitment (전업 시점) / 지분 / 베스팅:

[Founder 2 — 기술 총괄]
(같은 항목)

[법인]
설립일 / 소재지 / 자본금 / 기존 투자 · 정부과제 / 운영사 접촉 현황 (없으면 "없음") / 상호 · 상표 검색 결과
```
""")


# ================================================================ 20 investment memo
hw3 = 1 - v('bom')[2] / v('p_robot')
write('20_Investment_Memo.md', f"""# 20. 투자심사 Memo

{HEADER_INT}

## 1. Deal 개요

{md_table(['항목', '내용'], [
    ('회사', 'MH Robotics (Kitchen Manipulation Robotics) · Concept 단계'),
    ('제품', 'Adaptive Hand + Manipulation Skill + Calibration + Environment Interface + Safety를 묶은 주거용 Kitchen Robotics System'),
    ('첫 검증', 'CLEAN (식기 인식 → Pick → 식세기 Loading / Unloading → Storage Return) → ASSIST → COOK (장기)'),
    ('요청', f"Seed {F['seed_range'][0]}~{F['seed_range'][1]}억원 (Bottom-up, Base {eok(F['seed_base'])}) + TIPS R&D 8억원 (별도 재원, 선정 시)"),
    ('사용', f"24개월 {eok(F['spend_total'])}: 인건비 · 연구수당 {sum(sum(u['y']) for u in F['uses'] if u['cat'] in ('인건비', '연구수당')) / 1e4:.1f}억원 중심 · 목업 · Hand · 실증 · WTP · Partner · 인증 사전시험 · IP"),
    ('현재 Evidence', '시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 · Founder 정보 없음'),
])}

## 2. Investment Thesis (성립 조건)

1. 가전 사이 Physical Workflow = 가전사가 기기 안에서 풀기 어려운 문제 · 주방은 동작 · 영역 · 물체가 닫혀 있어 첫 Application으로 검증 가능.
2. 범용 Robot의 병목 = 지능만이 아닌 **설치 · Calibration · 반복 적용** → Hand · Skill · Calibration · 최소 Interface 결합으로 설치시간 · 서비스 원가 절감 가능 (검증 대상).
3. Remodeling · 신축 구매 계기 + Partner 시공 구조 → 현장 인력에 비례하지 않는 설치 확대 가능.
4. Installed Base 위에 Care · 소모품 · Skill · Tool 반복 · 확장 매출 누적.

## 3. 강점

""" + '\n'.join(f"- {x}" for x in C.VERDICT_WHY[1][1]) + """

## 4. 우려

""" + '\n'.join(f"- {x}" for x in C.VERDICT_WHY[0][1]) + f"""
- Hardware 마진이 얇음: Robot ASP {v('p_robot'):,}만원 vs BOM Y3 {v('bom')[2]:,}만원 → {pct(hw3)}. Conservative에서는 1세대 5년 기여이익이 Y3 원가 기준 적자.
- CLEAN만의 가사 대체 가치 (월 약 {VA['value']:.0f}만원) < Rental 월 {v('p_rent')}만원 → 가치 Gap.
- Series A 이후에도 Y3~Y4 약 {eok(M['post_seed_burn']['y3_y4'], 0)} 현금 소요 (Base) → 자본 집약도 높은 하드웨어 사업.
- Rental Partner 단순 회수 약 {PI['payback']:.0f}개월 > 요구 {PI['hurdle']}개월 (가정) → Partner 조건 미확보 시 MH 자산 보유 부담.

## 5. 숫자 점검

{md_table(['점검', '결과', 'Tag'], [
    ('시장', f"Bottom-up SAM 연 {MK['sam']:,.0f}억원 · Y5 계획 {B['rev'][4] / 1e4:.1f}억원 = 대상 세대 {MK['som_share_hh'] * 100:.1f}% (공격적이지 않음, 비율은 전부 가정)", 'DERIVED'),
    ('Unit Economics', f"Remodeling 1세대 5년 기여이익 {man(H3['contrib5'])} (Y3) → {man(H5['contrib5'])} (Y5). 민감도 1 · 2순위 = WTP · BOM", 'DERIVED'),
    ('자금', f"Seed {F['seed_range'][0]}~{F['seed_range'][1]}억원 · Runway 약 {F['runway_base']:.0f}개월 · TIPS 미선정 시 {eok(F['seed_no_tips'])}", 'DERIVED'),
    ('실행', 'WP1~WP6 · Gate 4개 · 중단 기준 명시 (Hand Buy 전환 · Retrofit 보류 · 범위 축소)', 'TARGET'),
])}

## 6. Scorecard (1~5, 5 = 강한 Evidence)

{md_table(['항목', '현재', 'M24 목표', '근거'], C.SCORE, ['l', 'c', 'c', 'l'])}

## 7. 판단: **{C.VERDICT}**

(INVEST · MEET · WATCH · PASS 중)

- **INVEST가 아닌 이유**: 팀 · 기술 측정값 · 고객 행동 증거가 없고, 원가가 모두 가정.
- **WATCH · PASS가 아닌 이유**: 문제 정의 → 기술 접근 → 측정 가능한 Gate → Bottom-up 자금 계획이 일관되고, FACT / ASSUMPTION 구분이 엄격해 실사 비용이 낮음. Founder 정보와 M3 기술 Baseline이 확인되면 빠르게 판단을 갱신할 수 있는 구조.

## 8. 판단을 바꿀 Evidence (최대 5개)

""" + '\n'.join(f"{i}. **{a}** — {b}" for i, (a, b) in enumerate(C.CHANGE_EVIDENCE, 1)) + """

## 9. 첫 미팅 의제 (MEET)

1. Founder 2인의 이력 · 역할 · 지분 · 전업 여부와 이 문제를 택한 이유.
2. 상용 Arm + Gripper 기준선 영상 (식기 파지 · 식세기 적재) 또는 M3까지의 확보 계획.
3. Premium 리모델링 고객 · 시공 Partner 접점 (실명 · 관계 수준, 없으면 없음).
4. 24개월 Gate별 중단 기준을 실제로 지킬 의사와 Lean안 전환 조건.
5. TIPS 운영사 접촉 현황 · 소재지 (선투자 요건) · 창업팀 지분 구조.

## 10. INVEST로 바뀌기 위한 조건 (요약)

팀 적합성 확인 + 기술 Baseline 영상 · 성공률 + 고객 예약금 (10세대 이상) 중 **세 가지가 확인되면** 운영사 투자 · TIPS 추천 검토 단계로 이동 가능.
""")

print('docs:', len(os.listdir(DOCS)))


# ================================================================ MH/README.md
main_rows = [(f"{m['no']:02d}", SPEC35[m['no'] - 1], m['title']) for m in MAIN]
apx_line = ' · '.join(f"{c} {t}" for c, t in [('A', 'TIPS 과제 상세 (KPI · WP · Gate · 과제 편성 · 팀)'), ('B', '제품 · 기술 (Hand 시험 · 평면 5종 · Robot Home · 대표 평면 · Safety · BOM)'),
                                               ('C', '시장 · 경쟁'), ('D', '경제성 · 재무 (가격 · Household · Unit Economics · 5Y FM · 민감도)'),
                                               ('E', 'IP · Risk'), ('F', '출처')])
readme = f"""# MH Robotics — Seed · TIPS IR Package (최종본, 2026.10)

**Kitchen Manipulation Robotics System — Adaptive Robot Hand · Manipulation Skill · Calibration · Environment Integration**

> Concept 단계 (시제품 · 고객 · 계약 · LOI · 파트너 · 매출 · 투자유치 없음). 수치 = FACT / DERIVED / ASSUMPTION / TARGET (+ CONCEPT · TBV · FUTURE). Founder 칸 = `[Founder 정보 필요]`. 평면 = 제공 도면 재작도 (단지명 미표기).

## 산출물

| 파일 | 내용 |
|---|---|
| `MH_Robotics_Seed_TIPS_IR_Final.pptx` | 제출용 IR: 본문 {N_MAIN}장 + 부록 {len(APX) - 1}장 + 목차 (16:9, 발표 요지 Notes 포함) |
| `MH_Robotics_Seed_TIPS_IR_Final_Main.pdf` | 본문 {N_MAIN}장 (발표 · 운영사 송부용) |
| `MH_Robotics_Seed_TIPS_IR_Final.pdf` | 본문 + 부록 전체 |
| `MH_Robotics_IR_Internal_QA.pptx` · `.pdf` | 내부 검토용 {len(INT)}장 (예상질문 · 방어논리 · Evidence · Founder 입력 · 투자심사 Memo · Tag 원칙) — 제출 제외 |
| `MH_Robotics_Financial_Model.xlsx` | 수식 기반 모델: Inputs (Tag · 출처) → 5Y FM 3 Scenario · Household · Unit_Economics · Market · Budget_24M · Sensitivity · Sources |
| `docs/00~20` | 결과물 20종 (01~15 제출 · 공유용 · 16~20 내부 검토용) · [docs/00_README_Index.md](docs/00_README_Index.md) |
| `render3d/` | 3D 콘셉트 렌더 생성기 (three.js + Playwright) · 충돌검사 · 보관/전개 경로 · 평면 JSON · Adaptive Hand 모델 (`web/hand.js`) |
| `assets/renders/` | 덱에 들어간 렌더 PNG + Callout Anchor · 충돌검사 JSON |
| `archive/ARKI_v4/` | 이전 판 (ARKI Robotics v4) 덱 · PDF · 재무모델 · 문서 · 문서 생성기 — 삭제 없이 보관 |

## 본문 구성 ({N_MAIN}장)

{md_table(['쪽', '구성', '화면 제목'], main_rows)}

부록: {apx_line}.

## 핵심 결과 (Base, 전부 DERIVED from ASSUMPTION · 물량은 TARGET)

- 1세대 5년 (Remodeling · 구매): 설치 시점 {man(H3['y0'])} · 5년 매출 {man(H3['rev5'])} · Lifetime Contribution {man(H3['contrib5'])} (Y3 원가) → {man(H5['contrib5'])} (Y5 원가). Conservative는 Y3 원가 기준 적자 → WTP · BOM이 1 · 2순위 변수.
- 가치 Gap: CLEAN만의 가사 대체 가치 월 약 {VA['value']:.0f}만원 < Rental 월 {v('p_rent')}만원 → Premium 고객 · ASSIST 확장 · WTP 검증 (M18).
- 시장 (Bottom-up): SAM 연 {MK['sam']:,.0f}억원 (Remodeling {MK['sam_remodel']:,.0f} · Retrofit {MK['sam_retro']:,.0f} · New-build {MK['sam_new']:,.0f}) · Y5 계획 {B['rev'][4] / 1e4:.1f}억원 = 대상 세대 {MK['som_share_hh'] * 100:.1f}%.
- 5개년: Y5 매출 {B['rev'][4] / 1e4:.1f}억원 · 설치 {B['kitchens'][4]:,.0f}세대 · 영업이익 {B['op'][4] / 1e4:.1f}억원 · 누적 현금 최저 {M['post_seed_burn']['min_cum'] / 1e4:.0f}억원 · 손익분기 연 약 {M['breakeven_kitchens']:,.0f}세대.
- 24개월: 지출 {eok(F['spend_total'])} = TIPS 정부지원 8억원 (선정 시) + Seed {F['seed_range'][0]}~{F['seed_range'][1]}억원 (Lean {eok(F['seed_lean'])} ~ Base {eok(F['seed_base'])}, Buffer 3개월 포함) · TIPS 미선정 시 {eok(F['seed_no_tips'])}. TIPS 과제 {TP['total'] / 1e4:.2f}억원 (정부 8 + 기관부담 {TP['private'] / 1e4:.2f}).
- Series A 이후 Y3~Y4 현금 소요 약 {eok(M['post_seed_burn']['y3_y4'], 0)} · Rental Partner 단순 회수 약 {PI['payback']:.0f}개월 (요구 {PI['hurdle']}개월 가정 → 조건 협의).
- 내부 검토 판단: **{C.VERDICT}** — 판단을 바꿀 Evidence 5개: {' · '.join(a for a, _ in C.CHANGE_EVIDENCE)} ([docs/20](docs/20_Investment_Memo.md)).

## Environment Interface 예 (Remodeling 채널, 3D 모델 기준 CONCEPT)

- 주방 전체 표준화가 아니라 반복 작업점에만 최소 Interface: Robot Home (Dock) · Rail · 식세기 Interface · Storage Dock · Vision Reference. Retrofit은 Compact Mount · Dock, New-build는 설계 단계 반영.
- Remodeling 예 (부록 B3 · B4): 로봇 작업 줄 Robot Home 45 · Drop Zone 70 · 싱크 80 · 서랍 60 · 식세기 60cm. Rail은 상부장 하단 (약 139cm), 바닥 사용 안 함. 조리기구 구역 = 로봇 금지 구역.
- 낮은 작업점: 식세기 하단 랙을 44cm 당겨 위에서 적재 (Gripper 최저 약 37cm), 서랍도 열어서 위에서 넣음.
- 충돌검사: 로봇 링크 = 캡슐, 가구 = 상자. 작업 자세 · 보관 · 전개 경로 · Rail 이동 · 자기충돌 관통 0cm (`assets/renders/*.json`의 `ik`). 실제 기구 검증 전.

## 확보 평면 5종 (Kitchen Variation 근거, 부록 B2)

{md_table(['평면', '구분', '크기 (mm)', '주방 형태', '3D', '기본 배치'], C.PLANS)}

## 다시 만들기

```bash
pip install python-pptx openpyxl pillow lxml pypdf          # LibreOffice: PDF · xlsx 재계산
python3 MH/source/model.py          # 가정 · 계산 · 24개월 예산 · Seed 범위 → model.json
python3 MH/source/xlsx_model.py     # 수식 기반 xlsx
python3 /mnt/skills/public/xlsx/scripts/recalc.py MH/MH_Robotics_Financial_Model.xlsx 120
python3 MH/source/check_xlsx.py     # xlsx 수식값 ↔ model.json 교차검증
cd MH/render3d && npm install && bash render_v2.sh && bash render_plans.sh && bash render_hand.sh && for f in render_fig_*.sh; do bash $f; done && cd ../..   # 3D 렌더 (선택)
python3 MH/source/build.py --pdf    # 제출용 덱 + 본문 PDF + 전체 PDF + 내부 검토용 (fit 검사, --png: 미리보기)
python3 MH/source/gen_docs.py       # docs/*.md + 이 README
```

- 단일 원천: `source/model.py` (입력 · Tag · 출처 · 계산) → `model.json` → 덱 · xlsx · 문서. 정성 표 (KPI · WP · Gate · IP · Risk · Q&A · Evidence · Founder 항목 · 경쟁 · 기준 · 평면)는 `source/content.py`.
- 덱: `source/slides_mh.py` (본문) · `source/slides_mh_apx.py` (부록 · 내부 검토용) · 공용 `kit.py` · `common.py` · `mhkit.py`. 이전 판 코드 = `archive/ARKI_v4/source`.

## 외부 제출 전 입력 · 확인

| 항목 | 위치 |
|---|---|
| Founder 2인 정보 · 증빙 · 지분 · 전업 여부 (Founder 2 확보 여부 포함) | 본문 17쪽 · 내부 I4 · docs/19 |
| TIPS 공고 원문 대조 (정부지원 비율 · 기관부담 현금 · 간접비 · 운영사 선투자 · 창업팀 지분 · 청년 채용) · 접수 일정 | 본문 16 · 18쪽 · 부록 A6 · docs/11 |
| 운영사명 · 투자 조건 (형태 · 기업가치 · 지분) | 본문 18쪽 (협의) |
| 공식 통계 · 회사 발표 원문 대조 (보도 인용분, 조회일 2026-10-07~08) | 부록 C1 · C2 · F1~F4 · docs/07 |
| 가격 · 원가 가정 (ASP · Interface · Rental · Care · BOM) → 견적 · WTP 결과로 교체 | 부록 D1 · B6 · docs/09 · 10 |
| 특허 후보 → 선행기술조사 · 변리사 검토 | 본문 15쪽 · 부록 E1 · docs/13 |
"""
with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(gaejo(readme.strip()) + '\n')
print('wrote MH/README.md')
