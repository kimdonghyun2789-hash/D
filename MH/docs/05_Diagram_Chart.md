# 05. Diagram / Chart

> MH Robotics · Seed 투자 · TIPS 운영사 검토용 IR · Draft v5 · 2026-10-08  
> Concept 단계: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 숫자는 FACT / DERIVED / ASSUMPTION / TARGET, 그림은 CONCEPT로 표기.

## 필수 Visual 8종 (Spec 36) → 반영 위치

| # | 필수 Visual | 본문 (부록) | 이미지 · 도형 | 내용 |
|---|---|---|---|---|
| 1 | 실제 한국 Apartment 느낌의 MH Kitchen Robotics System Concept Rendering | 01 · 08 (부록 B3 · B4) | v2_cover · v2_after · v2_stow_1~5 · plan_old2a_* | 구축 2Bay 대표 평면 비율 · 상부장 하단 Rail · Robot Home · 식세기 Interface. 특정 단지 표기 없음 |
| 2 | Adaptive Robot Hand 확대도 | 06 | hand_hero | Quick Changer · 힘/토크 센서 · Wrist Camera · 교체형 Food-contact Pad · Palm Suction |
| 3 | Plate · Cup · Bowl · Tool Handling | 06 | hand_plate · hand_cup · hand_bowl · hand_tool | 접시 가장자리 Pinch · 컵 외벽 감싸기 · 그릇 테두리 Pinch · 국자 손잡이 Power Grasp (손가락 각도를 접촉점에 맞춰 계산) |
| 4 | 다양한 Kitchen → Calibration → 동일 Skill | 07 | 도형 (평면 도식 3) | Kitchen A ㅡ자 · B ㄱ자 · C Retrofit → Mapping · 기준점 · 가전/수납 위치 · Task Parameter → 같은 CLEAN Skill Library |
| 5 | Kitchen CLEAN Workflow | 09 | v2_seq_1~5 | 식기 인식 → Pick → Dishwasher Loading → Unloading → Storage Return |
| 6 | Existing / Remodeling / New-build 비교 | 10 | 도형 · 표 | Integration 수준 막대 + 6행 비교표 (고객 상황 · 공사 범위 · Interface · 설치 · 매출 가설 · 역할) |
| 7 | Robot + Skill + Calibration + Environment Interface Architecture | 08 | v2_after + A~E 층 카드 | A Robot Module · B Manipulation · C Calibration · D Environment Interface · E Safety |
| 8 | Business Model: Install → Operate → Expand | 11 | 도형 · 막대 | 3층 항목 · 가격 가설 + 1세대 5년 층별 막대 + Rental 3자 구조 |

모든 제품 콘셉트 이미지는 `CONCEPT`, COOK · Robot Upgrade는 `FUTURE CONCEPT`로 표기. 과도한 Humanoid · SF 주방 · 미래도시 · 광고 카피 없음.

## 장별 도표와 Data 출처

| No | 장 | 도표 | Data 출처 (model.json key · xlsx 시트 · Source ID) |
|---|---|---|---|
| 01 | MH Robotics — Kitchen Manipulation Robot… | 3D 콘셉트 렌더 1개 (CONCEPT) | 렌더 v2_cover (CONCEPT) · 현재 단계 = FACT (Evidence 없음) |
| 02 | 가전은 자동화됐지만, 가전 사이의 일은 아직 사람이 합니다 | 카드 4 + 작업 띠 + 핵심 숫자 4 | 가계생산 위성계정 [S40] (FACT) · 정리 시간 a_cleanup_min (ASSUMPTION) |
| 03 | 주방은 기술과 사업성을 함께 검증하기 좋은 첫 공간입니다 | 2열 목록 + 결론 띠 | 정성 기준 (사업 가설) → WTP n ≥ 300 (M18) |
| 04 | 집마다 주방이 달라, 같은 로봇을 반복 설치하기 어렵습니다 | 변수 Grid + 반복 공정 체인 | 받은 평면 5종 재작도 (부록 B2, DERIVED) · LG CLOiD 보도 [S21] |
| 05 | 로봇이 적응하고, 주방은 필요한 곳만 맞춥니다 | 4열 대응 Diagram | 대응 관계 = CONCEPT (기술 개발 전) |
| 06 | 핵심 Hardware: 주방 물체를 다루는 Adaptive Robot H… | 3D 콘셉트 렌더 5컷 (CONCEPT) + 연결 체인 | Robotiq · Inspire 공개가 [S16 · S42] · 식품 접촉 규격 [S48] |
| 07 | 같은 Skill을 다른 주방으로 옮기는 것이 핵심 기술입니다 | 실행 체인 + Calibration 흐름도 (평면 도식 3개) | KPI 목표 (content.KPI, TARGET) |
| 08 | MH Kitchen Robotics System: 다섯 개 층을 하나의 … | 3D 콘셉트 렌더 (CONCEPT) + 5층 Architecture | 렌더 v2_after (CONCEPT) · 안전 기준 [S39 · S47] |
| 09 | CLEAN은 첫 검증 Workflow이고, 제품 범위는 주방 전체입니다 | 3D 콘셉트 렌더 5컷 (CONCEPT) + 단계 카드 | 렌더 v2_seq_1~5 (CONCEPT) |
| 10 | 제품은 하나, 설치 경로는 세 가지입니다 | Integration 수준 막대 + 3열 비교표 | inputs p_rt_if · p_rr · p_rr_new · p_robot · p_comm · p_comm_rt · comm_cost · comm_cost_rt · kpi_links.inst_h |
| 11 | 설치로 시작해, 쓰는 동안 반복매출이 쌓이는 3층 구조입니다 | 층별 가로 막대 + Rental 3자 구조도 | household.purchase_direct_Y3 / _Y5 · partner_irr.B · steady · inputs p_* (xlsx Household · Unit_Economics 시트) |
| 12 | 큰 TAM 대신, 세대 수 × 적용률 × 단가로 시작 시장을 계산합니다 | Bottom-up 시장 표 | market.B (xlsx Market 시트) · [S1~S6] |
| 13 | 고객의 돈과 설치비를 먼저 검증하고, 파트너로 늘립니다 | 3단계 카드 + 누적 막대 (Y1~Y5) + 역할 분담 | scenarios.B rd · rp · rt · ni · kitchens (xlsx FM 시트, TARGET) |
| 14 | R&D 성과가 설치비 · 서비스비 · 확장매출로 이어지는 구조입니다 | 연결 Diagram + 표 + Tornado 막대 | kpi_links (inst_h · care_unit · bom · pad_life) · sens_household (xlsx Sensitivity) |
| 15 | 경쟁은 이미 있습니다. 차이는 주방 적용 방식이며, 실증으로 증명합니다 | 비교표 2개 + 결론 띠 | content.COMP · content.IP · [S19~S25 · S41 · S45 · S46 · S49~S51] |
| 16 | TIPS는 기술 위험을, Seed는 사업 위험을 줄이는 데 씁니다 | 2열 비교 + 4구간 로드맵 + Gate | content.WP · content.GATES · TIPS 규정 [S33 · S52] |
| 17 | 투자 판단의 첫 질문은 팀입니다. Founder 칸은 아직 비어 있습니다 | 확인 항목 표 + 채용 계획 표 | model.TEAM · funding.team (xlsx Budget_24M) |
| 18 | 24개월 23.4억원 계획: TIPS 8억원 + Seed 14~19억원 | 사용처 표 + 4단계 흐름도 | funding.uses · tips.rows · funding.seed_* (xlsx Budget_24M) |

숫자가 들어간 도표는 모두 `model.json`에서 직접 읽어 그림 (손으로 입력한 숫자 없음). xlsx는 같은 입력으로 수식 재계산 후 `check_xlsx.py`로 대조.

## 3D 콘셉트 렌더 재생성

three.js + Playwright (Chromium) 기반. `MH/render3d`에서:

```bash
npm install                 # three 0.170 · playwright
bash render_v2.sh           # v2_cover · v2_after · v2_seq_1~5 · v2_stow_1~5 (충돌검사 포함)
bash render_plans.sh        # 대표 평면 (구축 2Bay A) 원본 · Interface 적용 · 충돌검사
bash render_hand.sh         # hand_hero · hand_plate · hand_cup · hand_bowl · hand_tool
```

각 PNG 옆 JSON = Callout 위치 (Anchor) · 충돌검사 결과. 렌더는 실물 · 성능 증거가 아님 (CONCEPT).
