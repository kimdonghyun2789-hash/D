# 09. Business Model

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

## 한 줄 정의

INSTALL (Robot System · Interface · 설치) → OPERATE (Rental · Care · 소모품 반복매출) → EXPAND (같은 Platform에 Skill · Tool 추가). Installed Base 증가 → 반복 · 확장 매출 비중 확대 구조 (가설)

## 3단계 구조 (가격 = ASSUMPTION, VAT 별도)

| 층 | 항목 | 가격 가설 | 근거 · 비고 |
|---|---|---|---|
| INSTALL | Robot System (Arm · Adaptive Hand · Vision · Safety) | 1,490만원 | BOM Y3 1,180 → Y5 915만원 · Hardware 마진 21% → 39% |
| INSTALL | Interface · Integration | Retrofit 150 · Remodeling 450 · New-build Option 220만원 | Robot Home · Rail · 식세기 Interface · Dock · Vision 기준점 (경로별 수준 다름) |
| INSTALL | Installation · Calibration · Safety Check | 80만원 (Retrofit 120) | 원가 Y3 60만원 (약 18인시) |
| OPERATE | Robot Rental (60개월, Care Basic · Grip Kit 포함) | 월 33만원 | 월 원가 Y3 25.6 → Y5 19.8만원 |
| OPERATE | Care (Robot Lifecycle Maintenance) | 연 48만원 | 원가 Y3 36.8 → Y5 26.8만원 · 가입률 70% |
| OPERATE | Consumables (Grip · Cleaning · Protection Kit) | 연 36만원 (정가) | 구매율 70% · 원가율 35% |
| EXPAND | ASSIST Skill Pack (설치 다음 해) | 60만원 | 구매율 20% (FUTURE: ASSIST 출시 전제) |
| EXPAND | Tool · End-effector (설치 2년 후) | 80만원 | 구매율 25% |
| EXPAND | COOK Skill · Robot Upgrade | FUTURE | 5년 Base 매출 미반영 |

## 가격 가설의 범위 (원가 Floor · 시장 Reference · 가치 Anchor)

| 항목 | 가격 가설 | 원가 Floor (DERIVED) | 시장 Reference (FACT) | 가치 Anchor |
|---|---|---|---|---|
| Robot System | 1,490만원 | BOM Y3 1,180 → Y5 915만원 (Hardware 마진 21% → 39%) | 1X NEO $20,000 (약 2,800만원) · Sunday Memo 목표 $10k 미만 · UR3e $23k~33k | 가사 대체 월 약 18만원 × 60개월 ≈ 1,080만원 |
| Interface · Integration (Remodeling) | 450만원 | Kit 원가 Y3 약 277만원 (표준부품 65%) | Premium 주방 2,000~4,000만원의 11~23% (ASSUMPTION) · 신축 유상옵션 분양가 대비 9.7% (FACT) | 주방 공사와 동시 시공 → 별도 공사 회피 |
| Installation · Calibration | 80만원 (Retrofit 120) | 원가 Y3 60만원 (약 18인시) | 가전 출장비 2.8만원 (소비자 부과, 비교 불가) [S13] | - |
| Rental | 월 33만원 (60개월) | 월 원가 Y3 25.6만원 (마진 20% 요금 32.0만원) | 1X NEO 월 $499 (약 70만원) | 가사 대체 월 약 18만원 → Gap |
| Care | 연 48만원 | 원가 Y3 36.8 → Y5 26.8만원 | LG 구독 정기관리 포함 (가격 구조 비공개) | 안전 · 성능 유지 |
| Consumables | 연 36만원 (정가) | 원가율 35% | Robotiq Fingertip $175~195 · 식품용 실리콘 컵 £7~20 | 위생 · 마모 교체 |

**가치 Gap**: CLEAN만의 가사 대체 가치 = 월 약 18만원 (정리 40분/일 × 60% 자동화 × 가사서비스 1.5만원/h, 범위 11~24만원) < Rental 월 33만원. → Premium Remodeling 고객부터, ASSIST 확장 · 위생 · 편의 가치를 묶어 WTP 조사 (n ≥ 300 · 예약금, M18)

## 설치 경로별 세대당 경제성 (구매, 5년, 만원)

| 경로 | 설치 시점 매출 | 5년 매출 | 5년 공헌이익 (Y3 원가) | 5년 공헌이익 (Y5 원가) |
|---|---:|---:|---:|---:|
| Existing Retrofit | 1,760만원 | 2,158만원 | 314만원 (15%) | 662만원 (31%) |
| Remodeling (직접) | 2,020만원 | 2,418만원 | 428만원 (18%) | 798만원 (33%) |
| Remodeling (Partner 경유) | 2,020만원 | 2,418만원 | 376만원 (16%) | 746만원 (31%) |
| New-build (Option 세대 · 입주 후 Robot) | 1,790만원 | 2,188만원 | 470만원 (21%) | 807만원 (37%) |
| Remodeling Rental (MH 보유) | 530만원 | 2,605만원 | 524만원 (20%) | 925만원 (36%) |

Retrofit은 Partner 수수료 · 현장 Calibration 비용 때문에 낮고, New-build는 Project 수주비용이 세대당 작아 높음. 상세: [10_Household_Economics_5Y.md](10_Household_Economics_5Y.md)

## Rental 구조 (초기 부담 완화 수단)

- **Pilot (Y2~Y3)**: MH가 직접 보유 · 운영 (실증 3세대 + 초기 고객)
- **Scale (Y4~)**: Rental · Capital Partner가 Robot 자산을 ASP의 88%에 매입 · 보유, 고객은 Partner에 월 33만원, MH는 Product · SW · Care 담당 + 서비스료 월 6만원
- Partner 관점: 매입가 1,311만원 · 월 순유입 27만원 · 60개월 · 잔존 15% → 연 IRR 약 13.1% · 단순 회수기간 약 49개월 (DERIVED)
- 회수 약 49개월 > Partner 요구 36개월 (ASSUMPTION) → 매입가율 · 서비스료 · 계약기간 조건 협의 필요 (M24 Partner 조건)
- MH Balance Sheet의 Rental 자산 누적 지양 (Scale 단계 Partner 보유)

| Rental 월 단위 (만원) | Y3 | Y5 |
|---|---:|---:|
| 감가 (잔존 15%) | 16.7 | 13.0 |
| 금융비용 (연 8%) | 4.5 | 3.5 |
| Care 원가 | 3.1 | 2.2 |
| Grip Kit 원가 | 0.5 | 0.5 |
| Failure Reserve | 0.8 | 0.6 |
| **월 원가 합계** | 25.6 | 19.8 |
| 월 요금 | 33 | 33 |
| **월 공헌이익** | 7.4 | 13.2 |
| Payback (개월) | 40 | 30 |

## Care = Robot Lifecycle Maintenance (Software 구독 아님)

포함: 정기 안전점검 · Calibration · 원격진단 · Robot / Rail 상태점검 · Vision Calibration · SW Update · Consumables Check · A/S

| Care (만원/대 · 년) | Y3 | Y5 |
|---|---:|---:|
| 요금 | 48 | 48 |
| 정기 방문 원가 | 22.0 | 12.0 |
| 고장 방문 원가 | 10.8 | 10.8 |
| Cloud · SW | 4 | 4 |
| **원가 합계** | 36.8 | 26.8 |
| **마진** | 23% | 44% |

선례: 코웨이 국내 렌탈 계정 748만 (2026 1Q) · LG 가전 구독 매출 2조원+ · 케어매니저 약 4,000명 (2025) [S12 · S41]

## Consumables = 실제 마모 · 위생 기반 (억지 Lock-in 아님)

| Kit | 단가 (만원) | 교체 (회/년) | 연 (만원) |
|---|---:|---:|---:|
| Grip Kit | 4.5 | 4 | 18 |
| Cleaning Kit | 2.5 | 4 | 10 |
| Protection Kit | 4.0 | 2 | 8 |
| 정가 합계 |  |  | 36 |

후보: Grip Pad · Finger Pad · Food-contact Tip · Suction Seal · Cleaning Pad · Protective Cover. 교체주기는 Pad 수명 가속시험 (목표 ≥ 5,475회 파지, M18~M24)으로 확정. 식품 접촉 부품은 「기구 및 용기 · 포장의 기준 및 규격」 대응 [S48]

## 회사 매출 구성 (Base Plan, 억원, TARGET / ASSUMPTION)

| 층 | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---:|---:|---:|---:|---:|
| INSTALL (Interface · 설치 · Robot) | 0.0 | 0.2 | 7.0 | 34.5 | 87.7 |
| OPERATE (Rental · Care · 소모품) | 0.0 | 0.0 | 0.4 | 1.3 | 3.5 |
| EXPAND (Skill · Tool) | 0.0 | 0.0 | 0.0 | 0.1 | 0.3 |
| 매출 합계 | 0.0 | 0.3 | 7.4 | 35.9 | 91.5 |
| OPERATE + EXPAND 비중 | 0% | 9% | 5% | 4% | 4% |

반복매출 (OPERATE) Y3 0.4 → Y5 3.5억원 (Installed Base 663대) · Y5 매출 중 OPERATE + EXPAND 4% = 설치 초기 구조 (Installed Base 누적 후 비중 확대, DERIVED)

## MH Core vs Partner (Product Company 구조)

| MH Core | Partner |
|---|---|
| Robot · Robot Hand | 철거 · 가구 |
| Manipulation Skill | 전기 · 설비 |
| Calibration | 마감 공사 |
| Interface Standard | (신축) 건설사 · 주방가구사 |
| Safety · 시운전 · QA | (Rental) 렌탈 · 캐피탈사 |

Installation Volume 증가 ≠ 본사 현장인력 동일비율 증가. 현장 인력은 설치 · 서비스 엔지니어 (24개월 차 2명) 중심, 설치 인시는 Calibration 기술로 Y2 약 27 → Y5 약 12인시 목표 (TARGET)
