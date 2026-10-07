# 05. 5-Year Financial Model (Bottom-up · 3 Scenario)

> ARKI Robotics (가칭) · Seed Investment Proposal · Draft v1 · 2026-10-07 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·Partner 없음.

- 수식 모델: `ARKI/ARKI_Robotics_Financial_Model.xlsx` (Inputs → FM_Conservative / FM_Base / FM_Upside → Scenario_Summary). 1,778개 수식, LibreOffice 재계산 오류 0, `model.py`와 836개 값 교차검증 일치.
- 단위: 억원 (수량 제외). Year 정의: Y1 = Seed 후 M0~M12, Y2 = M12~M24, Y3 = Series A 이후 첫 해.
- 전부 DERIVED (from ASSUMPTION · TARGET). 실적 아님.

## Driver 구조

| Driver | 산식 | 주요 가정 (Base) |
|---|---|---|
| Kitchen Project | 구축 직접 + 구축 Partner + 신축 설치 | 직접 [0, 5, 30, 50, 60] · Partner [0, 0, 20, 130, 340] |
| Robot Unit | 구축 Kitchen × Attach + 신축 설치 × 입주 Attach + Robot-ready Only Pool × 후속 Attach | Attach 85% · 후속 10%/년 · 신축 25% |
| Robot-ready Only | (1 − Attach) 누적 Pool | 후속 Attach 대상 |
| Rental Unit | Robot × Rental 비중; Y2~Y3 ARKI 보유, Y4~ Rental Partner 보유 | Rental 비중 0%, 30%, 30%, 40%, 40% |
| Care / Consumables Base | 평균 가동 대수 × 가입·구매율 × 요금 | Care 가입 70% · Kit 구매 70% |
| Upgrade | 전년 설치 × SW 구매율 × 60만 + 2년 전 설치 × Tool 구매율 × 80만 | SW 20% · Tool 25% |
| 신축 | Project 계약 → 2년 후 입주 설치, Project당 800세대 × Option 선택률 | 계약 [0, 0, 1, 2, 3] · 선택률 10% |
| Cost | Robot BOM · Kitchen Module (Standard Module 사용률 연동) · 설치 · 물류 · Warranty · Care · Consumables COGS · Partner 수수료 · CAC · R&D·Opex | BOM [1600, 1450, 1150, 1000, 900] · SMR ['40%', '50%', '65%', '75%', '80%'] |

## 시나리오 정의

| 변수 | Conservative | Base | Upside | 원칙 |
|---|---|---|---|---|
| Robot ASP (만원) | 1290 | 1490 | 1490 | Upside 가격 인상 없음 |
| Rental 월 요금 (만원) | 29 | 33 | 33 |  |
| Robot BOM Y5 (만원) | 1080 | 900 | 800 | 물량·OEM |
| Standard Module 사용률 Y5 | 65% | 80% | 85% | 표준화 |
| 설치원가 Y5 (만원/대) | 55 | 38 | 30 | Installation Cost 하락 |
| Partner Kitchen Y5 | 150 | 340 | 600 | Partner Distribution 확대 |
| 신축 Project 계약 (Y3~Y5) | [0, 0, 0, 1, 2] | [0, 0, 1, 2, 3] | [0, 0, 2, 3, 4] |  |
| Robot Attach (구축) | 75% | 85% | 85% |  |
| Failure (고장 방문/년) | 0.9 | 0.6 | 0.5 |  |
| Opex | 동일 | 동일 | 동일 | 고정 계획 (인원 6→9→20→32→42명) |

## Base

| 억원 / 수량 | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| 구축 직접판매 Kitchen (세대) | 0 | 5 | 30 | 50 | 60 |
| 구축 Partner Kitchen (세대) | 0 | 0 | 20 | 130 | 340 |
| 신축 Robot-ready 설치 (세대) | 0 | 0 | 0 | 0 | 80 |
| Robot 설치 (대) | 0 | 5 | 42 | 154 | 363 |
| Installed Robot 기말 (대) | 0 | 5 | 48 | 201 | 565 |
| 신축 Backlog (세대) | 0 | 0 | 80 | 240 | 400 |
| Kitchen Build | 0.0 | 0.1 | 2.2 | 8.1 | 19.8 |
| 설치·Calibration | 0.0 | 0.0 | 0.3 | 1.2 | 2.9 |
| Robot Hardware | 0.0 | 0.3 | 4.4 | 21.8 | 51.5 |
| Rental (ARKI 보유) | 0.0 | 0.0 | 0.3 | 0.6 | 0.6 |
| Care | 0.0 | 0.0 | 0.1 | 0.5 | 1.8 |
| Consumables | 0.0 | 0.0 | 0.1 | 0.3 | 0.8 |
| Upgrade | 0.0 | 0.0 | 0.0 | 0.1 | 0.3 |
| **매출** | 0.0 | 0.4 | 7.5 | 32.5 | 77.6 |
| COGS | 0.0 | 0.8 | 5.6 | 22.7 | 49.7 |
| **매출총이익** | 0.0 | -0.3 | 1.8 | 9.8 | 27.9 |
| 매출총이익률 | — | -75% | 25% | 30% | 36% |
| 채널·변동판매비 (Partner·CAC·신축 BD) | 0.0 | 0.1 | 1.0 | 3.5 | 7.6 |
| **Contribution** | 0.0 | -0.4 | 0.8 | 6.4 | 20.3 |
| Opex | 10.2 | 12.8 | 30.5 | 43.9 | 56.7 |
| **영업이익 (근사)** | -10.2 | -13.3 | -29.7 | -37.5 | -36.4 |
| Rental 자산 취득 | 0.0 | 0.2 | 1.5 | 0.0 | 0.0 |
| 누적 현금흐름 | -10.2 | -23.6 | -54.6 | -91.9 | -128.0 |

## Conservative

| 억원 / 수량 | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| 구축 직접판매 Kitchen (세대) | 0 | 4 | 20 | 35 | 40 |
| 구축 Partner Kitchen (세대) | 0 | 0 | 10 | 60 | 150 |
| 신축 Robot-ready 설치 (세대) | 0 | 0 | 0 | 0 | 0 |
| Robot 설치 (대) | 0 | 4 | 22 | 72 | 144 |
| Installed Robot 기말 (대) | 0 | 4 | 26 | 98 | 242 |
| 신축 Backlog (세대) | 0 | 0 | 0 | 48 | 144 |
| Kitchen Build | 0.0 | 0.0 | 1.2 | 3.8 | 7.6 |
| 설치·Calibration | 0.0 | 0.0 | 0.2 | 0.6 | 1.2 |
| Robot Hardware | 0.0 | 0.1 | 2.0 | 8.9 | 17.8 |
| Rental (ARKI 보유) | 0.0 | 0.0 | 0.2 | 0.3 | 0.3 |
| Care | 0.0 | 0.0 | 0.0 | 0.2 | 0.6 |
| Consumables | 0.0 | 0.0 | 0.0 | 0.1 | 0.3 |
| Upgrade | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 |
| **매출** | 0.0 | 0.2 | 3.6 | 13.8 | 27.8 |
| COGS | 0.0 | 0.6 | 3.5 | 12.7 | 23.8 |
| **매출총이익** | 0.0 | -0.4 | 0.2 | 1.1 | 4.0 |
| 매출총이익률 | — | -224% | 5% | 8% | 14% |
| 채널·변동판매비 (Partner·CAC·신축 BD) | 0.0 | 0.1 | 0.5 | 1.9 | 3.7 |
| **Contribution** | 0.0 | -0.5 | -0.4 | -0.7 | 0.3 |
| Opex | 10.2 | 12.8 | 30.5 | 43.9 | 56.7 |
| **영업이익 (근사)** | -10.2 | -13.4 | -30.9 | -44.6 | -56.4 |
| Rental 자산 취득 | 0.0 | 0.2 | 0.9 | 0.0 | 0.0 |
| 누적 현금흐름 | -10.2 | -23.7 | -55.4 | -99.8 | -156.0 |

## Upside

| 억원 / 수량 | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| 구축 직접판매 Kitchen (세대) | 0 | 5 | 35 | 60 | 70 |
| 구축 Partner Kitchen (세대) | 0 | 0 | 30 | 220 | 600 |
| 신축 Robot-ready 설치 (세대) | 0 | 0 | 0 | 0 | 192 |
| Robot 설치 (대) | 0 | 5 | 55 | 239 | 633 |
| Installed Robot 기말 (대) | 0 | 5 | 60 | 299 | 933 |
| 신축 Backlog (세대) | 0 | 0 | 192 | 480 | 672 |
| Kitchen Build | 0.0 | 0.1 | 2.9 | 12.6 | 34.4 |
| 설치·Calibration | 0.0 | 0.0 | 0.4 | 1.9 | 5.1 |
| Robot Hardware | 0.0 | 0.3 | 5.8 | 33.7 | 89.2 |
| Rental (ARKI 보유) | 0.0 | 0.0 | 0.4 | 0.7 | 0.7 |
| Care | 0.0 | 0.0 | 0.1 | 0.8 | 3.0 |
| Consumables | 0.0 | 0.0 | 0.1 | 0.4 | 1.2 |
| Upgrade | 0.0 | 0.0 | 0.0 | 0.1 | 0.4 |
| **매출** | 0.0 | 0.5 | 9.7 | 50.1 | 134.0 |
| COGS | 0.0 | 0.7 | 6.8 | 32.5 | 77.7 |
| **매출총이익** | 0.0 | -0.2 | 2.8 | 17.7 | 56.3 |
| 매출총이익률 | — | -43% | 29% | 35% | 42% |
| 채널·변동판매비 (Partner·CAC·신축 BD) | 0.0 | 0.1 | 1.4 | 5.0 | 11.4 |
| **Contribution** | 0.0 | -0.3 | 1.5 | 12.7 | 44.8 |
| Opex | 10.2 | 12.8 | 30.5 | 43.9 | 56.7 |
| **영업이익 (근사)** | -10.2 | -13.1 | -29.0 | -31.2 | -11.9 |
| Rental 자산 취득 | 0.0 | 0.2 | 1.8 | 0.0 | 0.0 |
| 누적 현금흐름 | -10.2 | -23.5 | -54.2 | -85.1 | -96.6 |

## 해석

- Base Y5 매출 77.6억원, 매출총이익률 36%, Contribution 20.3억원, 영업이익 -36.4억원 → **5년 내 흑자 전환 없음** (Hardware 회사의 일반 경로). 손익분기는 Y5 단가·원가 기준 연 약 1,340세대 (Y6 이후, 신축 Backlog 설치 시점).
- 5년 누적 현금흐름 최저점 (Base): -128.0억원 → 필요 외부자본 = Seed 20억 + TIPS(최대 8억) + Series A 약 80~100억 (Y3~Y4 영업손실 67.2억원 + Buffer) + Series B.
- Conservative: Y5 Contribution 0.3억원 ≈ 0 → 가격·BOM 가정이 깨지면 물량을 늘려도 가치가 생기지 않음 → **Kill Criteria M24 (Scale 투자 보류)** 시나리오.
- Upside: 가격 동일, Partner 물량·표준화·설치원가 차이만으로 Y5 매출 134.0억원, 영업이익 -11.9억원.
- 신축은 계약 후 2년 Lag로 5년 매출 기여가 Y5에 한정 (Base Y5 80세대). Y5 말 Backlog 400세대가 Y6~Y7 매출로 이어짐.
- Revenue Mix (Base Y5): Build 29% · Robot 66% · Recurring 4% · Upgrade 0%. 정상상태(DERIVED) Recurring 약 15% + Upgrade 약 14%.
