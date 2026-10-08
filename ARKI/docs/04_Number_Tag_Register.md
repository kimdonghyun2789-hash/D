# 04. FACT / DERIVED / ASSUMPTION / TARGET 구분표

> ARKI Robotics (가칭) · TIPS 창업기업 IR · Draft v4 · 2026-10-08 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·파트너·투자유치 없음.

## Tag 정의

| Tag | 정의 | 사용 원칙 |
|---|---|---|
| FACT | 공식 통계 또는 공개자료로 확인된 값 | 출처 ID(S1~S32) 병기. 보도 인용은 원문 대조 필요 |
| DERIVED | FACT 또는 가정을 ARKI가 계산한 값 | 산식 병기. 가정 기반 계산은 "DERIVED (from ASSUMPTION)" |
| ASSUMPTION | 현재 사업가설 | 검증 방법·시점 병기 |
| TARGET | TIPS 기간 또는 이후 목표 | Kill Criteria와 연결 |
| CONCEPT | 실물 없는 설계 개념 | Concept Layout·단면·Module 구성 |
| TO BE VALIDATED (TBV) | 미확인 사실, 검증 방법 확정 | 본문 각주 |
| FUTURE CONCEPT | 현재 존재하지 않는 제품 | V2 ASSIST · V3 COOK · Tool 확장 |

## 입력값 전체 (95개, 재무모델 `Inputs` · `Inputs_Yearly` 시트와 동일)

연도별 값은 Y1~Y5 순서. C = Conservative, B = Base, U = Upside. 금액 단위 만원.

| Tag | Key | 항목 | 단위 | 값 | Source / Note |
|---|---|---|---|---|---|
| FACT | m_housing_total | 총주택 (2025.11.1 기준) | 천호 | 20181 | 국가데이터처, 2025 인구주택총조사 등록센서스 결과 (2026.7.28 발표) |
| FACT | m_apt_share | 아파트 비중 (총주택 대비) | % | 0.658 | 국가데이터처, 2025 인구주택총조사 |
| FACT | m_house_20y_share | 준공 20년 이상 주택 비중 | % | 0.56 | 국가데이터처, 2025 인구주택총조사 |
| FACT | m_house_30y_share | 준공 30년 이상 주택 비중 | % | 0.306 | 국가데이터처, 2025 인구주택총조사 |
| FACT | m_apt_2023 | 아파트 수 (2023) | 천호 | 12630 | 통계청, 2023 주택총조사 (보도 인용) |
| FACT | m_apt_20y_2023 | 준공 20년 이상 아파트 (2023) | 천호 | 6390 | 통계청, 2023 주택총조사 (보도 인용) |
| FACT | m_txn_2025 | 주택 매매거래 (2025, 전체 주택) | 천호 | 726 | KB주택시장리뷰 2026.2 (한국부동산원 자료) |
| FACT | m_completion_2025 | 주택 준공 (2025 연간, 전체 주택) | 천호 | 342.4 | 국토교통부, 2025년 12월 주택통계 |
| FACT | m_movein_2025 | 아파트 입주 (2025) | 천호 | 236.3 | 부동산114 REPS |
| FACT | m_movein_2026e | 아파트 입주 예정 (2026) | 천호 | 183.1 | 부동산114 REPS (예정 물량) |
| ASSUMPTION | a_replace_cycle | Kitchen 교체주기 (노후 아파트) | 년 | 22 | 교차검증용 가정. TIPS 기간 견적·인터뷰로 검증 |
| ASSUMPTION | a_txn_apt_share | 매매거래 중 아파트 비중 | % | 0.7 | 부동산원 월별 아파트 거래 비중 확인 필요 |
| ASSUMPTION | a_txn_kitchen_rate | 매수 후 Kitchen 교체율 | % | 0.4 | 인터뷰·인테리어 Partner 자료로 검증 |
| ASSUMPTION | a_aging_nontxn | 비거래 노후 교체 세대 | 천/년 | 100 | 교차검증용 가정 |
| ASSUMPTION | a_kitchen_replace | 연간 Kitchen 교체 세대 (아파트) | 천/년 | 300 | 두 방식 교차검증(29만·30만) 후 30만으로 설정 |
| ASSUMPTION | a_premium_share | Premium Kitchen 비중 | % | 0.1 | 주방 예산 2,000만원 이상 가정. 견적 수집으로 검증 |
| ASSUMPTION | a_fit_rate | Robot-ready 적용 가능률 (구조·전원·평면) | % | 0.6 | 평면 30개 분석으로 검증 |
| DERIVED | a_new_supply | 연간 신규 아파트 입주 (평균) | 천/년 | 200 | 2025 실적 23.6만·2026 예정 18.3만 → 20만 |
| ASSUMPTION | a_premium_project | Premium 단지 비중 (신축) | % | 0.15 | 브랜드·분양가 기준 정의 필요 |
| FACT | f_helper_rate | 가사서비스 시간당 요금 (플랫폼 4시간 59,900~64,900원) | 만원/h | 1.5 | 가사서비스 플랫폼 공개 요금 (2025, 보도·앱 정보) |
| ASSUMPTION | a_cleanup_min | Clean-up 시간 (식사 후 정리, 일) | 분/일 | 40 | Time-diary(n=30)로 검증 |
| ASSUMPTION | a_auto_share | V1 자동화 가능 비중 | % | 0.6 | 식기 이동·식세기·수납만. 행주·싱크 세척 제외 |
| ASSUMPTION | fx | 환율 (Benchmark 환산용) | 원/USD | 1400 | 부품 Benchmark 환산 전용 |
| ASSUMPTION | p_rr | Robot-ready Kitchen 증분가 (구축) | 만원/세대 | C: 400 / B: 450 / U: 450 | 기존 Kitchen 공사비 위 증분. 시스템에어컨 유상옵션(500~1,000만원) 대비 하단 |
| ASSUMPTION | p_rr_new | Robot-ready Option 공급가 (신축, ARKI 매출) | 만원/세대 | C: 200 / B: 220 / U: 220 | 건설사·가구사 마진 별도. 분양 고객가 약 300만원 가정 |
| ASSUMPTION | p_robot | Robot Module ASP (구매) | 만원/대 | C: 1290 / B: 1490 / U: 1490 | Upside는 가격 인상 없음. WTP 검증 대상 1순위 |
| ASSUMPTION | p_comm | 설치·Calibration·Safety Check | 만원/대 | 80 |  |
| ASSUMPTION | p_rent | Robot Rental 월 요금 (Care Basic·Grip Kit 포함, 60개월) | 만원/월 | C: 29 / B: 33 / U: 33 | 원가 Build-up(감가·금융·Care·Grip·Reserve)+마진 |
| ASSUMPTION | rent_months | Rental 계약기간 | 개월 | 60 |  |
| ASSUMPTION | p_care | Care Basic 연 요금 (구매 고객) | 만원/년 | C: 42 / B: 48 / U: 48 | 정기점검·Calibration·원격진단·SW Update·A/S 공임 |
| ASSUMPTION | p_care_plus | Care Plus 연 요금 (Kit 정기교체 포함) | 만원/년 | 72 | 옵션 상품. 재무 Base에는 미반영 |
| ASSUMPTION | p_grip | Grip Kit (Finger Pad·Food-contact Tip·Suction Cup) | 만원/Kit | 4.5 | 분기 교체 가정 |
| ASSUMPTION | n_grip | Grip Kit 교체 횟수 | 회/년 | 4 | Replacement Cycle 검증 대상 |
| ASSUMPTION | p_clean | Cleaning Kit (Brush·Wiper·Cleaning Pad) | 만원/Kit | 2.5 |  |
| ASSUMPTION | n_clean | Cleaning Kit 교체 횟수 | 회/년 | 4 |  |
| ASSUMPTION | p_protect | Protection Kit (Sensor Cover·Sleeve·Seal) | 만원/Kit | 4 |  |
| ASSUMPTION | n_protect | Protection Kit 교체 횟수 | 회/년 | 2 |  |
| ASSUMPTION | cons_attach | Consumables 구매율 | % | C: 0.55 / B: 0.7 / U: 0.7 |  |
| ASSUMPTION | care_attach | Care 가입률 (구매 고객) | % | C: 0.55 / B: 0.7 / U: 0.7 |  |
| ASSUMPTION | p_sw | Software Skill Pack (설치 다음 해) | 만원 | 60 | V2 기능 (재료 투입 보조 등) 출시 전제 |
| ASSUMPTION | sw_attach | Software Skill 구매율 | % | C: 0.1 / B: 0.2 / U: 0.2 |  |
| ASSUMPTION | p_tool | End-effector / Tool 추가 (설치 2년 후) | 만원 | 80 | FUTURE CONCEPT 제품 |
| ASSUMPTION | tool_attach | Tool 구매율 | % | C: 0.15 / B: 0.25 / U: 0.25 |  |
| ASSUMPTION | wholesale | Rental Partner 공급가율 (Robot ASP 대비) | % | 0.88 | Y4부터 Rental Partner가 자산 보유 |
| ASSUMPTION | partner_fee | Rental Partner → ARKI Care·Grip 서비스료 | 만원/월 | 6 |  |
| ASSUMPTION | realization | 가격 실현율 (Y2 Pilot 할인) | % | C: 1, 0.3, 1, 1, 1 / B: 1, 0.5, 1, 1, 1 / U: 1, 0.6, 1, 1, 1 | Pilot은 할인 유료 |
| ASSUMPTION | kit_std_cost | Kitchen Module 원가 (100% 표준부품 기준) | 만원/세대 | 200 | 하부 보강 프레임·Rail Interface·식세기 상향 하우징·Robot Garage·전원/통신·수납 Rack |
| ASSUMPTION | custom_factor | Custom 부품 원가 배수 | x | 1.6 |  |
| ASSUMPTION | design_cost | Design·Site Adjustment 원가 (100% Custom 시) | 만원/세대 | 100 |  |
| TARGET | smr | Standard Module 사용률 | % | C: 0.4, 0.45, 0.55, 0.62, 0.65 / B: 0.4, 0.5, 0.65, 0.75, 0.8 / U: 0.4, 0.55, 0.7, 0.8, 0.85 | 초기 종료 시 65% 이상 (Kill Criteria: M18 60% 미만) |
| ASSUMPTION | kit_new_cost | Robot-ready Option 원가 (신축, 공장 생산) | 만원/세대 | C: 145 / B: 130 / U: 120 |  |
| ASSUMPTION | bom | Robot Module BOM | 만원/대 | C: 1600, 1500, 1300, 1180, 1080 / B: 1600, 1450, 1150, 1000, 900 / U: 1600, 1400, 1080, 920, 800 | D5 부품 Benchmark 기반. 수량·국산화·전용 Arm으로 하락 가정 |
| ASSUMPTION | comm_cost | 설치·Calibration 원가 (ARKI 인력) | 만원/대 | C: 120, 100, 75, 62, 55 / B: 120, 90, 60, 45, 38 / U: 120, 85, 52, 38, 30 | 설치시간 TARGET과 연동 |
| ASSUMPTION | logistics | 물류 (프로젝트당) | 만원/세대 | 25 |  |
| ASSUMPTION | warranty | Warranty Reserve (Robot 매출 대비) | % | C: 0.05 / B: 0.04 / U: 0.035 | 1년 무상 A/S |
| ASSUMPTION | visits | 정기 방문 횟수 | 회/년 | C: 2, 2, 2, 2, 2 / B: 2, 2, 2, 1.5, 1.5 / U: 2, 2, 1.5, 1.2, 1 | 원격진단 고도화로 감소 |
| ASSUMPTION | visit_cost | 방문 1회 원가 (인건비·이동) | 만원/회 | C: 15, 14, 12.5, 11, 10 / B: 15, 13, 11, 9, 8 / U: 15, 12, 10, 8, 7 | 참고: 제조사 출장비 2.8만원(소비자 부과분, 2026)과 별개인 실제 원가. Route Density로 하락 |
| ASSUMPTION | corrective | 고장 방문 (Failure Rate) | 회/대·년 | C: 0.9 / B: 0.6 / U: 0.5 |  |
| ASSUMPTION | corr_cost | 고장 방문 1회 원가 (소부품 포함) | 만원/회 | 18 |  |
| ASSUMPTION | cloud | Cloud·Software 운영비 | 만원/대·년 | 4 |  |
| ASSUMPTION | cons_cogs | Consumables 원가율 (물류 포함) | % | C: 0.4 / B: 0.35 / U: 0.32 |  |
| ASSUMPTION | sw_cogs | Software 원가율 | % | 0.1 |  |
| ASSUMPTION | tool_cogs | Tool 원가율 | % | 0.45 |  |
| ASSUMPTION | partner_margin | Kitchen·Interior Partner 수수료 (Partner 경유 패키지) | % | C: 0.12 / B: 0.1 / U: 0.09 |  |
| ASSUMPTION | cac | 직접판매 획득비용 (상담·설계·Demo) | 만원/세대 | C: 180 / B: 150 / U: 140 |  |
| ASSUMPTION | bd_new | 신축 Project 수주비용 (Spec·견본주택) | 만원/Project | 2000 |  |
| ASSUMPTION | residual | Rental 자산 잔존가치 (60개월 후) | % | 0.15 | Refurbish 재배치 |
| ASSUMPTION | fin_rate | Rental 자산 금융비용 | %/년 | 0.08 | 캐피탈 조달금리+Spread 가정 |
| ASSUMPTION | payback_hurdle | Rental Partner 요구 Payback | 개월 | 36 | 렌탈·캐피탈사 협의로 검증 |
| TARGET | rd | 구축 직접판매 Kitchen | 세대 | C: 0, 3, 20, 35, 40 / B: 0, 3, 30, 50, 60 / U: 0, 3, 35, 60, 70 | Y2 = 가정 실증 3세대 (TIPS 과제, 유료 목표) |
| TARGET | rp | 구축 Partner 경유 Kitchen | 세대 | C: 0, 0, 10, 60, 150 / B: 0, 0, 20, 130, 340 / U: 0, 0, 30, 220, 600 | Kitchen 가구·인테리어 Partner |
| ASSUMPTION | attach | Robot Attach Rate (구축, 설치 시점) | % | C: 1, 1, 0.75, 0.75, 0.75 / B: 1, 1, 0.85, 0.85, 0.85 / U: 1, 1, 0.85, 0.85, 0.85 | 나머지는 Robot-ready Only |
| ASSUMPTION | later_attach | Robot-ready Only 세대의 연간 후속 Attach | %/년 | C: 0.05 / B: 0.1 / U: 0.12 |  |
| ASSUMPTION | rental_share | Rental 선택 비중 | % | C: 0, 0.3, 0.3, 0.35, 0.35 / B: 0, 0.3, 0.3, 0.4, 0.4 / U: 0, 0.3, 0.3, 0.45, 0.45 |  |
| ASSUMPTION | partner_rental | Rental 자산 보유 주체 (0 = ARKI Pilot, 1 = Rental Partner) | flag | 0, 0, 0, 1, 1 |  |
| TARGET | projects | 신축 Robot-ready Option 계약 Project | 개 | C: 0, 0, 0, 1, 2 / B: 0, 0, 1, 2, 3 / U: 0, 0, 2, 3, 4 | 계약 2년 후 입주·설치 |
| ASSUMPTION | hh_project | Project당 세대수 | 세대 | 800 |  |
| ASSUMPTION | option_rate | 신축 Robot-ready Option 선택률 | % | C: 0.06 / B: 0.1 / U: 0.12 |  |
| ASSUMPTION | new_attach | 신축 입주 시 Robot Attach | % | C: 0.15 / B: 0.25 / U: 0.3 |  |
| ASSUMPTION | fte | 평균 인원 | 명 | 4.4, 7, 20, 32, 42 | Y1~Y2 = TIPS 기간 (대표 + 신규 연구원 4명 → Y2 실증 엔지니어 · 사업개발 추가, TIPS_TEAM). Y3부터 후속 투자 전제 |
| ASSUMPTION | loaded | 인당 연 인건비 (4대보험·퇴직급여 포함) | 만원/년 | 8500 | 평균 연봉 약 7,100만원 × 1.2 |
| ASSUMPTION | proto | Robot·Kitchen Prototype (H/W) | 만원 | 12000, 4000, 30000, 35000, 40000 | Y1 시제품 1차 2식 + 실물 크기 목업 주방 2식 · Y2 2차 개선 부품 (실증 3세대 하드웨어는 원가에 반영) |
| ASSUMPTION | swdata | Vision·Software·Data (GPU·Cloud·Annotation) | 만원 | 2000, 3000, 10000, 15000, 20000 |  |
| ASSUMPTION | space | Full-scale Mock-up·공간 | 만원 | 6000, 4000, 10000, 12000, 15000 | Y1~Y2: 목업 공간 약 30평 임차 + 목업 시공 |
| ASSUMPTION | cert_ip | Safety·Certification·IP | 만원 | 2500, 6000, 20000, 10000, 10000 | Y1 선행기술조사 · 특허 출원 2건 / Y2 공인시험 · 안전 사전시험 · 특허 3건 / Y3 본인증 |
| ASSUMPTION | research | Pilot·Customer Validation | 만원 | 2000, 3500, 5000, 5000, 5000 | Y1 인터뷰 50명 · 정리 시간 기록 30세대 / Y2 지불의사 조사 n≥300 · 실증 가정 지원 |
| ASSUMPTION | mkt | Marketing·Partner Enablement | 만원 | 0, 1000, 30000, 50000, 70000 |  |
| ASSUMPTION | ga | G&A (법무·회계·보험·사무) | 만원 | 5000, 6000, 30000, 40000, 50000 |  |
| FACT | tips | TIPS R&D 정부지원금 (일반 트랙 최대) | 만원 | 80000 | 중소벤처기업부 공고 제2026-40호 (2026.1.26) 팁스 창업기업 지원계획. 선정 미확정 |
| FACT | tips_months | TIPS R&D 기간 (최대) | 개월 | 24 | 공고 제2026-40호 |
| FACT | tips_gov_ratio | 정부지원연구개발비 비율 상한 (총 연구개발비 대비) | % | 0.75 | 공고 제2026-40호 (사본 · 운용사 정리 기준: 정부 75% 이내, 기관부담 25% 이상) |
| FACT | tips_cash_ratio | 기관부담연구개발비 중 현금 최소 비율 | % | 0.1 | 공고 제2026-40호 (사본 · 운용사 정리 기준) |
| ASSUMPTION | op_invest | 운영사 투자 (요청액, TIPS 추천 전제) | 만원 | 30000 | 요건: 수도권 2억원 이상 · 비수도권 1억원 이상 (2026). 조건 (형태 · 기업가치 · 지분)은 협의 |
| TARGET | followon | 후속 투자 (M12 목표, 공동투자 · Pre-A) | 만원 | 50000 | M9 · M12 점검 결과 기반 |
| FACT | biz_link | 비R&D 연계 (창업사업화 · 해외마케팅) 각 최대 (선정 뒤 별도 신청, 기본안 미반영) | 만원 | 15000 | 공고 제2026-40호: 각 10개월 최대 1.5억원, 합산 3억원, 정부 70% 이내 |

## 주요 산출값 (DERIVED)

| Tag | 항목 | 값 | 위치 |
|---|---|---|---|
| DERIVED | 아파트 수 (2025) | 1,328만호 | 총주택 2,018.1만 × 65.8% |
| DERIVED | Kitchen 교체 세대 교차검증 ①·② | 29.0만 · 30.3만/년 | C1 |
| DERIVED | TAM / SAM / SOM(Y5) | 1.21조 / 3,396억 / 77.5억원 | C01장 · C3 |
| DERIVED | 가치 Anchor (월) | 18만원 (Range 11~24) | D1 |
| DERIVED | 세대 5년 매출 / Contribution (구매, Y3·Y5) | 2,418만원 / 458·813만원 | D2 |
| DERIVED | Rental 월 Contribution · Payback (Y3·Y5) | 7.9·13.4만원 · 39·30개월 | D7 |
| DERIVED | Rental Partner IRR (Base) | 13.1% (연체·해지 미반영) | D7 |
| DERIVED | Care Margin (Y3·Y5) | 23% · 44% | D8 |
| DERIVED | Consumables 연 매출 · Contribution / Robot | 25.2 · 16.4만원 | D8 |
| DERIVED | Y5 매출 C / B / U | 27.8 / 77.5 / 134.0억원 | D9 |
| DERIVED | Y5 영업이익 C / B / U | -56.4 / -36.4 / -11.9억원 | D9 |
| DERIVED | 5년 누적 현금흐름 최저 (Base) | -120.2억원 | D9 |
| DERIVED | 손익분기 Kitchen (연, Y5 단가·원가) | 1,340세대 | 15장 |
| DERIVED | TIPS 24개월 회사 전체 지출 / 후속 투자 없을 때 자금 지속 | 15.7억원 / 17.7개월 | D11 |
| ASSUMPTION | TIPS 과제 예산 (정부 · 민간 현금 · 현물) | 10.7억원 (8.0 · 1.82 · 0.85) | 본문 19쪽 |
| DERIVED | 정상상태 Recurring / Upgrade 비중 | 15% / 14% | C5 |

## 주요 목표값 (TARGET)

| Tag | 항목 | 목표 |
|---|---|---|
| TARGET | 평면 분석 | 30개 이상 (신축 15 · 구축 15) |
| TARGET | Layout Family / Robot Architecture | 3~5 / 2~3 |
| TARGET | Standard Module 사용률 | 65% (Y3) · 80% (Y5) · Kill: M18 60% 미만 |
| TARGET | 식기 정리 성공률 (사람 개입 없이) | 70% (M9 목업) · 90% (M24 가정 실증) |
| TARGET | 특허 출원 | 24개월 5건 (Y1 2 · Y2 3, 등록 미정) |
| TARGET | Consumer Interview / Conjoint | 50명 / n≥300 |
| TARGET | Home Pilot | 3~5세대 (Paid Pilot 포함) |
| TARGET | Installation · Calibration Time | 1일·2인 · 2시간 (M24) |
| TARGET | Patent 출원 | 5~8건 (선행기술조사 후) |
| TARGET | Volume (Base) | 구축 직접 [0, 3, 30, 50, 60] · Partner [0, 0, 20, 130, 340] · 신축 Project [0, 0, 1, 2, 3] |
