# ARKI Robotics — Seed IR Package (Draft v3, 2026.10)

**설거지 정리를 맡는 로봇 주방 · 첫 시장 구축 아파트 주방 리모델링 → 신축 옵션**

> Concept 단계 자료. 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음. 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET (+ CONCEPT · TO BE VALIDATED · FUTURE)로 구분. Founder 정보는 `[Founder 정보 필요]`로 비워 둠. 평면은 사용자 제공 도면이며 단지명은 표기하지 않음.

## 산출물

| 파일 | 내용 |
|---|---|
| `ARKI_Robotics_Seed_IR_Deck.pptx` | IR 덱 (본문 15쪽 + 부록 A~F), 16:9, 발표자 노트 포함 |
| `ARKI_Robotics_Seed_IR_Deck_Main15.pdf` | 본문 15쪽만 (공유용) |
| `ARKI_Robotics_Seed_IR_Deck_preview.pdf` | 전체 검토용 PDF |
| `ARKI_Robotics_Financial_Model.xlsx` | 수식 기반 5개년 모델 (Inputs → 3개 시나리오 · Household · Unit_Economics · Market · Sensitivity · Use_of_Funds · Sources) |
| `docs/00~11` | 장별 문구 · 그림 · 발표 메모, 시장 데이터 · 출처, 숫자 태그 구분표, 재무 · 세대 경제성, 자금 용도, 특허 후보, 예상 질문, 투자 메모 (WATCH), Evidence 공백 |
| `render3d/` | 3D 그림 생성기 (three.js + Playwright) · 충돌검사 · 보관/전개 경로 계획 · 평면 JSON |
| `assets/renders/` | 덱에 들어간 3D 그림 PNG + 앵커 · 충돌검사 결과 JSON |

## 본문 구성 (15쪽)

| 쪽 | 메시지 |
|---|---|
| 01 | 설거지 정리를 맡는 로봇 주방 |
| 02 | 식사 후 정리는 아직 사람이 합니다 |
| 03 | 로봇을 들이는 대신, 로봇 자리를 주방에 만듭니다 |
| 04 | 식사 후 정리를 다섯 단계로 끝냅니다 |
| 05 | 평소엔 보관함에 숨고, 낮은 곳은 랙을 당겨 위에서 넣습니다 |
| 06 | 받은 평면 그대로 3D로 옮겨, 주방 한 벽에 넣었습니다 |
| 07 | 평면이 달라도 같은 한 줄 모듈을 씁니다 |
| 08 | 첫 시장은 주방을 새로 하는 구축 아파트입니다 |
| 09 | 설치할 때 한 번 크게, 쓰는 동안 매년 받습니다 |
| 10 | 직접 팔며 배우고, 파트너로 늘리고, 신축 옵션으로 키웁니다 |
| 11 | 가전은 기기 안만, 범용 로봇은 집마다 새로 배워야 합니다 |
| 12 | 5년차 매출 77.6억원, 손익분기는 6년차 이후입니다 |
| 13 | 24개월 동안 다섯 번 점검하고, 기준에 못 미치면 멈춥니다 |
| 14 | Seed 판단의 첫 질문은 팀이고, 그 칸은 아직 비어 있습니다 |
| 15 | Seed 20억원으로 24개월간 사업 가설을 검증합니다 |

부록: A 투자 판단 요약 · B 제품 · 표준화 (B5 받은 평면 5종 상태, B6 구축 2Bay A 원래 평면 → ARKI, B7 구축 2Bay B 3D, B8~B10 이전 콘셉트 모델) · C 시장 · 사업화 · D 경제성 · 재무 · E 진입장벽 · 리스크 · 예상 질문 · F 숫자 표기 원칙 · 출처. v1 본문 · 부록은 삭제 없이 부록으로 옮김.

## 로봇 주방 설계 (3D 모델 기준, CONCEPT)

- 한 줄 모듈: 로봇 보관함 45 · 내려놓는 곳 70~80 · 싱크 80 · 로봇용 서랍 60 · 식기세척기 60cm. 조리기구는 이 줄에 두지 않음 (로봇 금지 구역).
- 레일: 상부장 바로 아래 (높이 139cm). 로봇은 레일에 매달려 이동, 바닥을 쓰지 않음.
- 보관함: 조리대 위 끝 (W45 × D62 × H137cm), 앞판 + 15cm 꺾인 판으로 된 여닫이 문 1짝 (왼쪽 경첩). 오른쪽 아래(상부장 하단선 아래)는 레일 통로. 평소 로봇은 위로 접혀 안에 있음.
- 나오는 순서: 문 열림 → 팔이 문 앞쪽으로 펴지며 레일 아래로 → 레일 방향 이동 자세 → 통로로 이동. 경로는 RRT-Connect로 찾고 짧게 다듬음. 펼칠 때 팔이 조리대 앞으로 최대 약 26cm 나옴.
- 낮은 곳: 일반 빌트인 식기세척기 하단 랙을 44cm 당겨 위에서 넣음 (집게 끝 최저 약 37cm). 서랍도 열어서 위에서 넣음.
- 충돌검사: 로봇 링크 = 캡슐, 가구 = 상자. 모든 작업 자세 · 보관 · 전개 경로 (관절 보간 0.015rad) · 레일 이동 (1cm 간격) · 레일/캐리지 · 로봇 자기충돌 · 조리대 위 식기까지 검사, 관통 0cm. 결과는 `assets/renders/*.json`의 `ik`.

## 실제 평면 (사용자 제공 5종)

| 평면 | 상태 |
|---|---|
| 구축 2Bay A (12,390 × 11,670, 코어 포함) | 3D 완료 · 원본과 겹쳐 확인 · ARKI 한 줄 3,150mm 배치 · 문 90° 조건 충돌검사 0cm (본문 6쪽 · 부록 B6) |
| 구축 2Bay B (10,940 × 8,500) | 3D 완료 · 원본과 겹쳐 확인 · ARKI 배치 검토 중 (부록 B7) |
| 신축 2 · 3 · 4Bay | 디지털화 진행 중 (부록 B5) |

## 핵심 결과 (기본 시나리오, 전부 DERIVED from ASSUMPTION)

- 세대 경제성 (구축 · 구매 · 5년): 매출 2,418만원, 기여이익 458만원 (Y3 원가) → 813만원 (Y5 원가). 설치 시점 매출 84%.
- 가격 위험: 가치 기준 월 약 11~24만원 < 렌탈 원가 하한 월 24~31만원 → 지불의사 검증이 Seed 1순위.
- 5개년: Y5 매출 77.6억원 · 매출총이익률 36% · 영업이익 −36.4억원 · 5년 누적 현금 최저 약 −128억원 · 손익분기 연 약 1,340세대 (6년차 이후).
- Seed 20억원 / 24개월 → 재산정 25.8억원 (부족 5.8억원, 20억원 단독 약 19개월) → TIPS R&D(최대 8억원) 연계 또는 25억원 / M18 브리지.
- Seed 판단: **WATCH** — 조건: 창업팀 역량 · 목업 검증 · 지불의사 신호 · 평면 표준안 · 실제 파트너 실증 합의.

## 다시 만들기

```bash
pip install python-pptx openpyxl pillow lxml pypdf      # LibreOffice: PDF · xlsx 재계산
python3 ARKI/source/model.py          # 가정 · 계산 → model.json
python3 ARKI/source/xlsx_model.py     # 수식 기반 xlsx
python3 ARKI/source/check_xlsx.py     # xlsx 값 ↔ model.py 교차검증
cd ARKI/render3d && npm install three@0.170.0 && bash render_v2.sh && bash render_plans.sh   # 3D 그림 + 충돌검사 (Playwright Chromium)
node shot.js stowsearch out/stow.png 64 64 "railz=30"    # 보관/전개 경로 다시 계획 → 결과를 web/stow_poses.json으로
python3 ARKI/source/build.py --pdf    # 덱 + 본문 PDF + 전체 PDF (--png: 미리보기)
python3 ARKI/source/gen_docs.py       # docs/*.md + 이 README
```

- 단일 원천: `source/model.py` 입력 (태그 · 출처 포함)이 덱 · xlsx · 문서의 숫자를 만듦. 덱 문구 기본값은 `slides_main.py`, 검토를 거친 문구는 `source/_copy_v3.json`.
- 평면 JSON: `render3d/plans/*.json` (mm, 치수선 기준). 원본 겹침 확인 스크립트는 작업 메모 참고.

## 외부 제출 전 입력 · 확인

| 항목 | 위치 |
|---|---|
| Founder 정보 7항목 · 회사 정보 · 연락처 | 본문 1 · 14 · 15쪽 |
| 투자 조건 (형태 · 기업가치 · 지분 · TIPS 운영사) | 본문 15쪽 · 부록 D11 |
| 신축 평면 3종 디지털화 · ARKI 배치 | 부록 B5 |
| 공식 통계 원문 대조 | 부록 C1 · F2 |
