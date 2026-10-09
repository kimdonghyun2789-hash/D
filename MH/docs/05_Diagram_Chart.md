# 05. Diagram / Chart

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

## 핵심 Visual 8종 → 반영 위치

| # | 필수 Visual | 본문 (부록) | 이미지 · 도형 | 내용 |
|---|---|---|---|---|
| 1 | 실제 한국 Apartment 느낌의 MH Kitchen Robotics System Concept Rendering | 01 · 08 (부록 B3 · B4) | v2_cover · v2_after · v2_stow_1~5 · plan_old2a_* | 구축 2Bay 대표 평면 비율 · 상부장 하단 Rail · Robot Home · 식세기 Interface. 특정 단지 표기 없음 |
| 2 | Adaptive Robot Hand 확대도 | 06 | hand_hero | Quick Changer · 힘/토크 센서 · Wrist Camera · 교체형 Food-contact Pad · Palm Suction |
| 3 | Plate · Cup · Bowl · Tool Handling | 06 | hand_plate · hand_cup · hand_bowl · hand_tool | 접시 가장자리 Pinch · 컵 외벽 감싸기 · 그릇 테두리 Pinch · 국자 손잡이 Power Grasp (손가락 각도를 접촉점에 맞춰 계산) |
| 4 | 다양한 Kitchen → Calibration → 동일 Skill | 07 | 도형 (평면 도식 3) | Kitchen A ㅡ자 · B ㄱ자 · C Retrofit → Mapping · 기준점 · 가전/수납 위치 · Task Parameter → 같은 CLEAN Skill Library |
| 5 | Kitchen CLEAN Workflow | 09 | v2_seq_1~5 | 식기 인식 → Pick → Dishwasher Loading → Unloading → Storage Return |
| 6 | Existing / Remodeling / New-build 비교 | 10 | fig_flow_retrofit · fig_flow_remodel · fig_flow_newbuild + 표 | 같은 주방 · 같은 시점 3D 3컷 (Compact Mount · Rail · 설계 반영, CONCEPT) + Integration 수준 막대 + 6행 비교표 (고객 상황 · 공사 범위 · Interface · 설치 · 매출 가설 · 역할) |
| 7 | Robot + Skill + Calibration + Environment Interface Architecture | 08 | v2_after + A~E 층 카드 | A Robot Module · B Manipulation · C Calibration · D Environment Interface · E Safety |
| 8 | Business Model: Install → Operate → Expand | 11 | 도형 · 막대 | 3층 항목 · 가격 가설 + 1세대 5년 층별 막대 + Rental 3자 구조 |

표기: 제품 콘셉트 이미지 = `CONCEPT` · COOK · Robot Upgrade = `FUTURE CONCEPT`.

## 장별 도표와 Data 출처

| No | 장 | 도표 | Data 출처 (model.json key · xlsx 시트 · Source ID) |
|---|---|---|---|
| 01 | MH Robotics — Kitchen Manipulation Robot… | 3D 콘셉트 렌더 1개 (CONCEPT) | 렌더 v2_cover (CONCEPT) |
| 02 | 가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workfl… | 3D 주방 Workflow 그림 1개 (로봇 없음) + 압축 카드 4 + 작업 띠 + 핵심 숫자 4 | 렌더 fig_flow_kitchen (로봇 없음 · 가전 사이 사람 작업 ①~④) · 가계생산 위성계정 [S40] (FACT) · 정리 시간 a_cleanup_min (ASSUMPTION) |
| 03 | 주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간 | 2열 목록 + 결론 띠 | 정성 기준 (사업 가설) → WTP n ≥ 300 (M18) |
| 04 | 주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계 | 평면 재작도 주방 4컷 (동일 축척 Axonometric) + 변수 칩 + 반복 공정 체인 + 근거 표 | 렌더 fig_var_k_old2a · old2b · new3 · new4 (확보 평면 주방 재작도 · 동일 축척) · content.PLANS · LG CLOiD 보도 [S21] |
| 05 | Robot 적응 + 반복 작업점에만 최소 Interface | 4열 대응 Diagram | 대응 관계 = CONCEPT (기술 개발 전) |
| 06 | 핵심 Hardware: 주방 물체 대응 Adaptive Robot Han… | 3D 콘셉트 렌더 5컷 (CONCEPT) + 연결 체인 | Robotiq · Inspire 공개가 [S16 · S42] · 식품 접촉 규격 [S48] |
| 07 | 핵심 기술: Calibration 기반 Skill의 주방 간 이전 | 실행 체인 + Calibration 흐름도 (평면 도식 3개) | KPI 목표 (content.KPI, TARGET) |
| 08 | MH Kitchen Robotics System: 5개 Layer 통합 … | 3D 콘셉트 렌더 (CONCEPT) + 5층 Architecture | 렌더 v2_after (CONCEPT) · 안전 기준 [S39 · S47] |
| 09 | CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK… | 3D 콘셉트 렌더 5컷 (CONCEPT) + 단계 카드 | 렌더 v2_seq_1~5 (CONCEPT) · 가치 Anchor value.value · p_rent |
| 10 | 단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · … | 3D 콘셉트 렌더 3컷 (CONCEPT, 동일 시점) + Integration 수준 막대 + 3열 비교표 | 렌더 fig_flow_retrofit · remodel · newbuild (CONCEPT) · inputs p_rt_if · p_rr · p_rr_new · p_robot · p_comm · p_comm_rt · comm_cost · comm_cost_rt · kpi_links.inst_h |
| 11 | 설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM | 층별 가로 막대 + Rental 3자 구조도 | household.purchase_direct_Y3 / _Y5 · partner_irr.B · scenarios.B recurring · oe_share · inputs p_* (xlsx Household · Unit_Economics 시트) |
| 12 | Bottom-up 시장 산정: 세대 수 × 적용률 × 단가 | Bottom-up 시장 표 | market.B (xlsx Market 시트) · [S1~S6] |
| 13 | Premium Remodeling 검증 → Retrofit → 신축 B2… | 3단계 카드 + 누적 막대 (Y1~Y5) + 역할 분담 | scenarios.B rd · rp · rt · ni · kitchens (xlsx FM 시트, TARGET) |
| 14 | R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조 | 연결 Diagram + 표 + Tornado 막대 | kpi_links (inst_h · care_unit · bom · pad_life) · sens_household (xlsx Sensitivity) |
| 15 | 경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증 | 비교표 2개 + 결론 띠 | content.COMP · content.IP · [S19~S25 · S41 · S45 · S46 · S49~S51] |
| 16 | TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제… | 2열 비교 + 4구간 로드맵 + Gate | content.WP · content.GATES · TIPS 규정 [S33 · S52] |
| 17 | Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획 | 확인 항목 표 + 채용 계획 표 | model.TEAM · funding.team (xlsx Budget_24M) |
| 18 | 24개월 사용 23.4억원 · Seed 14~19억원 요청 (TIPS 8… | 사용처 표 + 4단계 흐름도 | funding.uses · tips.rows · funding.seed_* · post_seed_burn · breakeven_kitchens (xlsx Budget_24M · FM) |

도표 숫자 원천 = `model.json` (xlsx 수식 재계산값과 대조 완료)

## 3D 콘셉트 렌더 재생성

three.js + Playwright (Chromium) 기반. `MH/render3d`에서:

```bash
npm install                 # three 0.170 · playwright
bash render_v2.sh           # v2_cover · v2_after · v2_seq_1~5 · v2_stow_1~5 (충돌검사 포함)
bash render_plans.sh        # 대표 평면 (구축 2Bay A) 원본 · Interface 적용 · 충돌검사
bash render_hand.sh         # hand_hero · hand_plate · hand_cup · hand_bowl · hand_tool
bash render_fig_flow.sh     # fig_flow_kitchen (02 · 로봇 없음) · fig_flow_retrofit · remodel · newbuild (10 · CONCEPT)
bash render_fig_var.sh      # fig_var_k_* (04 · 확보 평면 주방 재작도 · 동일 축척) · fig_var_top_* (부록 B2)
```

PNG 옆 JSON = Callout 위치 (Anchor) · 충돌검사 결과
