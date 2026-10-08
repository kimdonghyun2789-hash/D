# Archive — ARKI Robotics v4 (2026.10)

MH Robotics Draft v5로 전면 개편하기 전의 판. 내용은 삭제하지 않고 그대로 보관한다 (참고용, 현재 빌드에서 사용하지 않음).

| 파일 | 내용 |
|---|---|
| `ARKI_Robotics_TIPS_IR_Deck.pptx` · `_Main.pdf` · `_preview.pdf` | v4 IR 덱 (본문 19쪽 + 부록) |
| `ARKI_Robotics_Financial_Model.xlsx` | v4 수식 재무모델 |
| `docs/00~11` | v4 문서 (장별 문구 · 시장 Data · Tag 구분표 · 재무 · TIPS 예산 · 특허 · 예상질문 · Investment Memo (WATCH) · Evidence 공백) |
| `gen_docs_arki_v4.py` | v4 문서 생성기 |
| `source/` | v4 덱 생성 코드 (`slides_main.py` · `slides_appx.py` · `slides_apx2.py` · `slides_legacy.py` · `drawings.py` · `viz.py` · `qa_montage.py`) · `_facts_sheet.md` |

v4 코드는 `MH/source`의 `kit.py` · `common.py` · `model.py`에 의존하며, 이후 모델이 MH v5로 바뀌어 그대로 다시 실행되지 않는다. 결과물 (pptx · pdf · xlsx · docs)이 v4의 확정본이다.

v5 (MH Robotics)에서 달라진 점: 회사 정의를 "로봇 주방 / 식기 정리"에서 "Kitchen Manipulation Robotics System (Adaptive Hand · Skill · Calibration · Environment Integration)"으로 바꾸고, 설치 경로 3종 (Retrofit · Remodeling · New-build), 3층 BM (INSTALL · OPERATE · EXPAND), Seed (Commercial Validation)와 TIPS (Technology De-risking)의 역할 분리, Bottom-up Seed 범위를 추가했다. 대표 평면 (구축 2Bay A)과 Robot Home 3D 렌더는 v5 부록 B3 · B4에 그대로 쓰인다.
