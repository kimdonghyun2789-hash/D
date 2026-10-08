# 03. 각 Slide 실제 화면 문구 (본문 18장)

> MH Robotics · Seed · TIPS IR · 최종본 · 2026.10

- 표 = `셀 | 셀` · 대괄호 = 화면의 작은 Tag

## 01. MH Robotics — Kitchen Manipulation Robotics System

```text
M H   R O B O T I C S
Kitchen Manipulation
Robotics System
로봇손 · 작업 Skill · Calibration · 주방 Interface 통합 제품
식기 정리 → 조리까지 단계적 확장 · 기존 주방 · Remodeling · 신축 적용 · Installed Base 반복매출
CLEAN
첫 검증 Workflow (식기 정리)
ASSIST
중기 확장 (재료 이동 · 투입 · 도구)
COOK
장기 R&D 방향 (Recipe Workflow)
Seed 투자 · TIPS 창업기업 IR  |  2026.10
현재 단계: Concept (시제품 개발 전)
Robot Home (Dock)
Rail (필요 시)
식기세척기 Interface
[CONCEPT RENDERING]
```

## 02. 가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workflow

```text
02  문제
가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workflow
개별 가전 기능은 자동화 · 주방 Workflow 전체의 Physical Manipulation은 아직 사람 몫
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
가전 사이 사람이 하는 Physical Task
식기 이동
식세기 적재
식세기 인출
수납
식재료 이동
재료 투입
조리도구 조작
젓기
뚜껑 조작
조리 후 정리
앞 4개 = CLEAN 검증 범위
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
출처: 국가데이터처 2024 가계생산 위성계정 (2026.4) [S40] · 식사 후 정리 40분 = 가설 → Time-diary 30세대로 검증 예정
```

## 03. 주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간

```text
03  왜 Kitchen인가
주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간
Robot Engineering 4개 기준 · Business 4개 기준
Robot Engineering 기준
01
집기 · 이동 · 놓기 · 넣기 · 빼기 중심
동작 종류 적고 반복 → Skill Library화 용이
02
작업영역 고정
싱크 · 조리대 · 식세기 · 수납장 → Calibration 대상 명확
03
물체는 다양 · 범위는 닫힘
접시 · 컵 · 그릇 · 수저 · 뚜껑 · 집게 · 국자 → 이후 식재료
04
가전 사이 이동 반복
식세기 · 수납장 · 조리대 사이 물리적 이동
Business 기준
01
높은 일일 사용빈도
매일 식사 후 반복 → 사용 Data · 빠른 가치 체감
02
구매 계기 존재
주방 Remodeling · 신축 입주 시 공사 · 설치 동시 결정
03
CLEAN → ASSIST → COOK
같은 Platform + Skill · Tool 추가로 기능 확장
04
설치 이후 반복매출
Installed Base 기반 Care · 소모품 · Skill
→  주거용 Manipulation의 기술성 · 고객가치 동시 검증이 가능한 첫 Application
Why now: 6축 Arm $6,999~ [S15] · 공개 조작 모델 π0.5 [S46] · 가정용 로봇 안전기준 IEC 63682 초안 [S47] · 지불의사 = WTP n≥300 · 예약금 Test로 검증 (M18)
```

## 04. 주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계

```text
04  가정용 Robot 적용의 구조적 한계
주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계
Robot 지능 부족만이 아닌 높은 환경 편차 (Environment Variation) → 신뢰성 · 반복설치 제약
주방마다 다른 것
주방 형태
ㅡ자 · ㄱ자 · 반도형
가전 위치
식세기 · 인덕션 배치
수납 위치
상부장 · 서랍 · 키큰장
조리대 치수
높이 · 깊이 · 길이
가전 모델
랙 구조 · 문 열림
물건 위치
식기 놓는 자리
동선
통로 폭 · 사람 위치
조명
창 · 조명 반사
설치오차
벽 · 가구 수직 · 수평
범용 Robot 적용 시 집마다 반복
인식 (Perception)
Mapping
교시 (Teaching)
Programming
Calibration
검증 (Validation)
집마다
반복
확보 평면 5종 | 싱크 벽 길이 약 2.6~3.3m · 3종 기본 한 줄 배치 불가 · 1종 미검토 · ㄱ자 · 일자 · 반도형 혼재 | DERIVED
공개 사례 | LG CLOiD: 팔 작업 범위 무릎 높이 이상 (보도) → 낮은 작업점 (식세기 하단 랙) = 환경 측 보완 필요 (MH 해석) | FACT + 해석
모든 주방 표준화가 아닌
→ Robot 적응력 + 필요한 지점만 Interface
출처 [S21] · 평면 5종 = 제공 도면 재작도 (부록 B2) · 평면 30개 분석 예정 (M6)
```

## 05. Robot 적응 + 반복 작업점에만 최소 Interface

```text
05  MH Robotics Technology Strategy
Robot 적응 + 반복 작업점에만 최소 Interface
Robot Hand · Manipulation Skill · Calibration · Environment Interface 통합 설계
물체 다양성 (Object)
형상 · 재질 · 젖은 표면 · 얇은 Edge
Adaptive Robot Hand
파지 방식 전환 → 다양한 식기 · 도구를 하나의 손으로
작업 다양성 (Task)
집기 · 넣기 · 꺼내기 · 열기
Manipulation Skill Library
집기 · 놓기 · 넣기 · 빼기 · 열고 닫기 = 재사용 단위
주방 차이 (Kitchen)
가전 · 수납 위치 · 설치 오차
Perception + Calibration
현장에서 좌표 · 가전 · 수납 위치 등록 → 같은 Skill 실행
반복 작업점
Robot 대기 · 도구 · 식세기 랙
Minimal Robot-friendly Interface
Robot Home · Tool Dock · 가전 Interface · Vision 기준점
결과: 다양한 주방에서 같은 Platform · Skill의 반복 적용 가능성 확대
핵심 원칙  환경 표준화 = 목적이 아닌 신뢰성 · 반복설치 수단 · 주방 전체 표준화 없음
검증 순서 · Gate: 16쪽 · 부록 A5
```

## 06. 핵심 Hardware: 주방 물체 대응 Adaptive Robot Hand

```text
06  Adaptive Kitchen Robot Hand
핵심 Hardware: 주방 물체 대응 Adaptive Robot Hand
손가락 수 · 자유도 경쟁이 아닌 작업 완료율 · 가격 · 위생 · 유지관리 · 내구성 중심
교체형 Food-contact Pad
힘 · 토크 센서
Quick Changer
Wrist Camera
[CONCEPT]
[CONCEPT]
접시 · 가장자리 Pinch
[CONCEPT]
컵 · 외벽 감싸기
[CONCEPT]
그릇 · 테두리 Pinch
[CONCEPT]
국자 · 손잡이 파지
주방 물체의 어려움
형상 · 크기 · 재질 (유리 · 도자기 · 금속 · 플라스틱) · 젖은 표면 · 미끄러짐 · 파손 위험 · 얇은 가장자리 · 다양한 손잡이
핵심 기술 후보
적응 파지
유연 접촉 (Compliance)
파지력 제어
미끄럼 감지
다점 접촉
도구 파지
교체형 식품접촉 Module
Buy vs Build — M6 Gate
· 기준선: Robotiq 2F-85 약 $5,825 · Inspire RH56 $4,500~ (FACT)
· 30종 식기로 성공률 · 파손 · 교체 · 원가 비교
· Coverage +15%p 또는 Tool 교체 50%↓ 시에만 자체 Hand (TARGET)
물체 다양성 대응
전용 Gripper 수 ↓
같은 End-effector 활용 ↑
Skill 재사용 ↑
유지보수 단순화
+ Pad · Seal · Tip = 소모품
식품 접촉 부품: 식품위생법 "기구" · 「기구 및 용기 · 포장의 기준 및 규격」 고무제 규격 대응 (ASSIST · COOK 단계 필수) [S42 · S48]
```

## 07. 핵심 기술: Calibration 기반 Skill의 주방 간 이전

```text
07  Manipulation Skill · Calibration
핵심 기술: Calibration 기반 Skill의 주방 간 이전
Skill = Robot이 수행 가능한 작업을 늘리는 확장 Layer (Software 구독 아님)
01
감지
물체 · 위치 인식
02
파지
파지점 · 파지력
03
조작
이동 · 삽입
04
검증
완료 확인
05
복구
다시 잡기 · 내려놓기
실패 감지 → 다시 잡기 · 내려놓기
다른 주방 → Calibration → 같은 Skill
주방 A · ㅡ자 3.2m · 빌트인 식세기
R
S
수
D
주방 B · ㄱ자 · 짧은 싱크 벽
R
S
D
수
주방 C · Retrofit · 독립형 식세기
R
S
수
D
Calibration (설치 시)
주방 Mapping
좌표 Calibration (Dock · 기준점)
가전 · 수납 위치 등록
작업 Parameter 조정
같은 CLEAN Skill Library
식기 집기 (Pick)
식세기 적재 (Loading)
식세기 인출 (Unloading)
수납 복귀 (Return)
M18 검증 (TARGET)  구조 · 가전 모델이 다른 주방 3종에서 재배치 후 성공률 하락 ≤ 10%p · 현장 Calibration ≤ 4시간
R Robot Home · S 싱크 · D 식세기 · 수 수납 (평면 도식 = CONCEPT) · KPI 근거: 부록 A1~A2
```

## 08. MH Kitchen Robotics System: 5개 Layer 통합 제품

```text
08  MH Kitchen Robotics System
MH Kitchen Robotics System: 5개 Layer 통합 제품
왜 Arm: 식세기 랙 · 서랍 · 상부장 작업 = 6축 방향 제어 필요 · 이동형 = 낮은 작업점 · 가격 · 안전 부담
D · Robot Home
D · Drop Zone
D · 식세기 Interface
E · Robot Zone
E · Human Zone
[CONCEPT]
A
Robot Module
Robot Arm (OEM 구매) · Adaptive Hand (M6 Build/Buy) · Vision · 힘 · 안전 센서 · 필요 시 Rail / Dock
B
Manipulation Layer
물체 인식 · 파지 계획 · 경로 계획 · 작업 실행 · 실패 감지 · 복구
C
Calibration Layer
주방 Mapping · 좌표 Calibration · 가전 · 수납 위치 등록 · 작업 Parameter
D
Environment Interface
Robot Home · Tool Dock · 수납 Dock · 가전 Interface · Vision 기준점 · 필요 시 작업면 Guide
E
Human-Robot Safety
사람 감지 · 감속 · 충돌 감지 · 비상정지 · 안전 복귀 (Safe Home Return)
안전 기준: ISO 10218-2:2025 (감속 250mm/s · 접촉력) · 가정용 IEC 63682 (2026 초안) · ISO 13482 [S39 · S47]
```

## 09. CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장

```text
09  첫 검증 Workflow
CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장
단계별 새 로봇 개발이 아닌, 같은 Platform에 Skill · Tool 추가
[CONCEPT]
① 식기 인식
[CONCEPT]
② 집기 (Pick)
[CONCEPT]
③ 식세기 적재
[CONCEPT]
④ 식세기 인출
[CONCEPT]
⑤ 수납 복귀
CLEAN 검증
적응 파지
물체 인식
경로 계획
가전 조작
수납 조작
Calibration
안전
실패 복구
반복 실행
초기 · 기술검증
CLEAN
식기 이동 · 식세기 적재 · 인출 · 수납 복귀
추가되는 것
기본 Skill 4종 · 식세기 Interface · 수납 Dock
중기 · 기능 확장
ASSIST
재료 이동 · 재료 투입 · 젓기 · 뚜껑 조작 · 도구 조작
추가되는 것
ASSIST Skill Pack · 집게 · 국자 · 뚜껑 Tool
장기 · R&D 방향
COOK
Recipe Workflow · 복수 Skill 연결 · 가전 연동 · 조리 · 조리 후 정리
추가되는 것
Recipe Skill · 식재료 Tool · 열 · 액체 안전
[FUTURE CONCEPT]
CLEAN 단독 가사대체 가치 ≈ 월 18만원 < Rental 월 33만원 (DERIVED) → 지불의사 = Premium 고객 · ASSIST 묶음으로 검증 (M18) · COOK = 장기 R&D (FUTURE)
```

## 10. 단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · 신축)

```text
10  Existing / Remodeling / New-build
단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · 신축)
주방 전체 획일화 없이 Integration 수준만 차등 적용
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
Interface | Compact Mount · Dock · Vision 기준점 · Drop Zone | Rail · Robot Home · 식세기 Interface · 수납 Dock | Mount · 전원 · 통신 · Tool Dock · 가전 Interface · Service 공간
설치 · Calibration | 현장 Calibration 중심 · Y3 원가 95만원 (약 29인시) | Y3 원가 60만원 (약 18인시 = 2인 약 1일) | 입주 시 또는 후설치 (Option 세대)
MH 매출 (가설) | Kit 150 + Robot 1,490 + 설치 120 = 1,760만원 | Interface 450 + Robot 1,490 + 설치 80 = 2,020만원 | Option 220만원 (B2B) + 입주 Attach 25% × (Robot + 설치)
역할 | Phase 2 · 고객 확대 | Phase 1 · 검증 채널 | Phase 3 · Scale 채널
MH Core  Robot · Hand · Skill · Calibration · Interface Standard · Safety · Commissioning · QA     Partner  철거 · 가구 · 전기 · 배관 · 일반 시공
가격 · 원가 = ASSUMPTION · VAT · 주방 공사비 별도 · 인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 (부록 D)
```

## 11. 설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM

```text
11  Business Model
설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM
INSTALL → OPERATE → EXPAND · Hardware 외 매출 = 실제 유지관리 · 기능가치 기반
INSTALL
초기 매출
Robot System (Arm · Adaptive Hand · Vision · Safety)
1,490만원
Interface · Integration
150~450만원
설치 · Calibration
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
[가격 = ASSUMPTION (VAT 별도)]
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
제품 · SW · Care
월 33만원 · Partner가 Robot을 ASP의 88%에 매입 · MH 서비스료 월 6만원
Partner IRR 약 13.1% · 단순 회수 약 49개월 > 요구 36개월 (가정) → 조건 협의
Care = 정기 안전점검 · Calibration · 원격진단 · A/S (가입 70% 가정 → 실증 3세대로 확인, M24) · 소모품 = 마모 · 위생 기반 (교체주기 시험 후 확정) · 반복매출 Y3 0.4 → Y5 3.5억원 (Installed Base 663대) · Y5 매출 중 OPERATE + EXPAND 4% (DERIVED) · 선례: 코웨이 렌탈 748만 계정 · LG 구독 2조원+ [S12 · S41]
```

## 12. Bottom-up 시장 산정: 세대 수 × 적용률 × 단가

```text
12  Market / Beachhead
Bottom-up 시장 산정: 세대 수 × 적용률 × 단가
아파트 재고 = 기회 기반 (구매시장 아님) · 비율 = ASSUMPTION (검증 계획 부록 C3)
국내 아파트 (2025)
1,328만호
[DERIVED]
총주택 2,018만호 × 아파트 65.8%
준공 20년 이상 주택 56.0%
주택 매매 72.6만호 (2025)
아파트 입주 23.6만 (2025) · 18.3만 (2026 예정)
Stock ≠ 구매시장
시장 | 산식 (세대 × 적용률) | 대상 세대 | 패키지 | 연 규모
① Remodeling Beachhead | 주방 교체 30만 × Premium 10% × 적용 60% · Robot Attach 85% | 18,000/년 | 1,785만원 | 3,212억원
② Retrofit | 1,328만 × Premium 10% × 식세기 60% × 호환 40% = 31.9만 (재고) × 연 0.5% | 1,593/년 | 1,760만원 | 280억원
③ New-build | 입주 20만 × Premium 단지 15% × Option 10% | 3,000/년 | 613만원 | 184억원
④ Recurring | Installed Base × 구매 고객 ARPU 58.8만원/년 (Care · 소모품) | 1,000대당 | - | 5.9억원
SAM 합계 (① + ② + ③)
연 3,676억원
Y5 계획 매출 (Base · TARGET)
91.5억원 · 560세대
대상 세대의 약 2.5% (DERIVED)
적용 60% = 확보 평면 5종 (기본 배치 수용 1)보다 높은 가정 → 평면 30개 분석으로 검증 (M6) · 주방 교체 30만 = 교차검증 29.0만 · 30.3만 기반 가정 · 출처 [S1~S6]
```

## 13. Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장

```text
13  GTM / Partner Distribution
Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장
초기 Mass Market 진입 없음 · 검증 채널 (Remodeling) → 고객 확대 (Retrofit) → Scale 채널 (신축)
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
Interface 표준
안전 · 시운전 · QA
Partner
철거 · 가구
전기 · 배관
일반 시공
(신축) 건설사 · 가구사
(Rental) 캐피탈 · 렌탈사
설치 물량 증가 ≠ 본사 현장인력 비례 증가
선례: 건설사 · 가전사 구독 · 관리 번들 — LH 공공주택 5,400여 세대 · 압구정 재건축 약 7,000세대 선택지 (LG, 2026) [S41]
```

## 14. R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조

```text
14  Technology-to-Economics / Moat
R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조
성능 향상 자체가 아닌 Unit Economics · Scale 개선으로 연결
Adaptive Hand 고도화
Object Coverage ↑
Manipulation Skill 고도화
Task Coverage ↑
Calibration 고도화
신규 주방 적용시간 ↓
Environment Interface 최적화
Task Reliability ↑
설치시간 ↓
Engineering 비용 ↓
고객경험 ↑
반복설치 ↑
→ Installed Base ↑
Installed Base → Care · Consumables · Skill Upgrade 매출 ↑
KPI ↔ 원가 연결 (Base · ASSUMPTION, 인시 DERIVED)
연결 지표 | Y2 실증 | Y3 | Y5
설치 · Calibration 원가 (Remodeling) | 90만 · 27인시 | 60만 · 18인시 | 38만 · 12인시
Robot System BOM | 1,520만 | 1,180만 | 915만
Care 원가 / 대 · 년 | 40.8만 | 36.8만 | 26.8만
1세대 5년 기여이익 | - | 428만 | 798만
Pad 수명 요구치 ≥ 5,475회 파지 (분기 교체 가정 충족 조건)
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
Failure Rate 1.2 ↔ 0.3회
-84
+49
Moat = 단일 특허가 아닌 축적  ① 주방 물체 Grasp Data · Skill Library  ② Calibration 절차 · Interface 표준 (설치시간)  ③ Installed Base · Care Data  ④ 출원 예정 IP   (TARGET)
인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 약 3.3만원 (연 6,600만원 기준) · 민감도 = Remodeling 구매 1세대 · Y3 원가 · 기준 428만원 (부록 D5)
```

## 15. 경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증

```text
15  IP / Competition
경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증
가전사 · 가구사 직접 진입 가능 (LG CLOiD 2028 목표) → Interface · 시공 Partner 후보로 설계
구분 | 물체 Handling | Task 범위 | 주방 적응 · 설치 | 반복매출 · 확장
Kitchen Appliance 삼성 · LG | 기기 내부만 | 세척 · 가열 · 보관 | 가전 설치 | 구독 · Care (LG 2조원+)
Cooking Robot Moley · Posha | 조리 도구 · 재료 | 조리 중심 | 전용 주방 (£248k) · 조리대 기기 ($1,750) | 레시피 · 월 구독
Humanoid · Mobile 1X NEO · Figure · Sunday · LG CLOiD | 범용 손 | 가사 전반 시연 | 설치 불필요 · 모델 학습 중심 | 구독 ($499/월) · 출시 전
Cobot + Gripper UR · Doosan + Robotiq | 상용 Gripper | 산업 작업 | Integrator 맞춤 구축 | 부품 판매
Kitchen Furniture 한샘 · 리바트 | - | 수납 · 빌트인 가전 | 주방 시공 (로봇 협업 보도 없음) | 시공 매출
MH 목표 Position | Kitchen Hand (식기 · 도구) | CLEAN → ASSIST → COOK | Calibration + 최소 Interface · 공사 연계 | Care · 소모품 · Skill
영역 | 출원 후보 | 선행 Risk | 순위
Robot Hand | Food-contact Module (1) · Adaptive Finger (2) · Compliance (3) | 중~상 | 1
Calibration | Task Coordinate Calibration (1) · Kitchen Mapping (2) | 중 | 1
Interface | Robot Home (2) · Appliance Interface (2) · Tool Dock (3) | 상 | 2
Manipulation | 식기 Handling (2) · Failure Recovery (3) | 상 | 2
Safety | Zone Control (3) | 중~상 | 3
선행: Dishcare US 11,731,282 · Dishcraft US 10,507,584 · 주방 Rail Arm US 7,751,938 · 수납장 로봇 US 12,275,130 · Schmalz OFG · 24개월 출원 5건 + PCT 1건 (TARGET, 등록 미정)
Humanoid = 위협만이 아님  공개 범용 모델 (openpi π0 · π0.5) → MH Manipulation Layer 활용 가능 · MH Interface · Skill · Calibration → 다른 Robot Platform에도 적용 · 가격 ($20,000) · 낮은 작업점 Reach 등 가정 설치 제약 → 공간 Integration으로 보완
출처 [S19~S25 · S41 · S45 · S46 · S49~S51] · 비교 축 = 접근 방식 (공개 자료) · 특허 = 출원 후보 (등록 미정)
```

## 16. TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발

```text
16  TIPS R&D / 24개월 Roadmap
TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발
TIPS 과제 10.67억원 = WP1~6 기술 검증 · Seed = 기관부담금 · 과제 외 인건비 · 고객 · 실증 · 사업 검증
TIPS 과제  ·  기술 검증 (Technology De-risking)
WP1 Adaptive Kitchen Robot Hand
WP2 Kitchen Manipulation Skill
WP3 Perception / Calibration
WP4 Minimal Environment Interface
WP5 Human-Robot Safety
WP6 Integrated CLEAN 실증
민간 Seed  ·  사업 검증 (Commercial Validation)
과제 외 인건비 (사업 · 현장 · 지원)
목업 · 시제품 운영
고객 검증 · WTP
Pilot 운영 · 유료 전환
Partner 개발
BM 검증 · 기관부담금
0~6M
· 주방 작업 분석
· Robot 구조 설계
· Hand 시제품 v1
· 식기 30종 파지 시험
· 초기 Calibration
7~12M
· CLEAN Skill
· 식세기 연동
· Hand v2 · 안전 기능
· 1:1 주방 목업
· 목업 CLEAN 전 과정
13~18M
· 주방 3종 적용
· 주방 간 Transfer 시험
· 실패 복구
· Pilot 착수
· WTP 검증
19~24M
· 신뢰성 (연속 운전)
· 설치 표준
· 가정 실증 3세대
· BOM · 설치 · 서비스 원가
· 유료 실증 · Partner 조건
M6
상용 Gripper 대비 Hand 비교 (30종) → Build / Buy 결정
M12
목업 CLEAN 전 과정 · 식기 성공률 ≥ 80%
M18
주방 3종 Transfer (하락 ≤ 10%p) · WTP n≥300
M24
가정 3세대 성공률 ≥ 90% · 유료 전환 ≥ 2세대 · 원가 실측
[TARGET]
TIPS 2026 일반트랙: 정부 R&D 최대 8억원 · 24개월 · 정부 75% 이내 · 기관부담 25% 이상 [S33 · S52] · KPI: 부록 A1~A3
```

## 17. Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획

```text
17  Founder / Team
Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획
필요 역량 = 로봇 조작 (Hand · Skill) · 주방 · 건축 설치 · 고객 · Partner 영업
확인 항목 | Founder 1 (대표) | Founder 2 (확보 여부 확인)
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
TIPS 요건: 대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 30% 이하 · 정부지원 5억원당 청년 1명 신규 채용 [S33]
```

## 18. 24개월 사용 23.4억원 · Seed 14~19억원 요청 (TIPS 8억원 별도)

```text
18  Investment Ask / 24M Value Creation
24개월 사용 23.4억원 · Seed 14~19억원 요청 (TIPS 8억원 별도)
Bottom-up 사용처 산정 · Seed 범위 = Lean (팀 · 범위 축소) ~ Base (기술 + 사업 검증 + 3개월 Buffer)
사용처 (억원) | 24개월 | TIPS 편성
인건비 · 연구수당 | 15.55 | 6.90
Robot HW · Hand · Mock-up | 2.39 | 2.01
Software · Data | 0.55 | 0.44
Pilot · 실증 순비용 | 0.73 | -
Customer · Partner | 0.60 | -
Certification · IP | 1.05 | 0.71
Space · Operating | 1.86 | 0.60
예비비 (10%) | 0.68 | -
24개월 지출 합계 | 23.41 | 10.67
TIPS 정부지원 (선정 시 · 상한) | 8.00 | ASSUMPTION
기관부담 (현금 · 현물) | 2.67 | Seed 부담
Seed Base = 지출 − TIPS + Buffer 3.55 | 18.96 | DERIVED
Seed Lean (지출 19.11억원 규모) | 13.78 | DERIVED
TIPS 미선정 시 (Lean 범위) | 21.52 | DERIVED
TODAY
Concept
기술 가설
사업 가설
Seed
+
TIPS
24M TARGET
[TARGET]
기술
실제 주방 작동 시제품
Adaptive Robot Hand
Skill Library
Calibration System
안전 구조
주방 3종 시험
Transfer 증거
경제성
Robot BOM
설치 원가
서비스 원가
시장
Customer WTP
실증 · 유료 실증
Partner 조건
특허 출원
NEXT ROUND
제품화 · 양산
같은 Platform → ASSIST Skill
Retrofit · 신축 채널 확대
Installed Base 반복매출
Series A 판단 기준  기술 성공 + 유료 전환 + 설치 · 서비스 원가 실측
Series A 이후 Y3~Y4 현금 소요 약 68억원 · 손익분기 연 약 1,376세대 (DERIVED, 부록 D4) · Buffer = Y2 월평균 지출 × 3개월 · TIPS 과제 10.67억원 = 정부 8 + 기관부담 2.67 (현금 1.35 · 현물 1.32) · 운영사 선투자 (수도권 2억원 이상) = Seed 포함
```
