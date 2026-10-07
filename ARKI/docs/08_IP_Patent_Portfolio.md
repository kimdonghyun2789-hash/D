# 08. IP / Patent Portfolio (후보)

> ARKI Robotics (가칭) · Seed Investment Proposal · Draft v1 · 2026-10-07 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·Partner 없음.

> 등록 가능성을 주장하지 않음. 아래 10개 Family는 **출원 후보**이며 전부 TO BE VALIDATED (선행기술조사 필요). 특정 특허번호는 조사 전이므로 기재하지 않음.

## Patent Family 후보

| # | Family | Protectable Core | Business Relevance | Possible Prior Art Risk | 분류 후보 |
|---|---|---|---|---|---|
| 1 | 주방가구 일체형 Robot Rail · Dock · Storage 구조 | 상부장 하단 Rail과 Robot Garage의 일체 구조 · 가구가 아닌 구조체로의 하중 전달 경로 | 높음 — 모든 Rail형 제품의 기반 | 높음 — 천장 Rail 양팔 로봇주방(Moley 계열), 상부장 하단 Rail 양팔(삼성 Bot Chef Concept) 등 선례 존재 → 청구범위를 "가구 일체 Garage + 구조체 정착 Frame" 조합으로 좁혀야 할 가능성 | B25J 5/02, A47B 77/00 (확인 필요) |
| 2 | Robot-ready Kitchen Interface Module | Mount · 전원 · 통신 · Sensor · Tool Dock을 한 Module로 표준화한 주방가구 Interface 규격 | 높음 — Land 상품(신축 Option)의 핵심 | 중간 — 가전 Built-in 규격·가구 Interface 일반 기술 | A47B 77/00 · H02J (확인 필요) |
| 3 | Fold / Deploy Robot Storage System | 키큰장 내부 수납 Robot의 전개·복귀 기구, 문 Interlock | 중간 — Compact 평형 (Case A) | 중간 — 가전 Lift 기구 · 수납형 Robot | B25J 5/00 · A47B (확인 필요) |
| 4 | Human Zone / Robot Zone 기반 Safety Control | 주방 Zone Map 기반 감속·정지 · 통로 위 운반 금지 Logic | 높음 — 안전 인증·고객 수용성 | 높음 — 산업용 Speed & Separation Monitoring · 협동로봇 안전 특허 다수 | B25J 9/16 · B25J 19/06 · F16P 3/14 (확인 필요) |
| 5 | Kitchen End-effector | 한식 식기(밥공기·국그릇·접시) 형상 대응 Gripper + Suction 복합 | 중간 | 중간 — 식품·물류 Gripper | B25J 15/00 (확인 필요) |
| 6 | Food-contact Consumable Cartridge | 교체형 식품접촉 Tip·Pad 체결 구조 · 교체주기 인식 | 중간 — 반복매출 근거 | 중간 — 교체형 Gripper Pad | B25J 15/00 (확인 필요) |
| 7 | Installation Auto Calibration | 설치 후 Kitchen 기준점 Target 기반 자동 좌표 보정 · Template 좌표 불러오기 | 높음 — 설치시간·설치원가 | 중간 — Robot Calibration 일반 기술 | B25J 9/16 · G05B (확인 필요) |
| 8 | Dishwasher Robot Interface | 상향 Housing 식세기의 Door·Rack 위치 표준 · Robot 투입·인출 연동 | 높음 — 첫 제품 핵심 Task | 중간 — 가전사의 Robot 연동 특허 가능성 | A47L 15/00 · A47L 15/50 (확인 필요) |
| 9 | Robot Cleaning / Sanitizing Dock | Garage 내 End-effector 세척·건조·위생 관리 | 중간 — 위생·식품접촉 | 낮음~중간 | A47L · B08B (확인 필요) |
| 10 | Kitchen Layout 기반 Robot Module Selection | 평면·치수 입력 → Layout Family 분류 → Architecture·Module 자동 선택 Software | 중간 — 표준화·Design Lead Time | 낮음~중간 — 설계 자동화 SW (SW 특허 적격성 검토 필요) | G06F 30 · G06Q (확인 필요) |

## 선행기술조사 계획 (Seed M0~M3)

1. 검색 DB: KIPRIS · Google Patents · Espacenet · USPTO.
2. 검색 축: (a) Kitchen + Robot Arm + Rail/Gantry/Ceiling (b) Robot + Dishwasher Loading/Unloading (c) Cabinet-integrated / Retractable Robot (d) Zone-based Safety + Domestic Robot (e) Robot Installation Calibration + Furniture.
3. 우선 확인 대상 (선례가 공개된 주체): Moley Robotics 로봇 주방 특허 Family · Samsung (Bot Chef · Bot Handy) · LG (CLOiD 관련) · Sunday Robotics · 주방가구·빌트인 가전사의 Robot 연동 출원.
4. 산출: Family별 FTO 위험 (High/Medium/Low) · 청구범위 차별 포인트 · 출원 우선순위.

## 출원 우선순위 가설

- 1순위 (사업 핵심 + 선행 위험 상대적 낮음 추정): ② Interface Module · ⑦ Auto Calibration · ⑧ Dishwasher Interface.
- 2순위: ① Rail·Dock·Storage 일체 구조 (선행 위험 높음 → 구조체 정착 Frame·Garage 조합으로 범위 설계) · ④ Zone Safety.
- 3순위: ③ · ⑤ · ⑥ · ⑨ · ⑩ (Prototype 이후 실제 구조 확정 시).
- Seed 목표: KR 출원 5~8건 + PCT 1~2건 (비용은 Use of Funds Safety/Certification/IP 항목에 포함, ASSUMPTION).

## Moat에서 IP의 위치

IP는 7개 Moat Layer 중 L5. 경쟁사가 Hardware를 확보해도 복제하기 어려운 것은 **Kitchen Template Library (L2) · Installation Standard (L3) · Care/Service Data (L6) · Installed Base (L7)**라는 가설이며, 특허는 이를 보완하는 수단 (21장).
