# MH Robotics — Seed · TIPS IR 산출물 Index

> MH Robotics · Seed 투자 · TIPS 운영사 검토용 IR · Draft v5 · 2026-10-08  
> Concept 단계: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 숫자는 FACT / DERIVED / ASSUMPTION / TARGET, 그림은 CONCEPT로 표기.

## 결과물 (Spec 38 순서)

| No | 산출물 | 파일 | 내용 |
|---|---|---|---|
| 01 | Executive Summary | [01_Executive_Summary.md](01_Executive_Summary.md) | 회사 정의 · 문제 · 접근 · 제품 · BM · 시장 · 자금 · 24개월 Evidence · 판단 요약 |
| 02 | Main IR Deck | [02_Main_IR_Deck.md](02_Main_IR_Deck.md) | 본문 18장 구성 (Spec 35 순서) · 장별 핵심 메시지 · Red-team 질문 연결 · 부록 34장 목록 |
| 03 | 각 Slide 실제 화면 문구 | [03_Slide_Text.md](03_Slide_Text.md) | 본문 화면 문구 전체 (표기 순서 그대로) |
| 04 | 각 Slide Visual 구성 | [04_Slide_Visual.md](04_Slide_Visual.md) | 장별 레이아웃 · 사용 이미지 · CONCEPT 표기 |
| 05 | Diagram / Chart | [05_Diagram_Chart.md](05_Diagram_Chart.md) | 필수 Visual 8종 위치 · 도표별 Data 출처 · 3D 렌더 재생성 방법 |
| 06 | Speaker Note | [06_Speaker_Notes.md](06_Speaker_Notes.md) | 장별 발표 메모 · 예상 발표 시간 |
| 07 | 시장 Data 및 Source | [07_Market_Data_Sources.md](07_Market_Data_Sources.md) | 주택 · 리모델링 · 렌탈 · Care · Robot Arm · Hand Benchmark · 경쟁 · 기준 · 출처 전체 |
| 08 | FACT / DERIVED / ASSUMPTION / TARGET 구분표 | [08_Tag_Register.md](08_Tag_Register.md) | 재무모델 입력 108개 전체 · 주요 계산값 · CONCEPT 목록 |
| 09 | Business Model | [09_Business_Model.md](09_Business_Model.md) | INSTALL → OPERATE → EXPAND · 가격 가설 · Rental · Care · Consumables · MH Core vs Partner |
| 10 | 5-Year Household Economics | [10_Household_Economics_5Y.md](10_Household_Economics_5Y.md) | 대표 1세대 5년 매출 · 매출총이익 · 서비스 원가 · Lifetime Contribution · 범위 · 민감도 |
| 11 | TIPS R&D Work Package | [11_TIPS_RnD_Work_Package.md](11_TIPS_RnD_Work_Package.md) | TIPS (Technology De-risking) vs Seed (Commercial Validation) · WP1~WP6 · 과제 편성 |
| 12 | Technical KPI | [12_Technical_KPI.md](12_Technical_KPI.md) | Manipulation · Application · Business KPI 20개 · Benchmark · 목표 근거 · Hand 시험 계획 |
| 13 | Patent Portfolio | [13_Patent_Portfolio.md](13_Patent_Portfolio.md) | 출원 후보 12개 묶음 · 사업 중요도 · 차별성 · Prior Art Risk · 우선순위 |
| 14 | 24개월 Roadmap | [14_Roadmap_24M.md](14_Roadmap_24M.md) | 0~6 · 7~12 · 13~18 · 19~24M 실행 · Gate · 채용 · 24M Value Creation |
| 15 | Funding Plan | [15_Funding_Plan.md](15_Funding_Plan.md) | 24개월 사용처 · TIPS 과제 편성 · Seed 범위 산식 · 5개년 계획 맥락 |
| 16 | 투자심사 예상질문 20개 | [16_Investor_Questions_20.md](16_Investor_Questions_20.md) | 질문 · 심사역이 확인하려는 것 · 답하는 위치 |
| 17 | 각 질문의 방어논리 | [17_Defense_Logic.md](17_Defense_Logic.md) | 방어논리 · 근거 (Tag) · 약한 부분 · 보강 Evidence |
| 18 | 현재 부족한 Evidence | [18_Evidence_Gaps.md](18_Evidence_Gaps.md) | Evidence Gap · Risk Register · 첫 90일 실행 목록 |
| 19 | Founder 입력 필요정보 | [19_Founder_Inputs.md](19_Founder_Inputs.md) | Founder 입력 항목 · TIPS 요건 · 증빙 · 입력 양식 |
| 20 | 투자심사 Memo | [20_Investment_Memo.md](20_Investment_Memo.md) | 심사 의견 · Scorecard · 판단 MEET · 판단을 바꿀 Evidence 5개 |

## 함께 보는 파일

| 파일 | 내용 |
|---|---|
| `MH/MH_Robotics_Seed_TIPS_IR_Deck.pptx` | 본문 18장 + 부록 35장 (A TIPS 과제 · B 제품 · 기술 · C 시장 · 경쟁 · D 경제성 · E IP · 리스크 · Q&A · F 참고), 16:9 |
| `MH/MH_Robotics_Seed_TIPS_IR_Deck_Main.pdf` | 본문 18장만 (발표 · 송부용) |
| `MH/MH_Robotics_Seed_TIPS_IR_Deck_preview.pdf` | 본문 + 부록 전체 (검토용) |
| `MH/MH_Robotics_Financial_Model.xlsx` | 수식 재무모델: Inputs (Tag · 출처) · 5Y FM (3 Scenario) · Household · Unit Economics · Market · Budget_24M · Sensitivity |
| `MH/source/model.py` → `model.json` | 모든 숫자의 단일 원본 (deck · xlsx · docs가 같은 값을 사용) |
| `MH/archive/ARKI_v4/` | 이전 판 (ARKI Robotics v4) Deck · PDF · 재무모델 · 문서 — 삭제 없이 보관 |

## 재생성 순서

```bash
cd MH/source
python3 model.py                 # model.json (입력 · 계산 · 자금 계획)
python3 xlsx_model.py            # 수식 xlsx
python3 /mnt/skills/public/xlsx/scripts/recalc.py ../MH_Robotics_Financial_Model.xlsx 120
python3 check_xlsx.py            # xlsx 수식값 = model.json 대조
python3 build.py --pdf           # pptx + 본문 PDF + 전체 PDF (fit 검사 포함)
python3 gen_docs.py              # 이 문서들
```

## 작성 원칙

- 없는 고객 · 계약 · LOI · 파트너 · 매출 · Founder 이력은 쓰지 않음. Founder 칸은 `[Founder 정보 필요]`.
- "최초 · 압도적", 근거 없는 ROI · 비용절감률 · 점유율 · Robot 성능, 특허 등록 확정 표현 없음.
- 주방 전체 표준화가 아니라 Robot 적응 (Hand · Skill · Calibration) + 반복 작업점의 최소 Interface.
- 초기 Mass Market 진입 없음: Premium Remodeling → 호환 주방 Retrofit → 신축 B2B2C.
- 투자 요청액은 24개월 사용처에서 Bottom-up으로 계산하고, TIPS는 별도 재원으로 구분.
