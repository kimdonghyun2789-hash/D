# ARKI facts sheet (single source = ARKI/source/model.py; units 만원 unless noted). Tag in [ ].
## 회사·상태
- 회사: ARKI Robotics (아키로보틱스, 가칭). Concept 단계. Prototype·고객·계약·LOI·Partner·매출 모두 없음 [FACT]. Founder 정보 미제공 → [Founder 정보 필요] 그대로 표기, 절대 창작 금지.
- 제품: 로봇이 일할 수 있게 설계한 주방(Robot-ready Kitchen: 레일·로봇 차고·상향 식세기·로봇용 수납·전원/통신) + 로봇(6축 협동로봇 팔 + 그리퍼 + 비전). 첫 기능 = 식사 후 설거지 정리(식기 인식→집기→식세기 넣기→꺼내기→수납). 조리는 범위 밖.
- 수납/전개/낮은 위치 접근 방식은 설계 확정 중 (별도 spec으로 제공 예정) → 문구에는 [MECH] 자리표시 허용.
## 시장 (구축 리모델링 = 첫 시장)
- 총주택 2,018만호, 아파트 비중 65.8% → 아파트 약 1,328만호 [FACT/DERIVED] (국가데이터처 2025 인구주택총조사, 2026.7 발표)
- 준공 20년 이상 주택 56.0%, 30년 이상 30.6% [FACT]
- 연간 아파트 주방 교체 약 30만 세대 [ASSUMPTION] (두 방식 교차추정 29.0만·30.3만)
- 그중 Premium(주방 예산 2,000만원+) 10% → 3만 세대 [ASSUMPTION]; 로봇 레디 적용 가능 60% → 연 1.8만 세대 [ASSUMPTION]
- 구축 SAM 약 3,212억원/년 (세대당 1,784만원) [DERIVED]; 신축 SAM 약 184억원/년 [DERIVED]; 합계 약 3,396억원/년
- 신축: 연 아파트 입주 약 20만 세대 (2025 23.6만 실적, 2026 18.3만 예정) [FACT/DERIVED]; Premium 단지 15% × Option 선택 10% → 연 3천 세대 [ASSUMPTION]
- 신축 유상옵션 비용 = 분양가의 평균 9.7% (공개 7개 단지 사례) [FACT, 보도 인용]
- Y5 계획 매출 77.6억원 = SAM 세대의 약 2% [TARGET]
## 가격 (모두 가설 [ASSUMPTION], VAT 별도, 주방 공사비 별도)
- 로봇 레디 주방 증분(구축) 450만원 / 신축 옵션 공급가 220만원
- 로봇 구매 1,490만원 + 설치·캘리브레이션 80만원  → 구축 1세대 설치 시점 합계 약 2,020만원
- 또는 로봇 렌탈 월 33만원 × 60개월 (Care Basic·소모품 Grip Kit 포함)
- 관리(Care Basic) 연 48만원(구매 고객), Care Plus 연 72만원(옵션); 소모품 연 약 36만원(List, 구매율 70%)
- 확장: Software Skill 60만원(V2), Tool 80만원, 로봇 교체 5~7년
- 가치 Anchor: 정리 40분/일 × 30일 = 월 20시간 [ASSUMPTION] × 가사서비스 1.5만원/h [FACT] × 자동화 60% [ASSUMPTION] → 월 약 18만원 (범위 11~24만원) [DERIVED]
- 원가 기반 Rental 하한(마진 20%): 월 31만원(Y3) / 24만원(Y5) [DERIVED] → 가치 Anchor보다 높음 = 지불의사 검증이 1순위
## 원가·마진
- 로봇 BOM 1,600(파일럿) → 1,150(Y3) → 900만원(Y5) [ASSUMPTION]; 구성: 6축 Arm (가반 3~5kg, Controller 포함) 600, Linear Rail · Carriage · Servo (2.4~3.6m) 150, End-effector Set (Gripper + Suction + Tool Changer) 90, Vision (Depth Camera 2대 + Mount) 80, Compute (Edge GPU) 80, Safety (Zone Sensor·Safety Controller) 60, Garage Door · Harness · Enclosure 50, 조립·시험 (Pilot은 Opex 인건비 처리) 40 (Y3 기준)
- 주방 모듈 원가 332→244만원/세대 (표준모듈 사용률 40%→80%) [DERIVED]
- 1세대 5년(구축·구매·Y3 원가): 매출 2,418만원, 매출총이익 608만원, 기여이익 458만원 [DERIVED]; Y5 원가 기준 기여이익 813만원; 설치 시점 매출 비중 84%
- Rental Payback: Y3 39개월 → Y5 30개월 [DERIVED]; 렌탈 파트너 요구 36개월 충족하려면 BOM 약 1,059만원 이하
## 판매 채널·물량 (Base, [TARGET])
- 구축 직접판매(학습용) [0, 5, 30, 50, 60] 세대 (Y1~Y5), 인테리어·주방가구 파트너 경유 [0, 0, 20, 130, 340], 신축 프로젝트 계약 [0, 0, 1, 2, 3]개 (프로젝트당 800세대 × 옵션 선택 10%)
- 파트너 수수료 0.1 (패키지 대비) [ASSUMPTION]; 직접판매 획득비용 세대당 150만원 [ASSUMPTION]
- 신축 계약→입주 약 2년 [ASSUMPTION] → 신축 설치 Y5 80세대, Y5 말 Backlog 400세대 [DERIVED]
## 재무 (Base, 억원)
- 매출 Y1 0.0 / Y2 0.4 / Y3 7.5 / Y4 32.5 / Y5 77.6 [DERIVED from ASSUMPTION/TARGET]
- 매출총이익률 Y1 0% / Y2 -75% / Y3 25% / Y4 30% / Y5 36%
- 영업이익 Y1 -10.2 / Y2 -13.3 / Y3 -29.7 / Y4 -37.5 / Y5 -36.4
- 5년 누적 현금 최저 약 -128억원; 손익분기 연 약 1,340세대 (Y5 단가·원가, Y6 이후)
- 시나리오 Y5 매출: 보수 27.8 / 기본 77.6 / 상향 134.0억원
## 투자 요청
- Seed 20억원 / 24개월 [ASSUMPTION]. 실제 인건비·시제품·목업 공간·인증 반영 재산정 25.8억원 → 부족 5.8억원, 20억원 단독 약 19개월 [DERIVED]
- 대안: TIPS R&D 최대 8억원 연계(선정 미확정) 또는 Seed 25억원 / M18 Bridge
- 용도(재산정 기준): Core Development Team 12.8억, Robot / Kitchen Prototype 3.0억, Mock-up / Installation Development 1.8억, Vision / Software / Data 1.0억, Pilot / Customer Validation 2.1억, Safety / Certification / IP 1.0억, Operations (G&A) 1.8억, Contingency (10%) 2.3억
- 24개월 검증 목표 [TARGET]: 실물 크기 Mock-up 2식, 평면 30개 분석→주방 표준안(Template) 3~5개, 승인된 작업 3개+, 인터뷰 50명·지불의사 조사 n≥300, 가정 실증 3~5세대(유료 포함), 검증된 BOM·설치비·설치시간, 관리·소모품 원가 실측, 주방가구·인테리어 파트너 실증 협의, 특허 출원 5~8건
- 중단·재검토 기준 [TARGET]: M6 사람 동선과 로봇 동작범위 양립 실패→구조 변경 / M9 정리 성공률 70% 미만→작업 범위 축소 / M12 지불의사 중앙값 < 목표가 60%→B2C 재검토 / M18 표준모듈 사용률 60% 미만→표준화 재검토 / M24 유료 실증·파트너 실패→확장 투자 보류
## 경쟁·사례 (공개 보도, FACT)
- 1X NEO: 2만 달러 또는 월 499달러, 2026 출하 발표 / LG CLOiD: CES 2026에서 식세기 비우기 시연 / Moley Robotic Kitchen: 팔 포함 £248,000 / Samsung Bot Chef: CES 2020 콘셉트 / Sunday Memo: 2026 베타
- 가전사(식세기·인덕션)는 가전 내부만 자동화; 범용 로봇은 집마다 다른 공간을 AI가 현장에서 해결해야 함; ARKI는 공간과 로봇을 함께 설계 (우위는 미검증)
## 팀
- Founder 7개 항목 모두 [Founder 정보 필요]. 필요 역량: 로봇 조작(Manipulation), 주방·건축 시공 통합, 고객·파트너 영업. 채용: M0 로봇 리드·주방/건축 통합 리드, M0~M3 비전/ML·메카트로닉스, M3~M6 임베디드·전기·안전, M6 사업개발, M12 현장 설치 엔지니어. 평균 인원 Y1 6명→Y2 9명 [ASSUMPTION]
## 금지
- 가상 고객·계약·LOI·파트너·매출, 근거 없는 점유율·ROI·비용절감률·TAM·로봇 성능, 세계 최초/국내 최초, 압도적 기술, 특허 등록 확정 표현 금지. 미검증 수치는 FACT/DERIVED/ASSUMPTION/TARGET/CONCEPT/TO BE VALIDATED로 표기(작게).