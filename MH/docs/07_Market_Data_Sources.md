# 07. 시장 Data 및 Source

> MH Robotics · Seed 투자 · TIPS 운영사 검토용 IR · Draft v5 · 2026-10-08  
> Concept 단계: 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 숫자는 FACT / DERIVED / ASSUMPTION / TARGET, 그림은 CONCEPT로 표기.

- 조회일 2026-10-07~08. 공식 통계 · 회사 발표 중 보도 인용이 있어 **외부 제출 전 원문 (국가데이터처 · 국토부 · 중기부 공고 · 회사 IR) 대조 필요**.
- 우선 Source: 국가데이터처 (통계청) · KOSIS · 국토교통부 · 한국부동산원 · 중소벤처기업부 · 기업 공식자료 · 사업보고서 · 학술자료.

## 1. 주택 · Apartment Stock · 노후 · 거래 · 입주

| 항목 | 값 | Tag | 출처 / 산식 |
|---|---|---|---|
| 총주택 (2025.11.1) | 2,018.1만호 | FACT | 국가데이터처 2025 인구주택총조사 (2026.7.28) [S1] |
| 아파트 비중 / 아파트 수 | 65.8% / 약 1,328만호 | FACT | 비중 FACT, 호수는 2,018.1만 × 65.8% (DERIVED) |
| 준공 20년 이상 / 30년 이상 주택 비중 | 56.0% / 30.6% | FACT | 2025 인구주택총조사 [S1] |
| 아파트 수 · 20년 이상 아파트 (2023) | 1,263만호 · 639만호 (50.7%) | FACT | 2023 주택총조사 인용 보도 [S2] |
| 주택 준공 · 인허가 · 착공 (2025) | 34.2만 · 38.0만 · 27.3만호 | FACT | 국토부 2025.12 주택통계 [S3] |
| 아파트 입주 2025 / 2026 예정 | 23만6,263 / 18만3,124가구 | FACT | 부동산114 REPS [S5] |
| 주택 매매거래 (2025) | 72.6만호 (10년 평균 88.5만) | FACT | KB주택시장리뷰 (부동산원 자료) [S6] |
| 무급 가사노동 가치 (2024) | 582.4조원 · 가정관리 459.5조원 (78.9%) · 1인당 132분/일 | FACT | 국가데이터처 가계생산 위성계정 (2026.4) [S40] |
| 연간 주방 교체 교차검증 ① / ② | 29.0만 / 30.3만 | DERIVED | 20년+ 아파트 ÷ 22년 · 매매 × 70% × 40% + 10만 (ASSUMPTION) |
| 연간 주방 교체 (설정값) | 30만 세대/년 | ASSUMPTION | ①·② 범위 → 견적 · Partner Data로 보정 |

## 2. Remodeling · Premium Kitchen · Rental · Care 사례

| 항목 | 값 | Tag | 비고 |
|---|---|---|---|
| 국내 리모델링 시장 (건축물 전체) | 2025 37조원 → 2030 44조원 (전망) | FACT | 한국건설산업연구원 · 주택 주방 단독 아님 [S7] |
| 프리미엄 Kitchen 동향 | 수입 · 고가 맞춤 약 90% · 키친바흐 +17% · 밀레 연계 +173% | FACT | 한샘 발표 인용 보도 [S9] |
| 한샘 리하우스 매출 | 2025 1Q 1,147억원 (−4.3%) | FACT | 분기 실적 [S10] |
| 신축 유상옵션 / 분양가 | 평균 9.7% (분양가상한제 7개 단지) | FACT | 보도 · 옵션 선택 문화 [S11] |
| 코웨이 (렌탈 · 방문관리) | 2025 매출 4조9,636억 · 영업이익 8,787억 · 국내 계정 748만 (2026 1Q) | FACT | 실적 보도 [S12] |
| LG 가전 구독 · Care | 2025 구독 매출 2조원+ · 케어매니저 약 4,000명 · LH 5,400세대 · 재건축 약 7,000세대 선택지 | FACT | 실적 · 보도 [S41] |
| 가전 A/S 출장비 (소비자 부과) | 2.8만원 (삼성 · LG, 2026) | FACT | MH 방문 원가와 다름 [S13] |
| 식기세척기 보급률 | 10%대 초반 (2019~2020 업계 추정, 전체 가구) | TBV | 최신 공식 통계 없음 → 조사 [S30] |
| 주방 단독 교체 가격: 일반 / Premium | 600~1,500만원 / 2,000~4,000만원 | ASSUMPTION | 공식 자료 없음 → 견적 20건 (M6) |

## 3. Robot Arm · Hand · Sensor Benchmark (공개 판매가)

| Benchmark | USD (FACT) | 만원 (환율 1,400원/USD, ASSUMPTION) |
|---|---:|---:|
| UR3e (3kg) | $23k~33k | 3,220~4,620 |
| Doosan E0509 (5kg) | 약 $22k | 3,080 |
| UFACTORY xArm 6 (5kg) | $8,399 | 1,176 |
| FAIRINO FR5 (5kg) | $6,999 | 980 |
| Robotiq 2F-85 (2026 판매가) | 약 $5,825 | 816 |
| Inspire RH56 계열 (Dexterous) | $4,500~9,899 | 630~1,386 |
| Robotiq Fingertip | $175~195 | 24~27 |
| Orbbec Gemini 335 / RealSense D405 | $384~400 / $514 | 54~56 / 72 |

## 4. 경쟁 · 인접 Player (공개 자료)

| Player | 구분 | 공개 내용 | 가격 · 상태 | 접근 | 출처 |
|---|---|---|---|---|---|
| 1X NEO | Humanoid (가정) | 가사 전반 · 원격조작 학습 | $20,000 또는 월 $499 · 2026년 말 첫 배송 목표 (확인 안 됨) | 이동 · 범용 손 · 설치 불필요 | [S19] |
| Figure (Helix 02) | Humanoid | 식세기 인출 → 수납 → 적재 약 4분 연속 시연 (회사 발표) | 가격 · 출시 미공개 | 범용 VLA 모델 학습 | [S45] |
| Sunday Robotics Memo | 이동형 가정 로봇 | 식세기 적재 · 테이블 정리 시연 | Beta 2026년 말 · 양산 $10k 미만 목표 | 집안 이동 · 학습 Data | [S20] |
| LG CLOiD | Humanoid형 홈로봇 | 식세기 비우기 · 빨래 등 시연 (CES 2026) | 2026 실증 · 2028 상용화 목표 · 가격 미공개 | 가전 연계 · 팔 범위 무릎 높이 이상 (보도) | [S21] |
| Samsung | 가전 · 로봇 | Bot Handy (2021 Concept) · 2026 AI 가전 중심 | 출시 확인 안 됨 | 가전 내부 자동화 | [S22] |
| Moley Robotic Kitchen | 로봇 주방 | 천장 Rail 양팔 조리 | £248,000 (Arm 포함, 2021) | 전용 주방 · 조리 중심 | [S23] |
| Posha | 조리대 조리 로봇 | 자동 조리 | $1,750 + 월 $15 | 조리 전용 기기 | [S24] |
| Tesla Optimus | Humanoid | 가정용 목표 | 소비자 목표가 $20k~30k (양산 시) | 범용 | [S25] |
| UR · Doosan + Robotiq | Cobot + Gripper | 부품 (산업용) | UR3e $23k~33k · E0509 약 $22k · 2F-85 약 $5,825 | Integrator 맞춤 | [S15 · S42] |
| 한샘 · 리바트 | 주방가구 | 키친바흐 × 가게나우 빌트인 협업 | 로봇 협업 보도 없음 (2026) | 주방 시공 · 수납 | [S51] |

## 5. 안전 · 인증 · 식품 접촉 기준

| 항목 | 내용 | Tag | 출처 |
|---|---|---|---|
| 협동 운전 기준 | ISO 10218-1/-2:2025 (2025.2 발행): ISO/TS 15066 요구 통합 · 감속 기능 250mm/s 이하 · 손 · 손가락 준정적 접촉력 140N (부속서 M) | FACT | [S28 · S39] |
| 가정용 로봇 안전 | IEC 63682 (구 IEC 60335-2-123) Robots for household and similar use: 2026 CDV 단계 (발행 전) | FACT | [S47] |
| 개인 서비스 로봇 | ISO 13482 개정 FDIS (2025.7) · 국내 ISO 13482 인증 사례 (유진로봇 AMR) | FACT | [S31 · S47] |
| 전기 · EMC | KC 전기용품 안전 · 전자파 적합성 (가정용) — 적용 범위 사전상담 필요 | TBV | - |
| 식품 접촉 | 「기구 및 용기 · 포장의 기준 및 규격」 고무제 규격 (ASSIST · COOK 단계 필수) | FACT | [S48] |
| MH 안전 원칙 | 사람 위로 운반 금지 · Zone 진입 시 감속 · 정지 · 저가반 · 조리기구 구역 No-go · 고장 시 Safe Home Return · 수동 주방으로 사용 가능 | CONCEPT | - |
| 일정 | M4 Risk Assessment · M9 인증기관 사전상담 · M12 안전 기능 시험 · M18 사전시험 (전기 · EMC) · Series A 이후 본인증 | TARGET | - |

## 6. 재무모델에 쓰인 FACT 입력 (17개)

| Key | 항목 | 값 | 단위 | 출처 |
|---|---|---|---|---|
| m_housing_total | 총주택 (2025.11.1 기준) | 20,181 | 천호 | 국가데이터처, 2025 인구주택총조사 등록센서스 결과 (2026.7.28 발표) |
| m_apt_share | 아파트 비중 (총주택 대비) | 0.658 | % | 국가데이터처, 2025 인구주택총조사 |
| m_house_20y_share | 준공 20년 이상 주택 비중 | 0.56 | % | 국가데이터처, 2025 인구주택총조사 |
| m_house_30y_share | 준공 30년 이상 주택 비중 | 0.306 | % | 국가데이터처, 2025 인구주택총조사 |
| m_apt_2023 | 아파트 수 (2023) | 12,630 | 천호 | 통계청, 2023 주택총조사 (보도 인용) |
| m_apt_20y_2023 | 준공 20년 이상 아파트 (2023) | 6,390 | 천호 | 통계청, 2023 주택총조사 (보도 인용) |
| m_txn_2025 | 주택 매매거래 (2025, 전체 주택) | 726 | 천호 | KB주택시장리뷰 2026.2 (한국부동산원 자료) |
| m_completion_2025 | 주택 준공 (2025 연간, 전체 주택) | 342.4 | 천호 | 국토교통부, 2025년 12월 주택통계 |
| m_movein_2025 | 아파트 입주 (2025) | 236.3 | 천호 | 부동산114 REPS |
| m_movein_2026e | 아파트 입주 예정 (2026) | 183.1 | 천호 | 부동산114 REPS (예정 물량) |
| f_helper_rate | 가사서비스 시간당 요금 (플랫폼 4시간 59,900~64,900원) | 1.5 | 만원/h | 가사서비스 플랫폼 공개 요금 (2025, 보도 · 앱 정보) |
| tips | TIPS R&D 정부지원금 (일반 트랙 최대) | 80,000 | 만원 | 중소벤처기업부 공고 제2026-40호 (2026.1.26) 팁스 창업기업 지원계획. 선정 미확정 |
| tips_months | TIPS R&D 기간 (최대) | 24 | 개월 | 공고 제2026-40호 |
| tips_gov_ratio | 정부지원연구개발비 비율 상한 (총 연구개발비 대비) | 0.75 | % | 공고 제2026-40호 (사본 · 운용사 정리 기준: 정부 75% 이내, 기관부담 25% 이상) |
| tips_cash_ratio | 기관부담연구개발비 중 현금 최소 비율 | 0.1 | % | 공고 제2026-40호 (사본 · 운용사 정리 기준) |
| op_invest_min | TIPS 운영사 선투자 요건 (수도권) | 20,000 | 만원 | 2026: 수도권 2억원 이상 · 비수도권 1억원 이상 |
| biz_link | 비R&D 연계 (창업사업화 · 해외마케팅) 각 최대 (선정 뒤 별도 신청, 기본안 미반영) | 15,000 | 만원 | 공고 제2026-40호: 각 10개월 최대 1.5억원, 합산 3억원, 정부 70% 이내 |

## 7. 공식 통계가 없는 항목 → ASSUMPTION + 검증 계획

| 가정 | Tag | 검증 방법 | 시점 |
|---|---|---|---|
| 연 주방 교체 30만 세대 | ASSUMPTION (교차검증 29.0만 · 30.3만) | 견적 20건 · 인테리어 Partner 인터뷰 · 부동산원 아파트 거래 비중 | M6 |
| Premium 비중 10% | ASSUMPTION | 견적 분포 (주방 2,000만원 이상) | M6 |
| Remodeling 적용 가능률 60% | ASSUMPTION | 평면 30개 분석 · 상담 주방 실측 | M6 |
| Premium 재고 10% · 식세기 60% · 호환 40% · 전환 0.5%/년 | ASSUMPTION / TBV | 소비자 조사 n ≥ 300 · 평면 분석 | M18 |
| 신축 Premium 단지 15% · Option 10% · 입주 Attach 25% | ASSUMPTION | 건설사 · 분양 옵션 사례 조사 | M18 |
| Care 가입 70% · 소모품 구매 70% | ASSUMPTION | 실증 3세대 · Pilot 가입 · 교체 Data | M24 |

- 식기세척기 보급률 · 연간 주방 교체 세대 수 · Premium Kitchen 시장 규모는 공식 통계를 찾지 못함 → 가정으로 두고 견적 20건 · 평면 30개 · 소비자 조사 n ≥ 300으로 대체.

## 8. 전체 출처 (52건, sources.json)

| ID | 항목 | 값 | 기준 | 출처 | 사용처 |
|---|---|---|---|---|---|
| S1 | 총주택 / 아파트 비중 / 준공 20년·30년 이상 비중 / 미거주 주택 | 2,018.1만호 / 65.8% / 56.0%·30.6% / 172.2만호 | 2025.11.1 기준 | 국가데이터처, 2025 인구주택총조사 결과 (2026.7.28 발표) — 보도: https://www.newsis.com/view/NISX20260728_0003726109 , https://www.fnnews.com/news/202607281048203456 | 05, 17, A2 |
| S2 | 아파트 수 / 준공 20년 이상 아파트 (2023) | 1,263만호 / 639만호 (50.7%) | 2023 주택총조사 | 통계청 주택총조사 인용 보도: https://www.smarttoday.co.kr/ko-kr/articles/49322 | 17, A2 |
| S3 | 2025 주택 준공 / 인허가 / 착공 / 공동주택 분양 | 34만2,399호 (−17.8%) / 37만9,834호 / 27만2,685호 (−10.1%) / 19만8,373호 (−14.1%) | 2025 연간 | 국토교통부, '25년 12월 주택통계 (2026.1.30): https://www.korea.kr/briefing/pressReleaseView.do?newsId=156742136 , https://www.m-economynews.com/news/article.html?no=64226 | 05, A2 |
| S4 | 아파트 인허가 (2025) | 34만6,773가구 (2024: 39만7,904) | 2025 연간 | 국토교통부 주택통계 인용 보도: https://www.newsis.com/view/NISX20260129_0003495426 | A2 |
| S5 | 아파트 입주 물량 | 2025 23만6,263가구 / 2026 예정 18만3,124가구 | 부동산114 REPS | https://v.daum.net/v/GCidIvCEQs | 05, 17, A2 |
| S6 | 주택 매매거래 (2025) | 72.6만호 (+13%, 10년 평균 88.5만호) | 2025 연간, 한국부동산원 자료 | KB주택시장리뷰 2026년 2월호: https://kbthink.com/realestate/insights/research/260213-3.html | 17, A2 |
| S7 | 국내 리모델링 시장 전망 (건축물 전체, 비주거 포함) | 2025년 37조원 → 2030년 44조원 (리모델링 23.3조 + 유지보수 13.8조, 2025) | 한국건설산업연구원 전망치 | https://m.ekn.kr/view.php?key=523568 | A3 |
| S8 | 한샘 리하우스 스타일패키지 (전체 리모델링) | 30평대 평당 100만원대 → 약 3,000만원 | 2019 보도 (가격 시점 오래됨) | https://www.dailian.co.kr/news/view/1008108/ | 14, A3 |
| S9 | 프리미엄 Kitchen 동향 (한샘 키친바흐·빌트인 가전 연계) | 국내 프리미엄 키친 시장 약 90%가 수입·고가 맞춤 / 키친바흐 매출 +17% (2025.6 기준) / 밀레 연계 부엌 매출 +173% (2024 대비) | 회사 발표 인용 보도 | https://www.heraldk.com/article/2025072318143590645 , https://www.heraldk.com/article/2026062223520679105 | 17, A3 |
| S10 | 한샘 리하우스 부문 매출 | 2025 1Q 1,147억원 (−4.3%) | 분기 실적 | https://newstomato.com/ReadNews.aspx?no=1284742 | A3 |
| S11 | 신축 유상옵션 비용 비중 | 분양가상한제 단지 7곳 평균 분양가 대비 9.7% | 수도권 분양 단지 보도 | https://www.etoday.co.kr/news/view/2392578 | 12, 13, A3 |
| S12 | 코웨이 실적 · 렌탈 계정 (가전 Rental · 방문관리 사례) | 2024 매출 4조3,101억원 · 국내 계정 671만 / 2025 매출 4조9,636억원 · 영업이익 8,787억원 / 2026 1Q 국내 계정 748만 (전체 1,173만) | 회사 실적 발표 인용 보도 | https://news.bizwatch.co.kr/article/consumer/2025/02/14/0029 , https://dealsite.co.kr/articles/156536 , https://www.heraldk.com/article/2026050717254859414 | A12, A19 |
| S13 | 가전 A/S 출장비 (소비자 부과분) | 삼성전자서비스 평절기 기본 2.8만원 (2026.1.8~) / LG전자 평절기 평일 주간 2.8만원 | 2026 | https://biz.sbs.co.kr/amp/article/20000282569 , https://biz.sbs.co.kr/amp/article/20000310315 | A13 |
| S14 | 가사서비스 요금 | 플랫폼 4시간 59,900~64,900원 (약 1.5~1.6만원/h) / 2026 최저임금 10,320원 | 공개 요금·고시 | https://apps.apple.com/pl/app/id997730211 , https://www.activpayroll.com/news-articles/south-korea-announces-2026-minimum-wage-increase | 14 |
| S15 | 협동로봇 가격 (Arm + Controller) | UR3e $23k~33k (공식 정가 미공개, 유통가) / Doosan E0509 약 $22k / UFACTORY xArm 6 $8,399 / FAIRINO FR5 $6,999 / UFACTORY Lite 6 Kit $4,482 (가반 0.6kg) | 유통가·공개가 (2025~2026) | https://standardbots.com/blog/universal-robot-price , https://robotomated.com/explore/manufacturing/doosan-e-series-e0509 , https://www.robotshop.com/products/xarm-6-dof-robotic-arm , https://top3dshop.com/product/fairino-fr5-robotic-arm , https://www.robotshop.com/products/ufactory-6-axis-robot-arm-lite-6-kit | A4 |
| S16 | Gripper / Fingertip / Food-grade Suction Cup | Robotiq 2F-85 $4,999~ / OnRobot RG2 약 $3,200 / Robotiq Fingertip $175~195 / Piab Food-grade Silicone Cup £7~20 (FDA 21 CFR 177.2600) / 2026 판매가 2F-85 약 $5,825 (미국 리셀러, Coupling · Fingertip 포함) | 공개가 | https://qviro.com/product/robotiq/2f-85-robotiq/ , https://www.roboticscenter.ai/en/hardware/robotiq-2f-85 , https://automationdistribution.com/brands/Robotiq.html , https://uk.rubix.com/en/flat-suction-cups-f-silicone/p-G2010133211 , https://www.roboticscenter.ai/ko/blog/robotiq-gripper-guide | A4, A13 |
| S17 | Depth Camera | Intel RealSense D405 $514 / D435 $538 / Orbbec Gemini 335 $384~400 | 공개가 | https://openelab.com/collections/robotic-camera , https://knoxlabs.com/products/orbbec-gemini-335-depth-camera | A4 |
| S18 | Linear Module (소형) | HIWIN KK 계열 $73~245 (소형 모듈, Robot 7축 Rail과 다름) | 유통가 | https://qviro.com/product/hiwin/electric-linear-axis-kk-series | A4 |
| S19 | 1X NEO (가정용 Humanoid) | $20,000 구매 또는 월 $499 구독. 첫 가정 배송 목표 2026년 말 (2026.10 기준 고객 배송 완료 확인 안 됨) | 회사 발표 인용 보도 | https://www.fastcompany.com/91428202/1x-technologies-home-robot-neo , https://heise.de/-11287205 | 14, 20, A9 |
| S20 | Sunday Robotics Memo | 식세기 적재 · 테이블 정리 시연 (회사 발표, 낯선 Airbnb 6곳 시연 보도) · Beta 2026년 말 (회사 웹사이트) · 양산 시 $10k 미만 목표 | 보도 | https://euronews.com/next/2025/11/25/meet-memo-a-home-robot-that-can-grab-wine-glasses-and-load-the-dishwasher , https://sacra.com/c/sunday/ , https://sunday.ai/ , https://www.eweek.com/news/sunday-memo-home-robot/ | 20, A9 |
| S21 | LG CLOiD | CES 2026 공개 · 식세기 비우기 등 시연 · 2026 현장 실증 → 가정용 상용화 2028 목표 (회사 언급 보도) · 팔 작업 범위 무릎 높이 이상 (보도) · 판매가 미공개 | CES 2026 | https://www.dezeen.com/2026/01/06/lg-ai-powered-robot-ces-2026/ , https://v.daum.net/v/20260429185809070 , https://www.nocutnews.co.kr/news/6453121 | 20, A9 |
| S22 | Samsung (가정용 로봇 · 주방) | Bot Handy: CES 2021 공개 Concept (식기 이동 시연), 출시 일정 미공개 / CES · IFA 2026 주방 전시는 AI 가전 중심, 식기 로봇 출시 확인 안 됨 | 보도 | https://www.sammobile.com/news/meet-samsung-new-ai-powered-household-robots-ces-2021/ , https://www.tomsguide.com/home/home-appliances/2026-could-be-a-tipping-point-for-the-smart-kitchen-according-to-samsung | A9 |
| S23 | Moley Robotic Kitchen | Arm 포함 £248,000 / Arm 제외 £128,000~140,000 (천장 Rail 양팔) | 2021 판매 개시 보도 | https://thespoon.tech/moleys-robotic-kitchen-goes-on-sale/ | 20, A9 |
| S24 | Posha (Countertop Cooking Robot) | $1,750 (선주문 $1,500) + 월 $15 | 2025 | https://techcrunch.com/2025/05/06/meet-posha-a-countertop-robot-that-cooks-your-meals-for-you | A9 |
| S25 | Tesla Optimus / Figure 03 | Optimus 소비자 목표가 $20k~30k (양산 시, 2027 전후) / Figure 03 가사 시연, 가격 미공개 | 보도 | https://www.notebookcheck.net/Optimus-as-a-household-helper-Elon-Musk-plans-to-bring-Tesla-robots-into-private-homes-starting-in-2027.1212513.0.html , https://getcoai.com/news/stay-at-home-bots-figure-03-humanoid-robot-can-fold-laundry-wash-dishes | A9 |
| S26 | IFR World Robotics 2025 — Service Robots | 소비자용 서비스로봇 약 2,000만대 (2024, +11%, 대부분 청소·잔디) / 전문 서비스로봇 약 20만대 (+9%) | 2024 판매 | https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom | A19 |
| S27 | Robot Density (IFR World Robotics 2024) | 한국 제조업 근로자 1만명당 1,012대 (세계 1위, 2023) | IFR | https://www.koreaherald.com/article/10011543 | A19 |
| S28 | ISO 10218-1/-2:2025 | 2025.2 발행. ISO/TS 15066 (PFL·SSM) 요구사항을 본문에 통합, 기능안전·Cybersecurity 강화 | 표준 | https://www.sick.com/kr/ko/w/blog-robotic-norm-iso10218 , https://www.evsint.com/industrial-robot-safety-standards-iso-10218-ce-marking-2026/ | A7 |
| S29 | TIPS 2026 | 일반 TIPS R&D 최대 8억원·24개월 / 딥테크 TIPS 최대 15억원·36개월 (요건 별도) | 중소벤처기업부 2026 공고 | https://www.unicornfactory.co.kr/article/2026012511000214016 , https://www.venturesquare.net/announcement/1035119 | 23, A16 |
| S30 | 식기세척기 보급률 | 2019~2020 업계 추정 10%대 초반 (최신 공식 통계 확인 안 됨 → TO BE VALIDATED) | 업계 추정 보도 | https://www.etoday.co.kr/news/view/1789343 | A3 |
| S31 | ISO 13482 (Personal Care Robot) 국내 인증 사례 | 유진로봇 GoCart, 국내 첫 ISO 13482 인증 AMR | 회사 발표 | https://yujinrobot.com/blog/yujin-robots-gocart-becomes-koreas-first-iso-13482-safety-certified-autonomous-mobile-robot | A7 |
| S32 | 가정용 로봇 인증 동향 | 반려로봇 KS 인증 도입 (2026.4, 정부) | 보도 | https://news.mtn.co.kr/news-detail/2026042014042480949 | A7 |
| S33 | 2026 TIPS 일반트랙 규정 (R&D) | 정부지원 최대 8억원 · 24개월 · 정부 75% 이내 / 기관부담 25% 이상 (그중 현금 10% 이상) · 운영사 투자 수도권 2억원 이상 · 비수도권 1억원 이상 · 대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 30% 이하 · 정부지원 5억원당 청년 1명 신규 채용 · 업력 7년 이내 (신산업 10년) · 분기별 접수 연 3회 (IRIS) | 중소벤처기업부 공고 제2026-40호 (2026.1.26) — 공고 사본 · 운용사 정리 · 집계 사이트 기준 (원문 대조 필요) | https://www.kakao.vc/blog/2026-tips-what-changed , https://app.rndcircle.io/gov-grant/de57c07b-23b7-4eca-a812-90fb66a88b56 , https://grant-documents.thevc.kr/288079_(%EC%B5%9C%EC%A2%85)_2026%EB%85%84_%ED%8C%81%EC%8A%A4_%EC%B0%BD%EC%97%85%EA%B8%B0%EC%97%85_%EC%A7%80%EC%9B%90%EA%B3%84%ED%9A%8D_%EA%B3%B5%EA%B3%A0.pdf | 본문 2 · 14 · 18 · 19, D11 |
| S34 | 2026 TIPS 비R&D 연계 (창업사업화 · 해외마케팅) | 각 10개월 최대 1.5억원, 합산 3억원 · 정부 70% 이내 (기업 30% 이상: 현금 10% 이상 · 현물 20% 이하) | 공고 제2026-40호 사본 · 집계 사이트 | https://app.rndcircle.io/gov-grant/4a69b298-641c-445a-9dac-66cf5dd0ee72 | 본문 19, D11 |
| S35 | TIPS 일반트랙 선정평가 배점 (비공식) | 기술성 40 · 사업성 40 (글로벌 성장 가능성 포함) · 사업수행 역량 20 (창업기업 전문성 · 운영사 지원계획) / 2026 가점 최대 5점 | 특허사무소 · 운용사 블로그 정리 (적용 연도 · 원문 미확인) | https://www.pinepat.com/ko/insights/columns/tips-application-guide , https://www.kakao.vc/blog/2026-tips-what-changed | 덱 구성 점검 |
| S36 | 식기세척기 적재 연구 (Voysey · Thuruthel · Iida) | 트레이 25개 실험에서 식기 58.7% 정리 (one-shot, preprint 기준) · 비교 대회 시스템 49~79% | Engineering Reports 2021 (DOI 10.1002/eng2.12321), 실험실 주방 | https://onlinelibrary.wiley.com/doi/10.1002/eng2.12321 , https://www.researchgate.net/publication/342426874 | 본문 15 (세계 최고 수준) |
| S37 | Dobb-E (가정 조작 학습) | 뉴욕 10가구 · 단순 가사 과제 109종 · 과제당 10회 평균 성공률 81% | Shafiullah et al., arXiv 2311.16098 (2023) | https://arxiv.org/abs/2311.16098 | 본문 15 (세계 최고 수준) |
| S38 | TidyBot · π0.5 (가정 정리) | TidyBot 실물 정리 85% (배치 기준, 2023) · π0.5 처음 보는 가정 주방 · 침실 정리, 부분 점수 기준 자체 보고 (2025) | arXiv 2305.05658 · arXiv 2504.16054 | https://arxiv.org/abs/2305.05658 , https://arxiv.org/abs/2504.16054 | 본문 15 (참고) |
| S39 | 협동로봇 안전 기준 값 | ISO 10218-2:2025 감속 기능 접근 가능한 가동부 250mm/s 이하 · 부속서 M (구 ISO/TS 15066) 손 · 손가락 준정적 접촉력 140N | 표준 원문 미확인 — 제조사 · 인증 컨설팅 · 연구 정리 | https://blog.robotiq.com/compliance-of-the-hand-e-gripper-with-iso-10218-22025 , https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 본문 15 · 18 |
| S40 | 무급 가사노동 가치 (2024 가계생산 위성계정) | 582.4조원 (GDP 약 22%) · 그중 가정관리 (음식 준비 · 청소 등) 459.5조원 (78.9%) · 1인당 하루 가사노동 132분 (2019 137분) | 국가데이터처 2026.4 발표 (보도 인용) | https://biz.sbs.co.kr/amp/article/20000307502 , https://magazine.hankyung.com/business/article/202604295997b | 본문 02 |
| S41 | 가전 구독 · Care 사례 (LG전자) | 2025 구독 매출 2조원 이상 (4Q 실적 발표) · 케어매니저 약 4,000명 · LH 공공주택 5,400여 세대 구독형 가전 + 6년 정기관리 · 압구정 재건축 빌트인 가전 + Care 구독 선택지 (조합원 약 7,000세대) | 회사 실적 · 발표 인용 보도 (2026) | https://files-scs.pstatic.net/2026/01/30/SgKPKOCyxu/2025.4Q%20Earnings%20Release%20of%20LGE_KR.pdf , https://www.heraldk.com/article/2026053118272769372 , https://www.smarttoday.co.kr/ko-kr/articles/73353 | 본문 11 · 13 |
| S42 | Robot Hand Benchmark (상용) | Robotiq 2F-85 약 $5,825 (2026 판매가) · Inspire RH56 계열 $4,500~9,899 (판매가) · Inspire RH56E2 엄지 파지력 30N | 판매처 공개가 (2026) | https://www.roboticscenter.ai/ko/blog/robotiq-gripper-guide , https://www.knoxlabs.com/collections/robotic-hands | 본문 06 · 부록 |
| S43 | 식품 직접 접촉용 Finger Gripper (상용) | Schmalz OFG: 실리콘 파지부 · IP68 · 최대 80°C · 마모부품 Kit 별도 | 제조사 제품 페이지 | https://www.schmalz.com/en/vacuum-technology-for-automation/vacuum-components/area-gripping-systems-and-end-effectors/finger-grippers/finger-grippers-ofg-312389/10.01.51.00001/ | 본문 06 · 15 · 부록 (선행기술) |
| S44 | 미끄럼 감지 연구 (촉각 센서) | GelSight Mini 기반 실시간 미끄럼 감지, 일상 물체 10종 평균 정확도 99% (실험실) · 센서 가격 비공개 (견적) | Hu et al., arXiv 2303.00935 | https://arxiv.org/abs/2303.00935 , https://www.roboticscenter.ai/guides/best-tactile-sensors-robot-learning/ | 부록 KPI |
| S45 | Figure Helix 식기세척기 시연 | 2025.9 식세기 적재 시연 · 2026.1 Helix 02 식세기 인출 → 수납 → 적재 약 4분 연속 (회사 발표, 독립 검증 없음) | 보도 | https://futurism.com/future-society/figure-robot-loading-dishwasher , https://interestingengineering.com/innovation/humanoid-robot-tackles-dishwasher-ai | 본문 15 |
| S46 | Physical Intelligence openpi (공개 모델) | π0 · π0-FAST · π0.5 코드 · 가중치 공개 (2025.2~), 테이블 정리 등 Fine-tune 예시 | 회사 공개 Repository | https://github.com/Physical-Intelligence/openpi , https://pi.website/blog/openpi | 본문 15 |
| S47 | 가정용 로봇 안전 표준 동향 | IEC 63682 (구 IEC 60335-2-123) Robots for household and similar use — Safety: 2026 CDV 단계 (독일 의견수렴 2026.5.15~7.15) · ISO 13482 개정 FDIS (2025.7) | 표준기관 프로젝트 페이지 (발행 전) | https://www.vde-verlag.de/standards/1701976/e-din-iec-63682-vde-0700-123-2026-06.html , https://knowledge.bsigroup.com/products/bs-en-iec-63682-robots-for-household-and-similar-use-safety-particular-requirements , https://din.de/en/getting-involved/standards-committees/nam/projects/wdc-proj:din21:348357354 | 본문 08 · 16 · 부록 |
| S48 | 식품 접촉 부품 규정 | 식품위생법상 "기구" (식품에 직접 닿는 기계 · 기구) · 「기구 및 용기 · 포장의 기준 및 규격」 (식약처 고시) 고무제 (실리콘) 재질 · 용출 규격 | 법령 · 고시 | https://www.mfds.go.kr/brd/m_207/view.do?seq=14529 , https://food.chemlinked.com/database/view/6844 | 본문 06 · 부록 |
| S49 | 선행기술 — 식기 조작 로봇 | US 11,731,282 (Dishcare, 쌓인 식기 사이에 넣는 Tapered Finger · 수납 Module 통합) · US 10,507,584 (Dishcraft, 식기 인식 · 랙 적재) · WO 2018/031489 (Dishcraft, 자성 식기 Gripper) · US 2023/0165427 (가정용 식세기 맞춤 Routine) | 특허 공보 검색 결과 (청구항 · 권리상태 미확인) | https://patents.justia.com/patent/11731282 , https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10507584 , https://brevets-patents.ic.gc.ca/opic-cipo/cpd/eng/patent/3032941/summary.html , https://patents.justia.com/patent/20230165427 | 본문 15 · 부록 IP |
| S50 | 선행기술 — 주방 로봇팔 · Rail · 수납장 · Skill Library | US 7,751,938 외 3건 (주방 벽 Rail 이동 로봇팔 제어) · EP 3,881,977 (가전 · 주변 고정 모듈형 Arm, 교체형 End piece) · US 12,275,130 (수납장 내 Gantry 조리 로봇) · US 10,518,409 B2 (Minimanipulation Library · Instrumented Environment) | 특허 공보 검색 결과 (청구항 · 권리상태 미확인) | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7751938 , https://data.epo.org/publication-server/rest/v1.2/patents/EP3881977NWA1/document.html , https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12275130 , https://patents.google.com/patent/US10518409 | 본문 15 · 부록 IP |
| S51 | 주방가구사 동향 (2026) | 한샘 키친바흐 × 가게나우 빌트인장 협업 · 코리아빌드 2026 신제품 (로봇 제품 없음) — 가구사의 가정용 주방 로봇 협업 보도 확인 안 됨 | 보도 (2026.6~8) | https://www.hankyung.com/amp/202606170891P | 본문 15 |
| S52 | 2026 TIPS 접수 방식 | 공고 접수 기간 2026.1.26~12.31 · 일반트랙 분기 단위 평가 (운용사 해설) — 남은 차수 일정은 운영사 확인 | 공고 요약 · 운용사 해설 | https://www.venturesquare.net/announcement/1035119 , https://zuzu.network/resource/blog/2026-different-tips-required/ | 본문 16 |
