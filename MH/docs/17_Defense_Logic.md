# 17. 각 질문의 방어논리

> MH Robotics · IR 내부 검토용 (제출 제외) · 2026.10

답변 기준: 미검증 항목 = "미검증" 명시 + 확인 Gate · Evidence 제시

## Q1. 왜 Kitchen인가?

- **방어논리**: 동작이 적고 반복되며 (Pick · Place · Insert · Remove), 작업영역이 정해져 있고 (싱크 · 식세기 · 수납), 다룰 식기 종류가 한정돼 있어 기술 검증이 가능함. 매일 쓰고 주방 리모델링 · 입주라는 구매 계기가 있어 사업 검증도 가능. CLEAN → COOK 확장 경로
- **근거 (Tag)**: 가정관리 무급노동 459.5조원 (2024, FACT) · 연 주방 교체 약 30만 (ASSUMPTION)
- **약한 부분**: 지불의사 미검증 → M18 WTP
- **위치**: 본문 · 부록 03

## Q2. 왜 Robot Arm인가?

- **방어논리**: 식세기 랙 · 서랍 · 상부장 작업은 위치 · 자세 제어가 필요해 6축 Arm이 맞음. 전용 기계는 식기 · 주방마다 재설계, 이동형은 하단 작업 · 가격 · 안전 부담. Arm은 Skill · Tool로 ASSIST · COOK 확장
- **근거 (Tag)**: FAIRINO FR5 $6,999 · xArm 6 $8,399 (FACT) → BOM 하락 경로
- **약한 부분**: Pilot BOM 중 Arm 950만원 → OEM · 국산 Partner 필요
- **위치**: 본문 · 부록 08 · B6

## Q3. 기존 Appliance로 해결 불가능한가?

- **방어논리**: 식세기는 세척만 하고 넣기 · 꺼내기 · 수납은 가전 밖의 일. 가전 개선은 사람 작업을 줄일 뿐 이동 · 적재는 남음. MH는 가전과 경쟁하지 않고 가전 사이를 잇는 Appliance Interface를 만듦
- **근거 (Tag)**: -
- **약한 부분**: 가전사가 로봇을 내장할 가능성 → Q15
- **위치**: 본문 · 부록 02

## Q4. CLEAN만으로 고객이 돈을 내는가?

- **방어논리**: 아직 모름 (핵심 미검증 가설). 가치 Anchor: 식후 정리 40분/일 × 가사서비스 1.5만원/h × 자동화 60% ≈ 월 18만원 vs Rental 월 33만원 → Gap 존재. 그래서 Premium Remodeling 고객부터, CLEAN은 Platform 검증용, ASSIST 확장 · 위생 · 편의 가치를 묶어 WTP 조사
- **근거 (Tag)**: 가사서비스 요금 1.5만원/h (FACT) · 정리 40분 (ASSUMPTION)
- **약한 부분**: 가치 Gap 명시 · WTP n ≥ 300 + 예약금 (M18)
- **위치**: 본문 · 부록 03 · 11

## Q5. COOK까지 기술적으로 연결 가능한가?

- **방어논리**: 같은 Arm · Hand · Calibration · Safety를 쓰고, 추가 항목은 Skill · Tool · 식품접촉 규격 · 열/액체 안전. 24개월 범위는 CLEAN, ASSIST가 중간 단계, COOK은 장기 R&D (FUTURE). 공개 범용 모델 (π0.5) 발전이 Skill 확장 속도를 높일 수 있음
- **근거 (Tag)**: openpi π0 · π0.5 공개 (FACT) [S46]
- **약한 부분**: 조리 안전 · 위생 규격 부담 큼
- **위치**: 본문 · 부록 09

## Q6. 상용 Gripper를 쓰면 안 되는가? 왜 자체 Hand인가?

- **방어논리**: 처음엔 상용 Gripper로 시작해 비교 기준을 잡고 M6에 30종 식기로 비교. 자체 Hand 가설: 얇은 접시 Edge + 컵 · 그릇 감싸쥐기를 Tool 교체 없이, 젖은 표면 미끄럼 감지, 교체형 식품접촉 Pad (위생 · 소모품), 목표 원가. 우위가 없으면 Buy로 전환 (중단 기준)
- **근거 (Tag)**: Robotiq 2F-85 약 $5,825 (FACT) vs 자체 Hand 원가 가정 Pilot 200만원 → Y5 85만원
- **약한 부분**: 자체 개발 비용 · 기간
- **위치**: 본문 · 부록 06

## Q7. 주방마다 다른데 실제 적용 가능한가?

- **방어논리**: 모든 주방이 아니라 호환 주방부터. 적용률 Remodeling 60% · Retrofit 40% (가정) → 평면 30개 분석 (M6). Calibration (Mapping · 기준점 · Template)으로 타 주방 적용, M18 주방 3종 하락 ≤ 10%p · ≤ 4시간
- **근거 (Tag)**: 확보 평면 5종 중 3종 기본 배치 불가 · 1종 미검토 (DERIVED)
- **약한 부분**: 표본 작음
- **위치**: 본문 · 부록 04 · 07

## Q8. 환경 Integration이 과도한 공사를 요구하지 않는가?

- **방어논리**: Remodeling은 주방 공사와 동시에 진행 (Interface 증분 450만원 = Premium 주방 2,000~4,000만원의 약 11~23%). Retrofit은 Compact Mount · Dock만 (150만원). New-build는 설계 단계 반영. 인테리어 시공은 Partner
- **근거 (Tag)**: Premium 주방 가격대는 ASSUMPTION (견적 20건으로 검증)
- **약한 부분**: Retrofit 호환률 미검증
- **위치**: 본문 · 부록 10

## Q9. 결국 Interior Company 아닌가?

- **방어논리**: 아님. Remodeling 세대당 5년 매출 2,418만원 중 Interface는 450만원 (약 19%), 나머지는 Robot · Care · 소모품 · Skill. 시공은 Partner, MH Core는 Robot · Hand · Skill · Calibration · Interface 표준 · Safety · 시운전
- **근거 (Tag)**: 설치 원가 목표 90 → 38만원 (ASSUMPTION)
- **약한 부분**: 초기 Remodeling 채널 의존
- **위치**: 본문 · 부록 10 · 13

## Q10. A/S 비용이 너무 크지 않은가?

- **방어논리**: Care 원가 Build-up (Y3): 방문 2회 × 11만원 + 고장 0.6회 × 18만원 + Cloud 4만원 = 연 36.8만원 vs Care 요금 48만원 → 마진 23% (Y3) → 44% (Y5, 원격진단 · 동선 밀도). 고장 1.2회/년 (Warranty 6% 동반) 시 세대당 5년 −84만원
- **근거 (Tag)**: ASSUMPTION (실측 없음)
- **약한 부분**: M24 실거주 3세대 실측 필요
- **위치**: 본문 · 부록 14 · D3

## Q11. Rental이 자본집약적이지 않은가?

- **방어논리**: Pilot만 MH 직접 보유, Y4부터 Rental · Capital Partner가 자산 보유 (ASP의 88%에 매입, MH 서비스료 월 6만원, Partner IRR 약 13.1%). MH B/S 부담 지양. 단, Partner 단순 회수기간 약 49개월 > 요구 36개월 (가정) → 매입가율 · 서비스료 · 기간 협의 (M24)
- **근거 (Tag)**: 코웨이 국내 렌탈 계정 748만 (2026 1Q) · LG 가전 구독 매출 2조원+ (2025) (FACT)
- **약한 부분**: Partner 조건 미확인 → M24
- **위치**: 본문 · 부록 11 · D3

## Q12. Care에 고객이 돈을 내는가?

- **방어논리**: Care는 소프트웨어 구독이 아니라 고가 로봇의 안전 · 성능 유지 계약 (정기점검 · Calibration · 원격진단 · A/S). 가전 구독의 정기관리 수요가 선례. 가입률 70%는 가정이며 실증에서 확인
- **근거 (Tag)**: LG 케어매니저 약 4,000명 · 정기관리 포함 구독 (FACT) [S41]
- **약한 부분**: 가입률 미검증
- **위치**: 본문 · 부록 11

## Q13. Consumables가 실제 필요한가?

- **방어논리**: 억지 Lock-in이 아니라 식품 · 식기 접촉 Pad · Seal의 마모 · 위생 교체. 교체주기는 Pad 수명 시험 (M18~M24)으로 확정. 구매 고객 기대 매출은 연 약 25만원으로 비중이 작음
- **근거 (Tag)**: 식품위생법 "기구" · 고무제 규격 (FACT) [S48]
- **약한 부분**: 교체주기 미검증
- **위치**: 본문 · 부록 06 · 11

## Q14. Humanoid가 발전하면?

- **방어논리**: 위협이자 기회. 공개 범용 모델은 MH Manipulation Layer에 활용 가능. Humanoid도 주방에서는 하단 작업 · 위생 · 안전 · 가격 ($20,000 · 월 $499) 제약이 있음. MH의 Interface · Skill · Calibration 자산은 다른 Robot Platform에도 적용 가능 (Interface 표준 제공자 Position)
- **근거 (Tag)**: 1X NEO 가격 · Figure 식세기 시연 · LG CLOiD 2028 목표 (FACT)
- **약한 부분**: Humanoid 가격 급락 시 가격 압박
- **위치**: 본문 · 부록 15

## Q15. Samsung / LG / Kitchen Furniture Company가 직접 하면?

- **방어논리**: 가능성 있음 (LG CLOiD 2028 상용화 목표). 대응: 가전사 · 가구사는 Partner · 채널 후보 (Appliance Interface · 주방 시공), MH는 설치 · Calibration Know-how와 Installed Base Data로 차별화, 좁은 IP (Food-contact Module · 기준점 Calibration)
- **근거 (Tag)**: 한샘 등 가구사의 로봇 협업 보도 없음 (2026) [S51]
- **약한 부분**: 대기업 진입 시 채널 협상력 약함
- **위치**: 본문 · 부록 15

## Q16. Robot OEM과 무엇이 다른가?

- **방어논리**: OEM은 Arm을 파는 회사, MH는 Arm을 사서 Hand · Skill · Calibration · Interface · Safety · Care로 주방 System을 만드는 회사. OEM은 공급 Partner이자 BOM 하락 경로
- **근거 (Tag)**: -
- **약한 부분**: 핵심 부품 OEM 의존
- **위치**: 본문 · 부록 08

## Q17. 실제 핵심 IP는 무엇인가?

- **방어논리**: 1순위: 교체형 Food-contact Module, Task Coordinate Calibration (Dock · 가전 기준점). 2순위: Robot Home · Appliance Interface · 식기 Handling. 식기 로봇 · 주방 Rail 선행특허가 있어 넓은 청구는 어렵고 구체 구조 · 방법 청구를 목표. 실제 방어력은 Data · 절차 · Installed Base
- **근거 (Tag)**: US 11,731,282 · US 10,507,584 · US 7,751,938 등 (FACT, 청구항 미검토)
- **약한 부분**: IP 단독 방어력 약함 · 등록 미정
- **위치**: 본문 · 부록 15 · E1

## Q18. 20억원 전후 Seed가 필요하다면 왜 그 규모인가?

- **방어논리**: Bottom-up: 24개월 지출 23.41억원 (인건비 15.3억원 · 24개월 차 약 14명) − TIPS 8억원 + 3개월 Buffer 3.55억원 = 18.96억원 (≈ 19억원). Lean (팀 · 범위 축소, 지출 19.1억원) 13.8억원. TIPS 미선정 시 Lean 범위 21.5억원
- **근거 (Tag)**: TIPS 규정 (FACT) · 비용 (ASSUMPTION)
- **약한 부분**: 인건비 · 채용 속도 가정
- **위치**: 본문 · 부록 18 · A6 · A7

## Q19. 24개월 뒤 어떤 Evidence가 있어야 후속투자가 가능한가?

- **방어논리**: 실거주 3세대 CLEAN ≥ 90% · 유료 전환 ≥ 2세대 · 주방 3종 적용 하락 ≤ 10%p · Calibration ≤ 4시간 · BOM · 설치 · Service 원가 실측 · WTP n ≥ 300 (1,490만원 ≥ 30%) · Partner 조건 (리모델링 1 · 렌탈/캐피탈 1) · 출원 5건
- **근거 (Tag)**: TARGET
- **약한 부분**: 실증 3세대는 표본이 작음
- **위치**: 본문 · 부록 16 · 18

## Q20. Founder가 왜 적합한가?

- **방어논리**: [Founder 정보 필요] — 현재 답할 수 없음. 필요한 역량은 로봇 조작 (Hand · Skill), 주방 · 건축 시공 (Interface · 시공 Partner), 고객 · 파트너 영업의 세 축. 이 칸이 채워지기 전에는 투자 판단 불가
- **근거 (Tag)**: 없음
- **약한 부분**: 가장 큰 공백
- **위치**: 본문 · 부록 17
