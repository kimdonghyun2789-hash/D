# MH Robotics — Seed · TIPS IR 최종본 Main Deck (18 slides, Spec 35 order). 개조식 문구.
# One message per slide. Number Tags are small outlined chips. Orange only for Robot Zone / Path / Key Number.
from mhkit import *
from mhkit import M
import kit
from kit import T, W, H, MX, CW, text, rect, hline, vline, table, arrow, alpha, text_h, ttxt, column_chart, bar_chart
from pptx.enum.shapes import MSO_SHAPE


def F():
    return M['funding']


def HH(k='purchase_direct_Y3'):
    return M['household'][k]


# ================================================================= 01 cover
def m01(prs):
    s = start(prs, 'm01', pg(prs), 'MH Robotics — Kitchen Manipulation Robotics System',
              visual='좌측 짙은 패널: 회사명 · 제품 정의 · CLEAN → ASSIST → COOK · 현재 단계. 우측 3D 콘셉트 렌더: 구축 아파트 주방 한 벽 (Robot Home · Rail · 식기세척기 Interface).',
              chart='3D 콘셉트 렌더 1개 (CONCEPT)',
              note=('- MH Robotics: 다양한 실제 주방에서 식기 정리부터 조리까지 단계적으로 수행하는 주거용 Manipulation Robotics System\n'
                    '- 핵심: 로봇손 · 작업 Skill · Calibration · 주방 Interface의 단일 제품화\n'
                    '- 첫 검증 Workflow = CLEAN (식기 정리) → 같은 Platform에 ASSIST · COOK 단계적 추가\n'
                    '- 적용: 기존 주방 · Remodeling · 신축 → Installed Base 기반 Care · 소모품 · Skill 반복매출\n'
                    '- 현재 Concept 단계 (시제품 · 고객 · 계약 · 매출 없음) → Seed · TIPS 24개월 Evidence 확보 계획'))
    pw = 5.35
    rect(s, 0, 0, pw, H, fill=INK)
    x = 0.62; w = pw - 1.0
    text(s, x, 0.72, w, 0.3, 'M H   R O B O T I C S', size=12, bold=True, color='A9AEB5')
    text(s, x, 1.3, w, 1.95, 'Kitchen Manipulation\nRobotics System', size=30, bold=True, color='FFFFFF', line=1.0)
    text(s, x, 3.28, w, 0.62, '로봇손 · 작업 Skill · Calibration · 주방 Interface 통합 제품', size=13.5, bold=True,
         color='E3E5E8', line=1.05)
    text(s, x, 3.98, w, 0.48, '식기 정리 → 조리까지 단계적 확장 · 기존 주방 · Remodeling · 신축 적용 · Installed Base 반복매출',
         size=10.5, color='A9AEB5', line=1.05)
    hline(s, x, 4.7, w, color='3A3F46', lw=1.0)
    for i, (a, b) in enumerate([('CLEAN', '첫 검증 Workflow (식기 정리)'), ('ASSIST', '중기 확장 (재료 이동 · 투입 · 도구)'),
                                ('COOK', '장기 R&D 방향 (Recipe Workflow)')]):
        yy = 4.88 + i * 0.36
        text(s, x, yy, 1.0, 0.3, a, size=11, bold=True, color='FFFFFF' if i == 0 else '80868D', anchor='m')
        text(s, x + 1.0, yy, w - 1.0, 0.3, b, size=10, color='C9CDD2' if i == 0 else '80868D', anchor='m')
    text(s, x, 6.32, w, 0.26, 'Seed 투자 · TIPS 창업기업 IR  |  2026.10', size=9.5, color='A9AEB5')
    text(s, x, 6.62, w, 0.42, '현재 단계: Concept (시제품 개발 전)',
         size=8.5, color='80868D', line=1.05)
    rx = pw; rw = W - pw
    at = render(s, 'v2_cover', rx, 0, rw, H, focus=(0.55, 0.5))
    callout(s, at, 'garage', 'Robot Home (Dock)', -0.35, -0.55, side='l')
    callout(s, at, 'rail', 'Rail (필요 시)', 0.3, -0.55)
    callout(s, at, 'dw', '식기세척기 Interface', 0.55, 0.45)
    mt(s, W - 1.75, H - 0.4, 'CONCEPT', label='CONCEPT RENDERING', fill='FFFFFF')


# ================================================================= 02 problem
def _flow_tag(s, at, key, txt, dx, dy, side=None):
    """m02 figure label: appliance (기기 안 자동화) = white chip + thin leader, grey text."""
    ax, ay = at(key); lx, ly = ax + dx, ay + dy
    seg(s, ax, ay, lx, ly, color=GREY, lw=0.6)
    dot(s, ax, ay, 0.06, fill=INK2)
    chipl(s, lx, ly, txt, size=8.5, side=side or ('r' if dx >= 0 else 'l'), color=INK2)


def _flow_kitchen(s, x, y, w, h):
    """m02 figure: ordinary kitchen without robot (3D) · appliances = white chips · human tasks between them = dark dashed paths ①~④."""
    rect(s, x, y, w, h, fill=SOFT)
    at = render(s, 'fig_flow_kitchen', x, y, w, h, focus=(0.5, 0.5), bg=(244, 245, 246))
    _flow_tag(s, at, 'ih', '인덕션', -0.3, -0.42)
    _flow_tag(s, at, 'oven', '오븐', -0.62, 0.2)
    _flow_tag(s, at, 'fridge', '냉장고', 0.0, -0.5, side='c')
    _flow_tag(s, at, 'dwDoor', '식기세척기', 0.62, 0.36)
    for i, key in enumerate(['p1_35', 'p2_55', 'p3_35', 'p4_55']):
        cx, cy = at(key)
        marker(s, cx, cy, i + 1, d=0.23, fill=INK, size=8.5)


def m02(prs):
    s = start(prs, 'm02', pg(prs), '가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workflow',
              visual='좌측 3D 주방 그림 (로봇 없음): 냉장고 · 인덕션 · 오븐 · 식기세척기 = 기기 안 자동화 (흰 라벨) · 가전 사이 사람 작업 = 짙은 점선 ①~④ (식탁 → 싱크 → 식세기 → 조리대 → 수납장) + 사람 형상. 우측: 가전 4종 압축 카드 (기기 안 자동화) · 짙은 띠 Physical Task 10개 (①~④ = CLEAN 범위). 하단 공식: Appliance Automation ≠ Physical Workflow Automation · 근거 숫자 4개.',
              chart='3D 주방 Workflow 그림 1개 (로봇 없음) + 압축 카드 4 + 작업 띠 + 핵심 숫자 4',
              note=('- 식세기 · 인덕션 · 냉장고 · 오븐 = 기기 안의 일만 자동화\n'
                    '- 식기 이동 · 식세기 적재 · 인출 · 수납 · 재료 투입 · 도구 조작 = 여전히 사람 몫\n'
                    '- 문제 정의: 개별 가전 기능이 아닌 주방 Workflow 전체의 Physical Manipulation 미자동화\n'
                    '- 근거: 2024 무급 가사노동 가치 582.4조원 · 그중 가정관리 (음식 준비 · 청소 등) 78.9% (가계생산 위성계정)\n'
                    '- 식사 후 정리 하루 약 40분 = 가설 → Time-diary 30세대로 검증 예정\n'
                    '- 가전 사이 사람 작업 흐름 ①~④: 식탁 → 싱크 → 식세기 → 조리대 → 수납장 (CLEAN 범위)'))
    y = mhead(s, '02  문제', '가전 자동화 이후에도 사람 몫으로 남은 주방 Physical Workflow',
              '개별 가전 기능은 자동화 · 주방 Workflow 전체의 Physical Manipulation은 아직 사람 몫')
    fw, fh = 6.55, 3.05
    _flow_kitchen(s, MX, y, fw, fh)
    rx = MX + fw + 0.3; rw = W - MX - rx
    text(s, rx, y, rw, 0.24, '기기 안 자동화', size=10, bold=True, color=GREY)
    apps = [('식기세척기', '세척 자동화'), ('인덕션', '가열 자동화'), ('냉장고', '보관 자동화'), ('오븐', '조리 일부 자동화')]
    gap = 0.14; cw = (rw - gap) / 2; ch = 0.6
    for i, (a, b) in enumerate(apps):
        cx = rx + (i % 2) * (cw + gap); cy = y + 0.3 + (i // 2) * (ch + 0.1)
        rect(s, cx, cy, cw, ch, fill=SOFT)
        text(s, cx + 0.16, cy, cw - 0.32, ch, a, size=12.5, bold=True, anchor='m')
        text(s, cx + 0.16, cy, cw - 0.32, ch, b, size=9.5, color=INK2, align='r', anchor='m')
    y2 = y + 0.3 + 2 * ch + 0.1 + 0.17; bh = y + fh - y2
    rect(s, rx, y2, rw, bh, fill=INK)
    text(s, rx + 0.2, y2 + 0.14, rw - 0.4, 0.28, '가전 사이 사람이 하는 Physical Task', size=11.5, bold=True, color='FFFFFF')
    text(s, rx + 0.2, y2 + 0.16, rw - 0.4, 0.26, '①~④ = CLEAN 검증 범위', size=8.5, color='A9AEB5', align='r', check=False)
    tasks = ['① 식기 이동', '② 식세기 적재', '③ 식세기 인출', '④ 수납', '식재료 이동', '재료 투입', '조리도구 조작', '젓기', '뚜껑 조작', '조리 후 정리']
    xx = rx + 0.2; yy = y2 + 0.52
    for i, t in enumerate(tasks):
        wv = kit.text_w(t, 9, True) + 0.2
        if xx + wv > rx + rw - 0.2: xx = rx + 0.2; yy += 0.34
        rect(s, xx, yy, wv, 0.27, fill='2C3036')
        text(s, xx, yy, wv, 0.27, t, size=9, bold=True, color='FFFFFF' if i < 4 else 'C9CDD2', align='c', anchor='m', check=False)
        xx += wv + 0.07
    assert yy + 0.27 <= y2 + bh - 0.1, yy
    y3 = y + fh + 0.2
    text(s, MX, y3, CW, 0.44, [[('Appliance Automation  ', {'color': INK}), ('≠', {'color': INK}), ('  Physical Workflow Automation', {'color': INK})]],
         size=20, bold=True, align='c')
    y4 = y3 + 0.6
    nw = (CW - 3 * 0.3) / 4
    items = [('582.4조원', '무급 가사노동 가치 (2024)', 'FACT'), ('78.9%', '그중 가정관리 (음식 준비 · 청소 등) 459.5조원', 'FACT'),
             ('132분', '1인당 하루 가사노동 (2024, 2019년 137분)', 'FACT'), ('약 40분', '하루 식사 후 정리 (식기 이동 · 식세기 · 수납)', 'ASSUMPTION')]
    for i, (v, lab, tg) in enumerate(items):
        knum(s, MX + i * (nw + 0.3), y4, nw, v, lab, tg, vsize=22, color=ACC if i == 3 else INK, lsize=9.5, tag_y=y4 + 0.7)
    note(s, '출처: 국가데이터처 2024 가계생산 위성계정 (2026.4) [S40] · 식사 후 정리 40분 = 가설 → Time-diary 30세대로 검증 예정')
    mfoot(s)


# ================================================================= 03 why kitchen
def _tech_brk(t, w, size):
    """Two-line text: break at the last ' · ' / ' → ' separator that fits in `w` (no break inside a phrase)."""
    if kit.text_w(t, size) <= w: return t
    cuts = [(i, sep) for sep in (' · ', ' → ') for i in range(len(t)) if t.startswith(sep, i)
            and kit.text_w(t[:i] + sep.rstrip(), size) <= w]
    if not cuts: return t
    i, sep = max(cuts)
    return t[:i] + sep.rstrip() + '\n' + t[i + len(sep):]


def _tech_kitchen(s, x, y, w, h):
    """m03 figure: 확보 평면 구축 2Bay A 주방 + MH Interface (3D, CONCEPT) · 주황 = Robot 작업영역 · 회색 지시선 라벨."""
    rect(s, x, y, w, h, fill=SOFT)
    at = render(s, 'fig_tech_m03_kitchen', x, y, w, h, bg=(244, 245, 246))
    callout(s, at, 'garage', 'Robot Home', 0.35, -0.28, size=8, side='r')
    callout(s, at, 'sink', '싱크', -0.55, -0.62, size=8, side='l')
    callout(s, at, 'drawer', '수납 (서랍)', -0.75, 0.55, size=8, side='l')
    callout(s, at, 'dw', '식세기', 0.25, 0.62, size=8, side='l')
    callout(s, at, 'cooktop', '인덕션 (옆벽 이동)', 0.1, 0.62, size=8, side='c')
    mt(s, x + 0.05, y + 0.05, 'CONCEPT', size=5.5, h=0.14, fill='FFFFFF')
    lx, ly = x + 0.08, y + h - 0.3
    lw_ = kit.text_w('Robot 작업영역 (고정)', 8, True) + 0.44
    rect(s, lx, ly, lw_, 0.22, fill='FFFFFF', line=EDGE, lw=0.5)
    kit.alpha(rect(s, lx + 0.08, ly + 0.06, 0.18, 0.1, fill=ACC, line=ACC, lw=0.75), 45)
    text(s, lx + 0.32, ly, lw_ - 0.34, 0.22, 'Robot 작업영역 (고정)', size=8, bold=True, color=INK, anchor='m', check=False)


def m03(prs):
    s = start(prs, 'm03', pg(prs), '주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간',
              visual='좌측 3D 콘셉트 그림 (CONCEPT): 확보 평면 구축 2Bay A 주방 + MH Interface · 주황 = Robot 작업영역 (조리대 한 줄 고정) · 라벨 Robot Home · 싱크 · 수납 · 식세기 · 인덕션 (옆벽). 우측 2열: Robot Engineering 기준 4개 · Business 기준 4개 (번호 + 굵은 제목 + 한 줄 근거). 하단 결론 띠.',
              chart='3D 콘셉트 그림 1개 (CONCEPT) + 2열 목록 + 결론 띠',
              note=('- 기술: 동작 종류 적음 (집기 · 옮기기 · 놓기 · 넣기 · 빼기) · 작업영역 고정 (싱크 · 조리대 · 식세기 · 수납장)\n'
                    '- 물체 범위 닫힘: 접시 · 컵 · 그릇 · 수저 · 뚜껑 · 도구 → 이후 식재료\n'
                    '- 사업: 매일 사용 → 빠른 가치 체감 · 주방 Remodeling · 신축 입주 = 구매 계기\n'
                    '- Why now: 6축 Arm 가격 하락 ($6,999~) · 공개 조작 모델 (π0.5) · 가정용 로봇 안전기준 (IEC 63682 초안)\n'
                    '- 지불의사 = 별도 검증 (M18 WTP 조사 n ≥ 300 · 예약금 Test)\n'
                    '- 그림: 확보 평면 (구축 2Bay A) 주방에 Interface 적용 예 → Robot 작업영역 = 조리대 한 줄 (Robot Home · 싱크 · 수납 · 식세기) 고정'))
    y = mhead(s, '03  왜 Kitchen인가', '주방: 기술 · 사업성 동시 검증이 가능한 첫 적용 공간',
              'Robot Engineering 4개 기준 · Business 4개 기준')
    fw = 4.1
    text(s, MX, y, fw, 0.3, '구축 2Bay A 주방 · Interface 적용 예', size=12, bold=True, color=GREY)
    hline(s, MX, y + 0.36, fw, color=INK, lw=1.0)
    _tech_kitchen(s, MX, y + 0.5, fw, 3 * 0.92 + 0.8)
    cols = [('Robot Engineering 기준', [
                ('집기 · 이동 · 놓기 · 넣기 · 빼기 중심', '동작 종류 적고 반복 → Skill Library화 용이'),
                ('작업영역 고정', '싱크 · 조리대 · 식세기 · 수납장 → Calibration 대상 명확'),
                ('물체는 다양 · 범위는 닫힘', '접시 · 컵 · 그릇 · 수저 · 뚜껑 · 집게 · 국자 → 이후 식재료'),
                ('가전 사이 이동 반복', '식세기 · 수납장 · 조리대 사이 물리적 이동')]),
            ('Business 기준', [
                ('높은 일일 사용빈도', '매일 식사 후 반복 → 사용 Data · 빠른 가치 체감'),
                ('구매 계기 존재', '주방 Remodeling · 신축 입주 시 공사 · 설치 동시 결정'),
                ('CLEAN → ASSIST → COOK', '같은 Platform + Skill · Tool 추가로 기능 확장'),
                ('설치 이후 반복매출', 'Installed Base 기반 Care · 소모품 · Skill')])]
    x0 = MX + fw + 0.4; cg = 0.35
    cw = (W - MX - x0 - cg) / 2; ni = 0.48
    for ci, (head_, rows) in enumerate(cols):
        cx = x0 + ci * (cw + cg)
        text(s, cx, y, cw, 0.3, head_, size=12, bold=True, color=GREY)
        hline(s, cx, y + 0.36, cw, color=INK, lw=1.0)
        for ri, (a, b) in enumerate(rows):
            ry = y + 0.5 + ri * 0.92
            text(s, cx, ry, ni, 0.4, f'0{ri + 1}', size=15, bold=True, color=INK)
            text(s, cx + ni, ry, cw - ni, 0.32, a, size=13 if kit.text_w(a, 13, True) < cw - ni - 0.1 else 12.5, bold=True)
            b = _tech_brk(b, cw - ni - 0.12, 10.5)
            text(s, cx + ni, ry + 0.35, cw - ni, kit.text_h(b, 10.5, cw - ni, line=1.0) + 0.02, b, size=10.5, color=INK2, line=1.0)
            if ri < 3: hline(s, cx, ry + 0.84, cw)
    by = y + 0.5 + 4 * 0.92 + 0.08
    bar(s, MX, by, CW, 0.52, '→  주거용 Manipulation의 기술성 · 고객가치 동시 검증이 가능한 첫 Application', size=13)
    note(s, 'Why now: 6축 Arm $6,999~ [S15] · 공개 조작 모델 π0.5 [S46] · 가정용 로봇 안전기준 IEC 63682 초안 [S47] · 지불의사 = WTP n≥300 · 예약금 Test로 검증 (M18)')
    mfoot(s)


# ================================================================= 04 limits
_VAR_KITCHENS = [('old2a', '구축 2Bay A', 'ㄱ자 · 윗벽 3,255mm'), ('old2b', '구축 2Bay B', 'ㄱ자 · 싱크 줄 약 2.6m'),
                 ('new3', '신축 3Bay', '반도형 · 싱크 줄 약 2.6m'), ('new4', '신축 4Bay', '반도형 · 싱크 줄 약 2.8m')]


def _var_strip(s, x, y, w, ih, gap=0.12):
    """확보 평면 4종 주방 (도면 그대로 재작도 · 로봇 없음 · 동일 축척 Axonometric) + 3줄 캡션. Returns the bottom y."""
    import content as C
    plans = {p[0]: p for p in C.PLANS}
    tw = (w - 3 * gap) / 4
    for i, (pid, name, kind) in enumerate(_VAR_KITCHENS):
        row = plans[name]
        assert all(t in row[3] for t in kind.replace('·', ' ').split() if t in ('ㄱ자', '반도형') or t[0].isdigit()), (name, kind)
        tx = x + i * (tw + gap)
        render(s, 'fig_var_k_' + pid, tx, y, tw, ih, bg=(244, 245, 246))
        fit = '기본 한 줄 배치 수용' if row[5].startswith('수용') else '기본 한 줄 배치 불가'
        text(s, tx, y + ih + 0.05, tw, 0.5, [[(name, {'bold': True})], [(kind, {'size': 8, 'color': INK2})],
                                             [(fit, {'size': 7.5, 'color': GREY})]], size=8.5, label='m04cap ' + name)
    return y + ih + 0.55


def m04(prs):
    s = start(prs, 'm04', pg(prs), '주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계',
              visual='좌측 상단: 확보 평면 4종 주방 3D 재작도 4컷 (구축 2Bay A · B · 신축 3Bay · 4Bay, 도면 그대로 · 로봇 없음 · 같은 시점 · 동일 축척) + 평면명 · 주방 형태 · 기본 한 줄 배치 수용/불가 캡션. 좌측 하단: 주방마다 달라지는 9개 변수 칩. 우측 세로 체인: 범용 Robot 적용 시 집마다 반복되는 6단계 (Perception → Validation) + 결론 상자. 하단 전체 폭: 근거 2행 (확보 평면 5종 · 공개 사례).',
              chart='평면 재작도 주방 4컷 (동일 축척 Axonometric) + 변수 칩 + 반복 공정 체인 + 근거 표',
              note=('- 가정용 로봇의 한계 = AI 성능만이 아닌 높은 환경 편차\n'
                    '- 집마다 다른 것: 주방 형태 · 가전 위치 · 모델 · 수납 위치 · 조리대 치수 · 물건 위치 · 동선 · 조명 · 설치 오차\n'
                    '- 범용 로봇 적용 시 집마다 인식 · Mapping · 교시 · Programming · Calibration · 검증 반복 → 설치시간 · 비용 · 신뢰성 좌우\n'
                    '- 확보 평면 5종: 싱크 벽 길이 약 2.6~3.3m · 3종 기본 배치 불가 · 1종 미검토\n'
                    '- MH 접근 = 모든 주방 표준화가 아닌 Robot 적응 + 필요한 지점만 Interface (다음 장)\n'
                    '- 확보 평면 4종 주방 재작도 (로봇 없음 · 동일 축척): ㄱ자 2종 · 반도형 2종 · 기본 한 줄 배치 수용 = 구축 2Bay A 1종'))
    y = mhead(s, '04  가정용 Robot 적용의 구조적 한계', '주방마다 다른 환경 → 동일 로봇 반복 설치의 구조적 한계',
              'Robot 지능 부족만이 아닌 높은 환경 편차 (Environment Variation) → 신뢰성 · 반복설치 제약')
    lw = 7.0
    text(s, MX, y, 2.0, 0.28, '주방마다 다른 것', size=11, bold=True, color=GREY)
    text(s, MX + 2.0, y + 0.06, lw - 2.0, 0.2, '확보 평면 재작도 (단지명 미표기) · 동일 축척 · 신축 2Bay = 3D 미착수', size=7.5,
         color=GREY, align='r')
    cy = _var_strip(s, MX, y + 0.36, lw, 1.52)
    vars_ = [('주방 형태', 'ㅡ자 · ㄱ자 · 반도형'), ('가전 위치', '식세기 · 인덕션 배치'), ('수납 위치', '상부장 · 서랍 · 키큰장'),
             ('조리대 치수', '높이 · 깊이 · 길이'), ('가전 모델', '랙 구조 · 문 열림'), ('물건 위치', '식기 놓는 자리'),
             ('동선', '통로 폭 · 사람 위치'), ('조명', '창 · 조명 반사'), ('설치오차', '벽 · 가구 수직 · 수평')]
    gw = (lw - 2 * 0.1) / 3; gh = 0.34
    for i, (a, b) in enumerate(vars_):
        gx = MX + (i % 3) * (gw + 0.1); gy = cy + 0.2 + (i // 3) * (gh + 0.08)
        rect(s, gx, gy, gw, gh, fill=SOFT)
        text(s, gx + 0.12, gy, gw - 0.24, gh, [[(a, {'bold': True}), ('   ' + b, {'size': 9, 'color': INK2})]], size=10,
             anchor='m', check=False)
    rx = MX + lw + 0.45; rw = W - MX - rx
    text(s, rx, y, rw, 0.28, '범용 Robot 적용 시 집마다 반복', size=11, bold=True, color=GREY)
    steps = ['인식 (Perception)', 'Mapping', '교시 (Teaching)', 'Programming', 'Calibration', '검증 (Validation)']
    sy = y + 0.36; sh = 0.34; sg = 0.105
    for i, st in enumerate(steps):
        yy = sy + i * (sh + sg)
        rect(s, rx, yy, rw - 0.7, sh, fill=INK)
        text(s, rx, yy, rw - 0.7, sh, st, size=11.5, bold=True, color='FFFFFF', align='c', anchor='m')
        if i < len(steps) - 1: arrow(s, rx + (rw - 0.7) / 2, yy + sh, rx + (rw - 0.7) / 2, yy + sh + sg, color=GREY, lw=1.0)
    by0 = sy; by1 = sy + 6 * (sh + sg) - sg
    bx = rx + rw - 0.6
    seg(s, bx, by0, bx, by1, color=INK, lw=1.5)
    seg(s, bx - 0.1, by0, bx, by0, color=INK, lw=1.5); seg(s, bx - 0.1, by1, bx, by1, color=INK, lw=1.5)
    text(s, bx + 0.06, (by0 + by1) / 2 - 0.3, 0.5, 0.6, '집마다\n반복', size=8.5, bold=True, color=INK, align='l', anchor='m', check=False)
    bar(s, rx, by1 + 0.32, rw - 0.3, 0.62, '모든 주방 표준화가 아닌\n→ Robot 적응력 + 필요한 지점만 Interface', size=10.5, fill=SOFT, color=INK)
    ey = max(cy + 0.2 + 3 * gh + 2 * 0.08, by1 + 0.32 + 0.62) + 0.22
    rows = [[('확보 평면 5종', {'bold': True}), '싱크 벽 길이 약 2.6~3.3m · 3종 기본 한 줄 배치 불가 · 1종 미검토 · ㄱ자 · 일자 · 반도형 혼재', ttxt('DERIVED')],
            [('공개 사례', {'bold': True}), 'LG CLOiD: 팔 작업 범위 무릎 높이 이상 (보도) → 낮은 작업점 (식세기 하단 랙) = 환경 측 보완 필요 (MH 해석)', ('FACT + 해석', {'bold': True, 'size': 9})]]
    table(s, MX, ey, CW, None, rows, col_w=[1.35, CW - 2.35, 1.0], size=9.5, label='m04ev')
    note(s, '출처 [S21] · 평면 5종 = 제공 도면 재작도 (부록 B2) · 평면 30개 분석 예정 (M6)')
    mfoot(s)


# ================================================================= 05 technology strategy
_TECH_M05 = [('fig_tech_m05_hand', (0.5, 0.5), 1.0, '국자 · 컵 · 접시 파지'), ('v2_seq_3_load', (0.6, 0.62), 1.0, '식세기 적재'),
             ('v2_seq_1_detect', (0.45, 0.55), 1.0, '조리대 식기 인식'), ('v2_stow_2_open', (0.4, 0.45), 1.0, 'Robot Home · Rail')]


def _tech_tile(s, x, y, w, h, name, focus, zoom, cap):
    """m05 card image: SOFT 바탕 3D 콘셉트 렌더 (CONCEPT) + 우하단 작은 예시 라벨."""
    rect(s, x, y, w, h, fill=SOFT)
    render(s, name, x, y, w, h, focus=focus, zoom=zoom, bg=(244, 245, 246))
    mt(s, x + 0.05, y + 0.05, 'CONCEPT', size=5.5, h=0.14, fill='FFFFFF')
    cw_ = kit.text_w(cap, 8, False) + 0.16
    rect(s, x + w - cw_ - 0.05, y + h - 0.24, cw_, 0.19, fill='FFFFFF', line=EDGE, lw=0.5)
    text(s, x + w - cw_ - 0.05, y + h - 0.24, cw_, 0.19, cap, size=8, color=INK2, align='c', anchor='m', check=False)


def m05(prs):
    s = start(prs, 'm05', pg(prs), 'Robot 적응 + 반복 작업점에만 최소 Interface',
              visual='4열 대응표: 위 회색 칩 = 변동 요인 (Object · Task · Kitchen · 반복 작업점), 아래 카드 = MH 기술 (Hand · Skill · Calibration · Interface) + 카드마다 3D 콘셉트 그림 1개 (CONCEPT · 같은 크기): 같은 Hand의 국자 · 컵 · 접시 파지 · 식세기 적재 · 조리대 식기 인식 · Robot Home · Rail. 하단 짙은 결론 띠.',
              chart='4열 대응 Diagram + 3D 콘셉트 그림 4컷 (CONCEPT)',
              note=('- 접근: 주방 전체를 로봇에 맞게 바꾸는 방식이 아님\n'
                    '- 물체 다양성 → Adaptive Robot Hand · 작업 다양성 → Manipulation Skill Library\n'
                    '- 주방 차이 → Perception + Calibration (현장에서 좌표 · 가전 · 수납 위치 등록)\n'
                    '- 매일 반복되는 작업점 (Robot 대기 자리 · 도구 거치대 · 식세기 랙)에만 최소 Interface\n'
                    '- 환경 표준화 = 목적이 아닌 신뢰성 · 반복설치 수단 → 같은 Robot · Skill의 여러 주방 반복 적용\n'
                    '- 카드 그림 예 (CONCEPT): 같은 Hand의 국자 · 컵 · 접시 파지 · 식세기 적재 · 조리대 식기 인식 · Robot Home · Rail'))
    y = mhead(s, '05  MH Robotics Technology Strategy', 'Robot 적응 + 반복 작업점에만 최소 Interface',
              'Robot Hand · Manipulation Skill · Calibration · Environment Interface 통합 설계')
    cols = [('물체 다양성 (Object)', '형상 · 재질 · 젖은 표면 · 얇은 Edge', 'Adaptive Robot Hand', '파지 방식 전환 → 다양한 식기 · 도구를 하나의 손으로'),
            ('작업 다양성 (Task)', '집기 · 넣기 · 꺼내기 · 열기', 'Manipulation Skill Library', '집기 · 놓기 · 넣기 · 빼기 · 열고 닫기 = 재사용 단위'),
            ('주방 차이 (Kitchen)', '가전 · 수납 위치 · 설치 오차', 'Perception + Calibration', '현장에서 좌표 · 가전 · 수납 위치 등록 → 같은 Skill 실행'),
            ('반복 작업점', 'Robot 대기 · 도구 · 식세기 랙', 'Minimal Robot-friendly Interface', 'Robot Home · Tool Dock · 가전 Interface · Vision 기준점')]
    gap = 0.22; cw = (CW - 3 * gap) / 4
    kh = 0.8; b0 = y + kh + 0.36; ih = 1.15; bh = 2.48
    for i, (k, kd, t, d) in enumerate(cols):
        cx = MX + i * (cw + gap)
        rect(s, cx, y, cw, kh, fill=SOFT)
        text(s, cx + 0.16, y + 0.1, cw - 0.32, 0.3, k, size=12.5, bold=True, color=INK2)
        text(s, cx + 0.16, y + 0.44, cw - 0.32, 0.26, kd, size=9.5, color=GREY)
        arrow(s, cx + cw / 2, y + kh + 0.05, cx + cw / 2, b0 - 0.06, color=GREY, lw=1.5)
        rect(s, cx, b0, cw, bh, fill='FFFFFF', line=INK, lw=1.25)
        _tech_tile(s, cx + 0.08, b0 + 0.08, cw - 0.16, ih, *_TECH_M05[i])
        ty = b0 + 0.08 + ih + 0.08
        text(s, cx + 0.16, ty, cw - 0.32, 0.62, t, size=15, bold=True, line=1.0)
        text(s, cx + 0.16, ty + 0.62, cw - 0.32, b0 + bh - ty - 0.66, d, size=10.5, color=INK2, line=1.05)
    by = b0 + bh + 0.2
    bar(s, MX, by, CW, 0.56, '결과: 다양한 주방에서 같은 Platform · Skill의 반복 적용 가능성 확대', size=14)
    text(s, MX, by + 0.72, CW, 0.3, [[('핵심 원칙  ', {'bold': True, 'color': INK}),
                                      ('환경 표준화 = 목적이 아닌 신뢰성 · 반복설치 수단 · 주방 전체 표준화 없음', {'color': INK2})]],
         size=11)
    note(s, '검증 순서 · Gate: 16쪽 · 부록 A5')
    mfoot(s)


# ================================================================= 06 adaptive hand
def m06(prs):
    s = start(prs, 'm06', pg(prs), '핵심 Hardware: 주방 물체 대응 Adaptive Robot Hand',
              visual='좌측 Hand 확대 렌더 (Quick Changer · 힘/토크 센서 · Wrist Camera · 교체형 Food-contact Pad · Palm Suction 표시) + 접시 · 컵 · 그릇 · 국자 파지 4컷 (각 CONCEPT). 우측 주방 물체의 어려움 · 핵심 기술 후보 · Buy vs Build Gate. 하단 Hand → 사업성 연결 띠.',
              chart='3D 콘셉트 렌더 5컷 (CONCEPT) + 연결 체인',
              note=('- 핵심 Hardware = 주방 물체를 다루는 로봇손\n'
                    '- 파지 방식: 접시 가장자리 Pinch · 컵 외벽 감싸기 · 그릇 테두리 Pinch · 국자 손잡이 파지\n'
                    '- 목표 = 손가락 수 · 자유도 경쟁이 아닌 작업 완료율 · 가격 · 위생 · 유지관리 · 내구성\n'
                    '- 식품 접촉 Pad · Tip = 교체형 Module → 위생 관리 + 소모품 매출\n'
                    '- 자체 Hand 우위 = 미검증 → M6 상용 Gripper (Robotiq 2F-85 등) 기준선과 30종 식기 비교, Coverage +15%p 또는 Tool 교체 50% 감소 시에만 채택'))
    y = mhead(s, '06  Adaptive Kitchen Robot Hand', '핵심 Hardware: 주방 물체 대응 Adaptive Robot Hand',
              '손가락 수 · 자유도 경쟁이 아닌 작업 완료율 · 가격 · 위생 · 유지관리 · 내구성 중심')
    hw_, hh_ = 3.95, 3.3
    rect(s, MX, y, hw_, hh_, fill=SOFT)
    at = render(s, 'hand_hero', MX, y, hw_, hh_, focus=(0.5, 0.5), zoom=0.98, bg=(244, 245, 246))
    callout(s, at, 'pad', '교체형 Food-contact Pad', 0.42, -0.02, size=7.5)
    callout(s, at, 'ft', '힘 · 토크 센서', 0.4, -0.1, size=7.5)
    callout(s, at, 'qc', 'Quick Changer', 0.45, 0.02, size=7.5)
    callout(s, at, 'cam', 'Wrist Camera', -0.3, 0.38, size=7.5, side='l')
    mt(s, MX + 0.08, y + 0.08, 'CONCEPT', fill='FFFFFF')
    tw_ = 1.5; tg = 0.1; tx0 = MX + hw_ + 0.14
    tiles = [('hand_plate', '접시 · 가장자리 Pinch', (0.45, 0.42)), ('hand_cup', '컵 · 외벽 감싸기', (0.62, 0.45)),
             ('hand_bowl', '그릇 · 테두리 Pinch', (0.42, 0.52)), ('hand_tool', '국자 · 손잡이 파지', (0.55, 0.5))]
    th_ = (hh_ - tg) / 2
    for i, (nm, lab, fc) in enumerate(tiles):
        tx = tx0 + (i % 2) * (tw_ + tg); ty = y + (i // 2) * (th_ + tg)
        rect(s, tx, ty, tw_, th_, fill=SOFT)
        render(s, nm, tx, ty, tw_, th_ - 0.3, focus=fc, zoom=1.15, bg=(244, 245, 246))
        mt(s, tx + 0.05, ty + 0.05, 'CONCEPT', size=5.5, h=0.14, fill='FFFFFF')
        text(s, tx + 0.06, ty + th_ - 0.29, tw_ - 0.12, 0.26, lab, size=8.5, bold=True, align='c', anchor='m', check=False)
    rx = tx0 + 2 * tw_ + tg + 0.28; rw = W - MX - rx
    text(s, rx, y, rw, 0.26, '주방 물체의 어려움', size=10.5, bold=True, color=GREY)
    text(s, rx, y + 0.28, rw, 0.62, '형상 · 크기 · 재질 (유리 · 도자기 · 금속 · 플라스틱) · 젖은 표면 · 미끄러짐 · 파손 위험 · 얇은 가장자리 · 다양한 손잡이',
         size=10, color=INK, line=1.05)
    text(s, rx, y + 0.98, rw, 0.26, '핵심 기술 후보', size=10.5, bold=True, color=GREY)
    techs = ['적응 파지', '유연 접촉 (Compliance)', '파지력 제어', '미끄럼 감지', '다점 접촉', '도구 파지',
             '교체형 식품접촉 Module']
    xx = rx; yy = y + 1.28
    for t in techs:
        wv = kit.text_w(t, 8.5, True) + 0.18
        if xx + wv > rx + rw: xx = rx; yy += 0.28
        rect(s, xx, yy, wv, 0.23, fill=SOFT2)
        text(s, xx, yy, wv, 0.23, t, size=8.5, bold=True, align='c', anchor='m', check=False)
        xx += wv + 0.06
    gy = yy + 0.36
    rect(s, rx, gy, rw, y + hh_ - gy, fill='FFFFFF', line=INK, lw=1.0)
    text(s, rx + 0.14, gy + 0.08, rw - 0.28, 0.26, 'Buy vs Build — M6 Gate', size=11, bold=True)
    text(s, rx + 0.14, gy + 0.38, rw - 0.28, y + hh_ - gy - 0.45,
         ['기준선: Robotiq 2F-85 약 $5,825 · Inspire RH56 $4,500~ (FACT)',
          '30종 식기로 성공률 · 파손 · 교체 · 원가 비교',
          'Coverage +15%p 또는 Tool 교체 50%↓ 시에만 자체 Hand (TARGET)'], size=9, color=INK2, bullet='–', space_after=1, line=1.0)
    cy = y + hh_ + 0.22
    chain = ['물체 다양성 대응', '전용 Gripper 수 ↓', '같은 End-effector 활용 ↑', 'Skill 재사용 ↑', '유지보수 단순화']
    cwid = (CW - 2.25 - 4 * 0.24) / 5
    for i, c in enumerate(chain):
        cx = MX + i * (cwid + 0.24)
        rect(s, cx, cy, cwid, 0.46, fill=SOFT)
        text(s, cx, cy, cwid, 0.46, c, size=9.5, bold=True, align='c', anchor='m')
        if i < 4: arrow(s, cx + cwid + 0.02, cy + 0.23, cx + cwid + 0.22, cy + 0.23, color=GREY, lw=1.25)
    ex = MX + 5 * cwid + 4 * 0.24 + 0.15
    rect(s, ex, cy, W - MX - ex, 0.46, fill=INK)
    text(s, ex, cy, W - MX - ex, 0.46, '+ Pad · Seal · Tip = 소모품', size=9.5, bold=True, color='FFFFFF', align='c', anchor='m')
    note(s, '식품 접촉 부품: 식품위생법 "기구" · 「기구 및 용기 · 포장의 기준 및 규격」 고무제 규격 대응 (ASSIST · COOK 단계 필수) [S42 · S48]')
    mfoot(s)


# ================================================================= 07 skill / calibration
def _kitchen_tile(s, x, y, w, h, name, kind):
    """Schematic plan of a kitchen run (top view): counter, sink, dishwasher, storage, robot home."""
    rect(s, x, y, w, h, fill='FFFFFF', line=EDGE, lw=0.75)
    text(s, x + 0.08, y + 0.05, w - 0.16, 0.22, name, size=8.5, bold=True, check=False)
    cy = y + 0.32; ch = 0.3
    if kind == 'I':
        segs = [(0.0, 0.14, 'home'), (0.14, 0.42, 'cnt'), (0.42, 0.62, 'sink'), (0.62, 0.8, 'st'), (0.8, 1.0, 'dw')]
        L = w - 0.24
        for a, b, k in segs: _part(s, x + 0.12 + a * L, cy, (b - a) * L, ch, k)
    elif kind == 'L':
        L = (w - 0.24) * 0.78
        segs = [(0.0, 0.18, 'home'), (0.18, 0.5, 'cnt'), (0.5, 0.78, 'sink'), (0.78, 1.0, 'dw')]
        for a, b, k in segs: _part(s, x + 0.12 + a * L, cy, (b - a) * L, ch, k)
        _part(s, x + 0.12 + L, cy, (w - 0.24) - L, h - 0.42, 'st')
    else:
        L = (w - 0.24) * 0.72
        segs = [(0.0, 0.14, 'home'), (0.14, 0.4, 'cnt'), (0.4, 0.68, 'sink'), (0.68, 1.0, 'st')]
        for a, b, k in segs: _part(s, x + 0.12 + a * L, cy, (b - a) * L, ch, k)
        _part(s, x + 0.12 + L + 0.1, cy, (w - 0.24) - L - 0.1, ch, 'dw')
    return cy + ch


def _part(s, x, y, w, h, k):
    fill, lab, col = {'home': ('FFFFFF', 'R', ACC), 'cnt': (SOFT2, '', INK), 'sink': ('C9D3DC', 'S', INK),
                      'st': ('E9EBEE', '수', INK2), 'dw': ('3A3F46', 'D', 'FFFFFF')}[k]
    sh = rect(s, x, y, w, h, fill=fill, line=ACC if k == 'home' else 'FFFFFF', lw=1.0 if k == 'home' else 0.5)
    if lab: text(s, x, y, w, h, lab, size=7.5, bold=True, color=col, align='c', anchor='m', check=False)


def m07(prs):
    s = start(prs, 'm07', pg(prs), '핵심 기술: Calibration 기반 Skill의 주방 간 이전',
              visual='상단: Skill 실행 5단계 체인 (감지 → 파지 → 조작 → 검증 → 복구, 실패 시 복구 루프). 하단: 서로 다른 주방 3종 평면 도식 → Calibration 4요소 → 같은 CLEAN Skill Library.',
              chart='실행 체인 + Calibration 흐름도 (평면 도식 3개)',
              note=('- Skill = Software 구독이 아닌 Robot이 수행 가능한 작업을 늘리는 Layer\n'
                    '- 모든 Skill = 감지 → 파지 → 조작 → 검증 → 복구의 같은 구조 · 실패 감지 시 다시 잡기 · 내려놓기\n'
                    '- 핵심 = Skill의 주방 간 이전: 설치 시 주방 Mapping · 기준점 좌표 Calibration · 가전 · 수납 위치 등록 · 작업 Parameter 조정\n'
                    '- M18 검증: 구조 · 가전 모델이 다른 주방 3종에서 재배치 후 성공률 하락 ≤ 10%p · 현장 Calibration ≤ 4시간'))
    y = mhead(s, '07  Manipulation Skill · Calibration', '핵심 기술: Calibration 기반 Skill의 주방 간 이전',
              'Skill = Robot이 수행 가능한 작업을 늘리는 확장 Layer (Software 구독 아님)')
    steps = [('01', '감지', '물체 · 위치 인식'), ('02', '파지', '파지점 · 파지력'), ('03', '조작', '이동 · 삽입'),
             ('04', '검증', '완료 확인'), ('05', '복구', '다시 잡기 · 내려놓기')]
    gap = 0.3; bw = (CW - 4 * gap) / 5; bh = 0.92
    for i, (n, a, b) in enumerate(steps):
        bx = MX + i * (bw + gap)
        rect(s, bx, y, bw, bh, fill=SOFT)
        text(s, bx + 0.14, y + 0.1, 0.5, 0.24, n, size=9, bold=True, color=GREY, check=False)
        text(s, bx + 0.14, y + 0.3, bw - 0.28, 0.32, a, size=14, bold=True)
        text(s, bx + 0.14, y + 0.62, bw - 0.28, 0.24, b, size=9.5, color=INK2)
        if i < 4: arrow(s, bx + bw + 0.03, y + bh / 2, bx + bw + gap - 0.03, y + bh / 2, color=GREY, lw=1.5)
    lx0 = MX + 3 * (bw + gap) + bw / 2; lx1 = MX + 1 * (bw + gap) + bw / 2
    seg(s, lx0, y + bh, lx0, y + bh + 0.18, color=INK2, lw=1.25, dash=True)
    seg(s, lx1, y + bh + 0.18, lx0, y + bh + 0.18, color=INK2, lw=1.25, dash=True)
    arrow(s, lx1, y + bh + 0.18, lx1, y + bh + 0.01, color=INK2, lw=1.25)
    text(s, lx1 + 0.12, y + bh + 0.22, 3.5, 0.22, '실패 감지 → 다시 잡기 · 내려놓기', size=8.5, color=INK2, check=False)
    y2 = y + bh + 0.5
    text(s, MX, y2, 6, 0.26, '다른 주방 → Calibration → 같은 Skill', size=11, bold=True, color=GREY)
    ky = y2 + 0.32; kw = 2.35; kh = 0.8
    kits = [('주방 A · ㅡ자 3.2m · 빌트인 식세기', 'I'), ('주방 B · ㄱ자 · 짧은 싱크 벽', 'L'), ('주방 C · Retrofit · 독립형 식세기', 'R')]
    for i, (nm, kd) in enumerate(kits):
        _kitchen_tile(s, MX, ky + i * (kh + 0.1), kw, kh, nm, kd)
    cx = MX + kw + 0.55; cw2 = 3.6
    ctop = ky; cbot = ky + 3 * kh + 0.2
    for i in range(3):
        yy = ky + i * (kh + 0.1) + kh / 2
        arrow(s, MX + kw + 0.04, yy, cx - 0.04, (ctop + cbot) / 2, color=GREY, lw=1.0)
    rect(s, cx, ctop, cw2, cbot - ctop, fill=INK)
    text(s, cx + 0.2, ctop + 0.14, cw2 - 0.4, 0.3, 'Calibration (설치 시)', size=13, bold=True, color='FFFFFF')
    items = ['주방 Mapping', '좌표 Calibration (Dock · 기준점)', '가전 · 수납 위치 등록', '작업 Parameter 조정']
    for i, it in enumerate(items):
        yy = ctop + 0.52 + i * 0.5
        rect(s, cx + 0.2, yy, cw2 - 0.4, 0.4, fill='2C3036')
        text(s, cx + 0.32, yy, cw2 - 0.6, 0.4, it, size=10.5, bold=True, color='FFFFFF', anchor='m')
    sx = cx + cw2 + 0.5; sw = W - MX - sx
    arrow(s, cx + cw2 + 0.04, (ctop + cbot) / 2, sx - 0.04, (ctop + cbot) / 2, color=GREY, lw=1.5)
    rect(s, sx, ctop, sw, cbot - ctop, fill='FFFFFF', line=INK, lw=1.25)
    text(s, sx + 0.2, ctop + 0.14, sw - 0.4, 0.3, '같은 CLEAN Skill Library', size=13, bold=True)
    for i, it in enumerate(['식기 집기 (Pick)', '식세기 적재 (Loading)', '식세기 인출 (Unloading)', '수납 복귀 (Return)']):
        yy = ctop + 0.52 + i * 0.5
        rect(s, sx + 0.2, yy, sw - 0.4, 0.4, fill=SOFT)
        text(s, sx + 0.32, yy, sw - 0.6, 0.4, it, size=10.5, bold=True, anchor='m')
    gy = cbot + 0.12
    text(s, MX, gy, CW, 0.3, [[('M18 검증 (TARGET)  ', {'bold': True, 'color': INK}),
                               ('구조 · 가전 모델이 다른 주방 3종에서 재배치 후 성공률 하락 ≤ 10%p · 현장 Calibration ≤ 4시간', {'color': INK})]], size=11)
    note(s, 'R Robot Home · S 싱크 · D 식세기 · 수 수납 (평면 도식 = CONCEPT) · KPI 근거: 부록 A1~A2')
    mfoot(s)


# ================================================================= 08 system architecture
def m08(prs):
    s = start(prs, 'm08', pg(prs), 'MH Kitchen Robotics System: 5개 Layer 통합 제품',
              visual='좌측 대표 콘셉트 렌더 (주황 = Robot Working Zone, 회색 점선 = Human Zone) + Interface 위치 표시. 우측 A~E 5개 층 카드 (Robot Module · Manipulation · Calibration · Environment Interface · Safety).',
              chart='3D 콘셉트 렌더 (CONCEPT) + 5층 Architecture',
              note=('- 제품 = 5개 Layer 통합 (A Robot Module · B Manipulation · C Calibration · D Environment Interface · E Safety)\n'
                    '- A: Robot Arm (OEM 구매) · Adaptive Hand · Vision · 힘 · 안전 센서 · 필요 시 Rail · Dock\n'
                    '- B: 물체 인식 → 파지 · 경로 계획 → 실행 → 실패 감지 · 복구 / C: 주방 Mapping · 좌표 · 가전 · 수납 위치 등록\n'
                    '- D: Robot Home · 도구 · 수납 Dock · 가전 Interface · Vision 기준점 / E: 사람 감지 · 감속 · 충돌 감지 · 비상정지 · 안전 복귀\n'
                    '- 왜 Arm: 식세기 랙 · 서랍 · 상부장 작업 = 6축 방향 제어 필요 · 이동형은 낮은 작업점 · 가격 · 안전 부담\n'
                    '- Robot OEM과의 차이: Arm은 구매 · MH는 Hand · Skill · Calibration · Interface · Safety · Care로 주방 System 구성\n'
                    '- 주황 = Robot 작업 구역 · 회색 점선 = 사람 구역 (설계 개념)'))
    y = mhead(s, '08  MH Kitchen Robotics System', 'MH Kitchen Robotics System: 5개 Layer 통합 제품',
              '왜 Arm: 식세기 랙 · 서랍 · 상부장 작업 = 6축 방향 제어 필요 · 이동형 = 낮은 작업점 · 가격 · 안전 부담')
    lw = 6.55; lh = H - 0.62 - y - 0.45
    at = render(s, 'v2_after', MX, y, lw, lh, focus=(0.47, 0.5), zoom=1.08)
    callout(s, at, 'garage', 'D · Robot Home', -0.2, -0.38, size=8.5, side='l')
    callout(s, at, 'drop', 'D · Drop Zone', -0.25, 0.42, size=8.5, side='l')
    callout(s, at, 'dw', 'D · 식세기 Interface', 0.25, 0.45, size=8.5)
    callout(s, at, 'robotZone', 'E · Robot Zone', 0.35, -0.55, size=8.5)
    callout(s, at, 'humanZone', 'E · Human Zone', 0.4, 0.3, size=8.5)
    mt(s, MX + 0.08, y + 0.08, 'CONCEPT', fill='FFFFFF')
    rx = MX + lw + 0.3; rw = W - MX - rx
    L = [('A', 'Robot Module', 'Robot Arm (OEM 구매) · Adaptive Hand (M6 Build/Buy) · Vision · 힘 · 안전 센서 · 필요 시 Rail / Dock'),
         ('B', 'Manipulation Layer', '물체 인식 · 파지 계획 · 경로 계획 · 작업 실행 · 실패 감지 · 복구'),
         ('C', 'Calibration Layer', '주방 Mapping · 좌표 Calibration · 가전 · 수납 위치 등록 · 작업 Parameter'),
         ('D', 'Environment Interface', 'Robot Home · Tool Dock · 수납 Dock · 가전 Interface · Vision 기준점 · 필요 시 작업면 Guide'),
         ('E', 'Human-Robot Safety', '사람 감지 · 감속 · 충돌 감지 · 비상정지 · 안전 복귀 (Safe Home Return)')]
    ch = (lh - 4 * 0.1) / 5
    for i, (k, t, d) in enumerate(L):
        cy = y + i * (ch + 0.1)
        rect(s, rx, cy, rw, ch, fill=SOFT)
        rect(s, rx, cy, 0.42, ch, fill=INK)
        text(s, rx, cy, 0.42, ch, k, size=15, bold=True, color='FFFFFF', align='c', anchor='m')
        text(s, rx + 0.56, cy + 0.08, rw - 0.68, 0.3, t, size=12.5, bold=True)
        text(s, rx + 0.56, cy + 0.38, rw - 0.68, ch - 0.42, d, size=9.5, color=INK2, line=1.02)
    note(s, '안전 기준: ISO 10218-2:2025 (감속 250mm/s · 접촉력) · 가정용 IEC 63682 (2026 초안) · ISO 13482 [S39 · S47]')
    mfoot(s)


# ================================================================= 09 CLEAN -> ASSIST -> COOK
def m09(prs):
    s = start(prs, 'm09', pg(prs), 'CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장',
              visual='상단 CLEAN 5단계 콘셉트 렌더 (식기 인식 → 집기 → 식세기 적재 → 인출 → 수납 복귀, 각 CONCEPT). 중간 CLEAN 검증 기술 칩 9개. 하단 CLEAN · ASSIST · COOK 3단계 카드 (같은 Platform + Skill · Tool 확장).',
              chart='3D 콘셉트 렌더 5컷 (CONCEPT) + 단계 카드',
              note=('- 첫 기술검증 Workflow = CLEAN: 조리대 한쪽 식기 인식 → 집기 → 식세기 적재 → 세척 후 인출 → 수납장 복귀\n'
                    '- CLEAN 목적 = 식기 정리 시장이 아닌 Platform 전체 (적응 파지 · 가전 · 수납 조작 · Calibration · 안전 · 실패 복구 · 반복 실행)의 첫 End-to-End 검증\n'
                    '- 이후 같은 Robot에 ASSIST Skill (재료 이동 · 투입 · 젓기 · 뚜껑 · 도구) 추가 → 장기 Recipe 단위 COOK\n'
                    f"- CLEAN 단독 가사대체 가치 월 약 {M['value']['value']:.0f}만원 < Rental 월 {A('p_rent')}만원 → 지불의사 = Premium 고객 · ASSIST 묶음으로 검증 (M18)\n"
                    '- COOK = 현재 검증 결과가 아닌 장기 R&D 방향 (FUTURE)'))
    y = mhead(s, '09  첫 검증 Workflow', 'CLEAN 첫 검증 → 동일 Platform으로 ASSIST · COOK 확장',
              '단계별 새 로봇 개발이 아닌, 같은 Platform에 Skill · Tool 추가')
    seq = [('v2_seq_1_detect', '① 식기 인식'), ('v2_seq_2_pick', '② 집기 (Pick)'), ('v2_seq_3_load', '③ 식세기 적재'),
           ('v2_seq_4_unload', '④ 식세기 인출'), ('v2_seq_5_store', '⑤ 수납 복귀')]
    gap = 0.14; tw = (CW - 4 * gap) / 5; th = 1.45
    for i, (nm, lab) in enumerate(seq):
        tx = MX + i * (tw + gap)
        render(s, nm, tx, y, tw, th, focus=(0.5, 0.5), zoom=1.05)
        mt(s, tx + 0.05, y + 0.05, 'CONCEPT', size=5.5, h=0.14, fill='FFFFFF')
        rect(s, tx, y + th, tw, 0.3, fill=INK if i in (2, 3) else SOFT)
        text(s, tx, y + th, tw, 0.3, lab, size=9.5, bold=True, color='FFFFFF' if i in (2, 3) else INK, align='c', anchor='m')
    vy = y + th + 0.42
    text(s, MX, vy, 1.4, 0.28, 'CLEAN 검증', size=10, bold=True, color=GREY, anchor='m')
    xx = MX + 1.15
    for t in ['적응 파지', '물체 인식', '경로 계획', '가전 조작', '수납 조작',
              'Calibration', '안전', '실패 복구', '반복 실행']:
        wv = kit.text_w(t, 8.5, True) + 0.14
        rect(s, xx, vy, wv, 0.28, fill=SOFT2)
        text(s, xx, vy, wv, 0.28, t, size=8.5, bold=True, align='c', anchor='m', check=False)
        xx += wv + 0.045
    assert xx < W - MX + 0.05, xx
    cy = vy + 0.5
    stages = [('CLEAN', '초기 · 기술검증', '식기 이동 · 식세기 적재 · 인출 · 수납 복귀', INK, 'FFFFFF', None,
               '기본 Skill 4종 · 식세기 Interface · 수납 Dock'),
              ('ASSIST', '중기 · 기능 확장', '재료 이동 · 재료 투입 · 젓기 · 뚜껑 조작 · 도구 조작', SOFT, INK, None,
               'ASSIST Skill Pack · 집게 · 국자 · 뚜껑 Tool'),
              ('COOK', '장기 · R&D 방향', 'Recipe Workflow · 복수 Skill 연결 · 가전 연동 · 조리 · 조리 후 정리', 'FFFFFF', INK, 'FUTURE',
               'Recipe Skill · 식재료 Tool · 열 · 액체 안전')]
    sw = (CW - 2 * 0.42) / 3; sh = H - 0.62 - 0.32 - cy
    for i, (t, k, d, fill, col, tg, add) in enumerate(stages):
        sx = MX + i * (sw + 0.42)
        rect(s, sx, cy, sw, sh, fill=fill, line=EDGE if fill == 'FFFFFF' else None, lw=0.75)
        text(s, sx + 0.2, cy + 0.12, sw - 0.4, 0.22, k, size=9, bold=True, color='A9AEB5' if fill == INK else GREY, check=False)
        text(s, sx + 0.2, cy + 0.34, sw - 0.4, 0.42, t, size=19, bold=True, color=col)
        text(s, sx + 0.2, cy + 0.82, sw - 0.4, 0.62, d, size=10.5, color='D5D8DC' if fill == INK else INK2, line=1.05)
        hline(s, sx + 0.2, cy + sh - 0.62, sw - 0.4, color='3A3F46' if fill == INK else EDGE)
        text(s, sx + 0.2, cy + sh - 0.56, sw - 0.4, 0.22, '추가되는 것', size=8.5, bold=True, color='A9AEB5' if fill == INK else GREY, check=False)
        text(s, sx + 0.2, cy + sh - 0.33, sw - 0.4, 0.26, add, size=9.5, bold=True, color=col, check=False)
        if tg: mt(s, sx + sw - 1.05, cy + 0.14, tg)
        if i < 2: arrow(s, sx + sw + 0.04, cy + sh / 2, sx + sw + 0.38, cy + sh / 2, color=GREY, lw=1.5)
    note(s, f"CLEAN 단독 가사대체 가치 ≈ 월 {M['value']['value']:.0f}만원 < Rental 월 {A('p_rent')}만원 (DERIVED) → 지불의사 = Premium 고객 · ASSIST 묶음으로 검증 (M18) · COOK = 장기 R&D (FUTURE)", y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 10 channels
def _flow_install(s, x, y, w, h, name, labels):
    """m10 column image: same kitchen run · same camera · Integration 수준별 MH 요소 (CONCEPT). labels = (anchor, text, dx, dy, side)."""
    rect(s, x, y, w, h, fill=SOFT)
    at = render(s, name, x, y, w, h, focus=(0.555, 0.655), zoom=1.36, bg=(244, 245, 246))
    for key, txt, dx, dy, side in labels:
        callout(s, at, key, txt, dx, dy, size=8, side=side)
    mt(s, x + 0.05, y + 0.05, 'CONCEPT', size=5.5, h=0.14, fill='FFFFFF')


def m10(prs):
    hr, hrt, hnb = HH('purchase_direct_Y3'), HH('retrofit_purchase_Y3'), HH('newbuild_purchase_Y3')
    kl = M['kpi_links']
    s = start(prs, 'm10', pg(prs), '단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · 신축)',
              visual='상단 3열 머리 (Retrofit · Integration · 설계 반영 + Integration 수준 막대). 열마다 같은 주방 · 같은 시점 3D 콘셉트 렌더 1개 (CONCEPT): 기존 주방 = Compact Mount · Vision 기준점 · Drop Zone (Rail 없음) / Remodeling = Rail · Robot Home · 수납 Dock · 식세기 Interface / New-build = Tool Dock · Service 공간 · 전원 · 통신 매립. 주황 = Robot Zone · Path만. 아래 압축 비교표 6행 (고객 상황 · 공사 범위 · Interface · 설치 · MH 매출 가설 · 역할). 하단 MH Core vs Partner 띠.',
              chart='3D 콘셉트 렌더 3컷 (CONCEPT, 동일 시점) + Integration 수준 막대 + 3열 비교표',
              note=('- 제품 1개 · 설치 경로 3개 (Integration 수준만 차등)\n'
                    '- Retrofit (기존 주방): 호환성 확인 → Compact Mount · Dock · Vision 기준점만 설치 · 현장 Calibration 비중 큼\n'
                    '- Remodeling: 주방 교체 시 Rail · Robot Home · 식세기 Interface · 수납 Dock 동시 시공 = 첫 검증 채널\n'
                    '- New-build: 설계 단계에서 Mount · 전원 · 통신 · Tool Dock · 가전 Interface · Service 공간 반영 → 입주 시 또는 후설치\n'
                    '- MH Core = Robot · Hand · Skill · Calibration · Interface 표준 · 안전 · 시운전 · 품질 / Partner = 철거 · 가구 · 전기 · 배관 · 일반 시공'))
    y = mhead(s, '10  Existing / Remodeling / New-build', '단일 제품 · 3가지 설치 경로 (기존 주방 · Remodeling · 신축)',
              '주방 전체 획일화 없이 Integration 수준만 차등 적용')
    lab_w = 1.55; cw = (CW - lab_w) / 3
    heads = [('Existing Kitchen', 'Retrofit', 1), ('Remodeling', 'Integration', 2), ('New-build', '설계 반영', 3)]
    iy, ih = y + 0.62, 1.6
    imgs = [('fig_flow_retrofit', [('fid1', 'Vision 기준점', -0.05, 0.6, 'c'), ('drop', 'Drop Zone', 0.0, 0.62, 'c'),
                                   ('mount', 'Compact Mount', 0.72, 0.62, 'l')]),
            ('fig_flow_remodel', [('railR', 'Rail', 0.35, 0.25, 'r'), ((360, 400), 'Robot Home', 0.1, 0.6, 'r'),
                                  ('drawer', '수납 Dock', -0.2, 0.45, 'l'), ('dw', '식세기 Interface', 0.8, 0.35, 'l')]),
            ('fig_flow_newbuild', [('tooldock', 'Tool Dock', 0.25, 0.62, 'r'), ('service', 'Service 공간', 0.25, 0.5, 'r'),
                                   ('lineR', '전원 · 통신', -0.05, 0.62, 'l')])]
    for i, (a, b, lv) in enumerate(heads):
        cx = MX + lab_w + i * cw
        text(s, cx + 0.08, y, cw - 0.16, 0.3, a, size=14, bold=True)
        text(s, cx + 0.08, y + 0.32, 1.6, 0.22, b, size=9, bold=True, color=GREY)
        bx0 = cx + cw - 0.08 - 3 * 0.3 - 2 * 0.06
        for j in range(3):
            rect(s, bx0 + j * 0.36, y + 0.38, 0.3, 0.1, fill=INK if j < lv else SOFT2)
        text(s, bx0 - 1.12, y + 0.32, 1.04, 0.22, 'Integration 수준', size=8, color=GREY, align='r', check=False)
        _flow_install(s, cx + 0.08, iy, cw - 0.16, ih, *imgs[i])
    text(s, MX, iy, lab_w - 0.1, 0.24, '설치 형태', size=9, color=INK)
    rows = [
        ['고객 상황', '주방 유지 · 호환 주방', '주방 교체 시점 (Premium)', '분양 · 입주 전 (건설사 · 가구사)'],
        ['공사 범위', '최소 시공 (Mount · Dock)', '주방 공사와 동시 (Partner 시공)', '설계 단계에서 반영'],
        ['Interface', 'Compact Mount · Dock · Vision 기준점 · Drop Zone', 'Rail · Robot Home · 식세기 Interface · 수납 Dock',
         'Mount · 전원 · 통신 · Tool Dock · 가전 Interface · Service\u00a0공간'],
        ['설치 · Calibration', f"현장 Calibration 중심 · Y3 원가 {A('comm_cost_rt')[2]}만원 (약 {kl['inst_h_rt'][2]:.0f}인시)",
         f"Y3 원가 {A('comm_cost')[2]}만원 (약 {kl['inst_h'][2]:.0f}인시 = 2인 약 1일)", '입주 시 또는 후설치 (Option 세대)'],
        ['MH 매출 (가설)', f"Kit {A('p_rt_if')} + Robot {A('p_robot'):,} + 설치 {A('p_comm_rt')} = {hrt['y0']:,.0f}만원",
         f"Interface {A('p_rr')} + Robot {A('p_robot'):,} + 설치 {A('p_comm')} = {hr['y0']:,.0f}만원",
         f"Option {A('p_rr_new')}만원 (B2B) + 입주 Attach {A('new_attach') * 100:.0f}% × (Robot + 설치)"],
        ['역할', ('Phase 2 · 고객 확대', {'bold': True}), ('Phase 1 · 검증 채널', {'bold': True}), ('Phase 3 · Scale 채널', {'bold': True})],
    ]
    by = H - 0.62 - 0.32 - 0.42
    ty = iy + ih + 0.1
    table(s, MX, ty, CW, None, rows, col_w=[lab_w, cw, cw, cw], size=9, label='m10', pad=0.04, max_h=by - 0.08 - ty)
    rect(s, MX, by, CW, 0.42, fill=INK)
    text(s, MX + 0.2, by, CW - 0.4, 0.42, [[('MH Core  ', {'bold': True, 'color': 'FFFFFF'}),
                                           ('Robot · Hand · Skill · Calibration · Interface Standard · Safety · Commissioning · QA', {'color': 'E3E5E8'}),
                                           ('     Partner  ', {'bold': True, 'color': 'A9AEB5'}),
                                           ('철거 · 가구 · 전기 · 배관 · 일반 시공', {'color': 'A9AEB5'})]], size=10.5, anchor='m')
    note(s, '가격 · 원가 = ASSUMPTION · VAT · 주방 공사비 별도 · 인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 (부록 D)', y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 11 business model
def m11(prs):
    h3, h5 = HH('purchase_direct_Y3'), HH('purchase_direct_Y5')
    pi = M['partner_irr']['B']; cons = M['cons']; Bs = M['scenarios']['B']
    s = start(prs, 'm11', pg(prs), '설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM',
              visual='좌측 3층 사업모델 (INSTALL · OPERATE · EXPAND: 항목 + 가격 가설). 우측 상단 대표 1세대 5년 매출 막대 (층별) + Contribution. 우측 하단 Rental 구조 도식 (고객 · Capital Partner · MH).',
              chart='층별 가로 막대 + Rental 3자 구조도',
              note=('- BM 3층: INSTALL (Robot System · Interface · 설치) → OPERATE (Rental · Care · 소모품) → EXPAND (ASSIST Skill · Tool · 이후 COOK Skill · Upgrade)\n'
                    f"- Remodeling 구매 1세대 5년: 설치 {h3['layers']['install']:,.0f}만원 · 운영 {h3['layers']['operate']:,.0f}만원 · 확장 {h3['layers']['expand']:,.0f}만원\n"
                    f"- 5년 기여이익 {h3['contrib5']:,.0f}만원 (Y3 원가) → {h5['contrib5']:,.0f}만원 (Y5 원가)\n"
                    f"- 반복 · 확장매출 = Y5 매출의 {Bs['oe_share'][4] * 100:.0f}% (설치 초기 구조) → Installed Base 누적 후 비중 확대\n"
                    '- Rental = 고객 초기 부담 완화 수단 · Pilot은 MH 직접 · Scale은 렌탈 · 캐피탈 Partner 자산 보유 (MH = 제품 · SW · Care)\n'
                    f"- Partner 단순 회수 약 {pi['payback']:.0f}개월 > 요구 {pi['hurdle']}개월 (가정) → 매입가율 · 서비스료 · 기간 협의 필요"))
    y = mhead(s, '11  Business Model', '설치 매출 → 사용 기간 반복매출 → 기능 확장매출의 3층 BM',
              'INSTALL → OPERATE → EXPAND · Hardware 외 매출 = 실제 유지관리 · 기능가치 기반')
    lw = 7.25
    layers = [('INSTALL', '초기 매출', [('Robot System (Arm · Adaptive Hand · Vision · Safety)', f"{A('p_robot'):,}만원"),
                                       ('Interface · Integration', f"{A('p_rt_if')}~{A('p_rr')}만원"), ('설치 · Calibration', f"{A('p_comm')}~{A('p_comm_rt')}만원")]),
              ('OPERATE', '반복매출', [('Rental (60개월, Care · Grip Kit 포함)', f"월 {A('p_rent')}만원"), ('Care (Robot Lifecycle Maintenance)', f"연 {A('p_care')}만원"),
                                      ('Consumables (Pad · Seal · Tip · Cover)', f"연 {cons['list_y']:.0f}만원 (List)")]),
              ('EXPAND', '확장매출', [('ASSIST Skill Pack', f"{A('p_sw')}만원"), ('Tool · End-effector', f"{A('p_tool')}만원"),
                                     ('COOK Skill · Robot Upgrade', 'FUTURE')])]
    lh = 1.28
    for i, (k, kd, items) in enumerate(layers):
        ly = y + i * (lh + 0.14)
        rect(s, MX, ly, lw, lh, fill=SOFT)
        rect(s, MX, ly, 1.45, lh, fill=INK)
        text(s, MX, ly + 0.3, 1.45, 0.36, k, size=14, bold=True, color='FFFFFF', align='c')
        text(s, MX, ly + 0.7, 1.45, 0.26, kd, size=9.5, color='A9AEB5', align='c')
        for j, (a, b) in enumerate(items):
            iy = ly + 0.16 + j * 0.36
            text(s, MX + 1.65, iy, lw - 3.4, 0.3, a, size=10.5, anchor='m')
            text(s, MX + lw - 1.75, iy, 1.6, 0.3, b, size=10.5, bold=True, align='r', anchor='m')
        if i < 2: arrow(s, MX + 0.72, ly + lh + 0.01, MX + 0.72, ly + lh + 0.13, color=GREY, lw=1.25)
    mts(s, MX, y + 3 * (lh + 0.14) - 0.06, ['ASSUMPTION'], label='가격 = ASSUMPTION (VAT 별도)')
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y, rw, 0.26, '대표 1세대 · 5년 (Remodeling 구매, Y3 원가)', size=10.5, bold=True, color=GREY)
    tot = h3['rev5']; segs = [('INSTALL', h3['layers']['install'], INK), ('OPERATE', h3['layers']['operate'], '6B7078'), ('EXPAND', h3['layers']['expand'], 'B4B8BE')]
    bx = rx; by = y + 0.34; bw = rw
    for nm, v, col in segs:
        ww = bw * v / tot
        rect(s, bx, by, ww, 0.42, fill=col)
        bx += ww
    text(s, rx, by + 0.48, rw, 0.26, '  ·  '.join(f'{nm} {v:,.0f}' for nm, v, _ in segs) + f'  =  {tot:,.0f}만원', size=9.5, color=INK2)
    knum(s, rx, by + 0.86, rw / 2 - 0.1, f"{h3['contrib5']:,.0f}만원", f"5년 기여이익 (Y3 원가, 이익률 {h3['cm5'] * 100:.0f}%)", 'DERIVED', vsize=20, lsize=9)
    knum(s, rx + rw / 2 + 0.1, by + 0.86, rw / 2 - 0.1, f"{h5['contrib5']:,.0f}만원", f"Y5 원가 (BOM · 설치 · Care 하락, {h5['cm5'] * 100:.0f}%)", 'DERIVED', vsize=20, lsize=9, color=INK)
    ry = by + 2.08
    text(s, rx, ry, rw, 0.26, 'Rental 구조 (Scale 단계)', size=10.5, bold=True, color=GREY)
    bw3 = (rw - 2 * 0.36) / 3; byy = ry + 0.32
    for i, (t, d) in enumerate([('고객', '월 납부'), ('Capital Partner', 'Robot 자산 보유'), ('MH', '제품 · SW · Care')]):
        bx3 = rx + i * (bw3 + 0.36)
        rect(s, bx3, byy, bw3, 0.62, fill=INK if i == 2 else SOFT)
        text(s, bx3, byy + 0.06, bw3, 0.28, t, size=10.5, bold=True, color='FFFFFF' if i == 2 else INK, align='c')
        text(s, bx3, byy + 0.33, bw3, 0.24, d, size=8.5, color='C9CDD2' if i == 2 else INK2, align='c')
        if i < 2: arrow(s, bx3 + bw3 + 0.03, byy + 0.31, bx3 + bw3 + 0.33, byy + 0.31, color=GREY, lw=1.25)
    text(s, rx, byy + 0.7, rw, 0.62, [f"월 {A('p_rent')}만원 · Partner가 Robot을 ASP의 {A('wholesale') * 100:.0f}%에 매입 · MH 서비스료 월 {A('partner_fee'):.0f}만원",
                                       f"Partner IRR 약 {pi['irr_y'] * 100:.1f}% · 단순 회수 약 {pi['payback']:.0f}개월 > 요구 {pi['hurdle']}개월 (가정) → 조건 협의"], size=9, color=INK2, line=1.02)
    note(s, f"Care = 정기 안전점검 · Calibration · 원격진단 · A/S (가입 {A('care_attach') * 100:.0f}% 가정 → 실증 3세대로 확인, M24) · 소모품 = 마모 · 위생 기반 (교체주기 시험 후 확정) · "
            f"반복매출 Y3 {Bs['recurring'][2] / 1e4:.1f} → Y5 {Bs['recurring'][4] / 1e4:.1f}억원 (Installed Base {Bs['base_end'][4]:,.0f}대) · Y5 매출 중 OPERATE + EXPAND {Bs['oe_share'][4] * 100:.0f}% (DERIVED) · 선례: 코웨이 렌탈 748만 계정 · LG 구독 2조원+ [S12 · S41]")
    mfoot(s)


# ================================================================= 12 market
def m12(prs):
    mk = M['market']['B']; B = M['scenarios']['B']
    s = start(prs, 'm12', pg(prs), 'Bottom-up 시장 산정: 세대 수 × 적용률 × 단가',
              visual='좌측 짙은 박스: 아파트 재고 1,328만호 (기회 기반) + 노후 · 거래 FACT. 우측 4개 시장 Funnel 표 (산식 · 대상 세대 · 패키지 단가 · 연 규모) + SAM 합계 · SOM.',
              chart='Bottom-up 시장 표',
              note=('- 시장 산정 = 큰 TAM이 아닌 세대 수 × 적용률 × 단가\n'
                    f"- 국내 아파트 약 {mk['apt'] / 10:,.0f}만호 = 기회 기반 (구매자 수 아님)\n"
                    f"- Remodeling: 연 주방 교체 약 30만 × Premium 10% × 적용 60% = 연 약 {mk['fit'] / 10:.1f}만 세대 · {mk['sam_remodel']:,.0f}억원\n"
                    f"- Retrofit: 호환 기존 주방 약 {mk['retro_pool'] / 10:.1f}만 세대 × 연 0.5% = {mk['sam_retro']:,.0f}억원 · 신축 {mk['sam_new']:,.0f}억원\n"
                    f"- Y5 계획 매출 {mk['som']:.1f}억원 = 대상 세대의 약 {mk['som_share_hh'] * 100:.1f}%\n"
                    '- 비율 = 전부 가정 → 견적 20건 · 평면 30개 분석 · 소비자 조사로 검증'))
    y = mhead(s, '12  Market / Beachhead', 'Bottom-up 시장 산정: 세대 수 × 적용률 × 단가',
              '아파트 재고 = 기회 기반 (구매시장 아님) · 비율 = ASSUMPTION (검증 계획 부록 C3)')
    lw = 3.45; lh = H - 0.62 - 0.3 - y
    rect(s, MX, y, lw, lh, fill=INK)
    text(s, MX + 0.25, y + 0.2, lw - 0.5, 0.26, '국내 아파트 (2025)', size=10, bold=True, color='A9AEB5')
    text(s, MX + 0.25, y + 0.48, lw - 0.5, 0.75, f"{mk['apt'] / 10:,.0f}만호", size=36, bold=True, color='FFFFFF')
    mts(s, MX + 0.25, y + 1.25, ['DERIVED'], fill=INK)
    facts = [('총주택 2,018만호 × 아파트 65.8%', 'FACT'), ('준공 20년 이상 주택 56.0%', 'FACT'), ('주택 매매 72.6만호 (2025)', 'FACT'),
             ('아파트 입주 23.6만 (2025) · 18.3만 (2026 예정)', 'FACT')]
    for i, (t, tg) in enumerate(facts):
        yy = y + 1.65 + i * 0.52
        text(s, MX + 0.25, yy, lw - 0.5, 0.42, t, size=10, color='E3E5E8', line=1.02)
    text(s, MX + 0.25, y + lh - 0.62, lw - 0.5, 0.5, 'Stock ≠ 구매시장', size=9, color='A9AEB5', line=1.02)
    rx = MX + lw + 0.3; rw = W - MX - rx
    hdr = ['시장', '산식 (세대 × 적용률)', '대상 세대', '패키지', '연 규모']
    rows = [[('① Remodeling\nBeachhead', {'bold': True}), f"주방 교체 30만 × Premium 10% × 적용 60% · Robot Attach 85%", f"{mk['fit'] * 1000:,.0f}/년", f"{kit.nf(mk['pkg_remodel'])}만원", (f"{mk['sam_remodel']:,.0f}억원", {'bold': True})],
            [('② Retrofit', {'bold': True}), f"1,328만 × Premium 10% × 식세기 60% × 호환 40% = {mk['retro_pool'] / 10:.1f}만 (재고) × 연 0.5%", f"{mk['retro_annual'] * 1000:,.0f}/년", f"{mk['pkg_retro']:,.0f}만원", (f"{mk['sam_retro']:,.0f}억원", {'bold': True})],
            [('③ New-build', {'bold': True}), f"입주 20만 × Premium 단지 15% × Option 10%", f"{mk['new_opt'] * 1000:,.0f}/년", f"{kit.nf(mk['pkg_new'])}만원", (f"{mk['sam_new']:,.0f}억원", {'bold': True})],
            [('④ Recurring', {'bold': True}), f"Installed Base × 구매 고객 ARPU {mk['arpu']:.1f}만원/년 (Care · 소모품)", '1,000대당', '-', (f"{mk['recurring_per_1000']:.1f}억원", {'bold': True})]]
    th = table(s, rx, y, rw, hdr, rows, col_w=[1.35, rw - 1.35 - 1.0 - 0.95 - 1.05, 1.0, 0.95, 1.05], size=9.5,
               align=['l', 'l', 'r', 'r', 'r'], label='m12', pad=0.07)
    sy = y + th + 0.22
    sw = (rw - 0.3) / 2
    rect(s, rx, sy, sw, 1.05, fill=SOFT)
    text(s, rx + 0.2, sy + 0.12, sw - 0.4, 0.26, 'SAM 합계 (① + ② + ③)', size=10, bold=True, color=GREY)
    text(s, rx + 0.2, sy + 0.4, sw - 0.4, 0.5, f"연 {mk['sam']:,.0f}억원", size=22, bold=True)
    rect(s, rx + sw + 0.3, sy, sw, 1.05, fill='FFFFFF', line=INK, lw=1.0)
    text(s, rx + sw + 0.5, sy + 0.12, sw - 0.4, 0.26, 'Y5 계획 매출 (Base · TARGET)', size=10, bold=True, color=GREY)
    text(s, rx + sw + 0.5, sy + 0.4, sw - 0.4, 0.5, f"{mk['som']:.1f}억원 · {B['kitchens'][4]:,.0f}세대", size=22, bold=True, color=ACC)
    text(s, rx + sw + 0.5, sy + 0.78, sw - 0.4, 0.24, f"대상 세대의 약 {mk['som_share_hh'] * 100:.1f}% (DERIVED)", size=8.5, color=INK2, check=False)
    note(s, f"적용 60% = 확보 평면 5종 (기본 배치 수용 1)보다 높은 가정 → 평면 30개 분석으로 검증 (M6) · 주방 교체 30만 = 교차검증 {mk['tri1'] / 10:.1f}만 · {mk['tri2'] / 10:.1f}만 기반 가정 · 출처 [S1~S6]",
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 13 GTM
def m13(prs):
    B = M['scenarios']['B']
    s = start(prs, 'm13', pg(prs), 'Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장',
              visual='상단 3단계 카드 (Phase 1 Premium Remodeling → Phase 2 Retrofit → Phase 3 New-build). 좌하단 연도별 설치 세대 누적 막대 (채널별, TARGET). 우하단 MH Core vs Partner 역할 분담 도식.',
              chart='3단계 카드 + 누적 막대 (Y1~Y5) + 역할 분담',
              note=('- 초기 Mass Market 진입 없음\n'
                    '- Phase 1 Premium 주방 Remodeling: 제품 · 가격 수용성 · 설치 · 사용성 검증 → 첫 Reference · 실제 고객 Data\n'
                    '- Phase 2 호환 주방 Retrofit: 전체 Remodeling 없이 적용 가능한 고객 확대\n'
                    '- Phase 3 신축 B2B2C: 건설사 · 주방가구사 경유 Project 단위 확장\n'
                    '- 설치 물량 증가 ≠ 본사 현장인력 비례 증가: 철거 · 가구 · 전기 · 배관 = Partner / MH = Robot · Hand · Skill · Calibration · 안전 · 시운전\n'
                    '- Partner 조건 = M18~M24 협의 · 확보 예정'))
    y = mhead(s, '13  GTM / Partner Distribution', 'Premium Remodeling 검증 → Retrofit → 신축 B2B2C 확장',
              '초기 Mass Market 진입 없음 · 검증 채널 (Remodeling) → 고객 확대 (Retrofit) → Scale 채널 (신축)')
    ph = [('Phase 1', 'Premium Kitchen Remodeling', 'Y2 실증 → Y3~', '목적: 제품 · 가격수용성 · 설치 · 사용성 검증 · 초기 Reference · 고객 Data', '직접 판매 + 주방 · 인테리어 Partner', '검증 채널'),
          ('Phase 2', 'Compatible Existing Retrofit', 'Y4~', '전체 Remodeling 없이 적용 가능한 고객 확대 · 호환성 Check 표준화', '설치 Partner 경유', '고객 확대'),
          ('Phase 3', 'New-build Apartment', 'Y3 계약 → Y5 입주', '건설사 · 주방가구사 B2B2C · Project 단위 Scale', 'Interface Option + 후설치', 'Scale 채널')]
    gap = 0.36; pw = (CW - 2 * gap) / 3; phh = 1.6
    for i, (a, b, t, d, ch, role) in enumerate(ph):
        px = MX + i * (pw + gap)
        rect(s, px, y, pw, phh, fill=INK if i == 0 else SOFT)
        c1 = 'FFFFFF' if i == 0 else INK; c2 = 'C9CDD2' if i == 0 else INK2
        text(s, px + 0.18, y + 0.12, pw - 0.36, 0.22, f'{a}  ·  {t}', size=9, bold=True, color='A9AEB5' if i == 0 else GREY, check=False)
        text(s, px + 0.18, y + 0.36, pw - 0.36, 0.34, b, size=13.5, bold=True, color=c1)
        text(s, px + 0.18, y + 0.74, pw - 0.36, 0.5, d, size=9.5, color=c2, line=1.02)
        text(s, px + 0.18, y + 1.26, pw - 0.36, 0.26, f'{ch}  ·  {role}', size=9, bold=True, color=c1, check=False)
        if i < 2: arrow(s, px + pw + 0.04, y + phh / 2, px + pw + gap - 0.04, y + phh / 2, color=GREY, lw=1.5)
    cy = y + phh + 0.3
    cw_ = 6.1; ch_ = H - 0.62 - 0.32 - cy
    text(s, MX, cy, cw_, 0.26, '설치 세대 (Base, TARGET)', size=10.5, bold=True, color=GREY)
    cats = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']
    ser = [('Remodeling 직접', [B['rd'][t] for t in range(5)]), ('Remodeling Partner', [B['rp'][t] for t in range(5)]),
           ('Retrofit', [B['rt'][t] for t in range(5)]), ('New-build 입주', [B['ni'][t] for t in range(5)])]
    column_chart(s, MX, cy + 0.3, cw_, ch_ - 0.62, cats, ser, [INK, '6B7078', 'A9AEB5', 'D5D8DC'], stacked=True, show_labels=False,
                 plot=(0.02, 0.1, 0.96, 0.78), size=9.5, gap=60)
    for t in range(5):
        tot = sum(v[t] for _, v in ser)
        px = MX + cw_ * (0.02 + 0.96 * (t + 0.5) / 5)
        vmax = max(sum(v[k] for _, v in ser) for k in range(5))
        py = cy + 0.3 + (ch_ - 0.62) * (0.1 + 0.78 * (1 - tot / vmax)) - 0.27
        text(s, px - 0.5, py, 1.0, 0.24, f'{tot:,.0f}', size=10, bold=True, align='c', check=False)
    lx = MX
    for i, (nm, _) in enumerate(ser):
        col = [INK, '6B7078', 'A9AEB5', 'D5D8DC'][i]
        rect(s, lx, cy + ch_ - 0.2, 0.18, 0.14, fill=col)
        tw = kit.text_w(nm, 8.5) + 0.1
        text(s, lx + 0.22, cy + ch_ - 0.25, tw, 0.24, nm, size=8.5, color=INK2, check=False)
        lx += 0.22 + tw + 0.2
    rx = MX + cw_ + 0.4; rw = W - MX - rx
    text(s, rx, cy, rw, 0.26, 'Product Company 구조', size=10.5, bold=True, color=GREY)
    bw2 = (rw - 0.3) / 2; bh2 = ch_ - 0.86
    rect(s, rx, cy + 0.32, bw2, bh2, fill=INK)
    text(s, rx + 0.16, cy + 0.42, bw2 - 0.32, 0.28, 'MH Core', size=12, bold=True, color='FFFFFF')
    text(s, rx + 0.16, cy + 0.74, bw2 - 0.32, bh2 - 0.5, ['Robot · Robot Hand', 'Manipulation Skill', 'Calibration', 'Interface 표준', '안전 · 시운전 · QA'],
         size=9.5, color='E3E5E8', line=1.0, space_after=1)
    rect(s, rx + bw2 + 0.3, cy + 0.32, bw2, bh2, fill=SOFT)
    text(s, rx + bw2 + 0.46, cy + 0.42, bw2 - 0.32, 0.28, 'Partner', size=12, bold=True)
    text(s, rx + bw2 + 0.46, cy + 0.74, bw2 - 0.32, bh2 - 0.5, ['철거 · 가구', '전기 · 배관', '일반 시공', '(신축) 건설사 · 가구사', '(Rental) 캐피탈 · 렌탈사'],
         size=9.5, color=INK2, line=1.0, space_after=1)
    text(s, rx, cy + 0.32 + bh2 + 0.1, rw, 0.42, '설치 물량 증가 ≠ 본사 현장인력 비례 증가', size=11.5, bold=True, color=INK, anchor='m')
    note(s, '선례: 건설사 · 가전사 구독 · 관리 번들 — LH 공공주택 5,400여 세대 · 압구정 재건축 약 7,000세대 선택지 (LG, 2026) [S41]',
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 14 technology-to-economics / moat
def m14(prs):
    kl = M['kpi_links']; h3, h5 = HH('purchase_direct_Y3'), HH('purchase_direct_Y5'); sh = M['sens_household']
    s = start(prs, 'm14', pg(prs), 'R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조',
              visual='좌측 연결 Diagram: R&D 4개 Lever → 결과 지표 → 공통 효과 (설치시간 · Engineering 비용 ↓, 반복설치 ↑) → Installed Base → 반복 · 확장 매출. 우측 KPI ↔ 원가 표 (Y2 · Y3 · Y5) + 민감도 상위 5개 막대. 하단 Moat 정의 띠.',
              chart='연결 Diagram + 표 + Tornado 막대',
              note=('- R&D 목표 = 성능 향상 자체가 아닌 Unit Economics · Scale 개선\n'
                    '- Hand 고도화 → 다룰 수 있는 물체 ↑ · Skill → 작업 범위 ↑ · Calibration → 신규 주방 적용시간 ↓ · Interface → 작업 신뢰성 ↑\n'
                    '- 결과: 설치시간 · Engineering 비용 ↓ · 반복설치 ↑ → Installed Base ↑ → Care · 소모품 · Skill 매출 ↑\n'
                    f"- 설치 · Calibration 원가 목표: Y2 실증 {A('comm_cost')[1]}만원 → Y3 {A('comm_cost')[2]}만원 → Y5 {A('comm_cost')[4]}만원 (설치 엔지니어 약 {kl['inst_h'][1]:.0f}인시 → {kl['inst_h'][4]:.0f}인시)\n"
                    '- 1세대 5년 기여이익 최대 변수 = 고객 지불의사 · Robot BOM\n'
                    '- 방어력 = 특허 단독이 아닌 Grasp Data · Calibration 절차 · Interface 표준 · Installed Base 축적 (구축 예정)'))
    y = mhead(s, '14  Technology-to-Economics / Moat', 'R&D 성과의 설치비 · 서비스비 · 확장매출 연결 구조',
              '성능 향상 자체가 아닌 Unit Economics · Scale 개선으로 연결')
    lw = 6.2
    lev = [('Adaptive Hand 고도화', 'Object Coverage ↑'), ('Manipulation Skill 고도화', 'Task Coverage ↑'),
           ('Calibration 고도화', '신규 주방 적용시간 ↓'), ('Environment Interface 최적화', 'Task Reliability ↑')]
    a_w = 2.35; b_w = 1.75; rh = 0.5
    for i, (a, b) in enumerate(lev):
        yy = y + i * (rh + 0.1)
        rect(s, MX, yy, a_w, rh, fill=SOFT)
        text(s, MX + 0.12, yy, a_w - 0.24, rh, a, size=10, bold=True, anchor='m')
        arrow(s, MX + a_w + 0.03, yy + rh / 2, MX + a_w + 0.27, yy + rh / 2, color=GREY, lw=1.25)
        rect(s, MX + a_w + 0.3, yy, b_w, rh, fill='FFFFFF', line=EDGE)
        text(s, MX + a_w + 0.3, yy, b_w, rh, b, size=10, bold=True, align='c', anchor='m')
    ex = MX + a_w + 0.3 + b_w; mid = y + 2 * (rh + 0.1) - 0.05
    for i in range(4):
        yy = y + i * (rh + 0.1) + rh / 2
        seg(s, ex + 0.02, yy, ex + 0.2, yy, color=GREY, lw=1.0)
    seg(s, ex + 0.2, y + rh / 2, ex + 0.2, y + 3 * (rh + 0.1) + rh / 2, color=GREY, lw=1.0)
    arrow(s, ex + 0.2, mid, ex + 0.38, mid, color=GREY, lw=1.25)
    ox = ex + 0.42; ow = MX + lw - ox
    rect(s, ox, y, ow, 4 * rh + 0.3, fill=INK)
    text(s, ox + 0.12, y + 0.1, ow - 0.24, 4 * rh + 0.1, ['설치시간 ↓', 'Engineering 비용 ↓', '고객경험 ↑', '반복설치 ↑', '→ Installed Base ↑'],
         size=10, bold=True, color='FFFFFF', line=1.05, anchor='m', space_after=2)
    ry = y + 4 * rh + 0.45
    rect(s, MX, ry, lw, 0.46, fill=SOFT)
    text(s, MX + 0.15, ry, lw - 0.3, 0.46, [[('Installed Base → ', {'bold': True}), ('Care · Consumables · Skill Upgrade 매출 ↑', {'bold': True, 'color': INK})]],
         size=11, anchor='m')
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y - 0.02, rw, 0.26, 'KPI ↔ 원가 연결 (Base · ASSUMPTION, 인시 DERIVED)', size=10.5, bold=True, color=GREY)
    rows = [['설치 · Calibration 원가 (Remodeling)', f"{A('comm_cost')[1]}만 · {kl['inst_h'][1]:.0f}인시", f"{A('comm_cost')[2]}만 · {kl['inst_h'][2]:.0f}인시", f"{A('comm_cost')[4]}만 · {kl['inst_h'][4]:.0f}인시"],
            ['Robot System BOM', f"{kl['bom'][1]:,}만", f"{kl['bom'][2]:,}만", f"{kl['bom'][4]:,}만"],
            ['Care 원가 / 대 · 년', f"{kl['care_unit'][1]:.1f}만", f"{kl['care_unit'][2]:.1f}만", f"{kl['care_unit'][4]:.1f}만"],
            ['1세대 5년 기여이익', '-', (f"{h3['contrib5']:,.0f}만", {'bold': True}), (f"{h5['contrib5']:,.0f}만", {'bold': True, 'color': ACC})]]
    th = table(s, rx, y + 0.28, rw, ['연결 지표', 'Y2 실증', 'Y3', 'Y5'], rows, col_w=[rw - 3.15, 1.05, 1.05, 1.05], size=9.5,
               align=['l', 'r', 'r', 'r'], label='m14t', pad=0.06)
    text(s, rx, y + 0.28 + th + 0.04, rw, 0.24, f"Pad 수명 요구치 ≥ {kl['pad_life']:,.0f}회 파지 (분기 교체 가정 충족 조건)", size=8.5, color=INK2, check=False)
    sy = y + 0.28 + th + 0.38
    text(s, rx, sy, rw, 0.26, '1세대 5년 기여이익 민감도 (만원)', size=10.5, bold=True, color=GREY)
    top = sh['items'][:5]
    mx_ = max(max(abs(d['lo']), abs(d['hi'])) for d in top)
    cx0 = rx + 2.35; half = (rw - 2.35 - 0.1) / 2; cxm = cx0 + half
    for i, d in enumerate(top):
        yy = sy + 0.32 + i * 0.27
        text(s, rx, yy, 2.3, 0.22, d['name'], size=8.5, align='r', anchor='m', check=False)
        lo, hi = d['lo'], d['hi']
        wl = (half - 0.5) * abs(lo) / mx_; wh = (half - 0.5) * abs(hi) / mx_
        rect(s, cxm - wl, yy + 0.03, wl, 0.16, fill='A9AEB5')
        rect(s, cxm, yy + 0.03, wh, 0.16, fill=INK)
        text(s, cxm - wl - 0.5, yy, 0.46, 0.22, f'{lo:+,.0f}', size=7.5, color=INK2, align='r', anchor='m', check=False)
        text(s, cxm + wh + 0.04, yy, 0.5, 0.22, f'{hi:+,.0f}', size=7.5, color=INK2, anchor='m', check=False)
    vline(s, cxm, sy + 0.3, 5 * 0.27, color=INK)
    my = H - 0.62 - 0.3 - 0.62
    rect(s, MX, my, CW, 0.62, fill='FFFFFF', line=INK, lw=1.0)
    text(s, MX + 0.2, my, CW - 0.4, 0.62, [[('Moat = 단일 특허가 아닌 축적  ', {'bold': True}),
                                            ('① 주방 물체 Grasp Data · Skill Library  ② Calibration 절차 · Interface 표준 (설치시간)  ③ Installed Base · Care Data  ④ 출원 예정 IP', {'color': INK2}),
                                            ('   (TARGET)', {'color': GREY, 'bold': True})]], size=10, anchor='m')
    note(s, f"인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 약 {kl['hour']:.1f}만원 (연 6,600만원 기준) · 민감도 = Remodeling 구매 1세대 · Y3 원가 · 기준 {sh['base']:,.0f}만원 (부록 D5)",
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 15 IP / competition
def m15(prs):
    s = start(prs, 'm15', pg(prs), '경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증',
              visual='좌측 경쟁 비교표 (5개 Category + MH 목표 Position × 5개 비교 축, 공개 자료 기준). 우측 IP 후보 5개 영역 (출원 후보 · 선행기술 Risk · 우선순위). 하단 Humanoid 대응 띠.',
              chart='비교표 2개 + 결론 띠',
              note=('- 경쟁 존재: 가전사 (기기 내부 자동화 · 구독) · 조리 로봇 (전용 주방 · 조리대 기기) · Humanoid · 이동형 (범용 손 · 모델 학습) · Cobot + Gripper (부품) · 주방가구사 (시공)\n'
                    '- MH 목표 Position: 주방 물체용 Hand · CLEAN → COOK Skill 확장 · Calibration + 최소 Interface · 주방 공사 연계 설치 · Care · 소모품\n'
                    '- 우위 = 재배치 시간 · 경제성 실증으로 입증 필요\n'
                    '- 가전사 · 가구사 직접 진입 가능 (LG CLOiD 2028 목표) → Interface · 시공 Partner 후보로 설계\n'
                    '- IP 1순위: 교체형 식품접촉 Module · 가전 기준점 Calibration · 선행특허 존재 → 좁고 구체적인 청구 (등록 미정)\n'
                    '- Humanoid = 위협만이 아님: 공개 범용 모델 → MH 실행층 활용 · MH Interface · Skill → 다른 Robot에도 적용'))
    y = mhead(s, '15  IP / Competition', '경쟁 구도: 차별화 = 주방 적용 방식, 실증으로 입증',
              '가전사 · 가구사 직접 진입 가능 (LG CLOiD 2028 목표) → Interface · 시공 Partner 후보로 설계')
    lw = 7.55
    hdr = ['구분', '물체 Handling', 'Task 범위', '주방 적응 · 설치', '반복매출 · 확장']
    rows = [[('Kitchen Appliance\n삼성 · LG', {'bold': True}), '기기 내부만', '세척 · 가열 · 보관', '가전 설치', '구독 · Care\n(LG 2조원+)'],
            [('Cooking Robot\nMoley · Posha', {'bold': True}), '조리 도구 · 재료', '조리 중심', '전용 주방 (£248k) · 조리대 기기 ($1,750)', '레시피 · 월 구독'],
            [('Humanoid · Mobile\n1X NEO · Figure · Sunday · LG CLOiD', {'bold': True}), '범용 손', '가사 전반 시연', '설치 불필요 · 모델 학습 중심', '구독 ($499/월) · 출시 전'],
            [('Cobot + Gripper\nUR · Doosan + Robotiq', {'bold': True}), '상용 Gripper', '산업 작업', 'Integrator 맞춤 구축', '부품 판매'],
            [('Kitchen Furniture\n한샘 · 리바트', {'bold': True}), '-', '수납 · 빌트인 가전', '주방 시공 (로봇 협업 보도 없음)', '시공 매출'],
            [('MH 목표 Position', {'bold': True}), ('Kitchen Hand\n(식기 · 도구)', {'bold': True}), ('CLEAN → ASSIST\n→ COOK', {'bold': True}),
             ('Calibration + 최소 Interface · 공사 연계', {'bold': True}), ('Care · 소모품 · Skill', {'bold': True})]]
    table(s, MX, y, lw, hdr, rows, col_w=[1.95, 1.3, 1.3, 1.6, 1.4], size=8.8, label='m15c', pad=0.055)
    rx = MX + lw + 0.3; rw = W - MX - rx
    hdr2 = ['영역', '출원 후보', '선행 Risk', '순위']
    rows2 = [[('Robot Hand', {'bold': True}), 'Food-contact Module (1) · Adaptive Finger (2) · Compliance (3)', '중~상', ('1', {'bold': True})],
             [('Calibration', {'bold': True}), 'Task Coordinate Calibration (1) · Kitchen Mapping (2)', '중', ('1', {'bold': True})],
             [('Interface', {'bold': True}), 'Robot Home (2) · Appliance Interface (2) · Tool Dock (3)', '상', '2'],
             [('Manipulation', {'bold': True}), '식기 Handling (2) · Failure Recovery (3)', '상', '2'],
             [('Safety', {'bold': True}), 'Zone Control (3)', '중~상', '3']]
    th2 = table(s, rx, y, rw, hdr2, rows2, col_w=[1.05, rw - 1.05 - 0.75 - 0.5, 0.75, 0.5], size=8.8, align=['l', 'l', 'c', 'c'], label='m15ip', pad=0.055)
    text(s, rx, y + th2 + 0.06, rw, 0.62, '선행: Dishcare US 11,731,282 · Dishcraft US 10,507,584 · 주방 Rail Arm US 7,751,938 · 수납장 로봇 US 12,275,130 · Schmalz OFG · 24개월 출원 5건 + PCT 1건 (TARGET, 등록 미정)',
         size=8.5, color=INK2, line=1.02)
    by = H - 0.62 - 0.3 - 0.66
    rect(s, MX, by, CW, 0.66, fill=INK)
    text(s, MX + 0.2, by, CW - 0.4, 0.66, [[('Humanoid = 위협만이 아님  ', {'bold': True, 'color': 'FFFFFF'}),
                                            ('공개 범용 모델 (openpi π0 · π0.5) → MH Manipulation Layer 활용 가능 · MH Interface · Skill · Calibration → 다른 Robot Platform에도 적용 · '
                                             '가격 ($20,000) · 낮은 작업점 Reach 등 가정 설치 제약 → 공간 Integration으로 보완', {'color': 'D5D8DC'})]], size=9.5, anchor='m', line=1.02)
    note(s, '출처 [S19~S25 · S41 · S45 · S46 · S49~S51] · 비교 축 = 접근 방식 (공개 자료) · 특허 = 출원 후보 (등록 미정)', y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 16 TIPS R&D / roadmap
def m16(prs):
    s = start(prs, 'm16', pg(prs), 'TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발',
              visual='상단 좌우 비교: TIPS 과제 (WP1~WP6, 기술 검증) vs 민간 Seed (사업 검증 · 과제 외 개발). 중간 24개월 4구간 일정 (0~6 · 7~12 · 13~18 · 19~24M). 하단 Gate 4개 (M6 · M12 · M18 · M24) 판단 기준.',
              chart='2열 비교 + 4구간 로드맵 + Gate',
              note=(f"- TIPS 과제 {M['tips']['total'] / 10000:.2f}억원 = 기술 위험 해소 (WP1 Hand · WP2 Skill · WP3 Perception · Calibration · WP4 최소 Interface · WP5 안전 · WP6 통합 CLEAN 실증)\n"
                    '- Seed = 기관부담금 · 과제 외 인건비 · 고객 검증 · 실증 운영 · WTP · Partner 개발 · BM 검증\n'
                    '- 일정 6개월 단위 · Gate별 판단 (계속 · 범위 축소 · 전환)\n'
                    '- M6 상용 Gripper 대비 Hand 비교 · M12 목업 CLEAN 전 과정 · M18 주방 3종 Transfer · WTP · M24 가정 실증 · 유료 전환 · 원가 실측'))
    y = mhead(s, '16  TIPS R&D / 24개월 Roadmap', 'TIPS = 기술 검증 (WP1~6) · Seed = 사업 검증 · 과제 외 개발',
              f"TIPS 과제 {M['tips']['total'] / 10000:.2f}억원 = WP1~6 기술 검증 · Seed = 기관부담금 · 과제 외 인건비 · 고객 · 실증 · 사업 검증")
    lw = (CW - 0.3) / 2; bh = 1.32
    rect(s, MX, y, lw, bh, fill=INK)
    text(s, MX + 0.2, y + 0.1, lw - 0.4, 0.3, 'TIPS 과제  ·  기술 검증 (Technology De-risking)', size=12, bold=True, color='FFFFFF')
    wps = ['WP1 Adaptive Kitchen Robot Hand', 'WP2 Kitchen Manipulation Skill', 'WP3 Perception / Calibration',
           'WP4 Minimal Environment Interface', 'WP5 Human-Robot Safety', 'WP6 Integrated CLEAN 실증']
    for i, w_ in enumerate(wps):
        text(s, MX + 0.2 + (i % 2) * (lw / 2 - 0.1), y + 0.48 + (i // 2) * 0.27, lw / 2 - 0.2, 0.26, w_, size=9.5, color='E3E5E8', check=False)
    rx = MX + lw + 0.3
    rect(s, rx, y, lw, bh, fill=SOFT)
    text(s, rx + 0.2, y + 0.1, lw - 0.4, 0.3, '민간 Seed  ·  사업 검증 (Commercial Validation)', size=12, bold=True)
    seeds = ['과제 외 인건비 (사업 · 현장 · 지원)', '목업 · 시제품 운영', '고객 검증 · WTP', 'Pilot 운영 · 유료 전환',
             'Partner 개발', 'BM 검증 · 기관부담금']
    for i, w_ in enumerate(seeds):
        text(s, rx + 0.2 + (i % 2) * (lw / 2 - 0.1), y + 0.48 + (i // 2) * 0.27, lw / 2 - 0.2, 0.26, w_, size=9.5, color=INK2, check=False)
    gy = y + bh + 0.22
    per = [('0~6M', ['주방 작업 분석', 'Robot 구조 설계', 'Hand 시제품 v1', '식기 30종 파지 시험', '초기 Calibration']),
           ('7~12M', ['CLEAN Skill', '식세기 연동', 'Hand v2 · 안전 기능', '1:1 주방 목업', '목업 CLEAN 전 과정']),
           ('13~18M', ['주방 3종 적용', '주방 간 Transfer 시험', '실패 복구', 'Pilot 착수', 'WTP 검증']),
           ('19~24M', ['신뢰성 (연속 운전)', '설치 표준', '가정 실증 3세대', 'BOM · 설치 · 서비스 원가', '유료 실증 · Partner 조건'])]
    pw = (CW - 3 * 0.14) / 4; ph = 1.62
    for i, (t, items) in enumerate(per):
        px = MX + i * (pw + 0.14)
        rect(s, px, gy, pw, 0.32, fill=INK if i == 3 else '3A3F46')
        text(s, px, gy, pw, 0.32, t, size=11, bold=True, color='FFFFFF', align='c', anchor='m')
        rect(s, px, gy + 0.32, pw, ph - 0.32, fill=SOFT)
        text(s, px + 0.14, gy + 0.4, pw - 0.28, ph - 0.46, items, size=9.5, color=INK, bullet='–', line=1.0, space_after=1)
    ky = gy + ph + 0.16
    gates = [('M6', '상용 Gripper 대비 Hand 비교 (30종) → Build / Buy 결정'),
             ('M12', '목업 CLEAN 전 과정 · 식기 성공률 ≥ 80%'),
             ('M18', '주방 3종 Transfer (하락 ≤ 10%p) · WTP n≥300'),
             ('M24', '가정 3세대 성공률 ≥ 90% · 유료 전환 ≥ 2세대 · 원가 실측')]
    for i, (g, d) in enumerate(gates):
        px = MX + i * (pw + 0.14)
        rect(s, px, ky, pw, 0.78, fill='FFFFFF', line=INK if i == 3 else EDGE, lw=1.25 if i == 3 else 0.75)
        text(s, px + 0.12, ky + 0.06, 0.6, 0.26, g, size=11, bold=True, color=INK)
        text(s, px + 0.12, ky + 0.32, pw - 0.24, 0.44, d, size=8.8, color=INK, line=1.0)
    mts(s, MX + CW - 0.75, ky - 0.24, ['TARGET'])
    note(s, 'TIPS 2026 일반트랙: 정부 R&D 최대 8억원 · 24개월 · 정부 75% 이내 · 기관부담 25% 이상 [S33 · S52] · KPI: 부록 A1~A3', y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 17 founder / team
def m17(prs):
    Fd = F()
    s = start(prs, 'm17', pg(prs), 'Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획',
              visual='좌측 Founder 확인 항목 7행 × Founder 2인 (입력 전 [Founder 정보 필요]). 우측 24개월 채용 계획 표 (역할 · 시작 월 · 구분) + 인원 요약.',
              chart='확인 항목 표 + 채용 계획 표',
              note=('- 필요 핵심 역량 3개: 로봇 조작 (Hand · Skill) · 주방 · 건축 설치 (Interface · 시공 Partner) · 고객 · Partner 영업\n'
                    '- Founder 확인 항목 7개: Why This Problem · 관련 엔지니어링 경험 · 하드웨어 · 제품 개발 · Robot · 기계 · AI 역량 · 건설 · 주방 · 제조 지식 · 고객 · Partner 네트워크 · 전업 여부 · 지분\n'
                    f"- 24개월 채용 계획: Founder 2명 포함 24개월 차 약 {Fd['heads_m24']:.0f}명 · R&D 중심 · 리드 3명 (Manipulation · Perception · Hand) 우선 채용\n"
                    '- TIPS 요건: 대표 포함 창업팀 2인 이상 지분 60% 이상 · 정부지원 5억원당 청년 1명 신규 채용'))
    y = mhead(s, '17  Founder / Team', 'Founder / Team: 필요 핵심 역량 3개 · 24개월 채용 계획',
              '필요 역량 = 로봇 조작 (Hand · Skill) · 주방 · 건축 설치 · 고객 · Partner 영업')
    lw = 6.3
    items = ['Why This Problem', 'Relevant Engineering Experience', 'Hardware / Product Development', 'Robot · Mechanical · AI Capability',
             'Construction · Kitchen · Manufacturing Knowledge', 'Customer / Partner Network', 'Full-time Commitment · 지분']
    NEED = ('[Founder 정보 필요]', {'color': INK2, 'bold': True})
    rows = [[it, NEED, NEED] for it in items]
    table(s, MX, y, lw, ['확인 항목', 'Founder 1 (대표)', 'Founder 2 (확보 여부 확인)'], rows, col_w=[2.9, 1.7, 1.7], size=9.5, label='m17f', pad=0.075)
    rx = MX + lw + 0.35; rw = W - MX - rx
    tm = Fd['team']
    trows = []
    for m in tm:
        role = m['role'].replace(' [Founder 정보 필요]', '')
        trows.append([role, f"M{m['start']}", M['team_kind'][m['kind']]])
    table(s, rx, y, rw, ['역할 (채용 계획, ASSUMPTION)', '시작', '구분'], trows, col_w=[rw - 1.45, 0.6, 0.85], size=8.5, label='m17t', pad=0.035,
          align=['l', 'c', 'l'])
    kinds = {}
    for m in tm:
        if m['pm'][1] > 0: kinds[m['kind']] = kinds.get(m['kind'], 0) + m['frac']
    summ = f"M24 약 {Fd['heads_m24']:.0f}명 = Founder {kinds.get('founder', 0):.0f} · R&D {kinds.get('rnd', 0):.0f} · 사업 {kinds.get('biz', 0):.0f} · 현장 {kinds.get('field', 0):.0f} · 경영지원 {kinds.get('ops', 0):.1f}  |  평균 FTE {Fd['fte'][0]:.1f} (Y1) → {Fd['fte'][1]:.1f} (Y2)"
    yb = H - 0.62 - 0.3 - 0.52
    rect(s, MX, yb, CW, 0.52, fill=SOFT)
    text(s, MX + 0.2, yb, CW - 0.4, 0.52, summ, size=10.5, bold=True, anchor='m')
    note(s, 'TIPS 요건: 대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 30% 이하 · 정부지원 5억원당 청년 1명 신규 채용 [S33]',
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 18 investment ask / value creation
def m18(prs):
    Fd = F(); TP = Fd['tips']
    s = start(prs, 'm18', pg(prs), f"24개월 사용 {Fd['spend_total'] / 10000:.1f}억원 · Seed {Fd['seed_range'][0]}~{Fd['seed_range'][1]}억원 요청 (TIPS 8억원 별도)",
              visual='좌측 24개월 사용처 표 (억원) + 재원 · Seed 산식. 우측 Value Creation 흐름: TODAY → Seed + TIPS → 24M TARGET (기술 · 경제성 · 시장 Evidence) → NEXT ROUND (회사 정의로 마무리).',
              chart='사용처 표 + 4단계 흐름도',
              note=(f"- 투자 요청액 = 24개월 사용처 Bottom-up 산정 · 24개월 지출 약 {Fd['spend_total'] / 10000:.1f}억원 (인건비 중심)\n"
                    f"- Seed Base = 지출 − TIPS 정부지원 8억원 + Buffer 3개월 {Fd['buffer'] / 10000:.2f}억원 = 약 {Fd['seed_base'] / 10000:.1f}억원\n"
                    f"- Seed Lean (팀 · 목업 · 실증 축소) 약 {Fd['seed_lean'] / 10000:.1f}억원 · TIPS 미선정 시 Lean 범위 약 {Fd['seed_no_tips'] / 10000:.1f}억원\n"
                    '- 24개월 Evidence: 실제 주방 작동 시제품 · 주방 간 Transfer · BOM · 설치 · 서비스 원가 실측 · WTP · 유료 실증 · Partner 조건 · 특허 출원\n'
                    f"- Series A 이후 Y3~Y4 현금 소요 약 {M['post_seed_burn']['y3_y4'] / 10000:.0f}억원 → 후속 투자 기준 = 기술 성공 + 유료 전환 + 원가 Evidence\n"
                    '- 회사 정의: Hand · Skill · Calibration · Environment Integration 결합 → CLEAN 검증 → 같은 Platform에서 ASSIST · COOK 확장 → 기존 주방 · Remodeling · 신축 설치 → Installed Base 반복매출'))
    y = mhead(s, '18  Investment Ask / 24M Value Creation',
              f"24개월 사용 {Fd['spend_total'] / 10000:.1f}억원 · Seed {Fd['seed_range'][0]}~{Fd['seed_range'][1]}억원 요청 (TIPS 8억원 별도)",
              'Bottom-up 사용처 산정 · Seed 범위 = Lean (팀 · 범위 축소) ~ Base (기술 + 사업 검증 + 3개월 Buffer)')
    lw = 4.9
    groups = [('인건비 · 연구수당', ['인건비', '연구수당']), ('Robot HW · Hand · Mock-up', ['Robot Hardware', 'Hand Prototype', 'Kitchen Mock-up']),
              ('Software · Data', ['Software · Data']), ('Pilot · 실증 순비용', ['Pilot', '실증 순비용']), ('Customer · Partner', ['Customer · Partner']),
              ('Certification · IP', ['Certification', 'IP']), ('Space · Operating', ['Space', 'Operating']), ('예비비 (10%)', ['예비비'])]
    U = {u['cat']: u for u in Fd['uses']}
    rows = []
    for g, cats in groups:
        v = sum(sum(U[c]['y']) for c in cats); tv = sum(sum(U[c]['tips']) for c in cats)
        rows.append([g, f'{v / 10000:.2f}', f'{tv / 10000:.2f}' if tv else '-'])
    rows.append([('24개월 지출 합계', {'bold': True}), (f"{Fd['spend_total'] / 10000:.2f}", {'bold': True}), (f"{TP['total'] / 10000:.2f}", {'bold': True})])
    th = table(s, MX, y, lw, ['사용처 (억원)', '24개월', 'TIPS 편성'], rows, col_w=[lw - 1.9, 0.95, 0.95], size=9.5,
               align=['l', 'r', 'r'], label='m18u', pad=0.05)
    sy = y + th + 0.14
    tg = lambda t: (t, {'size': 7.5, 'color': GREY})       # small tag cell (low visual priority)
    srows = [['TIPS 정부지원 (선정 시 · 상한)', f"{TP['gov'] / 10000:.2f}", tg('ASSUMPTION')],
             ['기관부담 (현금 · 현물)', f"{TP['private'] / 10000:.2f}", tg('Seed 부담')],
             [(f"Seed Base = 지출 − TIPS + Buffer {Fd['buffer'] / 10000:.2f}", {'bold': True}), (f"{Fd['seed_base'] / 10000:.2f}", {'bold': True, 'color': ACC}), tg('DERIVED')],
             [f"Seed Lean (지출 {Fd['lean_total'] / 10000:.2f}억원 규모)", f"{Fd['seed_lean'] / 10000:.2f}", tg('DERIVED')],
             ['TIPS 미선정 시 (Lean 범위)', f"{Fd['seed_no_tips'] / 10000:.2f}", tg('DERIVED')]]
    sh = table(s, MX, sy, lw, None, srows, col_w=[lw - 1.9, 0.95, 0.95], size=9.5, align=['l', 'r', 'l'], label='m18s', pad=0.05)
    assert sy + sh < H - 0.6 - 0.4 - 0.08, ('m18 source table runs into the footnote', sy + sh)
    rx = MX + lw + 0.35; rw = W - MX - rx
    bh = H - 0.6 - 0.4 - 0.1 - 0.48 - 0.14 - y
    w1 = 1.05; w4 = 1.2; gap = 0.28; w3 = rw - w1 - w4 - 2 * gap
    rect(s, rx, y, w1, bh, fill=SOFT)
    text(s, rx + 0.12, y + 0.12, w1 - 0.24, 0.3, 'TODAY', size=12, bold=True)
    text(s, rx + 0.12, y + 0.5, w1 - 0.24, bh - 0.6, ['Concept', '기술 가설', '사업 가설'], size=9, color=INK2, line=1.02, space_after=3)
    arrow(s, rx + w1 + 0.03, y + bh / 2, rx + w1 + gap - 0.03, y + bh / 2, color=GREY, lw=1.5)
    text(s, rx + w1 - 0.12, y + bh / 2 - 0.62, gap + 0.24, 0.55, 'Seed\n+\nTIPS', size=7.5, bold=True, color=GREY, align='c', check=False)
    x3 = rx + w1 + gap
    rect(s, x3, y, w3, bh, fill=INK)
    text(s, x3 + 0.18, y + 0.12, w3 - 0.36, 0.3, '24M TARGET', size=12, bold=True, color='FFFFFF')
    mt(s, x3 + w3 - 0.75, y + 0.14, 'TARGET', fill=INK)
    gx = x3 + 0.18; gw = (w3 - 0.36 - 0.16) / 2; gx2 = gx + gw + 0.16; yy = y + 0.5
    text(s, gx, yy, gw, 0.22, '기술', size=8.5, bold=True, color='A9AEB5', check=False)
    text(s, gx, yy + 0.24, gw, bh - 0.84, ['실제 주방 작동 시제품', 'Adaptive Robot Hand', 'Skill Library', 'Calibration System',
                                           '안전 구조', '주방 3종 시험', 'Transfer 증거'],
         size=9, color='FFFFFF', line=1.0, space_after=2)
    text(s, gx2, yy, gw, 0.22, '경제성', size=8.5, bold=True, color='A9AEB5', check=False)
    text(s, gx2, yy + 0.24, gw, 0.8, ['Robot BOM', '설치 원가', '서비스 원가'], size=9, color='FFFFFF', line=1.0, space_after=2)
    text(s, gx2, yy + 1.12, gw, 0.22, '시장', size=8.5, bold=True, color='A9AEB5', check=False)
    text(s, gx2, yy + 1.36, gw, bh - 1.96, ['Customer WTP', '실증 · 유료 실증', 'Partner 조건', '특허 출원'], size=9, color='FFFFFF',
         line=1.0, space_after=2)
    arrow(s, x3 + w3 + 0.03, y + bh / 2, x3 + w3 + gap - 0.03, y + bh / 2, color=GREY, lw=1.5)
    x4 = x3 + w3 + gap
    rect(s, x4, y, w4, bh, fill='FFFFFF', line=INK, lw=1.0)
    text(s, x4 + 0.1, y + 0.12, w4 - 0.2, 0.3, 'NEXT ROUND', size=10.5, bold=True)
    text(s, x4 + 0.12, y + 0.5, w4 - 0.24, bh - 0.6, ['제품화 · 양산', '같은 Platform → ASSIST Skill', 'Retrofit · 신축 채널 확대', 'Installed Base 반복매출'], size=9, color=INK2, line=1.02, space_after=3)
    by = y + bh + 0.14
    rect(s, rx, by, rw, 0.48, fill=SOFT)
    text(s, rx + 0.15, by, rw - 0.3, 0.48, [[('Series A 판단 기준  ', {'bold': True}), ('기술 성공 + 유료 전환 + 설치 · 서비스 원가 실측', {'color': INK, 'bold': True})]],
         size=11, anchor='m')
    note(s, f"Series A 이후 Y3~Y4 현금 소요 약 {M['post_seed_burn']['y3_y4'] / 10000:.0f}억원 · 손익분기 연 약 {M['breakeven_kitchens']:,.0f}세대 (DERIVED, 부록 D4) · Buffer = Y2 월평균 지출 × 3개월 · "
            f"TIPS 과제 {TP['total'] / 10000:.2f}억원 = 정부 8 + 기관부담 {TP['private'] / 10000:.2f} (현금 {TP['private_cash'] / 10000:.2f} · 현물 {TP['inkind'] / 10000:.2f}) · 운영사 선투자 (수도권 2억원 이상) = Seed 포함", y=H - 0.6 - 0.4)
    mfoot(s)


MAIN = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, m12, m13, m14, m15, m16, m17, m18]
