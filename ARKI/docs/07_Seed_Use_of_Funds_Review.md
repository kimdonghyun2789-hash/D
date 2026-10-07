# 07. Seed Use of Funds 검증

> ARKI Robotics (가칭) · Seed 투자 제안서 · Draft v3 · 2026-10-07 · 모든 수치는 FACT / DERIVED / ASSUMPTION / TARGET 표기. 실적·계약·고객·Partner 없음.

## 결론

- **20억원은 과다가 아니라 24개월 기준 약 5.8억원 부족**. 실제 인건비·Prototype·Mock-up 공간·Pilot 손실을 반영한 수정안은 25.8억원, 20억원 단독 Runway는 약 18.6개월.
- 권고 구조: **Plan A = Seed 20억 + TIPS R&D(일반, 최대 8억·24개월) = 28억** (여유 2.2억). TIPS는 운영사 투자·선정 절차가 필요하며 미확정. **Plan B = Seed 25억원 또는 M18 Bridge** (M12 Evidence 기반).
- 인증 본비용(KC 본인증 · ISO 13482 적용 등)은 Series A로 이연. Seed는 Risk Assessment · 예비시험 · 설계 기준 적용까지.

## Draft vs 수정안 (억원, 24개월)

| 항목 | Draft | 수정안 | 근거 (ASSUMPTION) |
|---|---|---|---|
| Core Development Team | 8.0 | 12.8 | 평균 인원 Y1 6명·Y2 9명 × 인당 연 8,500만원 (평균 연봉 약 7,100만원 × 1.2) |
| Robot / Kitchen Prototype | 4.0 | 3.0 | Arm 3~4대 (FR5·xArm 급 공개가 $7~8k) · Rail 2식 · End-effector 반복 · Garage 기구 |
| Mock-up / Installation Development | 2.5 | 1.8 | 약 50평 임차 24개월 + Full-scale Kitchen Mock-up 2식 (11자·ㄷ자) + 재시공 |
| Vision / Software / Data | 1.5 | 1.0 | GPU·Cloud · Data 수집·Annotation · Depth Camera |
| Pilot / Customer Validation | 1.5 | 2.1 | Interview·Time-diary·PSM·Conjoint(n≥300) + Home Pilot 5세대 매출총손실 + Pilot 획득비용 + Marketing |
| Safety / Certification / IP | 1.0 | 1.0 | Risk Assessment · 예비시험 · 선행기술조사 · 출원 5~8건 (KR) + PCT 1~2건 |
| Operations / Contingency | 1.5 | 4.1 | G&A 1.8 (법무·회계·보험·사무) + Contingency 10% 2.3 |
| **합계** | **20.0** | **25.8** |  |

## 항목별 현실성 검토

1. **인건비 (가장 큰 차이)**: Draft 8억원 = 24개월 평균 약 4.7명 (인당 8,500만원 기준). Robot 제어·Perception·Mechatronics·주방/건축 Integration·Embedded/Safety·현장 설치·BD를 동시에 수행할 수 없음. 수정안은 평균 7.5명 (Y1 6 → Y2 9).
2. **Prototype**: Draft 4억원은 과다 가능. 구매형 Arm(공개가 $7~8k급) 기반 Prototype이면 2년 3억원 내외로 가능 (D5). 단, 전용 Arm 개발은 Series A 이후.
3. **Mock-up 공간**: Full-scale Kitchen Mock-up 2식은 최소 30~50평 필요. 경기 남부 지식산업센터·공장형 임차 가정 (임대료 ASSUMPTION, 견적 필요).
4. **Pilot**: Home Pilot 5세대는 할인 유료 (실현율 50%) → Robot·Kitchen 원가 대비 손실 발생. 고객 조사(Panel n≥300 Conjoint) 비용 포함.
5. **인증**: 로봇 KC·EMC·안전 본인증 비용은 공개 자료 없음 (ASSUMPTION). Seed에는 예비시험·Risk Assessment만 반영.
6. **Runway 관리**: M12에 Evidence Review (WTP·Template·Task 성공률) → Bridge 또는 Series A 조기 착수 판단.

## 절감 옵션 (일정 Risk 증가)

- 채용 3개월 순연 (−1.5~2억) · Mock-up 공간 공유 (가구 Partner 공장·쇼룸 활용, −0.5억) · Prototype 1식 축소 (−0.5~1억).
- 절감 시 M12 Clean-up Integrated Demo 지연 가능성 → Kill Criteria 일정 재조정 필요.
