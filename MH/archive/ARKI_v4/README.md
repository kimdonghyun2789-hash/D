# Archive — ARKI Robotics v4 (2026.10)

- MH Robotics 최종본으로 전면 개편 전 판
- 내용 삭제 없이 그대로 보관 (참고용 · 현재 빌드 미사용)

| 파일 | 내용 |
|---|---|
| `ARKI_Robotics_TIPS_IR_Deck.pptx` · `_Main.pdf` · `_preview.pdf` | v4 IR 덱 (본문 19쪽 + 부록) |
| `ARKI_Robotics_Financial_Model.xlsx` | v4 수식 재무모델 |
| `docs/00~11` | v4 문서 (장별 문구 · 시장 Data · Tag 구분표 · 재무 · TIPS 예산 · 특허 · 예상질문 · Investment Memo (WATCH) · Evidence 공백) |
| `gen_docs_arki_v4.py` | v4 문서 생성기 |
| `source/` | v4 덱 생성 코드 (`slides_main.py` · `slides_appx.py` · `slides_apx2.py` · `slides_legacy.py` · `drawings.py` · `viz.py` · `qa_montage.py`) · `_facts_sheet.md` |

- v4 코드 = `MH/source`의 `kit.py` · `common.py` · `model.py` 의존 → 이후 모델 변경 (MH)으로 재실행 불가
- v4 확정본 = 결과물 (pptx · pdf · xlsx · docs)

## MH Robotics 최종본에서 달라진 점

- 회사 정의: "로봇 주방 / 식기 정리" → "Kitchen Manipulation Robotics System (Adaptive Hand · Skill · Calibration · Environment Integration)"
- 설치 경로 3종 (Retrofit · Remodeling · New-build) · 3층 BM (INSTALL · OPERATE · EXPAND)
- Seed (Commercial Validation) · TIPS (Technology De-risking) 역할 분리 · Bottom-up Seed 범위
- 대표 평면 (구축 2Bay A) · Robot Home 3D 렌더 = MH 부록 B3 · B4에 그대로 사용
