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
    ('B', '제품 · 기술', [('B1', 'Adaptive Hand 시험 계획 (Buy vs Build)'), ('B2', 'Kitchen Variation 근거: 확보 평면 5종'),
                        ('B3', 'Environment Interface 예: Robot Home'), ('B4', '대표 평면 적용 예 (구축 2Bay A)'),
                        ('B5', 'Safety · Certification 경로'), ('B6', 'Robot System BOM · Benchmark')]),
    ('C', '시장 · 경쟁', [('C1', 'Housing · 시장 통계 (FACT)'), ('C2', 'Remodeling · Rental · Care Reference'), ('C3', 'Market Sizing 산식 · 검증 계획'),
                       ('C4', '경쟁사 상세')]),
    ('D', '경제성 · 재무', [('D1', '가격 가설 (원가 · 시장 · 가치)'), ('D2', 'Household 5년 경제성 상세'), ('D3', 'Rental · Care · Consumables'),
                         ('D4', '5-Year Financial Model (3 Scenario)'), ('D5', 'Sensitivity')]),
    ('E', 'IP · 리스크', [('E1', 'IP Portfolio 상세'), ('E2', 'Risk Register')]),
    ('F', '출처', [('F1~F4', 'Sources (조회일 2026-10-07~08)')]),
]


def idx(prs):
    s = start(prs, 'xIDX', 'Index', 'Appendix 목차', visual='3열 목차 (A~F Section · Code · 제목)', chart='없음',
              note='- 부록 = 본문 18쪽의 근거 · 계산 · 검증 계획\n- A TIPS 과제 상세 · B 제품 · 기술 · C 시장 · 경쟁 · D 경제성 · 재무 · E IP · Risk · F 출처')
    y = head(s, 'APPENDIX', 'Appendix 목차',
             sub='본문 수치의 근거 · 계산 · 검증 계획 · 재무 수식 모델: MH_Robotics_Financial_Model.xlsx')
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
    text(s, MX, H - 1.0, CW, 0.3, [[('Tag  ', {'bold': True, 'color': INK}), ('FACT 공식 자료 · DERIVED 계산값 · ASSUMPTION 사업 가설 · TARGET 목표 · CONCEPT 설계 개념 · TBV 검증 예정 · FUTURE 향후 제품', {'color': INK2})]], size=9.5)
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
           sub='목표 근거 = 공개 Benchmark · 경제성 가정 · Benchmark 없는 지표 = 측정 후 설정',
           note='- Manipulation KPI: 식기 단위 성공률 목업 80% → 주방 3종 85% → 가정 90%\n- 공개 연구 식세기 적재 58.7% (참고) → 더 높은 목표 = 환경 Interface 효과 확인 지표\n- 복구율 등 비교 기준 없는 지표 = M12 측정 후 설정')


def a2(prs):
    tslide(prs, 'A2', '기술 KPI (2/3) · Application', ['KPI', '정의', 'Benchmark (출처)', 'M6', 'M12', 'M18', 'M24', '목표 근거', 'Tag'], _kpi_rows('Application'),
           [1.35, 2.0, 1.6, 0.85, 0.85, 1.0, 1.2, 1.95, 1.03], size=8.2, pad=0.04,
           sub='Application KPI = 설치 원가 가정 (인시)과 직접 연결 → Calibration · 설치 시간 단축 = Unit Economics 개선',
           note='- Application KPI: Calibration 4시간 · 설치 2인 1일 = 설치 원가 가정에서 역산한 목표\n- 주방 호환률 = 평면 30개 분석 · 상담 주방 실측으로 가정값 대체')


def a2b(prs):
    tslide(prs, 'A3', '기술 KPI (3/3) · Business', ['KPI', '정의', 'Benchmark (출처)', 'M6', 'M12', 'M18', 'M24', '목표 근거', 'Tag'], _kpi_rows('Business'),
           [1.35, 2.0, 1.6, 0.85, 0.85, 1.0, 1.2, 1.95, 1.03], size=8.2, pad=0.04,
           sub='Business KPI = 재무모델 가정 (BOM · 설치 · Care · 소모품 · WTP)의 실측 대체 지표',
           note='- Business KPI: BOM · 설치비 · A/S · Care 원가 = 가정 → 24개월 내 견적 · 실측으로 대체\n- 지불의사 = M18 조사 n ≥ 300 · 예약금 Test · 실증 3세대 유료 전환으로 확인')


def a3(prs):
    rows = [[(c, {'bold': True}), (n, {'bold': True}), per, goal, '\n'.join('· ' + x for x in items), out, kpi, who] for c, n, per, goal, items, out, kpi, who in C.WP]
    tslide(prs, 'A4', 'R&D Work Package 상세 (TIPS 과제)', ['WP', '이름', '기간', '목표', '주요 내용', '산출물', 'KPI', '담당 (채용 계획)'], rows,
           [0.5, 1.45, 0.75, 1.65, 3.2, 1.6, 1.5, 1.18], size=8, pad=0.045,
           sub='TIPS 과제 = 기술 검증 (Technology De-risking) · WP6 실증 = 목업 → 주방 3종 → 가정 3세대 · 담당 = 채용 계획 기준',
           note='- WP 6개: 목표 · 내용 · 산출물 · KPI\n- Hand = 상용 Gripper 비교 → v1~v3 개선 · Skill = Template화 → 주방마다 재사용\n- Calibration = 새 주방 4시간 · Interface = 필요한 곳만 표준화 · 안전 = 표준 Gap · 사전시험\n- WP6 = 목업 → 주방 3종 → 가정 3세대 실증')


def a4(prs):
    rows = [[(g, {'bold': True, 'color': ACC}), ev, ok, ng] for g, ev, ok, ng in C.GATES]
    tslide(prs, 'A5', 'Gate · 중단 기준 (24개월)', ['Gate', '확인할 Evidence', '통과 기준 (TARGET)', '미달 시 조치'], rows, [0.8, 4.6, 3.3, 3.13], size=9.5,
           sub='기업가치를 바꾸는 Evidence 중심 Gate · 기준 미달 시 구조 변경 · 범위 축소 · Scale 보류',
           takeaway='Series A 판단 = 기술 성공 + 유료 전환 + 설치 · 서비스 원가 실측 (M24) · 기준 미달 시 Bridge 또는 범위 축소 후 재검증',
           note='- 6개월 단위 Gate\n- M6 자체 Hand 우위 없음 → 상용 Gripper 전환\n- M12 목업 80% · M18 주방 3종 Transfer · WTP · M24 가정 실증 · 유료 전환 · 원가 실측 = Series A 조건')


def a5(prs):
    s, y = S(prs, 'A6', 'TIPS 과제 편성 · 24개월 사용처 (Base)', sub=f"TIPS 과제 총 {TP['total'] / 10000:.2f}억원 = 정부 8억원 (75%) + 기관부담 {TP['private'] / 10000:.2f}억원 · 회사 전체 24개월 지출 {F['spend_total'] / 10000:.1f}억원 중 일부 (금액 ASSUMPTION · 규정 FACT)",
             note=f"- TIPS 과제 예산 + 회사 전체 24개월 지출 비교\n- 과제 총액 = 정부 8억원 ÷ 75% = 약 {TP['total'] / 10000:.2f}억원 · 기관부담 {TP['private'] / 10000:.2f}억원 (현물 = Founder 인건비 참여분 · 현금 = Seed)\n- 우측 = 24개월 전체 사용처 (TIPS 편성분 · Seed 부담분 구분)")
    lw = 5.4
    rows = [[r['cat'], (kit.nf(r['y1']), {}), (kit.nf(r['y2']), {}), (kit.nf(r['total']), {'bold': True}), r['kind']] for r in TP['rows']]
    rows.append([('합계', {'bold': True}), f"{TP['year_total'][0]:,.0f}", f"{TP['year_total'][1]:,.0f}", (f"{TP['total']:,.0f}", {'bold': True}), ''])
    th = table(s, MX, y, lw, ['TIPS 비목 (만원)', '1차년도', '2차년도', '합계', '구분'], rows, col_w=[1.75, 0.9, 0.9, 1.0, 0.85], size=9,
               align=['l', 'r', 'r', 'r', 'c'], label='A6p', pad=0.05)
    chk = [['정부지원 (75%)', f"{TP['gov']:,.0f}", 'FACT 상한'], ['기관부담 현금', f"{TP['private_cash']:,.0f}", f"≥ 10% 충족 ({TP['private_cash'] / TP['private'] * 100:.0f}%)"],
           ['기관부담 현물', f"{TP['inkind']:,.0f}", 'Founder 참여분'], ['간접비율 (현금 직접비 대비)', f"{TP['indirect_rate'] * 100:.1f}%", '협약 기준 적용']]
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
           sub=f"Founder 2인 = TIPS 창업팀 요건 기준 · 연 인건비 = 연봉 × 1.2 (4대보험 · 퇴직급여) · 평균 FTE {F['fte'][0]:.1f} → {F['fte'][1]:.1f} · 24개월 차 약 {F['heads_m24']:.0f}명",
           note='- 리드 3명 (조작 · 인식 · Hand) 우선 채용 · 사업개발 M7 · 설치 엔지니어 M13\n- Lean안: Hand 센싱 · Skill/Data · 현장 Technician 제외 · 시험 인력 M19로 연기\n- 연봉 = 평균 가정 → 실제 채용 조건으로 대체')


# ---------------------------------------------------------------- B: product · technology
def b1(prs):
    rows = [list(r) for r in C.HAND_TEST]
    tslide(prs, 'B1', 'Adaptive Hand 시험 계획 (Buy vs Build)', ['항목', '내용', 'Tag'], [[(a, {'bold': True}), b, TG(c.split(' ')[0]) if c.split(' ')[0] in kit.TAGS else c] for a, b, c in rows],
           [1.7, 8.75, 1.38], size=9.5,
           sub='상용 Gripper 기준선 → 30종 식기 세트 비교 → 자체 Hand 개발 범위 결정 (WP1)',
           takeaway='자체 Hand 채택 조건 = Coverage +15%p 또는 Tool 교체 50% 감소 · 미달 시 Buy 전환 → 교체형 Pad · Skill 집중',
           note='- M6 자체 Hand 필요 여부 판정\n- 30종 세트 (접시 · 그릇 · 컵 · 유리잔 · 수저 · 뚜껑 · 도구) · 젖은 조건 · 식세기 랙 조건 시험\n- 비교군: 상용 Gripper · 흡착 · Soft Finger\n- 식품 접촉 부품 = 식품위생법 기구 기준 · 고무제 규격 대응')


def _var_thumbs(s, y, hmax, legend_w=2.15):
    """확보 평면 4종 평면도 썸네일 (동일 축척 · 주방/식당 음영) + 범례. Returns the bottom y."""
    from PIL import Image
    from pptx.util import Inches
    items = [('old2a', '구축 2Bay A'), ('old2b', '구축 2Bay B'), ('new3', '신축 3Bay'), ('new4', '신축 4Bay')]
    size_ = {p[0]: p[2] for p in C.PLANS}
    rd = os.path.join(common.ROOT, 'assets', 'renders')
    px = {pid: Image.open(os.path.join(rd, f'fig_var_top_{pid}.png')).size for pid, _ in items}
    js = {pid: json.load(open(os.path.join(rd, f'fig_var_top_{pid}.json'), encoding='utf-8')) for pid, _ in items}
    assert len({j['px_per_cm'] for j in js.values()}) == 1          # one scale for all thumbnails
    k = hmax / max(h for _, h in px.values())                        # slide inch per image px
    gap = (CW - legend_w - sum(w_ for w_, _ in px.values()) * k) / len(items)
    x = MX; yb = y + hmax
    for pid, name in items:
        w, h = px[pid][0] * k, px[pid][1] * k
        at = render(s, 'fig_var_top_' + pid, x, yb - h, w, h)
        pts = [at(tuple(p)) for p in js[pid]['kitchen']]
        ff = s.shapes.build_freeform(round(pts[0][0] * 1000), round(pts[0][1] * 1000), scale=Inches(1) / 1000)
        ff.add_line_segments([(round(px_ * 1000), round(py_ * 1000)) for px_, py_ in pts[1:]], close=True)
        sh = ff.convert_to_shape(0, 0)
        sh.fill.solid(); sh.fill.fore_color.rgb = kit._rgb(INK); kit.alpha(sh, 16)
        sh.line.color.rgb = kit._rgb(INK); sh.line.width = kit.Pt(1.0)
        kit._nostyle(sh)
        text(s, x, yb + 0.06, w, 0.36, [[(name, {'bold': True})], [(size_[name] + 'mm', {'size': 8, 'color': INK2})]], size=8.5,
             label='B2cap ' + name)
        x += w + gap
    lx = W - MX - legend_w
    kit.alpha(rect(s, lx, yb - 0.6, 0.26, 0.16, fill=INK, line=INK, lw=1.0), 16)
    text(s, lx + 0.36, yb - 0.63, legend_w - 0.36, 0.22, '주방 · 식당', size=8.5, color=INK2, check=False)
    text(s, lx, yb - 0.32, legend_w, 0.36, '확보 평면 재작도 (단지명 미표기)\n4종 동일 축척 · 신축 2Bay = 3D 미착수', size=8, color=GREY, line=1.05)
    return yb + 0.42


def b2(prs):
    s, y = S(prs, 'B2', 'Kitchen Variation 근거: 확보 평면 5종', sub='제공 도면 치수선 기준 재작도 · 표본 5종 → 평면 30개 분석으로 확대 (M6, TARGET)',
             visual='표 (평면 · 구분 · 크기 · 주방 형태 · 3D · 기본 배치) + 결론 띠 + 하단 평면도 썸네일 4장 (확보 평면 재작도 · 동일 축척 · 주방/식당 음영 · 평면명 · 크기 캡션) + 범례',
             chart='표 + 평면도 4 (확보 평면 재작도)',
             note='- 확보 평면 5종: 구축 2Bay A 1종만 기본 한 줄 배치 수용 · 3종 싱크 줄 2.6~2.8m · 1종 미검토\n- 주방마다 다른 환경의 실제 예 → Retrofit · 짧은 벽용 Compact 구성 개발 필요\n- 표본 작음 → 평면 30개 분석으로 확대 (M6)')
    rows = [list(r) for r in C.PLANS]
    th = table(s, MX, y, CW, ['평면', '구분', '크기 (mm)', '주방 형태', '디지털화 (3D)', '기본 배치 (Remodeling 한 줄)'], rows,
               col_w=[1.25, 1.85, 1.35, 3.0, 1.6, 2.78], size=9.5, header_size=9.5, label='B2', max_h=H - y - 1.25)
    sy = min(y + th + 0.16, H - 1.2)
    sh = statement(s, MX, sy, CW, '5종 모두 싱크 · 조리기구가 다른 벽 → 로봇 구역 분리 가능 · 3종 싱크 줄 2.6~2.8m → 짧은 벽용 Compact 구성 필요 (Kitchen Compatibility KPI)', size=11)
    ty = sy + sh + 0.28
    _var_thumbs(s, ty, H - 0.6 - 0.42 - ty)
    foot(s, 'B2')


def b3(prs):
    s, y = S(prs, 'B3', 'Environment Interface 예: Robot Home 보관 · 전개 (Remodeling)', sub='평소 Robot Home에 접힌 상태 → 문 열림 → Rail로 전개 · 식세기 하단 랙 = 당겨서 위에서 적재 (3D 충돌검사, CONCEPT)',
             visual='3D 콘셉트 렌더 5컷: ① 문 닫힘 ② 문 열림 ③ 전개 ④ Rail 이동 ⑤ 하단 랙 적재 (낮은 작업점)', chart='3D 렌더 5컷',
             note='- Remodeling 채널 Interface 예: 조리대 끝 Robot Home에 접힌 상태 → 문 열림 → 전개 → Rail 이동\n- 낮은 작업점 (식세기 하단 랙) = 랙을 당겨 위에서 적재\n- 3D 모델 기준 보관 · 전개 · 이동 경로 충돌검사 · 실제 기구 검증 예정')
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
    s, y = S(prs, 'B4', '대표 평면 적용 예: 구축 2Bay A (CONCEPT)', sub='제공 도면 (12,390 × 11,670mm, 코어 포함) 치수선 기준 3D화 · 왼쪽 원래 주방 · 오른쪽 MH Interface 적용',
             visual='평면도 2장 (원래 ㄱ자 주방 / Interface 적용 후) + 변경 사항 표', chart='평면도 2 + 표',
             note='- 대표 평면 1종에 Remodeling 방식 Interface 적용 예\n- 원래 ㄱ자 주방 윗벽 = 로봇 작업 줄 · 인덕션 = 옆벽 이동\n- 보관함 문 최대 90° (옆벽) 조건에서 보관 · 전개 · 이동 경로 재검사')
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


def _tech_wrap(txt, w, size=9):
    """Line breaks only at top-level ' · ' / ': ' separators (not inside parentheses) for a cell `w` inches wide."""
    parts, depth, buf, i = [], 0, '', 0
    while i < len(txt):
        sep = next((d for d in (' · ', ': ') if txt.startswith(d, i)), None) if depth == 0 else None
        if sep: parts.append((buf, sep)); buf = ''; i += len(sep); continue
        depth += {'(': 1, ')': -1}.get(txt[i], 0); buf += txt[i]; i += 1
    parts.append((buf, ''))
    lines, cur, prev = [], '', ''
    for p, sep in parts:
        cand = p if not cur else cur + prev + p
        if cur and kit.text_w(cand, size, False) > w: lines.append(cur + prev.rstrip()); cur = p
        else: cur = cand
        prev = sep
    return '\n'.join(lines + [cur])


def _tech_legend(s, x, y, kind, label, desc):
    """B5 legend row: swatch (robot = 주황 반투명 · human = 회색 점선 · nogo = 빗금) + 굵은 이름 + 설명."""
    from pptx.enum.dml import MSO_PATTERN_TYPE
    if kind == 'robot':
        kit.alpha(rect(s, x, y + 0.04, 0.3, 0.16, fill=ACC, line=ACC, lw=1.0), 40)
    elif kind == 'human':
        rect(s, x, y + 0.04, 0.3, 0.16, fill='DADDE1')
        kit.dashed_rect(s, x, y + 0.04, 0.3, 0.16, color=INK2, lw=1.0)
    else:
        sh = rect(s, x, y + 0.04, 0.3, 0.16, line=INK, lw=1.0)
        sh.fill.patterned(); sh.fill.pattern = MSO_PATTERN_TYPE.WIDE_UPWARD_DIAGONAL
        sh.fill.fore_color.rgb = kit._rgb(INK2); sh.fill.back_color.rgb = kit._rgb('FFFFFF')
    text(s, x + 0.4, y, 3.4, 0.24, [[(label + '  ', {'bold': True, 'color': INK}), (desc, {'color': INK2})]], size=8.5,
         anchor='m', label='B5leg ' + label)


def _tech_zones(s, x, y, w, h):
    """B5 figure: 위에서 본 주방 Zoning (3D 콘셉트) · 주황 = Robot Zone · 회색 점선 = Human Zone · 빗금 = No-go (조리기구)."""
    rect(s, x, y, w, h, fill=SOFT)
    at = render(s, 'fig_tech_b5_zones', x, y, w, h, bg=(244, 245, 246))
    mt(s, x + 0.05, y + 0.05, 'CONCEPT', size=5.5, h=0.14, fill='FFFFFF')
    return at


def b5(prs):
    s, y = S(prs, 'B5', 'Safety · Certification 경로', sub='가정용 로봇 기준 발행 전 (IEC 63682 초안) → 인증기관 사전상담으로 경로 우선 확정 (WP5)',
             visual='좌측 표 (항목 · 내용 · Tag · 출처, 7행) + 우측 위에서 본 주방 Zoning 3D 콘셉트 그림 (CONCEPT): 주황 = Robot Zone (조리대 한 줄) · 회색 점선 = Human Zone · 빗금 = No-go (조리기구 구역) + 범례 3줄. 하단 결론 띠.',
             chart='표 + Zoning 콘셉트 그림 1개 (CONCEPT) + 범례',
             note='- 협동로봇 기준 ISO 10218 (2025) 감속 · 접촉력 = 최소선\n- 가정용 IEC 63682 = 초안 → Gap 분석으로 반영\n- M9 인증기관 사전상담 · M18 전기 · EMC 사전시험\n'
                  '- Zoning 그림: Robot Zone = 조리대 한 줄 · 사람 동선 = Human Zone (진입 시 감속 · 정지) · 조리기구 구역 = No-go (MH 안전 원칙, CONCEPT)')
    cw = [1.08, 5.49, 0.8, 0.88]
    rows = [[a, _tech_wrap(b, cw[1] - 0.4), TG(t), src] for a, b, t, src in C.SAFETY]
    lw = sum(cw); fx = MX + lw + 0.3; fw = W - MX - fx
    th = table(s, MX, y, lw, ['항목', '내용', 'Tag', '출처'], rows, col_w=cw, size=9, header_size=9, label='B5', pad=0.05)
    text(s, fx, y + 0.02, fw, 0.24, 'MH 안전 원칙: Zoning 예', size=9.5, bold=True, color=GREY)
    lg = 3 * 0.26
    fh = max(th - 0.32 - lg - 0.08, 2.2)
    _tech_zones(s, fx, y + 0.32, fw, fh)
    ly = y + 0.32 + fh + 0.1
    for i, (k, lab, d) in enumerate([('robot', 'Robot Zone', '조리대 한 줄 · Robot 작업 범위'), ('human', 'Human Zone', '사람 동선 · 진입 시 감속 · 정지'),
                                     ('nogo', 'No-go', '조리기구 구역 · Robot 진입 금지')]):
        _tech_legend(s, fx, ly + i * 0.26, k, lab, d)
    sy = max(y + th, ly + lg) + 0.18
    statement(s, MX, sy, CW, '안전 설계 = 기준 발행 전 착수: 협동로봇 기준 (감속 · 접촉력) = 최소선 · 가정용 초안 요구 = Gap 분석 반영', size=11)
    foot(s, 'B5')


def b6(prs):
    s, y = S(prs, 'B6', 'Robot System BOM · Component Benchmark', sub='Benchmark = 공개 판매가 (FACT, 환율 1,400원/USD ASSUMPTION) · BOM = ASSUMPTION (재무모델 Base BOM과 합계 일치)',
             visual='좌측 공개가 Benchmark 표, 우측 BOM Pilot · Y3 · Y5 표 (Adaptive Hand 포함)', chart='표 2개',
             note=f"- Robot System 원가 = 공개가 부품 기준 추정\n- BOM Y1 시제품 {AV('bom')[0]:,}만원 → Y3 {AV('bom')[2]:,}만원 → Y5 {AV('bom')[4]:,}만원 (가정)\n- 최대 항목 = Arm · 자체 Hand = 상용 Gripper보다 낮은 목표 원가")
    bm = [list(r) for r in C.BENCH]
    lw = 5.3
    table(s, MX, y, lw, ['Benchmark (FACT)', 'USD', '만원'], bm, col_w=[2.9, 1.3, 1.1], size=9.5, align=['l', 'r', 'r'], label='B6b')
    rx = MX + lw + 0.3; rw = W - MX - rx
    rows = [[r[0], f"{r[1]:,}", f"{r[2]:,}", f"{r[3]:,}"] for r in M['bom_breakdown']]
    tot = [sum(r[i] for r in M['bom_breakdown']) for i in (1, 2, 3)]
    rows.append([('합계 (재무모델 BOM)', {'bold': True}), (f"{tot[0]:,}", {'bold': True}), (f"{tot[1]:,}", {'bold': True}), (f"{tot[2]:,}", {'bold': True, 'color': ACC})])
    table(s, rx, y, rw, ['BOM (ASSUMPTION, 만원/대)', 'Y1 시제품', 'Y3', 'Y5'], rows, col_w=[rw - 2.25, 0.75, 0.75, 0.75], size=9, align=['l', 'r', 'r', 'r'], label='B6m')
    statement(s, MX, 5.95, CW, 'BOM 하락 경로 = 수량 + Arm OEM Partner (국산 · 중국산 Cobot) + 자체 Hand 원가 설계 · Y5 Arm 450만원 = 공격적 가정 → 민감도 2순위 (D5)', size=10.5)
    foot(s, 'B6')


# ---------------------------------------------------------------- C: market · competition
def c1(prs):
    rows = [[a, b, TG(t), src] for a, b, t, src in C.HOUSING]
    tslide(prs, 'C1', 'Housing · 시장 통계', ['항목', '값', 'Tag', '출처 / 산식'], rows, [3.3, 3.2, 1.2, 4.13], size=9.5,
           sub='출처: 국가데이터처 · 국토부 · 부동산원 · 부동산114 (2026.10 기준)',
           note='- 주택 통계: 국가데이터처 2025 인구주택총조사 · 국토부 주택통계\n- 문제 크기: 2024 가계생산 위성계정 무급 가사노동 가치\n- 주방 교체 세대 수 = 공식 통계 없음 → 두 방법 교차 추정 (ASSUMPTION)')


def c2(prs):
    rows = [[a, b, TG(t), n] for a, b, t, n in C.REFS]
    tslide(prs, 'C2', 'Remodeling · Rental · Care Reference', ['항목', '값', 'Tag', '비고'], rows, [3.0, 4.6, 1.2, 3.03], size=9.5,
           sub='렌탈 · 방문관리 · 빌트인 통합 수요 = 공개 실적으로 확인 (FACT) · 로봇 Integration 지불 여부 = 별개 → WTP 조사',
           note='- 주방 리모델링 · 렌탈 · 관리 서비스 참고 자료\n- 렌탈 · 정기관리 수요 = 코웨이 · LG 실적으로 확인 (FACT)\n- 로봇에 대한 같은 지불 여부 = 별개 → WTP 조사')


def c3(prs):
    mk = M['market']['B']
    s, y = S(prs, 'C3', 'Market Sizing 산식 · 검증 계획', sub='세대 수 × 적용률 × 단가 · 핵심 비율 = ASSUMPTION → 검증 방법 · 시점 지정',
             note=f"- 본문 시장 산식 · 가정 전체\n- Remodeling · Retrofit · 신축 대상 시장 = 연 약 {M['market']['B']['sam']:,.0f}억원 · Y5 계획 매출 {M['market']['B']['som']:.1f}억원 = 대상 세대의 약 {M['market']['B']['som_share_hh'] * 100:.1f}%\n- 각 비율 → M6~M24 견적 · 평면 분석 · 소비자 조사 · 실증 Data로 대체")
    rows = [['① Remodeling', '30만 × 10% × 60%', f"{mk['fit'] * 1000:,.0f}세대/년", f"{kit.nf(mk['pkg_remodel'])}만원 (Interface 450 + Attach 85% × 1,570)", f"{mk['sam_remodel']:,.0f}억원"],
            ['② Retrofit', f"1,328만 × 10% × 60% × 40% = {mk['retro_pool'] / 10:.1f}만 × 0.5%", f"{mk['retro_annual'] * 1000:,.0f}세대/년", f"{mk['pkg_retro']:,.0f}만원 (Kit 150 + 1,490 + 120)", f"{mk['sam_retro']:,.0f}억원"],
            ['③ New-build', '20만 × 15% × 10%', f"{mk['new_opt'] * 1000:,.0f}세대/년", f"{kit.nf(mk['pkg_new'])}만원 (Option 220 + 25% × 1,570)", f"{mk['sam_new']:,.0f}억원"],
            ['④ Recurring', f"Installed Base × ARPU {mk['arpu']:.1f}만원 (Care 70% × 48 + 소모품 70% × 36)", '1,000대', '-', f"{mk['recurring_per_1000']:.1f}억원/1,000대"],
            [('SAM (① + ② + ③)', {'bold': True}), '', '', '', (f"{mk['sam']:,.0f}억원", {'bold': True})],
            [('Y5 계획 매출 (Base · TARGET)', {'bold': True}), f"{mk['som_hh']:,.0f}세대 · 대상의 {mk['som_share_hh'] * 100:.1f}%", '', '', (f"{mk['som']:.1f}억원", {'bold': True, 'color': ACC})]]
    th = table(s, MX, y, CW, ['시장', '산식', '대상', '패키지 단가', '연 규모'], rows, col_w=[1.7, 4.3, 1.4, 3.0, 1.43], size=9, align=['l', 'l', 'r', 'l', 'r'], label='C3a', pad=0.05)
    rows2 = [[a, b, c, d] for a, b, c, d in C.MKT_VALID]
    table(s, MX, y + th + 0.2, CW, ['가정', 'Tag', '검증 방법', '시점'], rows2, col_w=[4.2, 2.0, 4.6, 1.03], size=9, label='C3b', pad=0.05)
    foot(s, 'C3')


def c4(prs):
    rows = [[(n, {'bold': True}), k, d, p, ap, f'[{src}]'] for n, k, d, p, ap, src in C.COMP]
    tslide(prs, 'C4', '경쟁사 상세 (공개 자료)', ['Player', '구분', '공개 내용', '가격 · 상태', '접근', '출처'], rows, [1.9, 1.5, 3.1, 2.75, 1.7, 0.88], size=8.8, pad=0.045,
           sub='공개 보도 · 회사 발표 기준 · 성능 비교 Data 비공개 → 접근 방식 비교',
           takeaway='MH의 차이 = 고정형 Kitchen System (Hand · Skill · Calibration · Interface · Care) · 우위 = 재배치 시간 · 원가 · 유료 전환으로 입증 예정',
           note='- Humanoid · 이동형 = 설치 불필요 범용 접근 · 조리 로봇 = 전용 주방 · 조리대 기기 · Cobot · Gripper = 부품\n- 가구사 로봇 협업 보도 없음 (2026)\n- MH 우위 = 미검증 → 실증 Data로 입증 필요')


# ---------------------------------------------------------------- D: economics
def d1(prs):
    rows = [[(a, {'bold': True}), (b, {'bold': True}), c, d, e] for a, b, c, d, e in C.PRICE]
    tslide(prs, 'D1', '가격 가설: 원가 Floor · 시장 Reference · 가치 Anchor', ['항목', '가격 가설 (VAT 별도)', '원가 Floor (ASSUMPTION 기반)', '시장 Reference (FACT)', '가치 Anchor'], rows,
           [2.1, 1.6, 2.8, 3.3, 2.03], size=9, pad=0.05,
           sub='가격 범위 산정 → WTP 검증 · 모든 가격 = ASSUMPTION',
           takeaway=f"가치 Gap: CLEAN만의 가사 대체 가치 (월 약 {M['value']['value']:.0f}만원) < Rental 월 {AV('p_rent')}만원 → Premium 고객 · ASSIST 확장 · 위생 · 편의 가치로 검증 (WTP M18)",
           note=f"- 가격 범위 = 원가 하한 · 시장 참고가 · 고객 가치 3방향\n- CLEAN 단독 가사대체 가치 월 약 {M['value']['value']:.0f}만원 < Rental 요금 → 가치 Gap\n- Premium 고객부터 · ASSIST 확장 · 위생 · 편의 가치 묶음으로 지불의사 확인")


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
            r_('Skill · Tool 원가', lambda h: f"{h['C']['sw'] + h['C']['tool']:,.0f}"),
            r_('서비스 원가 (Care · 소모품 · Warranty)', lambda h: f"{h['service_cost5']:,.0f}"),
            r_('Rental 금융비용', lambda h: f"{h['C'].get('finance', 0):,.0f}"),
            r_('채널비용 (획득 · Partner · 수주)', lambda h: f"{h['C']['channel']:,.0f}"),
            r_('5년 매출총이익 (채널 전)', lambda h: f"{h['gp5']:,.0f}", True),
            r_('5년 Lifetime Contribution', lambda h: f"{h['contrib5']:,.0f}", True, ACC),
            r_('Contribution Margin', lambda h: f"{h['cm5'] * 100:.1f}%")]
    tslide(prs, 'D2', 'Household 5년 경제성 상세 (1세대 · 만원 · Base)', ['항목'] + [l for _, l in keys], rows, [3.15] + [1.445] * 6, size=9,
           align=['l'] + ['r'] * 6, pad=0.05,
           sub='구매 = Care 가입 세대 기준 · Skill · Tool = 구매율 반영 기대값 · Y3 / Y5 = 해당 연도 원가 수준 5년 적용 · 전부 DERIVED (from ASSUMPTION)',
           takeaway='매출보다 서비스 원가 · BOM에 민감: Y3 → Y5 원가 개선 (BOM · 설치 · 방문)만으로 Contribution 약 2배',
           note=f"- 대표 1세대 5년: Remodeling 구매 설치 시점 {M['household']['purchase_direct_Y3']['y0']:,.0f}만원 · 5년 매출 {M['household']['purchase_direct_Y3']['rev5']:,.0f}만원\n- 기여이익 {M['household']['purchase_direct_Y3']['contrib5']:,.0f}만원 (Y3 원가) → {M['household']['purchase_direct_Y5']['contrib5']:,.0f}만원 (Y5 원가)\n- Retrofit = Partner 수수료 · 현장 Calibration 비용으로 낮음 · 신축 = 세대당 수주비용 작아 높음")


def d3(prs):
    s, y = S(prs, 'D3', 'Rental · Care · Consumables 단위 경제성 (Base)', sub='Rental = 초기 부담 완화 수단 (Pilot = MH 직접 · Scale = Partner 자산) · Care = Robot Lifecycle Maintenance · 모두 DERIVED (from ASSUMPTION)',
             note=f"- Rental 월 {AV('p_rent')}만원 (Care · Grip Kit 포함) · Y3 월 원가 약 {M['rental']['Y3']['cost_m']:.1f}만원 · 회수 약 {M['rental']['Y3']['payback']:.0f}개월\n- Scale = Partner 자산 보유 · MH 서비스료 월 {AV('partner_fee'):.0f}만원 · Partner IRR 약 {M['partner_irr']['B']['irr_y'] * 100:.0f}%\n- Partner 단순 회수 약 {M['partner_irr']['B']['payback']:.0f}개월 > 요구 {M['partner_irr']['B']['hurdle']}개월 (가정) → 매입가율 · 서비스료 · 기간 협의\n- Care 마진 Y3 {M['care']['Y3']['margin'] * 100:.0f}% → Y5 {M['care']['Y5']['margin'] * 100:.0f}%")
    lw = (CW - 0.6) / 3
    R3, R5 = M['rental']['Y3'], M['rental']['Y5']
    rows = [['감가 (잔존 15%)', f"{R3['lines']['dep']:.1f}", f"{R5['lines']['dep']:.1f}"], ['금융비용', f"{R3['lines']['fin']:.1f}", f"{R5['lines']['fin']:.1f}"],
            ['Care 원가', f"{R3['lines']['care']:.1f}", f"{R5['lines']['care']:.1f}"], ['Grip Kit 원가', f"{R3['lines']['grip']:.1f}", f"{R5['lines']['grip']:.1f}"],
            ['Failure Reserve', f"{R3['lines']['reserve']:.1f}", f"{R5['lines']['reserve']:.1f}"], [('월 원가 합계', {'bold': True}), f"{R3['cost_m']:.1f}", f"{R5['cost_m']:.1f}"],
            ['월 요금 (가정)', f"{R3['fee']:.0f}", f"{R5['fee']:.0f}"], [('월 Contribution', {'bold': True}), f"{R3['contrib_m']:.1f}", f"{R5['contrib_m']:.1f}"],
            ['Payback (개월)', f"{R3['payback']:.1f}", f"{R5['payback']:.1f}"], ['Partner IRR (연)', f"{M['partner_irr']['B']['irr_y'] * 100:.1f}%", ''],
            ['Partner 단순 회수 / 요구', f"{M['partner_irr']['B']['payback']:.0f} / {M['partner_irr']['B']['hurdle']}개월", '']]
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
    s, y = S(prs, 'D4', '5-Year Financial Model (3 Scenario)', sub='Bottom-up Driver: 채널별 설치 · Robot Attach · Rental 비중 · Care / 소모품 구매율 · Interface 표준부품 사용률 · Y1~Y2 = Seed + TIPS 24개월 · Y3~ = Series A 전제 · 모두 TARGET / ASSUMPTION',
             visual='좌측 3 시나리오 표 (매출 · 매출총이익 · Contribution · Opex · 영업이익 · 누적현금 · 설치 · Robot · Installed Base), 우측 매출 막대 (시나리오별 Y1~Y5)', chart='표 + 묶은 막대',
             note=f"- Base Y5 매출 {sc['B']['rev'][4] / 1e4:.1f}억원 · 누적 현금 최저 약 {sc['B']['min_cum_cash'] / 1e4:.0f}억원 → Series A 이후 추가 투자 필요 구조\n- Conservative {sc['C']['rev'][4] / 1e4:.1f}억원 · Upside {sc['U']['rev'][4] / 1e4:.1f}억원 (가격 인상 없이 Partner 물량 · 원가 개선 차이)")
    lw = 7.6
    rows = []
    for k, lab, fmt in [('rev', '매출', 1), ('gp', '매출총이익', 1), ('contrib', 'Contribution', 1), ('opex', 'Opex', 1), ('op', '영업이익 (근사)', 1),
                        ('cum_cash', '누적 현금', 1), ('kitchens', '설치 세대', 0), ('pl', 'Robot 설치', 0), ('base_end', 'Installed Robot', 0)]:
        for sk, sn in (('B', 'Base'),):
            L = sc[sk]
            vals = [f"{x / 1e4:.1f}" if fmt else kit.nf(x) for x in L[k]]
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
    s, y = S(prs, 'D5', 'Sensitivity', sub='왼쪽 = Remodeling 구매 1세대 5년 Contribution (만원, Y3 원가) · 오른쪽 = 회사 Y5 Contribution (억원). 불리 ↔ 유리 · 전부 DERIVED',
             note='- 1세대 · 회사 기준 모두 최대 변수 = 고객 지불의사 · Robot BOM\n- 회사 기준 다음 순위 = Partner 경유 Remodeling · Retrofit 물량 · Robot Attach Rate · Rental 비중 · Failure Rate\n- 24개월 핵심 Evidence = WTP · BOM 견적 · 설치 · 서비스 원가 실측')
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
           note='- 특허 후보 12개 묶음\n- 1순위: 교체형 식품접촉 Module · 가전 기준점 기반 좌표 Calibration (Robot Home = 2순위)\n- 식기 로봇 · 주방 Rail · 수납장 로봇 선행특허 존재 → 구체적인 구조 · 방법 청구\n- 등록 가능성 미정')


def e2(prs):
    rows = [[(a, {'bold': True}), b, c, d, e] for a, b, c, d, e in C.RISKS]
    tslide(prs, 'E2', 'Risk Register: Risk → Evidence → 대응 → 중단 기준', ['구분', 'Risk', '확인 Evidence (시점)', '대응', '중단 · 재편 기준'], rows,
           [1.1, 3.2, 2.4, 3.1, 2.03], size=9, pad=0.05,
           sub='초기 자금 목적 = 기술 · 사업 Risk → 측정 가능한 Evidence로 축소',
           note='- 주요 Risk: 자체 Hand 우위 · 주방 간 Transfer · 지불의사 · 설치 · 서비스 원가 · 가정용 안전 기준\n- 각 Risk = M6~M24 Gate에서 측정 가능한 Evidence로 확인 · 중단 · 재편 기준 사전 정의')


def _qa(prs, code, part, items, start_no):
    rows = [[(f"{start_no + i}", {'bold': True}), (q, {'bold': True}), a, ev, (wk, {'color': ACC})] for i, (q, a, ev, wk, where) in enumerate(items)]
    tslide(prs, code, f'투자심사 예상질문 · 방어논리 ({part}/3)', ['#', '질문', '방어논리', '근거 (Tag)', '약한 부분'], rows,
           [0.35, 1.85, 6.0, 2.05, 1.58], size=7.8, pad=0.035,
           sub='비판적 Seed VC · TIPS 운영사 관점 · 약한 항목 = 본문 보강 + 24개월 Evidence 연결',
           note='- 예상 질문 · 방어논리 · 근거 · 약한 부분\n- 가장 약한 부분 = 지불의사 · 원가 실측 · 팀 정보')


def e3(prs): _qa(prs, 'I1', 1, C.QA[0:7], 1)
def e4(prs): _qa(prs, 'I2', 2, C.QA[7:14], 8)
def e5(prs): _qa(prs, 'I3', 3, C.QA[14:20], 15)


def e6(prs):
    s, y = S(prs, 'I4', '현재 부족한 Evidence · Founder 입력 필요 정보', sub='현재 없는 Evidence = "없음" · Founder 칸 = 입력 전 [Founder 정보 필요]',
             note='- 현재 없음: 고객 · 계약 · 파트너 · 매출 · 시제품 Data\n- 우선순위: 팀 정보 → 상용 Gripper 기술 기준선 → 예약금 등 고객 행동 Evidence')
    lw = 7.3
    rows = [[(a, {'bold': True}), b, c, d] for a, b, c, d, _ in C.EVIDENCE]
    table(s, MX, y, lw, ['Evidence', '현재', '필요한 Evidence', '시점'], rows, col_w=[1.75, 1.75, 2.8, 1.0], size=7.8, label='E6a', pad=0.03)
    rx = MX + lw + 0.3; rw = W - MX - rx
    rows2 = [[(a, {'bold': True}), b] for a, b in C.FOUNDER_INPUTS]
    table(s, rx, y, rw, ['Founder 입력 필요', '내용'], rows2, col_w=[1.6, rw - 1.6], size=7.8, label='E6b', pad=0.03)
    foot(s, 'I4')


def e7(prs):
    s, y = S(prs, 'I5', f'투자심사 Memo: {C.VERDICT}', sub='내부 반론 검토 의견 · 점수 1~5 (5 = 강한 Evidence)',
             visual='좌측 판단 (MEET) 근거 2블록 · 가운데 평가표 (현재 → M24) · 우측 판단을 바꿀 Evidence 5개', chart='표 + 목록',
             note='- 판단 = MEET (미팅 검토 단계)\n- INVEST 아님: 팀 정보 · 기술 측정값 · 고객 행동 Evidence 부재\n- WATCH · PASS 아님: 문제 정의 · 접근 · 단계별 검증 구조 · 자금 계획 일관\n- 판단을 바꿀 Evidence 5개 (우측)')
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
    foot(s, 'I5')


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
    tslide(prs, 'I6', 'Number Tag 원칙', ['Tag', '정의', '대표 예시', '적용'], rows, [1.45, 3.0, 5.6, 1.78], size=10,
           sub='주요 숫자 · 미검증 내용 = Tag 구분 · 전체 입력 · Tag · 출처: xlsx Inputs 시트 · docs/08',
           takeaway='금지: 가상 고객 · 계약 · LOI · Partner · 매출 · 근거 없는 점유율 · "최초" · 근거 없는 ROI · 비용절감률 · 성능 · 특허 등록 확정 표현',
           note='- 모든 숫자 = FACT · DERIVED · ASSUMPTION · TARGET 중 하나\n- 그림 · 미검증 내용 = CONCEPT · TO BE VALIDATED · FUTURE')


def _wrap_url(u, width, size):
    # full URL (no truncation), broken after '/' '-' '_' '?' '&' '=' '.' so the estimated row height matches the render
    import re
    lines, cur = [], ''
    for tok in [t for t in re.findall(r'[^/\-_?&=.]*[/\-_?&=.]?', u) if t]:
        if cur and kit.text_w(cur + tok, size) > width * 0.88:
            lines.append(cur); cur = tok
        else:
            cur += tok
    return '\n'.join(lines + [cur])


def _src_slide(prs, code, items, part, n):
    rows = [[(d['id'], {'bold': True}), d['item'], d['value'], _wrap_url(d['source'].split(' , ')[0], 3.78 - 0.19, 7.2)] for d in items]
    tslide(prs, code, f'Sources ({part}/{n})', ['ID', '항목', '값', '대표 URL'], rows, [0.55, 2.6, 4.9, 3.78], size=7.2, pad=0.025,
           sub='조회일 2026-10-07~08 · 공식 통계 · 회사 발표 · 보도 인용',
           note='- 출처 목록 (조회일 2026-10-07~08 · 공식 통계 · 회사 발표 · 보도 인용)')


def f2(prs):
    src = M['src']
    n = 4; k = (len(src) + n - 1) // n
    for i in range(n):
        _src_slide(prs, f'F{1 + i}', src[i * k:(i + 1) * k], i + 1, n)


def iidx(prs):
    rows = [[('I1~I3', {'bold': True}), '투자심사 예상질문 20개 · 방어논리 · 근거 · 약한 부분', '발표 Q&A 준비'],
            [('I4', {'bold': True}), '현재 부족한 Evidence · Founder 입력 필요 정보', 'Founder 자료 · 첫 90일 실행'],
            [('I5', {'bold': True}), f'투자심사 Memo ({C.VERDICT}) · Scorecard · 판단을 바꿀 Evidence 5개', '내부 반론 검토'],
            [('I6', {'bold': True}), 'Number Tag 원칙 (FACT · DERIVED · ASSUMPTION · TARGET · CONCEPT · TBV · FUTURE)', '작성 기준']]
    tslide(prs, 'I0', 'IR 내부 검토용 자료 (제출 제외)', ['Code', '내용', '용도'], rows, [1.2, 7.4, 3.23], size=11,
           sub='제출용 IR (본문 18장 + 부록)과 분리 · 발표 준비 · 내부 검토 전용',
           note='- 제출 제외 자료: 예상질문 · 방어논리 · Evidence 공백 · Founder 입력 항목 · 투자심사 Memo · Tag 원칙\n- 제출용 IR = MH_Robotics_Seed_TIPS_IR_Final')


ORDER = [idx, a1, a2, a2b, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, d1, d2, d3, d4, d5, e1, e2, f2]
INTERNAL = [iidx, e3, e4, e5, e6, e7, f1]


def _run(prs, fns, pack):
    common.APX['on'] = True; common.APX['pack'] = pack
    try:
        for f in fns:
            f(prs)
    finally:
        common.APX['on'] = False; common.APX['pack'] = 'main'; kit.XFORM['fn'] = None


def build(prs):
    _run(prs, ORDER, 'appendix')


def build_internal(prs):
    _run(prs, INTERNAL, 'internal')
