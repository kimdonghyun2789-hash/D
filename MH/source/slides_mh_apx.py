# MH Robotics — Appendix (A TIPS · B 제품 · 기술 · C 시장 · 경쟁 · D 경제성 · E IP · 리스크 · Q&A · F 참고).
# Table-led. Every number carries a tag; content shared with docs via content.py.
import os, json
import kit
from kit import T, W, H, MX, CW, text, rect, hline, table, ttxt, column_chart
import common
from common import M, start, head, foot, statement, note_line
import content as C
from mhkit import render, mt, mts, INK, INK2, GREY, SOFT, SOFT2, ACC, EDGE, A as AV

TG = ttxt
F = M['funding']; TP = F['tips']


def S(prs, code, title, sub=None, visual='표 중심 Appendix', chart='표', note=''):
    s = start(prs, 'x' + code, code, title, visual=visual, chart=chart, note=note)
    y = head(s, '', title, sub=sub)
    return s, y


def tslide(prs, code, title, header, rows, col_w, sub=None, size=9.5, note='', takeaway=None, align=None, pad=0.06, visual=None):
    s, y = S(prs, code, title, sub, visual=visual or '표 중심 Appendix', note=note)
    th = table(s, MX, y, CW, header, rows, col_w=col_w, size=size, header_size=size, align=align, pad=pad, label=code,
               max_h=H - y - (1.25 if takeaway else 0.8))
    if takeaway:
        statement(s, MX, min(y + th + 0.16, H - 1.2), CW, takeaway, size=11)
    foot(s, code)
    return s


# ---------------------------------------------------------------- index
INDEX = [
    ('A', 'TIPS 과제 상세', [('A1', '기술 KPI · Manipulation'), ('A2', '기술 KPI · Application'), ('A3', '기술 KPI · Business'),
                          ('A4', 'R&D Work Package 상세'), ('A5', 'Gate · 중단 기준'), ('A6', 'TIPS 과제 편성 · 24개월 사용처'), ('A7', '24개월 팀 계획')]),
    ('B', '제품 · 기술', [('B1', 'Adaptive Hand 시험 계획 (Buy vs Build)'), ('B2', 'Kitchen Variation 근거: 받은 평면 5종'),
                        ('B3', 'Environment Interface 예: Robot Home'), ('B4', '대표 평면 적용 예 (구축 2Bay A)'),
                        ('B5', 'Safety · Certification 경로'), ('B6', 'Robot System BOM · Benchmark')]),
    ('C', '시장 · 경쟁', [('C1', 'Housing · 시장 통계 (FACT)'), ('C2', 'Remodeling · Rental · Care Reference'), ('C3', 'Market Sizing 산식 · 검증 계획'),
                       ('C4', '경쟁사 상세')]),
    ('D', '경제성 · 재무', [('D1', '가격 가설 (원가 · 시장 · 가치)'), ('D2', 'Household 5년 경제성 상세'), ('D3', 'Rental · Care · Consumables'),
                         ('D4', '5-Year Financial Model (3 Scenario)'), ('D5', 'Sensitivity')]),
    ('E', 'IP · 리스크 · Q&A', [('E1', 'IP Portfolio 상세'), ('E2', 'Risk Register'), ('E3~E5', '투자심사 예상질문 20 · 방어논리'),
                             ('E6', '부족한 Evidence · Founder 입력 필요'), ('E7', '투자심사 Memo · 판단')]),
    ('F', '참고', [('F1', 'Number Tag 원칙'), ('F2~F5', 'Sources')]),
]


def idx(prs):
    s = start(prs, 'xIDX', 'Index', 'Appendix 목차', visual='3열 목차 (A~F Section · Code · 제목)', chart='없음',
              note='부록은 본문 18쪽의 근거, 계산, 검증 계획입니다. A는 TIPS 과제 상세, B는 제품과 기술, C는 시장과 경쟁, D는 경제성, E는 IP와 리스크, 예상 질문, 투자 메모, F는 Tag 원칙과 출처입니다.')
    y = head(s, 'APPENDIX', 'Appendix 목차',
             sub='본문 수치의 근거 · 계산 · 검증 계획. 재무 수식 모델: MH_Robotics_Financial_Model.xlsx · 이전 판 (ARKI v4) 본문 · 부록은 archive/ARKI_v4에 삭제 없이 보관')
    cols = [INDEX[0:2], INDEX[2:4], INDEX[4:6]]
    cw = (CW - 0.6) / 3
    for ci, secs in enumerate(cols):
        cx = MX + ci * (cw + 0.3); yy = y
        for key, name, items in secs:
            rect(s, cx, yy, cw, 0.32, fill=INK)
            text(s, cx + 0.12, yy, cw - 0.24, 0.32, f'{key}   {name}', size=10.5, bold=True, color='FFFFFF', anchor='m')
            yy += 0.36
            for code, t in items:
                text(s, cx + 0.05, yy, 0.62, 0.22, code, size=9, bold=True, anchor='m')
                text(s, cx + 0.68, yy, cw - 0.7, 0.22, t, size=9, color=INK2, anchor='m')
                yy += 0.22
            yy += 0.12
        assert yy < H - 0.55, ('index column too long', ci, yy)
    foot(s, 'Index')


# ---------------------------------------------------------------- A: TIPS
def _kpi_rows(group):
    rows = []
    for g, name, d, bench, m6, m12, m18, m24, basis, tag in C.KPI:
        if g != group:
            continue
        rows.append([(name, {'bold': True}), d, bench, m6, m12, m18, (m24, {'bold': True}), basis, TG(tag)])
    return rows


def a1(prs):
    tslide(prs, 'A1', '기술 KPI (1/3) · Manipulation', ['KPI', '정의', 'Benchmark (출처)', 'M6', 'M12', 'M18', 'M24', '목표 근거', 'Tag'], _kpi_rows('Manipulation'),
           [1.45, 2.0, 1.85, 0.85, 0.85, 0.9, 0.95, 1.95, 1.03], size=8, pad=0.04,
           sub='근거 없는 정량목표 금지: 목표는 공개 Benchmark 또는 경제성 가정에서 도출. Benchmark가 없는 지표는 측정 후 확정.',
           note='Manipulation KPI입니다. 식기 단위 성공률은 목업 80%, 주방 3종 85%, 가정 90%를 목표로 합니다. 공개 연구의 식기세척기 적재 성공률은 58.7%였고, 이보다 높은 목표는 환경 Interface 효과를 확인하는 지표입니다. 복구율처럼 비교 기준이 없는 지표는 12개월 차 측정 후 확정합니다.')


def a2(prs):
    tslide(prs, 'A2', '기술 KPI (2/3) · Application', ['KPI', '정의', 'Benchmark (출처)', 'M6', 'M12', 'M18', 'M24', '목표 근거', 'Tag'], _kpi_rows('Application'),
           [1.35, 2.0, 1.6, 0.85, 0.85, 1.0, 1.2, 1.95, 1.03], size=8.2, pad=0.04,
           sub='Application KPI는 설치 원가 가정 (인시)과 직접 연결 → Calibration · 설치 시간이 줄면 Unit Economics가 바뀜',
           note='적용 KPI입니다. Calibration 4시간과 설치 2인 1일은 설치 원가 가정에서 거꾸로 계산한 목표입니다. 주방 호환률은 평면 30개 분석과 상담 주방 실측으로 가정값을 대체합니다.')


def a2b(prs):
    tslide(prs, 'A3', '기술 KPI (3/3) · Business', ['KPI', '정의', 'Benchmark (출처)', 'M6', 'M12', 'M18', 'M24', '목표 근거', 'Tag'], _kpi_rows('Business'),
           [1.35, 2.0, 1.6, 0.85, 0.85, 1.0, 1.2, 1.95, 1.03], size=8.2, pad=0.04,
           sub='Business KPI는 재무모델 가정 (BOM · 설치 · Care · 소모품 · WTP)을 실측으로 바꾸는 지표',
           note='사업 KPI입니다. BOM, 설치비, A/S와 Care 원가는 모두 가정이며 24개월 안에 견적과 실측으로 바꿉니다. 지불의사는 18개월 차 300명 이상 조사와 예약금 테스트, 실증 3세대의 유료 전환으로 확인합니다.')


def a3(prs):
    rows = [[(c, {'bold': True}), (n, {'bold': True}), per, goal, '\n'.join('· ' + x for x in items), out, kpi, who] for c, n, per, goal, items, out, kpi, who in C.WP]
    tslide(prs, 'A4', 'R&D Work Package 상세 (TIPS 과제)', ['WP', '이름', '기간', '목표', '주요 내용', '산출물', 'KPI', '담당 (채용 계획)'], rows,
           [0.5, 1.45, 0.75, 1.65, 3.2, 1.6, 1.5, 1.18], size=8, pad=0.045,
           sub='TIPS R&D = Technology De-risking. WP6 실증은 목업 → 주방 3종 → 가정 3세대 순서. 담당은 채용 계획 기준 (현재 인원 없음).',
           note='여섯 개 작업 묶음의 목표, 내용, 산출물, KPI입니다. Hand는 상용 Gripper 비교에서 시작해 세 번 개선하고, Skill은 Template으로 만들어 주방마다 재사용합니다. Calibration은 새 주방 4시간, Interface는 필요한 곳만 표준화, 안전은 표준 Gap과 사전시험, 마지막 WP6에서 가정 실증까지 끝까지 검증합니다.')


def a4(prs):
    rows = [[(g, {'bold': True, 'color': ACC}), ev, ok, ng] for g, ev, ok, ng in C.GATES]
    tslide(prs, 'A5', 'Gate · 중단 기준 (24개월)', ['Gate', '확인할 Evidence', '통과 기준 (TARGET)', '미달 시 조치'], rows, [0.8, 4.6, 3.3, 3.13], size=9.5,
           sub='Roadmap이 아니라 기업가치를 바꾸는 Evidence 중심. 기준 미달 시 구조 변경 · 범위 축소 · Scale 보류.',
           takeaway='Series A 판단 = 기술 성공 + 유료 전환 + 설치 · 서비스 원가 실측 (M24). 기준 미달 시 Bridge 또는 범위 축소 후 재검증',
           note='6개월마다 판단 지점을 둡니다. 6개월 차에 자체 Hand가 상용 대비 우위가 없으면 상용 Gripper로 전환합니다. 12개월 차 목업 80%, 18개월 차 주방 세 종 Transfer와 지불의사, 24개월 차 가정 실증과 유료 전환, 원가 실측이 Series A의 조건입니다.')


def a5(prs):
    s, y = S(prs, 'A6', 'TIPS 과제 편성 · 24개월 사용처 (Base)', sub=f"TIPS 과제 총 {TP['total'] / 10000:.2f}억원 = 정부 8억원 (75%) + 기관부담 {TP['private'] / 10000:.2f}억원. 회사 전체 24개월 지출 {F['spend_total'] / 10000:.1f}억원 중 일부 (모든 값 ASSUMPTION, 규정은 FACT)",
             note='TIPS 과제 예산과 회사 전체 지출을 함께 보여드립니다. 과제 총액은 정부지원 8억원을 75%로 나눈 약 10.67억원이고, 회사 부담 2.67억원 중 현물은 Founder 인건비 참여분, 현금은 Seed 자금으로 냅니다. 오른쪽은 24개월 전체 사용처이며 TIPS 편성분과 Seed 부담분을 나눴습니다.')
    lw = 5.4
    rows = [[r['cat'], (f"{r['y1']:,.0f}", {}), (f"{r['y2']:,.0f}", {}), (f"{r['total']:,.0f}", {'bold': True}), r['kind']] for r in TP['rows']]
    rows.append([('합계', {'bold': True}), f"{TP['year_total'][0]:,.0f}", f"{TP['year_total'][1]:,.0f}", (f"{TP['total']:,.0f}", {'bold': True}), ''])
    th = table(s, MX, y, lw, ['TIPS 비목 (만원)', '1차년도', '2차년도', '합계', '구분'], rows, col_w=[1.75, 0.9, 0.9, 1.0, 0.85], size=9,
               align=['l', 'r', 'r', 'r', 'c'], label='A6p', pad=0.05)
    chk = [['정부지원 (75%)', f"{TP['gov']:,.0f}", 'FACT 상한'], ['기관부담 현금', f"{TP['private_cash']:,.0f}", f"≥ 10% 충족 ({TP['private_cash'] / TP['private'] * 100:.0f}%)"],
           ['기관부담 현물', f"{TP['inkind']:,.0f}", 'Founder 참여분'], ['간접비율 (현금 직접비 대비)', f"{TP['indirect_rate'] * 100:.1f}%", '협약 기준 확인 필요']]
    table(s, MX, y + th + 0.15, lw, None, chk, col_w=[2.2, 1.2, 2.0], size=9, align=['l', 'r', 'l'], label='A6c', pad=0.05)
    rx = MX + lw + 0.3; rw = W - MX - rx
    rows2 = []
    for u in F['uses']:
        tot = sum(u['y']); tv = sum(u['tips'])
        rows2.append([u['cat'], f"{tot:,.0f}", f"{tv:,.0f}" if tv else '-', f"{tot - tv:,.0f}"])
    rows2.append([('합계', {'bold': True}), (f"{F['spend_total']:,.0f}", {'bold': True}), (f"{TP['total']:,.0f}", {'bold': True}), (f"{F['spend_total'] - TP['total']:,.0f}", {'bold': True})])
    table(s, rx, y, rw, ['24개월 사용처 (만원)', '합계', 'TIPS 편성', '그 외 (Seed)'], rows2, col_w=[rw - 3.0, 1.0, 1.0, 1.0], size=8.5,
          align=['l', 'r', 'r', 'r'], label='A6u', pad=0.035)
    foot(s, 'A6')


def a6(prs):
    rows = []
    for key, role, m0, cost, frac, part, kind, lean, lean_m0 in __import__('model').TEAM:
        tm = next(m for m in F['team'] if m['key'] == key)
        rows.append([role.replace(' [Founder 정보 필요]', ''), M['team_kind'][kind], f'M{m0}', f'{cost:,}', f'{frac:.1f}', f'{part * 100:.0f}%',
                     f"{tm['cost'][0]:,.0f}", f"{tm['cost'][1]:,.0f}", ('예' if lean else '아니오') + (f' (M{lean_m0})' if lean_m0 else '')])
    rows.append([('합계', {'bold': True}), '', '', '', '', '', (f"{F['people'][0]:,.0f}", {'bold': True}), (f"{F['people'][1]:,.0f}", {'bold': True}), f"Lean {sum(F['lean_people']):,.0f}"])
    tslide(prs, 'A7', '24개월 팀 계획 (채용 계획, ASSUMPTION)', ['역할', '구분', '시작', '연 인건비 (만원)', 'FTE', 'TIPS 참여율', 'Y1 인건비', 'Y2 인건비', 'Lean 포함'], rows,
           [3.6, 0.95, 0.65, 1.25, 0.6, 1.0, 1.1, 1.1, 1.58], size=8.5, pad=0.035, align=['l', 'l', 'c', 'r', 'r', 'r', 'r', 'r', 'l'],
           sub=f"Founder 2인 = TIPS 요건 기준의 자리 (인물 정보 없음). 연 인건비 = 연봉 × 1.2 (4대보험 · 퇴직급여). 평균 FTE {F['fte'][0]:.1f} → {F['fte'][1]:.1f}, 24개월 차 약 {F['heads_m24']:.0f}명.",
           note='24개월 채용 계획입니다. 리드 세 명 (조작, 인식, Hand)을 먼저 뽑고, 사업개발은 7개월 차, 설치 엔지니어는 13개월 차에 합류합니다. Lean안에서는 Hand 센싱, Skill/Data, 현장 Technician을 빼고 시험 인력을 19개월 차로 늦춥니다. 연봉은 평균 가정이며 실제 채용 조건으로 바꿉니다.')


# ---------------------------------------------------------------- B: product · technology
def b1(prs):
    rows = [list(r) for r in C.HAND_TEST]
    tslide(prs, 'B1', 'Adaptive Hand 시험 계획 (Buy vs Build)', ['항목', '내용', 'Tag'], [[(a, {'bold': True}), b, TG(c.split(' ')[0]) if c.split(' ')[0] in kit.TAGS else c] for a, b, c in rows],
           [1.7, 8.75, 1.38], size=9.5,
           sub='상용 Gripper를 먼저 기준선으로 쓰고, 30종 식기 세트로 비교한 뒤 자체 Hand 개발 범위를 결정 (WP1)',
           takeaway='자체 Hand 채택 조건 = 성공률 · 교체 횟수 · 원가 중 하나 이상에서 명확한 우위. 우위가 없으면 Buy로 전환하고 교체형 Pad · Skill에 집중',
           note='자체 Hand가 필요한지 6개월 차에 판정합니다. 접시, 그릇, 컵, 유리잔, 수저, 뚜껑, 도구까지 30종 세트를 젖은 조건과 식기세척기 랙 조건에서 시험하고, 상용 Gripper와 흡착, Soft Finger를 비교군으로 둡니다. 식품이 닿는 부품은 식품위생법상 기구 기준과 고무제 규격을 따릅니다.')


def b2(prs):
    rows = [list(r) for r in C.PLANS]
    tslide(prs, 'B2', 'Kitchen Variation 근거: 받은 평면 5종', ['평면', '구분', '크기 (mm)', '주방 형태', '디지털화 (3D)', '기본 배치 (Remodeling 한 줄)'], rows,
           [1.25, 1.85, 1.35, 3.0, 1.6, 2.78], size=9.5,
           sub='사용자 제공 도면을 치수선 기준으로 재작도 (특정 단지 표기 없음). 표본 5종 → 평면 30개 분석으로 확대 (M6, TARGET)',
           takeaway='5종 모두 싱크와 조리기구가 다른 벽 → 로봇 구역 분리 가능. 다만 3종은 싱크 줄 2.6~2.8m → 짧은 벽용 Compact 구성 필요 (Kitchen Compatibility KPI)',
           note='받은 평면 다섯 종의 분류입니다. 구축 2Bay A 한 종만 기본 한 줄 배치가 들어갔고, 나머지는 싱크 줄이 2.6에서 2.8미터로 짧습니다. 이것이 주방마다 다른 환경의 실제 예이고, Retrofit과 짧은 벽용 Compact 구성을 개발해야 하는 이유입니다. 표본이 작아 평면 30개로 확대합니다.')


def b3(prs):
    s, y = S(prs, 'B3', 'Environment Interface 예: Robot Home 보관 · 전개 (Remodeling)', sub='평소엔 Robot Home에 접혀 있다가 문이 열리면 Rail로 나옴 · 낮은 식세기 하단 랙은 랙을 당겨 위에서 적재 (3D 충돌검사, CONCEPT)',
             visual='3D 콘셉트 렌더 5컷: ① 문 닫힘 ② 문 열림 ③ 전개 ④ Rail 이동 ⑤ 하단 랙 적재 (낮은 작업점)', chart='3D 렌더 5컷',
             note='Remodeling 채널에서 쓰는 Interface의 예입니다. 로봇은 조리대 끝 Robot Home에 접혀 있다가 문이 열리면 펴지면서 레일로 나옵니다. 식기세척기 하단 랙처럼 낮은 작업점은 랙을 당겨 위에서 넣습니다. 3D 모델에서 보관, 전개, 이동 경로의 충돌을 검사했으며 실제 기구 검증 전 개념입니다.')
    names = [('v2_stow_1_closed', '① 평소: 문 닫힘'), ('v2_stow_2_open', '② 문 열림'), ('v2_stow_3_deploy', '③ 전개'), ('v2_stow_4_exit', '④ Rail 이동'), ('v2_stow_5_low', '⑤ 하단 랙 적재')]
    gap = 0.12; tw = (CW - 4 * gap) / 5; th = tw * 840 / 1100
    for i, (nm, lab) in enumerate(names):
        x = MX + i * (tw + gap)
        render(s, nm, x, y, tw, th, focus=(0.5, 0.5))
        rect(s, x, y + th, tw, 0.3, fill=SOFT)
        text(s, x, y + th, tw, 0.3, lab, size=9.5, bold=True, align='c', anchor='m')
    mt(s, MX + 0.06, y + 0.06, 'CONCEPT', fill='FFFFFF')
    rows = [['Robot Home (Dock)', '조리대 위 끝 W45 × D62 × H137cm · 여닫이 문 1짝 · 평소 로봇 수납 (보이지 않음)', TG('CONCEPT')],
            ['Rail', '상부장 하단 (높이 약 139cm) · 바닥 사용 안 함 · Retrofit은 Compact Mount로 대체', TG('CONCEPT')],
            ['낮은 작업점', '식세기 하단 랙 44cm 당김 → 위에서 적재 (Gripper 최저 약 37cm) · 서랍도 열어서 위에서 넣음', TG('CONCEPT')],
            ['검증 방법', '캡슐 (로봇) · 상자 (가구) 충돌검사: 작업 자세 · 보관 · 전개 · Rail 이동 경로 관통 0cm (3D 모델 기준)', TG('DERIVED')]]
    table(s, MX, y + th + 0.45, CW, None, rows, col_w=[1.8, 8.85, 1.18], size=9.5, label='B3t')
    foot(s, 'B3')


def b4(prs):
    s, y = S(prs, 'B4', '대표 평면 적용 예: 구축 2Bay A (CONCEPT)', sub='받은 도면 (12,390 × 11,670mm, 코어 포함)을 치수선 기준으로 3D화 · 왼쪽 원래 주방, 오른쪽 MH Interface 적용 (특정 단지 아님)',
             visual='평면도 2장 (원래 ㄱ자 주방 / Interface 적용 후) + 변경 사항 표', chart='평면도 2 + 표',
             note='대표 평면 한 종에 Remodeling 방식으로 Interface를 넣은 예입니다. 원래 ㄱ자 주방의 윗벽을 로봇 작업 줄로 쓰고 인덕션은 옆벽으로 옮겼습니다. 보관함 문이 옆벽 때문에 90도까지만 열리는 조건에서 보관, 전개, 이동 경로를 다시 검사했습니다.')
    jp = os.path.join(common.ROOT, 'assets', 'renders', 'plan_old2a_verify.json')
    V = json.load(open(jp, encoding='utf-8'))['ik']['verify']
    ph = 3.6; pw = ph * (1400 / 1320)
    for i, (nm, lab) in enumerate([('plan_old2a_top_orig', '원래 평면 (ㄱ자 주방)'), ('plan_old2a_top_arki', 'Interface 적용 (윗벽 로봇 줄 + 인덕션 옆벽)')]):
        x = MX + i * (pw + 0.3)
        render(s, nm, x, y, pw, ph, bg=(255, 255, 255))
        text(s, x, y + ph + 0.04, pw, 0.24, lab, size=9.5, bold=True, check=False)
    rx = MX + 2 * pw + 0.65; rw = W - MX - rx
    rows = [['주방 윗벽', '3,255mm'], ['로봇 작업 줄', '3,150mm (Robot Home 45 · Drop Zone 70 · 싱크 80 · 서랍 60 · 식세기 60cm)'],
            ['싱크 중심 이동', '약 21cm'], ['인덕션', '옆벽 아래쪽으로 이동 (로봇 금지 구역)'], ['보관함 문', '최대 90° (옆벽)'],
            ['충돌검사', f"보관 {V['park']:.0f}cm · 전개 경로 {V['path']:.0f}cm · Rail 이동 {V['transit']:.0f}cm 관통 (가구 {V['obstacles']}개)"]]
    table(s, rx, y, rw, ['항목', '값'], rows, col_w=[1.15, rw - 1.15], size=9.5, label='B4')
    foot(s, 'B4')


def b5(prs):
    rows = [[a, b, TG(t), src] for a, b, t, src in C.SAFETY]
    tslide(prs, 'B5', 'Safety · Certification 경로', ['항목', '내용', 'Tag', '출처'], rows, [1.7, 8.0, 1.2, 0.93], size=9.5,
           sub='가정용 로봇 기준이 발행 전 (IEC 63682 초안)이므로 인증기관 사전상담으로 경로를 먼저 확정 (WP5)',
           takeaway='안전 설계는 기준 발행을 기다리지 않음: 협동로봇 기준 (감속 · 접촉력)을 최소선으로, 가정용 초안 요구를 Gap 분석으로 반영',
           note='안전과 인증 경로입니다. 협동로봇 기준인 ISO 10218 2025년판의 감속과 접촉력 기준을 최소선으로 쓰고, 가정용 로봇 기준 IEC 63682는 아직 초안이라 Gap 분석으로 반영합니다. 9개월 차에 인증기관 사전상담, 18개월 차에 전기와 EMC 사전시험을 합니다.')


def b6(prs):
    s, y = S(prs, 'B6', 'Robot System BOM · Component Benchmark', sub='Benchmark = 공개 판매가 (FACT, 환율 1,400원/USD ASSUMPTION). BOM = ASSUMPTION, 재무모델 Base BOM과 합계 일치 (model.py assert).',
             visual='좌측 공개가 Benchmark 표, 우측 BOM Pilot · Y3 · Y5 표 (Adaptive Hand 포함)', chart='표 2개',
             note='로봇 시스템 원가는 공개가 부품을 기준으로 추정했습니다. Pilot 1,680만원에서 Series A 이후 1,180만원, 5년차 915만원으로 내려간다고 가정했습니다. 가장 큰 항목은 Arm이며, 자체 Hand는 상용 Gripper보다 낮은 목표 원가를 둡니다.')
    bm = [list(r) for r in C.BENCH]
    lw = 5.3
    table(s, MX, y, lw, ['Benchmark (FACT)', 'USD', '만원'], bm, col_w=[2.9, 1.3, 1.1], size=9.5, align=['l', 'r', 'r'], label='B6b')
    rx = MX + lw + 0.3; rw = W - MX - rx
    rows = [[r[0], f"{r[1]:,}", f"{r[2]:,}", f"{r[3]:,}"] for r in M['bom_breakdown']]
    tot = [sum(r[i] for r in M['bom_breakdown']) for i in (1, 2, 3)]
    rows.append([('합계 (재무모델 BOM)', {'bold': True}), (f"{tot[0]:,}", {'bold': True}), (f"{tot[1]:,}", {'bold': True}), (f"{tot[2]:,}", {'bold': True, 'color': ACC})])
    table(s, rx, y, rw, ['BOM (ASSUMPTION, 만원/대)', 'Pilot', 'Y3', 'Y5'], rows, col_w=[rw - 2.25, 0.75, 0.75, 0.75], size=9, align=['l', 'r', 'r', 'r'], label='B6m')
    statement(s, MX, 5.95, CW, 'BOM 하락 경로 = 수량 + Arm OEM Partner (국산 · 중국산 Cobot) + 자체 Hand 원가 설계. Y5 Arm 450만원은 공격적 가정 → 민감도 2순위 (D5)', size=10.5)
    foot(s, 'B6')


# ---------------------------------------------------------------- C: market · competition
def c1(prs):
    rows = [[a, b, TG(t), src] for a, b, t, src in C.HOUSING]
    tslide(prs, 'C1', 'Housing · 시장 통계', ['항목', '값', 'Tag', '출처 / 산식'], rows, [3.3, 3.2, 1.2, 4.13], size=9.5,
           sub='공식 통계는 검색 시점 (2026-10-07~08) 보도 인용 → 외부 제출 전 원문 (국가데이터처 · 국토부 보도자료) 대조 필요',
           note='주택 통계는 국가데이터처 2025 인구주택총조사와 국토부 주택통계를 기준으로 했고, 문제의 크기는 2024 가계생산 위성계정의 무급 가사노동 가치로 보여드립니다. 주방 교체 세대 수는 공식 통계가 없어 두 방법으로 교차 추정하고 가정으로 표시했습니다.')


def c2(prs):
    rows = [[a, b, TG(t), n] for a, b, t, n in C.REFS]
    tslide(prs, 'C2', 'Remodeling · Rental · Care Reference', ['항목', '값', 'Tag', '비고'], rows, [3.0, 4.6, 1.2, 3.03], size=9.5,
           sub='렌탈 · 방문관리 · 빌트인 통합 수요는 공개 실적으로 확인 (FACT). 단, 로봇 Integration에 대한 지불 여부는 별개 → WTP 조사',
           note='주방 리모델링과 렌탈, 관리 서비스의 참고 자료입니다. 렌탈과 정기관리 시장이 이미 크다는 것은 코웨이와 LG 실적으로 확인되지만, 로봇에 같은 지불이 일어날지는 별개라서 지불의사 조사가 필요합니다.')


def c3(prs):
    mk = M['market']['B']
    s, y = S(prs, 'C3', 'Market Sizing 산식 · 검증 계획', sub='세대 수 × 적용률 × 단가. 핵심 비율은 ASSUMPTION → 검증 방법과 시점 지정',
             note='본문 시장 슬라이드의 산식과 가정을 모두 보여드립니다. Remodeling, Retrofit, 신축 세 시장을 더한 대상 시장은 연 약 3,676억원이고, 5년차 계획 매출 91.5억원은 그 안의 약 2.5%입니다. 각 비율은 6개월에서 24개월 사이에 견적, 평면 분석, 소비자 조사, 실증 데이터로 대체합니다.')
    rows = [['① Remodeling', '30만 × 10% × 60%', f"{mk['fit'] * 1000:,.0f}세대/년", f"{mk['pkg_remodel']:,.0f}만원 (Interface 450 + Attach 85% × 1,570)", f"{mk['sam_remodel']:,.0f}억원"],
            ['② Retrofit', f"1,328만 × 10% × 60% × 40% = {mk['retro_pool'] / 10:.1f}만 × 0.5%", f"{mk['retro_annual'] * 1000:,.0f}세대/년", f"{mk['pkg_retro']:,.0f}만원 (Kit 150 + 1,490 + 120)", f"{mk['sam_retro']:,.0f}억원"],
            ['③ New-build', '20만 × 15% × 10%', f"{mk['new_opt'] * 1000:,.0f}세대/년", f"{mk['pkg_new']:,.0f}만원 (Option 220 + 25% × 1,570)", f"{mk['sam_new']:,.0f}억원"],
            ['④ Recurring', f"Installed Base × ARPU {mk['arpu']:.1f}만원 (Care 70% × 48 + 소모품 70% × 36)", '1,000대', '-', f"{mk['recurring_per_1000']:.1f}억원/1,000대"],
            [('SAM (① + ② + ③)', {'bold': True}), '', '', '', (f"{mk['sam']:,.0f}억원", {'bold': True})],
            [('SOM (Y5 Base Plan)', {'bold': True}), f"{mk['som_hh']:,.0f}세대 · 대상의 {mk['som_share_hh'] * 100:.1f}%", '', '', (f"{mk['som']:.1f}억원", {'bold': True, 'color': ACC})]]
    th = table(s, MX, y, CW, ['시장', '산식', '대상', '패키지 단가', '연 규모'], rows, col_w=[1.7, 4.3, 1.4, 3.0, 1.43], size=9, align=['l', 'l', 'r', 'l', 'r'], label='C3a', pad=0.05)
    rows2 = [[a, b, c, d] for a, b, c, d in C.MKT_VALID]
    table(s, MX, y + th + 0.2, CW, ['가정', 'Tag', '검증 방법', '시점'], rows2, col_w=[4.2, 2.0, 4.6, 1.03], size=9, label='C3b', pad=0.05)
    foot(s, 'C3')


def c4(prs):
    rows = [[(n, {'bold': True}), k, d, p, ap, f'[{src}]'] for n, k, d, p, ap, src in C.COMP]
    tslide(prs, 'C4', '경쟁사 상세 (공개 자료)', ['Player', '구분', '공개 내용', '가격 · 상태', '접근', '출처'], rows, [1.9, 1.5, 3.1, 2.75, 1.7, 0.88], size=8.8, pad=0.045,
           sub='공개 보도 · 회사 발표 기준. 성능 비교 Data는 공개되지 않아 하지 않음. "최초 · 압도적" 주장 없음.',
           takeaway='MH의 차이 = 고정형 Kitchen System (Hand · Skill · Calibration · Interface · Care). 우위는 미검증 → 재배치 시간 · 원가 · 유료 전환으로 증명',
           note='경쟁사 상세입니다. 휴머노이드와 이동형 로봇은 설치가 필요 없는 범용 접근이고, 조리 로봇은 전용 주방이나 조리대 기기, 협동로봇과 Gripper는 부품입니다. 가구사의 로봇 협업 보도는 찾지 못했습니다. MH가 낫다는 것은 아직 검증 전이며 실증 데이터로 보여드려야 합니다.')


# ---------------------------------------------------------------- D: economics
def d1(prs):
    rows = [[(a, {'bold': True}), (b, {'bold': True}), c, d, e] for a, b, c, d, e in C.PRICE]
    tslide(prs, 'D1', '가격 가설: 원가 Floor · 시장 Reference · 가치 Anchor', ['항목', '가격 가설 (VAT 별도)', '원가 Floor (DERIVED)', '시장 Reference (FACT)', '가치 Anchor'], rows,
           [2.1, 1.6, 2.8, 3.3, 2.03], size=9, pad=0.05,
           sub='범위를 먼저 계산하고 WTP로 검증하는 구조. 모든 가격 = ASSUMPTION',
           takeaway=f"가치 Gap: CLEAN만의 가사 대체 가치 (월 약 {M['value']['value']:.0f}만원) < Rental 월 33만원 → Premium 고객 · ASSIST 확장 · 위생 · 편의 가치로 검증 (WTP M18)",
           note='가격은 원가 하한, 시장 참고가, 고객 가치의 세 방향에서 범위를 잡았습니다. 솔직히 말씀드리면 식기 정리만의 가사 대체 가치는 월 18만원 수준으로 렌탈 요금보다 낮습니다. 그래서 Premium 고객부터 시작하고, ASSIST 확장과 위생, 편의 가치를 묶어 지불의사를 확인합니다.')


def d2(prs):
    keys = [('purchase_direct_Y3', 'Remodeling 구매 Y3'), ('purchase_direct_Y5', 'Remodeling 구매 Y5'), ('rental_direct_Y3', 'Remodeling Rental Y3'),
            ('rental_direct_Y5', 'Remodeling Rental Y5'), ('retrofit_purchase_Y3', 'Retrofit 구매 Y3'), ('newbuild_purchase_Y3', 'New-build 구매 Y3')]
    HHd = {k: M['household'][k] for k, _ in keys}
    def r_(lab, f, bold=False, color=None):
        o = {'bold': bold}
        if color: o['color'] = color
        return [(lab, {'bold': bold})] + [(f(HHd[k]), o) for k, _ in keys]
    rows = [r_('INSTALL (Interface · 설치 · Robot)', lambda h: f"{h['layers']['install']:,.0f}"),
            r_('OPERATE (Rental · Care · 소모품, 5년)', lambda h: f"{h['layers']['operate']:,.0f}"),
            r_('EXPAND (Skill · Tool 기대값)', lambda h: f"{h['layers']['expand']:,.0f}"),
            r_('5년 매출', lambda h: f"{h['rev5']:,.0f}", True),
            r_('Robot BOM (Rental은 잔존가치 차감)', lambda h: f"{h['C']['robot']:,.0f}"),
            r_('Interface · 설치 · 물류 원가', lambda h: f"{h['C']['kitchen'] + h['C']['comm'] + h['C']['log']:,.0f}"),
            r_('서비스 원가 (Care · 소모품 · Warranty)', lambda h: f"{h['service_cost5']:,.0f}"),
            r_('Rental 금융비용', lambda h: f"{h['C'].get('finance', 0):,.0f}"),
            r_('채널비용 (획득 · Partner · 수주)', lambda h: f"{h['C']['channel']:,.0f}"),
            r_('5년 매출총이익 (채널 전)', lambda h: f"{h['gp5']:,.0f}", True),
            r_('5년 Lifetime Contribution', lambda h: f"{h['contrib5']:,.0f}", True, ACC),
            r_('Contribution Margin', lambda h: f"{h['cm5'] * 100:.1f}%")]
    tslide(prs, 'D2', 'Household 5년 경제성 상세 (1세대 · 만원 · Base)', ['항목'] + [l for _, l in keys], rows, [3.15] + [1.445] * 6, size=9,
           align=['l'] + ['r'] * 6, pad=0.05,
           sub='구매 = Care 가입 세대 기준, Skill · Tool은 구매율 반영 기대값. Y3 / Y5 = 해당 연도 원가 수준을 5년간 적용. 전부 DERIVED (from ASSUMPTION)',
           takeaway='매출보다 서비스 원가 · BOM에 민감: Y3 → Y5 원가 개선 (BOM · 설치 · 방문)만으로 Contribution이 약 2배',
           note='대표 1세대의 5년 경제성입니다. Remodeling 구매 고객은 설치 시점 2,020만원, 5년 매출 2,418만원이고 3년차 원가 기준 기여이익은 428만원, 5년차 원가 기준 798만원입니다. Retrofit은 Partner 수수료와 현장 Calibration 비용 때문에 낮고, 신축은 수주비용이 세대당으로 작아 높게 나옵니다.')


def d3(prs):
    s, y = S(prs, 'D3', 'Rental · Care · Consumables 단위 경제성 (Base)', sub='Rental = 초기 부담을 낮추는 수단 (Pilot은 MH 직접, Scale은 Partner 자산). Care = Robot Lifecycle Maintenance. 모두 DERIVED (from ASSUMPTION)',
             note='Rental은 월 33만원에 Care와 Grip Kit를 포함하고, 3년차 원가 기준 월 원가는 약 25.6만원, 현금 회수 기간은 약 40개월입니다. Scale 단계에서는 Partner가 자산을 갖고 MH는 월 6만원 서비스료를 받으며, Partner의 내부수익률은 약 13%로 계산됩니다. Care는 3년차 마진 23%, 5년차 44%입니다.')
    lw = (CW - 0.6) / 3
    R3, R5 = M['rental']['Y3'], M['rental']['Y5']
    rows = [['감가 (잔존 15%)', f"{R3['lines']['dep']:.1f}", f"{R5['lines']['dep']:.1f}"], ['금융비용', f"{R3['lines']['fin']:.1f}", f"{R5['lines']['fin']:.1f}"],
            ['Care 원가', f"{R3['lines']['care']:.1f}", f"{R5['lines']['care']:.1f}"], ['Grip Kit 원가', f"{R3['lines']['grip']:.1f}", f"{R5['lines']['grip']:.1f}"],
            ['Failure Reserve', f"{R3['lines']['reserve']:.1f}", f"{R5['lines']['reserve']:.1f}"], [('월 원가 합계', {'bold': True}), f"{R3['cost_m']:.1f}", f"{R5['cost_m']:.1f}"],
            ['월 요금 (가정)', f"{R3['fee']:.0f}", f"{R5['fee']:.0f}"], [('월 Contribution', {'bold': True}), f"{R3['contrib_m']:.1f}", f"{R5['contrib_m']:.1f}"],
            ['Payback (개월)', f"{R3['payback']:.1f}", f"{R5['payback']:.1f}"], ['Partner IRR (연)', f"{M['partner_irr']['B']['irr_y'] * 100:.1f}%", '']]
    table(s, MX, y, lw, ['Rental (만원/월)', 'Y3', 'Y5'], rows, col_w=[lw - 1.5, 0.75, 0.75], size=9, align=['l', 'r', 'r'], label='D3r', pad=0.045)
    cx = MX + lw + 0.3
    C3, C5 = M['care']['Y3'], M['care']['Y5']
    rows2 = [['Care 연 요금', f"{C3['fee']}", f"{C5['fee']}"], ['정기 방문 원가', f"{C3['visits']:.1f}", f"{C5['visits']:.1f}"],
             ['고장 방문 원가', f"{C3['corrective']:.1f}", f"{C5['corrective']:.1f}"], ['Cloud · SW', f"{C3['cloud']:.0f}", f"{C5['cloud']:.0f}"],
             [('Care 원가 합계', {'bold': True}), f"{C3['cost']:.1f}", f"{C5['cost']:.1f}"], [('Care Margin', {'bold': True}), f"{C3['margin'] * 100:.0f}%", f"{C5['margin'] * 100:.0f}%"]]
    table(s, cx, y, lw, ['Care (만원/대 · 년)', 'Y3', 'Y5'], rows2, col_w=[lw - 1.5, 0.75, 0.75], size=9, align=['l', 'r', 'r'], label='D3c', pad=0.045)
    kx = cx + lw + 0.3
    cons = M['cons']
    rows3 = [[k, f"{p}", f"{n}", f"{p * n:.0f}"] for k, p, n in cons['kits']]
    rows3 += [[('List 합계', {'bold': True}), '', '', f"{cons['list_y']:.0f}"], ['구매율 반영 매출', '', '', f"{cons['rev']:.1f}"],
              ['원가 (35%)', '', '', f"{cons['cogs']:.1f}"], [('Contribution', {'bold': True}), '', '', f"{cons['contrib']:.1f}"]]
    table(s, kx, y, lw, ['Consumables (만원/년)', '단가', '횟수', '연'], rows3, col_w=[lw - 1.8, 0.6, 0.55, 0.65], size=9, align=['l', 'r', 'r', 'r'], label='D3k', pad=0.045)
    foot(s, 'D3')


def d4(prs):
    sc = M['scenarios']
    s, y = S(prs, 'D4', '5-Year Financial Model (3 Scenario)', sub='Bottom-up Driver: 채널별 설치 · Robot Attach · Rental 비중 · Care / 소모품 구매율 · Interface 표준부품 사용률. Y1~Y2 = Seed + TIPS 24개월, Y3~ = Series A 전제. 모두 TARGET / ASSUMPTION',
             visual='좌측 3 시나리오 표 (매출 · 매출총이익 · Contribution · Opex · 영업이익 · 누적현금 · 설치 · Robot · Installed Base), 우측 매출 막대 (시나리오별 Y1~Y5)', chart='표 + 묶은 막대',
             note=f"5개년 재무 모델입니다. 기준 시나리오의 5년차 매출은 {sc['B']['rev'][4] / 1e4:.1f}억원, 누적 현금 최저는 약 {sc['B']['min_cum_cash'] / 1e4:.0f}억원으로 Series A 이후 추가 투자가 필요한 구조입니다. 보수 시나리오 {sc['C']['rev'][4] / 1e4:.1f}억원, 상향 {sc['U']['rev'][4] / 1e4:.1f}억원이며 상향은 가격 인상 없이 파트너 물량과 원가 개선으로 차이가 납니다.")
    lw = 7.6
    rows = []
    for k, lab, fmt in [('rev', '매출', 1), ('gp', '매출총이익', 1), ('contrib', 'Contribution', 1), ('opex', 'Opex', 1), ('op', '영업이익 (근사)', 1),
                        ('cum_cash', '누적 현금', 1), ('kitchens', '설치 세대', 0), ('pl', 'Robot 설치', 0), ('base_end', 'Installed Robot', 0)]:
        for sk, sn in (('B', 'Base'),):
            L = sc[sk]
            vals = [f"{x / 1e4:.1f}" if fmt else f"{x:,.0f}" for x in L[k]]
            rows.append([(lab, {'bold': k in ('rev', 'op')})] + vals)
    rows.append([('OPERATE + EXPAND 비중', {})] + [f"{x * 100:.0f}%" for x in sc['B']['oe_share']])
    rows.append([('Conservative 매출 / 영업이익', {})] + [f"{a / 1e4:.1f} / {b / 1e4:.1f}" for a, b in zip(sc['C']['rev'], sc['C']['op'])])
    rows.append([('Upside 매출 / 영업이익', {})] + [f"{a / 1e4:.1f} / {b / 1e4:.1f}" for a, b in zip(sc['U']['rev'], sc['U']['op'])])
    table(s, MX, y, lw, ['Base (억원 · 세대 · 대)', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'], rows, col_w=[2.6, 1.0, 1.0, 1.0, 1.0, 1.0], size=9, align=['l'] + ['r'] * 5, label='D4', pad=0.045)
    rx = MX + lw + 0.3; rw = W - MX - rx
    text(s, rx, y, rw, 0.26, '매출 (억원)', size=10, bold=True, color=GREY)
    column_chart(s, rx, y + 0.3, rw, 3.6, ['Y1', 'Y2', 'Y3', 'Y4', 'Y5'],
                 [(n, [x / 1e4 for x in sc[k]['rev']]) for k, n in (('C', 'Conservative'), ('B', 'Base'), ('U', 'Upside'))],
                 ['C9CDD2', INK, ACC], show_labels=False, plot=(0.02, 0.08, 0.96, 0.8), size=9, gap=50, legend=True)
    mts(s, rx, y + 4.0, ['TARGET', 'ASSUMPTION'])
    text(s, rx, y + 4.25, rw, 0.7, f"손익분기 설치 물량 (Y5 단가 · 원가): 연 약 {M['breakeven_kitchens']:,.0f}세대 (DERIVED) · Series A 이후 2년 (Y3~Y4) 현금 소요 약 {M['post_seed_burn']['y3_y4'] / 1e4:.0f}억원",
         size=9, color=INK2, line=1.02)
    foot(s, 'D4')


def d5(prs):
    sh, scm = M['sens_household'], M['sens_company']
    s, y = S(prs, 'D5', 'Sensitivity', sub='왼쪽 = Remodeling 구매 1세대 5년 Contribution (만원, Y3 원가) · 오른쪽 = 회사 Y5 Contribution (억원). 불리 ↔ 유리. 전부 DERIVED',
             note='민감도 분석입니다. 한 세대 기준으로도, 회사 전체 기준으로도 가장 큰 변수는 고객 지불의사와 로봇 BOM입니다. 그다음이 파트너 물량, Retrofit 물량, 획득비용, 고장률입니다. 그래서 24개월 계획의 핵심 증거도 지불의사, BOM 견적, 설치와 서비스 원가 실측입니다.')
    lw = (CW - 0.4) / 2
    rows = [[d['name'], f"{d['lo']:+,.0f}", f"{d['hi']:+,.0f}"] for d in sh['items']]
    table(s, MX, y, lw, [f"1세대 5년 (기준 {sh['base']:,.0f}만원)", '불리', '유리'], rows, col_w=[lw - 1.7, 0.85, 0.85], size=9, align=['l', 'r', 'r'], label='D5h', pad=0.045)
    rows2 = [[d['name'], f"{d['lo'] / 1e4:+.1f}", f"{d['hi'] / 1e4:+.1f}"] for d in scm['items']]
    table(s, MX + lw + 0.4, y, lw, [f"회사 Y5 (기준 {scm['base'] / 1e4:.1f}억원)", '불리', '유리'], rows2, col_w=[lw - 1.7, 0.85, 0.85], size=9, align=['l', 'r', 'r'], label='D5c', pad=0.045)
    statement(s, MX, H - 1.3, CW, 'Top 2 변수 = Customer WTP · Robot BOM → 24개월 Evidence 우선순위: WTP (M18) · BOM 견적 (M18) · 설치 · 서비스 원가 실측 (M24)', size=10.5)
    foot(s, 'D5')


# ---------------------------------------------------------------- E: IP · risk · Q&A · memo
def e1(prs):
    rows = [[(a, {'bold': True}), f, i, d, r, (str(p), {'bold': True, 'color': ACC if p == 1 else T['text']}), t] for a, f, i, d, r, p, t in C.IP]
    tslide(prs, 'E1', 'IP Portfolio 상세 (출원 후보 · 등록 미정)', ['영역', '출원 후보 (Family)', '사업 중요도', '차별성', 'Prior Art Risk (참고)', '순위', '시점'], rows,
           [1.15, 4.0, 1.2, 0.9, 3.15, 0.5, 0.93], size=8.3, pad=0.04,
           sub=C.IP_PLAN,
           note='특허 후보 12개 묶음입니다. 1순위는 교체형 식품접촉 모듈과 Robot Home, 가전 기준점 기반 좌표 보정입니다. 식기 로봇과 주방 레일 로봇, 수납장 로봇 관련 선행특허가 있어 넓은 권리는 어렵고, 구체적인 구조와 방법 청구를 목표로 합니다. 등록 가능성은 단정하지 않습니다.')


def e2(prs):
    rows = [[(a, {'bold': True}), b, c, d, e] for a, b, c, d, e in C.RISKS]
    tslide(prs, 'E2', 'Risk Register: Risk → Evidence → 대응 → 중단 기준', ['구분', 'Risk', '확인 Evidence (시점)', '대응', '중단 · 재편 기준'], rows,
           [1.1, 3.2, 2.4, 3.1, 2.03], size=9, pad=0.05,
           sub='초기 자금의 목적 = 기술 · 사업 Risk를 측정 가능한 Evidence로 줄이는 것',
           note='주요 리스크와 확인 시점, 대응, 중단 기준입니다. 가장 큰 리스크는 자체 Hand의 우위, 주방 간 Transfer, 지불의사, 설치와 서비스 원가, 가정용 안전 기준입니다. 각 리스크는 6개월에서 24개월 사이의 Gate에서 측정 가능한 증거로 확인합니다.')


def _qa(prs, code, part, items, start_no):
    rows = [[(f"{start_no + i}", {'bold': True}), (q, {'bold': True}), a, ev, (wk, {'color': ACC})] for i, (q, a, ev, wk, where) in enumerate(items)]
    tslide(prs, code, f'투자심사 예상질문 · 방어논리 ({part}/3)', ['#', '질문', '방어논리', '근거 (Tag)', '약한 부분'], rows,
           [0.35, 1.85, 6.0, 2.05, 1.58], size=7.8, pad=0.035,
           sub='매우 비판적인 Seed VC · TIPS 운영사 관점. 답이 약한 항목은 본문 논리 보강 + 24개월 Evidence로 연결.',
           note='투자 심사에서 예상되는 질문과 방어 논리입니다. 각 질문마다 근거와 함께 아직 약한 부분을 그대로 적었습니다. 특히 지불의사, 원가 실측, 팀 정보가 가장 약한 부분입니다.')


def e3(prs): _qa(prs, 'E3', 1, C.QA[0:7], 1)
def e4(prs): _qa(prs, 'E4', 2, C.QA[7:14], 8)
def e5(prs): _qa(prs, 'E5', 3, C.QA[14:20], 15)


def e6(prs):
    s, y = S(prs, 'E6', '현재 부족한 Evidence · Founder 입력 필요 정보', sub='존재하지 않는 Evidence는 "없음"으로 표기. Founder 정보는 임의 작성하지 않음.',
             note='현재 부족한 증거와 Founder가 채워야 할 정보입니다. 고객, 계약, 파트너, 매출, 시제품 데이터는 모두 없음입니다. 팀 정보가 가장 먼저 필요하고, 그다음이 상용 Gripper로 만든 기술 기준선, 고객의 예약금 같은 행동 증거입니다.')
    lw = 7.3
    rows = [[(a, {'bold': True}), b, c, d] for a, b, c, d, _ in C.EVIDENCE]
    table(s, MX, y, lw, ['Evidence', '현재', '필요한 Evidence', '시점'], rows, col_w=[1.75, 1.75, 2.8, 1.0], size=7.8, label='E6a', pad=0.03)
    rx = MX + lw + 0.3; rw = W - MX - rx
    rows2 = [[(a, {'bold': True}), b] for a, b in C.FOUNDER_INPUTS]
    table(s, rx, y, rw, ['Founder 입력 필요', '내용'], rows2, col_w=[1.6, rw - 1.6], size=7.8, label='E6b', pad=0.03)
    foot(s, 'E6')


def e7(prs):
    s, y = S(prs, 'E7', f'투자심사 Memo: {C.VERDICT}', sub='본 판단은 자료 작성자의 반론 검토 의견 (실제 투자 결정 아님). 점수 1~5 (5 = 강한 Evidence).',
             visual='좌측 판단 (MEET) 근거 2블록 · 가운데 평가표 (현재 → M24) · 우측 판단을 바꿀 Evidence 5개', chart='표 + 목록',
             note='투자 심사역 관점에서 현재 자료만으로는 MEET, 즉 만나서 확인할 단계라고 판단합니다. 투자하지 않는 이유는 팀 정보, 기술 측정값, 고객 행동 증거가 없기 때문이고, 지켜보기만 하지 않는 이유는 문제 정의와 접근, 단계별 검증 구조, 자금 계획이 일관되기 때문입니다. 판단을 바꿀 증거는 다섯 가지입니다.')
    lw = 3.9
    rect(s, MX, y, lw, 0.9, fill=INK)
    text(s, MX + 0.2, y + 0.08, lw - 0.4, 0.3, '판단', size=10, bold=True, color='A9AEB5')
    text(s, MX + 0.2, y + 0.32, 1.4, 0.5, C.VERDICT, size=20, bold=True, color='FFFFFF')
    text(s, MX + 1.45, y + 0.42, lw - 1.65, 0.3, '(INVEST · MEET · WATCH · PASS 중)', size=9, color='A9AEB5')
    yy = y + 1.05
    for head_, items in C.VERDICT_WHY:
        text(s, MX, yy, lw, 0.26, head_, size=10, bold=True, color=GREY)
        hh = kit.text_h(items, 8.8, lw - 0.2, space_after=1) + 0.05
        text(s, MX, yy + 0.28, lw, hh, items, size=8.8, color=INK, bullet='–', space_after=1, line=1.0)
        yy += 0.28 + hh + 0.12
    cx = MX + lw + 0.3; cw = 3.9
    rows = [[a, f'{b}', f'{c}', d] for a, b, c, d in C.SCORE]
    table(s, cx, y, cw, ['항목', '현재', 'M24', '근거'], rows, col_w=[1.2, 0.5, 0.5, cw - 2.2], size=8.5, align=['l', 'c', 'c', 'l'], label='E7s', pad=0.04)
    rx = cx + cw + 0.3; rw = W - MX - rx
    text(s, rx, y, rw, 0.26, '판단을 바꿀 Evidence (최대 5)', size=10, bold=True, color=ACC)
    yy = y + 0.34
    for i, (a, b) in enumerate(C.CHANGE_EVIDENCE):
        hb = kit.text_h(b, 8.5, rw - 0.4) + 0.32
        rect(s, rx, yy, rw, hb, fill=SOFT)
        text(s, rx + 0.12, yy + 0.06, 0.3, 0.24, f'{i + 1}', size=10, bold=True, color=ACC)
        text(s, rx + 0.4, yy + 0.06, rw - 0.5, 0.24, a, size=9, bold=True)
        text(s, rx + 0.4, yy + 0.3, rw - 0.5, hb - 0.32, b, size=8.5, color=INK2, line=1.0)
        yy += hb + 0.08
    foot(s, 'E7')


# ---------------------------------------------------------------- F: reference
def f1(prs):
    cnt = {}
    for d in M['inputs']:
        cnt[d['tag']] = cnt.get(d['tag'], 0) + 1
    rows = [[TG('FACT'), '공식 통계 · 공개자료로 확인된 값', '총주택 2,018만호 · 가사노동 가치 582.4조원 · TIPS 8억원 · Robotiq 2F-85 약 $5,825', f"{cnt.get('FACT', 0)}개 입력"],
            [TG('DERIVED'), 'FACT 또는 가정으로 계산한 값', '아파트 약 1,328만호 · 1세대 5년 Contribution · Seed 범위 · 인시', '계산 전부'],
            [TG('ASSUMPTION'), '현재 사업가설 (검증 전)', 'Robot ASP 1,490만원 · BOM · Rental 월 33만원 · Premium 10% · 적용률 60%', f"{cnt.get('ASSUMPTION', 0)}개 입력"],
            [TG('TARGET'), '24개월 · 이후 목표', '가정 실증 ≥ 90% · Calibration ≤ 4시간 · 출원 5건 · 설치 물량', f"{cnt.get('TARGET', 0)}개 입력 + KPI"],
            [TG('CONCEPT'), '실물 없는 설계 개념', 'Adaptive Hand 렌더 · Robot Home · 주방 3D', '그림 · 도식'],
            [TG('TBV'), '검증 방법이 정해진 미확인 사실', '식세기 보급률 · 인증 적용 범위 · Founder 정보', '각주'],
            [TG('FUTURE'), '현재 없는 제품 · 기능', 'COOK · Robot Upgrade · Tool 확장', 'Roadmap']]
    tslide(prs, 'F1', 'Number Tag 원칙', ['Tag', '정의', '대표 예시', '적용'], rows, [1.45, 3.0, 5.6, 1.78], size=10,
           sub='모든 주요 숫자와 미검증 내용을 Tag로 구분. 전체 입력 · Tag · 출처: xlsx Inputs 시트 · docs/08_Tag_Register.md',
           takeaway='금지: 가상 고객 · 계약 · LOI · Partner · 매출 · 근거 없는 점유율 · "최초" · 근거 없는 ROI · 비용절감률 · 성능 · 특허 등록 확정 표현',
           note='모든 숫자는 FACT, DERIVED, ASSUMPTION, TARGET 중 하나의 Tag를 갖고, 그림과 미검증 내용은 CONCEPT, TO BE VALIDATED, FUTURE로 표시합니다.')


def _src_slide(prs, code, items, part, n):
    rows = [[(d['id'], {'bold': True}), d['item'], d['value'], d['source'].split(' , ')[0][:95]] for d in items]
    tslide(prs, code, f'Sources ({part}/{n})', ['ID', '항목', '값', '대표 URL (전체: docs/07)'], rows, [0.55, 2.6, 4.9, 3.78], size=7.2, pad=0.025,
           sub='조회일 2026-10-07~08 · 검색 결과 · 보도 인용 기준. 외부 제출 전 원문 대조 필요.',
           note='출처 목록입니다. 공식 통계와 회사 발표는 보도 인용이 많아 외부 제출 전 원문 대조가 필요합니다.')


def f2(prs):
    src = M['src']
    n = 4; k = (len(src) + n - 1) // n
    for i in range(n):
        _src_slide(prs, f'F{2 + i}', src[i * k:(i + 1) * k], i + 1, n)


ORDER = [idx, a1, a2, a2b, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, d1, d2, d3, d4, d5, e1, e2, e3, e4, e5, e6, e7, f1, f2]


def build(prs):
    common.APX['on'] = True
    try:
        for f in ORDER:
            f(prs)
    finally:
        common.APX['on'] = False; kit.XFORM['fn'] = None
