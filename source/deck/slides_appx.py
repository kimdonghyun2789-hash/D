from deckkit import *
import json, math
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from paths import RENDERS as A, ORIGINAL as O, MODEL_JSON
M = json.load(open(MODEL_JSON, encoding='utf-8'))
B = M['base']; SEEDP = M['seed']; HIRES = M['hires']

def ahead(s, code, kicker, title, sub=None):
    dot(s, 0.6, 0.495, 0.1, OR)
    text(s, 0.8, 0.42, 9.5, 0.26, f'APPENDIX  ·  {code}  ·  {kicker}', size=10, f='S', color=OR, spc=140, name='Kicker')
    text(s, 0.6, 0.72, 12.13, 0.48, title, size=22, f='K', color=L_TEXT, ls=1.05, name='Title')
    if sub: text(s, 0.6, 1.2, 12.13, 0.3, sub, size=11.5, color=L_TEXT2, name='Subtitle')

def lslide(prs, code):
    s = new_slide(prs, code, bg=L_BG)
    return s

def lcard(s, x, y, w, h, title=None, tcolor=OR):
    c = card(s, x, y, w, h, fill=L_CARD, r=0.08, shadow=True, name='Light card')
    if title: text(s, x + 0.2, y + 0.16, w - 0.35, 0.22, title, size=9, f='S', color=tcolor, spc=100)
    return c

def lnote(s, t, y=6.62):
    text(s, 0.6, y, 12.13, 0.4, t, size=9, color=L_TEXT2, ls=1.15)

# ---------------------------------------------------------------- A1 evidence
def a01(prs):
    s = lslide(prs, 'A1')
    ahead(s, 'A1', '근거 상태', '무엇이 확인되었고, 무엇이 가설인가', 'Evidence Status — 투자자는 미완성보다, 사실과 가설을 구분하는 Founder를 신뢰한다')
    rows = [['구분', '현재 내용', 'IR 표기 원칙'],
            ['FACT (확인됨)', '사업 아이디어 · 기술 구상 · IR 초안(2026.10). 외부 시장 자료(IFR · BCG)는 출처 확인.\n법인 · 창업팀 · 특허 · 시제품 · 고객계약 · 매출 · 보유자금은 확인되지 않음', '회사 실적으로 표현하지 않음\n→ Founding & Seed Proposal'],
            ['PLAN (계획)', 'SoftHand-4 V1 · Machine Tending Skill Pack · Design Partner 3곳 · Paid PoC 5건 · Robot Platform 2종\n고객 인터뷰 30곳 · 24개월 Roadmap · Seed Gate', 'Planned · Target · Seed Milestone'],
            ['ASSUMPTION (가정)', 'Hand 패키지 ₩1,500만(원가 ₩950만→₩750만) · Skill Package ₩300만 · Runtime 연 ₩150만\nPaid PoC ₩5,000만 · Base Case 매출 · 손익 · 성능 목표치', 'Assumption · Management Forecast'],
            ['MISSING EVIDENCE', 'Founder · 핵심인력 이력 · 시제품 / 무편집 시험영상 · 특허 / FTO · 고객 인터뷰 · LOI · Design Partner\nPaid PoC · BOM · 고객 Baseline · 동일조건 비교시험 · 실측 현금계획', '[정보 입력 필요] 표기\n→ 실사 전 확보']]
    table(s, 0.6, 1.75, 12.13, [2.0, 7.2, 2.9], rows, row_h=[0.38, 0.95, 0.85, 0.85, 0.95], size=10, head_size=10, name='Evidence table')
    lnote(s, 'Concept Rendering은 실제 시제품이 아니다 — 실제 Prototype 사진 → 시험 영상 → 고객 현장 → CAD → Concept 순으로 교체한다. 본 Deck의 SoftHand 이미지는 모두 동일한 SoftHand-4 Concept 모델(4지 · 대향 Thumb · Graphite Palm · Orange Pad · White Wrist Module)로 통일했다.', y=6.05)
    footer(s, 'A1', appendix=True, light=True)

# ---------------------------------------------------------------- A2 seed gates
def a02(prs):
    s = lslide(prs, 'A2')
    ahead(s, 'A2', 'Seed Gate', 'Seed Gate: 실패 조건과 의사결정을 먼저 정한다', '투자금은 R&D 소비가 아니라 가설검증 자본이다 — 각 Gate는 이사회 · 투자자와 분기별 KPI 리뷰로 판단')
    rows = [['Gate', '검증하는 가설', '통과 기준 (Target)', '미달 시 결정', '자금 영향'],
            [('M6', {'color': OR, 'f': 'K', 'size': 13}), '기술: 하나의 Hand로 대표 Sequence 수행', '대표 Task 5종 반복 시연 · 목표 토크 · 반복성 Log 공개', 'Hand Architecture 재검토\n(구동 방식 · 골격 · 잠금)', '후속 채용 보류 · Prototype 예산 재배분'],
            [('M12', {'color': OR, 'f': 'K', 'size': 13}), '고객: 전환비용 개선에 돈을 낸다', 'Paid PoC 1건+ · 고객 Baseline 데이터 · 지불의사 확인', 'Beachhead · Task 재정의\n(다른 공정 · 다른 고객군)', 'Milestone Extension 집행 재검토'],
            [('M18', {'color': OR, 'f': 'K', 'size': 13}), '제품: 반복 가능한 제품 · Skill 재사용', 'Design Freeze · First Repeat Order · 재사용률 측정 시작 · Platform B 통합', 'Platform Thesis 재검토\n→ Product + Service 모델 검토', f"Extension ₩{SEEDP['ext6']:.1f}억 집행 여부 결정"],
            [('M24', {'color': OR, 'f': 'K', 'size': 13}), '확장: 반복 발주 · Skill 이식성', 'Repeat Customer 2곳+ · 2 Platform Portability · Gross Margin 검증', 'Series A Scale-up 보류\n축소 운영 · Bridge 검토', 'Series A 규모 · 시점 결정']]
    table(s, 0.6, 1.75, 12.13, [0.8, 2.6, 3.4, 2.9, 2.4], rows, row_h=[0.38, 0.85, 0.85, 0.85, 0.85], size=10, name='Gate table', first_col_bold=True)
    lcard(s, 0.6, 5.72, 12.13, 1.05, 'GATE 운영 원칙')
    text(s, 0.8, 6.18, 11.8, 0.55, ['Gate 통과 조건 미달 시 → 범위 축소 또는 피벗을 결정한 뒤 다음 단계 자금을 집행한다 (18개월 Core Runway + 6개월 Milestone Extension 구조와 연동)',
                                     '모든 시험 결과는 시험 횟수 · 성공 건수 · 최초 시도 / 재시도 분리 · 신뢰구간으로 보고한다 — 데모 영상이 아니라 Log로 판단'], size=10, color=L_TEXT2, ls=1.25)
    footer(s, 'A2', appendix=True, light=True)

# ---------------------------------------------------------------- A3 red-team index
def a03(prs):
    s = lslide(prs, 'A3')
    ahead(s, 'A3', 'VC Red-Team', 'VC 예상 질문 17개와 본문 답변 위치', '실제 투자심의에서 나올 질문에 본문만으로 답할 수 있는지 점검한 결과')
    qa = [('왜 기존 Adaptive Gripper로는 충분하지 않은가?', '형상 Pick은 강하지만 Door · Lever 조작과 토크는 제한 → 결국 설비 개조 · 추가 툴', '08'),
          ('왜 Machine Tending에서 SoftHand가 필요한가?', '한 Cell에 Pick · Door · Lever · Button이 모여 Hand 하나의 가치가 가장 큼', '05·06'),
          ('전용 End-effector가 더 싼 작업은 어떻게 하나?', '고속 단일 SKU · 고토크 체결은 공략하지 않음 — Hand가 개조를 줄이는 작업부터', '05'),
          ('첫 번째 실제 구매자는 누구인가?', '다품종 가공 라인 제조기업 생산기술팀(가설) · 도입은 Robot SI 경유 · 90일 인터뷰', '05·11'),
          ('왜 ₩1,500만 Hand를 사는가?', '비교 대상은 전용 Tooling + 설비 개조 + Engineering × 전환 횟수 · Paid PoC로 검증', '07'),
          ('SI 회사가 되는 것을 어떻게 막는가?', '승인 Task 목록 내 수주 · 공통 Task를 Skill Pack으로 제품화 · 재사용 매출 KPI', '09'),
          ('2 · 3번째 고객에서 무엇이 재사용되나?', 'Hand HW · Control Logic · ToolSkill · Runtime / Calibration Tool → 재사용률 측정', '09'),
          ('동일 Skill이 다른 Robot에서도 동작하나?', '아직 가설 — Robot 독립 Task 정의 + Calibration · 24개월 내 2 Platform 검증', '10'),
          ('Soft 구조가 토크 · 내구성을 버티나?', '하중은 골격이 부담 · 작업 순간 강성 상승 · 교체형 패드 · 30만 cycle · M6 Gate', '04·A7'),
          ('왜 지금 5지 Hand가 아닌가?', '4지가 Machine Tending 최소 구성 · 비용 · 내구성 우선 · 5지는 Series A 이후', '04'),
          ('왜 Kitchen을 주력시장에 두지 않나?', '회수기간이 가동률에 민감 · 위생 · 안전 부담 → 공장이 사업성, 주방은 Demonstrator', '12·A15'),
          ('왜 Robot OEM이 직접 만들지 않나?', '다수 OEM은 Arm · Controller 집중, EOAT는 생태계 의존 · 멀티브랜드 Skill은 독립 Layer', '11·A4'),
          ('OEM Design Win 이전에도 생존 가능한가?', 'Base Case는 OEM · Kitchen 0원 — HW + Skill + Integration으로 Y5 손익분기 근접(가정)', 'A11'),
          ('20억원으로 24개월이 가능한가?', '8명 단계 채용 ₩9.6억 포함 · 18M Core + 6M Extension · 매출 0원이어도 M24', '15·A12'),
          ('24개월 후 어떤 숫자면 Series A인가?', 'Paid PoC 5+ · Repeat 2+ · 완료율 95%+ · 30만 cycle · 2 Platform · 재사용률 ↑', '15'),
          ('Repeat Customer가 나오지 않으면?', 'M24 Gate — Series A Scale-up 보류 · Beachhead 재정의 · 축소 운영', '13·A2'),
          ('왜 이 Founder가 이 사업을 해야 하는가?', '[정보 입력 필요] — Founder 정보 없이는 답할 수 없음 (외부 제출 전 필수)', '14')]
    rows = [['#', '질문', '본문의 답 (요약)', 'Slide']]
    for i, (q, a, sl) in enumerate(qa):
        rows.append([f'{i+1}', q, (a, {'color': YEL if '[정보' in a else L_TEXT2, 'f': 'S' if '[정보' in a else 'R'}), sl])
    table(s, 0.6, 1.62, 12.13, [0.35, 3.9, 6.9, 0.85], rows, row_h=[0.3] + [0.276] * 17, size=8.5, head_size=9, name='Red team table', col_align=['c', 'l', 'l', 'c'])
    footer(s, 'A3', appendix=True, light=True)

# ---------------------------------------------------------------- A4 competition detail
def a04(prs):
    s = lslide(prs, 'A4')
    ahead(s, 'A4', '경쟁사 상세', '경쟁 Category 상세와 OEM 내재화 분석', '위치는 공개 정보 기반 정성 배치 · 독립 비교시험 아님 — Seed 기간 동일조건 비교시험으로 검증')
    rows = [['Category', '대표 사례 (공개 정보)', '강점', 'Machine Tending 관점 한계'],
            ['전통 Gripper · EOAT', '평행 · 진공 · 맞춤 EOAT (예: SCHUNK 등)', '정밀 · 저가 · 고신뢰', '작업마다 교체 · Interface 조작은 설비 개조'],
            ['Adaptive Gripper', 'Robotiq Adaptive Gripper', '다양한 형상 Pick · 통합 용이', 'Door · Lever 조작 · 도구 토크 제한'],
            ['Soft Hand', 'qb SoftHand Industry (5지 · 1모터 · 파워그립 2kg, 제조사 공개)', '형상 적응 · 안전한 접촉', '도구 토크 · 강성 전환 제한'],
            ['Dexterous / Humanoid Hand', 'Shadow · Allegro · Tesollo DG-5F-S · Sharpa Wave · Tesla · Figure 자체', '고자유도 · 복잡 조작', '비용 · 복잡도 · 내구성 → 연구 · 휴머노이드 중심'],
            ['Dedicated Tool System', '전용 체결 툴 · 전용 조리 설비 (예: Moley형 로봇 주방)', '특정 작업 최적', '범용 아님 · 설비 투자 큼'],
            [('Our Target', {'color': OR, 'f': 'K'}), 'SoftHand-4 + Machine Tending Skill Pack', 'Interface 조작 + 재사용 Skill (목표)', ('미검증 — Seed 기간 비교시험 대상', {'color': OR, 'f': 'S'})]]
    table(s, 0.6, 1.72, 8.05, [1.9, 2.9, 1.7, 2.3], rows, row_h=[0.36] + [0.62] * 6, size=9, head_size=9.5, name='Competitor table')
    lcard(s, 8.9, 1.72, 3.83, 4.1, 'OEM이 직접 만든다면?')
    text(s, 9.1, 2.18, 3.5, 3.7, [[('관찰', {'f': 'S', 'color': L_TEXT})], 'Tesla · Figure는 휴머노이드 손을 내재화', '다수 산업용 · 협동로봇 OEM은 EOAT 파트너 생태계에 의존',
                                   'NVIDIA Isaac GR00T 레퍼런스 휴머노이드(2026.6)도 외부 촉각 핸드(Sharpa Wave, 22 DoF) 채택', '',
                                   [('해석', {'f': 'S', 'color': L_TEXT})], 'OEM은 경쟁자이자 채널 — 단일 OEM은 멀티브랜드 Skill을 만들기 어렵다', '',
                                   [('대응', {'f': 'S', 'color': L_TEXT})], 'Robot-agnostic 통합 · 2 Platform 이식성 검증 · OEM 파트너십 우선 (Scale Trigger = Design Win)'], size=9.5, color=L_TEXT2, ls=1.18)
    lnote(s, '출처: 제조사 공개 사양 · 보도자료 (Sources A17: S5 · S15 · S16 · S17). 회사명은 범주 예시이며 성능 우열을 주장하지 않는다.', y=6.15)
    footer(s, 'A4', appendix=True, light=True)

# ---------------------------------------------------------------- A5 physical AI signals
def a05(prs):
    s = lslide(prs, 'A5')
    ahead(s, 'A5', 'Physical AI 시장 신호', 'Physical AI Stack: 보고 판단하는 기술은 빨라졌고, 손이 남았다', '본문 Slide 16의 4단계 요약 근거 — 각 수치는 출처 발표 기준이며 독립 검증 아님')
    rows = [['Layer', '상태', '근거 (출처 · 시점)'],
            ['BRAIN  · AI / VLA', '빠르게 발전', 'Gemini Robotics 1.5 (2025.9) · NVIDIA Isaac GR00T N1.6 (2026.1) · Physical Intelligence 기업가치 $5.6B (2025.11)'],
            ['EYES  · Vision / Edge', '상용 수준', 'NVIDIA Jetson AGX Thor — 2,070 FP4 TFLOPS, 이전 세대 대비 AI 연산 7.5배 (2025.8)'],
            ['BODY  · Arm / Cobot / Humanoid', '대규모 보급', '산업용 로봇 가동 약 508만 대 · 연 60만 대+ 설치 (IFR 2026.9) · Figure 기업가치 $39B (2025.9)'],
            [('HAND  · Manipulation', {'color': OR, 'f': 'K'}), ('여전히 어려운 문제', {'color': OR, 'f': 'S'}), '"The forearm and hand are more difficult than the entire rest of the robot." — Elon Musk, Tesla Q3 2025 Earnings Call (2025.10)\nNVIDIA 레퍼런스 휴머노이드(2026.6) 외부 촉각 핸드 채택 · Figure 03 촉각 손끝(3g 감지, 2025.10)'],
            ['CAPITAL', '자본 유입', '로보틱스 스타트업 투자 2025년 $15B(사상 최대) → 2026년 상반기 $18.8B (Crunchbase News, 2026.6)']]
    table(s, 0.6, 1.72, 12.13, [2.6, 1.6, 7.9], rows, row_h=[0.36, 0.62, 0.55, 0.62, 0.95, 0.55], size=9.5, head_size=9.5, name='Physical AI table')
    lnote(s, '해석: Physical AI의 두뇌 · 눈 · 몸이 상용화되면서, 현실 세계의 사람용 Interface를 다루는 Manipulation Layer가 병목으로 남는다. 다만 이것은 장기 Vision의 근거이며, 회사의 첫 매출 근거는 기존 생산설비의 자동화 전환비용(Slide 02)이다.', y=5.65)
    footer(s, 'A5', appendix=True, light=True)

# ---------------------------------------------------------------- A6 market sizing
def a06(prs):
    s = lslide(prs, 'A6')
    ahead(s, 'A6', '시장 규모', '첫 시장은 설치 기반, 상한은 OEM 출하량', '숫자의 크기보다 Scale Mechanism — OEM 매출을 단순 곱셈으로 계산하지 않는다')
    lcard(s, 0.6, 1.72, 5.0, 4.25, '연간 산업용 로봇 신규 설치 (천 대) · IFR')
    cd = CategoryChartData(); cd.categories = ['2024', '2025', '2026F', '2029F']; cd.add_series('Installations', (542, 603, 655, 806))
    gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, I(0.75), I(2.05), I(4.7), I(3.0), cd)
    ch = gf.chart; ch.has_legend = False; ch.has_title = False
    plot = ch.plots[0]; plot.gap_width = 70; plot.has_data_labels = True
    dl = plot.data_labels; dl.font.size = Pt(10); dl.font.bold = True; dl.font.color.rgb = RGBColor.from_string(L_TEXT); dl.position = XL_LABEL_POSITION.OUTSIDE_END
    ser = plot.series[0]
    for i, pt in enumerate(ser.points):
        pt.format.fill.solid(); pt.format.fill.fore_color.rgb = RGBColor.from_string(OR if i == 1 else ('C9CCD1' if i < 1 else 'E3E1DC'))
    va = ch.value_axis; va.visible = False; va.has_major_gridlines = False
    ca = ch.category_axis; ca.tick_labels.font.size = Pt(10); ca.tick_labels.font.color.rgb = RGBColor.from_string(L_TEXT2); ca.format.line.color.rgb = RGBColor.from_string(L_LINE)
    dl.font.name = 'Noto Sans KR SemiBold'; ca.tick_labels.font.name = 'Noto Sans KR'
    text(s, 0.8, 5.15, 4.6, 0.7, [[('약 508만 대  ', {'f': 'K', 'size': 15, 'color': L_TEXT}), ('가동 중 산업용 로봇 (2025년 말)', {})], '한국: 연 3.0만 대 설치 · 로봇밀도 1,220대 / 직원 1만 명 (세계 1위)'], size=9.5, color=L_TEXT2, ls=1.2)
    rows = [['단계', '정의', '규모 근거', '성격'],
            ['Beachhead', '국내 다품종 Machine Tending\n(Robot SI · 제조기업)', '국내 연 3.0만 대 설치 · 로봇밀도 세계 1위', '구매의향 미검증 → 고객 인터뷰 30곳'],
            ['Expansion', '글로벌 산업용 · 협동로봇 설치 기반', '가동 약 508만 대 · 2025년 60만 대+ (+11%) · 2029F 80.6만 대', 'IFR World Robotics 2026'],
            ['Scale', 'Robot OEM 출하량 · Humanoid / Physical AI', 'OEM Design Win 시 출하량 연동 (Slide 11 공식) · 휴머노이드 전망은 기관별 편차 큼', '매출 수치 계산하지 않음']]
    table(s, 5.85, 1.72, 6.88, [1.15, 2.05, 2.25, 1.43], rows, row_h=[0.36, 0.95, 0.95, 1.05], size=9, head_size=9.5, name='Market table')
    text(s, 5.85, 5.2, 6.88, 0.8, ['삭제한 계산 — 기존 Deck의 OEM 채택률 × 단가 매출표(302억~1,810억)와 초기 기회 ₩75억(100개사 × 5대 × ₩1,500만)', 'EOAT 시장 추정치는 조사기관별 편차가 커 TAM 근거로 사용하지 않음'], size=9, color=L_TEXT2, ls=1.2)
    lnote(s, 'Source: IFR World Robotics 2026 (2026.9) · IFR Robot Density (2026.4) · 휴머노이드 전망 예: Goldman Sachs 2035년 648만 대(2026.8, Investing.com 보도)', y=6.3)
    footer(s, 'A6', appendix=True, light=True)

# ---------------------------------------------------------------- A7 hand engineering
def a07(prs):
    s = lslide(prs, 'A7')
    ahead(s, 'A7', 'Technical Due Diligence', 'Hand Engineering: 구동 · 하중 · 센싱', '구동 방식은 미확정 — 창업 후 3개월 내 비교시험으로 선정 (M6 Gate와 연동)')
    rows = [['기술 요소', '개발 내용', '검증 기준'],
            ['구성 (4지)', '3 Finger + 대향 Thumb — Door · Pick · Lever · Button 수행 최소 구성', '5지 대비 부품 수 · 비용 · 내구성 · 제어 복잡도 (5지는 Series A 이후)'],
            ['구동부', '전동 Tendon을 기준 후보로 소형 유압 · 공압과 비교', '손 무게 · 유지력 · 응답 · 누설 · 소음 · 소비전력 · 정비비'],
            ['가변 순응성', '탄성요소 · 장력 제어 · 필요 시 잠금기구', '접촉 충격 완화와 조작 토크 유지의 균형'],
            ['감각부', '손끝 · 손바닥 접촉센서 · 관절 / 장력 센서 · 손목 6축 F/T', '절삭유 · 분진 · 오염 조건 편차와 재교정'],
            ['접촉부', '교체형 패드 · 외피, 용도별 재질 분리 (제조: 내마모 · 내유 / 주방: 세척 · 내열)', '미끄럼 · 마모 · 세척 · 재질 적합성 시험'],
            ['로봇 장착', '공통 Wrist Module · 플랜지 어댑터 · TCP 교정 · 통신 드라이버', 'Robot Platform 2종 실제 통합 · 이식성 측정']]
    table(s, 0.6, 1.72, 8.0, [1.3, 3.6, 3.1], rows, row_h=[0.36] + [0.58] * 6, size=9, head_size=9.5, name='Engineering table')
    lcard(s, 8.85, 1.72, 3.88, 2.15, 'LOAD DESIGN EXAMPLE · MACHINE TENDING')
    text(s, 9.05, 2.18, 3.55, 1.8, ['소재 1.5kg, 파지점에서 무게중심 0.10m', '→ 정적 모멘트 ≈ 1.5 N·m (가속 · 충격 시 증가)', 'Door 개방력 · Lever 조작 토크는 설비별 Baseline 측정 후 Spec 확정', '손의 파지 하중 ≠ 로봇 팔 가반하중 (손 · 어댑터 · 소재 합산)'], size=9, color=L_TEXT2, ls=1.2)
    lcard(s, 8.85, 4.02, 3.88, 1.95, 'SENSING ROLES')
    text(s, 9.05, 4.48, 3.55, 1.6, ['비전: 형상 · Interface 위치 · 배치 상태', '촉각: 접촉 · 미끄러짐', '손목 F/T: 반력 · 토크', 'VLA · 모방학습은 상위 작업 선택에 활용, 힘 · 속도 · 안전 한계는 독립 제어 계층에서 보장'], size=9, color=L_TEXT2, ls=1.2)
    lnote(s, '공통 제어기 · 통신 · Wrist Module은 유지하고 접촉부만 용도별로 분리한다 — 모든 용도를 하나의 재질 · 손가락 사양으로 충족한다고 가정하지 않는다.', y=6.15)
    footer(s, 'A7', appendix=True, light=True)

# ---------------------------------------------------------------- A8 performance tests
def a08(prs):
    s = lslide(prs, 'A8')
    ahead(s, 'A8', '성능 정의와 시험', '잘 잡는 손이 아니라, 일을 끝내는 손', 'Tasks, Not Just Grasps. — 모든 수치는 Target(제안 목표)이며 실적이 아님 · 파지 성공률은 보조 지표')
    rows = [['지표', '12개월 Target', '24개월 Target', '시험 정의'],
            ['대표 Sequence 완료율 (6단계)', '단계별 반복 시연', '승인 Task ≥ 95%', '최초 시도 / 재시도 / 중단 분리 보고 · 신뢰구간'],
            ['소재 Pick → Loading (등록 소재)', '10종 · 95%+', '20종 · 98%+', '종별 100회, 낙하 없이 Loading 완료'],
            ['Door · Lever · Button 조작', '대표 설비 2종', '설비 4종 · 완료율 95%+', '조작력 · 작업시간 동시 보고'],
            ['핸드 하중', '원통 소재 1kg', '동일 조건 2kg', '자세 · 속도 · 모멘트 한계 명시'],
            ['내구성', '반복 개폐 10만 회', '30만 회 (양산 목표 100만 회)', '하중 · 패드 교체주기 · 힘 저하율 명시'],
            ['Skill 이식성', 'Platform A 기준 Log', 'Platform B 재사용 검증', '추가 Engineering 시간 · 완료율 · 재사용 Module 비중'],
            ['재사용률 (Reusability)', '측정 체계 수립', 'M12부터 측정 · 상승 추세', '신규 고객 적용 시 그대로 쓴 Module 비중'],
            ['사람 개입 · 전환 시간', '공정별 고객 Baseline 확보', 'Baseline 대비 감소 [PoC 측정]', '재료 보충 · 복구 포함 · 임의 목표치 없음'],
            [('R&D 트랙 (Gate 제외)', {'color': L_TEXT2}), 'Screwdriver 저토크 체결 Demo', '유연체 · Kitchen Bench Demo', 'Seed 성공조건이 아닌 기술 트랙']]
    table(s, 0.6, 1.72, 12.13, [2.8, 2.6, 2.9, 3.8], rows, row_h=[0.36] + [0.43] * 9, size=9.5, head_size=9.5, name='Performance table')
    lnote(s, '보고 원칙: 시험 횟수 · 성공 건수 · 신뢰구간 공개, 편집 없는 시험 영상 제공. 기존 "사람 개입 −30%" 같은 감소율 목표는 고객 Baseline 확보 전이므로 삭제하고 PoC 측정 항목으로 전환했다.', y=6.15)
    footer(s, 'A8', appendix=True, light=True)

# ---------------------------------------------------------------- A9 tech demo screwdriver
def a09(prs):
    s = lslide(prs, 'A9')
    ahead(s, 'A9', 'Technology Demonstration', '기술 Demo: Screwdriver는 핵심 상용 Use Case가 아니다', "Tool Use를 보여주는 Demo — 고객 ROI는 Door · Lever · 다품종 Handling에서 먼저 증명한다")
    card(s, 0.6, 1.72, 5.2, 4.3, fill=CARD, r=0.08, name='Dark card')
    picture_fit(s, A + 'screwdriver.png', 0.8, 1.9, 4.8, 3.6, name='Screwdriver demo rendering')
    text(s, 0.8, 5.62, 4.8, 0.26, 'CONCEPT RENDERING · 저토크 체결 Demo', size=8.5, f='S', color=TEXT2, spc=60, align='c')
    items = [('이 Demo가 증명하는 것', ['도구 토크 전달 — Rigid to Work', '대향 Thumb 파지 안정성', '작업 순간 강성 전환 (검증 예정)']),
             ('핵심 Use Case가 아닌 이유', ['Robot Wrist에 전용 전동 Screwdriver를 직접 다는 편이 더 싸고 빠르고 정밀하다', 'Hand를 써서 얻는 설비 · End-effector 절감 효과가 작다']),
             ('언제 의미가 생기나', ['한 Cell에서 체결이 가끔만 필요해 Tool Changer 추가가 과한 경우', '사람용 공구를 그대로 써야 하는 서비스 · 주방 환경 (Tongs 등은 Kitchen Bench Demo)'])]
    y = 1.72
    for t, lines in items:
        lcard(s, 6.05, y, 6.68, 1.35, t)
        text(s, 6.25, y + 0.45, 6.3, 0.85, lines, size=10, color=L_TEXT2, ls=1.2)
        y += 1.47
    footer(s, 'A9', appendix=True, light=True)

# ---------------------------------------------------------------- A10 business model
def a10(prs):
    s = lslide(prs, 'A10')
    ahead(s, 'A10', 'Business Model', '제품회사로 시작해 Platform Economics로 확장한다', 'Hardware First. Skills Next. OEM at Scale. — 모든 가격 · 원가 · 마진은 검증 전 가정')
    rows = [['단계', '매출원', '과금 단위 · 가정 가격', 'GM 가정', '역할'],
            ['초기 (Seed)', 'Paid PoC', '건당 ₩5,000만 (8~12주 · 대여 Hand 포함)', '40%', '지불의사 검증 · Baseline 확보'],
            ['초기', 'Integration Engineering', '프로젝트당 ₩4,000만', '40%', '진입 수단 — 비중 축소 목표'],
            ['초기 ~ 중기', 'SoftHand Hardware', 'Hand 패키지 ₩1,500만 (직판) / ₩1,200만 (SI 파트너 순매출)', '원가 ₩950만 → ₩750만', 'BOM · 공급사 확정 후 재산정 (M18)'],
            ['초기 ~ 중기', 'Task Skill Package', 'Hand당 ₩300만 (파트너 ₩240만) · Hand당 1.0 → 1.6개', '85%', '승인 Task 단위 판매'],
            ['중기', 'Runtime / Support', '설치 Hand당 연 ₩150만', '70%', '설치 기반 반복 매출'],
            [('장기', {'color': OR, 'f': 'S'}), ('OEM License · Embedded Runtime · Royalty', {'color': OR, 'f': 'S'}), '출하량 연동 [OEM 협의 후 검증]', '—', 'Base Case 미반영 (Scale Trigger)']]
    table(s, 0.6, 1.72, 12.13, [1.4, 2.6, 4.0, 1.8, 2.3], rows, row_h=[0.36] + [0.52] * 6, size=9.5, head_size=9.5, name='Business model table')
    lcard(s, 0.6, 5.35, 12.13, 1.2, '기존 Deck 대비 변경')
    text(s, 0.8, 5.81, 11.8, 0.85, ['"Skill 연간 구독 ₩300만 · Software GM 70%" 확정 표현 삭제 → 단계별 매출원과 가정으로 전환',
                                     'Integration 매출을 숨기지 않되 장기 모델이 아닌 진입 · 제품화 수단으로 정의 · Kitchen 셀 판매(₩2억/셀)는 Base Case에서 제외'], size=10, color=L_TEXT2, ls=1.25)
    footer(s, 'A10', appendix=True, light=True)

# ---------------------------------------------------------------- A11 base case
def a11(prs):
    s = lslide(prs, 'A11')
    ahead(s, 'A11', 'Financial Model', 'Base Case 5개년: Story와 같은 사업을 설명하는 숫자', 'Management Forecast · 단위: 억원 · Y1 = 투자 집행 첫해 · Kitchen · OEM 매출 0원 (Upside로 분리)')
    f1 = lambda v: f'{v:,.1f}'
    pct = lambda v: f'{v*100:.0f}%'
    A_ = M['assumptions']
    hd = A_['hand_direct']; hp = A_['hand_partner']
    rows = [['항목', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'],
            ['Paid PoC / Integration (건)'] + [f"{a} / {b}" for a, b in zip(A_['poc_n'], A_['int_n'])],
            ['신규 Hand (대) 직판 / 파트너'] + [f"{a} / {b}" for a, b in zip(hd, hp)],
            ['설치 Hand 누적 (대)'] + [f"{int(v)}" for v in B['installed_end']],
            ['매출 — Paid PoC · Integration'] + [f1(v) for v in B['poc_int']],
            ['매출 — SoftHand Hardware'] + [f1(v) for v in B['hw']],
            ['매출 — ToolSkill Package'] + [f1(v) for v in B['skill']],
            ['매출 — Runtime / Support'] + [f1(v) for v in B['runtime']],
            ['매출 — Partner Sales (HW+Skill)'] + [f1(v) for v in B['partner']],
            [('총매출', {'f': 'K', 'color': L_TEXT})] + [(f1(v), {'f': 'K', 'color': L_TEXT}) for v in B['rev']],
            ['매출총이익 (GM)'] + [f"{f1(g)} ({pct(m)})" for g, m in zip(B['gp'], B['gm'])],
            ['운영비'] + [f1(v) for v in B['opex']],
            [('영업손익', {'f': 'K', 'color': OR})] + [(f1(v), {'f': 'K', 'color': OR}) for v in B['op']],
            ['재사용 매출 비중 (KPI)'] + [pct(v) for v in B['reuse_share']]]
    table(s, 0.6, 1.62, 7.6, [2.6, 1.0, 1.0, 1.0, 1.0, 1.0], rows, row_h=[0.32] + [0.33] * 13, size=9, head_size=9.5, name='Base case table', col_align=['l', 'r', 'r', 'r', 'r', 'r'])
    lcard(s, 8.45, 1.62, 4.28, 2.55, 'SENSITIVITY (Y5)')
    sens = [('판매량 −30% (Y3~Y5)', '매출 31.4억 · 영업손익 −7.1억'), ('Hand 원가 절감 지연 (₩900만 유지)', '영업손익 −3.1억'), ('SI 파트너 채널 1년 지연', '매출 32.3억 · 영업손익 −6.4억'), ('판매량 −50%', '매출 22.4억 · 영업손익 −11.9억')]
    y = 2.08
    for a, b in sens:
        text(s, 8.65, y, 3.95, 0.24, a, size=9, f='S', color=L_TEXT)
        text(s, 8.65, y + 0.22, 3.95, 0.24, b, size=9, color=L_TEXT2)
        y += 0.51
    lcard(s, 8.45, 4.32, 4.28, 2.3, '기존 Deck 대비 · 조달')
    text(s, 8.65, 4.78, 3.95, 1.95, [[('기존: ', {'f': 'S', 'color': L_TEXT}), ('Y5 ₩112억 (Kitchen 셀 ₩50억 = 45%)', {})], [('수정: ', {'f': 'S', 'color': OR}), (f"Y5 ₩{B['rev'][4]:.1f}억 (Kitchen 0 · OEM 0)", {})],
                                     f"Y3~Y5 누적 영업손실 약 ₩{-sum(B['op'][2:]):.0f}억 + 운전자본 → Series A 규모는 M18 KPI로 확정",
                                     'Upside (미반영): Kitchen 파트너 공동 제품화(Hand · Skill · Engineering만 인식) · OEM Design Win'], size=9, color=L_TEXT2, ls=1.22)
    lnote(s, '운영비 Y1 · Y2 = Seed 24개월 집행계획과 동일(A12) · Y3~Y5 = 평균 인원 14 / 19 / 23명 × 1인 연 ₩0.72~0.76억 + 비인건비 ₩4.5~6.2억 · 매출원가 = PoC · Integration 60%, Hand 원가, Skill 15%, Runtime 30%', y=6.68)
    footer(s, 'A11', appendix=True, light=True)

# ---------------------------------------------------------------- A12 use of funds detail
def a12(prs):
    s = lslide(prs, 'A12')
    ahead(s, 'A12', 'Use of Funds', 'Seed ₩20억 집행 계획과 P&L 연결', '18개월 Core Runway + 6개월 Milestone Extension · 정부지원금 · 공동개발비 미반영')
    rows = [['역할', '합류', '24M 인건비']]
    tot = 0
    for role, start, mc in HIRES:
        v = (24 - start + 1) * mc; tot += v
        rows.append([role, f'M{start}', f'₩{v:.2f}억'])
    rows.append([('합계 · 8명', {'f': 'K'}), '', (f'₩{tot:.1f}억', {'f': 'K', 'color': OR})])
    table(s, 0.6, 1.62, 5.6, [3.3, 0.9, 1.4], rows, row_h=[0.32] + [0.36] * 9, size=9, head_size=9.5, name='Hiring table', col_align=['l', 'c', 'r'])
    text(s, 0.6, 5.3, 5.6, 0.55, ['인건비 기준: 창업자 연 ₩5,000만 · 엔지니어 연 ₩7,000만 + 4대보험 · 퇴직충당 15%', '기존 "개발인력 9.0억"은 같은 채용 범위에서 과소 추정 → 9.6억으로 현실화'], size=8.5, color=L_TEXT2, ls=1.2)
    import model as MM
    npm = MM.np_month
    rows2 = [['Use of Funds', 'Y1', 'Y2', '합계', '비중']]
    pers_y1, pers_y2 = SEEDP['pers_y1'], SEEDP['pers_y2']
    rows2.append(['핵심 인력', f'{pers_y1:.1f}', f'{pers_y2:.1f}', f'{pers_y1+pers_y2:.1f}', f'{(pers_y1+pers_y2)/20*100:.0f}%'])
    for k, v in npm.items():
        y1, y2 = sum(v[:12]), sum(v[12:])
        rows2.append([k, f'{y1:.2f}', f'{y2:.2f}', f'{y1+y2:.1f}', f'{(y1+y2)/20*100:.1f}%'])
    cont = SEEDP['uof'][-1][1]
    rows2.append(['예비비 · 운전자본', '—', '—', f'{cont:.1f}', f'{cont/20*100:.1f}%'])
    rows2.append([('P&L 운영비 (예비비 제외)', {'f': 'K'}), (f"{SEEDP['opex_y1']:.1f}", {'f': 'K'}), (f"{SEEDP['opex_y2']:.1f}", {'f': 'K'}), (f"{SEEDP['opex_y1']+SEEDP['opex_y2']:.1f}", {'f': 'K', 'color': OR}), ''])
    table(s, 6.45, 1.62, 6.28, [2.75, 0.8, 0.8, 0.85, 0.75], rows2, row_h=[0.32] + [0.33] * 11, size=9, head_size=9.5, name='UoF table', col_align=['l', 'r', 'r', 'r', 'r'])
    lcard(s, 6.45, 5.45, 6.28, 1.25, 'P&L 연결')
    text(s, 6.65, 5.91, 5.95, 0.75, [f"P&L 운영비 Y1 ₩{SEEDP['opex_y1']:.1f}억 + Y2 ₩{SEEDP['opex_y2']:.1f}억 = Use of Funds − 예비비 · 매출원가는 매출로 충당",
                                     f"Core 18M ₩{SEEDP['core18']:.1f}억 · Extension 6M ₩{SEEDP['ext6']:.1f}억 · 월 Burn M6 ₩0.56억 → M18 ₩0.87억",
                                     f"매출 0원이어도 M24 잔액 ₩{cont:.1f}억 (예비비)"], size=9, color=L_TEXT2, ls=1.2)
    footer(s, 'A12', appendix=True, light=True)

# ---------------------------------------------------------------- A13 data architecture
def a13(prs):
    s = lslide(prs, 'A13')
    ahead(s, 'A13', 'Data Architecture', '데이터는 Productization Loop 위에 쌓이는 복리 자산이다', '현재 보유 데이터 없음 — Data Moat를 앞세우지 않고, 고객 프로젝트가 제품이 되는 구조(Slide 09) 다음에 둔다')
    lcard(s, 0.6, 1.72, 3.7, 3.9, "TODAY'S MOAT · SEED에서 만드는 것")
    text(s, 0.8, 2.18, 3.35, 3.5, [[('Mechanical Architecture', {'f': 'S', 'color': L_TEXT})], 'Soft-Rigid 하이브리드 · 교체형 접촉부 · 강성 전환', '', [('Tool-oriented Control', {'f': 'S', 'color': L_TEXT})], '힘 · 미끄러짐 기반 Interface 조작 제어', '',
                                    [('Task Integration Know-how', {'f': 'S', 'color': L_TEXT})], 'SI 현장 통합 · PoC 운영 경험', '', [('Reusable Skill Library', {'f': 'S', 'color': L_TEXT})], 'Productization Loop의 산출물'], size=9.5, color=L_TEXT2, ls=1.18)
    # flywheel
    cx, cy, R = 6.45, 3.65, 1.45
    nodes = ['더 많은 배치', '더 많은 실제 Task', '실패 · 복구 Data', '더 나은 Skill', '더 높은 완료율']
    pts = [(cx + R * 1.12 * math.cos(-math.pi / 2 + i * 2 * math.pi / 5), cy + R * math.sin(-math.pi / 2 + i * 2 * math.pi / 5)) for i in range(5)]
    nw, nh = 1.55, 0.5
    for i in range(5):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 5]
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        tx = (nw / 2) / abs(ux) if abs(ux) > 1e-6 else 1e9; ty = (nh / 2) / abs(uy) if abs(uy) > 1e-6 else 1e9; d0 = min(tx, ty) + 0.06
        line(s, x1 + ux * d0, y1 + uy * d0, x2 - ux * d0, y2 - uy * d0, color=OR, w=1.25, arrow=True)
    for i, t in enumerate(nodes):
        x, y = pts[i]
        b = box(s, x - nw / 2, y - nh / 2, nw, nh, fill=L_CARD, line=OR if i == 2 else L_LINE, lw=1.0, r=0.1)
        box_text(b, t, size=9.5, f='S', color=OR if i == 2 else L_TEXT)
    text(s, cx - 1.0, cy - 0.2, 2.0, 0.42, ['Manipulation Data', 'Compounding Asset'], size=9, f='S', color=OR, align='c', ls=1.1)
    lcard(s, 8.85, 1.72, 3.88, 1.9, 'SEED DATA PLAN · PLANNED')
    text(s, 9.05, 2.18, 3.55, 1.55, ['도구 · 부품 · 설비 Interface 30종+', '시도 1만 회+ · 시간동기화', '실패 원인 라벨링 · 복구 Log', '물체 · 세션 · 현장 단위 분리 검증'], size=9.5, color=L_TEXT2, ls=1.2)
    lcard(s, 8.85, 3.75, 3.88, 1.87, 'DATA RIGHTS')
    text(s, 9.05, 4.21, 3.55, 1.5, ['고객 데이터의 수집 · 학습 · 재사용 범위를 계약으로 분리 합의', '고객 고유 공정 정보는 고객 자산으로 보호', 'Skill 개선에 쓰는 일반화 데이터만 회사 자산'], size=9.5, color=L_TEXT2, ls=1.2)
    chips = ['OBJECT', 'TOOL / INTERFACE', 'GRIP', 'FORCE', 'POSE', 'MOTION', 'FAILURE', 'RECOVERY']
    x = 0.6; w = (12.13 - 7 * 0.12) / 8
    for i, t in enumerate(chips):
        b = box(s, x, 5.85, w, 0.42, fill=L_CARD, line=OR if i >= 6 else L_LINE, lw=1.0, r=0.06)
        box_text(b, t, size=8.5, f='S', color=OR if i >= 6 else L_TEXT)
        x += w + 0.12
    lnote(s, '성공 영상이 아니라 "어떤 상황에서 실패했고 어떻게 복구했는가"를 축적하는 것이 목표 — Data Flywheel은 Productization Loop와 Skill Portability가 검증된 이후의 보조 해자다.', y=6.42)
    footer(s, 'A13', appendix=True, light=True)

# ---------------------------------------------------------------- A14 kitchen
def a14(prs):
    s = lslide(prs, 'A14')
    ahead(s, 'A14', 'Robot Kitchen', 'Robot Kitchen: Seed 범위 · 경제성 · 안전', 'Future Application — Seed 매출 목표가 아닌 Technology Demonstrator의 설계 조건')
    rows = [['구분', 'Seed (M18~M24)', 'Series A 이후 (Future Vision)'],
            ['형태', 'Single-arm · Bench-scale Demo', 'Ceiling Rail · Dual-arm Full Kitchen'],
            ['대표 작업', 'Handle · Tongs · Pan · Plate', '재료 투입 · 세척 · 가열 · 배식 · 수납'],
            ['Hardware', '기존 Robot Platform 활용 (추가 구매 없음)', 'Robot Arm Loan · Partner Hardware · 공동개발 전제'],
            ['예산', '₩0.3억 (기존 ₩0.5억에서 축소)', '파트너 확보 후 별도 산정'],
            ['전제 조건', '없음', '실제 파트너 · 공동개발 계약 (현재 미확보)']]
    table(s, 0.6, 1.72, 7.0, [1.3, 2.75, 2.95], rows, row_h=[0.36] + [0.5] * 5, size=9.5, head_size=9.5, name='Kitchen scope table')
    picture(s, O + 'hero05_ceiling_dual_arm_kitchen.png', 0.6, 4.75, w=2.75, name='Future vision kitchen rendering')
    text(s, 3.5, 4.8, 4.1, 0.9, ['FUTURE VISION · CONCEPT RENDERING', '천장형 양팔 Full Kitchen은 Series A 이후 비전이며, 실제 파트너 전제가 생긴 뒤 진행한다'], size=8.5, color=L_TEXT2, ls=1.2)
    lcard(s, 7.85, 1.72, 4.88, 2.9, 'CUSTOMER ROI — ILLUSTRATIVE (가정)')
    text(s, 8.05, 2.18, 4.5, 2.5, ['셀 투자 ₩2억 · 인건비 ₩2.5만/h · 연 300일 · 추가 운영비 ₩1,000만/년', [('6h/일 절감  ', {'f': 'S', 'color': L_TEXT}), ('연 순절감 ₩3,500만 → 단순 회수 ≈ 5.7년', {})],
                                    [('10h/일 절감  ', {'f': 'S', 'color': L_TEXT}), ('연 순절감 ₩6,500만 → 단순 회수 ≈ 3.1년', {})], '→ 회수기간이 가동률에 민감 · 초기 매출 엔진으로 두지 않음', '→ 금융 · 세금 · 잔존가치 제외'], size=9.5, color=L_TEXT2, ls=1.25)
    lcard(s, 7.85, 4.75, 4.88, 1.75, 'LOAD · SAFETY')
    text(s, 8.05, 5.21, 4.5, 1.4, ['3kg 냄비, 무게중심 0.20m → 정적 모멘트 ≈ 5.9 N·m → 큰 냄비는 양손 · 거치대 보조', '고온 도구 · 칼 · 튀김: 차폐 · 접근 제한 · 독립 인터록 충족 전 기능 비활성'], size=9, color=L_TEXT2, ls=1.2)
    footer(s, 'A14', appendix=True, light=True)

# ---------------------------------------------------------------- A15 safety & IP
def a15(prs):
    s = lslide(prs, 'A15')
    ahead(s, 'A15', 'Safety · IP', '안전 · 인증 · IP 전략', '인증 · 권리 확보 전에는 적합성 · 독자성 · 세계 최초를 주장하지 않는다')
    lcard(s, 0.6, 1.72, 5.95, 4.3, 'SAFETY · MACHINE TENDING CELL')
    text(s, 0.8, 2.18, 5.6, 4.2, ['Soft Hand를 달아도 Cell 전체가 자동으로 안전해지지 않는다 → 설비 · 공구 · 소재 · 이동 범위를 포함한 통합 위험성 평가',
                                   '적용 검토: ISO 10218-2:2025 (산업용 로봇 응용 · 로봇 Cell 안전)',
                                   'Robot이 설비 Door를 여는 경우에도 설비의 안전 인터록은 우회하지 않는다 — 사람 작업자와 같은 조건으로 운전',
                                   '절삭유 · 분진 환경의 접촉부 재질 · 센서 신뢰성 별도 검증',
                                   '주방 확장 시 식품접촉 · 세척 · 내열 요구는 판매국별로 시험기관과 결정 (IP 등급 ≠ 위생 적합성)'], size=11, color=L_TEXT2, ls=1.4, after=6)
    lcard(s, 6.78, 1.72, 5.95, 4.3, 'IP · TRADE SECRETS (PLANNED)')
    text(s, 6.98, 2.18, 5.6, 4.2, [[('출원 후보 ', {'f': 'S', 'color': L_TEXT})], '대향 Thumb · 관절 순응 / 잠금 구조 · 교체형 손끝 · 밀봉 구조', '사람용 Interface 조작을 위한 Hand-Skill 구조 · Robot 독립 Task Skill 표현 · Calibration 이식 방법', '',
                                    [('영업비밀 후보', {'f': 'S', 'color': L_TEXT})], '데이터 정제 · 장력 보정 · 실패 복구 Parameter', '',
                                    [('원칙', {'f': 'S', 'color': L_TEXT})], '선행기술 조사 · 권리범위 검토(FTO) 후 출원 — 그 전에는 비침해 · 독자성 주장 금지', '오픈소스 모델 · 라이브러리 상업 이용 조건 출시 전 확인',
                                    [('현재 특허 출원 없음 ', {'f': 'S', 'color': OR}), ('· 예산: 제조 · 품질 · 안전 · IP ₩1.1억', {})]], size=10.5, color=L_TEXT2, ls=1.3)
    footer(s, 'A15', appendix=True, light=True)

# ---------------------------------------------------------------- A16 risks
def a16(prs):
    s = lslide(prs, 'A16')
    ahead(s, 'A16', 'Risk', '주요 위험과 대응 · 판정 기준')
    rows = [['주요 위험', '사업 영향', '대응 · 판정'],
            ['순응성과 강성 충돌', 'Lever · Door 조작 시 처짐 · 미끄러짐', '골격 · 잠금 비교시험 · 작업 토크별 출시 제한 · M6 Gate'],
            ['과도한 맞춤 개발 (SI화)', '낮은 마진 · 확장 불가', '승인 Task 목록 · 비표준 요청 별도 견적 · 재사용률 KPI · M18 Gate'],
            ['Skill 이식성 실패', 'Platform Thesis 약화', 'Robot 독립 Task 표현 · Calibration Tool · 2 Platform 검증'],
            ['지불의사 부족', '매출 지연 · Beachhead 오류', 'Paid PoC 선수금 · Baseline 계약 · M12 Gate'],
            ['긴 영업주기 · 후속 조달', '운전자금 부족', '18 + 6 집행 · 예비비 · Series A 조기 착수 (M15~)'],
            ['설비 안전 · 인터록', '도입 지연', '통합 위험성 평가 · 설비 인터록 유지 · ISO 10218-2 검토'],
            ['OEM 내재화', 'OEM 채널 축소', 'Robot-agnostic 통합 · 멀티브랜드 Skill · OEM 파트너십 우선'],
            ['창업팀 구성 지연', '일정 · 실행력 저하', '공동창업자 · 핵심 2인 합류를 Seed 클로징 조건으로 설정'],
            ['접촉부 마모 · 오염', '유지비 증가', '교체형 패드 · 교체주기 명시 · 내구시험 (30만 cycle Target)']]
    table(s, 0.6, 1.45, 12.13, [2.6, 3.0, 6.5], rows, row_h=[0.36] + [0.5] * 9, size=10, head_size=10, name='Risk table')
    footer(s, 'A16', appendix=True, light=True)

# ---------------------------------------------------------------- A17 sources
def a17(prs):
    s = lslide(prs, 'A17')
    ahead(s, 'A17', 'Sources', '출처', '열람 기준 2026-10-06 · 가격 · 원가 · 성능 · 고객수 · 일정 · 매출은 출처 수치가 아닌 본 계획의 가정')
    src = [('S1', "IFR, World Robotics 2026 — 'Five Million Robots now Operate in Factories Globally' (2026-09-24)", 'ifr.org/ifr-press-releases/news/five-million-robots-now-operate-in-factories-globally'),
           ('S2', 'IFR, Robot Density — Republic of Korea 1,220 robots per 10,000 employees (2026-04)', 'ifr.org (press release, 2026-04-08)'),
           ('S3', "BCG, 'How Physical AI Is Reshaping Robotics Today—and What Comes Next' (2026-04-14)", 'bcg.com/publications/2026/how-physical-ai-is-reshaping-robotics-today'),
           ('S4', 'Tesla Q3 2025 Earnings Call Transcript, The Motley Fool (2025-10-22)', 'fool.com/earnings/call-transcripts/2025/10/22/tesla-tsla-q3-2025-earnings-call-transcript/'),
           ('S5', 'NVIDIA, Isaac GR00T Reference Humanoid Robot 발표 (2026-06-01)', 'investor.nvidia.com'),
           ('S6', 'NVIDIA, CES 2026 Physical AI 모델 발표 — GR00T N1.6 (2026-01-05)', 'nvidianews.nvidia.com'),
           ('S7', 'CNBC, NVIDIA Jetson AGX Thor 출시 (2025-08-25)', 'cnbc.com/2025/08/25/nvidias-thor-t5000-robot-brain-chip.html'),
           ('S8', 'Google DeepMind, Gemini Robotics 1.5 (2025-09)', 'deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/'),
           ('S9', 'Figure, Series C — $39B post-money (2025-09) · Introducing Figure 03 (2025-10-09)', 'figure.ai/news'),
           ('S10', 'Bloomberg, Physical Intelligence $5.6B 가치 평가 (2025-11-20)', 'bloomberg.com'),
           ('S11', 'Crunchbase News, Robotics startup funding record (2026-06-22)', 'news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/'),
           ('S12', 'Investing.com, Goldman Sachs 휴머노이드 전망 — 2035년 648만 대 (2026-08-31)', 'investing.com'),
           ('S13', 'qbrobotics, qb SoftHand Industry 제품 사양 (제조사 공개)', 'qbrobotics.com/product/qb-softhand-industry/'),
           ('S14', 'Robotics & Automation News, Tesollo DG-5F-S (2026-03-13)', 'roboticsandautomationnews.com'),
           ('S15', 'Moley Robotics, A-AiR kitchen (공급사 소개)', 'moley.com/a-air-kitchen/'),
           ('S16', 'ISO 10218-2:2025 — Industrial robot applications and robot cells', 'iso.org/standard/73934.html'),
           ('S17', 'Noh et al., YORI — Yummy Operations Robot Initiative, arXiv:2405.11094', 'arxiv.org/abs/2405.11094'),
           ('S18', 'PR Newswire, Chef Robotics $43M Series A (2025-04) · 헤럴드경제 외식업계 인력난 (2025-05-10)', 'prnewswire.com · biz.heraldcorp.com')]
    half = 9
    for col in range(2):
        x = 0.6 + col * 6.18; y = 1.62
        for sid, t, u in src[col * half:(col + 1) * half]:
            text(s, x, y, 5.95, 0.5, [[(f'[{sid}] ', {'f': 'S', 'color': OR}), (t, {'color': L_TEXT})], [(u, {'size': 7.5, 'color': L_MUTED})]], size=8.5, ls=1.1)
            y += 0.55
    footer(s, 'A17', appendix=True, light=True)
