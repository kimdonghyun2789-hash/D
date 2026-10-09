# MH Robotics — Seed · TIPS IR Package (최종본, 2026.10)

**Kitchen Manipulation Robotics System — Adaptive Robot Hand · Manipulation Skill · Calibration · Environment Integration**

> Concept 단계 (시제품 · 고객 · 계약 · LOI · 파트너 · 매출 · 투자유치 없음). 수치 = FACT / DERIVED / ASSUMPTION / TARGET (+ CONCEPT · TBV · FUTURE). Founder 칸 = `[Founder 정보 필요]`. 평면 = 제공 도면 재작도 (단지명 미표기)

## 산출물

| 파일 | 내용 |
|---|---|
| `MH_Robotics_Seed_TIPS_IR_Final.pptx` | 제출용 IR: 본문 18장 + 부록 28장 + 목차 (16:9, 발표 요지 Notes 포함) |
| `MH_Robotics_Seed_TIPS_IR_Final_Main.pdf` | 본문 18장 (발표 · 운영사 송부용) |
| `MH_Robotics_Seed_TIPS_IR_Final.pdf` | 본문 + 부록 전체 |
| `MH_Robotics_IR_Internal_QA.pptx` · `.pdf` | 내부 검토용 7장 (예상질문 · 방어논리 · Evidence · Founder 입력 · 투자심사 Memo · Tag 원칙) — 제출 제외 |
| `MH_Robotics_Financial_Model.xlsx` | 수식 기반 모델: Inputs (Tag · 출처) → 5Y FM 3 Scenario · Household · Unit_Economics · Market · Budget_24M · Sensitivity · Sources |
| `docs/00~20` | 결과물 20종 (01~15 제출 · 공유용 · 16~20 내부 검토용) · [docs/00_README_Index.md](docs/00_README_Index.md) |
| `render3d/` | 3D 콘셉트 렌더 생성기 (three.js + Playwright) · 충돌검사 · 보관/전개 경로 · 평면 JSON · Adaptive Hand 모델 (`web/hand.js`) |
| `assets/renders/` | 덱에 들어간 렌더 PNG + Callout Anchor · 충돌검사 JSON |
| `archive/ARKI_v4/` | 이전 판 (ARKI Robotics v4) 덱 · PDF · 재무모델 · 문서 · 문서 생성기 — 삭제 없이 보관 |

## 본문 구성 (18장)

| 쪽 | 구성 | 화면 제목 |
|---|---|---|
| 01 | MH Robotics · Kitchen Manipulation Robotics System | MH Robotics — Kitchen Manipulation Robotics System |
| 02 | 가전 자동화 이후 남은 Physical Workflow | 가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workflow |
| 03 | 왜 Kitchen인가 | 주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간 |
| 04 | 가정용 Robot 적용의 구조적 한계 | 주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계 |
| 05 | MH Robotics Technology Strategy | Robot 적응 + 반복 작업점에만 최소 Interface |
| 06 | Adaptive Kitchen Robot Hand | 핵심 Hardware: 주방 물체 대응 Adaptive Robot Hand |
| 07 | Manipulation Skill / Calibration | 핵심 기술: Calibration 기반 Skill의 주방 간 이전 |
| 08 | MH Kitchen Robotics System | MH Kitchen Robotics System: 5개 Layer 통합 제품 |
| 09 | 첫 검증 Workflow: CLEAN → ASSIST → COOK | CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장 |
| 10 | Existing / Remodeling / New-build 적용 | 단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · 신축) |
| 11 | Business Model | 설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM |
| 12 | Market / Beachhead | Bottom-up 시장 산정: 세대 수 × 적용률 × 단가 |
| 13 | GTM / Partner Distribution | Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장 |
| 14 | Technology-to-Economics / Moat | R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조 |
| 15 | IP / Competition | 경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증 |
| 16 | TIPS R&D / 24개월 Roadmap | TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발 |
| 17 | Founder / Team | Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획 |
| 18 | Investment Ask / 24M Value Creation | 24개월 사용 23.4억원 · Seed 14~19억원 요청 (TIPS 8억원 별도) |

부록: A TIPS 과제 상세 (KPI · WP · Gate · 과제 편성 · 팀) · B 제품 · 기술 (Hand 시험 · 평면 5종 · Robot Home · 대표 평면 · Safety · BOM) · C 시장 · 경쟁 · D 경제성 · 재무 (가격 · Household · Unit Economics · 5Y FM · 민감도) · E IP · Risk · F 출처

## 핵심 결과 (Base, 전부 DERIVED from ASSUMPTION · 물량은 TARGET)

- 1세대 5년 (Remodeling · 구매): 설치 시점 2,020만원 · 5년 매출 2,418만원 · Lifetime Contribution 428만원 (Y3 원가) → 798만원 (Y5 원가). Conservative는 Y3 원가 기준 적자 → WTP · BOM이 1 · 2순위 변수
- 가치 Gap: CLEAN만의 가사 대체 가치 월 약 18만원 < Rental 월 33만원 → Premium 고객 · ASSIST 확장 · WTP 검증 (M18)
- 시장 (Bottom-up): SAM 연 3,676억원 (Remodeling 3,212 · Retrofit 280 · New-build 184) · Y5 계획 91.5억원 = 대상 세대 2.5%
- 5개년: Y5 매출 91.5억원 · 설치 560세대 · 영업이익 -33.6억원 · 누적 현금 최저 -125억원 · 손익분기 연 약 1,376세대
- 24개월: 지출 23.4억원 = TIPS 정부지원 8억원 (선정 시) + Seed 14~19억원 (Lean 13.8억원 ~ Base 19.0억원, Buffer 3개월 포함) · TIPS 미선정 시 21.5억원. TIPS 과제 10.67억원 (정부 8 + 기관부담 2.67)
- Series A 이후 Y3~Y4 현금 소요 약 68억원 · Rental Partner 단순 회수 약 49개월 (요구 36개월 가정 → 조건 협의)
- 내부 검토 판단: **MEET** — 판단을 바꿀 Evidence 5개: Founder · 핵심 팀 · 기술 Baseline (M3 이내) · 고객 행동 · 설치 경제성 · Partner ([docs/20](docs/20_Investment_Memo.md))

## Environment Interface 예 (Remodeling 채널, 3D 모델 기준 CONCEPT)

- 주방 전체 표준화가 아니라 반복 작업점에만 최소 Interface: Robot Home (Dock) · Rail · 식세기 Interface · Storage Dock · Vision Reference. Retrofit은 Compact Mount · Dock, New-build는 설계 단계 반영
- Remodeling 예 (부록 B3 · B4): 로봇 작업 줄 Robot Home 45 · Drop Zone 70 · 싱크 80 · 서랍 60 · 식세기 60cm. Rail은 상부장 하단 (약 139cm), 바닥 사용 안 함. 조리기구 구역 = 로봇 금지 구역
- 낮은 작업점: 식세기 하단 랙을 44cm 당겨 위에서 적재 (Gripper 최저 약 37cm), 서랍도 열어서 위에서 넣음
- 충돌검사: 로봇 링크 = 캡슐, 가구 = 상자. 작업 자세 · 보관 · 전개 경로 · Rail 이동 · 자기충돌 관통 0cm (`assets/renders/*.json`의 `ik`). 실제 기구 검증 전

## 확보 평면 5종 (Kitchen Variation 근거, 부록 B2)

| 평면 | 구분 | 크기 (mm) | 주방 형태 | 3D | 기본 배치 |
|---|---|---|---|---|---|
| 구축 2Bay A | 구축 · 계단실형 (코어 포함) | 12,390 × 11,670 | ㄱ자 (윗벽 3,255mm + 옆벽) | 완료 · 원본과 겹쳐 확인 | 수용: Remodeling 한 줄 3,150mm · 충돌검사 0cm (B4) |
| 구축 2Bay B | 구축 · 전면 발코니 | 10,940 × 8,500 | ㄱ자 (싱크 줄 약 2.6m + 아랫벽) · 거실과 개방 | 완료 | 미수용 · 냉장고 이전 시 약 3.3m |
| 신축 2Bay | 신축 · 탑상형 | 15,120 × 10,730 | 옆벽 + 윗벽 + 아일랜드형 카운터 | 미착수 | 미검토 |
| 신축 3Bay | 신축 · 판상형 | 12,400 × 10,550 | 윗벽 싱크 줄 약 2.6m + 옆벽 쿡탑 + 반도형 | 완료 | 미수용 · 단축형 (Compact Mount) 검토 |
| 신축 4Bay | 신축 · 판상형 | 14,700 × 9,780 | 윗벽 싱크 줄 약 2.8m + 옆벽 쿡탑 + 반도형 | 완료 | 미수용 · 단축형 검토 |

## 다시 만들기

```bash
pip install python-pptx openpyxl pillow lxml pypdf          # LibreOffice: PDF · xlsx 재계산
python3 MH/source/model.py          # 가정 · 계산 · 24개월 예산 · Seed 범위 → model.json
python3 MH/source/xlsx_model.py     # 수식 기반 xlsx
python3 /mnt/skills/public/xlsx/scripts/recalc.py MH/MH_Robotics_Financial_Model.xlsx 120
python3 MH/source/check_xlsx.py     # xlsx 수식값 ↔ model.json 교차검증
cd MH/render3d && npm install && bash render_v2.sh && bash render_plans.sh && bash render_hand.sh && for f in render_fig_*.sh; do bash $f; done && cd ../..   # 3D 렌더 (선택)
python3 MH/source/build.py --pdf    # 제출용 덱 + 본문 PDF + 전체 PDF + 내부 검토용 (fit 검사, --png: 미리보기)
python3 MH/source/gen_docs.py       # docs/*.md + 이 README
```

- 단일 원천: `source/model.py` (입력 · Tag · 출처 · 계산) → `model.json` → 덱 · xlsx · 문서. 정성 표 (KPI · WP · Gate · IP · Risk · Q&A · Evidence · Founder 항목 · 경쟁 · 기준 · 평면)는 `source/content.py`.
- 덱: `source/slides_mh.py` (본문) · `source/slides_mh_apx.py` (부록 · 내부 검토용) · 공용 `kit.py` · `common.py` · `mhkit.py`. 이전 판 코드 = `archive/ARKI_v4/source`.

## 외부 제출 전 입력 · 확인

| 항목 | 위치 |
|---|---|
| Founder 2인 정보 · 증빙 · 지분 · 전업 여부 (Founder 2 확보 여부 포함) | 본문 17쪽 · 내부 I4 · docs/19 |
| TIPS 공고 원문 대조 (정부지원 비율 · 기관부담 현금 · 간접비 · 운영사 선투자 · 창업팀 지분 · 청년 채용) · 접수 일정 | 본문 16 · 18쪽 · 부록 A6 · docs/11 |
| 운영사명 · 투자 조건 (형태 · 기업가치 · 지분) | 본문 18쪽 (협의) |
| 공식 통계 · 회사 발표 원문 대조 (보도 인용분, 조회일 2026-10-07~08) | 부록 C1 · C2 · F1~F4 · docs/07 |
| 가격 · 원가 가정 (ASP · Interface · Rental · Care · BOM) → 견적 · WTP 결과로 교체 | 부록 D1 · B6 · docs/09 · 10 |
| 특허 후보 → 선행기술조사 · 변리사 검토 | 본문 15쪽 · 부록 E1 · docs/13 |
