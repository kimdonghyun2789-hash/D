# 04. 각 Slide Visual 구성

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

공통: 16:9 · 흰 배경 · 짙은 회색 글자 · 주황은 Robot Zone / Path / Key Number만 · 상단 Kicker (번호 · 구성명) → 결론형 제목 → 부제 → 본문 → 하단 출처 · 각주 → Footer

## 01. MH Robotics — Kitchen Manipulation Robotics System

- **구성**: 좌측 짙은 패널: 회사명 · 제품 정의 · CLEAN → ASSIST → COOK · 현재 단계. 우측 3D 콘셉트 렌더: 구축 아파트 주방 한 벽 (Robot Home · Rail · 식기세척기 Interface)
- **도표 유형**: 3D 콘셉트 렌더 1개 (CONCEPT)
- **사용 이미지**: `assets/renders/v2_cover.png`, `assets/renders/fig_flow_kitchen.png`
- **CONCEPT 표기**: 렌더 우하단 [CONCEPT RENDERING]

## 02. 가전 자동화 이후에도 사람이 하는 주방 Physical Workflow

- **구성**: 좌측 3D 주방 그림 (로봇 없음): 냉장고 · 인덕션 · 오븐 · 식기세척기 = 가전 내부 자동화 (흰 라벨) · 가전 사이 사람 작업 = 짙은 점선 ①~④ (식탁 → 싱크 → 식세기 → 조리대 → 수납장) + 사람 형상. 우측: 가전 4종 압축 카드 (가전 내부 자동화) · 짙은 띠 Physical Task 10개 (①~④ = CLEAN 범위). 하단 공식: Appliance Automation ≠ Physical Workflow Automation · 근거 숫자 4개
- **도표 유형**: 3D 주방 Workflow 그림 1개 (로봇 없음) + 압축 카드 4 + 작업 띠 + 핵심 숫자 4
- **사용 이미지**: `assets/renders/fig_tech_m03_kitchen.png`

## 03. 주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간

- **구성**: 좌측 3D 콘셉트 그림 (CONCEPT): 확보 평면 구축 2Bay A 주방 + MH Interface · 주황 = Robot 작업영역 (싱크대 벽 일자 구간 고정) · 라벨 Robot Home · 싱크 · 수납 · 식세기 · 인덕션 (측면). 우측 2열: Robot Engineering 기준 4개 · Business 기준 4개 (번호 + 굵은 제목 + 한 줄 근거). 하단 결론 띠
- **도표 유형**: 3D 콘셉트 그림 1개 (CONCEPT) + 2열 목록 + 결론 띠
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)

## 04. 주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계

- **구성**: 좌측 상단: 확보 평면 4종 주방 3D 재작도 4컷 (구축 2Bay A · B · 신축 3Bay · 4Bay, 도면 그대로 · 로봇 없음 · 같은 시점 · 동일 축척) + 평면명 · 주방 형태 · 기본 일자 배치 가능/불가 캡션. 좌측 하단: 주방마다 달라지는 9개 변수 칩. 우측 세로 체인: 범용 Robot 적용 시 집마다 반복되는 6단계 (Perception → Validation) + 결론 상자. 하단 전체 폭: 근거 2행 (확보 평면 5종 · 공개 사례)
- **도표 유형**: 평면 재작도 주방 4컷 (동일 축척 Axonometric) + 변수 칩 + 반복 공정 체인 + 근거 표
- **사용 이미지**: `assets/renders/fig_tech_m05_hand.png`, `assets/renders/v2_seq_3_load.png`, `assets/renders/v2_seq_1_detect.png`, `assets/renders/v2_stow_2_open.png`

## 05. 로봇이 주방에 적응 + 반복 작업 위치에만 최소 Interface

- **구성**: 4열 대응표: 위 회색 칩 = 변동 요인 (Object · Task · Kitchen · 반복 작업 위치), 아래 카드 = MH 기술 (Hand · Skill · Calibration · Interface) + 카드마다 3D 콘셉트 그림 1개 (CONCEPT · 같은 크기): 같은 Hand의 국자 · 컵 · 접시 파지 · 식세기 적재 · 조리대 식기 인식 · Robot Home · Rail. 하단 짙은 결론 띠
- **도표 유형**: 4열 대응 Diagram + 3D 콘셉트 그림 4컷 (CONCEPT)
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)

## 06. 핵심 Hardware: 식기 · 도구 대응 Adaptive Robot Hand

- **구성**: 좌측 Hand 확대 렌더 (Quick Changer · 힘/토크 센서 · Wrist Camera · 교체형 Food-contact Pad · Palm Suction 표시) + 접시 · 컵 · 그릇 · 국자 파지 4컷 (각 CONCEPT). 우측 식기 · 도구 파지의 어려움 · 핵심 기술 후보 · Buy vs Build Gate. 하단 Hand → 사업성 연결 띠
- **도표 유형**: 3D 콘셉트 렌더 5컷 (CONCEPT) + 연결 체인
- **사용 이미지**: `assets/renders/hand_hero.png`, `assets/renders/hand_plate.png`, `assets/renders/hand_cup.png`, `assets/renders/hand_bowl.png`, `assets/renders/hand_tool.png`
- **CONCEPT 표기**: Hand 확대 렌더 · 파지 렌더 4컷 각각 [CONCEPT]

## 07. 핵심 기술: Calibration 기반 Skill의 타 주방 적용

- **구성**: 상단: Skill 실행 5단계 체인 (인식 → 파지 → 조작 → 확인 → 복구, 실패 시 복구 루프). 하단: 서로 다른 주방 3종 평면 도식 → Calibration 4요소 → 같은 CLEAN Skill Library
- **도표 유형**: 실행 체인 + Calibration 흐름도 (평면 도식 3개)
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)
- **CONCEPT 표기**: 평면 도식 범례 (CONCEPT)

## 08. MH Kitchen Robotics System: 5개 Layer 통합 제품

- **구성**: 좌측 대표 콘셉트 렌더 (주황 = Robot Working Zone, 회색 점선 = Human Zone) + Interface 위치 표시. 우측 A~E 5개 층 카드 (Robot Module · Manipulation · Calibration · Environment Interface · Safety)
- **도표 유형**: 3D 콘셉트 렌더 (CONCEPT) + 5층 Architecture
- **사용 이미지**: `assets/renders/v2_after.png`
- **CONCEPT 표기**: 렌더 좌상단 [CONCEPT]

## 09. CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장

- **구성**: 상단 CLEAN 5단계 콘셉트 렌더 (식기 인식 → 집기 → 식세기 적재 → 꺼내기 → 제자리 수납, 각 CONCEPT). 중간 CLEAN 검증 기술 칩 9개. 하단 CLEAN · ASSIST · COOK 3단계 카드 (같은 Platform + Skill · Tool 확장)
- **도표 유형**: 3D 콘셉트 렌더 5컷 (CONCEPT) + 단계 카드
- **사용 이미지**: `assets/renders/v2_seq_1_detect.png`, `assets/renders/v2_seq_2_pick.png`, `assets/renders/v2_seq_3_load.png`, `assets/renders/v2_seq_4_unload.png`, `assets/renders/v2_seq_5_store.png`
- **CONCEPT 표기**: 렌더 5컷 각각 [CONCEPT] · COOK 카드 [FUTURE CONCEPT]

## 10. 단일 제품 · 3가지 설치 유형 (기존 주방 · Remodeling · 신축)

- **구성**: 상단 3열 머리 (Retrofit · 주방 공사 연계 · 설계 반영 + 시공 범위 막대). 열마다 같은 주방 · 같은 시점 3D 콘셉트 렌더 1개 (CONCEPT): 기존 주방 = Compact Mount · Vision 기준점 · Drop Zone (Rail 없음) / Remodeling = Rail · Robot Home · 수납 Dock · 식세기 Interface / New-build = Tool Dock · 점검 공간 · 전원 · 통신 매립. 주황 = Robot Zone · Path만. 아래 압축 비교표 6행 (고객 상황 · 공사 범위 · Interface · 설치 · MH 매출 가설 · 역할). 하단 MH Core vs Partner 띠
- **도표 유형**: 3D 콘셉트 렌더 3컷 (CONCEPT, 동일 시점) + 시공 범위 막대 + 3열 비교표
- **사용 이미지**: `assets/renders/fig_flow_retrofit.png`, `assets/renders/fig_flow_remodel.png`, `assets/renders/fig_flow_newbuild.png`

## 11. 설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3단계 BM

- **구성**: 좌측 3단계 사업모델 (INSTALL · OPERATE · EXPAND): 층마다 짙은 라벨 + 제품 콘셉트 그림 1컷 (Rail 장착 Robot System · 식세기 적재 / 교체형 Pad 손끝 + 가는 회색 지시선 / 국자 Tool 파지, 각 CONCEPT) + 항목 · 가격 가설. 우측 상단 대표 세대 5년 매출 막대 (층별) + 공헌이익. 우측 하단 Rental 구조 도식 (고객 · Capital Partner · MH)
- **도표 유형**: 층별 3D 콘셉트 그림 3컷 (CONCEPT) + 층별 가로 막대 + Rental 3자 구조도
- **사용 이미지**: `assets/renders/v2_seq_3_load.png`, `assets/renders/hand_hero.png`, `assets/renders/hand_tool.png`

## 12. Bottom-up 시장 산정: 세대 수 × 적용률 × 단가

- **구성**: 좌측 짙은 박스: 아파트 재고 1,328만호 (잠재 대상) + 노후 · 거래 FACT + 재고 대비 연 주방 교체 약 30만 막대 (재고 ≠ 실구매 시장). 우측 4개 시장 Funnel 표 (산식 · 대상 세대 · 패키지 단가 · 연 규모) + SAM 합계 · SOM. 우하단 채널 구성 막대: 연 대상 세대 (① · ② · ③) → × 패키지 단가 → 연 규모 (억원) 100% 막대 2개 + 연결 띠 · Y5 계획 560세대 = 같은 축척 막대 (약 2.5%)
- **도표 유형**: Bottom-up 시장 표 + 채널 구성 100% 막대 2개 (세대 → 억원, 연결 띠) + Y5 비교 막대 + 재고 대비 연 교체 막대
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)

## 13. Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장

- **구성**: 상단 3단계 카드 (Phase 1 Premium Remodeling → Phase 2 Retrofit → Phase 3 New-build). 좌하단 연도별 설치 세대 누적 막대 (채널별, TARGET). 우하단 MH Core vs Partner 역할 분담 도식
- **도표 유형**: 3단계 카드 + 누적 막대 (Y1~Y5) + 역할 분담
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)

## 14. R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조

- **구성**: 좌측 연결 Diagram: R&D 4개 Lever → 결과 지표 → 공통 효과 (설치시간 · Engineering 비용 ↓, 반복 설치 ↑) → Installed Base → 반복 · 확장 매출. 우측 KPI ↔ 원가 표 (Y2 · Y3 · Y5) + 민감도 상위 5개 막대. 하단 Moat 정의 띠
- **도표 유형**: 연결 Diagram + 표 + Tornado 막대
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)

## 15. 경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증

- **구성**: 좌측 경쟁 비교표 (5개 Category + MH 목표 Position × 5개 비교 축, 공개 자료 기준). 우측 IP 후보 5개 영역 (출원 후보 · 선행기술 Risk · 우선순위). 하단 Humanoid 대응 띠
- **도표 유형**: 비교표 2개 + 결론 띠
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)

## 16. TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발

- **구성**: 상단 좌우 비교: TIPS 과제 (WP1~WP6, 기술 검증) vs 민간 Seed (사업 검증 · 과제 외 개발). 중간 24개월 4구간 일정 (0~6 · 7~12 · 13~18 · 19~24M): 구간 머리 아래 같은 크기 콘셉트 그림 (Hand v1 · 접시 · 컵 파지 / 주방 CLEAN 경로 · 식세기 적재 / 서로 다른 주방 3종 / 가정 주방 Robot Zone · 사람 공존, 각 CONCEPT) + 구간별 과업 목록. 하단 Gate 4개 (M6 · M12 · M18 · M24) 판단 기준
- **도표 유형**: 2열 비교 + 4구간 로드맵 (구간별 3D 콘셉트 그림, CONCEPT 8컷) + Gate
- **사용 이미지**: `assets/renders/hand_hero.png`, `assets/renders/hand_plate.png`, `assets/renders/hand_cup.png`, `assets/renders/v2_cover.png`, `assets/renders/apt2_kitchen.png`, `assets/renders/apt3_kitchen.png`, `assets/renders/apt4_kitchen.png`, `assets/renders/v2_after.png`

## 17. Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획

- **구성**: 좌측 Founder 확인 항목 7행 × Founder 2인 (입력 전 [Founder 정보 필요]) + 하단 월별 인원 누적 막대 (M1~M24 · Founder · R&D · 사업 · 현장 · 경영지원 · Y1 · Y2 평균 FTE 선). 우측 24개월 채용 계획 표 (역할 · 시작 월 · 구분) + 인원 요약 띠
- **도표 유형**: 확인 항목 표 + 월별 인원 누적 막대 (FTE, 24개월) + 채용 계획 표
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)

## 18. 24개월 사용 23.4억원 · Seed 14~19억원 요청 (TIPS 8억원 별도)

- **구성**: 좌측 24개월 사용처 표 (억원) + 재원 · Seed 산식. 우측 Value Creation 흐름: TODAY → Seed + TIPS → 24M TARGET (기술 · 경제성 · 시장 Evidence) → NEXT ROUND (회사 정의로 마무리)
- **도표 유형**: 사용처 표 + 4단계 흐름도
- **사용 이미지**: 없음 (도형 · 표 · 텍스트)
