# 01. Executive Summary

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

## 한 문장 정의

> Adaptive Robot Hand · Manipulation Skill · Calibration · Environment Integration 결합 → 다양한 실제 주방에서 식기 정리부터 조리까지 단계적으로 확장하는 Kitchen Manipulation Robotics System 개발  
- 초기 CLEAN Workflow로 기술 검증 → 같은 Platform에서 ASSIST · COOK으로 Capability 확장  
- 기존 주방 · Remodeling · New-build에 서로 다른 Integration 수준으로 적용  
- Robot · 설치 매출 이후 Rental · Care · Consumables · Skill · Tool · Upgrade로 Installed Base 기반 반복매출 확보

현재 단계: **Concept** (시제품 개발 전)

## 요약

| 항목 | 내용 | 근거 · Tag |
|---|---|---|
| 문제 | 가전은 기기 안의 일을 자동화했지만, 가전 사이의 Physical Workflow (식기 이동 · 식세기 적재/인출 · 수납 · 재료 투입 · 도구)는 사람 몫. Appliance Automation ≠ Physical Workflow Automation | 무급 가사노동 582.4조원 중 가정관리 459.5조원 (2024) FACT · 식사 후 정리 40분/일 ASSUMPTION |
| 왜 Kitchen | 동작 종류가 적고 반복 (Pick · Place · Insert · Remove) · 작업영역 고정 · 물체 범위가 닫혀 있음 (기술). 매일 사용 · Remodeling / 입주라는 구매 계기 (사업) | 사업 가설 → WTP n ≥ 300 (M18) |
| 구조적 한계 | 주방마다 형태 · 가전 · 수납 · 치수 · 설치오차가 달라 범용 Robot은 집마다 인식 · 교시 · Calibration을 반복 → 설치시간 · 비용 · 신뢰성 문제 | 받은 평면 5종 중 3종 기본 배치 불가 (DERIVED) |
| 접근 | Object → Adaptive Hand · Task → Skill Library · Kitchen → Perception + Calibration · 반복 작업점 → Minimal Interface. 주방 전체 표준화는 하지 않음 | CONCEPT |
| 제품 | A Robot Module · B Manipulation Layer · C Calibration Layer · D Environment Interface · E Human-Robot Safety. CLEAN (첫 검증) → ASSIST (중기) → COOK (장기 R&D) | CONCEPT · FUTURE |
| 설치 경로 | 제품 하나 · 경로 셋: Retrofit 1,760만원 · Remodeling 2,020만원 · New-build Option 220만원 (B2B) + 입주 후 Robot | ASSUMPTION (VAT 별도) |
| BM | INSTALL → OPERATE (Rental 월 33만 · Care 연 48만 · 소모품 연 36만) → EXPAND (Skill 60만 · Tool 80만). 1세대 5년 매출 2,418만원 · 기여이익 428만원 (Y3 원가) → 798만원 (Y5 원가) | DERIVED (from ASSUMPTION) |
| 시장 | Bottom-up SAM 연 3,676억원 (Remodeling 3,212 · Retrofit 280 · New-build 184). Y5 계획 매출 91.5억원 = 대상 세대의 2.5% | DERIVED · TARGET |
| GTM | Phase 1 Premium Kitchen Remodeling (검증) → Phase 2 호환 주방 Retrofit → Phase 3 신축 B2B2C (Scale). 일반 시공은 Partner, MH는 Robot · Hand · Skill · Calibration · Interface 표준 · Safety · Commissioning | Partner 조건 협의 (M18~M24) |
| 자금 | 24개월 지출 23.4억원 = TIPS 정부지원 8억원 (Technology De-risking, 선정 시) + Seed 14~19억원 (Commercial Validation, Lean ~ Base). TIPS 미선정 시 Lean 범위 21.5억원 | DERIVED · TIPS 규정 FACT |
| 24개월 Evidence | 가정 3세대 CLEAN ≥ 90% · 주방 3종 Transfer 하락 ≤ 10%p · Calibration ≤ 4시간 · BOM · 설치 · Service 원가 실측 · WTP n ≥ 300 · 유료 전환 ≥ 2세대 · Partner 조건 · 출원 5건 | TARGET |

## 핵심 숫자

| 항목 | 값 | Tag · 산식 |
|---|---|---|
| 국내 아파트 (기회 기반, 구매시장 아님) | 약 1,328만호 | DERIVED (총주택 2,018.1만 × 65.8%, FACT) |
| 연간 주방 교체 (아파트) | 30만 세대 | ASSUMPTION (교차검증 29.0만 · 30.3만) |
| Remodeling Beachhead | 18,000세대/년 · 3,212억원 | DERIVED (30만 × Premium 10% × 적용 60%) |
| Robot System ASP | 1,490만원 | ASSUMPTION (WTP 검증 1순위) |
| Robot BOM Y1 시제품 → Y3 → Y5 | 1,680 → 1,180 → 915만원 | ASSUMPTION (공개가 Benchmark 기반) |
| Remodeling 1세대 설치 시점 매출 | 2,020만원 | DERIVED (Interface 450 + Robot 1,490 + 설치 80) |
| 1세대 5년 Lifetime Contribution | 428만원 (Y3) · 798만원 (Y5) | DERIVED |
| Y5 매출 · 설치 (Base Plan) | 91.5억원 · 560세대 | TARGET |
| 24개월 지출 | 23.4억원 | DERIVED (Bottom-up) |
| Seed 범위 | 14~19억원 (Lean 13.8억원 · Base 19.0억원) | DERIVED |
| TIPS 정부지원 (일반트랙 상한) | 8억원 · 24개월 · 정부 75% 이내 | FACT (상한) · 수령 = 선정 시 |

## TIPS와 Seed의 역할 분담

| 재원 | 목적 | 쓰는 곳 |
|---|---|---|
| TIPS 과제 10.67억원 (정부 8억원 + 기관부담 2.67억원) | 기술 검증 (Technology De-risking) | WP1 Adaptive Hand · WP2 Skill · WP3 Perception / Calibration · WP4 Minimal Interface · WP5 Safety · WP6 Integrated CLEAN 실증 |
| 민간 Seed | 사업 검증 · 과제 외 개발 (Commercial Validation) | 기관부담금 · 과제 외 인건비 8.65억원 (참여율 외 R&D · 사업 · 현장 · 경영지원) · 목업 운영 · 고객 검증 · WTP · 실증 · Partner 개발 · 운영사 선투자 요건 |

## 24개월 Gate (판단 기준)

| Gate | 확인할 Evidence | 통과 기준 (TARGET) | 미달 시 |
|---|---|---|---|
| M6 | Hand v1 vs 상용 Gripper (30종) · Robot Architecture 확정 · 평면 30개 분석 · 인터뷰 50명 | Coverage +15%p 또는 Tool 교체 50% 감소 | 상용 Gripper + 교체형 Pad로 전환 (Buy) · WP1 예산 재배분 |
| M12 | 목업 CLEAN 전 과정 · 식기 성공률 · 안전 기능 · 특허 출원 2건 | 식기 성공률 ≥ 80% · Safety 기능 동작 | Loading 범위로 축소 · Interface 보강 후 재시험 |
| M18 | 주방 3종 Transfer · Calibration 시간 · WTP n ≥ 300 · 예약금 Test · 인증 사전상담 | 하락 ≤ 10%p · Calibration ≤ 4시간 · WTP ≥ 30% (1,490만원) | Retrofit 보류 · Remodeling 집중 / 가격 · 구성 재설계 |
| M24 | 가정 3세대 실증 · 유료 전환 · BOM · 설치 · Service 원가 실측 · Partner 조건 · 출원 5건 | 가정 ≥ 90% · 유료 전환 ≥ 2세대 · 원가가 가정 범위 안 | Bridge 또는 범위 축소 후 재검증 (Series A 연기) |

## 가장 큰 Risk 5개

| 구분 | Risk | 확인 시점 | 대응 | 중단 · 재편 기준 |
|---|---|---|---|---|
| 기술 | 자체 Hand가 상용 Gripper보다 낫지 않음 | M6 30종 비교 | Buy 전환 · 교체형 Pad · Skill에 집중 | M6 열위 → 자체 Hand 중단 |
| 기술 | 주방이 바뀌면 성능 급락 (Calibration 과다) | M18 주방 3종 Transfer | Interface 보강 · Remodeling 채널 집중 | Calibration > 8시간 → Retrofit 보류 |
| 시장 | CLEAN 가치에 비해 가격이 높음 (WTP 부족) | M18 n ≥ 300 · 예약금 | Rental 중심 · 구성 · 가격 재설계 · ASSIST 묶음 | WTP < 15% → Seed 범위 재편 |
| 사업 | 설치 · A/S 원가 과다 | M24 가정 3세대 실측 | 원격진단 · Partner 교육 · 설치 표준 | 설치 > 2인 2일 → 채널 재검토 |
| 안전 · 인증 | 가정용 로봇 기준 불확실 (IEC 63682 발행 전) | M9 인증기관 사전상담 · M18 사전시험 | 저속 · Zone 분리 · 사람 감지 시 정지 · 표준 Gap 관리 | 인증 경로 미확정 → 판매 보류 |
