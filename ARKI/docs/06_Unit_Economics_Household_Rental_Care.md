# 06. Household · Rental · Care · Consumables Economics

> ARKI Robotics (가칭) · Seed 투자 제안서 · Draft v3 · 2026-10-07 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·Partner 없음.

수식: xlsx `Household` · `Unit_Economics` · `Sensitivity` 시트. 전부 DERIVED (from ASSUMPTION). 단위 만원.

## 1. 가격 가설 (Purchase · Rental)

| 근거 | 내용 | Tag |
|---|---|---|
| Cost Floor | Robot BOM 1,150 (Y3) / 900 (Y5) → GM 30% Robot 가격 1,643 / 1,286만원 · Rental 마진 20% 요금 월 31.3 / 24.4만원 | DERIVED |
| Market Reference | 1X NEO $20,000 또는 월 $499 · Sunday Memo 양산 $10k 미만 목표 · Moley £248,000 · 신축 유상옵션 분양가의 9.7% · 30평대 전체 리모델링 약 3,000만원(2019) | FACT |
| Value Anchor | Clean-up 40분/일 (A) × 30일 × 가사서비스 1.5만원/h (F) × 자동화 60% (A) = 월 18만원 (Range 11~24) | DERIVED |
| 가격 가설 (구매) | Robot-ready 450 + Robot 1,490 + 설치 80 = ARKI 2,020만원 (Kitchen 공사비 별도) | ASSUMPTION |
| 가격 가설 (Rental) | Robot-ready 450 + 설치 80 + 월 33만원 × 60개월 (Care Basic · Grip Kit 포함) | ASSUMPTION |
| WTP Test Point | Robot 990 / 1,290 / 1,490 / 1,790만원 · Rental 월 19 / 25 / 29 / 33 / 39만원 | TARGET (조사 설계) |

**핵심 Gap**: 가치 Anchor(월 11~24만원) < 원가 기반 Rental(월 24~31만원). V1 단일 Task의 "가사 대체 가치"만으로는 가격 정당화가 어려움 → (1) Premium Kitchen Amenity로서의 가치 (2) V2 Task 확장 (3) BOM 절감이 필요하며, WTP 검증이 Seed 1순위.

## 2. Household Economics — 구축 Premium 1세대 · 5년 · 직접판매

구매 모델은 Care 가입 세대 기준, Software·Tool은 구매율 반영 기대값. Rental은 ARKI 자산 보유 가정 (잔존가치 15% 회수, 금융비용 8%).

| 만원 | 구매 · Y3 원가 | 구매 · Y5 원가 | Rental · Y3 원가 | Rental · Y5 원가 |
|---|---|---|---|---|
| Robot-ready Kitchen 증분 | 450 | 450 | 450 | 450 |
| 설치·Calibration | 80 | 80 | 80 | 80 |
| Robot (구매) | 1,490 | 1,490 | 0 | 0 |
| Rental 60개월 | 0 | 0 | 1,980 | 1,980 |
| Care Basic 5년 | 240 | 240 | 0 | 0 |
| Consumables 5년 | 126 | 126 | 63 | 63 |
| Software Skill (기대값) | 12 | 12 | 12 | 12 |
| Tool (기대값) | 20 | 20 | 20 | 20 |
| **5년 매출** | 2,418 | 2,418 | 2,605 | 2,605 |
| Kitchen Module 원가 | 277 | 244 | 277 | 244 |
| Robot BOM (Rental: 순감가) | 1,150 | 900 | 978 | 765 |
| Rental 금융비용 | 0 | 0 | 264 | 207 |
| 설치·Calibration 원가 | 60 | 38 | 60 | 38 |
| 물류 | 25 | 25 | 25 | 25 |
| Warranty Reserve | 60 | 60 | 46 | 36 |
| Care 원가 5년 | 184 | 134 | 184 | 134 |
| Consumables 원가 | 44 | 44 | 54 | 54 |
| Upgrade 원가 | 10 | 10 | 10 | 10 |
| 획득비용 (CAC) | 150 | 150 | 150 | 150 |
| **5년 매출총이익 (CAC 전)** | 608 | 963 | 707 | 1,092 |
| **Lifetime Contribution** | 458 | 813 | 557 | 942 |
| Contribution Margin | 18.9% | 33.6% | 21.4% | 36.2% |

- 구매 · Y3 원가: Year 0 매출 2,020만원이 5년 매출의 84% → 세대 경제성은 **Robot ASP(WTP) × BOM**이 결정.
- Recurring(Care+Consumables) 5년 366만원 → 보완 역할, 핵심 Value Driver 아님.
- Partner 경유 시 Contribution 약 52만원 감소 (수수료 10%).

## 3. Unit Economics 요약

| Unit | Y3 원가 | Y5 원가 | 조건 / 해석 |
|---|---|---|---|
| Purchase Year-0 Contribution (CAC 포함) | 298 | 603 | BOM 하락이 핵심 |
| Rental 월 Contribution · Margin | 7.9 · 24% | 13.4 · 41% | 월 33만원 기준 |
| Rental Payback (개월) | 39 | 30 | Partner 허들 36개월 → BOM ≤ 1,059만원 |
| Care Contribution · Margin (연) | 11.2 · 23% | 21.2 · 44% | 방문 1.5회 이하 · 방문원가 9만원 이하 |
| Consumables Contribution · Margin (연) | 16.4 · 65% | 16.4 · 65% | 교체주기 미실측 |

## 4. Rental Economics

| 월 원가 Build-up (Robot 1대) | Y3 | Y5 |
|---|---|---|
| 감가 (BOM × 85% ÷ 60) | 16.29 | 12.75 |
| 금융비용 (평균잔액 × 8% ÷ 12) | 4.41 | 3.45 |
| Care 원가 ÷ 12 | 3.07 | 2.23 |
| Grip Kit 원가 ÷ 12 | 0.53 | 0.53 |
| Failure Reserve (BOM × 4% ÷ 60) | 0.77 | 0.60 |
| **월 원가** | 25.06 | 19.56 |
| 월 요금 (가정) | 33.0 | 33.0 |
| **월 Contribution** | 7.94 | 13.44 |
| 마진 20% 확보 요금 | 31.3 | 24.4 |
| Payback (개월, 금융 제외) | 39.1 | 29.8 |
| 36개월 Payback 최대 BOM | 1,059 | 1,089 |

- 구조: Seed = ARKI 직접 Rental Pilot (소량) · Scale(Y4~) = Rental / Capital Partner가 Robot을 ASP의 88%(1,311만원)에 매입하고 월 27만원 순유입 · 잔존 197만원 → Partner IRR 약 13.1% (Conservative 12.4%). 연체·중도해지·회수비용 미반영.
- 결론: Y3 원가로는 Payback 39개월 > 36개월 → **Rental은 BOM ≤ 1,059만원 달성 전까지 Pilot 규모로 제한**.

## 5. Care Economics

| Care Basic (Robot 1대·년) | Y3 | Y5 | Tag |
|---|---|---|---|
| 요금 | 48 | 48 | ASSUMPTION |
| 정기 방문 (횟수 × 원가) | 22.0 | 12.0 | ASSUMPTION (Y3 2회×11만, Y5 1.5회×8만) |
| 고장 방문 (0.6회 × 18만원) | 10.8 | 10.8 | ASSUMPTION |
| Cloud·Software | 4.0 | 4.0 | ASSUMPTION |
| **Contribution · Margin** | 11.2 · 23% | 21.2 · 44% | DERIVED |

- 포함: 정기 안전점검 · Calibration · Remote Diagnosis · Joint / Rail / Vision 상태 · Consumables Check · Software Update · A/S 공임.
- 참고 (FACT): 삼성·LG 가전 A/S 출장비 2.8만원 (2026, 소비자 부과분) — ARKI 실제 방문 원가(인건비·이동)와 다름.
- Care가 Profit Center가 되는 조건: 원격진단으로 정기방문 1.5회 이하 + Route Density로 방문원가 9만원 이하 → Y5 Margin 44%. Y3에는 Profit Center 아님.

## 6. Consumables Economics

| Kit | 구성 | 가격(만원) | 교체/년 | 연 List |
|---|---|---|---|---|
| Grip Kit | Finger Pad · Food-contact Tip · Suction Cup | 4.5 | 4 | 18 |
| Cleaning Kit | Brush · Wiper · Cleaning Pad | 2.5 | 4 | 10 |
| Protection Kit | Sensor Cover · Protective Sleeve · Seal | 4 | 2 | 8 |
| 합계 |  |  |  | 36 |

- 구매율 70% → 연 매출 25.2만원 · 원가 35% → Contribution 16.4만원/Robot.
- 설계 원칙: 억지 Lock-in이 아니라 위생 · 마모 · Grip 성능 유지 · 식품접촉부 교체 · 안전성 유지. Care Plus(연 72만원)에 정기 교체 포함 가능.
- 검증 KPI: Replacement Cycle · Cost per Kit · Annual Consumables Revenue per Robot · Gross Margin · Care Attach Rate.

## 7. 5-Year Household Economics 요약 (대표 1세대)

|  | 구매 · Y3 원가 | 구매 · Y5 원가 | Rental · Y3 원가 | Rental · Y5 원가 |
|---|---|---|---|---|
| Initial (Kitchen Module + Robot / 설치) | 2,020 | 2,020 | 530 | 530 |
| Recurring (Rental 또는 Care + Consumables) | 366 | 366 | 2,043 | 2,043 |
| Expansion (Tool · Software 기대값) | 32 | 32 | 32 | 32 |
| 5-Year Revenue | 2,418 | 2,418 | 2,605 | 2,605 |
| 5-Year Gross Profit | 608 | 963 | 707 | 1,092 |
| Expected Service Cost (Care 원가 5년) | 184 | 134 | 184 | 134 |
| Lifetime Contribution | 458 | 813 | 557 | 942 |

## 8. Sensitivity (Top 3 Critical Variable = Customer WTP · Robot BOM · Partner Distribution)

세대 5년 Contribution (구매·Y3, Base 458만원):

| 변수 | 불리 Δ (만원) | 유리 Δ (만원) |
|---|---|---|
| Robot ASP (WTP) ±20% | -286 | +286 |
| Robot BOM ±20% | -230 | +230 |
| Robot-ready 증분가 ±20% | -90 | +90 |
| 직접판매 획득비용 ±50% | -75 | +75 |
| Failure Rate 0.3 ↔ 1.2회 | -84 | +49 |
| Care 요금 ±20% | -48 | +48 |
| 방문 원가 ±30% | -33 | +33 |
| Standard Module 사용률 -15pp/+15pp | -33 | +33 |
| 설치 원가 ±50% | -30 | +30 |
| Consumables 구매율 50% ↔ 90% | -23 | +23 |

회사 Y5 Contribution (Base 20.3억원):

| 변수 | 불리 Δ (억원) | 유리 Δ (억원) |
|---|---|---|
| Customer WTP (Robot ASP·증분가 ±20%) | -12.3 | +12.3 |
| Robot BOM ±20% | -6.6 | +6.6 |
| Partner 경유 Kitchen ±30% | -4.8 | +4.8 |
| Robot Attach Rate 65% ↔ 95% | -3.1 | +1.6 |
| Failure Rate 0.3 ↔ 1.2회 | -1.4 | +0.9 |
| Rental 비중 20% ↔ 60% | -1.1 | +1.1 |
| Standard Module 사용률 -15pp/+10pp | -1.3 | +0.9 |
| 신축 Option 선택률 5% ↔ 15% | -0.8 | +0.8 |
| 설치 원가 ±50% | -0.7 | +0.7 |
| Service 원가 (방문) ±30% | -0.1 | +0.1 |
