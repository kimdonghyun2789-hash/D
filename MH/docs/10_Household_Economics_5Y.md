# 10. 5-Year Household Economics

> MH Robotics · Seed 투자 · TIPS 운영사 검토용 IR · Draft v5 · 2026-10-08  
> Concept 단계: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 숫자는 FACT / DERIVED / ASSUMPTION / TARGET, 그림은 CONCEPT로 표기.

## 대표 고객 1세대 정의

- Premium 주방 Remodeling 시점에 MH System을 함께 설치하는 아파트 1세대, **직접 판매 · 구매 · Care 가입**.
- 5년 기대값 (Skill · Tool은 구매율 반영). 원가는 해당 연도 수준을 5년간 적용: **Y3 원가** (첫 상용 단계) · **Y5 원가** (BOM · 설치 · 방문 개선 후).
- 모든 값 만원 · VAT 별도 · 주방 공사비 별도 · DERIVED (from ASSUMPTION). 가격 실측 없음 → 공개가격 · Component Benchmark 기반 ASSUMPTION 범위 (아래 3).

## 1. 대표 1세대 5년 (Remodeling 구매, Y3 원가)

| 매출 (만원) | 5년 |
|---|---:|
| Interface · Integration | 450 |
| Installation · Calibration | 80 |
| Robot System | 1,490 |
| Care (5년) | 240 |
| Consumables (5년, 구매율 반영) | 126 |
| ASSIST Skill (기대값) | 12 |
| Tool · End-effector (기대값) | 20 |
| **5-Year Revenue** | **2,418** |

| 원가 (만원) | 5년 |
|---|---:|
| Interface Kit 원가 | 277 |
| 설치 · Calibration 원가 | 60 |
| 물류 | 25 |
| Skill 원가 | 1.2 |
| Tool 원가 | 9 |
| Robot BOM | 1,180 |
| Warranty Reserve | 59.6 |
| Care 원가 (5년) | 184 |
| Consumables 원가 | 44.1 |
| 채널비용 (획득 · Partner · 수주) | 150 |
| **총원가** | **1,989.9** |

| 산출 항목 | 값 | 정의 |
|---|---|---|
| Initial (INSTALL) | 2,020만원 | Interface 450 + 설치 80 + Robot 1,490 |
| Recurring (OPERATE, 5년) | 366만원 | Care 5 × 48 + 소모품 5 × 70% × 36 |
| Expansion (EXPAND, 5년) | 32만원 | ASSIST Skill 20% × 60 + Tool 25% × 80. COOK Skill · Upgrade = FUTURE (0) |
| 5-Year Revenue | 2,418만원 | 합계 |
| Gross Profit (채널비용 전) | 578만원 (24%) | 매출 − 제품 · 설치 · 서비스 원가 |
| Expected Service Cost | 287.7만원 | Care 원가 + 소모품 원가 + Warranty |
| **Lifetime Contribution** | **428만원 (17.7%)** | Gross Profit − 채널비용 (직접판매 획득비용 150) |

같은 1세대를 **Y5 원가**로 보면: Robot BOM 915 · 설치 38 · Care 원가 134 → Lifetime Contribution **798만원 (33%)**.

## 2. 고객 지불 구조

| 구분 | 구매 | Rental |
|---|---|---|
| 설치 시점 | 2,020만원 | 530만원 (Interface + 설치) |
| 매월 | - | 33만원 × 60개월 (Care Basic · Grip Kit 포함) |
| 매년 | Care 48만원 (선택) · 소모품 약 36만원 (List) | 추가 소모품 (Cleaning · Protection) |
| 5년 총지불 (기대값) | 2,418만원 | 2,605만원 |

가치 Anchor: CLEAN만의 가사 대체 가치 월 약 18만원 (범위 11~24) × 60개월 ≈ 1,080만원 → 구매가보다 낮음. **CLEAN 단독 가치로는 가격을 정당화하지 못할 수 있음** (핵심 미검증 가설 · WTP M18).

## 3. ASSUMPTION 범위 (Scenario, 구매 · Remodeling 직접)

| Scenario | Robot ASP | BOM Y3 / Y5 | 설치 시점 | 5년 매출 | Contribution (Y3 원가) | Contribution (Y5 원가) |
|---|---:|---:|---:|---:|---:|---:|
| Conservative | 1,290 | 1,330 / 1,100 | 1,770만원 | 2,097만원 | -148만원 (-7%) | 149만원 (7%) |
| Base | 1,490 | 1,180 / 915 | 2,020만원 | 2,418만원 | 428만원 (18%) | 798만원 (33%) |
| Upside | 1,490 | 1,100 / 820 | 2,020만원 | 2,418만원 | 592만원 (24%) | 967만원 (40%) |

Conservative (ASP 1,290 · Interface 400 · Care 42만원 · BOM 높음 · 고장 0.9회/년 · 획득비용 180만원)에서는 Y3 원가 기준 **적자**. → 가격 · BOM이 사업성의 1 · 2순위 변수.

## 4. 설치 경로 · 판매 방식별 (만원)

| 경로 | 설치 시점 매출 | 5년 매출 | Gross Profit | Service Cost | Contribution (Y3 원가) | Contribution (Y5 원가) |
|---|---:|---:|---:|---:|---:|---:|
| Remodeling 구매 (직접) | 2,020 | 2,418 | 578 | 288 | 428 (18%) | 798 (33%) |
| Remodeling 구매 (Partner) | 2,020 | 2,418 | 578 | 288 | 376 (16%) | 746 (31%) |
| Remodeling Rental (MH 보유) | 530 | 2,605 | 674 | 285 | 524 (20%) | 925 (36%) |
| Remodeling Rental (Partner 경유 판매) | 530 | 2,605 | 674 | 285 | 472 (18%) | 873 (34%) |
| Retrofit 구매 | 1,760 | 2,158 | 490 | 288 | 314 (15%) | 662 (31%) |
| New-build 구매 | 1,790 | 2,188 | 495 | 288 | 470 (21%) | 807 (37%) |

Rental (MH 보유)은 금융비용을 포함하고 잔존가치 15%를 회수하는 기준. Scale 단계에서는 Partner가 자산을 보유 (09 문서).

## 5. 민감도 (Remodeling 구매 1세대 · Y3 원가 · 기준 428만원)

| 변수 | 불리 | 유리 |
|---|---:|---:|
| Robot ASP (WTP) ±20% | -286 | +286 |
| Robot BOM ±20% | -236 | +236 |
| Interface 가격 ±20% | -90 | +90 |
| 직접판매 획득비용 ±50% | -75 | +75 |
| Failure Rate 0.3 ↔ 1.2회 | -84 | +49 |
| Care 요금 ±20% | -48 | +48 |
| Care 방문 원가 ±30% | -33 | +33 |
| Interface 표준부품 사용률 -15pp/+15pp | -33 | +33 |
| 설치 · Calibration 원가 ±50% | -30 | +30 |
| Consumables 구매율 50% ↔ 90% | -23 | +23 |

## 6. 검증 계획

- Robot ASP · Interface 가격: WTP 조사 n ≥ 300 + 예약금 Test (M18) · 유료 전환 ≥ 2세대 (M24).
- BOM: 100대/년 견적 (M18). 설치 · Care · 고장 원가: 가정 3세대 실측 (M24).
- 소모품 교체주기: Pad 수명 가속시험 (M18~M24).
