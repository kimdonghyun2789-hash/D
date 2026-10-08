> **저장소 구성** — `MH/`: MH Robotics Seed · TIPS IR Package (2026.10, Draft v5: 본문 18장 + 부록 35장 · 수식 재무모델 · 결과물 문서 20종 · 투자심사 Memo) → [`MH/README.md`](MH/README.md). 이전 판 ARKI Robotics v4는 `MH/archive/ARKI_v4/`에 보관. 아래는 기존 SoftHand Seed IR.

# SoftHand — 투자유치 사업계획서 (Seed, 최종본)

**사람용 도구를 잡고 사용하는 소프트 로봇핸드 개발 및 사업화**
4지·5지 소프트 로봇핸드와 도구 사용 제어 소프트웨어, 천장 이동형 양팔 로봇 주방으로 확장 · Seed 20억 원 / 24개월 · 초기 고객: 로봇 SI·반복 취급 공정 보유 제조기업

## 이번 수정 (5차, 최종본)

기존 사업계획서(스타트업 투자유치 사업계획서, 2026.10.6)를 반영해 수치·사업 순서·제품 정의를 사업계획서와 통일. 4차의 사업계획서 형식·문체(번호 붙은 항목, 표·숫자 중심, 개조식)는 유지.

- 사업 순서: 핸드 + 도구 사용 제어 SDK를 로봇 SI·제조 반복 취급 고객에 먼저 판매, 로봇 주방은 3년차부터 주방 제조사와 공동 판매하는 응용 제품
- 재무: 사업계획서 기준 시나리오 (5년차 매출 112억 원, 영업이익 17.55억 원, 4년차 흑자 전환, 1~2년차 누적 영업손실 14.49억 원), 가격·원가, Seed 사용 6항목, 핵심 인력 7명
- 추가: 비전 AI 제어 흐름, 천장 이동형 양팔 로봇 주방, 성능 목표 10개 지표와 출시 게이트, 경쟁 비교(qbrobotics·Moley·YORI), 위험 7개·투자 실사 전 증거 8개, 대표자 발표 문안(발표자 노트)
- 이미지: 사업계획서 구성(천장 LM 이동축 + 역설치 양팔 + 공통 캐리지)에 맞춘 주방 렌더링 2장 신규 제작
- 검증: 재무 모델(`source/deck/model.py`)이 사업계획서의 매출·총이익·영업손익·민감도·누적 손실·자금 사용 합계를 그대로 재현하는지 assert로 검사

상세 내용은 `SoftHand_IR_Revision_Report` (통합 원칙, 슬라이드별 변경, 사업계획서와 수치 대조, 투자 심사 관점 평가) 참고.

## 산출물

| 파일 | 내용 |
|---|---|
| `SoftHand_Founding_Seed_IR_Deck_Final.pptx` | 투자유치 사업계획서, 33장 (본문 17 + 부록 목차 1 + 부록 15), 16:9 |
| `SoftHand_Founding_Seed_IR_Deck_Final_preview.pdf` | 검토용 PDF |
| `SoftHand_IR_Revision_Report.docx` / `.md` | 5차 수정 보고서 |
| `assets/renders/kitchen/` | 주방 장면 렌더링 (`ck_*`: 천장 이동형 양팔 구성, 본문 06장·부록 A6·A7 / `lx_*`: 작업 장면, 부록 A6 / `pro_*`: 교체용) |
| `assets/renders/` | SoftHand-4 콘셉트 렌더링 (`product`: 본문 03장 / `raw/`: 제조 반복 취급 장면, 부록 A5) |
| `assets/original/` | 원본 덱 이미지 2장 (미사용, 보존) |
| `source/` | 사업계획서·보고서·재무 모델·렌더링 생성 코드 |

## 구성

| 장 | 항목 | 제목 |
|---|---|---|
| 01 | 표지 | 사람용 도구를 잡고 사용하는 소프트 로봇핸드 개발 및 사업화 |
| 02 | 01 투자 제안 요약 | 핸드·제어 소프트웨어로 시작해 로봇 주방으로 확장하는 사업 |
| 03 | 02 고객 문제와 사업 기회 | 다품종 작업의 그리퍼 교체·재설정 부담과 사람용 도구 조작의 한계 |
| 04 | 03 제품 구성과 사업 범위 | 초기 제품은 4지 핸드와 제어 SDK, 5지 핸드와 로봇 주방은 확장 제품 |
| 05 | 04 소프트 핸드 핵심 기술 | 소프트 접촉면과 하중 지지 골격을 결합한 하이브리드 핸드 |
| 06 | 05 비전 AI와 촉각·힘 제어 | 인식부터 작업 결과 확인까지 하나의 제어 흐름으로 개발 |
| 07 | 06 천장 이동형 양팔 로봇 주방 | 로봇 주방은 3년차부터 주방 제조사와 공동 판매하는 응용 제품 |
| 08 | 07 성능 목표와 검증 계획 | 작업 완료율과 사람 개입 시간 중심의 12·24개월 성능 목표 |
| 09 | 08 경쟁·차별화·지식재산 | 차별화 요소는 동일 조건 비교 시험과 고객 평가로 검증 |
| 10 | 09 시장 진입 전략 | 비가열 취급·정렬·저하중 도구 작업으로 진입해 SI 반복 판매로 확대 |
| 11 | 10 시장 규모·가격·고객 경제성 | 시장 규모는 고객 후보와 판매 단가를 곱하는 상향식으로 산정 |
| 12 | 11 5개년 재무 계획 | 5년차 매출 112억 원, 영업이익 17.55억 원 (기준 시나리오, 가정) |
| 13 | 12 개발 일정 | 36개월 6단계 개발, 단계 통과 조건을 충족하면 다음 단계로 진행 |
| 14 | 13 Seed 자금 사용 계획 | Seed 20억 원은 24개월 개발·유료 실증의 현금 집행 한도 |
| 15 | 14 조직 및 인력 | 핵심 인력 7명 단계 채용, 안전·위생·특허·주방 설계는 외부 협력 |
| 16 | 15 제품화 위험과 투자 검증 항목 | 주요 위험 7가지와 투자 실사 전에 확보할 증거 8가지 |
| 17 | 16 투자 제안 | Seed 20억 원으로 24개월 내 제품 성능과 유료 고객 경제성 입증 |

부록: A1 작성 전제와 사실·가정 구분 · A2 작업군별 개발 단계와 도구별 제어 · A3 핸드 설계 상세 · A4 비전 AI·데이터 상세 · A5 적용 장면: 제조 반복 취급 · A6 적용 장면: 주방 작업 · A7 로봇 주방 설치·운영 상세 · A8 경쟁 상세 · A9 시장 근거 상세 · A10 로봇 기술 동향 · A11 가격·원가·판매 조건 가정 · A12 5개년 재무 상세와 민감도 · A13 Seed 자금 사용 상세 · A14 안전·위생·인증·지식재산 · A15 출처

## 외부 제출 전 입력할 정보

확인되지 않은 정보는 만들지 않고 `[입력 필요]`로 남김.

| 항목 | 위치 |
|---|---|
| 회사 현황 (회사명·대표자·설립일·소재지·지식재산) | 02 |
| 창업자 정보 (성명·경력·보유 기술·이 사업과의 연결·공동창업 여부·참여 조건) | 15 |
| 투자 조건 (투자 형태·기업가치·지분율·라운드 현황·후속 투자 규모) | 14 · 17 |
| 월별 채용·인건비 계획, 월별 현금계획 | 14 · A13 |
| 투자 실사 전 증거 8가지 | 16 |
| 연락처 | 01 · 17 |
| 실물 이미지 (시제품 사진 → 시험 영상 → 고객 현장 순으로 교체) | 04 · 07 · A5 · A6 |

## 다시 만들기

재무 모델(`source/deck/model.py`)이 덱과 보고서의 숫자를 함께 관리하며, 사업계획서 수치와 다르면 실행 단계에서 멈춤.

```bash
pip install python-pptx python-docx pillow numpy lxml

python3 source/deck/model.py           # 재무 모델 → source/deck/model.json (사업계획서 수치 검사 포함)
python3 source/deck/build.py --pdf     # 덱 + 검토용 PDF
python3 source/deck/make_report.py SoftHand_IR_Revision_Report.md SoftHand_IR_Revision_Report.docx   # 덱 생성 후 실행
```

- 글꼴: Noto Sans KR (Regular·Bold). 발표용 PC에 설치되어 있지 않으면 대체 글꼴로 줄바꿈이 달라질 수 있음
- 글자 넘침 검사: `NotoSansKR-400.ttf`·`NotoSansKR-700.ttf`를 `~/.fonts` 또는 `NOTO_KR_DIR`에 두면 실제 글꼴 폭으로 검사
- 검토용 PDF: LibreOffice 사용. 영문·숫자와 한글 사이 자동 간격을 끈 상태로 변환. LibreOffice는 한글을 음절 단위로 줄바꿈할 수 있어 긴 항목은 원고에서 줄을 나눠 둠
- 발표자 노트: 02·17장 노트에 사업계획서의 대표자 발표 문안 수록

**콘셉트 렌더링 (선택)**: three.js r170을 Headless Chromium에서 렌더링.

```bash
cd source/render3d
npm install                          # three@0.170.0, playwright
npx playwright install chromium      # Chromium이 없는 경우만
mkdir -p final
bash batch.sh && python3 make_assets.py                    # 핸드·제조 장면 → assets/renders/
bash batch_kitchen.sh && python3 make_kitchen_assets.py    # 주방 장면 (양팔·LM 이동축 포함) → assets/renders/kitchen/
```

## 폴더 구조

```
.
├── SoftHand_Founding_Seed_IR_Deck_Final.pptx
├── SoftHand_Founding_Seed_IR_Deck_Final_preview.pdf
├── SoftHand_IR_Revision_Report.docx / .md
├── assets/
│   ├── renders/      # kitchen/ 주방 장면, raw/ 제조 장면, product·screwdriver 핸드 이미지
│   └── original/     # 원본 덱에서 보존한 이미지
└── source/
    ├── deck/         # model.py · build.py · kit.py · slides_main.py · slides_appx.py · to_pdf.py · make_report.py
    └── render3d/     # shot.js · batch.sh · batch_kitchen.sh · make_assets.py · make_kitchen_assets.py · web/(lib.js · scenes.js · kitchen.js · luxe.js)
```
