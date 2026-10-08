# 08. FACT / DERIVED / ASSUMPTION / TARGET 구분표

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

## Tag 정의

| Tag | 정의 | 예 |
|---|---|---|
| FACT | 공식 통계 · 공개자료로 확인된 값 | 총주택 2,018.1만호 · TIPS 8억원 · Robotiq 2F-85 약 $5,825 |
| DERIVED | FACT 또는 가정으로 계산한 값 (산식 공개) | 아파트 약 1,328만호 · 1세대 5년 기여이익 · Seed 범위 |
| ASSUMPTION | 현재 사업 가설 (검증 전) | Robot ASP 1,490만원 · Premium 10% · 적용률 60% |
| TARGET | 24개월 · 이후 목표 | 가정 실증 ≥ 90% · 출원 5건 · 설치 물량 |
| CONCEPT | 실물 없는 설계 개념 (그림 · 도식) | Hand 렌더 · Robot Home |
| TBV (To Be Validated) | 검증 방법이 정해진 미확인 사실 | 식세기 보급률 · 인증 적용 범위 |
| FUTURE | 현재 없는 제품 · 기능 | COOK · Upgrade |

재무모델 입력 108개: ASSUMPTION 84개 · FACT 17개 · TARGET 5개 · DERIVED 2개. 같은 표가 xlsx `Inputs` 시트에 있음 (Tag · 출처 포함)

## 1. 재무모델 입력 전체 (Scenario별 값, `=`은 Base와 같음)

연도별 값은 Y1 / Y2 / Y3 / Y4 / Y5 순서

### 시장 (23)

| Key | 항목 | 단위 | Tag | Conservative | Base | Upside | 출처 · 근거 |
|---|---|---|---|---|---|---|---|
| `m_housing_total` | 총주택 (2025.11.1 기준) | 천호 | FACT | = | 20,181 | = | 국가데이터처, 2025 인구주택총조사 등록센서스 결과 (2026.7.28 발표) |
| `m_apt_share` | 아파트 비중 (총주택 대비) | % | FACT | = | 65.8% | = | 국가데이터처, 2025 인구주택총조사 |
| `m_house_20y_share` | 준공 20년 이상 주택 비중 | % | FACT | = | 56% | = | 국가데이터처, 2025 인구주택총조사 |
| `m_house_30y_share` | 준공 30년 이상 주택 비중 | % | FACT | = | 30.6% | = | 국가데이터처, 2025 인구주택총조사 |
| `m_apt_2023` | 아파트 수 (2023) | 천호 | FACT | = | 12,630 | = | 통계청, 2023 주택총조사 (보도 인용) |
| `m_apt_20y_2023` | 준공 20년 이상 아파트 (2023) | 천호 | FACT | = | 6,390 | = | 통계청, 2023 주택총조사 (보도 인용) |
| `m_txn_2025` | 주택 매매거래 (2025, 전체 주택) | 천호 | FACT | = | 726 | = | KB주택시장리뷰 2026.2 (한국부동산원 자료) |
| `m_completion_2025` | 주택 준공 (2025 연간, 전체 주택) | 천호 | FACT | = | 342.4 | = | 국토교통부, 2025년 12월 주택통계 |
| `m_movein_2025` | 아파트 입주 (2025) | 천호 | FACT | = | 236.3 | = | 부동산114 REPS |
| `m_movein_2026e` | 아파트 입주 예정 (2026) | 천호 | FACT | = | 183.1 | = | 부동산114 REPS (예정 물량) |
| `a_replace_cycle` | Kitchen 교체주기 (노후 아파트) | 년 | ASSUMPTION | = | 22 | = | 교차검증용 가정. 견적 · 인터뷰로 검증 |
| `a_txn_apt_share` | 매매거래 중 아파트 비중 | % | ASSUMPTION | = | 70% | = | 부동산원 월별 아파트 거래 비중 확인 필요 |
| `a_txn_kitchen_rate` | 매수 후 Kitchen 교체율 | % | ASSUMPTION | = | 40% | = | 인터뷰 · 인테리어 Partner 자료로 검증 |
| `a_aging_nontxn` | 비거래 노후 교체 세대 | 천/년 | ASSUMPTION | = | 100 | = | 교차검증용 가정 |
| `a_kitchen_replace` | 연간 Kitchen 교체 세대 (아파트) | 천/년 | ASSUMPTION | = | 300 | = | 두 방식 교차검증 (29만 · 30만) 후 30만으로 설정 |
| `a_premium_share` | Premium Kitchen 비중 (교체 세대 중) | % | ASSUMPTION | = | 10% | = | 주방 예산 2,000만원 이상 가정. 견적 수집으로 검증 |
| `a_fit_rate` | Remodeling 적용 가능률 (구조 · 전원 · 평면) | % | ASSUMPTION | = | 60% | = | 평면 30개 분석으로 검증 |
| `a_prem_stock` | Premium 세대 비중 (아파트 재고 기준) | % | ASSUMPTION | = | 10% | = | Retrofit 대상. 소득 · 주택가격 기준 정의 필요 |
| `a_dw_premium` | Premium 세대 식기세척기 보유율 | % | ASSUMPTION | = | 60% | = | 공식 보급률 통계 확인 안 됨 (2019~20 업계 추정 10%대 초반 · 전체 가구) → TO BE VALIDATED |
| `a_retro_fit` | Retrofit 호환률 (주방 형태 · 식세기 위치 · 상부장) | % | ASSUMPTION | = | 40% | = | 가설. 확보 평면 5종 (Remodeling 기본 배치 수용 1 · 미수용 3 · 미검토 1)으로는 판단 불가 → 평면 30개 · 상담 주방 실측으로 검증 |
| `a_retro_conv` | Retrofit 연간 전환율 (호환 세대 중, 제품 성숙 후) | % | ASSUMPTION | = | 0.5% | = | 가설. Phase 2 시작 전 검증 |
| `a_new_supply` | 연간 신규 아파트 입주 (평균) | 천/년 | ASSUMPTION | = | 200 | = | 2025 실적 23.6만 · 2026 예정 18.3만 (평균 21.0만) → 보수적으로 20만 |
| `a_premium_project` | Premium 단지 비중 (신축) | % | ASSUMPTION | = | 15% | = | 브랜드 · 분양가 기준 정의 필요 |

### 고객 가치 (4)

| Key | 항목 | 단위 | Tag | Conservative | Base | Upside | 출처 · 근거 |
|---|---|---|---|---|---|---|---|
| `f_helper_rate` | 가사서비스 시간당 요금 (플랫폼 4시간 59,900~64,900원) | 만원/h | FACT | = | 1.5 | = | 가사서비스 플랫폼 공개 요금 (2025, 보도 · 앱 정보) |
| `a_cleanup_min` | 식사 후 정리 시간 (식기 이동 · 식세기 · 수납, 일) | 분/일 | ASSUMPTION | = | 40 | = | Time-diary(n=30)로 검증 |
| `a_auto_share` | CLEAN 자동화 가능 비중 | % | ASSUMPTION | = | 60% | = | 식기 이동 · 식세기 적재/인출 · 수납만. 행주 · 싱크 세척 제외 |
| `fx` | 환율 (Benchmark 환산용) | 원/USD | ASSUMPTION | = | 1,400 | = | 부품 Benchmark 환산 전용 |

### 가격 (25)

| Key | 항목 | 단위 | Tag | Conservative | Base | Upside | 출처 · 근거 |
|---|---|---|---|---|---|---|---|
| `p_rr` | Interface · Integration — Remodeling (Robot Home · Rail · 식세기 Interface · Storage Dock) | 만원/세대 | ASSUMPTION | 400 | 450 | = | 주방 공사비 위 증분. 시스템에어컨 유상옵션(500~1,000만원) 대비 하단 |
| `p_rr_new` | Interface Option — New-build (설계 반영, MH 공급가) | 만원/세대 | ASSUMPTION | 200 | 220 | = | 건설사 · 가구사 마진 별도. 분양 고객가 약 300만원 가정 |
| `p_rt_if` | Interface Kit — Retrofit (Compact Mount · Dock · Vision Reference · Drop Zone) | 만원/세대 | ASSUMPTION | = | 150 | = | 기존 주방 유지. 최소 시공 |
| `p_robot` | Robot System ASP (Arm · Adaptive Hand · Vision · Safety · Controller) | 만원/대 | ASSUMPTION | 1,290 | 1,490 | = | Upside는 가격 인상 없음. WTP 검증 대상 1순위 |
| `p_comm` | Installation · Calibration · Safety Check (Remodeling · New-build) | 만원/대 | ASSUMPTION | = | 80 | = | - |
| `p_comm_rt` | Installation · Calibration (Retrofit, 현장 Calibration 비중 큼) | 만원/대 | ASSUMPTION | = | 120 | = | - |
| `p_rent` | Robot Rental 월 요금 (Care Basic · Grip Kit 포함, 60개월) | 만원/월 | ASSUMPTION | 29 | 33 | = | 원가 Build-up (감가 · 금융 · Care · Grip · Reserve) + 마진 |
| `rent_months` | Rental 계약기간 | 개월 | ASSUMPTION | = | 60 | = | - |
| `p_care` | Care Basic 연 요금 (구매 고객) | 만원/년 | ASSUMPTION | 42 | 48 | = | 정기 안전점검 · Calibration · 원격진단 · SW Update · A/S 공임 |
| `p_care_plus` | Care Plus 연 요금 (Kit 정기교체 포함) | 만원/년 | ASSUMPTION | = | 72 | = | 옵션 상품. 재무 Base에는 미반영 |
| `p_grip` | Grip Kit (Finger Pad · Food-contact Tip · Suction Seal) | 만원/Kit | ASSUMPTION | = | 4.5 | = | 분기 교체 가정 |
| `n_grip` | Grip Kit 교체 횟수 | 회/년 | ASSUMPTION | = | 4 | = | Pad 마모율 · 교체주기 검증 대상 (KPI: Pad 수명) |
| `p_clean` | Cleaning Kit (Brush · Wiper · Cleaning Pad) | 만원/Kit | ASSUMPTION | = | 2.5 | = | - |
| `n_clean` | Cleaning Kit 교체 횟수 | 회/년 | ASSUMPTION | = | 4 | = | - |
| `p_protect` | Protection Kit (Sensor Cover · Sleeve · Seal) | 만원/Kit | ASSUMPTION | = | 4 | = | - |
| `n_protect` | Protection Kit 교체 횟수 | 회/년 | ASSUMPTION | = | 2 | = | - |
| `cons_attach` | Consumables 구매율 | % | ASSUMPTION | 55% | 70% | = | - |
| `care_attach` | Care 가입률 (구매 고객) | % | ASSUMPTION | 55% | 70% | = | - |
| `p_sw` | ASSIST Skill Pack (설치 다음 해) | 만원 | ASSUMPTION | = | 60 | = | ASSIST 기능 (재료 이동 · 투입 보조 등) 출시 전제 |
| `sw_attach` | ASSIST Skill 구매율 | % | ASSUMPTION | 10% | 20% | = | - |
| `p_tool` | Tool · End-effector 추가 (설치 2년 후) | 만원 | ASSUMPTION | = | 80 | = | FUTURE CONCEPT 제품 |
| `tool_attach` | Tool 구매율 | % | ASSUMPTION | 15% | 25% | = | - |
| `wholesale` | Rental Partner 공급가율 (Robot ASP 대비) | % | ASSUMPTION | = | 88% | = | Y4부터 Rental Partner가 자산 보유 |
| `partner_fee` | Rental Partner → MH Care · Grip 서비스료 | 만원/월 | ASSUMPTION | = | 6 | = | - |
| `realization` | 가격 실현율 (Y2 Pilot 할인) | % | ASSUMPTION | 100% / 30% / 100% / 100% / 100% | 100% / 50% / 100% / 100% / 100% | 100% / 60% / 100% / 100% / 100% | Pilot은 할인 유료 |

### 원가 (25)

| Key | 항목 | 단위 | Tag | Conservative | Base | Upside | 출처 · 근거 |
|---|---|---|---|---|---|---|---|
| `kit_std_cost` | Interface Kit 원가 — Remodeling (표준부품 100% 기준) | 만원/세대 | ASSUMPTION | = | 200 | = | Robot Home (Dock) · Rail Interface · 식세기 상향 하우징 · 전원/통신 · Storage Dock |
| `custom_factor` | Custom 부품 원가 배수 | x | ASSUMPTION | = | 1.6 | = | - |
| `design_cost` | Site 설계 · 조정 원가 (100% Custom 시) | 만원/세대 | ASSUMPTION | = | 100 | = | - |
| `smr` | Interface 표준부품 사용률 | % | TARGET | 40% / 45% / 55% / 62% / 65% | 40% / 50% / 65% / 75% / 80% | 40% / 55% / 70% / 80% / 85% | M24 65% 이상 목표 (M18 60% 미만이면 Interface 설계 재검토) |
| `kit_new_cost` | Interface Option 원가 — New-build (공장 생산) | 만원/세대 | ASSUMPTION | 145 | 130 | 120 | - |
| `rt_kit_cost` | Interface Kit 원가 — Retrofit | 만원/세대 | ASSUMPTION | = | 70 | = | Compact Mount · Dock · Vision Reference |
| `bom` | Robot System BOM (Adaptive Hand 포함) | 만원/대 | ASSUMPTION | 1,680 / 1,580 / 1,330 / 1,210 / 1,100 | 1,680 / 1,520 / 1,180 / 1,030 / 915 | 1,680 / 1,460 / 1,100 / 950 / 820 | BOM 구성 Benchmark 기반 (부록). 수량 · 국산화 · 자체 Hand 원가 하락 가정 |
| `comm_cost` | Installation · Calibration 원가 — Remodeling · New-build (MH 인력) | 만원/대 | ASSUMPTION | 120 / 100 / 75 / 62 / 55 | 120 / 90 / 60 / 45 / 38 | 120 / 85 / 52 / 38 / 30 | Calibration 시간 KPI와 연동 |
| `comm_cost_rt` | Installation · Calibration 원가 — Retrofit (MH 인력) | 만원/대 | ASSUMPTION | 160 / 140 / 110 / 95 / 85 | 160 / 130 / 95 / 75 / 62 | 160 / 120 / 85 / 65 / 52 | 현장 Calibration 비중 큼 |
| `logistics` | 물류 (세대당) | 만원/세대 | ASSUMPTION | = | 25 | = | - |
| `warranty` | Warranty Reserve (Robot 매출 대비) | % | ASSUMPTION | 5% | 4% | 3.5% | 1년 무상 A/S |
| `visits` | 정기 방문 횟수 | 회/년 | ASSUMPTION | 2 / 2 / 2 / 2 / 2 | 2 / 2 / 2 / 1.5 / 1.5 | 2 / 2 / 1.5 / 1.2 / 1 | 원격진단 고도화로 감소 |
| `visit_cost` | 방문 1회 원가 (인건비 · 이동) | 만원/회 | ASSUMPTION | 15 / 14 / 12.5 / 11 / 10 | 15 / 13 / 11 / 9 / 8 | 15 / 12 / 10 / 8 / 7 | 참고: 제조사 출장비 2.8만원 (소비자 부과분, 2026)과 별개인 실제 원가. Route Density로 하락 |
| `corrective` | 고장 방문 (Failure Rate) | 회/대·년 | ASSUMPTION | 0.9 | 0.6 | 0.5 | - |
| `corr_cost` | 고장 방문 1회 원가 (소부품 포함) | 만원/회 | ASSUMPTION | = | 18 | = | - |
| `cloud` | Cloud · Software 운영비 | 만원/대·년 | ASSUMPTION | = | 4 | = | - |
| `cons_cogs` | Consumables 원가율 (물류 포함) | % | ASSUMPTION | 40% | 35% | 32% | - |
| `sw_cogs` | Skill 원가율 | % | ASSUMPTION | = | 10% | = | - |
| `tool_cogs` | Tool 원가율 | % | ASSUMPTION | = | 45% | = | - |
| `partner_margin` | Kitchen · Interior · 설치 Partner 수수료 (Partner 경유 판매) | % | ASSUMPTION | 12% | 10% | 9% | - |
| `cac` | 직접판매 획득비용 (상담 · 설계 · Demo) | 만원/세대 | ASSUMPTION | 180 | 150 | 140 | - |
| `bd_new` | 신축 Project 수주비용 (Spec · 견본주택) | 만원/Project | ASSUMPTION | = | 2,000 | = | - |
| `residual` | Rental 자산 잔존가치 (60개월 후) | % | ASSUMPTION | = | 15% | = | Refurbish 재배치 |
| `fin_rate` | Rental 자산 금융비용 | %/년 | ASSUMPTION | = | 8% | = | 캐피탈 조달금리 + Spread 가정 |
| `payback_hurdle` | Rental Partner 요구 Payback | 개월 | ASSUMPTION | = | 36 | = | 렌탈 · 캐피탈사 협의로 검증 |

### 물량 (11)

| Key | 항목 | 단위 | Tag | Conservative | Base | Upside | 출처 · 근거 |
|---|---|---|---|---|---|---|---|
| `rd` | Remodeling — MH 직접 판매 (시공은 파트너) | 세대 | TARGET | 0 / 3 / 20 / 35 / 40 | 0 / 3 / 30 / 50 / 60 | 0 / 3 / 35 / 60 / 70 | Y2 = 가정 실증 3세대 (유료 목표, 할인) |
| `rp` | Remodeling — 주방 · 인테리어 Partner 경유 | 세대 | TARGET | 0 / 0 / 10 / 60 / 150 | 0 / 0 / 20 / 130 / 340 | 0 / 0 / 30 / 220 / 600 | Kitchen 가구 · 인테리어 Partner |
| `rt` | Existing Kitchen Retrofit (호환 주방, Partner 설치) | 세대 | TARGET | 0 / 0 / 0 / 10 / 40 | 0 / 0 / 0 / 20 / 80 | 0 / 0 / 0 / 30 / 120 | Phase 2. Y4 시작 |
| `attach` | Robot Attach Rate (Remodeling, 설치 시점) | % | ASSUMPTION | 100% / 100% / 75% / 75% / 75% | 100% / 100% / 85% / 85% / 85% | = | 나머지는 Interface 선설치 (Robot 후설치) |
| `later_attach` | Interface 선설치 세대의 연간 Robot 후설치 | %/년 | ASSUMPTION | 5% | 10% | 12% | - |
| `rental_share` | Rental 선택 비중 | % | ASSUMPTION | 0% / 30% / 30% / 35% / 35% | 0% / 30% / 30% / 40% / 40% | 0% / 30% / 30% / 45% / 45% | - |
| `partner_rental` | Rental 자산 보유 주체 (0 = MH Pilot, 1 = Rental Partner) | flag | ASSUMPTION | = | 0 / 0 / 0 / 1 / 1 | = | - |
| `projects` | 신축 Interface Option 계약 Project | 개 | TARGET | 0 / 0 / 0 / 1 / 2 | 0 / 0 / 1 / 2 / 3 | 0 / 0 / 2 / 3 / 4 | 계약 2년 후 입주 · 설치 |
| `hh_project` | Project당 세대수 | 세대 | ASSUMPTION | = | 800 | = | - |
| `option_rate` | 신축 Interface Option 선택률 | % | ASSUMPTION | 6% | 10% | 12% | - |
| `new_attach` | 신축 입주 시 Robot Attach | % | ASSUMPTION | 15% | 25% | 30% | - |

### 운영비 (14)

| Key | 항목 | 단위 | Tag | Conservative | Base | Upside | 출처 · 근거 |
|---|---|---|---|---|---|---|---|
| `fte` | 평균 인원 (FTE) | 명 | ASSUMPTION | = | 7.042 / 12.75 / 20 / 32 / 42 | = | Y1~Y2 = 팀 계획 (Budget_24M, Founder 2 + 신규 채용) · Y3부터 Series A 전제 |
| `loaded` | 인당 연 인건비 (4대보험 · 퇴직급여 포함, 평균) | 만원/년 | ASSUMPTION | = | 7,927.81 / 7,611.76 / 8,500 / 8,500 / 8,500 | = | Y1~Y2 = 팀 계획 가중평균 · Y3~ 평균 연봉 약 7,100만원 × 1.2 |
| `robot_hw` | Robot Hardware (R&D 로봇 셀) | 만원 | ASSUMPTION | = | 4,800 / 1,600 / 12,000 / 14,000 / 16,000 | = | - |
| `hand_proto` | Hand Prototype (비교군 · 자체 Hand v1~v3) | 만원 | ASSUMPTION | = | 6,000 / 4,000 / 10,000 / 12,000 / 14,000 | = | - |
| `mockup` | Kitchen Mock-up (실물 크기 3종) | 만원 | ASSUMPTION | = | 5,000 / 2,500 / 8,000 / 9,000 / 10,000 | = | - |
| `swdata` | Software · Data (GPU · Cloud · Annotation) | 만원 | ASSUMPTION | = | 2,500 / 3,000 / 10,000 / 15,000 / 20,000 | = | - |
| `pilot` | Pilot 운영 (실증 하드웨어 제외) | 만원 | ASSUMPTION | = | 0 / 3,500 / 5,000 / 5,000 / 5,000 | = | - |
| `custval` | Customer Validation · Partner · Marketing | 만원 | ASSUMPTION | = | 2,000 / 4,000 / 30,000 / 50,000 / 70,000 | = | - |
| `cert` | Safety · Certification | 만원 | ASSUMPTION | = | 1,500 / 4,500 / 15,000 / 6,000 / 5,000 | = | Y3 본인증 |
| `ip` | IP (선행기술조사 · 출원) | 만원 | ASSUMPTION | = | 1,500 / 3,000 / 5,000 / 4,000 / 5,000 | = | - |
| `space` | Space (실험실 · 목업 공간) | 만원 | ASSUMPTION | = | 4,800 / 4,800 / 10,000 / 12,000 / 15,000 | = | - |
| `ga` | Operating · G&A (법무 · 회계 · 보험 · 사무) | 만원 | ASSUMPTION | = | 4,000 / 5,000 / 30,000 / 40,000 / 50,000 | = | - |
| `contingency` | 예비비 (인건비 외 지출의 10%, Y1~Y2) | 만원 | DERIVED | = | 3,210 / 3,590 / 0 / 0 / 0 | = | 24개월 계획의 하드웨어 · 일정 Risk 대비 |
| `rnd_allow` | 연구수당 (TIPS 과제 현금 인건비 × 5%) | 만원 | DERIVED | = | 1,032.75 / 1,626 / 0 / 0 / 0 | = | TIPS 선정 시 |

### 자금 · TIPS (6)

| Key | 항목 | 단위 | Tag | Conservative | Base | Upside | 출처 · 근거 |
|---|---|---|---|---|---|---|---|
| `tips` | TIPS R&D 정부지원금 (일반 트랙 최대) | 만원 | FACT | = | 80,000 | = | 중소벤처기업부 공고 제2026-40호 (2026.1.26) 팁스 창업기업 지원계획. 선정 미확정 |
| `tips_months` | TIPS R&D 기간 (최대) | 개월 | FACT | = | 24 | = | 공고 제2026-40호 |
| `tips_gov_ratio` | 정부지원연구개발비 비율 상한 (총 연구개발비 대비) | % | FACT | = | 75% | = | 공고 제2026-40호 (사본 · 운용사 정리 기준: 정부 75% 이내, 기관부담 25% 이상) |
| `tips_cash_ratio` | 기관부담연구개발비 중 현금 최소 비율 | % | FACT | = | 10% | = | 공고 제2026-40호 (사본 · 운용사 정리 기준) |
| `op_invest_min` | TIPS 운영사 선투자 요건 (수도권) | 만원 | FACT | = | 20,000 | = | 2026: 수도권 2억원 이상 · 비수도권 1억원 이상 |
| `biz_link` | 비R&D 연계 (창업사업화 · 해외마케팅) 각 최대 (선정 뒤 별도 신청, 기본안 미반영) | 만원 | FACT | = | 15,000 | = | 공고 제2026-40호: 각 10개월 최대 1.5억원, 합산 3억원, 정부 70% 이내 |

## 2. 주요 계산값 (DERIVED)

| 항목 | 값 | 산식 | model.json key |
|---|---|---|---|
| 국내 아파트 수 | 약 1,328만호 | 총주택 2,018.1만 × 65.8% | market.B.apt |
| 연간 주방 교체 교차검증 ① · ② | 29.0만 · 30.3만 | 20년+ 아파트 ÷ 교체주기 22년 · 매매 × 70% × 40% + 비거래 10만 | market.B.tri1 · tri2 |
| Remodeling SAM | 3,212억원/년 | 30만 × 10% × 60% × 패키지 1,784.5만원 | market.B.sam_remodel |
| Retrofit SAM | 280억원/년 | 31.9만 (재고) × 0.5% × 1,760만원 | market.B.sam_retro |
| New-build SAM | 184억원/년 | 20만 × 15% × 10% × 612.5만원 | market.B.sam_new |
| Recurring (1,000대당) | 5.9억원/년 | ARPU 58.8만원 (Care 70% × 48 + 소모품 70% × 36) | market.B.recurring_per_1000 |
| Y5 매출 / 대상 세대 비중 | 91.5억원 · 2.5% | 560세대 ÷ 대상 세대 합 | market.B.som · som_share_hh |
| 1세대 5년 매출 · 기여이익 (Y3 원가) | 2,418만원 · 428만원 (17.7%) | 부록 D2 · 10번 문서 | household.purchase_direct_Y3 |
| 1세대 5년 기여이익 (Y5 원가) | 798만원 (33.0%) | BOM 915 · 설치 38 · Care 26.8만원 | household.purchase_direct_Y5 |
| Rental 월 원가 · Payback (Y3) | 25.6만원 · 40개월 | 감가 + 금융 + Care + Grip + Reserve | rental.Y3 |
| Partner IRR (연) | 13.1% | Robot을 ASP의 88% (1,311만원)에 매입, 월 27만원 순유입, 잔존 15% | partner_irr.B |
| Care 마진 Y3 → Y5 | 23% → 44% | 요금 48만원 − (방문 + 고장 + Cloud) | care.Y3 · Y5 |
| 설치 인시 (Remodeling) Y2 · Y3 · Y5 | 27 · 18 · 12인시 | 설치 원가 ÷ 시간당 3.3만원 | kpi_links.inst_h |
| Pad 수명 목표 | 5,475회 | 하루 60회 × 365 ÷ 4 (분기 교체) | kpi_links.pad_life |
| 24개월 지출 | 23.4억원 | 팀 계획 + 비용 + 예비비 10% + 연구수당 | funding.spend_total |
| TIPS 과제 총액 | 10.67억원 | 정부 8억원 ÷ 75% | tips.total |
| Seed Base · Lean · TIPS 미선정 | 19.0억원 · 13.8억원 · 21.5억원 | 지출 − TIPS 정부지원 + Y2 월지출 × 3개월 | funding.seed_* |
| 손익분기 설치 물량 (Y5 단가 · 원가) | 연 약 1,376세대 | Y5 Opex ÷ 세대당 기여이익 | breakeven_kitchens |
| Series A 이후 2년 (Y3~Y4) 현금 소요 | 68억원 | Base 계획 기준 | post_seed_burn.y3_y4 |

## 3. TARGET (물량 · 표준화 목표)

| Key | 항목 | Base (Y1~Y5) | 근거 |
|---|---|---|---|
| `smr` | Interface 표준부품 사용률 | 40% / 50% / 65% / 75% / 80% | M24 65% 이상 목표 (M18 60% 미만이면 Interface 설계 재검토) |
| `rd` | Remodeling — MH 직접 판매 (시공은 파트너) | 0 / 3 / 30 / 50 / 60 | Y2 = 가정 실증 3세대 (유료 목표, 할인) |
| `rp` | Remodeling — 주방 · 인테리어 Partner 경유 | 0 / 0 / 20 / 130 / 340 | Kitchen 가구 · 인테리어 Partner |
| `rt` | Existing Kitchen Retrofit (호환 주방, Partner 설치) | 0 / 0 / 0 / 20 / 80 | Phase 2. Y4 시작 |
| `projects` | 신축 Interface Option 계약 Project | 0 / 0 / 1 / 2 / 3 | 계약 2년 후 입주 · 설치 |

기술 KPI 목표 (M6~M24)는 [12_Technical_KPI.md](12_Technical_KPI.md)

## 4. CONCEPT · FUTURE

| 대상 | 위치 (본문 · 부록) | Tag |
|---|---|---|
| Adaptive Robot Hand 형상 · 구성 | 06 · 부록 B1 | CONCEPT (v1~v3 설계 전) |
| Robot Home · Rail · 식세기 Interface · Storage Dock | 01 · 08 · 10 · 부록 B3 · B4 | CONCEPT (3D 충돌검사 = 모델 기준) |
| CLEAN 5단계 동작 장면 | 09 | CONCEPT |
| Kitchen A~C 평면 도식 | 07 | CONCEPT (개념 예시) |
| Calibration 4요소 · Skill 실행 구조 | 07 · 08 | CONCEPT (개발 전) |
| ASSIST Skill Pack · Tool | 09 · 11 | FUTURE (출시 전제, Y3~) |
| COOK · Robot Upgrade | 09 · 11 | FUTURE CONCEPT (5년 Base 매출 미반영) |
| MH 안전 원칙 (Zone · 감속 · Safe Home Return) | 08 · 부록 B5 | CONCEPT |
