# SoftHand Seed IR deck v2 - main slides (light design, 개조식 copy).
import json, os
from kit import *
import kit

from paths import RAW as _RAW, RENDERS as _RENDERS, ORIGINAL as _ORIGINAL, MODEL_JSON as _MODEL
PATHS = dict(raw=_RAW, renders=_RENDERS, original=_ORIGINAL, model=_MODEL)
def RAW(n): return os.path.join(PATHS['raw'], n)
def REN(n): return os.path.join(PATHS['renders'], n)
def ORI(n): return os.path.join(PATHS['original'], n)

M = {}
def load_model():
    M.update(json.load(open(PATHS['model'], encoding='utf-8')))

def eok(v, d=1):
    return f'{v:.{d}f}억'


# ---------------------------------------------------------------- helpers
def num_item(s, x, y, w, n, title, desc, tsize=15, dsize=12, nw=0.42, gap=0.04):
    text(s, x, y - 0.03, nw, 0.46, str(n), size=tsize + 5, bold=True, color=T['accent'])
    text(s, x + nw, y, w - nw, 0.32, title, size=tsize, bold=True, label='item ' + title)
    dh = text_h(desc, dsize, w - nw)
    text(s, x + nw, y + tsize * LH / 72 + gap, w - nw, dh + 0.02, desc, size=dsize, color=T['text2'], label='item desc ' + title)
    return tsize * LH / 72 + gap + dh

def flow_row(s, x, y, w, label, steps, label_color=None, strong=(), size=14, lw=1.45):
    text(s, x, y, lw, 0.3, label, size=size, bold=True, color=label_color or T['text'])
    runs = []
    for i, st in enumerate(steps):
        if i: runs.append(('   ›   ', {'color': T['muted']}))
        runs.append((st, {'bold': st in strong, 'color': T['text'] if st in strong else T['text2']}))
    text(s, x + lw, y, w - lw, 0.3, [runs], size=size, label='flow ' + label)


# ---------------------------------------------------------------- 01 cover
def s01(prs):
    s = new_slide(prs, '01 cover')
    ix = 6.25
    image(s, RAW('cover_color.png'), ix, 0, W - ix, H, focus=(0.56, 0.42), zoom=1.22)
    text(s, MX, 0.7, 5, 0.3, '[회사명 입력 필요]', size=12, color=T['muted'])
    text(s, MX, 1.62, 5, 0.32, 'Seed 투자 제안서', size=15, bold=True, color=T['accent'])
    text(s, MX, 2.08, 5.3, 2.32, '사람용 설비를\n그대로 쓰는\n로봇 핸드', size=40, bold=True, line=0.95, label='cover title')
    text(s, MX, 4.55, 5.3, 0.7, 'SoftHand-4 + 머신텐딩 스킬 팩\n기존 설비를 크게 바꾸지 않는 공장 자동화', size=16, color=T['text2'], label='cover sub')
    xs = [MX, MX + 1.85, MX + 3.45]
    for i, (k, v) in enumerate([('투자 요청', '20억 원'), ('기간', '24개월'), ('첫 시장', '머신텐딩')]):
        if i: vline(s, xs[i] - 0.22, 5.62, 0.72)
        text(s, xs[i], 5.6, 1.6, 0.26, k, size=11, color=T['muted'])
        text(s, xs[i], 5.9, 1.7, 0.45, v, size=20, bold=True)
    text(s, MX, H - 0.62, 3, 0.25, 'ONE HAND. MANY TOOLS.', size=11, bold=True, color=T['text2'], check=False)
    text(s, MX + 3.1, H - 0.62, 2.2, 0.25, '2026. 10', size=11, color=T['muted'], check=False)
    text(s, MX + 3.1, H - 0.36, 2.4, 0.2, '이미지: 콘셉트 렌더링', size=9, color=T['muted'], check=False)
    notes(s, '표지. 사람이 쓰도록 만든 공장 설비를 로봇이 그대로 쓰게 하는 로봇 핸드 회사. 첫 제품 SoftHand-4 + 머신텐딩 스킬 팩, Seed 20억 원 / 24개월.')


# ---------------------------------------------------------------- 02 summary
def s02(prs):
    s = new_slide(prs, '02 summary')
    y0 = header(s, '투자 요약', '설비를 크게 바꾸지 않는 로봇 자동화,\n첫 시장은 머신텐딩')
    rows = [
        ('문제', '로봇 도입 시 전용 그리퍼·지그·설비 개조 동반, 품목이 바뀌면 같은 작업 반복'),
        ('해결', '문 열기·소재 집기·버튼 조작까지 하는 로봇 핸드 SoftHand-4, 기존 설비는 그대로 사용'),
        ('첫 시장', '공작기계 소재 투입·배출(머신텐딩), 품목이 자주 바뀌는 중소·중견 가공 공장'),
        ('수익 구조', '핸드 판매·유료 PoC로 초기 매출, 현장 작업을 표준 스킬로 만들어 다음 고객에 재판매'),
        ('확장', 'SI 파트너 판매 후 로봇 제조사(OEM) 기본 옵션 탑재 목표'),
    ]
    y = y0 + 0.25; lw = 7.9; rh = 0.78
    hline(s, MX, y, lw, color=T['text'], lw=1.0)
    for k, v in rows:
        text(s, MX, y + 0.17, 1.45, 0.3, k, size=14, bold=True, label='row ' + k)
        text(s, MX + 1.55, y + 0.15, lw - 1.55, rh - 0.2, v, size=14, color=T['text2'], label='row text ' + k)
        y += rh
        hline(s, MX, y, lw)
    bx = 9.2; bw = W - MX - bx; by = y0 + 0.25; bh = y - by
    rect(s, bx, by, bw, bh, fill=T['dark'])
    text(s, bx + 0.35, by + 0.32, bw - 0.7, 0.3, '투자 요청', size=13, color=T['on_dark2'])
    text(s, bx + 0.35, by + 0.6, bw - 0.7, 0.92, '20억 원', size=44, bold=True, color=T['accent'], label='ask')
    text(s, bx + 0.35, by + 1.5, bw - 0.7, 0.3, 'Seed  ·  24개월', size=14, color=T['on_dark'])
    hline(s, bx + 0.35, by + 1.98, bw - 0.7, color='3A3E44')
    text(s, bx + 0.35, by + 2.12, bw - 0.7, 0.3, '24개월 목표', size=12, color=T['on_dark2'])
    text(s, bx + 0.35, by + 2.46, bw - 0.7, 1.5,
         ['유료 PoC 5건', '재구매 고객 2곳', '로봇 2종에서 같은 스킬 검증', 'Series A 준비'],
         size=15, color=T['on_dark'], space_after=5, label='ask list')
    footer(s, 2)
    notes(s, '투자자가 한 장으로 설명할 수 있어야 하는 내용. 문제-해결-첫 시장-수익 구조-확장, 그리고 요청 금액과 24개월 목표.')


# ---------------------------------------------------------------- 03 problem
def s03(prs):
    s = new_slide(prs, '03 problem')
    y0 = header(s, '문제', '로봇 도입마다 반복되는 설비 재설계', '품목이 바뀌면 같은 과정을 처음부터 반복')
    steps = [('전용 그리퍼', '부품 모양별\n신규 제작'), ('지그·고정구', '위치 맞춤용\n치공구 제작'),
             ('설비 개조', '자동문·센서·\n구동기 추가'), ('프로그래밍', '로봇 동작\n재입력(티칭)'), ('시운전·검증', '라인 정지 후\n반복 시험')]
    lx, lw = MX, 7.75; ty = y0 + 0.55
    hline(s, lx, ty, lw, color=T['text'], lw=1.25)
    cw = lw / 5
    for i, (a, b) in enumerate(steps):
        x = lx + i * cw
        dot(s, x + 0.05, ty)
        text(s, x, ty - 0.42, cw - 0.1, 0.26, f'{i + 1:02d}', size=11, bold=True, color=T['muted'])
        text(s, x, ty + 0.2, cw - 0.12, 0.32, a, size=15, bold=True, label='step ' + a)
        text(s, x, ty + 0.58, cw - 0.12, 0.6, b, size=12, color=T['text2'], label='step note ' + a)
    iy = ty + 1.35
    cutout(s, ORI('hero02_dedicated_grippers.png'), lx, iy, 5.3, 2.75, align='l')
    text(s, lx + 5.55, iy + 1.0, 2.2, 0.9, '작업별로 새로 만드는\n전용 그리퍼와 지그', size=13, color=T['text2'], label='grip cap')
    rx = 9.2; rw = W - MX - rx
    vline(s, rx - 0.45, y0 + 0.2, 4.6)
    text(s, rx, y0 + 0.12, rw, 1.5, '75%', size=80, bold=True, color=T['accent'], line=0.9, label='75')
    text(s, rx, y0 + 1.62, rw, 0.85, '로봇 도입 총비용(TCO) 중\n초기 셋업·재설계 비중', size=15, label='75 cap')
    text(s, rx, y0 + 2.5, rw, 0.25, '출처: BCG, 2026년 4월', size=10, color=T['muted'])
    text(s, rx, y0 + 3.05, rw, 1.0, ['비용 대부분이 설비 맞춤 작업에서 발생', '품목 전환이 잦을수록 자동화 지연'],
         size=13, color=T['text2'], space_after=6, bullet='–', indent=0.22, label='75 take')
    footer(s, 3)
    notes(s, 'BCG(2026.4): 기존 로봇 도입에서 총소유비용의 약 75%가 초기 셋업과 재설계(워크플로 구성, 신제품 대응, 기존 설비 통합). '
             '고객의 진짜 비용은 핸드 가격이 아니라 작업이 바뀔 때마다 반복되는 자동화 전환 비용.')


# ---------------------------------------------------------------- 04 solution
def s04(prs):
    s = new_slide(prs, '04 solution')
    y0 = header(s, '해결', '설비는 그대로, 핸드가 사람처럼 사용', '잡을 때는 부드럽게, 일할 때는 단단하게')
    iw = 2.3; ix = (W - iw) / 2
    cutout(s, REN('product.png'), ix, y0 + 0.05, iw, 3.45)
    cols = [
        (MX, '잡기', '부드러워야 잘 잡음', [('형상 차이 대응', '다른 부품·용기를 같은 핸드로'), ('위치 오차 흡수', '지그 의존도 감소'), ('미끄러짐 대응', '촉각·힘 제어')]),
        (ix + iw + 0.45, '일하기', '단단해야 일을 끝냄', [('토크 전달', '레버·노브 조작'), ('반력 지지', '문·손잡이 개폐'), ('모멘트 저항', '투입 자세 유지')]),
    ]
    cwid = ix - 0.45 - MX
    for x, h1, h2, items in cols:
        text(s, x, y0 + 0.15, cwid, 0.42, h1, size=20, bold=True)
        text(s, x, y0 + 0.62, cwid, 0.3, h2, size=12, color=T['muted'])
        hline(s, x, y0 + 1.0, cwid, color=T['text'], lw=1.0)
        yy = y0 + 1.12
        for a, b in items:
            text(s, x, yy, cwid, 0.3, a, size=15, bold=True, label='sol ' + a)
            text(s, x, yy + 0.32, cwid, 0.28, b, size=12, color=T['text2'], label='sol d ' + a)
            yy += 0.78
            hline(s, x, yy - 0.1, cwid)
    by = y0 + 3.7
    text(s, MX, by, 6, 0.3, '핵심 구조', size=12, bold=True, color=T['accent'])
    comps = [('부드러운 접촉면', '교체형 탄성 패드'), ('하중 지지 골격', '토크·반력은 골격이 부담'), ('대향 엄지', '손잡이·레버를 감싸 쥠'),
             ('가변 강성', '작업 순간 관절 강성 상승'), ('힘·미끄러짐 제어', '손끝 촉각 + 손목 힘센서')]
    ccw = CW / 5
    for i, (a, b) in enumerate(comps):
        x = MX + i * ccw
        text(s, x, by + 0.36, ccw - 0.15, 0.3, a, size=13, bold=True, label='comp ' + a)
        text(s, x, by + 0.66, ccw - 0.15, 0.28, b, size=11, color=T['text2'], label='comp d ' + a)
    footer(s, 4, note='4지(손가락 3 + 대향 엄지) 콘셉트 · 구동 방식(전동 텐던·유압·공압)은 창업 후 3개월 내 비교시험으로 결정 · 콘셉트 렌더링')
    notes(s, '설비를 로봇에 맞게 바꾸는 대신 로봇이 기존 설비를 사용. 잡기(순응성)와 일하기(강성)는 서로 충돌하므로 '
             '부드러운 접촉면 + 단단한 골격 + 전환 가능한 강성으로 해결. 4지(손가락 3 + 대향 엄지)는 머신텐딩 최소 구성, 5지는 Series A 이후.')


# ---------------------------------------------------------------- 05 product workflow
def s05(prs):
    s = new_slide(prs, '05 product')
    y0 = header(s, '제품', '핸드 하나로 공정 하나 완결', 'SoftHand-4 + 머신텐딩 스킬 팩, 핸드 교체 없이 6단계 처리')
    steps = [('s1_door', '문 열기', '손잡이 파지 후 개방'), ('s2_pick', '소재 집기', '트레이에서 소재 파지'),
             ('s3_load', '기계에 넣기', '바이스에 소재 투입'), ('s4_press', '버튼 누르기', '기존 조작 버튼 그대로'),
             ('s5_unload', '완성품 꺼내기', '가공 완료 부품 배출'), ('s6_close', '문 닫기', '다음 사이클 시작')]
    gap = 0.18; cw = (CW - 5 * gap) / 6; iy = y0 + 0.28; ih = 1.62
    for i, (f, a, b) in enumerate(steps):
        x = MX + i * (cw + gap)
        image(s, RAW(f + '_color.png'), x, iy, cw, ih, focus=(0.5, 0.5))
        text(s, x, iy + ih + 0.14, cw, 0.3, [[(f'{i + 1}  ', {'color': T['accent']}), (a, {})]], size=14, bold=True, label='wf ' + a)
        text(s, x, iy + ih + 0.48, cw, 0.5, b, size=11.5, color=T['text2'], label='wf note ' + a)
    by = iy + ih + 1.18
    hline(s, MX, by, CW, color=T['text'], lw=1.0)
    cols = [('1', '핸드', '로봇 1대에 핸드 1개'), ('5', '작업 종류', '열기·집기·투입·조작·배출'), ('0', '핸드 교체', '툴 체인저 없이 1사이클')]
    cw3 = CW / 3
    for i, (n, k, d) in enumerate(cols):
        x = MX + i * cw3 + (0.25 if i else 0)
        if i: vline(s, MX + i * cw3 - 0.02, by + 0.25, 1.05)
        text(s, x, by + 0.12, 1.1, 1.1, n, size=60, bold=True, color=T['accent'] if n == '0' else T['text'], line=0.9)
        text(s, x + 1.05, by + 0.35, cw3 - 1.45, 0.34, k, size=17, bold=True)
        text(s, x + 1.05, by + 0.74, cw3 - 1.45, 0.3, d, size=12, color=T['text2'], label='col ' + k)
    footer(s, 5, note='개념 공정 · 창업 후 6개월 내 대표 공정 반복시험, 단계별 완료율·사람 개입 시간 분리 보고 · 콘셉트 렌더링')
    notes(s, '6단계 = 5종 작업(열기와 닫기는 같은 스킬). 기존 방식은 그리퍼 2종 + 툴 체인저 + 자동문·I/O 개조. Seed 기간 검증 목표.')


# ---------------------------------------------------------------- 06 first market
def s06(prs):
    s = new_slide(prs, '06 market wedge')
    y0 = header(s, '첫 시장', '첫 시장은 다품종 머신텐딩', '공작기계 소재 투입·배출, 기존 설비를 크게 바꾸지 않는 자동화')
    iw, ih = 5.75, 3.3
    image(s, RAW('overview_color.png'), MX, y0 + 0.2, iw, ih, focus=(0.5, 0.5))
    text(s, MX, y0 + ih + 0.38, iw, 0.3, '첫 고객 (가설)', size=12, bold=True, color=T['accent'])
    text(s, MX, y0 + ih + 0.68, iw, 0.62, '다품종 가공 라인을 운영하는 중소·중견 제조사 생산기술팀, 도입은 로봇 SI 경유. 창업 후 90일 내 고객 인터뷰 30곳으로 검증',
         size=12, color=T['text2'], label='first buyer')
    rx = MX + iw + 0.55; rw = W - MX - rx
    text(s, rx, y0 + 0.2, rw, 0.32, '머신텐딩부터 시작하는 이유', size=14, bold=True, color=T['muted'])
    yy = y0 + 0.65
    for n, a, b in [(1, '사람용 장치가 한 셀에 집중', '문·손잡이·바이스 레버·버튼·트레이, 핸드 하나의 가치가 가장 큰 공정'),
                    (2, '전환 비용 측정 가능', '품목 변경·엔지니어링 시간·사람 개입을 PoC에서 고객 기존 수치와 비교'),
                    (3, 'SI가 이미 판매 중인 응용', '새 시장 개척 대신 기존 셀의 유연성 향상, SI 채널로 바로 진입')]:
        hgt = num_item(s, rx, yy, rw, n, a, b)
        yy += hgt + 0.28
    py = yy + 0.05
    hline(s, rx, py, rw, color=T['text'], lw=1.0)
    text(s, rx, py + 0.12, rw, 0.32, '원칙: 핸드가 경제적 가치를 만드는 작업부터', size=14, bold=True, label='principle')
    text(s, rx, py + 0.5, rw, 0.62,
         [[('우선  ', {'bold': True, 'color': T['text']}), ('다품종 부품 핸들링, 문·손잡이, 레버·노브·래치, 설비 조작부', {})],
          [('제외  ', {'bold': True, 'color': T['text']}), ('고속 단일 품목 반복, 고토크 체결, 진공이 유리한 평판', {})]],
         size=12, color=T['text2'], space_after=3, label='principle list')
    footer(s, 6, note='스크루드라이버 체결은 핵심 상용 작업이 아닌 기술 데모로 분리 (부록 A8) · 콘셉트 렌더링')
    notes(s, '모든 공구를 핸드로 대체한다고 주장하지 않음. 핸드를 썼을 때 설비 개조와 엔드이펙터 수가 줄어드는 작업부터 자동화.')


# ---------------------------------------------------------------- 07 customer value
def s07(prs):
    s = new_slide(prs, '07 value')
    y0 = header(s, '고객 가치', '구매 이유: 품목이 바뀌어도 다시 쓰는 자동화',
                '핸드 가격(가정 1,500만 원)의 비교 대상: 전용 툴링 + 설비 개조 + 엔지니어링 × 연간 전환 횟수')
    fy = y0 + 0.3
    hline(s, MX, fy, CW, color=T['text'], lw=1.0)
    flow_row(s, MX, fy + 0.16, CW, '기존 방식', ['새 작업', '새 그리퍼', '새 핑거', '새 지그', '엔지니어링', '티칭', '검증'])
    hline(s, MX, fy + 0.66, CW)
    flow_row(s, MX, fy + 0.82, CW, 'SoftHand', ['새 작업', '같은 핸드', '기존 스킬 재사용 또는 새 스킬 구성', '보정', '검증'],
             label_color=T['accent'], strong=('같은 핸드',))
    hline(s, MX, fy + 1.32, CW)
    text(s, MX, fy + 1.42, CW, 0.26, '엔지니어링·검증은 그대로 필요, 줄어드는 폭을 고객 현장에서 측정', size=11, color=T['muted'])
    vy = fy + 2.0; cw3 = (CW - 0.6) / 3
    for i, (a, b) in enumerate([('설비 개조 최소화', '설비 개조·고정구·추가 구동기를 줄일 가능성'),
                                ('반복 엔지니어링 감소', '전용 핑거·지그·티칭·통합 작업을 줄일 가능성'),
                                ('다음 작업에 재사용', '같은 핸드와 스킬 구조를 새 품목·다른 설비에 재사용')]):
        num_item(s, MX + i * (cw3 + 0.3), vy, cw3, i + 1, a, b, tsize=16)
    ky = vy + 1.32
    rect(s, MX, ky, CW, 1.05, fill=T['soft'])
    text(s, MX + 0.3, ky + 0.2, 2.4, 0.3, 'PoC 측정 지표', size=14, bold=True)
    text(s, MX + 0.3, ky + 0.52, 2.4, 0.3, '고객 기존 수치 대비', size=11, color=T['text2'])
    kpis = ['엔지니어링 시간', '전용 툴링 비용', '통합 기간', '사람 개입', '품목 전환 시간']
    kx = MX + 2.85; kw = (CW - 2.85 - 0.2) / 5
    for i, k in enumerate(kpis):
        x = kx + i * kw
        if i: vline(s, x - 0.12, ky + 0.22, 0.62, color='D5D8DC')
        text(s, x, ky + 0.2, kw - 0.2, 0.3, k, size=13, bold=True, label='kpi ' + k)
        text(s, x, ky + 0.52, kw - 0.2, 0.3, 'PoC에서 측정', size=11, color=T['accent'])
    footer(s, 7, note='감소율은 고객 기존 수치 확보 전이므로 확정하지 않음 · 유료 PoC에서 지불의사 검증 = Seed 투자의 사업 실험')
    notes(s, '고객에게 1,500만 원짜리 로봇 핸드를 파는 것이 아니라, 품목이 바뀌어도 다시 쓸 수 있는 자동화를 판다. '
             '엔지니어링과 검증이 사라진다고 주장하지 않음. 줄어드는 폭을 PoC에서 고객 기존 수치와 비교.')


# ---------------------------------------------------------------- 08 market size & why now
def s08(prs):
    s = new_slide(prs, '08 market')
    y0 = header(s, '시장', '첫 시장은 이미 공장에 설치된 로봇', '설치된 로봇과 신규 설치 로봇 모두 핸드 장착 대상')
    lw = 7.2
    stats = [([('약 ', {'size': 20}), ('500만 대', {})], '전 세계 가동 중\n산업용 로봇 (2025)'), ([('60만 대+', {})], '2025년 신규 설치\n전년 대비 +11%'),
             ([('1,220대', {})], '한국 로봇 밀도\n직원 1만 명당, 세계 1위')]
    sws = [2.75, 2.2, 2.25]
    x = MX
    for i, (v, k) in enumerate(stats):
        if i: vline(s, x - 0.18, y0 + 0.35, 1.45)
        text(s, x, y0 + 0.25, sws[i] - 0.3, 0.75, [v], size=30, bold=True, color=T['text'], label=f'stat {i}')
        text(s, x, y0 + 1.05, sws[i] - 0.3, 0.6, k, size=12, color=T['text2'], label=f'stat k {i}')
        x += sws[i]
    text(s, MX, y0 + 1.85, lw, 0.24, '출처: IFR World Robotics 2026 (2026.9), IFR 로봇 밀도 (2026.4)', size=10, color=T['muted'])
    by = y0 + 2.45
    hline(s, MX, by, lw, color=T['text'], lw=1.0)
    text(s, MX, by + 0.15, lw, 0.3, '5년차 계획 규모 (기본 시나리오)', size=12, bold=True, color=T['accent'])
    text(s, MX, by + 0.5, 2.0, 0.75, '200대', size=36, bold=True, label='200')
    text(s, MX + 2.05, by + 0.56, lw - 2.05, 0.75, '5년차 신규 핸드 판매 계획\n국내 연간 로봇 설치(약 3만 대)의 1% 미만', size=14, color=T['text2'], label='200 d')
    text(s, MX, by + 1.42, lw, 0.5, '장기 상한은 로봇 제조사 출하량 (OEM 탑재 시), 규모는 협의 후 산정', size=12, color=T['text2'], label='upper')
    rx = MX + lw + 0.6; rw = W - MX - rx
    vline(s, rx - 0.3, y0 + 0.3, 3.9)
    text(s, rx, y0 + 0.25, rw, 0.36, '왜 지금인가', size=18, bold=True)
    text(s, rx, y0 + 0.66, rw, 0.3, '로봇의 두뇌·눈·몸은 상용화, 남은 병목은 손', size=12, color=T['text2'], label='why sub')
    rows = [('두뇌', 'AI·VLA 모델', '빠르게 발전'), ('눈', '비전·엣지 컴퓨팅', '상용 수준'), ('몸', '로봇 팔·협동로봇', '대규모 보급'), ('손', '현실 세계 조작', '아직 병목')]
    yy = y0 + 1.15
    for i, (a, b, c) in enumerate(rows):
        hline(s, rx, yy, rw, color=T['text'] if i == 0 else T['line'], lw=1.0 if i == 0 else 0.75)
        last = a == '손'
        text(s, rx, yy + 0.14, 0.7, 0.32, a, size=15, bold=True, color=T['accent'] if last else T['text'])
        text(s, rx + 0.7, yy + 0.16, 1.85, 0.3, b, size=12, color=T['text2'], label='why b ' + a)
        text(s, rx + 2.55, yy + 0.14, rw - 2.55, 0.32, c, size=14, bold=last, color=T['accent'] if last else T['text'], align='r', label='why c ' + a)
        yy += 0.62
    hline(s, rx, yy, rw)
    text(s, rx, yy + 0.14, rw, 0.5, '근거와 사례는 부록 A4', size=11, color=T['muted'])
    footer(s, 8)
    notes(s, 'IFR World Robotics 2026: 2025년 가동 대수 약 500만 대(+9%), 신규 설치 60만 대 이상(+11%). IFR 로봇 밀도: 한국 1,220대/직원 1만 명(세계 최고). '
             '5년차 판매 계획 200대는 국내 연간 설치의 1% 미만. 휴머노이드를 기다리지 않고 이미 공장에 있는 로봇부터 공략.')


# ---------------------------------------------------------------- 09 productization / not an SI company
def s09(prs):
    s = new_slide(prs, '09 productization')
    y0 = header(s, '확장성', '고객 프로젝트를 표준 스킬로 축적', '2번째 고객부터 재사용, 다른 로봇에도 같은 스킬 적용 (SI 사업화 방지 구조)')
    lx = MX; lw = 5.75
    steps = [('고객 프로젝트', '현장별 작업 수행'), ('공통 작업 추출', '문 열기·투입·버튼 등 반복 작업 분리'), ('재사용 스킬', '로봇과 무관한 작업 정의'),
             ('검증된 스킬 팩', '승인 작업 목록으로 판매'), ('다음 고객', '같은 스킬 재사용, 고객별 구성만 추가')]
    sy = y0 + 0.32; step = 0.6
    vline(s, lx + 0.05, sy + 0.12, step * 4, color=T['text'], lw=1.25)
    for i, (a, b) in enumerate(steps):
        yy = sy + i * step
        dot(s, lx + 0.05, yy + 0.12, d=0.12, fill=T['accent'] if i == 4 else T['text'])
        text(s, lx + 0.32, yy, 2.1, 0.3, a, size=14, bold=True, label='loop ' + a)
        text(s, lx + 2.45, yy + 0.02, lw - 2.45, 0.3, b, size=12, color=T['text2'], label='loop d ' + a)
    ry = sy + step * 4 + 0.55
    hline(s, lx, ry, lw, color=T['text'], lw=1.0)
    table(s, lx, ry + 0.05, lw, None,
          [[('재사용', {'bold': True}), '핸드 · 런타임 · 기본 동작 · 작업 스킬 · 보정 도구'],
           [('고객별 구성', {'bold': True}), '부품 형상 등록 · 셀 배치 · 안전 검증'],
           [('운영 규칙', {'bold': True}), '승인 작업 목록 안에서만 수주, 비표준 요청은 별도 견적, 종료 시 공통 모듈 반영']],
          col_w=[1.4, lw - 1.4], size=12, pad=0.07, label='reuse table', max_h=7.0 - (ry + 0.05))
    rx = lx + lw + 0.55; rw = W - MX - rx
    text(s, rx, y0 + 0.25, rw, 0.32, '로봇 2종 호환 검증', size=14, bold=True, color=T['muted'])
    pw = (rw - 0.2) / 2; ph = pw * 0.75
    for i, (f, lab) in enumerate([('portA_color.png', '로봇 A · 협동로봇 6축'), ('portB_color.png', '로봇 B · 다른 브랜드·링크 길이')]):
        x = rx + i * (pw + 0.2)
        image(s, RAW(f), x, y0 + 0.65, pw, ph, focus=(0.5, 0.45))
        text(s, x, y0 + 0.72 + ph, pw, 0.26, lab, size=11, color=T['text2'], label='port ' + lab)
    ky = y0 + 1.1 + ph
    text(s, rx, ky, rw, 0.3, '같은 문 열기 스킬, 어댑터·좌표·카메라 보정만 재설정', size=12, label='port cap')
    hline(s, rx, ky + 0.42, rw, color=T['text'], lw=1.0)
    text(s, rx, ky + 0.55, rw, 0.32, [[('핵심 지표  ', {'color': T['accent']}), ('재사용률', {})]], size=15, bold=True)
    text(s, rx, ky + 0.92, rw, 0.62, '신규 고객 적용 시 그대로 쓴 하드웨어·제어·스킬·소프트웨어 비중. M12 측정 시작, M24까지 상승 추세 확인 (임의 목표치 없음)',
         size=12, color=T['text2'], label='kpi desc')
    footer(s, 9, note='검증 가설: 로봇이 바뀔 때마다 처음부터 다시 티칭해야 하면 플랫폼이 아닌 SI 사업 · 콘셉트 렌더링')
    notes(s, 'SI가 되지 않는 규칙: 승인 작업 목록 안에서만 수주, 비표준 요청은 별도 견적, 프로젝트 종료 시 공통 모듈을 라이브러리에 반영, 재사용 매출 비중을 경영 지표로 관리. '
             '로봇 B 통합은 M12~M18, 이식성 검증은 M18~M24.')


# ---------------------------------------------------------------- 10 business model & GTM
def s10(prs):
    s = new_slide(prs, '10 business model')
    y0 = header(s, '사업 모델', '제품 판매로 시작, 스킬과 로봇 제조사 탑재로 확장', '통합 엔지니어링 매출은 초기 진입·제품화 수단, 비중 축소 목표')
    stages = [
        ('1단계 · Seed (M0~M24)', 'SI와 함께 진입', '로봇 SI, 공동개발 고객, 유료 PoC', '핸드, 유료 PoC, 통합, 작업 스킬', '공동개발 고객 3곳, 유료 PoC 5건,\n재구매 고객 2곳'),
        ('2단계 · 3~5년차', '직판 + SI 파트너', '검증된 스킬 팩을 SI 파트너망으로 판매', '재사용 스킬, 런타임·유지보수, 핸드', '재사용 매출 비중 86%\n(5년차, 기본 시나리오)'),
        ('3단계 · 확장 계기', '로봇 제조사(OEM) 탑재', '핸드·런타임을 로봇 옵션으로 탑재', '라이선스, 내장 런타임,\n출하량 연동 로열티', 'OEM 채택(디자인 윈) 1건'),
    ]
    gap = 0.3; cw = (CW - 2 * gap) / 3; ty = y0 + 0.3
    for i, (st, nm, ch, rv, goal) in enumerate(stages):
        x = MX + i * (cw + gap)
        text(s, x, ty, cw, 0.28, st, size=12, bold=True, color=T['accent'])
        text(s, x, ty + 0.32, cw, 0.42, nm, size=19, bold=True, label='stage ' + nm)
        hline(s, x, ty + 0.85, cw, color=T['text'], lw=1.0)
        yy = ty + 0.97
        for lab, val in [('판매', ch), ('매출', rv), ('목표', goal)]:
            text(s, x, yy, 0.6, 0.26, lab, size=11, color=T['muted'])
            hh = text_h(val, 13, cw - 0.62)
            text(s, x + 0.62, yy, cw - 0.62, hh + 0.02, val, size=13, color=T['text'], label=f'stage {nm} {lab}')
            yy += max(hh, 0.3) + 0.2
            hline(s, x, yy - 0.1, cw)
    fy = ty + 3.25
    rect(s, MX, fy, CW, 1.12, fill=T['soft'])
    text(s, MX + 0.3, fy + 0.18, 2.3, 0.3, 'OEM 매출 구조', size=14, bold=True)
    text(s, MX + 0.3, fy + 0.5, 2.3, 0.5, '고객 한 곳씩 영업에서\n출하량 연동으로 전환', size=11, color=T['text2'])
    parts = ['대상 로봇 출하량', '×', '옵션 채택률', '×', '대당 핸드·런타임 매출', '=', 'OEM 매출']
    px = MX + 2.85; widths = [2.1, 0.35, 1.7, 0.35, 2.55, 0.35, 1.5]
    for p, wd in zip(parts, widths):
        op = p in '×='
        text(s, px, fy + 0.2, wd, 0.4, p, size=18 if op else 14, bold=not op, color=T['muted'] if op else (T['accent'] if p == 'OEM 매출' else T['text']),
             align='c' if op else 'l', label='oem ' + p)
        if not op and p != 'OEM 매출':
            text(s, px, fy + 0.6, wd, 0.26, '[OEM 협의 후 검증]', size=10, color=T['muted'])
        px += wd
    footer(s, 10, note='로봇 제조사는 팔·제어기에 집중, 핸드는 파트너 생태계 의존 · 경쟁자이자 판매 채널 (부록 A3)')
    notes(s, '초기에는 제품회사처럼 돈을 벌고, 장기에는 플랫폼 수익 구조로 확장. 통합 매출을 숨기지 않되 장기 모델이 아닌 진입·제품화 수단으로 정의. '
             'OEM 매출은 숫자를 계산하지 않고 구조만 제시 (기존 300억~1,800억 계산 삭제).')


# ---------------------------------------------------------------- 11 competition
def s11(prs):
    s = new_slide(prs, '11 competition')
    y0 = header(s, '경쟁', '경쟁 기준은 설비 변경 없이 끝낸 작업 수', '구매 기준: 손가락 수보다 실제 작업 완료와 설비 변경 최소화')
    cats = [
        ('전통 그리퍼', '정확성·신뢰성 높음, 특정 작업 중심', '정밀·저가·고속', '작업 변경 시 핑거·지그 교체, 문·레버는 설비 개조', '한계'),
        ('적응형 그리퍼', '다양한 형상 파지에 강점', '여러 형상을 하나로 파지', '손잡이 감아 당기기·레버 토크 제한, 결국 설비 개조', '한계'),
        ('다지 로봇 핸드', '높은 자유도, 복잡한 조작', '사람 손에 가까운 조작', '비용·내구성·통합 난이도, 연구·휴머노이드 중심', '한계'),
        ('SoftHand-4', '사람용 장치를 핸드 교체 없이 조작 (목표)', '부품·문·레버를 핸드 하나로', '산업 내구성·재사용 스킬, Seed 기간 검증', '과제'),
    ]
    gap = 0.18; cw = (CW - 3 * gap) / 4; ty = y0 + 0.3
    for i, (nm, one, st, lim, lim_lab) in enumerate(cats):
        x = MX + i * (cw + gap); ours = i == 3
        if ours: rect(s, x - 0.12, ty - 0.15, cw + 0.24, 3.38, fill=T['accent_soft'])
        text(s, x, ty, cw, 0.4, nm, size=18, bold=True, color=T['accent'] if ours else T['text'], label='cat ' + nm)
        text(s, x, ty + 0.45, cw, 0.6, one, size=12, color=T['text2'], label='cat one ' + nm)
        hline(s, x, ty + 1.1, cw, color=T['text'], lw=1.0)
        text(s, x, ty + 1.22, cw, 0.24, '강점', size=11, color=T['muted'])
        text(s, x, ty + 1.48, cw, 0.6, st, size=13, label='cat st ' + nm)
        hline(s, x, ty + 2.08, cw)
        text(s, x, ty + 2.2, cw, 0.24, lim_lab, size=11, color=T['muted'])
        text(s, x, ty + 2.46, cw, 0.72, lim, size=13, label='cat lim ' + nm)
    py = ty + 3.55
    text(s, MX, py, CW, 0.3, 'Seed 기간 증명 항목', size=12, bold=True, color=T['accent'])
    items = [('동일 조건 비교시험', '같은 작업·같은 로봇, 전용 그리퍼 대비'), ('승인 작업 완료율 95%+', '목표, 최초 시도·재시도 분리 보고'),
             ('내구성 30만 회', '반복 개폐 목표, 패드 교체 주기 명시'), ('총비용 비교', '전용 그리퍼 N개 + 엔지니어링 대비')]
    iw = CW / 4
    for i, (a, b) in enumerate(items):
        x = MX + i * iw
        text(s, x, py + 0.34, iw - 0.2, 0.3, a, size=14, bold=True, label='proof ' + a)
        text(s, x, py + 0.66, iw - 0.2, 0.3, b, size=11, color=T['text2'], label='proof d ' + a)
    footer(s, 11, note='공개 정보 기반 정성 비교, 독립 비교시험 아님 · 회사명·상세 사양은 부록 A3')
    notes(s, 'Adaptive Gripper는 형상 파지에 강하지만 문·레버 조작과 공구 토크는 제한적이라 결국 설비 개조가 필요. '
             '다지 핸드는 비용·내구성 때문에 연구·휴머노이드 중심. 우리는 손가락 수가 아니라 설비 변경 없이 끝낸 작업 수로 경쟁.')


# ---------------------------------------------------------------- 12 financials
def s12(prs):
    s = new_slide(prs, '12 financials')
    B = M['base']; A = M['assumptions']
    y0 = header(s, '재무 계획', f'5년차 매출 {B["rev"][4]:.1f}억 원, 손익분기 근접', '기본 시나리오: 주방·로봇 제조사(OEM) 매출 0원, 모든 수치는 검증 전 가정')
    eng = B['poc_int']; reuse = [r - p for r, p in zip(B['rev'], eng)]
    cx, cy, cw_, chh = MX, y0 + 0.95, 6.1, 3.45
    plot = (0.02, 0.1, 0.96, 0.8); vmax = 50
    text(s, MX, y0 + 0.2, 4, 0.3, '연도별 매출 (억 원)', size=12, bold=True, color=T['muted'])
    lg = MX
    for col, lab in [(T['grey_bar'], '고객별 엔지니어링 (PoC·통합)'), (T['accent'], '재사용 매출 (핸드·스킬·런타임·파트너)')]:
        rect(s, lg, y0 + 0.6, 0.13, 0.13, fill=col)
        text(s, lg + 0.2, y0 + 0.52, 3.2, 0.28, lab, size=11, color=T['text2'], check=False)
        lg += 0.3 + text_w(lab, 11) + 0.35
    column_chart(s, cx, cy, cw_, chh, ['1년차', '2년차', '3년차', '4년차', '5년차'],
                 [('고객별 엔지니어링', eng), ('재사용 매출', reuse)], [T['grey_bar'], T['accent']], stacked=True, vmax=vmax,
                 show_labels=False, gap=55, plot=plot, size=12)
    px, py, pw, ph = plot
    for i, tot in enumerate(B['rev']):
        ccx = cx + cw_ * (px + pw * (i + 0.5) / 5)
        top = cy + chh * (py + ph * (1 - tot / vmax))
        text(s, ccx - 0.6, top - 0.34, 1.2, 0.3, f'{tot:.1f}', size=13, bold=True, align='c', check=False)
    rx = MX + 6.55; rw = W - MX - rx
    rows = [['매출 (억 원)'] + [f'{v:.1f}' for v in B['rev']],
            ['매출총이익률'] + [f'{v * 100:.0f}%' for v in B['gm']],
            ['영업손익 (억 원)'] + [f'{v:.1f}'.replace('-', '−') for v in B['op']],
            ['신규 핸드 (대)'] + [str(int(v)) for v in B['hands_new']],
            [('재사용 매출 비중', {'bold': True})] + [(f'{v * 100:.0f}%', {'bold': True, 'color': T['accent']}) for v in B['reuse_share']]]
    table(s, rx, y0 + 0.2, rw, ['구분', '1년', '2년', '3년', '4년', '5년'], rows,
          col_w=[1.75] + [(rw - 1.75) / 5] * 5, size=12, align=['l', 'r', 'r', 'r', 'r', 'r'], pad=0.07, label='fin table')
    sy = y0 + 2.6
    text(s, rx, sy, rw, 0.3, '민감도 (5년차)', size=12, bold=True, color=T['accent'])
    sens = [('판매량 −30%', '매출 31.4억 · 영업손익 −7.1억'), ('SI 채널 1년 지연', '매출 32.3억 · 영업손익 −6.4억'),
            ('핸드 원가 절감 지연', '영업손익 −3.1억'), ('판매량 −50%', '매출 22.4억 · 영업손익 −11.9억')]
    table(s, rx, sy + 0.32, rw, None, [[(a, {'bold': True}), b] for a, b in sens], col_w=[1.95, rw - 1.95], size=12, pad=0.06, label='sens')
    footer(s, 12, note='1·2년차 운영비 = Seed 집행 계획 · 미반영 상승 요인: 주방 공동 제품화, OEM 채택 · 상세 부록 A10')
    notes(s, f'기본 시나리오: 핸드 직판 1,500만 원, 파트너 경유 1,200만 원, 스킬 300만 원, 런타임 연 150만 원, 유료 PoC 5,000만 원. 핸드 원가 950만 원에서 750만 원으로 절감 가정. '
             f'주방·OEM 매출 0원. 기존 덱의 5년차 112억(주방 50억 포함) 대신 사업 구조와 같은 숫자로 재산정.')


# ---------------------------------------------------------------- 13 roadmap
def s13(prs):
    s = new_slide(prs, '13 roadmap')
    y0 = header(s, '로드맵', '24개월 4단계 검증 계획', '단계마다 질문 하나, 미달 시 다음 단계 자금 집행 재검토')
    phases = [
        ('M0~M6', '기술 검증', '핸드 하나로 대표 공정 수행', ['법인 설립·핵심 인력 합류', 'SoftHand-4 알파 시제품', '머신텐딩 대표 공정 시연', '고객 인터뷰 30곳', '공동개발 고객 후보 확보', '반복 실험 기록']),
        ('M6~M12', '고객 검증', '고객이 돈을 낼 이유 확인', ['첫 유료 PoC', '고객 기존 수치 확보', '엔지니어링 시간 측정', '툴링 비용·통합 기간 측정', '작업 스킬 V1']),
        ('M12~M18', '제품 검증', '반복 판매되는 제품 확인', ['설계 확정·BOM·공급사', '내구성·제조원가 검증', '첫 재구매', '첫 재사용 스킬 팩', '재사용률 측정 시작', '로봇 B 통합']),
        ('M18~M24', '확장 검증', '확장 가능한 구조 확인', ['유료 PoC 5건+', '재구매 고객 2곳+', '재사용 스킬 다수 확보', '로봇 2종 스킬 호환', '매출총이익률 검증', 'Series A 준비']),
    ]
    gap = 0.25; cw = (CW - 3 * gap) / 4; ty = y0 + 0.35
    hline(s, MX, ty + 0.05, CW, color=T['text'], lw=1.25)
    for i, (per, nm, q, items) in enumerate(phases):
        x = MX + i * (cw + gap)
        dot(s, x + 0.05, ty + 0.05, d=0.12, fill=T['accent'] if i == 3 else T['text'])
        text(s, x, ty + 0.22, cw, 0.28, per, size=12, bold=True, color=T['accent'])
        text(s, x, ty + 0.52, cw, 0.4, nm, size=19, bold=True, label='ph ' + nm)
        text(s, x, ty + 0.95, cw, 0.3, q, size=12, color=T['text2'], label='ph q ' + nm)
        text(s, x, ty + 1.38, cw, 2.2, items, size=12, bullet='•', indent=0.17, space_after=4, label='ph items ' + nm)
    gy = ty + 3.55
    rect(s, MX, gy, CW, 0.95, fill=T['soft'])
    text(s, MX + 0.25, gy + 0.15, 2.0, 0.3, '점검 기준', size=13, bold=True)
    text(s, MX + 0.25, gy + 0.47, 2.0, 0.3, '미달 시 결정', size=11, color=T['text2'])
    gates = [('M6', '토크·반복성 미확보', '핸드 구조 재검토'), ('M12', '지불의사 없음', '첫 시장·작업 재정의'),
             ('M18', '재사용률 낮음', '플랫폼 가설 재검토'), ('M24', '재구매 없음', 'Series A 확장 보류')]
    gx = MX + 2.2; gw = (CW - 2.2) / 4
    for i, (m, c, d) in enumerate(gates):
        x = gx + i * gw
        text(s, x, gy + 0.15, gw - 0.15, 0.3, [[(m + '  ', {'color': T['accent']}), (c, {})]], size=12, bold=True, label='gate ' + m)
        text(s, x, gy + 0.47, gw - 0.15, 0.3, d, size=12, color=T['text2'], label='gate d ' + m)
    footer(s, 13, note='보조 일정: 주방 벤치 데모 (M19~M24) · 단계별 상세 기준 부록 A2')
    notes(s, '투자금을 단순 R&D 소비가 아닌 가설 검증 자본으로 운영. 각 단계 점검은 이사회·투자자와 분기별 지표 리뷰로 판단.')


# ---------------------------------------------------------------- 14 team
def s14(prs):
    s = new_slide(prs, '14 team')
    y0 = header(s, '팀', '이 문제를 풀 수 있는 팀', '창업자 2명 + 핵심 인력 6명 단계 채용')
    fx = MX; fw = 5.3
    for i, (role, hint) in enumerate([('대표 · 사업/제품', '산업 경력·직무·기간'), ('CTO · 핸드 메카트로닉스', '시제품·연구실적·특허')]):
        yy = y0 + 0.3 + i * 1.62
        rect(s, fx, yy, 1.2, 1.38, fill=T['soft'])
        text(s, fx, yy + 0.55, 1.2, 0.3, '사진', size=11, color=T['muted'], align='c')
        text(s, fx + 1.45, yy + 0.0, fw - 1.45, 0.36, '[이름 입력 필요]', size=17, bold=True)
        text(s, fx + 1.45, yy + 0.4, fw - 1.45, 0.28, role, size=12, bold=True, color=T['accent'])
        text(s, fx + 1.45, yy + 0.76, fw - 1.45, 0.62, [f'{hint}: [정보 입력 필요]', '사업과 직접 연결되는 경험만 기재'], size=12,
             color=T['text2'], space_after=3, label='founder ' + role)
    hy = y0 + 3.62
    hline(s, fx, hy, fw, color=T['text'], lw=1.0)
    text(s, fx, hy + 0.12, fw, 0.3, 'Seed 채용 계획 (6명 단계 채용)', size=12, bold=True)
    text(s, fx, hy + 0.42, fw, 0.6, '기구·구동, 제어·임베디드, 로봇 SW·스킬, 현장 통합, 비전·AI, 설계·품질', size=12, color=T['text2'], label='hire')
    rx = fx + fw + 0.55; rw = W - MX - rx
    text(s, rx, y0 + 0.3, rw, 0.32, '투자자가 확인할 3가지', size=14, bold=True, color=T['muted'])
    qs = [('왜 이 창업자가 이 문제를 발견했나', '창업 계기, 현장에서 직접 겪은 전환 비용 문제'),
          ('왜 이 팀이 이 제품을 만들 수 있나', '핸드 메카트로닉스·제어·현장 통합 역량의 근거'),
          ('왜 이 팀이 첫 고객을 확보할 수 있나', '고객 네트워크·공동개발 고객 후보·SI 관계')]
    yy = y0 + 0.75
    for i, (q, h_) in enumerate(qs):
        hline(s, rx, yy, rw, color=T['text'] if i == 0 else T['line'], lw=1.0 if i == 0 else 0.75)
        text(s, rx, yy + 0.13, 0.5, 0.32, f'Q{i + 1}', size=15, bold=True, color=T['accent'])
        text(s, rx + 0.55, yy + 0.13, rw - 0.55, 0.32, q, size=15, bold=True, label='q ' + q)
        text(s, rx + 0.55, yy + 0.48, rw - 0.55, 0.28, h_, size=12, color=T['text2'], label='q h ' + q)
        text(s, rx + 0.55, yy + 0.76, rw - 0.55, 0.28, '[정보 입력 필요]', size=12, color=T['accent'])
        yy += 1.1
    hline(s, rx, yy, rw)
    by = H - 0.95
    text(s, MX, by, CW, 0.26, [[('참여 조건   ', {'bold': True, 'color': T['text']}),
                                ('전업 참여 · 자기자본 투자 · 공동창업자 · 시제품 경험 · 연구실적 · 특허 · 고객 네트워크 · 공동개발 고객 후보 · 현 직장 정리 계획  ', {}),
                                ('[정보 입력 필요]', {'color': T['accent']})]], size=11, color=T['text2'], label='commit')
    footer(s, 14, note='없는 정보는 만들지 않음 · 외부 제출 전 실제 정보로 교체 필요')
    notes(s, 'Founder 장표의 목적은 이력 나열이 아니라 세 질문에 대한 답. 로봇·자동화·제조·AI·기계설계·현장 통합·고객 네트워크 중 사업과 직접 연결되는 경험만 선택.')


# ---------------------------------------------------------------- 15 ask
def s15(prs):
    s = new_slide(prs, '15 ask')
    SP = M['seed']
    y0 = header(s, '투자 요청', 'Seed 20억 원, 24개월 사업성 검증', '18개월 핵심 운영 + 6개월 연장, 매출이 없어도 24개월 운영 가능')
    lx = MX; lw = 3.55
    text(s, lx, y0 + 0.2, lw, 1.02, '20억 원', size=52, bold=True, color=T['accent'], line=0.95, label='ask big')
    text(s, lx, y0 + 1.15, lw, 0.3, 'Seed  ·  24개월', size=15, color=T['text2'])
    yy = y0 + 1.7
    contingency = SP['uof'][-1][1]
    for k, v in [('18개월 핵심 운영', SP['core18']), ('6개월 연장', SP['ext6']), ('예비비·운전자본', contingency)]:
        hline(s, lx, yy, lw, color=T['text'] if k.startswith('18') else T['line'], lw=1.0 if k.startswith('18') else 0.75)
        text(s, lx, yy + 0.13, 2.2, 0.3, k, size=13, label='struct ' + k)
        text(s, lx + 2.2, yy + 0.13, lw - 2.2, 0.3, f'{v:.1f}억', size=14, bold=True, align='r')
        yy += 0.52
    hline(s, lx, yy, lw)
    text(s, lx, yy + 0.18, lw, 0.6, '투자 조건 (기업가치·지분율)\n[투자 조건 입력 필요]', size=12, color=T['text2'], label='terms')
    mx_ = lx + lw + 0.5; mw = 4.35
    text(s, mx_, y0 + 0.2, mw, 0.3, '자금 사용 계획 (억 원)', size=12, bold=True, color=T['muted'])
    names = {'핵심 인력 (8명 단계 채용)': '핵심 인력 8명', 'Prototype · 내구시험': '시제품·내구시험', 'Robot 2종 · 시험 Cell': '로봇 2종·시험 셀',
             '고객 PoC · 현장통합(비청구)': '고객 PoC·현장 통합', 'SW · AI · Data': 'SW·AI·데이터', '제조 · 품질 · 안전 · IP': '제조·품질·안전·IP',
             'Kitchen Bench Demo': '주방 벤치 데모', '운영 (임차·법무·회계·보험·출장)': '운영·관리', '예비비 · 운전자본': '예비비·운전자본'}
    uof = [(names.get(k, k), v) for k, v in SP['uof']]
    bar_chart(s, mx_, y0 + 0.55, mw, 3.7, [k for k, _ in uof], [round(v, 2) for _, v in uof], T['grey_bar'],
              labels=[f'{v:.1f}' for _, v in uof], colors=[T['accent']] + [T['grey_bar']] * (len(uof) - 1),
              plot=(0.43, 0.0, 0.47, 1.0), size=11, vmax=11, gap=40)
    rx = mx_ + mw + 0.5; rw = W - MX - rx
    text(s, rx, y0 + 0.2, rw, 0.3, '24개월 뒤 Series A 조건 (목표)', size=12, bold=True, color=T['muted'])
    goals = [('유료 PoC', '5건+'), ('재구매 고객', '2곳+'), ('공동개발 고객', '3곳'), ('승인 작업 완료율', '95%+'), ('내구성', '30만 회'),
             ('로봇 2종 스킬 호환', '검증'), ('재사용률', '상승 추세'), ('핸드 원가(BOM)', '검증')]
    table(s, rx, y0 + 0.55, rw, None, [[k, (v, {'bold': True, 'align': 'r'})] for k, v in goals], col_w=[rw - 1.15, 1.15], size=12, pad=0.075, label='goals')
    footer(s, 15, note='정부지원금·공동개발비 제외 · 인건비: 창업자 연 5,000만 원, 엔지니어 연 7,000만 원 (+15%) · 상세 부록 A11')
    notes(s, f'핵심 인력 8명 단계 채용 {SP["pers_total"]:.1f}억 포함. 18개월 핵심 운영 {SP["core18"]:.1f}억으로 설계 확정과 첫 재구매까지, 18개월 점검을 통과하면 6개월 연장 {SP["ext6"]:.1f}억 집행. '
             f'매출이 없어도 24개월 뒤 예비비 {contingency:.1f}억 잔존.')


# ---------------------------------------------------------------- 16 closing
def s16(prs):
    s = new_slide(prs, '16 closing')
    text(s, MX, 0.7, CW, 0.68, '공장에서 시작, 사람 손이 필요한 현장으로 확장', size=32, bold=True, label='closing title')
    text(s, MX, 1.38, CW, 0.32, '하나의 핸드로 여러 작업 · 고객 작업을 재사용 스킬로 · 같은 스킬을 여러 로봇에서', size=15, color=T['text2'], label='closing sub')
    cols = [('공장', '지금 · Seed', '머신텐딩 매출로 사업성 검증', ['유료 PoC · 재구매 · 재사용 스킬', '기본 시나리오 매출의 100%'], ('img', RAW('overview_color.png'), (0.5, 0.5))),
            ('주방', '다음 · 기술 데모', '사람용 도구·설비 사용 능력 검증', ['Seed: 단일 팔 벤치 데모 (0.3억 원)', '회수기간이 가동률에 민감해 첫 매출원 제외'], ('img', RAW('kitchen_color.png'), (0.5, 0.55))),
            ('로봇 제조사', '장기 · 확장', '핸드·스킬 기본 탑재', ['피지컬 AI의 조작 계층', '출하량 연동 매출, 규모는 협의 후 산정'], ('cut', REN('closing.png'), None))]
    gap = 0.3; cw = (CW - 2 * gap) / 3; iy = 1.95; ih = 1.9
    for i, (nm, when, a, b, img) in enumerate(cols):
        x = MX + i * (cw + gap)
        if img[0] == 'img':
            image(s, img[1], x, iy, cw, ih, focus=img[2])
        else:
            rect(s, x, iy, cw, ih, fill='EEF0F2')
            cutout(s, img[1], x, iy + 0.1, cw, ih - 0.2)
        text(s, x, iy + ih + 0.15, cw, 0.36, [[(nm, {}), ('   ' + when, {'size': 12, 'bold': False, 'color': T['accent']})]], size=17, bold=True, label='cl ' + nm)
        text(s, x, iy + ih + 0.55, cw, 0.3, a, size=13, bold=True, color=T['text'], label='cl a ' + nm)
        text(s, x, iy + ih + 0.86, cw, 0.56, b, size=12, color=T['text2'], label='cl b ' + nm)
    by = 5.62
    rect(s, 0, by, W, H - by, fill=T['dark'])
    text(s, MX, by + 0.38, 5.0, 0.46, 'ONE HAND. MANY TOOLS.', size=22, bold=True, color=T['on_dark'])
    text(s, MX, by + 0.9, 5.4, 0.5, '[회사명 입력 필요]\n[대표자명 · 이메일 · 연락처 입력 필요]', size=11, color=T['on_dark2'], label='contact')
    rx = 6.55
    text(s, rx, by + 0.38, W - MX - rx, 0.46, [[('Seed 20억 원', {'color': T['accent']}), ('  ·  24개월', {'color': T['on_dark']})]], size=22, bold=True)
    proofs = ['제품', '유료 고객', '반복 구매', '스킬 재사용']
    pw = (W - MX - rx) / 4
    for i, p in enumerate(proofs):
        x = rx + i * pw
        text(s, x, by + 0.92, pw - 0.1, 0.25, f'증명 {i + 1}', size=10, color=T['on_dark2'])
        text(s, x, by + 1.16, pw - 0.1, 0.32, p, size=15, bold=True, color=T['on_dark'])
    notes(s, '기존 생산설비에서 시작. 하나의 핸드로 여러 작업을 수행하고, 고객 프로젝트를 재사용 스킬로 제품화하고, 같은 스킬을 여러 로봇에서 쓸 수 있음을 증명. '
             '이후 로봇 제조사로 확장해 피지컬 AI의 조작 계층이 되는 것이 장기 목표. 공장이 사업성을, 주방이 기술의 확장성을 증명.')


MAIN = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16]
