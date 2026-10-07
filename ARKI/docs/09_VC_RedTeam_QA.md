# 09. VC 예상질문 · Red-Team 답변

> ARKI Robotics (가칭) · Seed 투자 제안서 · Draft v3 · 2026-10-07 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·Partner 없음.

실제 Seed 심사역 관점의 25개 질문. "답의 강도"가 약한 항목은 본문에서 숨기지 않고 표기했고, Investment Memo의 Reasons Not to Invest와 연결됨.

| # | 질문 | 답 (근거 Slide) | 답의 강도 | 보완 Evidence |
|---|---|---|---|---|
| 1 | 왜 Robot Arm인가? | 식기 형상·위치가 매번 다름 → 고정 기구로 불가. 단, Arm 범위는 Rail·Dock으로 제한해 범용성보다 신뢰성 우선 (B4). | 보통 | — |
| 2 | 기존 Appliance로 해결 불가능한가? | 가전은 내부 공정만 자동화. 식탁→식세기→수납 이동은 가전 경계 밖 (02장). 가전사 확장 가능성은 Risk로 인정. | 보통 | — |
| 3 | 왜 Kitchen Clean-up인가? | 매 식사 반복 · 열·칼 위험 없음 · 식세기·수납이라는 고정 끝점 → 표준화 용이. 체감가치는 Cooking보다 낮음 (B3). | 강함 | — |
| 4 | 돈을 낼 만큼의 Pain인가? | 미검증. 가치 Anchor 월 11~24만원 < 원가 기반 Rental 24~31만원 → Gap 존재. Time-diary·WTP로 M12 판정 (D1). | 약함 | Time-diary 30세대 + PSM/Conjoint + 예약금 |
| 5 | Robot 가격은 얼마인가? | 가설 1,490만원 (Test 990~1,790). Y3 BOM 1,150만원 → GM 23% (D5·D6). | 보통 | — |
| 6 | Remodeling 포함 총 고객비용은? | Kitchen 공사비 (Premium 2,000~4,000만원, ASSUMPTION) + ARKI 2,020만원. 증분 부담 큼 → Rental·신축 Option 병행 (D1). | 약함 | Kitchen 견적 20건 + 총비용 기준 WTP 문항 |
| 7 | Rental은 얼마여야 하는가? | 원가 기반 마진 20% 요금: Y3 31만원 · Y5 24만원. 가설 33만원. Partner Payback 36개월 위해 BOM ≤ 1,060만원 (D7). | 보통 | — |
| 8 | Care는 왜 필요한가? | Calibration·Rail·Vision 점검과 위생 관리가 안전·성능 유지 조건. Software 구독 아님 (D8). | 보통 | — |
| 9 | Consumables는 실제로 얼마나? | 가설 연 36만원 List, 구매율 70% → 25만원. 교체주기 미실측 (D8). | 약함 | Pilot 세대 Kit 교체주기 실측 |
| 10 | Robot 고장 시 Kitchen 사용 가능한가? | 설계 Requirement: Garage 복귀·수동 해제·일반 Kitchen 기능 유지 (B4 #07, B17). | 보통 | — |
| 11 | 머리 위 Robot은 안전한가? | 사람 위 운반 금지 · Zone 진입 정지 · 1.5kg 이하 · ISO 10218:2025 · 13482 검토. 인증은 Series A (B17). | 보통 | — |
| 12 | 집마다 다른데 표준화 가능한가? | 가설. 4단계 분류 + 평면 30개로 M12 판정, Standard Module 60% 미만 시 재검토 (B13). | 약함 | 평면 30개 분석 결과 |
| 13 | Bay보다 Geometry가 중요한가? | Robot 설치는 주방 Run·설비 위치·Aisle이 결정, Bay는 거실·침실 배치 변수 (B12). | 강함 | — |
| 14 | 공사업체가 되는 것 아닌가? | 철거·가구·전기·배관 = Partner. ARKI = Module·Calibration·Safety QA. KPI: Build 비중 Y5 29% (C5). | 보통 | — |
| 15 | 왜 구축부터인가? | 이미 철거·시공하는 고객 → 추가 Integration 비용 최소 · 가격·설치 직접 검증 · 신축은 2년 Lag (C4). | 강함 | — |
| 16 | 왜 신축이 Scale Channel인가? | Project당 수백 세대 · 설계 단계 표준 Spec · 유상옵션 관행 (분양가 9.7%). 단, 매출 인식 지연 (C4). | 보통 | — |
| 17 | 건설사가 직접 하면? | 건설사는 Robot·SW·A/S 운영 역량보다 유통 역할. ARKI Spec을 Option으로 채택하는 Distribution 관계 (C6). | 보통 | — |
| 18 | Kitchen Furniture 회사가 직접 하면? | 가장 현실적 위협. Module·Channel Partner로 협력하되 Template·설치 Data·Calibration SW로 차별 (미검증). | 약함 | 가구사 2~3곳 Partner 조건 탐색 · 독점/비독점 구조 |
| 19 | Robot OEM이 직접 하면? | OEM은 Arm 판매가 목적, 주거 설치·A/S·가구 Interface는 비핵심 → Supplier 관계 (C6). | 보통 | — |
| 20 | Rental Asset 부담은? | Seed는 소량 Pilot만 ARKI 보유. Y4부터 Rental Partner가 자산 보유, Partner IRR 약 13% (연체 미반영, D7). | 보통 | — |
| 21 | A/S 비용은? | Y3 Robot당 연 36.8만원 (방문 2회 × 11만원 + 고장 0.6회) → Y5 26.8만원 (D8). | 보통 | — |
| 22 | Care가 Profit Center가 될 수 있는가? | Y3 Margin 23% → 아님. 방문 1.5회 이하·원가 9만원 이하에서 Y5 44%. Route Density 의존. | 보통 | — |
| 23 | 20억원이 충분한가? | 아니오. 24개월 수정안 약 25.8억원 → TIPS 8억 연계 또는 25억원 / M18 Bridge (D11). | 약함 | TIPS 운영사 접촉 · Plan B 확정 |
| 24 | 24개월 후 Series A Evidence는? | Paid Pilot · WTP · BOM ≤ 1,150만원 경로 · Template 3개 70% Cover · 설치 1일 · Partner Pilot (E3). | 보통 | — |
| 25 | Founder가 왜 적합한가? | [Founder 정보 필요] — 현재 답할 수 없음. 투자 판단 1순위 공백 (14장). | 약함 | Founder 정보 입력 |

## Red-Team 결과 본문 반영 내역

| 약점 | 반영 위치 |
|---|---|
| 가치 Anchor(월 11~24만원) < 원가 기반 Rental(월 24~31만원) | D1 Gap Statement · A1 Q2 |
| Rental Payback Y3 39개월 > 36개월 | D4 하단 · D7 결론 |
| Care는 Y3에 Profit Center 아님 | D4 · D8 |
| Seed 20억원 24개월 부족 | 15장 · D11 |
| 신축 매출 2년 Lag | C4 Timing |
| Founder 정보 공백 | A2 · 14장 · A4 |
| 범용 Humanoid의 월 $499 구독가 | C6 · C7 시사점 |
