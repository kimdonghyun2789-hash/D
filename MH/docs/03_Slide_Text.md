# 03. 각 Slide 실제 화면 문구 (본문 18장)

> MH Robotics · Seed 투자 · TIPS 운영사 검토용 IR · Draft v5 · 2026-10-08  
> Concept 단계: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 숫자는 FACT / DERIVED / ASSUMPTION / TARGET, 그림은 CONCEPT로 표기.

- PPTX에 들어간 문구를 화면 표기 순서대로 옮긴 것 (빌드 시 자동 기록). 표는 `셀 | 셀` 형태.
- `[FACT]` 등 대괄호는 화면의 작은 Tag. 부록 문구는 PPTX와 주제별 문서 (07~19)에 있음.

## 01. MH Robotics — Kitchen Manipulation Robotics System

```text
M H   R O B O T I C S
Kitchen Manipulation
Robotics System
로봇손 · 작업 Skill · Calibration · 주방 Interface를 하나의 제품으로
다양한 실제 주방에서 식기 정리부터 조리까지 단계적으로 확장하는 주거용 Manipulation Robotics
CLEAN
첫 검증 Workflow (식기 정리)
ASSIST
중기 확장 (재료 이동 · 투입 · 도구)
COOK
장기 R&D 방향 (Recipe Workflow)
Seed 투자 · TIPS 운영사 검토용  |  2026.10.08  |  Draft v5
Concept 단계 — 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 수치는 FACT · DERIVED · ASSUMPTION · TARGET 구분
Robot Home (Dock)
Rail (필요 시)
식기세척기 Interface
[CONCEPT RENDERING]
```

## 02. 가전은 자동화됐지만, 가전 사이의 일은 아직 사람이 합니다

```text
01  문제
가전은 자동화됐지만, 가전 사이의 일은 아직 사람이 합니다
개별 가전 기능의 자동화는 진행됐지만, 주방 Workflow 전체의 Physical Manipulation은 아직 사람 몫
기기 안
식기세척기
세척 자동화
기기 안
인덕션
가열 자동화
기기 안
냉장고
보관 자동화
기기 안
오븐
조리 일부 자동화
가전 사이에서 사람이 하는 Physical Task
식기 이동
식세기 적재
식세기 인출
수납
식재료 이동
재료 투입
조리도구 Handling
젓기
뚜껑 조작
조리 후 정리
앞 5개 = 첫 검증 범위 CLEAN과 직결
Appliance Automation  ≠  Physical Workflow Automation
582.4조원
무급 가사노동 가치 (2024)
[FACT]
78.9%
그중 가정관리 (음식 준비 · 청소 등) 459.5조원
[FACT]
132분
1인당 하루 가사노동 (2024, 2019년 137분)
[FACT]
약 40분
하루 식사 후 정리 (식기 이동 · 식세기 · 수납)
[ASSUMPTION]
출처: 국가데이터처 2024 가계생산 위성계정 (2026.4, 보도 인용) [S40]. 식사 후 정리 40분은 가설 → 30세대 시간 기록 (Time-diary)으로 검증.
```

## 03. 주방은 기술과 사업성을 함께 검증하기 좋은 첫 공간입니다

```text
02  왜 Kitchen인가
주방은 기술과 사업성을 함께 검증하기 좋은 첫 공간입니다
감성이나 미래 이미지가 아니라 Robot Engineering과 사업성 기준
Robot Engineering 기준
01
Pick · Move · Place · Insert · Remove 집중
동작 종류가 적고 반복 → Skill Library로 묶기 쉬움
02
작업영역이 정해져 있음
Sink · Counter · Dishwasher · Storage → Calibration 대상이 명확
03
물체는 다양하지만 범위가 닫혀 있음
접시 · 컵 · Bowl · 수저 · 뚜껑 · 집게 · 국자 → 이후 식재료
04
가전 사이 이동이 반복
식세기 · 수납장 · 조리대 사이의 Physical Movement
Business 기준
01
높은 일일 사용빈도
매일 식사 후 반복 → 사용 Data · 가치 체감이 빠름
02
구매 계기가 있음
주방 Remodeling · 신축 입주 때 공사와 설치를 함께 결정
03
CLEAN → ASSIST → COOK
같은 Platform에 Skill · Tool을 더해 기능 확장
04
설치 이후 반복매출
Installed Base 기반 Care · 소모품 · Skill
→  주거용 Manipulation의 기술성과 고객가치를 동시에 검증할 수 있는 첫 Application
[사업 가설] 주방이 첫 검증 공간으로 적합하다는 판단이며, 고객 지불의사는 별도 확인 (WTP 조사 n≥300 · 예약금 Test, M18).
```

## 04. 집마다 주방이 달라, 같은 로봇을 반복 설치하기 어렵습니다

```text
03  가정용 Robot 적용의 구조적 한계
집마다 주방이 달라, 같은 로봇을 반복 설치하기 어렵습니다
Robot Intelligence 부족만이 아니라 높은 Environment Variation이 Reliability와 반복설치를 막는 구조
주방마다 다른 것
Kitchen Geometry
ㅡ자 · ㄱ자 · 반도형
가전 위치
식세기 · 인덕션 배치
수납 위치
상부장 · 서랍 · 키큰장
조리대 치수
높이 · 깊이 · 길이
가전 Model
랙 구조 · 문 열림
Object 위치
식기 놓는 자리
동선
통로 폭 · 사람 위치
조명
창 · 조명 반사
설치오차
벽 · 가구 수직 · 수평
범용 Robot 적용 시 집마다 반복
Perception
Mapping
Teaching
Programming
Calibration
Validation
집마다
반복
받은 평면 5종 | 싱크 벽 길이 약 2.6~3.3m · 3종은 기본 한 줄 배치 불가 · ㄱ자 · 일자 · 반도형 혼재 (재작도, 특정 단지 아님) | DERIVED
공개 사례 | LG CLOiD: 팔 작업 범위 무릎 높이 이상 (보도) → 식세기 하단 랙 같은 낮은 작업점은 환경 측 보완 필요 | FACT
MH는 모든 주방을 표준화하지 않습니다
→ 로봇의 적응력 + 필요한 곳만 Interface
[S21] LG CLOiD 보도 · 평면 5종은 사용자 제공 도면을 치수선 기준으로 재작도한 결과 (부록 B2). 표본이 작아 평면 30개 분석으로 확대 (TARGET).
```

## 05. 로봇이 적응하고, 주방은 필요한 곳만 맞춥니다

```text
04  MH Robotics Technology Strategy
로봇이 적응하고, 주방은 필요한 곳만 맞춥니다
Robot Hand · Manipulation Skill · Calibration · Environment Interface를 함께 설계
Object Variation
형상 · 재질 · 젖은 표면 · 얇은 Edge
Adaptive Robot Hand
파지 방식을 바꿔 다양한 식기 · 도구를 하나의 손으로
Task Variation
집기 · 넣기 · 꺼내기 · 열기
Manipulation Skill Library
Pick · Place · Insert · Remove · Open/Close를 재사용 단위로
Kitchen Variation
가전 · 수납 위치 · 설치 오차
Perception + Calibration
현장에서 좌표 · 가전 · 수납 위치를 맞춰 같은 Skill 실행
반복 작업점
Robot 대기 · 도구 · 식세기 랙
Minimal Robot-friendly Interface
Robot Home · Tool Dock · Appliance Interface · Vision Reference
결과: 다양한 주방에서 같은 Robot Platform과 Skill을 반복 적용
핵심 원칙  Environment Standardization은 목적이 아니라 Reliability와 반복설치를 높이는 수단. 주방 전체 표준화는 하지 않음.
모든 기술 요소는 현재 개발 전 (CONCEPT · TARGET). 검증 순서와 Gate는 16쪽 · 부록 A.
```

## 06. 핵심 Hardware: 주방 물체를 다루는 Adaptive Robot Hand

```text
05  Adaptive Kitchen Robot Hand
핵심 Hardware: 주방 물체를 다루는 Adaptive Robot Hand
손가락 수 · 자유도 경쟁이 아닌 Task Completion · 가격 · 위생 · 유지관리 · 내구성 중심
교체형 Food-contact Pad
힘 · 토크 센서
Quick Changer
Wrist Camera
[CONCEPT]
Plate · 가장자리 Pinch
Cup · 외벽 감싸기
Bowl · 테두리 Pinch
Tool · 손잡이 Power Grasp
주방 물체의 어려움
형상 · 크기 · 재질 (유리 · 도자기 · 금속 · Plastic) · 젖은 표면 · 미끄러짐 · 파손 위험 · 얇은 Edge · 다양한 Handle
핵심 기술 후보
Adaptive Grasp
Compliance
Grip Force Control
Slip Detection
Multi-contact
Tool Handling
Replaceable Food-contact Module
Buy vs Build — M6 Gate
· 기준선: Robotiq 2F-85 약 $5,825 · Inspire RH56 $4,500~ (FACT)
· 30종 식기로 성공률 · 파손 · 교체 · 원가 비교
· 우위 확인 시에만 자체 Hand 채택 (TARGET)
Object Variation 대응
전용 Gripper 수 ↓
같은 End-effector 활용 ↑
Skill 재사용 ↑
유지보수 단순화
+ Pad · Seal · Tip = 소모품
렌더는 설계 검증 전 개념 형상 (CONCEPT). 식품 접촉 부품: 식품위생법 "기구" · 「기구 및 용기 · 포장의 기준 및 규격」 고무제 규격 대응 (ASSIST · COOK 단계 필수) [S42 · S48].
```

## 07. 같은 Skill을 다른 주방으로 옮기는 것이 핵심 기술입니다

```text
06  Manipulation Skill · Calibration
같은 Skill을 다른 주방으로 옮기는 것이 핵심 기술입니다
Skill = 단순 Software 구독이 아닌 Robot Capability의 확장 Layer
01
감지
Object Detection
02
파지
Grasp · Force
03
조작
Move · Insert
04
검증
Success Check
05
복구
Recovery
실패 감지 → 다시 잡기 · 내려놓기
다른 주방 → Calibration → 같은 Skill
Kitchen A · ㅡ자 3.2m · 빌트인 식세기
R
S
수
D
Kitchen B · ㄱ자 · 짧은 싱크 벽
R
S
D
수
Kitchen C · Retrofit · 독립형 식세기
R
S
수
D
Calibration (설치 시)
Kitchen Mapping
Coordinate Calibration (Dock · 기준점)
Appliance · Storage Position Mapping
Task Parameter Adjustment
같은 CLEAN Skill Library
식기 Pick
Dishwasher Loading
Dishwasher Unloading
Storage Return
M18 검증 (TARGET)  구조 · 가전 모델이 다른 주방 3종에서 재배치 후 성공률 하락 ≤ 10%p · 현장 Calibration ≤ 4시간
평면 도식은 개념 예시 (R = Robot Home, S = Sink, D = Dishwasher, 수 = 수납). 수치 목표의 근거는 부록 A1~A2 KPI 표.
```

## 08. MH Kitchen Robotics System: 다섯 개 층을 하나의 제품으로

```text
07  MH Kitchen Robotics System
MH Kitchen Robotics System: 다섯 개 층을 하나의 제품으로
Robot Module · 실행 · Calibration · Environment Interface · Safety의 시스템 통합
D · Robot Home
D · Drop Zone
D · 식세기 Interface
E · Robot Zone
E · Human Zone
[CONCEPT]
A
Robot Module
Robot Arm · Adaptive Hand · Vision · Force / Safety Sensor · Controller · 필요 시 Rail / Dock
B
Manipulation Layer
Object Detection · Grasp Planning · Motion Planning · Task Execution · Failure Detection · Recovery
C
Calibration Layer
Kitchen Mapping · Coordinate Calibration · Appliance / Storage Position Mapping · Task Parameter
D
Environment Interface
Robot Home · Tool Dock · Storage Dock · Appliance Interface · Vision Reference · 필요 시 Working Surface Guide
E
Human-Robot Safety
Human Detection · Speed Control · Collision Detection · Emergency Stop · Safe Home Return
설치 위치 · 동작범위는 설계 개념 (CONCEPT), 실제 Reach · 안전성은 검증 전. 안전 기준: ISO 10218-2:2025 감속 250mm/s 등 참고 · 가정용 IEC 63682 (2026 초안) · ISO 13482 개정 대응 [S39 · S47].
```

## 09. CLEAN은 첫 검증 Workflow이고, 제품 범위는 주방 전체입니다

```text
08  첫 검증 Workflow
CLEAN은 첫 검증 Workflow이고, 제품 범위는 주방 전체입니다
새 로봇을 단계마다 다시 만드는 것이 아니라, 같은 Platform에 Skill과 Tool을 추가
① 식기 인식
② Pick
③ Dishwasher Loading
④ Dishwasher Unloading
⑤ Storage Return
[CONCEPT]
CLEAN 검증
Adaptive Grasp
Object Recognition
Motion Planning
Appliance Interaction
Storage Interaction
Calibration
Safety
Failure Recovery
반복 Task Execution
초기 · 기술검증
CLEAN
식기 이동 · Dishwasher Loading / Unloading · Storage Return
추가되는 것
기본 Skill 4종 · 식세기 Interface · Storage Dock
중기 · 기능 확장
ASSIST
재료 이동 · 재료 투입 · 젓기 · 뚜껑 조작 · Tool Handling
추가되는 것
ASSIST Skill Pack · 집게 · 국자 · 뚜껑 Tool
장기 · R&D 방향
COOK
Recipe Workflow · 복수 Skill 연결 · Appliance 연동 · 조리 · 조리 후 정리
추가되는 것
Recipe Skill · 가전 연동 · 식재료 Tool (식품접촉 규격)
[FUTURE CONCEPT]
같은 Robot Platform + Skill 확장 + Tool 확장. COOK과 자율조리는 현재 검증 결과가 아닌 장기 R&D 방향 (FUTURE CONCEPT).
```

## 10. 제품은 하나, 설치 경로는 세 가지입니다

```text
09  Existing / Remodeling / New-build
제품은 하나, 설치 경로는 세 가지입니다
주방 전체를 획일화하지 않고 Integration 수준만 다르게 적용
Existing Kitchen
Retrofit
Integration 수준
Remodeling
Integration
Integration 수준
New-build
설계 반영
Integration 수준
고객 상황 | 주방 유지 · 호환 주방 | 주방 교체 시점 (Premium) | 분양 · 입주 전 (건설사 · 가구사)
공사 범위 | 최소 시공 (Mount · Dock) | 주방 공사와 동시 (Partner 시공) | 설계 단계에서 반영
Interface | Compact Mount · Dock · Vision Reference · Drop Zone | Rail · Robot Home · 식세기 Interface · Storage Dock | Mount · 전원 · 통신 · Tool Dock · Appliance Interface · Service Access
설치 · Calibration | 현장 Calibration 중심 · Y3 원가 95만원 (약 29인시) | Y3 원가 60만원 (약 18인시 = 2인 약 1일) | 입주 시 또는 후설치 (Option 세대)
MH 매출 (가설) | Kit 150 + Robot 1,490 + 설치 120 = 1,760만원 | Interface 450 + Robot 1,490 + 설치 80 = 2,020만원 | Option 220만원 (B2B) + 입주 Attach 25% × (Robot + 설치)
역할 | Phase 2 · 고객 확대 | Phase 1 · 검증 채널 | Phase 3 · Scale 채널
MH Core  Robot · Hand · Skill · Calibration · Interface Standard · Safety · Commissioning · QA     Partner  철거 · 가구 · 전기 · 배관 · 일반 시공
가격 · 원가 · 인시는 ASSUMPTION / DERIVED (VAT 별도, 주방 공사비 별도). 인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 (부록 D).
```

## 11. 설치로 시작해, 쓰는 동안 반복매출이 쌓이는 3층 구조입니다

```text
10  Business Model
설치로 시작해, 쓰는 동안 반복매출이 쌓이는 3층 구조입니다
INSTALL → OPERATE → EXPAND. Hardware 외 매출은 실제 유지관리와 기능가치에 근거
INSTALL
초기 매출
Robot System (Arm · Adaptive Hand · Vision · Safety)
1,490만원
Interface · Integration
150~450만원
Installation · Calibration
80~120만원
OPERATE
반복매출
Rental (60개월, Care · Grip Kit 포함)
월 33만원
Care (Robot Lifecycle Maintenance)
연 48만원
Consumables (Pad · Seal · Tip · Cover)
연 36만원 (List)
EXPAND
확장매출
ASSIST Skill Pack
60만원
Tool · End-effector
80만원
COOK Skill · Robot Upgrade
FUTURE
[가격 = ASSUMPTION (VAT 별도) · 실측 · WTP 검증 전]
대표 1세대 · 5년 (Remodeling 구매, Y3 원가)
INSTALL 2,020  ·  OPERATE 366  ·  EXPAND 32  =  2,418만원
428만원
5년 기여이익 (Y3 원가, 이익률 18%)
[DERIVED]
798만원
Y5 원가 (BOM · 설치 · Care 하락, 33%)
[DERIVED]
Rental 구조 (Scale 단계)
고객
월 납부
Capital Partner
Robot 자산 보유
MH
Product · SW · Care
월 33만원 → Partner가 Robot을 ASP의 88%에 매입 · MH 서비스료 월 6만원
Partner IRR 약 13.1% (DERIVED) · Pilot은 MH 직접, Scale은 Partner 보유
Care = 정기 안전점검 · Calibration · 원격진단 · SW Update · A/S (Software 구독 아님). Consumables = 실제 마모 · 위생 기반, 교체주기는 개발 중 검증. Installed Base가 연 설치의 6배일 때 OPERATE + EXPAND 비중 약 29% (DERIVED). 참고 FACT: 코웨이 국내 렌탈 계정 748만 (2026 1Q) · LG 가전 구독 매출 2조원+ (2025) [S12 · S41].
```

## 12. 큰 TAM 대신, 세대 수 × 적용률 × 단가로 시작 시장을 계산합니다

```text
11  Market / Beachhead
큰 TAM 대신, 세대 수 × 적용률 × 단가로 시작 시장을 계산합니다
아파트 재고는 기회 기반이지 확정 구매시장이 아님. 비율은 모두 ASSUMPTION (검증 계획 부록 C)
국내 아파트 (2025)
1,328만호
[DERIVED]
총주택 2,018만호 × 아파트 65.8%
준공 20년 이상 주택 56.0%
주택 매매 72.6만호 (2025)
아파트 입주 23.6만 (2025) · 18.3만 (2026 예정)
기회 기반 (Stock) ≠ 구매시장. 실제 계산은 오른쪽 Funnel
시장 | 산식 (세대 × 적용률) | 대상 세대 | 패키지 | 연 규모
① Remodeling Beachhead | 주방 교체 30만 × Premium 10% × 적용 60% | 18,000/년 | 1,784만원 | 3,212억원
② Retrofit | 1,328만 × Premium 10% × 식세기 60% × 호환 40% = 31.9만 (재고) × 연 0.5% | 1,593/년 | 1,760만원 | 280억원
③ New-build | 입주 20만 × Premium 단지 15% × Option 10% | 3,000/년 | 612만원 | 184억원
④ Recurring | Installed Base × 구매 고객 ARPU 58.8만원/년 (Care · 소모품) | 1,000대당 | - | 5.9억원
SAM 합계 (① + ② + ③)
연 3,676억원
SOM: Y5 매출 (Base Plan)
91.5억원 · 560세대
대상 세대의 약 2.5% (TARGET)
주방 교체 30만은 두 방식 교차검증 (29.0만 · 30.3만) 후 설정한 가정. 참고 TAM (Premium 세대 × 전체 패키지) 연 1.2조원은 판단에 쓰지 않음. 출처 [S1~S6].
```

## 13. 고객의 돈과 설치비를 먼저 검증하고, 파트너로 늘립니다

```text
12  GTM / Partner Distribution
고객의 돈과 설치비를 먼저 검증하고, 파트너로 늘립니다
초기 Mass Market 진입 없음. Premium Remodeling → 호환 주방 Retrofit → 신축 B2B2C
Phase 1  ·  Y2 실증 → Y3~
Premium Kitchen Remodeling
목적: 제품 · 가격수용성 · 설치 · 사용성 검증 · 초기 Reference · 고객 Data
직접 판매 + 주방 · 인테리어 Partner  ·  검증 채널
Phase 2  ·  Y4~
Compatible Existing Retrofit
전체 Remodeling 없이 적용 가능한 고객 확대 · 호환성 Check 표준화
설치 Partner 경유  ·  고객 확대
Phase 3  ·  Y3 계약 → Y5 입주
New-build Apartment
건설사 · 주방가구사 B2B2C · Project 단위 Scale
Interface Option + 후설치  ·  Scale 채널
설치 세대 (Base, TARGET)
Y1
Y2
Y3
Y4
Y5
0
3
50
200
560
Remodeling 직접
Remodeling Partner
Retrofit
New-build 입주
Product Company 구조
MH Core
Robot · Robot Hand
Manipulation Skill
Calibration
Interface Standard
Safety · Commissioning · QA
Partner
철거 · 가구
전기 · 배관
일반 시공
(신축) 건설사 · 가구사
(Rental) 캐피탈 · 렌탈사
설치 물량 증가 ≠ 본사 현장인력 비례 증가
선례 (FACT, MH와 무관): 건설사 · 가전사의 구독 · 관리 번들 — LH 공공주택 5,400여 세대 · 압구정 재건축 약 7,000세대 선택지 (LG, 2026) [S41]. 현재 MH 파트너 계약 · LOI 없음.
```

## 14. R&D 성과가 설치비 · 서비스비 · 확장매출로 이어지는 구조입니다

```text
13  Technology-to-Economics / Moat
R&D 성과가 설치비 · 서비스비 · 확장매출로 이어지는 구조입니다
성능 향상 자체가 아니라 Unit Economics와 Scale 개선으로 연결
Adaptive Hand 고도화
Object Coverage ↑
Manipulation Skill 고도화
Task Coverage ↑
Calibration 고도화
신규 주방 적용시간 ↓
Environment Interface 최적화
Task Reliability ↑
설치시간 ↓
Engineering Cost ↓
고객경험 ↑
반복설치 ↑
→ Installed Base ↑
Installed Base → Care · Consumables · Skill Upgrade 매출 ↑
KPI ↔ 원가 연결 (Base, DERIVED)
연결 지표 | Y2 실증 | Y3 | Y5
설치 · Calibration 원가 (Remodeling) | 90만 · 27인시 | 60만 · 18인시 | 38만 · 12인시
Robot System BOM | 1,520만 | 1,180만 | 915만
Care 원가 / 대 · 년 | 40.8만 | 36.8만 | 26.8만
1세대 5년 기여이익 | - | 428만 | 798만
Pad 수명 목표 ≥ 약 5,475회 파지 (분기 교체 · 하루 60회 가정)
1세대 5년 기여이익 민감도 (만원)
Robot ASP (WTP) ±20%
-286
+286
Robot BOM ±20%
-236
+236
Interface 가격 ±20%
-90
+90
직접판매 획득비용 ±50%
-75
+75
Failure Rate 0.3 ↔ 1.2회
-84
+49
Moat = 단일 특허가 아닌 축적  ① 주방 물체 Grasp Data · Skill Library  ② Calibration 절차 · Interface 표준 (설치시간)  ③ Installed Base · Care Data  ④ 출원 예정 IP   — 모두 구축 전 (TARGET)
인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 약 3.3만원 (연 6,600만원 기준). 민감도: Remodeling 구매 1세대 · Y3 원가 · 기준 428만원 (부록 D).
```

## 15. 경쟁은 이미 있습니다. 차이는 주방 적용 방식이며, 실증으로 증명합니다

```text
14  IP / Competition
경쟁은 이미 있습니다. 차이는 주방 적용 방식이며, 실증으로 증명합니다
비교는 접근 방식 설명이며 성능 우위 주장이 아님 (공개 자료 기준)
Category | Object Handling | Task 범위 | 주방 적응 · 설치 | 반복매출 · 확장
Kitchen Appliance 삼성 · LG | 기기 내부만 | 세척 · 가열 · 보관 | 가전 설치 | 구독 · Care (LG 2조원+)
Cooking Robot Moley · Posha | 조리 도구 · 재료 | 조리 중심 | 전용 주방 (£248k) · 조리대 기기 ($1,750) | 레시피 · 월 구독
Humanoid · Mobile 1X NEO · Figure · Sunday · LG CLOiD | 범용 손 | 가사 전반 시연 | 설치 불필요 · 모델 학습 중심 | 구독 ($499/월) · 출시 전
Cobot + Gripper UR · Doosan + Robotiq | 상용 Gripper | 산업 작업 | Integrator 맞춤 구축 | 부품 판매
Kitchen Furniture 한샘 · 리바트 | - | 수납 · 빌트인 가전 | 주방 시공 (로봇 협업 보도 없음) | 시공 매출
MH 목표 Position | Kitchen Hand (식기 · 도구) | CLEAN → ASSIST → COOK | Calibration + 최소 Interface · 공사 연계 | Care · 소모품 · Skill
영역 | 출원 후보 | 선행 Risk | 순위
Robot Hand | Replaceable Food-contact Module · Adaptive Finger · Compliance | 중~상 | 1
Calibration | Task Coordinate Calibration (Dock · 가전 기준점) · Kitchen Mapping | 중 | 1
Interface | Robot Home · Tool Dock · Appliance Interface | 상 | 2
Manipulation | 식기 Handling · Failure Recovery | 상 | 2
Safety | Human / Robot Zone Control | 중~상 | 3
선행: Dishcare US 11,731,282 · Dishcraft US 10,507,584 · 주방 Rail Arm US 7,751,938 · 수납장 로봇 US 12,275,130 · Schmalz OFG. 등록 가능성 미정 · 24개월 출원 5건 + PCT 1건 목표
Humanoid는 위협만이 아님  공개 범용 모델 (openpi π0 · π0.5)은 MH Manipulation Layer에 활용 가능 · MH의 Interface · Skill · Calibration은 다른 Robot Platform에도 적용 · 가격 ($20,000) · 낮은 작업점 Reach 같은 가정 설치 제약은 공간 Integration으로 보완
공개 자료 [S19~S25 · S41 · S45 · S46 · S49~S51]. 경쟁사 성능 비교 Data 없음 → 비교 축은 접근 방식. 특허 청구항 · 권리상태는 변리사 검토 전.
```

## 16. TIPS는 기술 위험을, Seed는 사업 위험을 줄이는 데 씁니다

```text
15  TIPS R&D / 24개월 Roadmap
TIPS는 기술 위험을, Seed는 사업 위험을 줄이는 데 씁니다
TIPS R&D = Technology De-risking · 민간 Seed = Commercial Validation (역할 중복 최소화)
TIPS R&D  ·  Technology De-risking
WP1 Adaptive Kitchen Robot Hand
WP2 Kitchen Manipulation Skill
WP3 Perception / Calibration
WP4 Minimal Environment Interface
WP5 Human-Robot Safety
WP6 Integrated CLEAN 실증
민간 Seed  ·  Commercial Validation
Core Team (사업 · 현장 · 경영지원)
Prototype · Mock-up 운영
Customer Validation · WTP
Pilot 운영 · 유료 전환
Partner Development
BM Validation · 인증 본시험 · 기관부담금
0~6M
· Kitchen Task 분석
· Robot Architecture
· Hand Prototype v1
· Object Grasp Test (30종)
· 초기 Calibration
7~12M
· CLEAN Skill
· Dishwasher Interaction
· Hand v2 · Safety
· 1:1 Kitchen Mock-up
· 목업 CLEAN 전 과정
13~18M
· 다양한 Kitchen 적용
· Task Transfer Test
· Failure Recovery
· Pilot 착수
· WTP Validation
19~24M
· Reliability
· Installation Standard
· Real-home Pilot 3세대
· BOM · 설치 · Service 원가
· Paid Pilot · Partner 검증
M6
상용 Gripper 대비 Hand 비교 (30종) → Build / Buy 결정
M12
목업 CLEAN 전 과정 · 식기 성공률 ≥ 80%
M18
주방 3종 Transfer (하락 ≤ 10%p) · WTP n≥300
M24
가정 실증 3세대 ≥ 90% · 유료 전환 · 원가 실측
[TARGET]
TIPS 2026 일반트랙: 정부 R&D 최대 8억원 · 24개월 · 정부 75% 이내 / 기관부담 25% 이상 (FACT, 선정 미확정) [S33 · S52]. KPI 근거 · 측정 방법은 부록 A1~A3.
```

## 17. 투자 판단의 첫 질문은 팀입니다. Founder 칸은 아직 비어 있습니다

```text
16  Founder / Team
투자 판단의 첫 질문은 팀입니다. Founder 칸은 아직 비어 있습니다
확인되지 않은 대표자 이력 · 기술 성과는 기재하지 않음
확인 항목 | Founder 1 (대표) | Founder 2
Why This Problem | [Founder 정보 필요] | [Founder 정보 필요]
Relevant Engineering Experience | [Founder 정보 필요] | [Founder 정보 필요]
Hardware / Product Development | [Founder 정보 필요] | [Founder 정보 필요]
Robot · Mechanical · AI Capability | [Founder 정보 필요] | [Founder 정보 필요]
Construction · Kitchen · Manufacturing Knowledge | [Founder 정보 필요] | [Founder 정보 필요]
Customer / Partner Network | [Founder 정보 필요] | [Founder 정보 필요]
Full-time Commitment · 지분 | [Founder 정보 필요] | [Founder 정보 필요]
역할 (채용 계획, ASSUMPTION) | 시작 | 구분
대표 · 사업 총괄 | M1 | Founder
공동창업자 · 기술 총괄 | M1 | Founder
Manipulation · 제어 리드 | M1 | R&D
Perception · ML 리드 | M2 | R&D
Hand · 기구 리드 (메카트로닉스) | M2 | R&D
임베디드 · 전기 · 안전 | M4 | R&D
Robot SW · 통합 (Motion · Skill) | M6 | R&D
제품 · 사업개발 (고객 검증 · 파트너) | M7 | 사업
Hand 센싱 (Grip Force · Slip) | M10 | R&D
경영지원 (재무 · 과제 관리, 0.5 FTE) | M10 | 경영지원
시험 · 신뢰성 (Test · QA) | M13 | R&D
설치 · Commissioning 엔지니어 | M13 | 현장
Skill · Data 엔지니어 | M16 | R&D
현장 서비스 Technician | M19 | 현장
M24 약 14명 = Founder 2 · R&D 8 · 사업 1 · 현장 2 · 경영지원 0.5  |  평균 FTE 7.0 (Y1) → 12.8 (Y2)
TIPS 요건 (2026 공고, 원문 확인 필요): 대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 30% 이하 · 정부지원 5억원당 청년 1명 신규 채용 [S33]. 필수 자료: 신원 · 역할 · 지분 · 고용형태 · 역량 증빙 · 특허 권리귀속.
```

## 18. 24개월 23.4억원 계획: TIPS 8억원 + Seed 14~19억원

```text
17  Investment Ask / 24M Value Creation
24개월 23.4억원 계획: TIPS 8억원 + Seed 14~19억원
Bottom-up 사용처 기준. Seed 범위 = Lean (팀 축소) ~ Base (기술 + 사업 검증 + 3개월 Buffer)
사용처 (억원) | 24개월 | TIPS 편성
인건비 · 연구수당 | 15.55 | 6.90
Robot HW · Hand · Mock-up | 2.39 | 2.01
Software · Data | 0.55 | 0.44
Pilot · 실증 순비용 | 0.73 | -
Customer · Partner | 0.60 | -
Certification · IP | 1.05 | 0.71
Space · Operating | 1.86 | 0.60
예비비 (10%) | 0.68 | -
24개월 지출 합계 | 23.4 | 10.67
TIPS 정부지원 (선정 시) | 8.0 | FACT
기관부담 (현금 · 현물) | 2.67 | Seed 부담
Seed Base = 지출 − TIPS + Buffer 3개월 | 19.0 | DERIVED
Seed Lean (팀 축소 · 범위 축소) | 13.8 | DERIVED
TIPS 미선정 시 (Lean 범위) | 21.5 | DERIVED
TODAY
Concept
Technology Hypothesis
Business Hypothesis
Seed
+
TIPS
24M TARGET
[TARGET]
기술
Working Kitchen Prototype
Adaptive Robot Hand
Skill Library
Calibration System
Safety Architecture
Multiple Kitchen Test
Task Transfer Evidence
경제성
Robot BOM
Installation Cost
Service Cost
시장
Customer WTP
Pilot · Paid Pilot
Partner Evidence
Patent 출원
NEXT ROUND
Productization
Production
Distribution
Scale
Series A 판단 기준  기술 성공 + 유료 전환 + 설치 · 서비스 원가 실측
Buffer = Y2 월평균 지출 × 3개월 (3.5억원). TIPS 과제 총 10.67억원 = 정부 8억원 (75%) + 기관부담 2.67억원 (현금 1.35 · 현물 1.32). 운영사 선투자 요건 (수도권 2억원 이상)은 Seed 라운드에 포함. 투자 조건 · 기업가치는 협의 (본 자료에서 제시하지 않음).
```
