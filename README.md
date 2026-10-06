# SoftHand — 창업 및 Seed 투자 제안서 (최종 수정본)

**사람용 설비를 그대로 쓰는 로봇 핸드, SoftHand-4**
기존 설비를 크게 바꾸지 않는 머신텐딩 자동화 · Seed 20억 원 / 24개월

## 이번 수정 (2차)

- 문체: 제목과 본문을 개조식 한국어로 다시 작성, 영어는 제품명·슬로건·업계 약어(PoC·SI·OEM)만 사용
- 디자인: 흰 배경, 큰 제목, 주황은 장마다 핵심 1곳, 3D 렌더링은 사각형 사진형으로 배치
- 구성: 2장 투자 요약, 8장 시장 규모와 "왜 지금인가", 15장 투자 요청, 16장 마무리에서 요청 금액 재강조
- 사업 전략·재무 모델·Seed 집행 계획은 1차 수정 내용 유지

상세 내용은 `SoftHand_IR_Revision_Report` (기존 → 수정 → 이유 → 투자자 효과) 참고.

## 산출물

| 파일 | 내용 |
|---|---|
| `SoftHand_Founding_Seed_IR_Deck_Final.pptx` | 최종 IR 덱, 33장 (본문 16 + 부록 목차 1 + 부록 16), 16:9 |
| `SoftHand_Founding_Seed_IR_Deck_Final_preview.pdf` | 검토용 PDF |
| `SoftHand_IR_Revision_Report.docx` / `.md` | 수정 보고서: 2차 수정 상세, 1차 필수 변경 반영 위치, 재무, VC 예상 질문 17개, 제출 전 입력 정보 |
| `assets/renders/` | SoftHand-4 콘셉트 렌더링 (`raw/`: 장면 렌더링, `*.png`: 핸드 단독 이미지) |
| `assets/original/` | 원본 덱에서 유지한 이미지 2장 (전용 그리퍼, 천장형 주방) |
| `source/` | 덱·보고서·재무 모델·렌더링 생성 코드 |

## 덱 구성

| 장 | 제목 |
|---|---|
| 01 | 사람용 설비를 그대로 쓰는 로봇 핸드 (표지) |
| 02 | 설비를 크게 바꾸지 않는 로봇 자동화, 첫 시장은 머신텐딩 (투자 요약) |
| 03 | 로봇 도입마다 반복되는 설비 재설계 |
| 04 | 설비는 그대로, 핸드가 사람처럼 사용 |
| 05 | 핸드 하나로 공정 하나 완결 |
| 06 | 첫 시장은 다품종 머신텐딩 |
| 07 | 구매 이유: 품목이 바뀌어도 다시 쓰는 자동화 |
| 08 | 첫 시장은 이미 공장에 설치된 로봇 |
| 09 | 고객 프로젝트를 표준 스킬로 축적 |
| 10 | 제품 판매로 시작, 스킬과 로봇 제조사 탑재로 확장 |
| 11 | 경쟁 기준은 설비 변경 없이 끝낸 작업 수 |
| 12 | 5년차 매출 44.7억 원, 손익분기 근접 |
| 13 | 24개월 4단계 검증 계획 |
| 14 | 이 문제를 풀 수 있는 팀 |
| 15 | Seed 20억 원, 24개월 사업성 검증 |
| 16 | 공장에서 시작, 사람 손이 필요한 현장으로 확장 |

부록: A1 주요 가정과 근거 수준 · A2 단계별 점검 기준 · A3 경쟁사 상세 · A4 피지컬 AI 흐름 · A5 시장 근거 · A6 핸드 설계 · A7 성능 지표 · A8 스크루드라이버 데모 · A9 수익 모델 가정 · A10 5개년 손익 · A11 자금 사용 · A12 데이터 축적 · A13 주방 데모 · A14 안전·인증·IP · A15 위험과 대응 · A16 출처

## 외부 제출 전 입력할 정보

확인되지 않은 정보는 만들지 않고 `[… 입력 필요]`로 남김.

| 항목 | 위치 |
|---|---|
| 회사명 `[회사명 입력 필요]` | 01 · 16 |
| 창업자 정보 (이름·사진·경력·시제품·연구실적·특허, 질문 3개에 대한 답, 참여 조건) `[정보 입력 필요]` | 14 |
| 투자 조건 (기업가치·지분율) `[투자 조건 입력 필요]` | 15 |
| 대표자 연락처 `[대표자명 · 이메일 · 연락처 입력 필요]` | 16 |
| OEM 매출 구조의 각 항목 `[OEM 협의 후 검증]` | 10 · A9 |
| 공동개발 고객 3곳 (현재 목표, 확보 시 실명·상태 표기) | 10 · 13 · 15 |
| 실물 이미지 (시제품 사진 → 시험 영상 → 고객 현장 → CAD 순으로 교체) | 전 장 |

## 다시 만들기

재무 모델(`source/deck/model.py`)이 덱과 보고서의 숫자를 함께 관리.

```bash
pip install python-pptx python-docx pillow numpy lxml

python3 source/deck/model.py           # 재무 모델 → source/deck/model.json
python3 source/deck/build.py --pdf     # 덱 + 검토용 PDF
python3 source/deck/make_report.py SoftHand_IR_Revision_Report.md SoftHand_IR_Revision_Report.docx
```

- 글꼴: Noto Sans KR (Regular·Bold). 발표용 PC에 설치되어 있지 않으면 대체 글꼴로 줄바꿈이 달라질 수 있음
- 글자 넘침 검사: `NotoSansKR-400.ttf`·`NotoSansKR-700.ttf`를 `~/.fonts` 또는 `NOTO_KR_DIR`에 두면 실제 글꼴 폭으로 검사
- 검토용 PDF: LibreOffice 사용. 영문·숫자와 한글 사이 자동 간격을 끈 상태로 변환해 PowerPoint 화면과 같은 문장으로 출력
- 보고서의 민감도 문구는 `model.py` 출력값을 옮겨 적은 것이므로 가정을 바꾸면 함께 갱신

**콘셉트 렌더링 (선택)**: three.js r170을 Headless Chromium에서 렌더링.

```bash
cd source/render3d
npm install                          # three@0.170.0, playwright
npx playwright install chromium      # Chromium이 없는 경우만
mkdir -p final && bash batch.sh      # 장면·핸드 렌더링 → final/
python3 make_assets.py               # → assets/renders/
```

## 폴더 구조

```
.
├── SoftHand_Founding_Seed_IR_Deck_Final.pptx
├── SoftHand_Founding_Seed_IR_Deck_Final_preview.pdf
├── SoftHand_IR_Revision_Report.docx / .md
├── assets/
│   ├── renders/      # raw/ 장면 렌더링, product·closing·screwdriver 핸드 이미지
│   └── original/     # 원본 덱에서 유지한 이미지
└── source/
    ├── deck/         # model.py · build.py · kit.py · slides_main.py · slides_appx.py · to_pdf.py · make_report.py
    └── render3d/     # shot.js · batch.sh · make_assets.py · web/(lib.js · scenes.js)
```
