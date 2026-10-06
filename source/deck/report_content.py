# -*- coding: utf-8 -*-
# Revision report content (single source for Markdown + DOCX)
import json
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import MODEL_JSON
M = json.load(open(MODEL_JSON, encoding='utf-8'))
B = M['base']; S = M['seed']
f1 = lambda v: f'{v:.1f}'

TITLE = 'SoftHand IR Deck — 최종 수정사항 및 수정 이유'
SUBTITLE = 'Revision Report · Founding & Seed Investment Proposal · 2026.10'

META = [
    ('대상 원본', 'SoftHand_Founding_Seed_IR_Deck.pptx — 27장 (본문 18 + Appendix 9)'),
    ('최종본', 'SoftHand_Founding_Seed_IR_Deck_Final.pptx — 33장 (본문 16 + Appendix 17)'),
    ('작성 기준일', '2026-10-06'),
    ('작성 원칙', '좋은 디자인 · 핵심 논리 · Appendix는 유지하고, 사업전략과 투자논리를 고도화. 확인되지 않은 고객 · 실적 · 특허 · 성능은 만들지 않고 [정보 입력 필요]로 표시'),
]

SUMMARY = [
    '회사의 출발점을 Physical AI가 아니라 "기존 설비 자동화의 재설계 비용(자동화 전환비용)"으로 재정의했다 — 설비를 Robot에 맞추는 대신, Robot이 기존 설비를 사용하게 한다 (Don\'t Rebuild the Workstation).',
    '첫 상용 Wedge를 "기존 설비를 크게 개조하지 않는 다품종 머신텐딩"으로 좁히고, 제품을 SoftHand-4 + Machine Tending Skill Pack으로 정의했다. 하나의 Hand로 문 열기 → 소재 집기 → 투입 → 버튼·레버 조작 → 완성품 배출 → 문 닫기를 끝내는 1 HAND · 5 TASKS · 0 HAND CHANGES를 핵심 Product Vision으로 만들었다.',
    '"결국 SI 회사 아닌가?"에 본문에서 직접 답하도록 Productization Loop · 재사용률(Reusability Ratio) · Skill Portability(동일 Skill의 2개 Robot 재사용)를 24개월 검증 KPI로 추가했다.',
    f"재무 모델을 Story와 같은 사업으로 다시 계산했다: Kitchen · OEM 매출 0원 Base Case — Y5 매출 ₩{B['rev'][4]:.1f}억, Y5 영업손익 ₩{B['op'][4]:.1f}억(손익분기 근접). OEM은 수백억 단순 계산 대신 Design Win 공식(각 항목 [OEM 협의 후 검증])으로 바꿨다.",
    f"Seed ₩20억을 18개월 Core Runway(₩{S['core18']:.1f}억) + 6개월 Milestone Extension(₩{S['ext6']:.1f}억) + 예비비(₩1.7억)로 재구성하고, 개발인력 9.0억을 8명 단계 채용 기준 ₩9.6억으로 현실화했다. 정부지원금 · 공동개발비는 기본 재원에서 제외했다.",
    '본문을 18장 → 16장으로 압축하고 제목을 한국어 중심 + 짧은 영문 Subcopy로 바꿨으며, 모든 SoftHand 이미지를 하나의 SoftHand-4 Concept 모델로 다시 렌더링해 통일했다.',
]

# The final judgment sentence -> where the deck answers it
JUDGMENT = [
    ('사람을 위해 만들어진 기존 생산설비를 크게 뜯어고치지 않고 Robot이 사용하게 하는 Manipulation 회사', '01 · 02 · 03'),
    ('첫 제품은 SoftHand-4 기반 Machine Tending Package', '01 · 05'),
    ('하나의 Hand로 부품 Handling · Door · Handle · Lever 등 여러 Task 수행, 고객 현장에서 전환비용 절감 검증', '06 · 07'),
    ('각 고객 프로젝트를 Reusable Skill로 제품화, 같은 Skill이 여러 Robot에서 재사용되는지 검증', '09 · 10'),
    ('초기 SI · Paid PoC로 진입, 장기적으로 Robot OEM의 Manipulation Layer로 확장', '11 · 16'),
    ('Seed 20억원으로 24개월 안에 제품 · 고객 · 반복발주 · 경제성 · 재사용성 · Skill Portability 증명', '13 · 15 · 16'),
]

# 14 mandated changes: (title, before, after, why, effect, slides)
CHANGES = [
    ('다수 독립 Use Case → Machine Tending Workflow 집중',
     'Container · Screwdriver · Handle/Lever · Tongs 4개 독립 Task를 나열 (START WITH 3 PAINFUL TASKS). 기술 범용성은 보이지만 "첫 번째로 돈 받고 해결하는 Job"이 흐렸다.',
     '첫 Wedge = 기존 설비를 크게 개조하지 않는 다품종 머신텐딩. 제품 = SoftHand-4 + Machine Tending Skill Pack. 6단계 Workflow(문 열기 → 소재 집기 → 설비 투입 → 버튼·레버 조작 → 완성품 배출 → 문 닫기)를 하나의 Hand로 수행하는 1 HAND · 5 TASKS · 0 HAND CHANGES 장표 신설.',
     '사람용 Interface(문 · 손잡이 · 바이스 레버 · 버튼 · 트레이)가 한 Cell에 모여 있어 Hand 하나의 가치가 가장 크게 드러나고, 전환비용을 고객 Baseline과 숫자로 비교할 수 있으며, SI가 이미 판매하는 Application이라 새 시장을 만들 필요가 없다.',
     '투자자가 "이 회사의 첫 제품과 첫 고객 문제"를 한 문장으로 설명할 수 있다. 기술 데모 회사가 아니라 공정 하나를 끝내는 제품 회사로 읽힌다.',
     '05 · 06'),
    ('Screwdriver Core Use Case → Technology Demo로 이동',
     'Task B · CORE "Low-torque Tool Manipulation(Screwdriver)"가 첫 상용 Use Case로 제시됨.',
     'Appendix A9 "기술 Demo: Screwdriver는 핵심 상용 Use Case가 아니다"로 이동. 이 Demo가 증명하는 것(도구 토크 · 대향 엄지 파지 · 강성 전환)과 핵심이 아닌 이유, 의미가 생기는 조건을 분리. 본문 05에 "Hand가 경제적 가치를 만드는 작업부터 자동화한다 — 고속 단일 SKU · 고토크 체결 · 평판 진공 Handling은 공략하지 않음" 원칙 추가.',
     '"Robot Wrist에 전용 전동 Screwdriver를 다는 편이 더 싸고 정밀하지 않나?"라는 반론이 정당하다. 모든 Tool을 Hand로 대체한다고 주장하면 신뢰를 잃는다.',
     '공략 범위를 스스로 제한하는 Founder로 보여, Q3("전용 End-effector가 더 싼 작업은?")에 즉답할 수 있다.',
     '05 · A9'),
    ('Physical AI 중심 설명 → 기존 설비 Automation 문제 중심으로 시작',
     'Cover "Building the Tool-Use Layer for Physical AI", Slide 04 Physical AI Stack(Gemini · NVIDIA · Tesla · Figure · 투자시장)이 앞부분에 배치.',
     'Cover: "기존 설비를 크게 바꾸지 않고, Robot이 사람용 Interface를 사용할 수 있게 합니다." 02 문제 = 기존 설비 자동화의 재설계 비용(BCG: TCO의 ~75%가 초기 셋업 · 재설계), 03 Insight = 설비를 Robot에 맞추는 대신 Robot이 기존 설비를 사용. Physical AI는 16 Closing의 4단계(BRAIN · EYES · BODY · HAND)로만 요약하고 사례는 A5로 이동.',
     'Physical AI는 장기 Vision이지 첫 매출 근거가 아니다. 미래의 큰 이야기가 첫 제품보다 앞서 보이는 문제를 해소.',
     '투자자는 "지금 누가 왜 돈을 내는가"를 먼저 이해하고, Vision은 마지막에 확장성으로 받아들인다.',
     '01 · 02 · 03 · 16 · A5'),
    ('Robot Hand 판매 → Automation Flexibility 판매',
     'SAME HAND. NEW SKILL. / Hand 패키지 ₩1,500만 중심의 하드웨어 판매 서술.',
     '07 "고객은 Hand가 아니라 Automation Flexibility에 돈을 낸다". 고객가치 3가지(기존 설비 개조 최소화 · 반복 엔지니어링 감소 · 다음 작업에서 재사용)로 단순화하고 모두 "가능성"으로 표기. SoftHand-4는 그것을 가능하게 하는 하드웨어 Interface로 정의(03).',
     '고객의 비교 대상은 다른 Hand 가격이 아니라 "전용 툴링 + 설비 개조 + 엔지니어링 × 연간 전환 횟수"이다.',
     'Q5("왜 ₩1,500만 Hand를 사는가")에 가격이 아닌 경제성 구조로 답한다. 동시에 숫자는 PoC에서 검증한다고 밝혀 과장 리스크를 줄인다.',
     '03 · 07'),
    ('Engineering 제거 표현 → Engineering 감소 가능성 검증',
     'WITH US 행에 Gripper · Finger · Jig · Line Downtime 칸을 "제거"로 표시, BCG "≤50% 절감 잠재력"을 우리 효과처럼 배치.',
     '기존: 새 작업 → 새 Gripper → 새 Finger → 새 Jig → 엔지니어링 → 티칭 → 검증. 우리: 새 작업 → 같은 Hand → 기존 Skill 재사용 또는 새 Skill 구성 → Calibration → 검증. "엔지니어링과 검증은 사라지지 않는다 — 얼마나 줄어드는지 측정한다" 명시. KPI 5개(엔지니어링 시간 · 전용 툴링 비용 · 통합 리드타임 · 사람 개입 · 전환 시간)를 ↓ ?로 표시하고 "PoC에서 고객 Baseline 대비 측정"을 Seed의 사업 실험으로 정의. 50% · 70% · −30% 같은 확정 감소율은 모두 삭제(A8 포함).',
     '실제 자동화에서도 엔지니어링과 검증은 남는다. 검증 전 숫자를 확정하면 실사에서 가장 먼저 무너진다.',
     '모르는 숫자를 모른다고 말하고, 그것을 측정하는 것이 투자금의 용도라고 설명해 "가설검증 자본" 논리가 선다.',
     '07 · A8'),
    ('Data Flywheel 중심 → Productization Loop + Reusability Ratio 강화',
     'Slide 10 EVERY DEPLOYMENT IMPROVES THE PLATFORM — 데이터 Flywheel이 Moat의 중심.',
     '09 "고객 프로젝트를 반복 가능한 Skill로 만든다": 고객 프로젝트 → 공통 Task 추출 → 재사용 Skill → 검증된 Skill Pack → 다음 고객 Loop, Design Partner 3곳(Target · 미확보), 재사용률(Reusability Ratio: 신규 고객 적용 시 그대로 쓴 하드웨어 · 제어 로직 · ToolSkill · 소프트웨어 모듈 비중) — M12부터 측정, M24 상승 추세 확인(임의 목표치 없음). "2번째 고객부터 재사용 / 고객마다 새로 구성" 구분, Base Case 매출 구성 변화(재사용 매출 비중 0% → 86%) 표시. Data Flywheel은 A13으로 이동해 보조 해자로 배치.',
     '현재 보유 데이터가 없는 단계에서 Data Moat를 앞세우면 설득력이 약하다. 투자자의 핵심 의문은 "고객별 개발이 쌓여 SI가 되는 것 아닌가"이다.',
     'Q6 · Q7(SI화 방지, 2·3번째 고객의 재사용 범위)에 본문만으로 답한다. 재사용률이 Custom SI 회사와 Scalable Product 회사를 구분하는 지표가 된다.',
     '09 · A13'),
    ('ToolSkill Vision → Skill Portability를 24개월 검증 KPI로 추가',
     'Robot-agnostic · model-agnostic 주장은 있었으나 검증 방법이 없었다.',
     '10 "하나의 Skill이 여러 Robot에서 동작해야 Platform이다 / One Skill. Multiple Robots.": Handle Opening Skill(파지 전략 · 힘 프로파일 · 동작 순서) → Calibration(어댑터 · TCP · 카메라 · 작업공간) → Robot Platform B에서 같은 Task. Seed 목표 = 동일 Task Skill을 최소 2개 Robot Platform에서 재사용 검증(기술 KPI이자 사업모델 KPI). "브랜드가 바뀔 때마다 처음부터 다시 티칭해야 한다면 Platform이 아니라 SI에 가깝다"를 스스로 인정하는 가설로 명시.',
     'Platform 주장은 이식성이 증명될 때만 성립한다.',
     'Q8에 정직하게 답하고, 실패 시 어떻게 판단할지(M18 Gate)까지 연결돼 신뢰도가 높아진다.',
     '10 · 13 · A2'),
    ('Software Subscription 중심 → Hardware + Integration + Skill에서 OEM Runtime으로 단계화',
     'Skill 연간 라이선스 ₩300만 · GM 70%, Software 반복매출을 확정된 모델처럼 제시.',
     '11 · A10: 초기(Seed) = SoftHand 하드웨어 + 유료 PoC + 통합 엔지니어링 + Task Skill 패키지 / 중기 = 재사용 Skill 패키지 + Runtime · 유지보수 / 장기 = OEM 라이선스 + 내장 Runtime + 출하량 연동 로열티. 메시지: "초기에는 제품회사처럼 돈을 벌고, 장기에는 Platform Economics로 확장한다 / Hardware First. Skills Next. OEM at Scale." Integration 매출은 숨기지 않되 진입 · 제품화 수단으로 정의.',
     'Pre-seed 단계에서 구독 · 고마진 SW 모델을 확정하면 근거가 없다.',
     '초기 매출의 현실(하드웨어 · 통합)을 인정하면서도 장기 경제성의 경로를 보여줘 Q13(OEM 이전 생존)과 연결된다.',
     '11 · A10 · A11'),
    ('OEM 매출 단순 계산 → OEM Design Win Scale Mechanism 중심으로 수정',
     '글로벌 신규 설치 603,307대 × OEM 채택률(0.5~2%) × Hand 단가 = 302억~1,810억 표, "₩100억 Base Case → ₩1,000억+ 구조".',
     '계산표 삭제. 11에 "OEM Design Win = Scale Trigger"(고객 한 곳씩 영업 → OEM 출하량에 실려 판매)와 공식 [대상 Robot 출하량] × [옵션 채택률] × [대당 Hand · Runtime 매출] = [OEM 매출], 각 항목 [OEM 협의 후 검증]만 표시. "OEM이 직접 만들면?"에 대한 답(경쟁자이자 채널)을 본문에 추가.',
     '현 단계에서 수백억 · 수천억 계산은 지나치게 단순하고 공격적으로 보인다. 투자자에게 필요한 것은 숫자의 크기가 아니라 Scale Mechanism이다.',
     'Venture Scale 가능성은 유지하면서 신뢰도 손상을 피한다. Q12에 본문에서 답한다.',
     '11 · A4 · A6'),
    ('Kitchen 매출 비중 → Base Case에서 제외, Future Upside로 분리',
     'Base Case Y5 매출 112억 중 Kitchen 셀 50억(45%) — "Kitchen은 첫 매출 시장이 아니다"라는 본문과 충돌.',
     f"Base Case를 새로 계산: 유료 PoC · 통합 / SoftHand 하드웨어 / ToolSkill 패키지 / Runtime · 유지보수 / Partner Sales(SI 파트너 경유)만 포함. Kitchen · OEM 매출 0원. Y1~Y5 매출 {f1(B['rev'][0])} · {f1(B['rev'][1])} · {f1(B['rev'][2])} · {f1(B['rev'][3])} · {f1(B['rev'][4])}억, 영업손익 Y5 {f1(B['op'][4])}억(손익분기 근접). Kitchen 파트너 공동 제품화와 OEM Design Win은 Upside(미반영)로 분리.",
     'Story와 Financial Model이 같은 사업을 설명해야 한다. 112억을 억지로 유지하는 것보다 일관성이 중요하다.',
     '숫자는 작아졌지만, 투자자가 모델을 실사할 때 이야기와 숫자가 서로를 반박하지 않는다.',
     '11 · 12 · A11'),
    ('Full Dual-arm Kitchen → Seed 단계 Demo 범위 현실화',
     'Seed ₩0.5억으로 천장 레일 · 양팔 · SoftHand 2개 · Vision · 주방 통합 Showcase를 암시.',
     'Seed 범위 = 단일 팔 · 벤치 스케일 Demo(손잡이 · 집게 · 팬 · 접시), 이미 구매하는 Robot Platform 활용, ₩0.3억. 천장형 양팔 Full Kitchen은 Series A 이후 Future Vision이며 Robot Arm Loan · Partner Hardware · 공동개발 같은 실제 전제가 생긴 뒤 진행(현재 미확보). 로드맵에서 Kitchen은 핵심 Milestone이 아닌 보조 Demo.',
     '0.5억으로 양팔 Full Kitchen은 과도하고, 없는 파트너를 전제로 할 수 없다.',
     '"공장이 사업성을, 주방이 기술의 확장성을 증명한다"는 역할 정의가 예산과 일치해 신뢰도가 높아진다.',
     '12 · 13 · A14'),
    ('영어 중심 Headline → 한국어 중심 + 짧은 영문 Subcopy',
     'EVERY NEW TASK STILL NEEDS A NEW HAND. 등 대문자 영어 제목과 영어 라벨이 대부분.',
     '모든 본문 제목을 한국어로 바꾸고 영어는 짧은 Subcopy(예: Don\'t Rebuild the Workstation. / Soft to Grasp. Rigid to Work. / One Skill. Multiple Robots.)로만 사용. 흐름 박스 · 칩 · 로드맵 항목 · KPI도 한국어화. 슬로건(ONE HAND. MANY TOOLS.) · 제품명 · 업계 표준 용어(Robot · Hand · Skill · OEM · SI · PoC)는 유지.',
     '한국 VC · 전략적 투자사 · 액셀러레이터가 한국어만 읽어도 이해해야 한다.',
     '읽는 피로가 줄고 메시지가 바로 들어온다. 본문 텍스트의 한국어 비중은 약 70%(모든 영어 토큰 포함) / 약 77%(Robot · Hand · Skill 등 핵심 용어 제외).',
     '전 장'),
    ('Founder Placeholder → Founder-Market Fit 중심 구조',
     '사진 · 이름 · 이력 Placeholder와 7개 직무 칸 나열.',
     '14 "왜 이 팀이 이 문제를 해결할 수 있는가": ① 왜 이 Founder가 이 문제를 발견했는가 ② 왜 이 Founder와 팀이 이 제품을 만들 수 있는가 ③ 왜 이 팀이 첫 고객을 확보할 수 있는가, 3개 질문 구조로 재설계. 사업과 직접 연결되는 경험 범주(Robot · Automation · Manufacturing · AI · Mechanical · Field Integration · Customer Network)와 Commitment 9항목(Full-time · 자기자본 · 공동창업자 · Prototype · 연구실적 · 특허 · 고객 네트워크 · 첫 Design Partner 후보 · 직장 정리 계획) 체크리스트. 실제 Founder 정보는 제공되지 않아 [정보 입력 필요]로 남김 — 임의로 만들지 않음.',
     'Pre-seed 투자에서 가장 중요한 것은 Founder-Market Fit이다. 이력 나열이 아니라 세 질문에 답해야 한다.',
     '정보만 채우면 투자 판단용 장표가 된다. 현재 상태로는 외부 제출 불가(장표에 "외부 제출 전 필수" 표기).',
     '14 · A3'),
    ('24개월 개발 Roadmap → 기술 · 고객 · 제품화 · 확장성 Risk Reduction Roadmap',
     'DOES IT WORK? / WILL CUSTOMERS PAY? / CAN IT BECOME A PRODUCT? / CAN IT SCALE? (영어) + Gate 한 줄.',
     '13: M0~M6 기술이 되는가? → M6~M12 고객이 돈을 낼 이유가 있는가? → M12~M18 반복 가능한 제품이 되는가? → M18~M24 확장 가능한가?로 재작성하고 요청 항목(첫 유료 PoC · Baseline · 엔지니어링 시간 · 툴링 비용 · 리드타임 · ToolSkill V1 · 설계 동결 · BOM · 공급사 · 내구성 · 제조원가 · 첫 반복 발주 · 재사용 Skill 패키지 · 재사용률 · Platform B · 유료 PoC 5건+ · 반복 고객 2곳+ · Skill 이식성 · 매출총이익률 · Series A 준비) 반영. 하단에 Seed Gate(M6 토크 · 반복성 → Hand 구조 재검토 / M12 지불의사 → 첫 시장 · Task 재정의 / M18 재사용률 → Platform 가설 재검토 / M24 반복 발주 → Series A 확장 보류), A2에 상세 Gate 표.',
     '좋은 Founder는 무조건 성공한다고 주장하지 않는다. 실패 조건과 의사결정을 먼저 정해야 투자금이 R&D 소비가 아니라 가설검증 자본이 된다.',
     'Q15 · Q16(Series A 조건, 반복 고객이 없을 때의 결정)에 본문으로 답한다.',
     '13 · A2'),
]

EXTRA = [
    ('문제 장표 문장 수정', 'EVERY NEW TASK STILL NEEDS A NEW HAND. — Adaptive Gripper를 고려하면 지나치게 단정적.',
     '"기존 설비 자동화에는 여전히 너무 많은 재설계가 필요하다 / Too Much Re-engineering for Every New Task." 구조: 기존 설비(사람 손에 맞춰 설계) → Robot 도입 → 작업마다 추가되는 재설계(전용 Finger · Jig/Fixture · 설비 개조 · 엔지니어링 · 티칭 · 검증) → 높은 자동화 전환비용.', '02'),
    ('설치 기반(Why Now)을 Insight 장표에 통합', '독립 장표 ROBOTS ARE ALREADY HERE (IFR 차트).',
     '권장 Storyline의 SLIDE 03 메시지 "이미 설치된 Robot이 우리의 첫 시장이다"를 03 Insight 장표 하단 띠(508만 대 · 60만+ 대 · 한국 3.0만 대 · 로봇밀도 세계 1위)로 통합하고, IFR 차트는 A6으로 이동. 이유: 20번 요구사항(경쟁 장표를 본문에 한국어 4 Category로 유지)과 25번 요구사항(본문 14~16장)을 동시에 만족시키기 위함 — 권장 Storyline 16장 + 경쟁 1장 = 17장이 되므로 가장 데이터성 장표를 통합.', '03 · A6'),
    ('경쟁 장표 단순화', 'THE GAP IS TOOL USE, NOT FINGER COUNT — 2x2 Matrix에 회사명 다수.',
     '08 "경쟁은 손가락 수가 아니라, 설비변경 없이 끝낸 작업 수다": 전통 Gripper · Adaptive Gripper · Dexterous Hand · Our Target 4 Category만 크게. 각 강점 · 한계와 설비변경 필요 / 현장 적용성 표시(Our Target은 TARGET). Seed 기간 증명 항목 4개. 회사명 · Spec · OEM 내재화 분석은 A4로 이동.', '08 · A4'),
    ('Core Technology 한국어화와 4지 근거', 'SOFT TO GRASP. RIGID TO WORK. — 영어 우선.',
     '"잡을 때는 부드럽게, 일할 때는 단단하게 / Soft to Grasp. Rigid to Work." 왼쪽 잡기(형상 차이 · 위치 오차 · 미끄러짐), 오른쪽 일하기(토크 전달 · 반력 지지 · 모멘트 저항), 중앙 Cutaway. 5요소는 한글 이름을 먼저(부드러운 접촉면 · 하중 지지 골격 · 대향 엄지 · 가변 강성/잠금 · 힘/미끄러짐 제어). 4지(손가락 3 + 대향 엄지)가 머신텐딩 최소 구성이며 5지는 Series A 이후임을 명시(Q10).', '04 · A7'),
    ('Design Partner 전략 추가', '없음 — 제품을 만든 뒤 고객을 찾는 구조로 읽힐 위험.',
     'Design Partner 3곳(A Machine Tending · B High-mix Handling · C Inspection/Loading, 대상: Robot SI · 제조기업 · Automation Integrator) — 모두 TARGET · 미확보로 표기. 목표 Flow: Design Partner 3곳 → 유료 PoC 5건 → 반복 고객 2곳.', '09 · 11'),
    ('Seed Use of Funds 재검토', '핵심 개발인력 9.0억(45%) 외 6개 항목, 24개월 집행 근거 없음.',
     f"8명 단계 채용(창업자 2 + 핵심 6, 157 인월) 기준 인력 ₩{S['pers_total']:.1f}억으로 현실화. 18개월 Core Runway ₩{S['core18']:.1f}억 + 6개월 Milestone Extension ₩{S['ext6']:.1f}억(M18 Gate 통과 시 집행) + 예비비 ₩1.7억. 매출 0원이어도 M24까지 집행 가능. 정부지원금 · 공동개발비는 확정 전이므로 제외(추가 재원으로만 표기). P&L 운영비 Y1 ₩{S['opex_y1']:.1f}억 + Y2 ₩{S['opex_y2']:.1f}억 = Use of Funds − 예비비로 연결(A12).", '15 · A12'),
    ('VC Red-Team 질문 Index', '없음.', 'A3에 17개 질문 · 본문 답 요약 · 답변 위치 Slide를 정리 — 발표자 예상 Q&A로 사용.', 'A3'),
    ('Concept Rendering 통일', '표지 · 제품 · Cutaway · Task · 주방 · Closing 이미지의 손 형태가 서로 달라 다른 Concept처럼 보임.',
     '하나의 SoftHand-4 3D Concept 모델로 전 이미지를 다시 렌더링(아래 8장 기준). 문제 장표의 전용 그리퍼 이미지(손이 아님)와 A14의 천장형 주방 Future Vision 이미지만 원본 유지. 모든 이미지에 CONCEPT RENDERING 표시 유지.', '전 장'),
]

SLIDEMAP = [
    ('01', 'Cover: ONE HAND. MANY TOOLS. / Tool-Use Layer for Physical AI', '01', '문제 중심 문장 · 첫 제품 · 첫 시장으로 재작성, 표지 렌더(문 손잡이를 잡은 SoftHand-4) 신규'),
    ('02', 'EVERY NEW TASK STILL NEEDS A NEW HAND.', '02', '재설계 비용 구조로 재작성 (BCG ~75% 유지)'),
    ('03', 'ROBOTS ARE ALREADY HERE. (설치 기반)', '03 하단 · A6', 'Insight 장표 하단 띠로 통합, 차트는 A6'),
    ('04', 'THE MISSING LAYER IS MANIPULATION. (Physical AI)', '16 · A5', '4단계 요약만 Closing에, 사례는 A5'),
    ('05', 'SOFT TO GRASP. RIGID TO WORK.', '04', '한국어 제목 · 한글 우선 5요소 · 4지 근거'),
    ('06', 'WE MEASURE TASKS, NOT GRASPS.', '07 · A8', 'KPI는 07, 시험 정의는 A8("잘 잡는 손이 아니라, 일을 끝내는 손")'),
    ('07', 'START WITH 3 PAINFUL TASKS. (4 Task)', '05 · 06 · A9', 'Machine Tending Workflow로 통합, Screwdriver는 A9'),
    ('08', 'SAME HAND. NEW SKILL.', '07', '"제거" 삭제, ↓ ? KPI, 사업 실험'),
    ('09', 'HARDWARE GETS US DEPLOYED. SKILLS LET US SCALE.', '11 · A10', '매출 단계화'),
    ('10', 'EVERY DEPLOYMENT IMPROVES THE PLATFORM. (Data)', '09 · A13', 'Productization Loop 우선, Data는 보조'),
    ('11', 'THE GAP IS TOOL USE, NOT FINGER COUNT.', '08 · A4', '4 Category 단순화'),
    ('12', 'OUR HARDEST TESTBED IS A KITCHEN.', '12 · A14', 'Factory vs Kitchen 역할 정의, Seed 범위 축소'),
    ('13', 'INTEGRATOR-LED. OEM-SCALED.', '11', 'SI → Partner → OEM Design Win'),
    ('14', 'FROM BASE CASE TO OEM SCALE.', 'A11 · 11', 'OEM 계산표 삭제, Base Case 재작성'),
    ('15', '24 MONTHS TO COMMERCIAL PROOF.', '13 · A2', '한국어 질문형 + Seed Gate'),
    ('16', 'WHY THIS TEAM.', '14', 'FMF 3질문 구조'),
    ('17', '₩2B TO BUILD THE COMPANY.', '15 · A12', '18 + 6 구조, 인력비 재산정'),
    ('18', 'Closing: THE TOOL-USE LAYER FOR PHYSICAL AI', '16', 'Story 회수 + PROVE 4개(REUSABILITY 추가)'),
    ('A1~A9', 'Evidence · Engineering · Targets · Market · Base Case · Kitchen · Safety/IP · Risk · Sources', 'A1 · A7 · A8 · A6 · A11 · A14 · A15 · A16 · A17', '모두 유지 · 갱신'),
    ('신규', '—', 'A2 · A3 · A4 · A5 · A9 · A10 · A12 · A13', 'Seed Gate · VC 질문 Index · 경쟁 상세 · Physical AI 신호 · 기술 Demo · Business Model · Use of Funds · Data Architecture'),
]

UOF_COMPARE = [
    ('핵심 인력', '9.0 (45%)', f"{S['pers_total']:.1f} (48%)", '8명 단계 채용 · 시장 연봉 · 4대보험 · 퇴직충당 반영'),
    ('Prototype · 내구시험', '3.0 (15%)', '2.7 (13.5%)', 'Alpha 3 · Beta 6 · PoC 대여 Hand · 시험 Rig'),
    ('Robot 2종 · 시험 Cell', '(미분리)', '1.3 (6.5%)', 'Robot Platform A · B + 머신텐딩 시험 Cell을 명시'),
    ('고객 PoC · 현장통합', '2.5 (12.5%)', '1.2 (6.0%)', '비청구 비용만 — 유료 PoC의 직접비는 매출원가로 매출에서 충당'),
    ('AI · Data · SW', '1.5 (7.5%)', '0.6 (3.0%)', '인건비는 인력에 포함, 여기는 Compute · License · Data 인프라'),
    ('제조 · 품질 · 안전 · IP', '1.5 (7.5%)', '1.1 (5.5%)', 'FTO · 출원 · DFM · 공급사 · 안전 사전평가'),
    ('Kitchen', '0.5 (2.5%)', '0.3 (1.5%)', '벤치 스케일 Demo · 기존 Robot 활용'),
    ('운영', '2.0 (10%, Contingency 포함)', '1.5 (7.5%)', '임차 · 법무 · 회계 · 보험 · 출장'),
    ('예비비 · 운전자본', '(운영에 포함)', '1.7 (8.4%)', '매출 0원이어도 M24까지 집행 가능한 완충'),
]

REDTEAM = [
    ('왜 기존 Adaptive Gripper로는 충분하지 않은가?', '08', '보완', 'Adaptive Gripper 한계를 "손잡이를 감싸 당기기 · 레버 토크 제한 → 결국 설비 개조"로 구체화'),
    ('왜 Machine Tending에서 SoftHand가 필요한가?', '05 · 06', '충분', '한 Cell의 사람용 Interface 집중 · 6단계 Workflow'),
    ('전용 End-effector가 더 싼 작업은 어떻게 하는가?', '05', '충분', '공략 / 비공략 원칙, Screwdriver를 A9로'),
    ('첫 번째 실제 구매자는 누구인가?', '05 · 11', '충분(가설)', '다품종 가공 라인 제조기업 생산기술팀 · Robot SI 경유 — 인터뷰로 검증 필요'),
    ('고객이 왜 ₩1,500만 Hand를 구매하는가?', '07', '충분', '비교 대상 = 전용 툴링 + 설비 개조 + 엔지니어링 × 전환 횟수 → 유료 PoC'),
    ('SI 회사가 되는 것을 어떻게 막는가?', '09', '충분', 'Loop · 운영 규칙 · 재사용률 · 매출 구성 변화'),
    ('2 · 3번째 고객부터 무엇이 재사용되는가?', '09', '보완', '"2번째 고객부터 재사용 / 고객마다 새로 구성" 줄 추가'),
    ('동일 Skill이 다른 Robot에서도 동작하는가?', '10', '충분(가설)', '2 Platform 검증 KPI, 실패 시 M18 Gate'),
    ('Soft 구조가 토크 · 내구성을 버티는가?', '04 · 08 · 13', '충분', '하중 지지 골격 · 강성 전환 · 30만 회 목표 · M6 Gate'),
    ('왜 지금 5지 Hand까지 만들지 않는가?', '04', '충분', '4지 최소 구성 · 5지는 Series A 이후'),
    ('왜 Kitchen을 주력시장에 두지 않는가?', '12', '보완', '"회수기간이 가동률에 민감 · 위생 · 안전 부담" 이유를 본문에 추가'),
    ('왜 Robot OEM이 직접 만들지 않는가?', '11', '보완', '"OEM이 직접 만들면?" 띠를 본문에 추가(경쟁자이자 채널)'),
    ('OEM Design Win 이전에도 생존할 수 있는가?', '11 · A11', '보완', f"Stage 2에 Base Case Y5 ₩{B['rev'][4]:.1f}억(OEM · Kitchen 0원) 추가"),
    ('20억원으로 24개월이 실제로 가능한가?', '15', '충분', '18 + 6 구조 · 인력비 재산정 · 매출 0원 시나리오'),
    ('24개월 후 어떤 숫자면 Series A를 받는가?', '15', '충분', 'Series A Readiness 8개 지표'),
    ('Repeat Customer가 나오지 않으면 어떤 결정을 하는가?', '13', '충분', 'M24 Gate: Series A 확장 보류 · A2 상세'),
    ('왜 이 Founder가 이 사업을 해야 하는가?', '14', '정보 필요', 'Founder 실제 정보 없이는 답할 수 없음 — 외부 제출 전 필수 입력'),
]

TODO = [
    ('회사명', '전 장 Footer · 표지', '[회사명 입력 필요]'),
    ('Founder 정보', '14', '이름 · 사진 · 산업 경력 · Prototype · 연구실적 · 특허 · FMF 3질문 답 · Commitment 9항목'),
    ('대표자 연락처', '16', '[대표자명 · 이메일 · 연락처 입력 필요]'),
    ('투자 조건', '15', 'Valuation · 지분율 [투자 조건 입력 필요]'),
    ('Design Partner 후보', '09 · 11', '현재 TARGET · 미확보 — 확보 시 실명 · 상태(MOU/LOI) 표기'),
    ('첫 구매자 가설 검증', '05', '고객 인터뷰 30곳 결과 · 지불의사'),
    ('가격 · 원가 가정', 'A10 · A11', 'Hand ₩1,500만 · 원가 · Skill ₩300만 · PoC ₩5,000만 — 견적 · BOM 확보 후 갱신'),
    ('실물 이미지', '전 장', 'Prototype 사진 → 시험 영상 → 고객 현장 → CAD 순으로 Concept Rendering 교체'),
]

DESIGN_LANG = [
    ('구성', '4지 = 손가락 3 + 대향 엄지(Opposable Thumb) — 5지는 Series A 이후 별도 제품'),
    ('Palm', 'Graphite Palm Frame + White Back Shell · 손바닥 상단 Graphite Band · 4개 고정 Screw'),
    ('Finger Segment', '각 손가락 3마디 · White 몸체 + 손바닥면 Orange Pad · 손끝은 Orange Cap'),
    ('Orange Contact Pad 위치', '각 마디 손바닥면 · 손끝 · 손바닥 하단 대형 Pad · 엄지 측면 Pad (주황은 접촉부에만 사용)'),
    ('Joint', 'Graphite Barrel + 양측 Bracket · 동일 반경'),
    ('Wrist Module', 'White 원통 + 상하 Graphite Ring + Graphite Flange · 단일 Connector'),
    ('Cable Management', '외부 노출 케이블 없음 · Wrist Module 내부 배선 · Connector 1개'),
    ('색 · 재질', 'White(무광 Satin) + Graphite(저광택) + Orange(무광 실리콘 Pad)'),
    ('비례', '손바닥 폭 약 9cm 기준의 실제 제작 가능한 산업용 제품 비례'),
]
