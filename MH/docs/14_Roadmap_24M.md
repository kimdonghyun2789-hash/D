# 14. 24개월 Roadmap

> MH Robotics · Seed 투자 · TIPS 운영사 검토용 IR · Draft v5 · 2026-10-08  
> Concept 단계: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 숫자는 FACT / DERIVED / ASSUMPTION / TARGET, 그림은 CONCEPT로 표기.

## 구간별 실행 (TARGET)

| 구간 | 기술 (TIPS WP) | 사업 검증 (Seed) | Gate |
|---|---|---|---|
| 0~6M | Kitchen Task 분석 · Robot Architecture · Hand v1 (M4) · Object Grasp Test (30종, 상용 Gripper 비교) · 초기 Calibration | 리드 3명 채용 · Time-diary 30세대 · 인터뷰 50명 · 평면 30개 분석 · 견적 20건 · 선행기술조사 (M3) | M6 |
| 7~12M | CLEAN Skill · Dishwasher Interaction · Hand v2 (M10) · Safety 기능 · 1:1 Kitchen Mock-up · 목업 CLEAN 전 과정 | 인증기관 사전상담 (M9) · 1순위 특허 2건 출원 · 리모델링 · 렌탈 Partner 탐색 · 사업개발 합류 (M7) | M12 |
| 13~18M | 다양한 Kitchen 적용 (주방 3종) · Task Transfer Test · Failure Recovery · Hand v3 (M18) · Pilot 착수 | WTP 조사 n ≥ 300 · 예약금 Test · 전기 · EMC 사전시험 · BOM 100대/년 견적 · PCT 1건 | M18 |
| 19~24M | Reliability (연속 운전) · Installation Standard · Real-home Pilot 3세대 · BOM · 설치 · Service 원가 실측 | Paid Pilot 전환 · Partner 조건 (리모델링 1 · 렌탈/캐피탈 1) · 출원 누적 5건 · Series A 준비 | M24 |

## Gate · 중단 기준

| Gate | 확인할 Evidence | 통과 기준 (TARGET) | 미달 시 조치 |
|---|---|---|---|
| M6 | Hand v1 vs 상용 Gripper (30종) · Robot Architecture 확정 · 평면 30개 분석 · 인터뷰 50명 | Coverage +15%p 또는 Tool 교체 50% 감소 | 상용 Gripper + 교체형 Pad로 전환 (Buy) · WP1 예산 재배분 |
| M12 | 목업 CLEAN 전 과정 · 식기 성공률 · 안전 기능 · 특허 출원 2건 | 식기 성공률 ≥ 80% · Safety 기능 동작 | Loading 범위로 축소 · Interface 보강 후 재시험 |
| M18 | 주방 3종 Transfer · Calibration 시간 · WTP n ≥ 300 · 예약금 Test · 인증 사전상담 | 하락 ≤ 10%p · Calibration ≤ 4시간 · WTP ≥ 30% (1,490만원) | Retrofit 보류 · Remodeling 집중 / 가격 · 구성 재설계 |
| M24 | 가정 3세대 실증 · 유료 전환 · BOM · 설치 · Service 원가 실측 · Partner 조건 · 출원 5건 | 가정 ≥ 90% · 유료 전환 ≥ 2세대 · 원가가 가정 범위 안 | Bridge 또는 범위 축소 후 재검증 (Series A 연기) |

각 Gate는 "계속 · 범위 축소 · 전환" 중 하나를 결정. 중단 기준이 있어야 초기 자금이 Option 매입으로 작동함.

## WP 일정

| WP | 이름 | 기간 |
|---|---|---|
| WP1 | Adaptive Kitchen Robot Hand | M1~M24 |
| WP2 | Kitchen Manipulation Skill | M3~M24 |
| WP3 | Kitchen Perception / Calibration | M2~M24 |
| WP4 | Minimal Environment Interface | M3~M22 |
| WP5 | Human-Robot Safety | M4~M24 |
| WP6 | Integrated CLEAN 실증 | M9~M24 |

## 채용 계획 (ASSUMPTION, 인물 정보 없음)

| 역할 | 구분 | 시작 | Y1 인건비 (만원) | Y2 인건비 (만원) |
|---|---|:---:|---:|---:|
| 대표 · 사업 총괄 [Founder 정보 필요] | Founder | M1 | 6,000 | 6,000 |
| 공동창업자 · 기술 총괄 [Founder 정보 필요] | Founder | M1 | 6,000 | 6,000 |
| Manipulation · 제어 리드 | R&D | M1 | 9,600 | 9,600 |
| Perception · ML 리드 | R&D | M2 | 8,800 | 9,600 |
| Hand · 기구 리드 (메카트로닉스) | R&D | M2 | 8,800 | 9,600 |
| 임베디드 · 전기 · 안전 | R&D | M4 | 5,850 | 7,800 |
| Robot SW · 통합 (Motion · Skill) | R&D | M6 | 4,550 | 7,800 |
| 제품 · 사업개발 (고객 검증 · 파트너) | 사업 | M7 | 3,600 | 7,200 |
| Hand 센싱 (Grip Force · Slip) | R&D | M10 | 1,950 | 7,800 |
| 경영지원 (재무 · 과제 관리, 0.5 FTE) | 경영지원 | M10 | 675 | 2,700 |
| 시험 · 신뢰성 (Test · QA) | R&D | M13 | 0 | 7,800 |
| 설치 · Commissioning 엔지니어 | 현장 | M13 | 0 | 6,600 |
| Skill · Data 엔지니어 | R&D | M16 | 0 | 5,850 |
| 현장 서비스 Technician | 현장 | M19 | 0 | 2,700 |

평균 FTE 7.0 (Y1) → 12.8 (Y2) · 24개월 차 약 14명. Lean안: Hand 센싱 · Skill/Data · 현장 Technician 제외, 시험 인력 M19로 연기 (24개월 차 약 10명).

## 24개월 Value Creation

| 단계 | 내용 |
|---|---|
| TODAY | Concept · Technology Hypothesis · Business Hypothesis (시제품 · 고객 · 매출 없음) |
| Seed + TIPS (24개월) | 23.4억원 지출 · 24개월 차 약 14명 |
| 24M TARGET — 기술 | Working Kitchen Prototype · Adaptive Robot Hand · Manipulation Skill Library · Calibration System · Safety Architecture · Multiple Kitchen Test · Task Transfer Evidence |
| 24M TARGET — 경제성 | Robot BOM (100대/년 견적) · Installation Cost · Service Cost (가정 3세대 실측) |
| 24M TARGET — 시장 | Customer WTP (n ≥ 300) · Pilot · Paid Pilot (≥ 2세대) · Partner Evidence · Patent 출원 5건 + PCT 1건 |
| NEXT ROUND | Productization · Production · Distribution · Scale (Series A 판단 기준 = 기술 성공 + 유료 전환 + 원가 실측) |
