# 11. TIPS R&D Work Package

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

## TIPS 과제 = 기술 검증 (Technology De-risking) · Seed = 사업 검증 + 과제 외 개발

| 구분 | TIPS 과제 | 민간 Seed |
|---|---|---|
| 목적 | 기술 검증 (Technology De-risking) | 사업 검증 (Commercial Validation) · 과제 외 개발 |
| 범위 | Adaptive Robot Hand · Manipulation · Calibration · Safety · Reliability · Integrated Workflow | 기관부담금 · 과제 외 인건비 8.65억원 (참여율 외 R&D · 사업 · 현장 · 경영지원) · Full-scale Mock-up 운영 · Customer Validation · Pilot · WTP · Partner Development · BM Validation |
| 결과물 | Hand v3 · CLEAN Skill Library · Calibration Tool · Interface 표준 · Safety Architecture · 실증 보고서 | WTP 조사 · 예약금 · 유료 전환 · Partner 조건 · BOM · 설치 · Service 원가 |
| 판단 Gate | M6 Hand Buy/Build · M12 목업 CLEAN · M18 타 주방 적용 | M18 WTP · M24 유료 전환 · 원가 |

TIPS 편성 = R&D 인력 (참여율분) · 연구재료 · 시험 · 인증 사전시험 · IP · 간접비 / Seed = 기관부담금 · 과제 외 인건비 · 고객 검증 · 실증 운영 · 사업개발 · 운영비

## TIPS 2026 규정

| 항목 | 내용 | Tag |
|---|---|---|
| 정부지원 R&D (일반트랙) | 최대 8억원 · 최대 24개월 | FACT [S33] |
| 정부지원 비율 | 총 연구개발비의 75% 이내 · 기관부담 25% 이상 (그중 현금 10% 이상) | FACT [S33] |
| 운영사 선투자 | 수도권 2억원 이상 · 비수도권 1억원 이상 (Seed 라운드에 포함) | FACT [S33] |
| 창업팀 요건 | 대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 지분 30% 이하 | FACT [S33] |
| 고용 | 정부지원 5억원당 청년 1명 신규 채용 | FACT [S33] |
| 비R&D 연계 | 창업사업화 · 해외마케팅 각 최대 1.5억원 (선정 뒤 별도 신청, 본 계획 미반영) | FACT [S33] |
| 접수 | 분기별 접수 (운영사 추천) | FACT [S52] |

## Work Package (WP1~WP6)

| WP | 이름 | 기간 | 목표 | 주요 내용 | 산출물 | KPI | 담당 (채용 계획) |
|---|---|---|---|---|---|---|---|
| WP1 | Adaptive Kitchen Robot Hand | M1~M24 | 주방 식기 · 도구 30종을 Tool 교체 없이 하나의 손으로 | 상용 Gripper 비교군 (M1~M6) · Hand v1 (M4) · v2 (M10) · v3 (M18) · 교체형 Food-contact Module · Grip Force · Slip Detection · 내구 · 위생 시험 (세척 · 열 · 세제) | Hand v3 · 30종 파지 Data · 내구 시험 결과 | Object Coverage · Grip Stability · Slip Detection · Pad 수명 | Hand · 기구 리드 · Hand 센싱 · Manipulation 리드 |
| WP2 | Kitchen Manipulation Skill | M3~M24 | CLEAN Skill을 Template으로 만들어 주방마다 재사용 | Pick · Place · Insert (식세기 랙) · Remove · Open/Close · Failure Detection · Recovery · Skill Template · 공개 범용 모델 (π0 계열) Fine-tune 검토 | CLEAN Skill Library v1 | Task Success · Intervention · Recovery · Cycle Time | Manipulation 리드 · Robot SW · Skill/Data |
| WP3 | Kitchen Perception / Calibration | M2~M24 | 새 주방에서 4시간 내 같은 Skill 실행 | 식기 30종 인식 Dataset · Kitchen Mapping · Coordinate Calibration (Dock · 가전 기준점) · Appliance / Storage Position Mapping · Task Parameter | Calibration Tool · 현장 절차서 | Calibration Time · Task Transferability | Perception 리드 · Skill/Data |
| WP4 | Minimal Environment Interface | M3~M22 | 필요한 곳에만 표준 Interface | Robot Home (보관 · 펼침) · Tool Dock · 수납 Dock · 식세기 Interface (랙 · 문) · Vision 기준점 · Retrofit Compact Mount · 설치 표준 | Interface 표준 v1 · 설치 표준서 | Installation Time · Compatibility · 표준부품 사용률 | 임베디드 · 전기 · 안전 · Hand 리드 · 설치 엔지니어 |
| WP5 | Human-Robot Safety | M4~M24 | 사람 곁 주방에서 안전 기준 충족 | Zone 감시 · 감속 · 정지 · 충돌 감지 · 비상정지 · Robot Home 자동 복귀 · 위험성평가 · 표준 Gap (ISO 10218-2:2025 · IEC 63682 초안 · ISO 13482) · 전기안전 · EMC 사전시험 | Safety Architecture · 사전시험 결과 | 감속 250mm/s · 접촉력 기준 충족 · 사전시험 통과 | 임베디드 · 전기 · 안전 · 시험 · 신뢰성 |
| WP6 | Integrated CLEAN 실증 | M9~M24 | 목업 → 주방 3종 → 실거주 3세대로 끝까지 검증 | 1:1 목업 CLEAN (M9~M12) · 주방 3종 적용 시험 (M13~M18) · 실거주 3세대 실증 · 연속 운전 신뢰성 (M19~M24) | 실증 보고서 · BOM · 설치 · Service 원가 실측 | Task Success (가정 ≥ 90%) · Pilot Conversion | 시험 · 신뢰성 · 설치 엔지니어 · 사업개발 |

KPI 정의 · 목표 근거: [12_Technical_KPI.md](12_Technical_KPI.md). Gate: [14_Roadmap_24M.md](14_Roadmap_24M.md)

## TIPS 과제 편성 (Base, 만원, ASSUMPTION)

| 비목 | 내용 | 1차년도 | 2차년도 | 합계 | 구분 |
|---|---|---:|---:|---:|:---:|
| 인건비 (현금) | R&D 인원 8명 × 참여율 40~60% | 20,655 | 32,520 | 53,175 | 현금 |
| 인건비 (현물) | Founder 2인 × 참여율 50~60% | 6,600 | 6,600 | 13,200 | 현물 |
| 연구재료비 | Robot Hardware · Hand Prototype · Kitchen Mock-up | 13,240 | 6,880 | 20,120 | 현금 |
| 연구활동비 | Software · Data · Certification · IP | 4,700 | 6,825 | 11,525 | 현금 |
| 연구수당 | 현금 인건비 × 5% | 1,033 | 1,626 | 2,659 | 현금 |
| 간접비 | 직접비 비례 (공간 · 관리비 일부 충당) | 2,749 | 3,238 | 5,988 | 현금 |
| **합계** |  | 48,977 | 57,689 | **106,667** |  |

| 점검 | 값 | 판단 |
|---|---|---|
| 정부지원 (75%) | 80,000 | 상한 충족 |
| 기관부담 (25%) | 26,667 | 현금 + 현물 |
| 기관부담 현금 | 13,467 | 현금 ≥ 10% 충족 (51% of 기관부담) |
| 기관부담 현물 | 13,200 | Founder 인건비 참여분 |
| 간접비율 | 6.8% | 협약 기준 확인 필요 |

- 인건비는 R&D 인원 8명 (참여율 40~60%) 현금 + Founder 2인 현물. 연구수당 = 현금 인건비 × 5%
- 회사 전체 24개월 지출 23.4억원 중 TIPS 과제 10.67억원, 나머지는 Seed ([15_Funding_Plan.md](15_Funding_Plan.md))
