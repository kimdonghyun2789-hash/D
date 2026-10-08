# 02. Main IR Deck — 구성

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

- 제출용: `MH/MH_Robotics_Seed_TIPS_IR_Final.pptx` (본문 18장 + 부록 28장 + 목차, 16:9) · 본문 PDF `MH_Robotics_Seed_TIPS_IR_Final_Main.pdf` · 전체 PDF `MH_Robotics_Seed_TIPS_IR_Final.pdf`
- 내부 검토용 (제출 제외): `MH/MH_Robotics_IR_Internal_QA.pptx` · `.pdf` (7장)
- 화면 문구 [03](03_Slide_Text.md) · Visual [04](04_Slide_Visual.md) · Diagram / Chart [05](05_Diagram_Chart.md) · 발표 요지 [06](06_Speaker_Notes.md)

## 흐름

- **Why: 문제와 첫 적용 공간**: 02~04쪽
- **How: 기술 전략과 제품**: 05~09쪽
- **Business: 적용 경로 · BM · 시장 · GTM**: 10~13쪽
- **Proof: 경제성 연결 · 경쟁 · 실행 계획**: 14~16쪽
- **Ask: 팀과 투자 요청**: 17~18쪽

## 본문 18장

| No | 구성 | 화면 제목 | 부제 | 예상 질문 (내부 Q#) |
|---|---|---|---|---|
| 01 | MH Robotics · Kitchen Manipulation Robotics System | MH Robotics — Kitchen Manipulation Robotics System | 로봇손 · 작업 Skill · Calibration · 주방 Interface 통합 제품 | - |
| 02 | 가전 자동화 이후 남은 Physical Workflow | 가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workflow | 개별 가전 기능은 자동화 · 주방 Workflow 전체의 Physical Manipulation은 아직 사람 몫 | Q3 |
| 03 | 왜 Kitchen인가 | 주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간 | Robot Engineering 4개 기준 · Business 4개 기준 | Q1, Q4 |
| 04 | 가정용 Robot 적용의 구조적 한계 | 주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계 | Robot 지능 부족만이 아닌 높은 환경 편차 (Environment Variation) → 신뢰성 · 반복설치 제약 | Q7 |
| 05 | MH Robotics Technology Strategy | Robot 적응 + 반복 작업점에만 최소 Interface | Robot Hand · Manipulation Skill · Calibration · Environment Interface 통합 설계 | - |
| 06 | Adaptive Kitchen Robot Hand | 핵심 Hardware: 주방 물체 대응 Adaptive Robot Hand | 손가락 수 · 자유도 경쟁이 아닌 작업 완료율 · 가격 · 위생 · 유지관리 · 내구성 중심 | Q6, Q13 |
| 07 | Manipulation Skill / Calibration | 핵심 기술: Calibration 기반 Skill의 주방 간 이전 | Skill = Robot이 수행 가능한 작업을 늘리는 확장 Layer (Software 구독 아님) | Q7 |
| 08 | MH Kitchen Robotics System | MH Kitchen Robotics System: 5개 Layer 통합 제품 | 왜 Arm: 식세기 랙 · 서랍 · 상부장 작업 = 6축 방향 제어 필요 · 이동형 = 낮은 작업점 · 가격 · 안전 부담 | Q2, Q16 |
| 09 | 첫 검증 Workflow: CLEAN → ASSIST → COOK | CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장 | 단계별 새 로봇 개발이 아닌, 같은 Platform에 Skill · Tool 추가 | Q5 |
| 10 | Existing / Remodeling / New-build 적용 | 단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · 신축) | 주방 전체 획일화 없이 Integration 수준만 차등 적용 | Q8, Q9 |
| 11 | Business Model | 설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM | INSTALL → OPERATE → EXPAND · Hardware 외 매출 = 실제 유지관리 · 기능가치 기반 | Q4, Q11, Q12, Q13 |
| 12 | Market / Beachhead | Bottom-up 시장 산정: 세대 수 × 적용률 × 단가 | 아파트 재고 = 기회 기반 (구매시장 아님) · 비율 = ASSUMPTION (검증 계획 부록 C3) | - |
| 13 | GTM / Partner Distribution | Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장 | 초기 Mass Market 진입 없음 · 검증 채널 (Remodeling) → 고객 확대 (Retrofit) → Scale 채널 (신축) | Q9 |
| 14 | Technology-to-Economics / Moat | R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조 | 성능 향상 자체가 아닌 Unit Economics · Scale 개선으로 연결 | Q10 |
| 15 | IP / Competition | 경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증 | 가전사 · 가구사 직접 진입 가능 (LG CLOiD 2028 목표) → Interface · 시공 Partner 후보로 설계 | Q14, Q15, Q17 |
| 16 | TIPS R&D / 24개월 Roadmap | TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발 | TIPS 과제 10.67억원 = WP1~6 기술 검증 · Seed = 기관부담금 · 과제 외 인건비 · 고객 · 실증 · 사업 검증 | Q19 |
| 17 | Founder / Team | Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획 | 필요 역량 = 로봇 조작 (Hand · Skill) · 주방 · 건축 설치 · 고객 · Partner 영업 | Q20 |
| 18 | Investment Ask / 24M Value Creation | 24개월 사용 23.4억원 · Seed 14~19억원 요청 (TIPS 8억원 별도) | Bottom-up 사용처 산정 · Seed 범위 = Lean (팀 · 범위 축소) ~ Base (기술 + 사업 검증 + 3개월 Buffer) | Q18, Q19 |

## 부록 (근거 · 계산 · 검증 계획)

| Code | 제목 |
|---|---|
| A1 | 기술 KPI (1/3) · Manipulation |
| A2 | 기술 KPI (2/3) · Application |
| A3 | 기술 KPI (3/3) · Business |
| A4 | R&D Work Package 상세 (TIPS 과제) |
| A5 | Gate · 중단 기준 (24개월) |
| A6 | TIPS 과제 편성 · 24개월 사용처 (Base) |
| A7 | 24개월 팀 계획 (채용 계획, ASSUMPTION) |
| B1 | Adaptive Hand 시험 계획 (Buy vs Build) |
| B2 | Kitchen Variation 근거: 확보 평면 5종 |
| B3 | Environment Interface 예: Robot Home 보관 · 전개 (Remodeling) |
| B4 | 대표 평면 적용 예: 구축 2Bay A (CONCEPT) |
| B5 | Safety · Certification 경로 |
| B6 | Robot System BOM · Component Benchmark |
| C1 | Housing · 시장 통계 |
| C2 | Remodeling · Rental · Care Reference |
| C3 | Market Sizing 산식 · 검증 계획 |
| C4 | 경쟁사 상세 (공개 자료) |
| D1 | 가격 가설: 원가 Floor · 시장 Reference · 가치 Anchor |
| D2 | Household 5년 경제성 상세 (1세대 · 만원 · Base) |
| D3 | Rental · Care · Consumables 단위 경제성 (Base) |
| D4 | 5-Year Financial Model (3 Scenario) |
| D5 | Sensitivity |
| E1 | IP Portfolio 상세 (출원 후보 · 등록 미정) |
| E2 | Risk Register: Risk → Evidence → 대응 → 중단 기준 |
| F1 | Sources (1/4) |
| F2 | Sources (2/4) |
| F3 | Sources (3/4) |
| F4 | Sources (4/4) |

## 내부 검토용 (제출 제외)

| Code | 제목 |
|---|---|
| I0 | IR 내부 검토용 자료 (제출 제외) |
| I1 | 투자심사 예상질문 · 방어논리 (1/3) |
| I2 | 투자심사 예상질문 · 방어논리 (2/3) |
| I3 | 투자심사 예상질문 · 방어논리 (3/3) |
| I4 | 현재 부족한 Evidence · Founder 입력 필요 정보 |
| I5 | 투자심사 Memo: MEET |
| I6 | Number Tag 원칙 |
