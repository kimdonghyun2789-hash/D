# 02. Appendix — Slide 문구 · Visual · Chart · Speaker Note (A0~A23)

> ARKI Robotics (가칭) · Seed Investment Proposal · Draft v1 · 2026-10-07 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·Partner 없음.

---

## A0. Appendix 목차

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX
Appendix 목차
본문 수치의 근거 · 계산 · 검증 계획. 재무 수식 모델: ARKI_Robotics_Financial_Model.xlsx
A1  Number Tag 원칙과 구분표
A2  Housing Data
A3  Kitchen Remodeling 시장 · 가격 Reference
A4  Robot Component Benchmark · BOM
A5  Kitchen Geometry · 평면 30개 분석 계획
A6  Robot Reach · 단면 치수
A7  Safety Architecture · Certification
A8  설치 Architecture (구조체 정착 · 전원 · 통신)
A9  Competition 상세
A10  IP / Patent Portfolio
A11  Household Unit Economics 상세
A12  Rental Model
A13  Care · Consumables Model
A14  5-Year Financial Model (3 Scenario)
A15  Sensitivity Analysis
A16  Seed Use of Funds 검증
A17  Customer Validation · 기술 KPI
A18  What Must Be True
A19  Risk Register
A20~21  VC Red-Team Q&A
A22  Investment Scorecard · 판단
A23  Sources
```

**Visual 구성**: 2열 목차

**Chart / Diagram**: 없음

**Speaker Note**: 부록은 본문 숫자의 근거와 계산 과정을 담습니다. 각 부록 번호는 본문에서 참조한 위치입니다.

## A1. Number Tag 원칙과 구분표

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A1
Number Tag 원칙과 구분표
모든 주요 숫자와 미검증 내용을 7개 Tag로 구분. 전체 입력 목록·Tag·출처: xlsx Inputs 시트, docs/04_Number_Tag_Register.md
Tag | 정의 | 대표 예시 | 적용 범위
FACT | 공식 통계 또는 공개자료로 확인된 값 | 총주택 2,018만호 · 아파트 65.8% · 2025 준공 34.2만호 · 1X NEO $20,000 | 12개 입력
DERIVED | FACT를 ARKI가 계산한 값 | 아파트 약 1,328만호 · 교체 세대 교차검증 29.0만·30.3만 · 가치 Anchor 월 18만원 | 계산 시트 전부
ASSUMPTION | 현재 사업가설 (검증 전) | Robot ASP 1,490만원 · BOM · Rental 월 33만원 · Premium 10% · 적용률 60% | 73개 입력
TARGET | Seed 기간 또는 이후 목표 | 평면 30개 · Template 3~5 · Standard Module 65% · 설치 1일 · Paid Pilot | 4개 입력 + KPI
CONCEPT | 실물 없는 설계 개념 | Concept Layout A~D · 단면 · Robot Module 구성 | 도면·Diagram
TBV | 검증 방법이 정해진 미확인 사실 | 식세기 보급률 · 벽식 단지 평면 반복성 · Founder 정보 | 본문 각주
FUTURE | 현재 존재하지 않는 제품 | V2 ASSIST · V3 COOK · End-effector Tool 확장 | Roadmap
금지: 가상 고객 · 가상 계약 · 가상 LOI · 가상 Partner · 가상 매출 · 근거 없는 점유율 · "최초" · Patent 등록 확정 표현
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 본 자료의 모든 숫자는 일곱 가지 Tag 중 하나를 갖습니다. 사실과 가설이 섞이지 않도록 입력 단계부터 Tag를 붙였고, 엑셀 모델의 Inputs 시트에서 전체 목록을 확인할 수 있습니다.

## A2. Housing Data

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A2
Housing Data
공식 통계는 검색 시점(2026-10-07) 보도 인용 → 외부 제출 전 원문 (국가데이터처·국토부 보도자료) 대조 필요
항목 | 값 | Tag | 출처 / 산식
총주택 (2025.11.1) | 2,018.1만호 | FACT | 국가데이터처 2025 인구주택총조사 (2026.7.28)
아파트 비중 / 아파트 수 | 65.8% / 약 1,328만호 | FACT | 비중 FACT, 호수는 2,018.1만 × 65.8% (DERIVED)
준공 20년 이상 / 30년 이상 주택 비중 | 56.0% / 30.6% | FACT | 2025 인구주택총조사
아파트 수 · 20년 이상 아파트 (2023) | 1,263만호 · 639만호 (50.7%) | FACT | 2023 주택총조사 인용 보도
주택 준공 (2025) | 34만2,399호 (−17.8%) | FACT | 국토부 2025.12 주택통계
주택 인허가 · 착공 · 공동주택 분양 (2025) | 37만9,834 · 27만2,685 · 19만8,373호 | FACT | 국토부 2025.12 주택통계
아파트 인허가 (2025) | 34만6,773가구 | FACT | 국토부 주택통계 인용 보도
아파트 입주 2025 / 2026 예정 | 23만6,263 / 18만3,124가구 | FACT | 부동산114 REPS
주택 매매거래 (2025) | 72.6만호 (10년 평균 88.5만) | FACT | KB주택시장리뷰 (부동산원 자료)
연간 Kitchen 교체 세대 교차검증 ① | 29.0만 | DERIVED | 20년+ 아파트 639만 ÷ 교체주기 22년 (ASSUMPTION)
연간 Kitchen 교체 세대 교차검증 ② | 30.3만 | DERIVED | 매매 72.6만 × 아파트 70% × 교체율 40% + 비거래 10만 (ASSUMPTION)
연간 Kitchen 교체 세대 (설정값) | 30만 세대/년 | ASSUMPTION | ①·② 교차검증 범위 → Seed 기간 Partner 판매 Data로 보정
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 주택 통계는 국가데이터처 2025 인구주택총조사와 국토부 2025년 12월 주택통계를 기준으로 했습니다. 주방 교체 세대 수는 공식 통계가 없어 두 가지 방법으로 교차 추정하고 가정값으로 표시했습니다.

## A3. Kitchen Remodeling 시장 · 가격 Reference

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A3
Kitchen Remodeling 시장 · 가격 Reference
Kitchen 단독 Remodeling 가격의 공식 통계 부재 → 가격가설은 ASSUMPTION, Seed 첫 90일 견적 수집으로 대체
항목 | 값 | Tag | 비고
국내 리모델링 시장 (건축물 전체, 비주거 포함) | 2025년 37조원 → 2030년 44조원 (전망) | FACT | 한국건설산업연구원 전망치 · 주택 Kitchen 단독 규모 아님
한샘 리하우스 부문 매출 | 2025 1Q 1,147억원 (−4.3%) | FACT | 분기 실적 보도
프리미엄 Kitchen 시장 구성 | 약 90%가 수입 · 고가 맞춤 | FACT | 한샘 발표 인용 보도 (2025.7)
키친바흐 · 밀레 연계 부엌 매출 | +17% (2025.6 기준) · +173% (2024 대비) | FACT | 회사 발표 인용 보도 — 빌트인 가전 통합 수요 신호
30평대 전체 리모델링 (스타일패키지) | 평당 100만원대 → 약 3,000만원 | FACT | 2019 보도 · 가격 시점 오래됨
신축 유상옵션 비용 / 분양가 | 평균 9.7% (분양가상한제 7개 단지) | FACT | 보도 · 옵션 선택 문화 근거
식기세척기 보급률 | 10%대 초반 (2019~2020 업계 추정) | TBV | 최신 공식 통계 확인 안 됨 → 소비자 조사로 확인
Kitchen 단독 교체 가격대: 일반 | 600~1,500만원 | ASSUMPTION | 공식 자료 없음 → 90일 내 견적 20건 수집 (TBV)
Kitchen 단독 교체 가격대: Premium | 2,000~4,000만원 (빌트인 가전 포함 시 상향) | ASSUMPTION | Beachhead 정의 기준 · 견적으로 검증
Robot-ready 증분가 / Kitchen 공사비 | 450만원 / Premium 2,000~4,000만원 → 11~23% | DERIVED | 증분 부담률 = WTP 조사 핵심 문항
Premium Kitchen + 빌트인 가전 통합 수요는 공개 실적으로 확인 (FACT). 단, Robot Integration Premium 지불 여부는 별개 → WTP 조사 필요
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: Kitchen 단독 리모델링 가격은 공식 통계가 없습니다. 그래서 일반과 Premium 가격대는 가정으로 표시했고, 첫 90일 안에 한샘, 리바트, 지역 업체 견적 20건을 모아 대체합니다. 빌트인 가전과 주방가구를 통합하려는 수요는 한샘 실적에서 확인됩니다.

## A4. Robot Component Benchmark · BOM

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A4
Robot Component Benchmark · BOM
Benchmark = 공개 판매가 (FACT, 환율 1,400원/USD ASSUMPTION). BOM = ASSUMPTION, 재무모델 Base BOM과 합계 일치 (model.py assert).
Benchmark (FACT) | USD | 만원 | 비고
UR3e (3kg) | $23k~33k | 3,220~4,620 | 유통가
Doosan E0509 (5kg) | 약 $22k | 3,080 | Aggregator
UFACTORY xArm 6 (5kg, 700mm) | $8,399 | 1,176 | RobotShop
FAIRINO FR5 (5kg, 922mm) | $6,999 | 980 | 판매가
UFACTORY Lite 6 (0.6kg) | $4,482 (Kit) | 627 | 가반 부족
Robotiq 2F-85 / OnRobot RG2 | $4,999 / 약 $3,200 | 700 / 448 | 판매가
Robotiq Fingertip | $175~195 | 24~27 | Consumable 참고
Orbbec Gemini 335 / RealSense D405 | $384~400 / $514 | 54 / 72 | 판매가
Piab Food-grade Cup | £7~20 | 1~4 | FDA 21 CFR 177.2600
BOM (ASSUMPTION, 만원/대) | Pilot | Y3 | Y5
6축 Arm (가반 3~5kg, Controller 포함) | 950 | 600 | 450
Linear Rail · Carriage · Servo (2.4~3.6m) | 180 | 150 | 120
End-effector Set (Gripper + Suction + Tool Changer) | 120 | 90 | 70
Vision (Depth Camera 2대 + Mount) | 110 | 80 | 60
Compute (Edge GPU) | 100 | 80 | 70
Safety (Zone Sensor·Safety Controller) | 70 | 60 | 50
Garage Door · Harness · Enclosure | 70 | 50 | 45
조립·시험 (Pilot은 Opex 인건비 처리) | 0 | 40 | 35
합계 (재무모델 BOM) | 1,600 | 1,150 | 900
BOM 하락 경로 = 수량 + Arm OEM Partner (국산·중국산 Cobot) + 전용 경량 Arm (Series A 이후). Y5 Arm 450만원은 공격적 가정 → Sensitivity 2순위 변수 (A15)
```

**Visual 구성**: 좌측 공개가 Benchmark 표 (USD→원화 환산), 우측 BOM Pilot/Y3/Y5 표 (ASSUMPTION, 합계는 재무모델과 일치).

**Chart / Diagram**: 표 2개

**Speaker Note**: Robot BOM은 공개가 부품을 기준으로 추정했습니다. Pilot 단계는 1,600만원, Series A 이후 1,150만원, Y5에 900만원으로 내려간다고 가정했습니다. 가장 큰 항목은 Arm이며, Y5 450만원은 OEM Partner나 전용 Arm 개발이 필요한 공격적 가정입니다.

## A5. Kitchen Geometry · 평면 30개 분석 계획

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A5
Kitchen Geometry · 평면 30개 분석 계획
표본 = TARGET. 자료: 입주자모집공고 평면 (공개) + 리모델링 상담 고객 동의 실측. 특정 단지 도면은 공개 자료 범위에서만 사용.
구분 | 59㎡ | 74㎡ | 84㎡ | 101㎡+ | 계
구축 2Bay | 3 | 1 | 2 | — | 6
구축 3Bay | 2 | 2 | 3 | 1 | 8
구축 4Bay | — | — | 1 | — | 1
신축 3Bay | 2 | 2 | 3 | 1 | 8
신축 4Bay | 1 | 1 | 3 | 2 | 7
합계 | 8 | 6 | 12 | 4 | 30
[TARGET]
· 84㎡ 비중 확대: 국민평형 · Mock-up 기준
· 구축은 1990~2000년대 준공 판상형 중심 (교체 수요)
· 신축은 4Bay · 대면형 · Island 포함
분석 항목 | 내용
Kitchen Geometry | 일자 / 11자 / ㄱ자 / ㄷ자 / Island · 대면형
설비 위치 | Sink · 식세기 · IH · 냉장고 · 키큰장 · 상부장
치수 | Run 길이 · Aisle Width · 상부장 하단 높이 · 천장고
구조 제약 | 벽체 구조 (RC 벽식 / 조적 / 경량) · 배관 Shaft · 창호
Robot | Home 후보 · Reach Coverage (Sink·식세기·수납) · 동선 간섭
산출 | Layout Family 3~5 · Template A/B/C · Template별 Coverage % · Site Adjustment 항목
성공 기준 (TARGET): 상위 3개 Template이 표본의 70% 이상 Cover · Template당 Site Adjustment 항목 5개 이하  |  실패 시: Architecture 수 확대 또는 Beachhead 평형 축소
```

**Visual 구성**: 좌측 표본 설계 Matrix (신축/구축 × Bay × 평형). 우측 분석 항목과 산출물, 자료 확보 방법.

**Chart / Diagram**: Matrix 표

**Speaker Note**: 평면 분석은 Seed 첫 3개월의 핵심 과업입니다. 신축 15개, 구축 15개를 평형과 Bay 구성별로 골고루 뽑고, 공개 분양 평면과 동의를 받은 실측을 함께 씁니다. 결과물은 Layout Family, Template, Coverage 비율입니다.

## A6. Robot Reach · 단면 치수

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A6
Robot Reach · 단면 치수
CONCEPT 단면. 치수는 국내 Kitchen 통상 치수 기반 개념값 → 평면 30개 실측으로 검증 (TBV).
[CONCEPT]
항목 | 값 | Tag
작업대 높이 | 850mm (통상) | TBV
상부장 하단 / 상단 | 1,450 / 2,250mm | TBV
천장고 (구축) | 약 2,300~2,400mm | TBV
통로 (11자형 Aisle) | 900~1,200mm | TBV
Arm Reach (5kg급) | 700mm (xArm 6) · 922mm (FR5) | FACT
가반하중 요구 (EE 포함) | 1.5kg 이상 (접시·국그릇) | ASSUMPTION
식세기 Rack 높이 (상향 배치) | 약 450~1,050mm | ASSUMPTION
Sink 바닥 깊이 | 상판 −200~250mm | TBV
Robot 통로 위 운반 | 금지 (사람 존재 시) | ASSUMPTION
바닥형 식세기 하단 Rack (약 150~300mm)은 역설치 Arm Reach 밖 → 식세기 상향 배치 또는 Z축 Lift 필요
```

**Visual 구성**: 좌측 Kitchen 단면 CONCEPT (Counter 850 · 상부장 1,450~2,250 · Rail · 역설치 Arm Reach R700 · Human Zone). 우측 핵심 치수 표 (FACT/ASSUMPTION/TBV).

**Chart / Diagram**: 단면 Diagram + 치수표

**Speaker Note**: 상부장 하단 Rail에 매단 Arm의 Reach를 700mm로 가정하면 작업대 상판과 Sink 바닥까지는 닿지만, 바닥 근처 식세기 하단 Rack까지는 어렵습니다. 그래서 식세기를 키큰장 안에 허리 높이로 올리는 것이 핵심 설계 규칙입니다. 치수는 업계 통상값이며 실측으로 검증합니다.

## A7. Safety Architecture · Certification

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A7
Safety Architecture · Certification
원칙: 사람 위 운반 금지 · Zone 진입 시 정지 · 저속 · 저가반 · 고장 시 일반 Kitchen. 인증 경로는 전문기관 사전상담으로 확정 (TBV).
기능 | Concept 설계
Zone 분리 | Robot / Human / No-go Zone 고정 · Rail 이동범위 기계적 Stopper
Zone 감시 | ToF·Radar Zone Sensor → Human 진입 시 Safety-rated Monitored Stop
속도·힘 제한 | Human 근접 시 저속 · PFL (Power & Force Limiting)
Payload 제한 | V1 운반 1.5kg 이하 · 칼·뜨거운 용기 제외
낙하 대응 | Grip Loss 감지 · 통로 위 운반 금지 · Counter 위 저고도 이동
Fail-safe | 정전·고장 시 Garage 복귀 또는 정지 · 수동 해제 · 일반 Kitchen 사용 유지
접근 제어 | Child Lock · Garage Door Interlock · 원격 정지
[CONCEPT]
표준 · 인증 | 내용 | 시점
ISO 10218-1/-2:2025 | 로봇·Robot 응용 안전. TS 15066 협동 요구 통합 (2025.2) | Seed: 설계 기준
ISO 13482 | Personal Care Robot 안전 (국내 인증 사례 존재) | A: 적용성 검토
IEC 60335-1 / KC | 가정용 전기기기 안전 · 전기용품안전관리법 | A: 본인증
KC 전자파 (EMC) | 전파법 적합성평가 | A: 본인증
ISO 13849-1 | 안전기능 PL (목표 PL d, ASSUMPTION) | Seed: 설계
식품용 기구 기준 | 식품접촉 Tip·Pad 재질 (식약처 기준 및 규격) | Seed: 재질 선정
Seed 범위: Risk Assessment · 설계 기준 적용 · 예비시험 (비용 ASSUMPTION 0.7억원 내외)  |  본인증: Series A (A16). 인증기간이 Launch 일정 Risk
```

**Visual 구성**: 좌측 Safety 기능 표 (Zone·Speed·Force·Payload·Fail-safe). 우측 적용 표준·인증 표 (단계별).

**Chart / Diagram**: 표 2개

**Speaker Note**: 머리 위 Robot의 안전은 투자자가 반드시 묻는 질문입니다. 원칙은 사람이 있는 Zone 위로 물건을 운반하지 않고, 사람이 Robot Zone에 들어오면 즉시 정지하며, 가반하중과 속도를 낮게 제한하는 것입니다. 2025년 개정된 ISO 10218에 협동 안전 요구사항이 통합되었고, 가정용은 ISO 13482와 KC 전기안전, 전자파, 식품용 기구 기준을 함께 봐야 합니다. 본인증은 Series A 단계로 계획했습니다.

## A8. 설치 Architecture: 구조체 정착 · 전원 · 통신

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A8
설치 Architecture: 구조체 정착 · 전원 · 통신
Robot 하중은 가구가 아닌 구조체로 전달. 구축은 벽체 유형 실측 확인이 설치 가능 여부의 1차 Gate (Robot-ready 적용 가능률 60% 가정의 근거 항목).
Arm · Payload
(동하중 포함)
Carriage
· Rail
보강 Steel
Frame
Post-installed
Anchor
RC 벽체 ·
슬래브
검토 | 내용 | 기준 · 방법 | Tag
구조 | 설계하중 = (Arm + Carriage + Payload) × 동적계수 · 피로 (반복 이동) | 콘크리트용 앵커 설계기준 (KDS 14 20 54) · ACI 318 Ch.17 참조 | ASSUMPTION
벽체 유형 | RC 벽식 → 직접 정착 / 조적·경량벽 → 바닥·천장 지지 Frame 또는 Dock Type 전환 | 실측 단계 판정 · 내력벽 손상 금지 | TBV
처짐·진동 | Rail 처짐 · 공진 → 위치정밀도 · 소음 영향 | Mock-up 계측 (가속도·변위) | TARGET
전기 | 전용 회로 · 누전차단 · Garage 내 전원 | 전기설비규정 (KEC) 기준 시공 (Partner) | CONCEPT
통신 | 유선 Ethernet / PoE + Wi-Fi 보조 · 원격진단 | 세대 내 통신 단자 위치 | CONCEPT
설비 | 식세기 상향 Housing 급·배수 · 환기 | 배관 Partner 시공 | CONCEPT
설치 순서 (TARGET): 실측 · 벽체 판정 → Partner 철거·가구·전기 → ARKI Frame·Rail → Robot 장착 → Auto Calibration → Safety Check → 인수  |  Robot Module 설치 1일 · 2인 (M24)
```

**Visual 구성**: 좌측 Load Path Diagram (Arm → Carriage → Rail → 보강 Frame → Anchor → RC 벽체). 우측 설치 검토 표 (구조·전기·통신·설비) + 설치 순서.

**Chart / Diagram**: Load Path Flow + 표

**Speaker Note**: Rail형 설치에서 Robot 하중은 상부장이 아니라 보강 Frame을 거쳐 구조체로 전달되어야 합니다. 동하중과 반복하중을 고려해 Anchor를 설계하고, 구축은 벽체가 철근콘크리트인지, 조적이나 경량벽인지 실측 단계에서 확인합니다. 이 검토 절차 자체가 설치 Standard이자 Partner 교육 내용입니다.

## A9. Competition 상세

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A9
Competition 상세
공개 보도 기준 (A23 Sources). 성능 비교는 공개 Data 부재로 하지 않음. "최초 · 압도적" 주장 없음.
Player | Category | 가격 · 상태 | 접근 | Tag
1X NEO | Humanoid | $20,000 또는 월 $499 (최소 6개월) · 2026 출하 | 원격조종 학습 병행 · 범용 가사 | FACT
Sunday Robotics Memo | Wheeled Mobile | 2026 베타 약 50가구 · 양산 $10k 미만 목표 | 식세기 적재·테이블 정리 시연 | FACT
LG CLOiD | Wheeled Humanoid | CES 2026 공개 · 가격 미공개 | 식세기 비우기·세탁 시연 · LG 가전 연동 | FACT
Figure 03 | Humanoid | 가격 미공개 (RaaS 언급) | 가사 시연 (빨래·설거지) | FACT
Tesla Optimus | Humanoid | 소비자 목표 $20~30k · 2027 전후 | 범용 | FACT
Samsung Bot Handy | Mobile Manipulator | CES 2021 Concept · 출시 미공개 | 식기 정리 시연 | FACT
Moley | Built-in Robotic Kitchen | Arm 포함 £248,000 / 제외 £128~140k | 천장 Rail 양팔 · 조리 | FACT
Samsung Bot Chef | Built-in (Concept) | CES 2020 Concept | 상부장 하단 Rail 양팔 조리 시연 | FACT
Posha | Countertop Cooking | $1,750 (선주문 $1,500) + 월 $15 | 자동 투입·젓기 조리기 | FACT
국내 Food-tech (로보아르테 · 웨이브 등) | Commercial Cobot | 상업 주방 · 매장 자동화 | 가정용 아님 | FACT
ARKI | Built-in Kitchen Integration | Concept 단계 · 실적 없음 | Clean-up · 공동주택 Template · 설치 Standard | CONCEPT
시사점: 범용 Mobile·Humanoid가 월 $499 수준 구독가를 제시 → ARKI는 고정 설치형의 신뢰성 · 바닥 점유 0 · Kitchen 일체 디자인 · 설치·A/S로 차별화해야 함 (미검증)
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 가정용 Robot 시장은 2025년 이후 빠르게 움직이고 있습니다. 1X는 월 499달러 구독을 내놓았고, Sunday와 LG는 식기세척기 작업을 시연했습니다. ARKI가 같은 가격대에서 선택받으려면 고정 설치형의 신뢰성, 바닥을 차지하지 않는 점, 주방과 일체화된 디자인, 설치와 A/S가 실제로 더 낫다는 것을 증명해야 합니다.

## A10. IP / Patent Portfolio 후보 (10 Family)

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A10
IP / Patent Portfolio 후보 (10 Family)
등록 가능성 주장 없음. Seed M3까지 선행기술조사 (KIPRIS · USPTO · EPO) → 5~8건 출원 우선순위 결정. 전체 = TBV
# | Family | Protectable Core | Business Relevance | Prior Art Risk (선행기술조사 필요)
1 | 주방가구 일체형 Robot Rail · Dock · Storage | 상부장 하단 Rail + Garage 일체 구조 · 하중 전달 | 높음 (모든 Rail형) | 높음 — 천장 Rail 로봇주방 (Moley) · Under-cabinet Rail (Bot Chef)
2 | Robot-ready Kitchen Interface Module | 표준 Mount · 전원 · 통신 · Sensor Interface 규격 | 높음 (Land 상품) | 중간 — 가구 Interface · 가전 Built-in 규격
3 | Fold / Deploy Robot Storage | 키큰장 내 수납·전개 기구 | 중간 (Compact) | 중간 — 가전 Lift · 수납형 Robot
4 | Human / Robot Zone Safety Control | 주방 Zone Map 기반 정지·감속 Logic | 높음 | 높음 — 산업 SSM · 협동 Robot 안전
5 | Kitchen End-effector | 식기 형상 (밥공기·국그릇) 대응 Gripper·Suction | 중간 | 중간 — 식품 Gripper
6 | Food-contact Consumable Cartridge | 교체형 Tip · Pad 체결 구조 · 교체주기 인식 | 중간 (반복매출) | 중간 — 교체형 Gripper Pad
7 | Installation Auto Calibration | 설치 후 Target 기반 자동 좌표 보정 | 높음 (설치시간) | 중간 — Robot Calibration 일반
8 | Dishwasher Robot Interface | Door · Rack 위치 표준 · 상향 Housing 연동 | 높음 | 중간 — 가전사 Robot 연동 특허 가능성
9 | Robot Cleaning / Sanitizing Dock | Garage 내 EE 세척·건조 | 중간 (위생) | 낮음~중간
10 | Layout 기반 Robot Module Selection | 평면 분류 → Architecture·Module 자동 선택 Software | 중간 (표준화) | 낮음~중간 — 설계 자동화 SW
출원 우선순위 가설: ② Interface Module · ⑦ Auto Calibration · ⑧ Dishwasher Interface — 사업 핵심이면서 선행 위험이 상대적으로 낮을 것으로 추정 (TBV)
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 특허 후보 열 개를 사업 관련성과 선행기술 위험으로 정리했습니다. Rail 일체형 구조는 Moley나 삼성 Bot Chef 같은 선례가 있어 선행기술 위험이 높습니다. 표준 Interface, 자동 Calibration, 식기세척기 Interface가 사업 핵심이면서 상대적으로 위험이 낮을 것으로 보지만, 모두 선행기술조사 후 판단합니다.

## A11. Household Unit Economics 상세 (1세대 · 5년 · 만원)

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A11
Household Unit Economics 상세 (1세대 · 5년 · 만원)
구축 Premium · 직접판매 · Base. Y3/Y5 = 해당 연도 원가 수준을 5년 적용. 전부 DERIVED (from ASSUMPTION). xlsx Household 시트와 동일.
항목 | 구매 Y3 | 구매 Y5 | Rental Y3 | Rental Y5
Robot-ready Kitchen 증분 | 450 | 450 | 450 | 450
설치·Calibration | 80 | 80 | 80 | 80
Robot (구매) | 1,490 | 1,490 | 0 | 0
Rental 60개월 | 0 | 0 | 1,980 | 1,980
Care Basic 5년 | 240 | 240 | 0 | 0
Consumables 5년 | 126 | 126 | 63 | 63
Software · Tool (기대값) | 32 | 32 | 32 | 32
5년 매출 | 2,418 | 2,418 | 2,605 | 2,605
Kitchen Module 원가 | 277 | 244 | 277 | 244
Robot BOM (Rental: 순감가) | 1,150 | 900 | 978 | 765
Rental 금융비용 | 0 | 0 | 264 | 207
설치·물류·Warranty | 145 | 123 | 131 | 99
Care 원가 5년 | 184 | 134 | 184 | 134
Consumables·Upgrade 원가 | 54 | 54 | 64 | 64
획득비용 (CAC) | 150 | 150 | 150 | 150
Lifetime Contribution | 458 | 813 | 557 | 942
Contribution Margin | 18.9% | 33.6% | 21.4% | 36.2%
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 한 세대 경제성의 상세 계산입니다. 구매 모델은 Robot 매출이 대부분이고, Rental 모델은 같은 Robot을 60개월 동안 회수합니다. Rental은 잔존가치를 15% 회수한다고 보고 순감가와 금융비용을 원가로 넣었습니다.

## A12. Rental Model: 월 요금 Build-up · Payback · Partner 구조

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A12
Rental Model: 월 요금 Build-up · Payback · Partner 구조
Rental = 초기부담 감소 수단. ARKI의 장기 자산보유 지양 → Seed는 직접 Pilot, Scale은 Rental / Capital Partner. 전부 DERIVED (from ASSUMPTION).
만원 / 월 (Robot 1대) | Y3 원가 | Y5 원가
감가 (BOM × 85% ÷ 60) | 16.3 | 12.8
금융비용 (평균잔액 × 8% ÷ 12) | 4.4 | 3.4
Care 원가 ÷ 12 | 3.1 | 2.2
Grip Kit 원가 ÷ 12 | 0.5 | 0.5
Failure Reserve (BOM × 4% ÷ 60) | 0.8 | 0.6
월 원가 | 25.1 | 19.6
월 요금 (가정) | 33.0 | 33.0
월 Contribution · Margin | 7.9 · 24% | 13.4 · 41%
마진 20% 확보 요금 | 31.3 | 24.4
Payback (개월) | 39 | 30
36개월 Payback 최대 BOM | 1,059 | 1,089
Rental Partner 경제성 (Base, Y4~)
· Robot 매입가: ASP × 88% = 1,311만원
· 월 순유입: 요금 33 − ARKI 서비스료 6 = 27만원 × 60개월
· 잔존가치 15% = 197만원 → 연 IRR 약 13.1% (연체·해지 미반영)
· Conservative (월 29만원): IRR 약 12.4%
[DERIVED]
단계 | 구조 | 목적
Seed (Y1~Y3) | ARKI 직접 Rental Pilot (소량) · 자산 = Opex·Capex | 요금·해지율·A/S 실측
Scale (Y4~) | Rental / Capital Partner가 자산 보유 · ARKI는 Product·Software·Care | ARKI Balance Sheet 경량화
결론: Rental은 Y3 원가에서 Payback 39개월로 Partner 허들(36개월) 미달 → BOM ≤ 1,059만원 달성 전까지 Rental은 Pilot 규모로 제한. Conservative 요금(월 29만원) 시 Y3 Payback 53개월
```

**Visual 구성**: 좌측 월 원가 Build-up 표 (Y3/Y5). 우측 Partner 구조 경제성 (매입가·월 순유입·IRR) + Seed/Scale 단계 구분.

**Chart / Diagram**: 표 + 구조 Diagram

**Speaker Note**: Rental 요금은 원가에서 출발했습니다. Y3 원가 수준에서 감가, 금융, Care, Grip, Reserve를 합치면 월 25.1만원이고 33만원 요금에서 마진은 24%입니다. Payback은 39개월로 36개월을 넘어서, Y3 원가로는 렌탈사가 자산을 사기 어렵습니다. Y5 원가에서는 30개월입니다. Partner가 ASP의 88%에 Robot을 사고 월 27만원을 받으면 연 IRR이 약 13%로 계산되지만, 고객 연체와 중도해지는 반영하지 않았습니다.

## A13. Care · Consumables Model

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A13
Care · Consumables Model
Care = Robot Lifecycle Maintenance Contract (Software 구독 아님). Consumables = 위생 · 마모 · Grip 성능 · 식품접촉부 교체 · 안전 유지 목적.
Care (만원/대·년) | Y3 | Y5 | Tag
Care Basic 연 요금 | 48 | 48 | ASSUMPTION
정기 방문 (횟수 × 원가) | 22.0 | 12.0 | ASSUMPTION
고장 방문 (0.6회 × 18만원) | 10.8 | 10.8 | ASSUMPTION
Cloud · Software | 4.0 | 4.0 | ASSUMPTION
Care Contribution · Margin | 11.2 · 23% | 21.2 · 44% | DERIVED
· 포함: 정기 안전점검 · Calibration · Remote Diagnosis · Joint / Rail / Vision 상태 · Consumables Check · Software Update · A/S
· 참고: 가전 A/S 출장비 2.8만원 (삼성·LG 2026, 소비자 부과분, FACT) ≠ ARKI 실제 방문 원가
· Care Plus 연 72만원 = Kit 정기교체 포함 (Base 재무 미반영)
Kit | 구성 | 만원 | 주기 | 연 List
Grip Kit | Finger Pad · Food-contact Tip · Suction Cup | 4.5 | 분기 | 18.0
Cleaning Kit | Brush · Wiper · Cleaning Pad | 2.5 | 분기 | 10.0
Protection Kit | Sensor Cover · Sleeve · Seal | 4.0 | 반기 | 8.0
합계 (List) |  |  |  | 36.0
구매율 70% 적용 매출 · 원가 35% |  |  |  | 25.2 · 8.8
[ASSUMPTION]
· 검증 KPI: Replacement Cycle · Cost per Kit · 연 Consumables 매출/Robot · Gross Margin · Care Attach Rate
· 부품 원가 참고: Robotiq Fingertip $175~195, Food-grade Cup £7~20 (FACT) → 자체 설계로 원가 35% 목표
Care는 Y3에 Profit Center 아님 (Margin 23%) → 원격진단으로 방문 1.5회 이하 · Route Density로 방문원가 9만원 이하 달성 시 Y5 Margin 44% (TARGET 경로)
```

**Visual 구성**: 좌측 Care 원가 구조 표 (Y3/Y5) + 포함 서비스. 우측 Consumables Kit 표 (구성·가격·교체주기·연 매출·원가) + 검증 KPI.

**Chart / Diagram**: 표 2개

**Speaker Note**: Care는 단순 Software 구독이 아니라 Robot 수명주기 유지보수 계약입니다. 연 48만원에 정기점검 2회, Calibration, 원격진단, Update, A/S 공임을 포함합니다. Y3에는 방문 원가 때문에 마진이 23%이고, 원격진단으로 방문을 줄이고 지역 밀도가 올라가는 Y5에 44%가 됩니다. 소모품은 억지 Lock-in이 아니라 위생과 Grip 성능, 식품접촉부 교체 관점에서 설계합니다. 교체주기는 실측 전 가정입니다.

## A14. 5-Year Financial Model (3 Scenario)

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A14
5-Year Financial Model (3 Scenario)
Bottom-up Driver: Kitchen · Robot · Robot-ready Only · Rental · Care / Consumables Installed Base · Upgrade. 억원. 상세 수식: xlsx FM 시트. 전부 DERIVED (from ASSUMPTION · TARGET).
Base (억원) | Y1 | Y2 | Y3 | Y4 | Y5
Kitchen Build + 설치 | 0.0 | 0.1 | 2.6 | 9.3 | 22.7
Robot Hardware | 0.0 | 0.3 | 4.4 | 21.8 | 51.5
Rental + Care + Consumables | 0.0 | 0.0 | 0.4 | 1.3 | 3.1
Upgrade | 0.0 | 0.0 | 0.0 | 0.1 | 0.3
매출 | 0.0 | 0.4 | 7.5 | 32.5 | 77.6
매출총이익 | 0.0 | -0.3 | 1.8 | 9.8 | 27.9
매출총이익률 | — | -75% | 25% | 30% | 36%
Contribution (채널비용 후) | 0.0 | -0.4 | 0.8 | 6.4 | 20.3
Opex | 10.2 | 12.8 | 30.5 | 43.9 | 56.7
영업이익 (근사) | -10.2 | -13.3 | -29.7 | -37.5 | -36.4
Kitchen · Robot 설치 | 0 · 0 | 5 · 5 | 50 · 42 | 180 · 154 | 480 · 363
Installed Robot (기말) | 0 | 5 | 48 | 201 | 565
Y1
Y2
Y3
Y4
Y5
Y5 (억원) | 매출 | Contrib. | 영업이익 | 누적현금
Conservative | 27.8 | 0.3 | -56.4 | -156.0
Base | 77.6 | 20.3 | -36.4 | -128.0
Upside | 134.0 | 44.8 | -11.9 | -96.6
누적현금 = 5년 누적 영업현금흐름 최저점 (투자유치 전, Rental 자산 포함)
Upside = 가격 동일, Partner 물량 · 표준화 · 설치원가 · Installed Base 차이. Conservative = WTP·BOM 하락 미달 → Y5 Contribution ≈ 0 → Scale 투자 보류 시나리오 (Kill Criteria M24)
```

**Visual 구성**: 상단 Base 손익 상세 표 (Y1~Y5, 억원). 하단 Conservative / Upside 요약 표 + 매출 Column Chart.

**Chart / Diagram**: 표 + 3-Scenario 매출 Column

**Speaker Note**: Base에서 매출은 Y3 7.5억원, Y5 77.6억원이고, 5년 내내 영업적자입니다. Hardware 회사의 일반적인 경로이며 Y5 영업손실은 36억원입니다. Conservative는 지불의사와 BOM 하락이 약해 Y5 Contribution이 거의 0으로, Scale 투자를 보류해야 하는 시나리오입니다. Upside는 가격을 올리지 않고 Partner 물량, 표준화, 설치원가로만 차이를 두었습니다.

## A15. Sensitivity Analysis

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A15
Sensitivity Analysis
Top 3 Critical Variable = Customer WTP · Robot BOM · Partner Distribution. 회색 = 불리, 주황 = 유리. 전부 DERIVED.
세대 5년 Lifetime Contribution (구매·Y3 원가)
Base 458만원 · 변화 (만원)
Robot ASP (WTP) ±20%
-286
+286
Robot BOM ±20%
-230
+230
Robot-ready 증분가 ±20%
-90
+90
직접판매 획득비용 ±50%
-75
+75
Failure Rate 0.3 ↔ 1.2회
-84
+49
Care 요금 ±20%
-48
+48
방문 원가 ±30%
-33
+33
Standard Module 사용률 -15pp/+15pp
-33
+33
설치 원가 ±50%
-30
+30
Consumables 구매율 50% ↔ 90%
-23
+23
회사 Y5 Contribution (Base)
Base 20.3억원 · 변화 (억원)
Customer WTP (Robot ASP·증분가 ±20%)
-12.3
+12.3
Robot BOM ±20%
-6.6
+6.6
Partner 경유 Kitchen ±30%
-4.8
+4.8
Robot Attach Rate 65% ↔ 95%
-3.1
+1.6
Failure Rate 0.3 ↔ 1.2회
-1.4
+0.9
Rental 비중 20% ↔ 60%
-1.1
+1.1
Standard Module 사용률 -15pp/+10pp
-1.3
+0.9
신축 Option 선택률 5% ↔ 15%
-0.8
+0.8
설치 원가 ±50%
-0.7
+0.7
Service 원가 (방문) ±30%
-0.1
+0.1
Robot Attach Rate · Standard Module 사용률 · Failure Rate는 중위권. Rental 비중은 P&L보다 현금(자산) 영향이 큼 (A12). 회사 기준 민감도는 model.py 산출 (xlsx Sensitivity 하단 정적 표).
```

**Visual 구성**: 좌우 Tornado 2개: (좌) 세대 5년 Contribution, (우) 회사 Y5 Contribution. Top 3 변수 강조.

**Chart / Diagram**: Tornado Chart 2개

**Speaker Note**: 두 기준으로 민감도를 봤습니다. 세대 기준으로는 Robot 가격, Robot BOM, Robot-ready 증분가 순서이고, 회사 기준으로는 고객 지불의사, BOM, Partner 경유 물량 순서입니다. 즉 Top 3 Critical Variable은 Customer WTP, Robot BOM, Partner Distribution입니다. 신축 Option 선택률은 5년 안에는 영향이 작은데, 계약에서 설치까지 2년 시차가 있기 때문입니다.

## A16. Seed Use of Funds 검증 (24개월)

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A16
Seed Use of Funds 검증 (24개월)
수정안 = 재무모델 Base Y1+Y2 (xlsx Use_of_Funds 시트 연동). 인당 연 8,500만원 = 평균 연봉 약 7,100만원 × 1.2 (4대보험·퇴직급여) ASSUMPTION.
억원 | Draft | 수정안 | 근거
Core Development Team | 8.0 | 12.8 | 평균 7.5명 × 2년 × 8,500만원
Robot / Kitchen Prototype | 4.0 | 3.0 | Arm 3~4대 · Rail 2식 · EE 반복 (BOM A4)
Mock-up / Installation Dev. | 2.5 | 1.8 | 50평 임차 24개월 + Full-scale Mock-up 2식
Vision / Software / Data | 1.5 | 1.0 | GPU · Cloud · Data 수집·Annotation
Pilot / Customer Validation | 1.5 | 2.1 | Interview·Conjoint + Pilot 5세대 손실 + Marketing
Safety / Certification / IP | 1.0 | 1.0 | 예비시험 · Risk Assessment · 출원 5~8건
Operations / Contingency | 1.5 | 4.1 | G&A 1.8 + Contingency 10%
합계 | 20.0 | 25.8 | 
판단
· 20억원 단독: 약 18.6개월 → 24개월 Milestone 미달 Risk
· Plan A: Seed 20억 + TIPS R&D 최대 8억 = 28억 (여유 2.2억). TIPS 선정은 미확정
· Plan B: Seed 25억 또는 M18 Bridge (M12 Evidence 기반)
· 절감 옵션: Arm 구매형 Prototype · Mock-up 공간 공유 · 채용 3개월 순연 (−2~3억, 일정 Risk 증가)
· Draft 8억 인건비 = 평균 4.7명 수준 → Robot·Vision·기구·주방통합·안전·현장 동시 수행 불가
결론: 20억원은 '과다'가 아니라 24개월 기준 약 5.8억원 부족 → TIPS 연계를 기본 구조로, 미선정 시 25억원 또는 Bridge. 인증 본비용은 Series A로 이연
```

**Visual 구성**: 좌측 Draft vs 수정안 상세 표 (산식 포함). 우측 판단: 20억원 적정성, Plan A/B, 비용 절감 옵션.

**Chart / Diagram**: 표

**Speaker Note**: 사용자 초안의 20억원 배분을 실제 비용 구조로 다시 계산했습니다. 가장 큰 차이는 인건비입니다. 초안 8억원은 24개월 기준 평균 4~5명 수준인데, 로봇·비전·기구·주방통합·안전·현장 인력을 고려하면 평균 7.5명이 필요하고 약 12.8억원이 됩니다. 전체로는 약 25.8억원이 필요해 20억원으로는 19개월 정도입니다. 그래서 TIPS 연계를 기본안으로 하고, 안 되면 증액이나 Bridge를 제안합니다.

## A17. Customer Validation · 기술 KPI

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A17
Customer Validation · 기술 KPI
현재 측정값 없음 → 모두 TARGET. 고객검증은 "말"이 아닌 "행동"(예약금·유료 Pilot)으로 종결.
방법 | 표본 | 확인 항목 | 시점
Time-diary | 30세대 · 7일 | Clean-up 빈도·시간 · Pain | M0~M3
Interview | 50명 (Premium 상담 30 · 최근 시공 10 · 신축 계약 10) | Pain · 수용성 · 안전·소음·디자인 우려 · 구매 vs Rental | M1~M4
PSM + Gabor-Granger | n≥300 (Panel) | Robot 가격 · Rental 월 요금 · Care 요금 Range | M4~M6
Choice-based Conjoint | n≥300 | 가격 × Task 범위 × 노출/은폐 × 소음 × 설치일수 × Care | M6~M9
Smoke Test | Mock-up Demo 방문자 | 환불가능 예약금 전환율 | M9~M12
Paid Pilot | 3~5세대 | 실제 결제 · 사용 Log · 해지 의향 | M12~M24
기술 KPI (TARGET) | M12 Mock-up | M24 Real Home
Task Success Rate (Approved Task) | 85% | 95%
Cycle Time (식기 1개 Pick→Place) | 25초 | 15초
Human Intervention | 20개당 1회 이하 | 100개당 1회 이하
Object Coverage (표준 한식 식기) | 60% | 80%
Recovery Rate (Grasp 실패 자동복구) | 50% | 70%
Noise (1m) | 측정 | 55dB(A) 이하
Safety Stop (Zone 진입) | 100% 정지 | 100% · 오정지 1일 1회 이하
Calibration · Installation Time | 측정 | 2시간 · 1일 2인
Kill 연동: M9 성공률 70% 미만 → Task Scope 축소 (Unloading·Storage 우선)  |  M12 WTP 중앙값이 목표가의 60% 미만 → B2C 재검토 (신축 B2B2C·Rental 중심)
```

**Visual 구성**: 좌측 고객검증 설계 표 (방법·표본·확인항목·시점). 우측 기술 KPI 표 (M12 Mock-up / M24 Real Home TARGET).

**Chart / Diagram**: 표 2개

**Speaker Note**: 고객 검증은 인터뷰만으로 끝내지 않습니다. 시간 일지로 Pain의 크기를 재고, Van Westendorp와 Gabor-Granger로 가격 구간을, Conjoint로 구매와 Rental, 기능, 노출 디자인의 상대 가치를 봅니다. 마지막으로 환불 가능한 예약금으로 실제 행동을 확인합니다. 기술 KPI는 현재 수치가 없어 목표만 제시했습니다.

## A18. What Must Be True

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A18
What Must Be True
7개 전제가 모두 성립해야 Built-in Residential Robotics Platform으로 Scale 가능. 현재 Evidence는 전부 "없음" 또는 추정.
전제 | 현재 Evidence | 향후 검증 (Seed) | Failure Condition
1  Remodeling 고객이 Robot Integration Premium 지불 | 없음 (가격 가설만) | PSM·Conjoint · 예약금 · Paid Pilot | WTP 중앙값 < 목표가 60% (M12)
2  주요 Kitchen Layout이 소수 Template으로 분류 | 없음 (통상 치수 Concept) | 평면 30개 · Template Coverage | 상위 3개 Template Cover < 70%
3  Single Robot Architecture 반복 설치 | 없음 | Mock-up 2식 · Home Pilot 설치시간 | 세대별 Custom 설계 필요 · 설치 > 2일
4  Robot + Installation GM 개선 | 부품 공개가 기반 BOM 추정 | BOM v2 견적 · 설치원가 실측 | Y3 BOM > 1,300만원 전망
5  Care + Consumables 반복매출 형성 | 없음 | Pilot 세대 Care 가입 · Kit 교체주기 | Care 가입 < 40% · 교체주기 > 2배
6  Partner Distribution이 Direct보다 빠르게 Scale | 없음 (가상 Partner 미기재) | Partner Pilot 시공 · 수수료 조건 | M24 Partner Pilot 0건
7  Service Cost ≤ Recurring Revenue | 없음 | 방문원가·고장률 실측 | 방문 원가 > Care 요금 (Y3 원가 기준)
Seed 투자 = 7개 전제를 24개월 안에 확인하는 Option 매입. 1·2·4번이 Series A 판단의 핵심 (Sensitivity Top 변수와 일치)
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: Seed 투자는 이 일곱 가지 전제를 확인하는 옵션을 사는 것입니다. 현재 Evidence는 모두 없거나 추정 단계이고, 각 전제마다 실패로 판정할 조건을 미리 정했습니다. 특히 지불의사, Template 분류, Robot 원가 개선이 Series A 판단의 핵심입니다.

## A19. Risk Register: Risk → 투자 후 Evidence → Kill Criteria

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A19
Risk Register: Risk → 투자 후 Evidence → Kill Criteria
Seed Capital의 목적 = Commercial Risk Reduction. 각 Risk를 측정 가능한 Evidence와 판단 시점에 연결.
Risk | 내용 | 투자 후 Evidence | Kill · 대응
Apartment Fit | 동선·Reach 양립 · 벽체 구조 · 천장고 | Mock-up · 평면 30개 · 벽체 판정 | M6 Architecture 변경
Technology | Clean-up 신뢰성 · 한식 식기 다양성 | 성공률 · 개입 · Recovery 측정 | M9 Scope 축소
Standardization | Custom 설계 비중 과다 | Standard Module 사용률 · Reuse | M18 Thesis 재검토
Customer WTP | Robot Premium 지불 거부 | PSM · Conjoint · 예약금 | M12 B2C 재검토
Installation Economics | 설치시간 · 현장 변수 | 설치·Calibration 시간 실측 | M18 원가 기준 미달 시 Template 재설계
Rental Economics | Payback > 36개월 | BOM 절감 · 요금 Test | BOM > 1,060만원 시 Rental Pilot 한정
Service Economics | 방문원가 > Care 요금 | 방문·고장 실측 · 원격진단 | Care 요금·구성 재설계
Channel | Partner 확보 실패 · 공사업체화 | Partner Pilot · 역할 분담 계약 | M24 Scale 보류
Safety · 인증 | 머리 위 작업 사고 · 인증 지연 | Risk Assessment · 예비시험 | 사고 0 · 인증 일정 Series A 계획 반영
Competition | 대기업·Humanoid 저가 구독 | Template·설치 Data · Partner 선점 | 차별화 미입증 시 B2B Module 공급으로 전환 검토
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 리스크마다 투자 후 어떤 증거로 줄일지, 실패하면 무엇을 할지를 연결했습니다. 기술 리스크만이 아니라 공간, 표준화, 가격, 설치·렌탈·서비스 경제성, 채널, 안전, 경쟁까지 포함했습니다.

## A20. VC Red-Team Q&A (1/2)

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A20
VC Red-Team Q&A (1/2)
Seed 심사역 관점 재검토. 답이 약한 항목은 본문 수정 반영 (가치 Gap · Rental Payback · Seed 부족분 · Founder 공백 명시).
# | 질문 | 답 (근거 위치)
1 | 왜 Robot Arm인가? | 식기 형상·위치가 매번 다름 → 고정 기구로 불가. 단, Arm 범위는 Rail·Dock으로 제한해 범용성보다 신뢰성 우선 (09장).
2 | 기존 Appliance로 해결 불가능한가? | 가전은 내부 공정만 자동화. 식탁→식세기→수납 이동은 가전 경계 밖 (04장). 가전사 확장 가능성은 Risk로 인정.
3 | 왜 Kitchen Clean-up인가? | 매 식사 반복 · 열·칼 위험 없음 · 식세기·수납이라는 고정 끝점 → 표준화 용이. 체감가치는 Cooking보다 낮음 (08장).
4 | 돈을 낼 만큼의 Pain인가? | 미검증. 가치 Anchor 월 11~24만원 < 원가 기반 Rental 24~31만원 → Gap 존재. Time-diary·WTP로 M12 판정 (14장).
5 | Robot 가격은 얼마인가? | 가설 1,490만원 (Test 990~1,790). Y3 BOM 1,150만원 → GM 23% (A4·A11).
6 | Remodeling 포함 총 고객비용은? | Kitchen 공사비 (Premium 2,000~4,000만원, ASSUMPTION) + ARKI 2,020만원. 증분 부담 큼 → Rental·신축 Option 병행 (14장).
7 | Rental은 얼마여야 하는가? | 원가 기반 마진 20% 요금: Y3 31만원 · Y5 24만원. 가설 33만원. Partner Payback 36개월 위해 BOM ≤ 1,060만원 (A12).
8 | Care는 왜 필요한가? | Calibration·Rail·Vision 점검과 위생 관리가 안전·성능 유지 조건. Software 구독 아님 (A13).
9 | Consumables는 실제로 얼마나? | 가설 연 36만원 List, 구매율 70% → 25만원. 교체주기 미실측 (A13).
10 | Robot 고장 시 Kitchen 사용 가능한가? | 설계 Requirement: Garage 복귀·수동 해제·일반 Kitchen 기능 유지 (09장 #07, A7).
11 | 머리 위 Robot은 안전한가? | 사람 위 운반 금지 · Zone 진입 정지 · 1.5kg 이하 · ISO 10218:2025 · 13482 검토. 인증은 Series A (A7).
12 | 집마다 다른데 표준화 가능한가? | 가설. 4단계 분류 + 평면 30개로 M12 판정, Standard Module 60% 미만 시 재검토 (11장).
13 | Bay보다 Geometry가 중요한가? | Robot 설치는 주방 Run·설비 위치·Aisle이 결정, Bay는 거실·침실 배치 변수 (06장).
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 심사역이 반드시 물을 질문에 대한 답입니다. 답이 약한 항목은 숨기지 않고 본문에 반영했습니다. 대표적으로 가치 기준 가격과 원가 기반 가격의 차이, Rental Payback, Seed 부족분, Founder 정보 공백입니다.

## A21. VC Red-Team Q&A (2/2)

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A21
VC Red-Team Q&A (2/2)
약한 답: 4 (Pain) · 6 (총 고객비용) · 18 (가구사 직접 진입) · 23 (자금) · 25 (Founder) → Investment Memo의 Reasons Not to Invest
# | 질문 | 답 (근거 위치)
14 | 공사업체가 되는 것 아닌가? | 철거·가구·전기·배관 = Partner. ARKI = Module·Calibration·Safety QA. KPI: Build 비중 Y5 29% (19장).
15 | 왜 구축부터인가? | 이미 철거·시공하는 고객 → 추가 Integration 비용 최소 · 가격·설치 직접 검증 · 신축은 2년 Lag (12장).
16 | 왜 신축이 Scale Channel인가? | Project당 수백 세대 · 설계 단계 표준 Spec · 유상옵션 관행 (분양가 9.7%). 단, 매출 인식 지연 (12장).
17 | 건설사가 직접 하면? | 건설사는 Robot·SW·A/S 운영 역량보다 유통 역할. ARKI Spec을 Option으로 채택하는 Distribution 관계 (20장).
18 | Kitchen Furniture 회사가 직접 하면? | 가장 현실적 위협. Module·Channel Partner로 협력하되 Template·설치 Data·Calibration SW로 차별 (미검증).
19 | Robot OEM이 직접 하면? | OEM은 Arm 판매가 목적, 주거 설치·A/S·가구 Interface는 비핵심 → Supplier 관계 (20장).
20 | Rental Asset 부담은? | Seed는 소량 Pilot만 ARKI 보유. Y4부터 Rental Partner가 자산 보유, Partner IRR 약 13% (연체 미반영, A12).
21 | A/S 비용은? | Y3 Robot당 연 36.8만원 (방문 2회 × 11만원 + 고장 0.6회) → Y5 26.8만원 (A13).
22 | Care가 Profit Center가 될 수 있는가? | Y3 Margin 23% → 아님. 방문 1.5회 이하·원가 9만원 이하에서 Y5 44%. Route Density 의존.
23 | 20억원이 충분한가? | 아니오. 24개월 수정안 약 25.8억원 → TIPS 8억 연계 또는 25억원 / M18 Bridge (A16).
24 | 24개월 후 Series A Evidence는? | Paid Pilot · WTP · BOM ≤ 1,150만원 경로 · Template 3개 70% Cover · 설치 1일 · Partner Pilot (22장).
25 | Founder가 왜 적합한가? | [Founder 정보 필요] — 현재 답할 수 없음. 투자 판단 1순위 공백 (23장).
```

**Visual 구성**: 표 중심 Appendix

**Chart / Diagram**: 

**Speaker Note**: 약한 답이 다섯 개 있습니다. Pain의 크기, 총 고객비용, 가구사의 직접 진입, Seed 금액, 그리고 Founder입니다. 이 다섯 개가 Investment Memo의 투자하지 않을 이유와 그대로 연결됩니다.

## A22. Investment Scorecard · Seed 판단

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A22
Investment Scorecard · Seed 판단
점수 1~5 (5 = 강한 Evidence). 현재 = 2026.10 · Target = M24. 본 판단은 자료 작성자의 Red-Team 의견.
항목
현재 → Target
핵심 Evidence
Market
공식 통계로 Stock·공급 확인. SAM 비율(Premium·적용·Option)은 가정
Product
Concept 정의 명확. 실물·Mock-up 없음
Technology
Cobot·Vision 부품은 상용. 가정 주방 Clean-up 신뢰성 미검증
Customer Demand
Interview·WTP·예약 없음. 가치 Anchor < 원가 Gap
Standardization
평면 분석 없음. 분류 체계만 존재
Unit Economics
Y3 세대 CM 19% · Y5 34% (가정). BOM 의존
Recurring Revenue
구조 설계됨. 비중 Y5 4% · 정상상태 약 15%
Distribution
Partner 접촉 없음. Partner 역할·수수료 구조만 설계
Team
[Founder 정보 필요] — 평가 불가
Capital Efficiency
20억 단독 약 19개월. 5년 누적 현금소요 약 128억 (Base)
■ 현재 점수   ■ 24개월 Target 증분 (연주황)   Team은 정보 부재로 Target 미설정
SEED VC 판단
WATCH
현재 17/50 → Target 33/50
INVEST 전환 조건 (최대 5개)
1
Founder: Robot Manipulation × 주방·건축 Integration 역량 보유 Full-time 2인 이상
2
Mock-up: 실제 크기 주방에서 식기 → 식세기 Loading 연속 시연 (영상 + 성공률 Log)
3
WTP 신호: Premium 상담 고객 30명 Interview + 실명 예약금 또는 유료 Pilot 의향 3건 이상
4
표준화 신호: 실제 평면 30개 중 상위 3개 Template이 70% 이상 Cover
5
Channel 신호: 주방가구·Interior 사업자 1곳과 Pilot 시공 협력 합의 (실재)
판단 근거: 진입 방식(구축 Validation → 신축 Scale)·Kill Criteria·BM 구조는 명확. 그러나 Founder·고객·표준화·Channel Evidence가 모두 공백 → 현 시점 20억원 집행 근거 부족
```

**Visual 구성**: 좌측 10개 항목 Scorecard 표 (현재/24개월 Target 점수 막대 + 핵심 Evidence). 우측 판단 박스 WATCH + INVEST 전환 조건 5개.

**Chart / Diagram**: Scorecard Bar + 판단 박스

**Speaker Note**: 실제 Seed 심사역 관점의 점수표입니다. 시장과 접근 방식은 구조가 분명하지만, 고객 수요, 표준화, 유통, 팀은 현재 증거가 없습니다. 그래서 판단은 WATCH입니다. 다섯 가지 증거가 확보되면 INVEST로 바뀔 수 있습니다. Founder 적합성, 실제 크기 Mock-up 시연, 실명 고객의 예약금이나 유료 Pilot 의향, 평면 30개 분석 결과, 실재하는 Partner 협력 합의입니다.

## A23. Sources

**Slide 실제 문구** (화면 표기 순서)

```text
APPENDIX A23
Sources
조회일 2026-10-07 · 검색 결과 기준. 외부 제출 전 원문 대조 필요. 전체 URL: docs/03_Market_Data_and_Sources.md · xlsx Sources 시트
[S1] 총주택 / 아파트 비중 / 준공 20년·30년 이상 비중 / 미거주 주택 — 국가데이터처, 2025 인구주택총조사 결과 (2026.7.28 발표) · newsis.com, fnnews.com
[S2] 아파트 수 / 준공 20년 이상 아파트 (2023) — 통계청 주택총조사 인용 · smarttoday.co.kr
[S3] 2025 주택 준공 / 인허가 / 착공 / 공동주택 분양 — 국토교통부, '25년 12월 주택통계 (2026.1.30) · korea.kr, m-economynews.com
[S4] 아파트 인허가 (2025) — 국토교통부 주택통계 인용 · newsis.com
[S5] 아파트 입주 물량 — v.daum.net
[S6] 주택 매매거래 (2025) — KB주택시장리뷰 2026년 2월호 · kbthink.com
[S7] 국내 리모델링 시장 전망 (건축물 전체, 비주거 포함) — ekn.kr
[S8] 한샘 리하우스 스타일패키지 (전체 리모델링) — dailian.co.kr
[S9] 프리미엄 Kitchen 동향 (한샘 키친바흐·빌트인 가전 연계) — heraldk.com
[S10] 한샘 리하우스 부문 매출 — newstomato.com
[S11] 신축 유상옵션 비용 비중 — etoday.co.kr
[S12] 코웨이 실적·렌탈 계정 — news.bizwatch.co.kr, dealsite.co.kr
[S13] 가전 A/S 출장비 (소비자 부과분) — biz.sbs.co.kr
[S14] 가사서비스 요금 — apps.apple.com, activpayroll.com
[S15] 협동로봇 가격 (Arm + Controller) — standardbots.com, robotomated.com
[S16] Gripper / Fingertip / Food-grade Suction Cup — qviro.com, roboticscenter.ai
[S17] Depth Camera — openelab.com, knoxlabs.com
[S18] Linear Module (소형) — qviro.com
[S19] 1X NEO (가정용 Humanoid) — fastcompany.com
[S20] Sunday Robotics Memo — euronews.com, sacra.com
[S21] LG CLOiD — dezeen.com
[S22] Samsung Bot Handy — sammobile.com
[S23] Moley Robotic Kitchen — thespoon.tech
[S24] Posha (Countertop Cooking Robot) — techcrunch.com
[S25] Tesla Optimus / Figure 03 — notebookcheck.net, getcoai.com
[S26] IFR World Robotics 2025 — Service Robots — ifr.org
[S27] Robot Density (IFR World Robotics 2024) — koreaherald.com
[S28] ISO 10218-1/-2:2025 — sick.com, evsint.com
[S29] TIPS 2026 — unicornfactory.co.kr, venturesquare.net
[S30] 식기세척기 보급률 — etoday.co.kr
[S31] ISO 13482 (Personal Care Robot) 국내 인증 사례 — yujinrobot.com
[S32] 가정용 로봇 인증 동향 — news.mtn.co.kr
```

**Visual 구성**: 출처 목록 2열

**Chart / Diagram**: 없음

**Speaker Note**: 출처는 검색 시점의 보도와 공개 자료입니다. 외부 제출 전에는 국가데이터처와 국토교통부 보도자료 원문으로 다시 확인해야 합니다.
