# 06. Speaker Note (본문 18장)

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

발표 시간 배분 (15분 기준, 질의응답 별도)

| 구간 | 쪽 | 분 |
|---|:---:|---:|
| 표지 · Why (01~04) | 01~04 | 3.0 |
| How (05~09) | 05~09 | 4.5 |
| Business (10~13) | 10~13 | 3.5 |
| Proof (14~16) | 14~16 | 2.5 |
| Ask (17~18) | 17~18 | 1.5 |

## 01. MH Robotics — Kitchen Manipulation Robotics System

- MH Robotics: 다양한 실제 주방에서 식기 정리부터 조리까지 단계적으로 수행하는 주거용 Manipulation Robotics System
- 핵심: 로봇손 · 작업 Skill · Calibration · 주방 Interface의 단일 제품화
- 첫 검증 Workflow = CLEAN (식기 정리) → 같은 Platform에 ASSIST · COOK 단계적 추가
- 적용: 기존 주방 · Remodeling · 신축 → Installed Base 기반 Care · 소모품 · Skill 반복매출
- 현재 Concept 단계 (시제품 · 고객 · 계약 · 매출 없음) → Seed · TIPS 24개월 Evidence 확보 계획

## 02. 가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workflow

- 식세기 · 인덕션 · 냉장고 · 오븐 = 기기 안의 일만 자동화
- 식기 이동 · 식세기 적재 · 인출 · 수납 · 재료 투입 · 도구 조작 = 여전히 사람 몫
- 문제 정의: 개별 가전 기능이 아닌 주방 Workflow 전체의 Physical Manipulation 미자동화
- 근거: 2024 무급 가사노동 가치 582.4조원 · 그중 가정관리 (음식 준비 · 청소 등) 78.9% (가계생산 위성계정)
- 식사 후 정리 하루 약 40분 = 가설 → Time-diary 30세대로 검증 예정
- 가전 사이 사람 작업 흐름 ①~④: 식탁 → 싱크 → 식세기 → 조리대 → 수납장 (CLEAN 범위)

## 03. 주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간

- 기술: 동작 종류 적음 (집기 · 옮기기 · 놓기 · 넣기 · 빼기) · 작업영역 고정 (싱크 · 조리대 · 식세기 · 수납장)
- 물체 범위 닫힘: 접시 · 컵 · 그릇 · 수저 · 뚜껑 · 도구 → 이후 식재료
- 사업: 매일 사용 → 빠른 가치 체감 · 주방 Remodeling · 신축 입주 = 구매 계기
- Why now: 6축 Arm 가격 하락 ($6,999~) · 공개 조작 모델 (π0.5) · 가정용 로봇 안전기준 (IEC 63682 초안)
- 지불의사 = 별도 검증 (M18 WTP 조사 n ≥ 300 · 예약금 Test)

## 04. 주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계

- 가정용 로봇의 한계 = AI 성능만이 아닌 높은 환경 편차
- 집마다 다른 것: 주방 형태 · 가전 위치 · 모델 · 수납 위치 · 조리대 치수 · 물건 위치 · 동선 · 조명 · 설치 오차
- 범용 로봇 적용 시 집마다 인식 · Mapping · 교시 · Programming · Calibration · 검증 반복 → 설치시간 · 비용 · 신뢰성 좌우
- 확보 평면 5종: 싱크 벽 길이 약 2.6~3.3m · 3종 기본 배치 불가 · 1종 미검토
- MH 접근 = 모든 주방 표준화가 아닌 Robot 적응 + 필요한 지점만 Interface (다음 장)
- 확보 평면 4종 주방 재작도 (로봇 없음 · 동일 축척): ㄱ자 2종 · 반도형 2종 · 기본 한 줄 배치 수용 = 구축 2Bay A 1종

## 05. Robot 적응 + 반복 작업점에만 최소 Interface

- 접근: 주방 전체를 로봇에 맞게 바꾸는 방식이 아님
- 물체 다양성 → Adaptive Robot Hand · 작업 다양성 → Manipulation Skill Library
- 주방 차이 → Perception + Calibration (현장에서 좌표 · 가전 · 수납 위치 등록)
- 매일 반복되는 작업점 (Robot 대기 자리 · 도구 거치대 · 식세기 랙)에만 최소 Interface
- 환경 표준화 = 목적이 아닌 신뢰성 · 반복설치 수단 → 같은 Robot · Skill의 여러 주방 반복 적용

## 06. 핵심 Hardware: 주방 물체 대응 Adaptive Robot Hand

- 핵심 Hardware = 주방 물체를 다루는 로봇손
- 파지 방식: 접시 가장자리 Pinch · 컵 외벽 감싸기 · 그릇 테두리 Pinch · 국자 손잡이 파지
- 목표 = 손가락 수 · 자유도 경쟁이 아닌 작업 완료율 · 가격 · 위생 · 유지관리 · 내구성
- 식품 접촉 Pad · Tip = 교체형 Module → 위생 관리 + 소모품 매출
- 자체 Hand 우위 = 미검증 → M6 상용 Gripper (Robotiq 2F-85 등) 기준선과 30종 식기 비교, Coverage +15%p 또는 Tool 교체 50% 감소 시에만 채택

## 07. 핵심 기술: Calibration 기반 Skill의 주방 간 이전

- Skill = Software 구독이 아닌 Robot이 수행 가능한 작업을 늘리는 Layer
- 모든 Skill = 감지 → 파지 → 조작 → 검증 → 복구의 같은 구조 · 실패 감지 시 다시 잡기 · 내려놓기
- 핵심 = Skill의 주방 간 이전: 설치 시 주방 Mapping · 기준점 좌표 Calibration · 가전 · 수납 위치 등록 · 작업 Parameter 조정
- M18 검증: 구조 · 가전 모델이 다른 주방 3종에서 재배치 후 성공률 하락 ≤ 10%p · 현장 Calibration ≤ 4시간

## 08. MH Kitchen Robotics System: 5개 Layer 통합 제품

- 제품 = 5개 Layer 통합 (A Robot Module · B Manipulation · C Calibration · D Environment Interface · E Safety)
- A: Robot Arm (OEM 구매) · Adaptive Hand · Vision · 힘 · 안전 센서 · 필요 시 Rail · Dock
- B: 물체 인식 → 파지 · 경로 계획 → 실행 → 실패 감지 · 복구 / C: 주방 Mapping · 좌표 · 가전 · 수납 위치 등록
- D: Robot Home · 도구 · 수납 Dock · 가전 Interface · Vision 기준점 / E: 사람 감지 · 감속 · 충돌 감지 · 비상정지 · 안전 복귀
- 왜 Arm: 식세기 랙 · 서랍 · 상부장 작업 = 6축 방향 제어 필요 · 이동형은 낮은 작업점 · 가격 · 안전 부담
- Robot OEM과의 차이: Arm은 구매 · MH는 Hand · Skill · Calibration · Interface · Safety · Care로 주방 System 구성
- 주황 = Robot 작업 구역 · 회색 점선 = 사람 구역 (설계 개념)

## 09. CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장

- 첫 기술검증 Workflow = CLEAN: 조리대 한쪽 식기 인식 → 집기 → 식세기 적재 → 세척 후 인출 → 수납장 복귀
- CLEAN 목적 = 식기 정리 시장이 아닌 Platform 전체 (적응 파지 · 가전 · 수납 조작 · Calibration · 안전 · 실패 복구 · 반복 실행)의 첫 End-to-End 검증
- 이후 같은 Robot에 ASSIST Skill (재료 이동 · 투입 · 젓기 · 뚜껑 · 도구) 추가 → 장기 Recipe 단위 COOK
- CLEAN 단독 가사대체 가치 월 약 18만원 < Rental 월 33만원 → 지불의사 = Premium 고객 · ASSIST 묶음으로 검증 (M18)
- COOK = 현재 검증 결과가 아닌 장기 R&D 방향 (FUTURE)

## 10. 단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · 신축)

- 제품 1개 · 설치 경로 3개 (Integration 수준만 차등)
- Retrofit (기존 주방): 호환성 확인 → Compact Mount · Dock · Vision 기준점만 설치 · 현장 Calibration 비중 큼
- Remodeling: 주방 교체 시 Rail · Robot Home · 식세기 Interface · 수납 Dock 동시 시공 = 첫 검증 채널
- New-build: 설계 단계에서 Mount · 전원 · 통신 · Tool Dock · 가전 Interface · Service 공간 반영 → 입주 시 또는 후설치
- MH Core = Robot · Hand · Skill · Calibration · Interface 표준 · 안전 · 시운전 · 품질 / Partner = 철거 · 가구 · 전기 · 배관 · 일반 시공

## 11. 설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM

- BM 3층: INSTALL (Robot System · Interface · 설치) → OPERATE (Rental · Care · 소모품) → EXPAND (ASSIST Skill · Tool · 이후 COOK Skill · Upgrade)
- Remodeling 구매 1세대 5년: 설치 2,020만원 · 운영 366만원 · 확장 32만원
- 5년 기여이익 428만원 (Y3 원가) → 798만원 (Y5 원가)
- 반복 · 확장매출 = Y5 매출의 4% (설치 초기 구조) → Installed Base 누적 후 비중 확대
- Rental = 고객 초기 부담 완화 수단 · Pilot은 MH 직접 · Scale은 렌탈 · 캐피탈 Partner 자산 보유 (MH = 제품 · SW · Care)
- Partner 단순 회수 약 49개월 > 요구 36개월 (가정) → 매입가율 · 서비스료 · 기간 협의 필요

## 12. Bottom-up 시장 산정: 세대 수 × 적용률 × 단가

- 시장 산정 = 큰 TAM이 아닌 세대 수 × 적용률 × 단가
- 국내 아파트 약 1,328만호 = 기회 기반 (구매자 수 아님)
- Remodeling: 연 주방 교체 약 30만 × Premium 10% × 적용 60% = 연 약 1.8만 세대 · 3,212억원
- Retrofit: 호환 기존 주방 약 31.9만 세대 × 연 0.5% = 280억원 · 신축 184억원
- Y5 계획 매출 91.5억원 = 대상 세대의 약 2.5%
- 비율 = 전부 가정 → 견적 20건 · 평면 30개 분석 · 소비자 조사로 검증

## 13. Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장

- 초기 Mass Market 진입 없음
- Phase 1 Premium 주방 Remodeling: 제품 · 가격 수용성 · 설치 · 사용성 검증 → 첫 Reference · 실제 고객 Data
- Phase 2 호환 주방 Retrofit: 전체 Remodeling 없이 적용 가능한 고객 확대
- Phase 3 신축 B2B2C: 건설사 · 주방가구사 경유 Project 단위 확장
- 설치 물량 증가 ≠ 본사 현장인력 비례 증가: 철거 · 가구 · 전기 · 배관 = Partner / MH = Robot · Hand · Skill · Calibration · 안전 · 시운전
- Partner 조건 = M18~M24 협의 · 확보 예정

## 14. R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조

- R&D 목표 = 성능 향상 자체가 아닌 Unit Economics · Scale 개선
- Hand 고도화 → 다룰 수 있는 물체 ↑ · Skill → 작업 범위 ↑ · Calibration → 신규 주방 적용시간 ↓ · Interface → 작업 신뢰성 ↑
- 결과: 설치시간 · Engineering 비용 ↓ · 반복설치 ↑ → Installed Base ↑ → Care · 소모품 · Skill 매출 ↑
- 설치 · Calibration 원가 목표: Y2 실증 90만원 → Y3 60만원 → Y5 38만원 (설치 엔지니어 약 27인시 → 12인시)
- 1세대 5년 기여이익 최대 변수 = 고객 지불의사 · Robot BOM
- 방어력 = 특허 단독이 아닌 Grasp Data · Calibration 절차 · Interface 표준 · Installed Base 축적 (구축 예정)

## 15. 경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증

- 경쟁 존재: 가전사 (기기 내부 자동화 · 구독) · 조리 로봇 (전용 주방 · 조리대 기기) · Humanoid · 이동형 (범용 손 · 모델 학습) · Cobot + Gripper (부품) · 주방가구사 (시공)
- MH 목표 Position: 주방 물체용 Hand · CLEAN → COOK Skill 확장 · Calibration + 최소 Interface · 주방 공사 연계 설치 · Care · 소모품
- 우위 = 재배치 시간 · 경제성 실증으로 입증 필요
- 가전사 · 가구사 직접 진입 가능 (LG CLOiD 2028 목표) → Interface · 시공 Partner 후보로 설계
- IP 1순위: 교체형 식품접촉 Module · 가전 기준점 Calibration · 선행특허 존재 → 좁고 구체적인 청구 (등록 미정)
- Humanoid = 위협만이 아님: 공개 범용 모델 → MH 실행층 활용 · MH Interface · Skill → 다른 Robot에도 적용

## 16. TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발

- TIPS 과제 10.67억원 = 기술 위험 해소 (WP1 Hand · WP2 Skill · WP3 Perception · Calibration · WP4 최소 Interface · WP5 안전 · WP6 통합 CLEAN 실증)
- Seed = 기관부담금 · 과제 외 인건비 · 고객 검증 · 실증 운영 · WTP · Partner 개발 · BM 검증
- 일정 6개월 단위 · Gate별 판단 (계속 · 범위 축소 · 전환)
- M6 상용 Gripper 대비 Hand 비교 · M12 목업 CLEAN 전 과정 · M18 주방 3종 Transfer · WTP · M24 가정 실증 · 유료 전환 · 원가 실측

## 17. Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획

- 필요 핵심 역량 3개: 로봇 조작 (Hand · Skill) · 주방 · 건축 설치 (Interface · 시공 Partner) · 고객 · Partner 영업
- Founder 확인 항목 7개: Why This Problem · 관련 엔지니어링 경험 · 하드웨어 · 제품 개발 · Robot · 기계 · AI 역량 · 건설 · 주방 · 제조 지식 · 고객 · Partner 네트워크 · 전업 여부 · 지분
- 24개월 채용 계획: Founder 2명 포함 24개월 차 약 14명 · R&D 중심 · 리드 3명 (Manipulation · Perception · Hand) 우선 채용
- TIPS 요건: 대표 포함 창업팀 2인 이상 지분 60% 이상 · 정부지원 5억원당 청년 1명 신규 채용

## 18. 24개월 사용 23.4억원 · Seed 14~19억원 요청 (TIPS 8억원 별도)

- 투자 요청액 = 24개월 사용처 Bottom-up 산정 · 24개월 지출 약 23.4억원 (인건비 중심)
- Seed Base = 지출 − TIPS 정부지원 8억원 + Buffer 3개월 3.55억원 = 약 19.0억원
- Seed Lean (팀 · 목업 · 실증 축소) 약 13.8억원 · TIPS 미선정 시 Lean 범위 약 21.5억원
- 24개월 Evidence: 실제 주방 작동 시제품 · 주방 간 Transfer · BOM · 설치 · 서비스 원가 실측 · WTP · 유료 실증 · Partner 조건 · 특허 출원
- Series A 이후 Y3~Y4 현금 소요 약 68억원 → 후속 투자 기준 = 기술 성공 + 유료 전환 + 원가 Evidence
- 회사 정의: Hand · Skill · Calibration · Environment Integration 결합 → CLEAN 검증 → 같은 Platform에서 ASSIST · COOK 확장 → 기존 주방 · Remodeling · 신축 설치 → Installed Base 반복매출
