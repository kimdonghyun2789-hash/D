# 12. Technical KPI

> MH Robotics · Seed 투자 · TIPS 운영사 검토용 IR · Draft v5 · 2026-10-08  
> Concept 단계: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 숫자는 FACT / DERIVED / ASSUMPTION / TARGET, 그림은 CONCEPT로 표기.

## 원칙

- 정확한 목표 수치는 선행 Benchmark와 Prototype 결과로 설정. **근거 없는 정량목표는 두지 않음** → Benchmark가 없는 KPI는 "Baseline 측정 → 다음 Gate에서 설정".
- 공개 연구 Benchmark는 실험실 · 조건이 달라 직접 비교가 아님 (참고선).
- 모든 목표 = TARGET (또는 원가 연결 DERIVED · 사업 가정 ASSUMPTION).

## Manipulation (8)

| KPI | 정의 | Benchmark (출처) | M6 | M12 | M18 | M24 | 목표 근거 | Tag |
|---|---|---|---|---|---|---|---|---|
| Task Success Rate (CLEAN) | 식기 1개를 사람 개입 없이 집기 → 식세기 적재 (또는 인출 → 수납)까지 끝낸 비율 | Voysey 2021 식세기 적재 58.7% (실험실 · one-shot) · Dobb-E 81% (단순 가사 · 10가구) · TidyBot 85% [S36~S38] | Baseline 측정 | ≥ 80% (목업) | ≥ 85% (주방 3종) | ≥ 90% (가정 3세대) | 식사 1회 식기 20개 기준 사람 개입 ≤ 2건 = 90%. 공개 연구보다 높은 목표 = 환경 Interface 효과를 확인하는 지표 | TARGET |
| Object Coverage | 30종 한국 식기 · 도구 세트 중 Tool 교체 없이 파지 가능한 종류 | 공개 Benchmark 없음 (자체 세트 정의) | 상용 Gripper Baseline | ≥ 24/30 | ≥ 26/30 | ≥ 27/30 | Buy vs Build 판정: 상용 Gripper 대비 +15%p 이상이면 자체 Hand 채택 | TARGET |
| Human Intervention Rate | 식세기 1회분 (식기 20개)당 사람 개입 횟수 | - | 측정 | ≤ 4회 | ≤ 3회 | ≤ 2회 | Task Success Rate와 같은 기준의 사용자 체감 지표 | TARGET |
| Failure Recovery Rate | 감지된 실패 (미끄러짐 · 기울어짐 · 적재 실패) 중 자율 복구 비율 | 공개 Benchmark 없음 | - | Baseline 측정 | M12 결과로 설정 | M18 설정값 달성 | 근거 없는 수치 목표는 두지 않음 → M12 측정 후 확정 | TARGET |
| Cycle Time | 식기 1개 적재 평균 시간 | 사람 약 3~5초/개 (참고, 측정 필요) | 측정 | 측정 | ≤ 40초/개 | ≤ 30초/개 | 식기 20개를 10분 안에 적재 → 식후 사람이 없는 시간에 끝남 | TARGET |
| Grip Stability | 파지 중 낙하 · 미끄러짐 발생률 | - | 측정 | ≤ 1/200회 | ≤ 1/500회 | ≤ 1/1,000회 | Pad 1세트 수명 (약 5,500회) 동안 낙하 ≤ 5회 | TARGET |
| Slip Detection | 낙하 전 미끄럼 감지율 | GelSight 기반 실시간 감지 99% (일상 물체 10종 · 실험실) [S44] | - | ≥ 90% | ≥ 93% | ≥ 95% | 연구 수준보다 낮게 시작 (젖은 표면 · 저가 센서 조건) | TARGET |
| Hand Durability (Pad 수명) | Pad 교체 전 파지 횟수 (가속 시험) | - | - | 시험 설계 | 가속 시험 | ≥ 5,475회 | Grip Kit 분기 교체 가정 × 하루 60회 파지 (식기 20개 × 적재 · 인출 × 1.5회) | DERIVED |

## Application (설치 · 반복 적용) (5)

| KPI | 정의 | Benchmark (출처) | M6 | M12 | M18 | M24 | 목표 근거 | Tag |
|---|---|---|---|---|---|---|---|---|
| Calibration Time | 새 주방에서 현장 Calibration 완료 시간 | - | - | ≤ 8시간 (목업) | ≤ 4시간 (주방 3종) | ≤ 4시간 (가정) | 설치 · Calibration 원가 Y3 60만원 = 약 18인시 (2인 1일) 안에 설치까지 끝내야 함 | DERIVED |
| Site Programming Time | 주방별 Custom 코드 · 교시 시간 | - | - | 측정 | Custom 코드 0 · 교시 ≤ 1시간 | 동일 | Template Skill만 써야 반복설치 가능 | TARGET |
| Installation Time | Robot 설치 + Calibration + Safety Check (Interface 시공 제외) | - | - | - | 측정 | Remodeling 2인 1일 · Retrofit 2인 2일 이내 | 설치 원가 가정과 연동 (Remodeling 약 18인시 · Retrofit 약 29인시, Y3) | DERIVED |
| Kitchen Compatibility | 분석 평면 · 상담 주방 중 적용 가능 비율 | 받은 평면 5종 중 2종 기본 배치 수용 (DERIVED) | 평면 30개 분석 | - | 상담 주방 실측 | - | 가정 Remodeling 60% · Retrofit 40%를 실측으로 대체 | ASSUMPTION |
| Task Transferability | 주방 재배치 후 성공률 하락 (같은 Skill) | - | - | - | ≤ 10%p (주방 3종) | ≤ 10%p (가정) | Platform 반복 적용의 핵심 증거 | TARGET |

## Business (7)

| KPI | 정의 | Benchmark (출처) | M6 | M12 | M18 | M24 | 목표 근거 | Tag |
|---|---|---|---|---|---|---|---|---|
| Robot BOM | Robot System 1대 원가 (Adaptive Hand 포함) | 공개가 Benchmark (부록 B6) | 1,680만원 (Pilot) | - | 100대/년 견적 | 견적 ≤ 1,180만원 (Y3 가정) | Robot ASP 1,490만원에서 Hardware 마진 확보 (민감도 2순위) | ASSUMPTION |
| Installation Cost | 1세대 설치 · Calibration 실비 | - | - | - | 목업 기준 | 실측 ≤ 90만원 (Y2 가정) | 가정 3세대 실측 | ASSUMPTION |
| Service Cost | 고장 방문 (A/S) 1회 원가 · 연 발생 횟수 | - | - | - | - | 실측 (가정 연 0.6회) | Failure Rate 민감도 (1.2회 시 1세대 5년 −84만원) | ASSUMPTION |
| Care Cost | 정기 방문 · 원격진단 · Cloud 연 원가 | - | - | - | - | 실측 ≤ 40.8만원/대·년 | Care 요금 48만원/년 대비 마진 | ASSUMPTION |
| WTP | 시스템 1,490만원 이상 지불 의향 비율 (Premium 리모델링 상담 고객) | - | 인터뷰 50명 (정성) | - | n ≥ 300 조사 · 예약금 Test | - | 판정 기준 ≥ 30% (가설). 15% 미만이면 가격 · 구성 재설계 | TARGET |
| Pilot Conversion | 가정 실증 3세대 중 유료 전환 | - | - | - | 실증 착수 | ≥ 2세대 | 실증 50% 할인 → 정가 전환 의향 | TARGET |
| Consumables Cost | Grip Kit 원가율 (물류 포함) | Robotiq Fingertip $175~195 (참고) [S16] | - | - | 견적 | ≤ 35% | 소모품 마진 가정 검증 | ASSUMPTION |

## KPI ↔ 원가 연결 (Base, DERIVED)

| 연결 지표 | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---:|---:|---:|---:|---:|
| 설치 · Calibration 인시 (Remodeling) | 36.5 | 27.4 | 18.2 | 13.7 | 11.6 |
| 설치 · Calibration 인시 (Retrofit) | 48.6 | 39.5 | 28.9 | 22.8 | 18.8 |
| Care 방문 1회 인시 | 4.6 | 4.0 | 3.3 | 2.7 | 2.4 |
| Care 원가 (만원/대 · 년) | 44.8 | 40.8 | 36.8 | 28.3 | 26.8 |
| Robot BOM (만원) | 1,680 | 1,520 | 1,180 | 1,030 | 915 |

인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 약 3.3만원 (연 6,600만원 기준). Pad 수명 목표 5,475회 = 하루 60회 파지 × 365 ÷ 4 (분기 교체).

## Adaptive Hand 시험 계획 (Buy vs Build, WP1)

| 항목 | 내용 | Tag |
|---|---|---|
| 시험 물체 (30종) | 접시 대 · 중 · 소 (도자기 · 멜라민) · 밥공기 · 국그릇 · 면기 · 컵 · 머그 · 유리잔 · 물병 · 수저 · 젓가락 · 냄비뚜껑 (유리 · 금속) · 집게 · 국자 · 뒤집개 · 보관용기 (유리 · Plastic) · 쟁반 · 도마 (소) | TARGET (세트 정의) |
| 조건 | 건조 / 젖은 표면 · 세제 잔여 · 식기 겹침 · 식세기 랙 (하단 · 상단 · 수저통) · 수납 서랍 · 상부장 | TARGET |
| 비교군 (Buy) | Robotiq 2F-85 (약 $5,825) · 저가 전동 Parallel Gripper · Suction Cup (식품용 실리콘) · Soft Finger (Fin-ray형) | FACT (가격) |
| 자체 Hand (Build) | v1 (M4): 2+1 손가락 저구동 + 교체형 Pad · v2 (M10): Edge Lip · Slip 감지 · v3 (M18): 내구 · 위생 · 원가 | CONCEPT |
| 측정 지표 | 종류별 성공률 · Tool 교체 횟수 · 파손 · 낙하 · 미끄럼 감지 · Cycle Time · Pad 마모 · 세척 후 성능 · 단가 | TARGET |
| 판정 (M6) | Coverage +15%p 이상 또는 Tool 교체 50% 감소 → 자체 Hand 채택 · 아니면 상용 Gripper + 교체형 Pad (Buy) | TARGET |
| 식품 접촉 규격 | 식품위생법 "기구" · 「기구 및 용기 · 포장의 기준 및 규격」 고무제 (실리콘) 재질 · 용출 · 해외: FDA 21 CFR 177.2600 · EU 1935/2004 (수출 시) | FACT [S48] |
| 연구 참고 | GelSight 기반 실시간 미끄럼 감지 99% (일상 물체 10종 · 실험실) · 식세기 적재 연구 58.7% (트레이 25개) | FACT [S36 · S44] |

자체 Hand 채택 조건 = 성공률 · Tool 교체 횟수 · 원가 중 하나 이상에서 명확한 우위. 우위가 없으면 상용 Gripper + 교체형 Pad (Buy)로 전환하고 Skill · Calibration에 집중.
