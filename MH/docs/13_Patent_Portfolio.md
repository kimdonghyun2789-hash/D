# 13. Patent Portfolio (출원 후보)

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

## 출원 전략

- 현재 출원 0건 · 선행기술조사 M3 · 청구항 변리사 검토 예정 · 등록 가능성 미정
- 식기 로봇 · 주방 Rail Arm · 수납장 로봇 · 교체형 Gripper 부품 선행특허 존재 → 넓은 청구 대신 구체 구조 · 방법 청구
- 방어력 = 특허 + Grasp Data · Skill Library · Calibration 절차 · Interface 표준 · Installed Base Data 축적 (TARGET)

## 출원 후보 12개 묶음 (기술 영역별)

| 영역 | 출원 후보 (Family) | 사업 중요도 | 차별성 | Prior Art Risk (참고) | 우선순위 | 시점 |
|---|---|---|---|---|---|---|
| Robot Hand | Replaceable Food-contact Module (교체형 Pad · Tip, 마모 표시, 위생 결합 구조) | 상 (소모품 · 위생) | 중 | 중~상 (Schmalz OFG 마모부품 · Robotiq Fingertip) [S43 · S16] | 1 | M6~M9 |
| Robot Hand | Adaptive Finger Mechanism (얇은 Edge 집기 + 감싸쥐기 겸용, Edge Lip) | 상 | 중 | 상 (Dishcare US 11,731,282 Tapered Finger · 부족구동 Gripper 일반) [S49] | 2 | M9~M12 |
| Robot Hand | Compliance / Stiffness (젖은 유리 · 도자기 대응 가변 강성) | 중 | 중 | 중~상 | 3 | M15 |
| Robot Hand | Tool Interface (국자 · 집게 · 뚜껑 Tool 결합 · Dock) | 중 | 중 | 상 (EP 3,881,977 교체형 End piece · Tool Changer 일반) [S50] | 3 | M18 |
| Manipulation | Kitchen Object Handling (식세기 랙 형상 기반 식기 배치 계획) | 상 | 중 | 상 (Dishcraft US 10,507,584) [S49] | 2 | M12 |
| Manipulation | Failure Recovery (적재 실패 · 기울어짐 감지 후 다시 놓기) | 중 | 중 | 중 | 3 | M15 |
| Calibration | Kitchen Mapping (가전 · 수납 Registry + Template) | 상 | 중 | 중 (Minimanipulation · Instrumented Environment US 10,518,409) [S50] | 2 | M12 |
| Calibration | Task Coordinate Calibration (Robot Home · 가전 기준점 기반 좌표 보정) | 상 | 중~상 (가설) | 중 | 1 | M6~M9 |
| Interface | Robot Mount / Robot Home (보관 · 펼침 경로 · Rail 결합) | 상 | 중 | 상 (주방 벽 Rail Arm US 7,751,938 외 · 수납장 로봇 US 12,275,130) [S50] | 2 | M9 |
| Interface | Tool Dock · Storage Dock | 중 | 하~중 | 중 | 3 | M18 |
| Interface | Appliance Interface (식세기 랙 · 문의 Robot 대응 구조 · 연동) | 상 | 중 | 중 (US 2023/0165427 식세기 맞춤 Routine) [S49] | 2 | M12 |
| Safety | Human / Robot Zone Control (주방 평면 기반 Zone · 감속 · Robot Home 자동 복귀) | 중 | 중 | 중~상 (협동로봇 일반 기술) | 3 | M18 |

## 출원 계획

24개월 국내 출원 5건 (1순위 2건 M6~M9 · 2순위 3건 M12~M18) + PCT 1건 (M18, 1순위 중 1건) · M3 선행기술조사 (KIPRIS · USPTO · EPO · Google Patents) · 청구항 변리사 검토 · 등록 가능성 미정

| 시점 | 내용 |
|---|---|
| M3 | 선행기술조사 (KIPRIS · USPTO · EPO · Google Patents) · 예비 FTO |
| M6~M9 | 1순위 2건 출원 (Replaceable Food-contact Module · Task Coordinate Calibration) → M12 Gate 확인 항목 |
| M12~M18 | 2순위 5개 후보 중 3건 출원 (Robot Home · Appliance Interface · Kitchen Object Handling · Kitchen Mapping · Adaptive Finger 중, 실시예 확보 순) |
| M18 | PCT 1건 (1순위 중 1건) |

24개월 IP 예산 4,500만원 (선행조사 · 국내 5건 · PCT 1건, ASSUMPTION) — TIPS 연구활동비 편성 대상

## 참고 선행기술 (청구항 미검토)

| ID | 항목 | 내용 | 출처 |
|---|---|---|---|
| S16 | Gripper / Fingertip / Food-grade Suction Cup | Robotiq 2F-85 $4,999~ / OnRobot RG2 약 $3,200 / Robotiq Fingertip $175~195 / Piab Food-grade Silicone Cup £7~20 (FDA 21 CFR 177.2600) / 2026 판매가 2F-85 약 $5,825 (미국 리셀러, Coupling · Fingertip 포함) | https://qviro.com/product/robotiq/2f-85-robotiq/ , https://www.roboticscenter.ai/en/hardware/robotiq-2f-85 , https://automationdistribution.com/brands/Robotiq.html , https://uk.rubix.com/en/flat-suction-cups-f-silicone/p-G2010133211 , https://www.roboticscenter.ai/ko/blog/robotiq-gripper-guide |
| S43 | 식품 직접 접촉용 Finger Gripper (상용) | Schmalz OFG: 실리콘 파지부 · IP68 · 최대 80°C · 마모부품 Kit 별도 | https://www.schmalz.com/en/vacuum-technology-for-automation/vacuum-components/area-gripping-systems-and-end-effectors/finger-grippers/finger-grippers-ofg-312389/10.01.51.00001/ |
| S49 | 선행기술 — 식기 조작 로봇 | US 11,731,282 (Dishcare, 쌓인 식기 사이에 넣는 Tapered Finger · 수납 Module 통합) · US 10,507,584 (Dishcraft, 식기 인식 · 랙 적재) · WO 2018/031489 (Dishcraft, 자성 식기 Gripper) · US 2023/0165427 (가정용 식세기 맞춤 Routine) | https://patents.justia.com/patent/11731282 , https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10507584 , https://brevets-patents.ic.gc.ca/opic-cipo/cpd/eng/patent/3032941/summary.html , https://patents.justia.com/patent/20230165427 |
| S50 | 선행기술 — 주방 로봇팔 · Rail · 수납장 · Skill Library | US 7,751,938 외 3건 (주방 벽 Rail 이동 로봇팔 제어) · EP 3,881,977 (가전 · 주변 고정 모듈형 Arm, 교체형 End piece) · US 12,275,130 (수납장 내 Gantry 조리 로봇) · US 10,518,409 B2 (Minimanipulation Library · Instrumented Environment) | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7751938 , https://data.epo.org/publication-server/rest/v1.2/patents/EP3881977NWA1/document.html , https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12275130 , https://patents.google.com/patent/US10518409 |

## 우선순위 판단 기준

1. **사업 중요도**: 소모품 매출 · 설치시간 · 반복 설치에 직접 연결되는가 (Food-contact Module · Coordinate Calibration · Robot Home)
2. **차별성**: 주방 · 식기 · 가전 기준점이라는 구체 조건에서만 성립하는 구조 · 절차인가
3. **Prior Art Risk**: 일반 Gripper · Tool Changer · 협동로봇 안전 기술과 겹치는 정도
4. **시점**: Hand v1 (M4) · 목업 CLEAN (M12) 결과로 실시예가 생긴 뒤 출원
