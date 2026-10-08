# MH Robotics — Seed · TIPS 운영사 검토용 Main IR Deck (18 slides, Spec 35 order).
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
              visual='좌측 짙은 패널: 회사명 · 제품 정의 · 검토 용도 · 현재 단계. 우측 3D 콘셉트 렌더: 구축 아파트 주방 한 벽에 설치된 로봇 (Robot Home · Rail · 식기세척기 Interface).',
              chart='3D 콘셉트 렌더 1개 (CONCEPT)',
              note=('MH Robotics는 다양한 실제 주방에서 식기 정리부터 조리까지 단계적으로 수행하는 주거용 Manipulation Robotics System을 만듭니다. '
                    '핵심은 로봇손, 작업 Skill, Calibration, 주방 Interface를 하나의 제품으로 묶는 것입니다. '
                    '첫 검증 Workflow는 식기 정리, 즉 CLEAN이고, 같은 Platform 위에 ASSIST와 COOK을 단계적으로 올립니다. '
                    '현재는 Concept 단계로 시제품, 고객, 계약, LOI, 파트너, 매출이 없습니다. 오늘은 Seed와 TIPS 24개월 동안 어떤 증거를 만들지 말씀드리겠습니다.'))
    pw = 5.35
    rect(s, 0, 0, pw, H, fill=INK)
    x = 0.62; w = pw - 1.0
    text(s, x, 0.72, w, 0.3, 'M H   R O B O T I C S', size=12, bold=True, color='A9AEB5')
    text(s, x, 1.3, w, 1.95, 'Kitchen Manipulation\nRobotics System', size=30, bold=True, color='FFFFFF', line=1.0)
    text(s, x, 3.28, w, 0.62, '로봇손 · 작업 Skill · Calibration · 주방 Interface를 하나의 제품으로', size=13.5, bold=True,
         color='E3E5E8', line=1.05)
    text(s, x, 3.98, w, 0.48, '다양한 실제 주방에서 식기 정리부터 조리까지 단계적으로 확장하는 주거용 Manipulation Robotics',
         size=10.5, color='A9AEB5', line=1.05)
    hline(s, x, 4.7, w, color='3A3F46', lw=1.0)
    for i, (a, b) in enumerate([('CLEAN', '첫 검증 Workflow (식기 정리)'), ('ASSIST', '중기 확장 (재료 이동 · 투입 · 도구)'),
                                ('COOK', '장기 R&D 방향 (Recipe Workflow)')]):
        yy = 4.88 + i * 0.36
        text(s, x, yy, 1.0, 0.3, a, size=11, bold=True, color='FFFFFF' if i == 0 else '80868D', anchor='m')
        text(s, x + 1.0, yy, w - 1.0, 0.3, b, size=10, color='C9CDD2' if i == 0 else '80868D', anchor='m')
    text(s, x, 6.32, w, 0.26, 'Seed 투자 · TIPS 운영사 검토용  |  2026.10.08  |  Draft v5', size=9.5, color='A9AEB5')
    text(s, x, 6.62, w, 0.42, 'Concept 단계 — 시제품 · 고객 · 계약 · LOI · 파트너 · 매출 없음 (FACT). 수치는 FACT · DERIVED · ASSUMPTION · TARGET 구분',
         size=8.5, color='80868D', line=1.05)
    rx = pw; rw = W - pw
    at = render(s, 'v2_cover', rx, 0, rw, H, focus=(0.55, 0.5))
    callout(s, at, 'garage', 'Robot Home (Dock)', -0.35, -0.55, side='l')
    callout(s, at, 'rail', 'Rail (필요 시)', 0.3, -0.55)
    callout(s, at, 'dw', '식기세척기 Interface', 0.55, 0.45)
    mt(s, W - 1.75, H - 0.4, 'CONCEPT', label='CONCEPT RENDERING', fill='FFFFFF')


# ================================================================= 02 problem
def m02(prs):
    s = start(prs, 'm02', pg(prs), '가전은 자동화됐지만, 가전 사이의 일은 아직 사람이 합니다',
              visual='상단 가전 4종 카드 (기기 안의 자동화). 중간 짙은 띠: 가전 사이에서 사람이 하는 Physical Task 10개. 하단 공식: Appliance Automation ≠ Physical Workflow Automation, 근거 숫자 4개.',
              chart='카드 4 + 작업 띠 + 핵심 숫자 4',
              note=('식기세척기, 인덕션, 냉장고, 오븐은 각자 기기 안의 일을 자동으로 합니다. 하지만 식기를 옮기고, 식세기에 넣고 꺼내고, 수납하고, 재료를 옮겨 넣고, 도구를 다루는 일은 여전히 사람이 합니다. '
                    '저희는 이 문제를 개별 가전 기능이 아니라 주방 전체 Workflow의 Physical Manipulation이 자동화되지 않은 문제로 정의합니다. '
                    '국가데이터처 가계생산 위성계정을 보면 2024년 무급 가사노동 가치는 582.4조원이고 그중 음식 준비와 청소를 포함한 가정관리가 78.9%입니다. '
                    '식사 후 정리 시간 하루 약 40분은 아직 가정이며, 30세대 시간 기록으로 확인할 계획입니다.'))
    y = mhead(s, '01  문제', '가전은 자동화됐지만, 가전 사이의 일은 아직 사람이 합니다',
              '개별 가전 기능의 자동화는 진행됐지만, 주방 Workflow 전체의 Physical Manipulation은 아직 사람 몫')
    apps = [('식기세척기', '세척 자동화'), ('인덕션', '가열 자동화'), ('냉장고', '보관 자동화'), ('오븐', '조리 일부 자동화')]
    gap = 0.22; cw = (CW - 3 * gap) / 4
    for i, (a, b) in enumerate(apps):
        cx = MX + i * (cw + gap)
        rect(s, cx, y, cw, 0.9, fill=SOFT)
        text(s, cx + 0.18, y + 0.12, cw - 0.36, 0.22, '기기 안', size=8.5, bold=True, color=GREY, check=False)
        text(s, cx + 0.18, y + 0.34, cw - 0.36, 0.32, a, size=14, bold=True)
        text(s, cx + cw - 2.0, y + 0.36, 1.82, 0.3, b, size=10.5, color=INK2, align='r')
    y2 = y + 1.12
    rect(s, MX, y2, CW, 1.3, fill=INK)
    text(s, MX + 0.25, y2 + 0.14, 6, 0.3, '가전 사이에서 사람이 하는 Physical Task', size=12, bold=True, color='FFFFFF')
    tasks = ['식기 이동', '식세기 적재', '식세기 인출', '수납', '식재료 이동', '재료 투입', '조리도구 Handling', '젓기', '뚜껑 조작', '조리 후 정리']
    xx = MX + 0.25; yy = y2 + 0.6
    for i, t in enumerate(tasks):
        wv = kit.text_w(t, 10.5, True) + 0.3
        if xx + wv > MX + CW - 0.2: xx = MX + 0.25; yy += 0.36
        rect(s, xx, yy, wv, 0.28, fill='2C3036')
        text(s, xx, yy, wv, 0.28, t, size=10.5, bold=True, color='FFFFFF' if i < 5 else 'C9CDD2', align='c', anchor='m', check=False)
        xx += wv + 0.1
    text(s, MX + CW - 4.2, y2 + 0.14, 3.95, 0.3, '앞 5개 = 첫 검증 범위 CLEAN과 직결', size=9, color='A9AEB5', align='r')
    y3 = y2 + 1.48
    text(s, MX, y3, CW, 0.48, [[('Appliance Automation  ', {'color': INK}), ('≠', {'color': ACC}), ('  Physical Workflow Automation', {'color': INK})]],
         size=21, bold=True, align='c')
    y4 = y3 + 0.72
    nw = (CW - 3 * 0.3) / 4
    items = [('582.4조원', '무급 가사노동 가치 (2024)', 'FACT'), ('78.9%', '그중 가정관리 (음식 준비 · 청소 등) 459.5조원', 'FACT'),
             ('132분', '1인당 하루 가사노동 (2024, 2019년 137분)', 'FACT'), ('약 40분', '하루 식사 후 정리 (식기 이동 · 식세기 · 수납)', 'ASSUMPTION')]
    for i, (v, lab, tg) in enumerate(items):
        knum(s, MX + i * (nw + 0.3), y4, nw, v, lab, tg, vsize=24, color=ACC if i == 3 else INK, lsize=9.5, tag_y=y4 + 0.92)
    note(s, '출처: 국가데이터처 2024 가계생산 위성계정 (2026.4, 보도 인용) [S40]. 식사 후 정리 40분은 가설 → 30세대 시간 기록 (Time-diary)으로 검증.')
    mfoot(s)


# ================================================================= 03 why kitchen
def m03(prs):
    s = start(prs, 'm03', pg(prs), '주방은 기술과 사업성을 함께 검증하기 좋은 첫 공간입니다',
              visual='2열 비교: 좌 Robot Engineering 기준 4개, 우 Business 기준 4개 (번호 + 굵은 제목 + 한 줄 근거). 하단 결론 띠.',
              chart='2열 목록 + 결론 띠',
              note=('왜 주방인지 감성이 아니라 엔지니어링과 사업성 기준으로 설명드리겠습니다. '
                    '주방 작업은 집기, 옮기기, 놓기, 넣기, 빼기 같은 적은 수의 동작이 반복되고, 싱크, 조리대, 식기세척기, 수납장처럼 작업 영역이 정해져 있습니다. '
                    '물체는 다양하지만 접시, 컵, 그릇, 수저, 뚜껑, 도구로 범위가 닫혀 있습니다. 사업 측면에서는 매일 쓰는 공간이라 가치 체감이 빠르고, 주방 리모델링이나 신축 입주라는 구매 계기가 있습니다. '
                    '다만 고객이 실제로 돈을 낼지는 별도 검증이 필요하며, 18개월 차에 300명 이상 지불의사 조사로 확인합니다.'))
    y = mhead(s, '02  왜 Kitchen인가', '주방은 기술과 사업성을 함께 검증하기 좋은 첫 공간입니다',
              '감성이나 미래 이미지가 아니라 Robot Engineering과 사업성 기준')
    cols = [('Robot Engineering 기준', [
                ('Pick · Move · Place · Insert · Remove 집중', '동작 종류가 적고 반복 → Skill Library로 묶기 쉬움'),
                ('작업영역이 정해져 있음', 'Sink · Counter · Dishwasher · Storage → Calibration 대상이 명확'),
                ('물체는 다양하지만 범위가 닫혀 있음', '접시 · 컵 · Bowl · 수저 · 뚜껑 · 집게 · 국자 → 이후 식재료'),
                ('가전 사이 이동이 반복', '식세기 · 수납장 · 조리대 사이의 Physical Movement')]),
            ('Business 기준', [
                ('높은 일일 사용빈도', '매일 식사 후 반복 → 사용 Data · 가치 체감이 빠름'),
                ('구매 계기가 있음', '주방 Remodeling · 신축 입주 때 공사와 설치를 함께 결정'),
                ('CLEAN → ASSIST → COOK', '같은 Platform에 Skill · Tool을 더해 기능 확장'),
                ('설치 이후 반복매출', 'Installed Base 기반 Care · 소모품 · Skill')])]
    cw = (CW - 0.4) / 2
    for ci, (head_, rows) in enumerate(cols):
        cx = MX + ci * (cw + 0.4)
        text(s, cx, y, cw, 0.3, head_, size=12, bold=True, color=GREY)
        hline(s, cx, y + 0.36, cw, color=INK, lw=1.0)
        for ri, (a, b) in enumerate(rows):
            ry = y + 0.5 + ri * 0.92
            text(s, cx, ry, 0.5, 0.42, f'0{ri + 1}', size=16, bold=True, color=INK)
            text(s, cx + 0.6, ry, cw - 0.6, 0.32, a, size=13, bold=True)
            text(s, cx + 0.6, ry + 0.36, cw - 0.6, 0.3, b, size=10.5, color=INK2)
            if ri < 3: hline(s, cx, ry + 0.8, cw)
    by = y + 0.5 + 4 * 0.92 + 0.08
    bar(s, MX, by, CW, 0.52, '→  주거용 Manipulation의 기술성과 고객가치를 동시에 검증할 수 있는 첫 Application', size=13)
    note(s, '[사업 가설] 주방이 첫 검증 공간으로 적합하다는 판단이며, 고객 지불의사는 별도 확인 (WTP 조사 n≥300 · 예약금 Test, M18).')
    mfoot(s)


# ================================================================= 04 limits
def m04(prs):
    s = start(prs, 'm04', pg(prs), '집마다 주방이 달라, 같은 로봇을 반복 설치하기 어렵습니다',
              visual='좌측 3×3 칩: 주방마다 달라지는 9개 변수. 우측 세로 체인: 범용 Robot 적용 시 집마다 반복되는 6단계 (Perception → Validation). 하단 근거 2개 (받은 평면 5종 · 공개 사례).',
              chart='변수 Grid + 반복 공정 체인',
              note=('가정용 로봇이 어려운 이유를 AI 성능만으로 보지 않습니다. 주방 형태, 가전 위치와 모델, 수납 위치, 조리대 치수, 물건 위치, 동선, 조명, 설치 오차가 집마다 다릅니다. '
                    '범용 로봇을 그대로 넣으면 집마다 인식, 지도 작성, 교시, 프로그래밍, Calibration, 검증을 다시 해야 하고, 이것이 설치시간과 비용, 신뢰성을 좌우합니다. '
                    '실제로 저희가 받은 평면 다섯 종만 봐도 싱크 벽 길이가 약 2.6에서 3.3미터로 다르고 세 종은 기본 배치가 들어가지 않습니다. '
                    '그렇다고 MH가 모든 주방을 표준화하겠다는 것은 아닙니다. 다음 장에서 접근 방식을 설명드리겠습니다.'))
    y = mhead(s, '03  가정용 Robot 적용의 구조적 한계', '집마다 주방이 달라, 같은 로봇을 반복 설치하기 어렵습니다',
              'Robot Intelligence 부족만이 아니라 높은 Environment Variation이 Reliability와 반복설치를 막는 구조')
    lw = 7.0
    text(s, MX, y, lw, 0.28, '주방마다 다른 것', size=11, bold=True, color=GREY)
    vars_ = [('Kitchen Geometry', 'ㅡ자 · ㄱ자 · 반도형'), ('가전 위치', '식세기 · 인덕션 배치'), ('수납 위치', '상부장 · 서랍 · 키큰장'),
             ('조리대 치수', '높이 · 깊이 · 길이'), ('가전 Model', '랙 구조 · 문 열림'), ('Object 위치', '식기 놓는 자리'),
             ('동선', '통로 폭 · 사람 위치'), ('조명', '창 · 조명 반사'), ('설치오차', '벽 · 가구 수직 · 수평')]
    gw = (lw - 2 * 0.14) / 3; gh = 0.78
    for i, (a, b) in enumerate(vars_):
        gx = MX + (i % 3) * (gw + 0.14); gy = y + 0.36 + (i // 3) * (gh + 0.12)
        rect(s, gx, gy, gw, gh, fill=SOFT)
        text(s, gx + 0.14, gy + 0.1, gw - 0.28, 0.3, a, size=12, bold=True)
        text(s, gx + 0.14, gy + 0.42, gw - 0.28, 0.28, b, size=9.5, color=INK2)
    rx = MX + lw + 0.45; rw = W - MX - rx
    text(s, rx, y, rw, 0.28, '범용 Robot 적용 시 집마다 반복', size=11, bold=True, color=GREY)
    steps = ['Perception', 'Mapping', 'Teaching', 'Programming', 'Calibration', 'Validation']
    sy = y + 0.36; sh = 0.34; sg = 0.105
    for i, st in enumerate(steps):
        yy = sy + i * (sh + sg)
        rect(s, rx, yy, rw - 0.7, sh, fill=INK)
        text(s, rx, yy, rw - 0.7, sh, st, size=11.5, bold=True, color='FFFFFF', align='c', anchor='m')
        if i < len(steps) - 1: arrow(s, rx + (rw - 0.7) / 2, yy + sh, rx + (rw - 0.7) / 2, yy + sh + sg, color=GREY, lw=1.0)
    by0 = sy; by1 = sy + 6 * (sh + sg) - sg
    bx = rx + rw - 0.6
    seg(s, bx, by0, bx, by1, color=ACC, lw=1.5)
    seg(s, bx - 0.1, by0, bx, by0, color=ACC, lw=1.5); seg(s, bx - 0.1, by1, bx, by1, color=ACC, lw=1.5)
    text(s, bx + 0.06, (by0 + by1) / 2 - 0.3, 0.5, 0.6, '집마다\n반복', size=8.5, bold=True, color=ACC, align='l', anchor='m', check=False)
    ey = y + 0.36 + 3 * (gh + 0.12) + 0.1
    rows = [[('받은 평면 5종', {'bold': True}), '싱크 벽 길이 약 2.6~3.3m · 3종은 기본 한 줄 배치 불가 · ㄱ자 · 일자 · 반도형 혼재 (재작도, 특정 단지 아님)', ttxt('DERIVED')],
            [('공개 사례', {'bold': True}), 'LG CLOiD: 팔 작업 범위 무릎 높이 이상 (보도) → 식세기 하단 랙 같은 낮은 작업점은 환경 측 보완 필요', ttxt('FACT')]]
    table(s, MX, ey, lw, None, rows, col_w=[1.35, lw - 2.35, 1.0], size=9.5, label='m04ev')
    bar(s, rx, by1 + 0.32, rw - 0.3, 0.62, 'MH는 모든 주방을 표준화하지 않습니다\n→ 로봇의 적응력 + 필요한 곳만 Interface', size=10.5, fill=SOFT, color=INK)
    note(s, '[S21] LG CLOiD 보도 · 평면 5종은 사용자 제공 도면을 치수선 기준으로 재작도한 결과 (부록 B2). 표본이 작아 평면 30개 분석으로 확대 (TARGET).')
    mfoot(s)


# ================================================================= 05 technology strategy
def m05(prs):
    s = start(prs, 'm05', pg(prs), '로봇이 적응하고, 주방은 필요한 곳만 맞춥니다',
              visual='4열 대응표: 위 회색 칩 = 변동 요인 (Object · Task · Kitchen · 반복 작업점), 아래 카드 = MH 기술 (Hand · Skill · Calibration · Interface). 하단 짙은 결론 띠.',
              chart='4열 대응 Diagram',
              note=('MH의 접근은 주방 전체를 로봇에 맞게 바꾸는 것이 아닙니다. 물체가 다양한 문제는 Adaptive Robot Hand로, 작업이 다양한 문제는 Manipulation Skill Library로, '
                    '주방마다 다른 문제는 Perception과 Calibration으로 풉니다. 그리고 매일 반복되는 작업 지점, 예를 들어 로봇이 쉬는 자리, 도구 거치대, 식기세척기 랙 같은 곳에만 최소한의 Interface를 둡니다. '
                    '환경 표준화는 목적이 아니라 신뢰성과 반복설치를 높이는 수단입니다. 이렇게 해야 같은 로봇과 같은 Skill을 여러 주방에서 반복 적용할 수 있다고 봅니다.'))
    y = mhead(s, '04  MH Robotics Technology Strategy', '로봇이 적응하고, 주방은 필요한 곳만 맞춥니다',
              'Robot Hand · Manipulation Skill · Calibration · Environment Interface를 함께 설계')
    cols = [('Object Variation', '형상 · 재질 · 젖은 표면 · 얇은 Edge', 'Adaptive Robot Hand', '파지 방식을 바꿔 다양한 식기 · 도구를 하나의 손으로'),
            ('Task Variation', '집기 · 넣기 · 꺼내기 · 열기', 'Manipulation Skill Library', 'Pick · Place · Insert · Remove · Open/Close를 재사용 단위로'),
            ('Kitchen Variation', '가전 · 수납 위치 · 설치 오차', 'Perception + Calibration', '현장에서 좌표 · 가전 · 수납 위치를 맞춰 같은 Skill 실행'),
            ('반복 작업점', 'Robot 대기 · 도구 · 식세기 랙', 'Minimal Robot-friendly Interface', 'Robot Home · Tool Dock · Appliance Interface · Vision Reference')]
    gap = 0.22; cw = (CW - 3 * gap) / 4
    for i, (k, kd, t, d) in enumerate(cols):
        cx = MX + i * (cw + gap)
        rect(s, cx, y, cw, 0.92, fill=SOFT)
        text(s, cx + 0.16, y + 0.12, cw - 0.32, 0.3, k, size=12.5, bold=True, color=INK2)
        text(s, cx + 0.16, y + 0.48, cw - 0.32, 0.3, kd, size=9.5, color=GREY)
        arrow(s, cx + cw / 2, y + 0.97, cx + cw / 2, y + 1.3, color=GREY, lw=1.5)
        rect(s, cx, y + 1.36, cw, 1.95, fill='FFFFFF', line=INK, lw=1.25)
        text(s, cx + 0.16, y + 1.52, cw - 0.32, 0.72, t, size=15, bold=True, line=1.0)
        text(s, cx + 0.16, y + 2.3, cw - 0.32, 0.9, d, size=10.5, color=INK2, line=1.05)
    by = y + 3.55
    bar(s, MX, by, CW, 0.56, '결과: 다양한 주방에서 같은 Robot Platform과 Skill을 반복 적용', size=14)
    text(s, MX, by + 0.72, CW, 0.3, [[('핵심 원칙  ', {'bold': True, 'color': INK}),
                                      ('Environment Standardization은 목적이 아니라 Reliability와 반복설치를 높이는 수단. 주방 전체 표준화는 하지 않음.', {'color': INK2})]],
         size=11)
    note(s, '모든 기술 요소는 현재 개발 전 (CONCEPT · TARGET). 검증 순서와 Gate는 16쪽 · 부록 A.')
    mfoot(s)


# ================================================================= 06 adaptive hand
def m06(prs):
    s = start(prs, 'm06', pg(prs), '핵심 Hardware: 주방 물체를 다루는 Adaptive Robot Hand',
              visual='좌측 Hand 확대 렌더 (Quick Changer · 힘/토크 센서 · Wrist Camera · 교체형 Food-contact Pad · Palm Suction 표시) + Plate · Cup · Bowl · Tool 파지 4컷. 우측 주방 물체의 어려움 · 핵심 기술 후보 · Buy vs Build Gate. 하단 Hand → 사업성 연결 띠.',
              chart='3D 콘셉트 렌더 5컷 (CONCEPT) + 연결 체인',
              note=('MH의 핵심 하드웨어는 주방 물체를 다루는 로봇손입니다. 접시는 얇은 가장자리를 집고, 컵은 바깥 벽을 감싸고, 그릇은 테두리를 집고, 국자 같은 도구는 손잡이를 쥡니다. '
                    '저희 목표는 손가락 수나 자유도 경쟁이 아니라 작업 완료율, 가격, 위생, 유지관리, 내구성입니다. 그래서 식품이 닿는 Pad와 Tip은 교체형 모듈로 만들고, 이 모듈이 소모품 매출로도 이어집니다. '
                    '다만 자체 Hand가 상용 Gripper보다 낫다는 것은 아직 증명되지 않았습니다. 6개월 차에 Robotiq 2F-85 같은 상용 Gripper를 기준선으로 30종 식기 세트에서 비교하고, '
                    '성공률, 파손, 교체 횟수, 원가에서 우위가 확인될 때만 자체 Hand를 채택합니다.'))
    y = mhead(s, '05  Adaptive Kitchen Robot Hand', '핵심 Hardware: 주방 물체를 다루는 Adaptive Robot Hand',
              '손가락 수 · 자유도 경쟁이 아닌 Task Completion · 가격 · 위생 · 유지관리 · 내구성 중심')
    hw_, hh_ = 3.95, 3.3
    rect(s, MX, y, hw_, hh_, fill=SOFT)
    at = render(s, 'hand_hero', MX, y, hw_, hh_, focus=(0.5, 0.5), zoom=0.98, bg=(244, 245, 246))
    callout(s, at, 'pad', '교체형 Food-contact Pad', 0.42, -0.02, size=7.5)
    callout(s, at, 'ft', '힘 · 토크 센서', 0.4, -0.1, size=7.5)
    callout(s, at, 'qc', 'Quick Changer', 0.45, 0.02, size=7.5)
    callout(s, at, 'cam', 'Wrist Camera', -0.3, 0.38, size=7.5, side='l')
    mt(s, MX + 0.08, y + 0.08, 'CONCEPT', fill='FFFFFF')
    tw_ = 1.5; tg = 0.1; tx0 = MX + hw_ + 0.14
    tiles = [('hand_plate', 'Plate · 가장자리 Pinch', (0.45, 0.42)), ('hand_cup', 'Cup · 외벽 감싸기', (0.62, 0.45)),
             ('hand_bowl', 'Bowl · 테두리 Pinch', (0.42, 0.52)), ('hand_tool', 'Tool · 손잡이 Power Grasp', (0.55, 0.5))]
    th_ = (hh_ - tg) / 2
    for i, (nm, lab, fc) in enumerate(tiles):
        tx = tx0 + (i % 2) * (tw_ + tg); ty = y + (i // 2) * (th_ + tg)
        rect(s, tx, ty, tw_, th_, fill=SOFT)
        render(s, nm, tx, ty, tw_, th_ - 0.3, focus=fc, zoom=1.15, bg=(244, 245, 246))
        text(s, tx + 0.06, ty + th_ - 0.29, tw_ - 0.12, 0.26, lab, size=8.5, bold=True, align='c', anchor='m', check=False)
    rx = tx0 + 2 * tw_ + tg + 0.28; rw = W - MX - rx
    text(s, rx, y, rw, 0.26, '주방 물체의 어려움', size=10.5, bold=True, color=GREY)
    text(s, rx, y + 0.28, rw, 0.62, '형상 · 크기 · 재질 (유리 · 도자기 · 금속 · Plastic) · 젖은 표면 · 미끄러짐 · 파손 위험 · 얇은 Edge · 다양한 Handle',
         size=10, color=INK, line=1.05)
    text(s, rx, y + 0.98, rw, 0.26, '핵심 기술 후보', size=10.5, bold=True, color=GREY)
    techs = ['Adaptive Grasp', 'Compliance', 'Grip Force Control', 'Slip Detection', 'Multi-contact', 'Tool Handling',
             'Replaceable Food-contact Module']
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
          '우위 확인 시에만 자체 Hand 채택 (TARGET)'], size=9, color=INK2, bullet='–', space_after=1, line=1.0)
    cy = y + hh_ + 0.22
    chain = ['Object Variation 대응', '전용 Gripper 수 ↓', '같은 End-effector 활용 ↑', 'Skill 재사용 ↑', '유지보수 단순화']
    cwid = (CW - 2.25 - 4 * 0.24) / 5
    for i, c in enumerate(chain):
        cx = MX + i * (cwid + 0.24)
        rect(s, cx, cy, cwid, 0.46, fill=SOFT)
        text(s, cx, cy, cwid, 0.46, c, size=9.5, bold=True, align='c', anchor='m')
        if i < 4: arrow(s, cx + cwid + 0.02, cy + 0.23, cx + cwid + 0.22, cy + 0.23, color=GREY, lw=1.25)
    ex = MX + 5 * cwid + 4 * 0.24 + 0.15
    rect(s, ex, cy, W - MX - ex, 0.46, fill=INK)
    text(s, ex, cy, W - MX - ex, 0.46, '+ Pad · Seal · Tip = 소모품', size=9.5, bold=True, color='FFFFFF', align='c', anchor='m')
    note(s, '렌더는 설계 검증 전 개념 형상 (CONCEPT). 식품 접촉 부품: 식품위생법 "기구" · 「기구 및 용기 · 포장의 기준 및 규격」 고무제 규격 대응 (ASSIST · COOK 단계 필수) [S42 · S48].')
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
    s = start(prs, 'm07', pg(prs), '같은 Skill을 다른 주방으로 옮기는 것이 핵심 기술입니다',
              visual='상단: Skill 실행 5단계 체인 (감지 → 파지 → 조작 → 검증 → 복구, 실패 시 복구 루프). 하단: 서로 다른 주방 3종 평면 도식 → Calibration 4요소 → 같은 CLEAN Skill Library.',
              chart='실행 체인 + Calibration 흐름도 (평면 도식 3개)',
              note=('Manipulation Skill은 단순한 소프트웨어 구독이 아니라 로봇이 할 수 있는 일을 늘리는 층입니다. 모든 Skill은 감지, 파지, 조작, 검증, 복구의 같은 구조로 실행되고, 실패를 감지하면 다시 잡거나 내려놓는 복구 동작으로 이어집니다. '
                    '핵심은 이 Skill을 다른 주방으로 옮기는 것입니다. 주방마다 가전과 수납 위치, 설치 오차가 다르기 때문에 설치 때 주방 지도를 만들고, 기준점으로 좌표를 맞추고, 가전과 수납 위치를 등록하고, 작업 파라미터를 조정합니다. '
                    '18개월 차에 구조와 가전 모델이 다른 주방 세 종에서 재배치 후 성공률 하락이 10%p 이내인지, 현장 Calibration이 4시간 안에 끝나는지 확인합니다.'))
    y = mhead(s, '06  Manipulation Skill · Calibration', '같은 Skill을 다른 주방으로 옮기는 것이 핵심 기술입니다',
              'Skill = 단순 Software 구독이 아닌 Robot Capability의 확장 Layer')
    steps = [('01', '감지', 'Object Detection'), ('02', '파지', 'Grasp · Force'), ('03', '조작', 'Move · Insert'),
             ('04', '검증', 'Success Check'), ('05', '복구', 'Recovery')]
    gap = 0.3; bw = (CW - 4 * gap) / 5; bh = 0.92
    for i, (n, a, b) in enumerate(steps):
        bx = MX + i * (bw + gap)
        rect(s, bx, y, bw, bh, fill=SOFT)
        text(s, bx + 0.14, y + 0.1, 0.5, 0.24, n, size=9, bold=True, color=GREY, check=False)
        text(s, bx + 0.14, y + 0.3, bw - 0.28, 0.32, a, size=14, bold=True)
        text(s, bx + 0.14, y + 0.62, bw - 0.28, 0.24, b, size=9.5, color=INK2)
        if i < 4: arrow(s, bx + bw + 0.03, y + bh / 2, bx + bw + gap - 0.03, y + bh / 2, color=GREY, lw=1.5)
    lx0 = MX + 3 * (bw + gap) + bw / 2; lx1 = MX + 1 * (bw + gap) + bw / 2
    seg(s, lx0, y + bh, lx0, y + bh + 0.18, color=ACC, lw=1.25, dash=True)
    seg(s, lx1, y + bh + 0.18, lx0, y + bh + 0.18, color=ACC, lw=1.25, dash=True)
    arrow(s, lx1, y + bh + 0.18, lx1, y + bh + 0.01, color=ACC, lw=1.25)
    text(s, lx1 + 0.12, y + bh + 0.22, 3.5, 0.22, '실패 감지 → 다시 잡기 · 내려놓기', size=8.5, color=ACC, check=False)
    y2 = y + bh + 0.5
    text(s, MX, y2, 6, 0.26, '다른 주방 → Calibration → 같은 Skill', size=11, bold=True, color=GREY)
    ky = y2 + 0.32; kw = 2.35; kh = 0.8
    kits = [('Kitchen A · ㅡ자 3.2m · 빌트인 식세기', 'I'), ('Kitchen B · ㄱ자 · 짧은 싱크 벽', 'L'), ('Kitchen C · Retrofit · 독립형 식세기', 'R')]
    for i, (nm, kd) in enumerate(kits):
        _kitchen_tile(s, MX, ky + i * (kh + 0.1), kw, kh, nm, kd)
    cx = MX + kw + 0.55; cw2 = 3.6
    ctop = ky; cbot = ky + 3 * kh + 0.2
    for i in range(3):
        yy = ky + i * (kh + 0.1) + kh / 2
        arrow(s, MX + kw + 0.04, yy, cx - 0.04, (ctop + cbot) / 2, color=GREY, lw=1.0)
    rect(s, cx, ctop, cw2, cbot - ctop, fill=INK)
    text(s, cx + 0.2, ctop + 0.14, cw2 - 0.4, 0.3, 'Calibration (설치 시)', size=13, bold=True, color='FFFFFF')
    items = ['Kitchen Mapping', 'Coordinate Calibration (Dock · 기준점)', 'Appliance · Storage Position Mapping', 'Task Parameter Adjustment']
    for i, it in enumerate(items):
        yy = ctop + 0.52 + i * 0.5
        rect(s, cx + 0.2, yy, cw2 - 0.4, 0.4, fill='2C3036')
        text(s, cx + 0.32, yy, cw2 - 0.6, 0.4, it, size=10.5, bold=True, color='FFFFFF', anchor='m')
    sx = cx + cw2 + 0.5; sw = W - MX - sx
    arrow(s, cx + cw2 + 0.04, (ctop + cbot) / 2, sx - 0.04, (ctop + cbot) / 2, color=GREY, lw=1.5)
    rect(s, sx, ctop, sw, cbot - ctop, fill='FFFFFF', line=INK, lw=1.25)
    text(s, sx + 0.2, ctop + 0.14, sw - 0.4, 0.3, '같은 CLEAN Skill Library', size=13, bold=True)
    for i, it in enumerate(['식기 Pick', 'Dishwasher Loading', 'Dishwasher Unloading', 'Storage Return']):
        yy = ctop + 0.52 + i * 0.5
        rect(s, sx + 0.2, yy, sw - 0.4, 0.4, fill=SOFT)
        text(s, sx + 0.32, yy, sw - 0.6, 0.4, it, size=10.5, bold=True, anchor='m')
    gy = cbot + 0.12
    text(s, MX, gy, CW, 0.3, [[('M18 검증 (TARGET)  ', {'bold': True, 'color': ACC}),
                               ('구조 · 가전 모델이 다른 주방 3종에서 재배치 후 성공률 하락 ≤ 10%p · 현장 Calibration ≤ 4시간', {'color': INK})]], size=11)
    note(s, '평면 도식은 개념 예시 (R = Robot Home, S = Sink, D = Dishwasher, 수 = 수납). 수치 목표의 근거는 부록 A1~A2 KPI 표.')
    mfoot(s)


# ================================================================= 08 system architecture
def m08(prs):
    s = start(prs, 'm08', pg(prs), 'MH Kitchen Robotics System: 다섯 개 층을 하나의 제품으로',
              visual='좌측 대표 콘셉트 렌더 (주황 = Robot Working Zone, 회색 점선 = Human Zone) + Interface 위치 표시. 우측 A~E 5개 층 카드 (Robot Module · Manipulation · Calibration · Environment Interface · Safety).',
              chart='3D 콘셉트 렌더 (CONCEPT) + 5층 Architecture',
              note=('제품은 다섯 개 층으로 구성됩니다. A는 로봇 팔, Adaptive Hand, 카메라, 힘과 안전 센서, 컨트롤러로 된 Robot Module이고 필요하면 레일과 Dock을 씁니다. '
                    'B는 물체 인식부터 파지 계획, 경로 계획, 실행, 실패 감지와 복구까지의 Manipulation Layer, C는 주방 지도와 좌표, 가전과 수납 위치를 맞추는 Calibration Layer입니다. '
                    'D는 Robot Home, 도구와 수납 Dock, 가전 Interface, 비전 기준점 같은 최소한의 환경 Interface이고, E는 사람 감지, 감속, 충돌 감지, 비상정지, 안전 복귀입니다. '
                    '그림의 주황 영역이 로봇 작업 구역, 회색 점선이 사람 구역입니다. 설치 위치와 동작 범위는 설계 개념이며 실제 도달 범위와 안전성은 검증 전입니다.'))
    y = mhead(s, '07  MH Kitchen Robotics System', 'MH Kitchen Robotics System: 다섯 개 층을 하나의 제품으로',
              'Robot Module · 실행 · Calibration · Environment Interface · Safety의 시스템 통합')
    lw = 6.55; lh = H - 0.62 - y - 0.45
    at = render(s, 'v2_after', MX, y, lw, lh, focus=(0.47, 0.5), zoom=1.08)
    callout(s, at, 'garage', 'D · Robot Home', -0.2, -0.38, size=8.5, side='l')
    callout(s, at, 'drop', 'D · Drop Zone', -0.25, 0.42, size=8.5, side='l')
    callout(s, at, 'dw', 'D · 식세기 Interface', 0.25, 0.45, size=8.5)
    callout(s, at, 'robotZone', 'E · Robot Zone', 0.35, -0.55, size=8.5)
    callout(s, at, 'humanZone', 'E · Human Zone', 0.4, 0.3, size=8.5)
    mt(s, MX + 0.08, y + 0.08, 'CONCEPT', fill='FFFFFF')
    rx = MX + lw + 0.3; rw = W - MX - rx
    L = [('A', 'Robot Module', 'Robot Arm · Adaptive Hand · Vision · Force / Safety Sensor · Controller · 필요 시 Rail / Dock'),
         ('B', 'Manipulation Layer', 'Object Detection · Grasp Planning · Motion Planning · Task Execution · Failure Detection · Recovery'),
         ('C', 'Calibration Layer', 'Kitchen Mapping · Coordinate Calibration · Appliance / Storage Position Mapping · Task Parameter'),
         ('D', 'Environment Interface', 'Robot Home · Tool Dock · Storage Dock · Appliance Interface · Vision Reference · 필요 시 Working Surface Guide'),
         ('E', 'Human-Robot Safety', 'Human Detection · Speed Control · Collision Detection · Emergency Stop · Safe Home Return')]
    ch = (lh - 4 * 0.1) / 5
    for i, (k, t, d) in enumerate(L):
        cy = y + i * (ch + 0.1)
        rect(s, rx, cy, rw, ch, fill=SOFT)
        rect(s, rx, cy, 0.42, ch, fill=INK)
        text(s, rx, cy, 0.42, ch, k, size=15, bold=True, color='FFFFFF', align='c', anchor='m')
        text(s, rx + 0.56, cy + 0.08, rw - 0.68, 0.3, t, size=12.5, bold=True)
        text(s, rx + 0.56, cy + 0.38, rw - 0.68, ch - 0.42, d, size=9.5, color=INK2, line=1.02)
    note(s, '설치 위치 · 동작범위는 설계 개념 (CONCEPT), 실제 Reach · 안전성은 검증 전. 안전 기준: ISO 10218-2:2025 감속 250mm/s 등 참고 · 가정용 IEC 63682 (2026 초안) · ISO 13482 개정 대응 [S39 · S47].')
    mfoot(s)


# ================================================================= 09 CLEAN -> ASSIST -> COOK
def m09(prs):
    s = start(prs, 'm09', pg(prs), 'CLEAN은 첫 검증 Workflow이고, 제품 범위는 주방 전체입니다',
              visual='상단 CLEAN 5단계 콘셉트 렌더 (식기 인식 → Pick → Loading → Unloading → Storage Return). 중간 CLEAN에서 검증하는 9개 기술 칩. 하단 CLEAN · ASSIST · COOK 3단계 카드 (같은 Platform + Skill · Tool 확장).',
              chart='3D 콘셉트 렌더 5컷 (CONCEPT) + 단계 카드',
              note=('첫 기술검증 Workflow는 CLEAN입니다. 사람이 식기를 조리대 한쪽에 두면, 로봇이 식기를 인식하고 집어서 식기세척기에 넣고, 세척이 끝나면 꺼내서 수납장에 돌려놓습니다. '
                    'CLEAN의 목적은 시장 가치를 식기 정리에 한정하는 것이 아니라, Adaptive Grasp부터 가전과 수납 상호작용, Calibration, 안전, 실패 복구, 반복 실행까지 Platform 전체를 처음으로 끝까지 검증하는 것입니다. '
                    '그다음 같은 로봇에 재료 이동과 투입, 젓기, 뚜껑, 도구 다루기 같은 ASSIST Skill을 더하고, 장기적으로 레시피 단위 COOK으로 갑니다. COOK은 현재 검증 결과가 아니라 장기 R&D 방향입니다.'))
    y = mhead(s, '08  첫 검증 Workflow', 'CLEAN은 첫 검증 Workflow이고, 제품 범위는 주방 전체입니다',
              '새 로봇을 단계마다 다시 만드는 것이 아니라, 같은 Platform에 Skill과 Tool을 추가')
    seq = [('v2_seq_1_detect', '① 식기 인식'), ('v2_seq_2_pick', '② Pick'), ('v2_seq_3_load', '③ Dishwasher Loading'),
           ('v2_seq_4_unload', '④ Dishwasher Unloading'), ('v2_seq_5_store', '⑤ Storage Return')]
    gap = 0.14; tw = (CW - 4 * gap) / 5; th = 1.45
    for i, (nm, lab) in enumerate(seq):
        tx = MX + i * (tw + gap)
        render(s, nm, tx, y, tw, th, focus=(0.5, 0.5), zoom=1.05)
        rect(s, tx, y + th, tw, 0.3, fill=INK if i in (2, 3) else SOFT)
        text(s, tx, y + th, tw, 0.3, lab, size=9.5, bold=True, color='FFFFFF' if i in (2, 3) else INK, align='c', anchor='m')
    mt(s, MX + 0.06, y + 0.06, 'CONCEPT', fill='FFFFFF')
    vy = y + th + 0.42
    text(s, MX, vy, 1.4, 0.28, 'CLEAN 검증', size=10, bold=True, color=GREY, anchor='m')
    xx = MX + 1.15
    for t in ['Adaptive Grasp', 'Object Recognition', 'Motion Planning', 'Appliance Interaction', 'Storage Interaction',
              'Calibration', 'Safety', 'Failure Recovery', '반복 Task Execution']:
        wv = kit.text_w(t, 8.5, True) + 0.14
        rect(s, xx, vy, wv, 0.28, fill=SOFT2)
        text(s, xx, vy, wv, 0.28, t, size=8.5, bold=True, align='c', anchor='m', check=False)
        xx += wv + 0.045
    assert xx < W - MX + 0.05, xx
    cy = vy + 0.5
    stages = [('CLEAN', '초기 · 기술검증', '식기 이동 · Dishwasher Loading / Unloading · Storage Return', INK, 'FFFFFF', None,
               '기본 Skill 4종 · 식세기 Interface · Storage Dock'),
              ('ASSIST', '중기 · 기능 확장', '재료 이동 · 재료 투입 · 젓기 · 뚜껑 조작 · Tool Handling', SOFT, INK, None,
               'ASSIST Skill Pack · 집게 · 국자 · 뚜껑 Tool'),
              ('COOK', '장기 · R&D 방향', 'Recipe Workflow · 복수 Skill 연결 · Appliance 연동 · 조리 · 조리 후 정리', 'FFFFFF', INK, 'FUTURE',
               'Recipe Skill · 가전 연동 · 식재료 Tool (식품접촉 규격)')]
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
    note(s, '같은 Robot Platform + Skill 확장 + Tool 확장. COOK과 자율조리는 현재 검증 결과가 아닌 장기 R&D 방향 (FUTURE CONCEPT).', y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 10 channels
def m10(prs):
    hr, hrt, hnb = HH('purchase_direct_Y3'), HH('retrofit_purchase_Y3'), HH('newbuild_purchase_Y3')
    kl = M['kpi_links']
    s = start(prs, 'm10', pg(prs), '제품은 하나, 설치 경로는 세 가지입니다',
              visual='상단 Integration 수준 막대 3개 (Retrofit 최소 → Remodeling 통합 → New-build 설계 반영). 아래 비교표 6행 (고객 상황 · 공사 범위 · Interface · 설치 · MH 매출 가설 · 역할). 하단 MH Core vs Partner 띠.',
              chart='Integration 수준 막대 + 3열 비교표',
              note=('제품은 하나이고 설치 경로만 세 가지입니다. 기존 주방을 그대로 쓰는 Retrofit은 호환성을 확인한 뒤 작은 Mount와 Dock, 비전 기준점만 붙이고 현장 Calibration 비중이 큽니다. '
                    'Remodeling은 주방을 바꿀 때 레일, Robot Home, 식기세척기 Interface, 수납 Dock을 함께 넣는 방식으로, 첫 검증 채널입니다. '
                    'New-build는 설계 단계에서 Mount, 전원, 통신, 도구 Dock, 가전 Interface, 서비스 접근 공간을 반영하고, 로봇은 입주 때 또는 나중에 설치합니다. '
                    '어느 경로든 MH가 맡는 것은 로봇, 손, Skill, Calibration, Interface 표준, 안전, 시운전, 품질이고, 철거와 가구, 전기, 배관 같은 일반 시공은 파트너가 맡습니다.'))
    y = mhead(s, '09  Existing / Remodeling / New-build', '제품은 하나, 설치 경로는 세 가지입니다',
              '주방 전체를 획일화하지 않고 Integration 수준만 다르게 적용')
    lab_w = 1.75; cw = (CW - lab_w) / 3
    heads = [('Existing Kitchen', 'Retrofit', 1), ('Remodeling', 'Integration', 2), ('New-build', '설계 반영', 3)]
    for i, (a, b, lv) in enumerate(heads):
        cx = MX + lab_w + i * cw
        text(s, cx + 0.1, y, cw - 0.2, 0.34, a, size=15, bold=True)
        text(s, cx + 0.1, y + 0.36, cw - 0.2, 0.24, b, size=9.5, bold=True, color=GREY)
        for j in range(3):
            rect(s, cx + 0.1 + j * 0.42, y + 0.66, 0.36, 0.12, fill=INK if j < lv else SOFT2)
        text(s, cx + 1.45, y + 0.6, cw - 1.55, 0.24, 'Integration 수준', size=8, color=GREY, check=False)
    rows = [
        ['고객 상황', '주방 유지 · 호환 주방', '주방 교체 시점 (Premium)', '분양 · 입주 전 (건설사 · 가구사)'],
        ['공사 범위', '최소 시공 (Mount · Dock)', '주방 공사와 동시 (Partner 시공)', '설계 단계에서 반영'],
        ['Interface', 'Compact Mount · Dock · Vision Reference · Drop Zone', 'Rail · Robot Home · 식세기 Interface · Storage Dock',
         'Mount · 전원 · 통신 · Tool Dock · Appliance Interface · Service Access'],
        ['설치 · Calibration', f"현장 Calibration 중심 · Y3 원가 {A('comm_cost_rt')[2]}만원 (약 {kl['inst_h_rt'][2]:.0f}인시)",
         f"Y3 원가 {A('comm_cost')[2]}만원 (약 {kl['inst_h'][2]:.0f}인시 = 2인 약 1일)", '입주 시 또는 후설치 (Option 세대)'],
        ['MH 매출 (가설)', f"Kit {A('p_rt_if')} + Robot {A('p_robot'):,} + 설치 {A('p_comm_rt')} = {hrt['y0']:,.0f}만원",
         f"Interface {A('p_rr')} + Robot {A('p_robot'):,} + 설치 {A('p_comm')} = {hr['y0']:,.0f}만원",
         f"Option {A('p_rr_new')}만원 (B2B) + 입주 Attach {A('new_attach') * 100:.0f}% × (Robot + 설치)"],
        ['역할', ('Phase 2 · 고객 확대', {'bold': True}), ('Phase 1 · 검증 채널', {'bold': True, 'color': ACC}), ('Phase 3 · Scale 채널', {'bold': True})],
    ]
    table(s, MX, y + 0.95, CW, None, rows, col_w=[lab_w, cw, cw, cw], size=10, label='m10', pad=0.07)
    by = H - 0.62 - 0.32 - 0.5
    rect(s, MX, by, CW, 0.5, fill=INK)
    text(s, MX + 0.2, by, CW - 0.4, 0.5, [[('MH Core  ', {'bold': True, 'color': 'FFFFFF'}),
                                           ('Robot · Hand · Skill · Calibration · Interface Standard · Safety · Commissioning · QA', {'color': 'E3E5E8'}),
                                           ('     Partner  ', {'bold': True, 'color': 'A9AEB5'}),
                                           ('철거 · 가구 · 전기 · 배관 · 일반 시공', {'color': 'A9AEB5'})]], size=10.5, anchor='m')
    note(s, '가격 · 원가 · 인시는 ASSUMPTION / DERIVED (VAT 별도, 주방 공사비 별도). 인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 (부록 D).', y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 11 business model
def m11(prs):
    h3, h5 = HH('purchase_direct_Y3'), HH('purchase_direct_Y5')
    st = M['steady']; pi = M['partner_irr']['B']; cons = M['cons']
    s = start(prs, 'm11', pg(prs), '설치로 시작해, 쓰는 동안 반복매출이 쌓이는 3층 구조입니다',
              visual='좌측 3층 사업모델 (INSTALL · OPERATE · EXPAND: 항목 + 가격 가설). 우측 상단 대표 1세대 5년 매출 막대 (층별) + Contribution. 우측 하단 Rental 구조 도식 (고객 · Capital Partner · MH).',
              chart='층별 가로 막대 + Rental 3자 구조도',
              note=('사업모델은 세 층입니다. INSTALL은 로봇 시스템, Interface와 Integration, 설치 매출로 초기 매출입니다. OPERATE는 Rental, Care, 소모품으로 쓰는 동안 받는 반복매출이고, '
                    'EXPAND는 ASSIST Skill, 도구, End-effector, 이후 COOK Skill과 업그레이드 같은 확장매출입니다. '
                    f"Remodeling 구매 고객 한 세대를 5년으로 보면 설치 {h3['layers']['install']:,.0f}만원, 운영 {h3['layers']['operate']:,.0f}만원, 확장 {h3['layers']['expand']:,.0f}만원이고, "
                    f"3년차 원가 기준 기여이익은 {h3['contrib5']:,.0f}만원, 5년차 원가 기준 {h5['contrib5']:,.0f}만원입니다. "
                    'Rental은 고객의 초기 부담을 낮추는 수단입니다. 초기 실증은 MH가 직접 하지만, 확장 단계에서는 렌탈이나 캐피탈 파트너가 자산을 보유하고 MH는 제품, 소프트웨어, Care를 맡아 대차대조표 부담을 줄입니다.'))
    y = mhead(s, '10  Business Model', '설치로 시작해, 쓰는 동안 반복매출이 쌓이는 3층 구조입니다',
              'INSTALL → OPERATE → EXPAND. Hardware 외 매출은 실제 유지관리와 기능가치에 근거')
    lw = 7.25
    layers = [('INSTALL', '초기 매출', [('Robot System (Arm · Adaptive Hand · Vision · Safety)', f"{A('p_robot'):,}만원"),
                                       ('Interface · Integration', f"{A('p_rt_if')}~{A('p_rr')}만원"), ('Installation · Calibration', f"{A('p_comm')}~{A('p_comm_rt')}만원")]),
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
    mts(s, MX, y + 3 * (lh + 0.14) - 0.06, ['ASSUMPTION'], label='가격 = ASSUMPTION (VAT 별도) · 실측 · WTP 검증 전')
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
    for i, (t, d) in enumerate([('고객', '월 납부'), ('Capital Partner', 'Robot 자산 보유'), ('MH', 'Product · SW · Care')]):
        bx3 = rx + i * (bw3 + 0.36)
        rect(s, bx3, byy, bw3, 0.62, fill=INK if i == 2 else SOFT)
        text(s, bx3, byy + 0.06, bw3, 0.28, t, size=10.5, bold=True, color='FFFFFF' if i == 2 else INK, align='c')
        text(s, bx3, byy + 0.33, bw3, 0.24, d, size=8.5, color='C9CDD2' if i == 2 else INK2, align='c')
        if i < 2: arrow(s, bx3 + bw3 + 0.03, byy + 0.31, bx3 + bw3 + 0.33, byy + 0.31, color=GREY, lw=1.25)
    text(s, rx, byy + 0.7, rw, 0.62, [f"월 {A('p_rent')}만원 → Partner가 Robot을 ASP의 {A('wholesale') * 100:.0f}%에 매입 · MH 서비스료 월 {A('partner_fee'):.0f}만원",
                                       f"Partner IRR 약 {pi['irr_y'] * 100:.1f}% (DERIVED) · Pilot은 MH 직접, Scale은 Partner 보유"], size=9, color=INK2, line=1.02)
    note(s, f"Care = 정기 안전점검 · Calibration · 원격진단 · SW Update · A/S (Software 구독 아님). Consumables = 실제 마모 · 위생 기반, 교체주기는 개발 중 검증. "
            f"Installed Base가 연 설치의 6배일 때 OPERATE + EXPAND 비중 약 {(st['rec_share'] + st['upg_share']) * 100:.0f}% (DERIVED). 참고 FACT: 코웨이 국내 렌탈 계정 748만 (2026 1Q) · LG 가전 구독 매출 2조원+ (2025) [S12 · S41].")
    mfoot(s)


# ================================================================= 12 market
def m12(prs):
    mk = M['market']['B']; B = M['scenarios']['B']
    s = start(prs, 'm12', pg(prs), '큰 TAM 대신, 세대 수 × 적용률 × 단가로 시작 시장을 계산합니다',
              visual='좌측 짙은 박스: 아파트 재고 1,328만호 (기회 기반) + 노후 · 거래 FACT. 우측 4개 시장 Funnel 표 (산식 · 대상 세대 · 패키지 단가 · 연 규모) + SAM 합계 · SOM.',
              chart='Bottom-up 시장 표',
              note=('시장은 큰 TAM이 아니라 세대 수, 적용률, 단가로 계산했습니다. 국내 아파트는 약 1,328만호지만 이것은 기회 기반이지 살 사람의 수가 아닙니다. '
                    f"첫 시장인 Remodeling은 해마다 주방을 바꾸는 약 30만 세대 중 Premium 10%, 구조상 적용 가능한 60%로 연 약 {mk['fit'] / 10:.1f}만 세대, 연 약 {mk['sam_remodel']:,.0f}억원입니다. "
                    f"Retrofit은 호환 가능한 기존 주방 약 {mk['retro_pool'] / 10:.1f}만 세대 중 해마다 0.5%가 전환한다고 보면 연 약 {mk['sam_retro']:,.0f}억원, 신축은 연 약 {mk['sam_new']:,.0f}억원입니다. "
                    f"5년차 계획 매출 {mk['som']:.1f}억원은 이 대상 세대의 약 {mk['som_share_hh'] * 100:.1f}%입니다. 모든 비율은 가정이며 견적 수집과 평면 분석으로 검증합니다."))
    y = mhead(s, '11  Market / Beachhead', '큰 TAM 대신, 세대 수 × 적용률 × 단가로 시작 시장을 계산합니다',
              '아파트 재고는 기회 기반이지 확정 구매시장이 아님. 비율은 모두 ASSUMPTION (검증 계획 부록 C)')
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
    text(s, MX + 0.25, y + lh - 0.62, lw - 0.5, 0.5, '기회 기반 (Stock) ≠ 구매시장. 실제 계산은 오른쪽 Funnel', size=9, color='A9AEB5', line=1.02)
    rx = MX + lw + 0.3; rw = W - MX - rx
    hdr = ['시장', '산식 (세대 × 적용률)', '대상 세대', '패키지', '연 규모']
    rows = [[('① Remodeling\nBeachhead', {'bold': True, 'color': ACC}), f"주방 교체 30만 × Premium 10% × 적용 60%", f"{mk['fit'] * 1000:,.0f}/년", f"{mk['pkg_remodel']:,.0f}만원", (f"{mk['sam_remodel']:,.0f}억원", {'bold': True})],
            [('② Retrofit', {'bold': True}), f"1,328만 × Premium 10% × 식세기 60% × 호환 40% = {mk['retro_pool'] / 10:.1f}만 (재고) × 연 0.5%", f"{mk['retro_annual'] * 1000:,.0f}/년", f"{mk['pkg_retro']:,.0f}만원", (f"{mk['sam_retro']:,.0f}억원", {'bold': True})],
            [('③ New-build', {'bold': True}), f"입주 20만 × Premium 단지 15% × Option 10%", f"{mk['new_opt'] * 1000:,.0f}/년", f"{mk['pkg_new']:,.0f}만원", (f"{mk['sam_new']:,.0f}억원", {'bold': True})],
            [('④ Recurring', {'bold': True}), f"Installed Base × 구매 고객 ARPU {mk['arpu']:.1f}만원/년 (Care · 소모품)", '1,000대당', '-', (f"{mk['recurring_per_1000']:.1f}억원", {'bold': True})]]
    th = table(s, rx, y, rw, hdr, rows, col_w=[1.35, rw - 1.35 - 1.0 - 0.95 - 1.05, 1.0, 0.95, 1.05], size=9.5,
               align=['l', 'l', 'r', 'r', 'r'], label='m12', pad=0.07)
    sy = y + th + 0.22
    sw = (rw - 0.3) / 2
    rect(s, rx, sy, sw, 1.05, fill=SOFT)
    text(s, rx + 0.2, sy + 0.12, sw - 0.4, 0.26, 'SAM 합계 (① + ② + ③)', size=10, bold=True, color=GREY)
    text(s, rx + 0.2, sy + 0.4, sw - 0.4, 0.5, f"연 {mk['sam']:,.0f}억원", size=22, bold=True)
    rect(s, rx + sw + 0.3, sy, sw, 1.05, fill='FFFFFF', line=INK, lw=1.0)
    text(s, rx + sw + 0.5, sy + 0.12, sw - 0.4, 0.26, 'SOM: Y5 매출 (Base Plan)', size=10, bold=True, color=GREY)
    text(s, rx + sw + 0.5, sy + 0.4, sw - 0.4, 0.5, f"{mk['som']:.1f}억원 · {B['kitchens'][4]:,.0f}세대", size=22, bold=True, color=ACC)
    text(s, rx + sw + 0.5, sy + 0.78, sw - 0.4, 0.24, f"대상 세대의 약 {mk['som_share_hh'] * 100:.1f}% (TARGET)", size=8.5, color=INK2, check=False)
    note(s, f"주방 교체 30만은 두 방식 교차검증 ({mk['tri1'] / 10:.1f}만 · {mk['tri2'] / 10:.1f}만) 후 설정한 가정. 참고 TAM (Premium 세대 × 전체 패키지) 연 {mk['tam'] / 10000:.1f}조원은 판단에 쓰지 않음. 출처 [S1~S6].",
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 13 GTM
def m13(prs):
    B = M['scenarios']['B']
    s = start(prs, 'm13', pg(prs), '고객의 돈과 설치비를 먼저 검증하고, 파트너로 늘립니다',
              visual='상단 3단계 카드 (Phase 1 Premium Remodeling → Phase 2 Retrofit → Phase 3 New-build). 좌하단 연도별 설치 세대 누적 막대 (채널별, TARGET). 우하단 MH Core vs Partner 역할 분담 도식.',
              chart='3단계 카드 + 누적 막대 (Y1~Y5) + 역할 분담',
              note=('처음부터 대중 시장에 들어가지 않습니다. 1단계는 Premium 주방 리모델링입니다. 여기서 제품, 가격 수용성, 설치, 사용성을 검증하고 첫 Reference와 실제 고객 데이터를 만듭니다. '
                    '2단계는 전체 리모델링 없이 붙일 수 있는 호환 주방 Retrofit이고, 3단계는 건설사와 주방가구사를 통한 신축 B2B2C로 프로젝트 단위 확장입니다. '
                    '설치 물량이 늘어도 본사 현장 인력이 같은 비율로 늘지 않도록, 철거, 가구, 전기, 배관 같은 일반 시공은 파트너에게 맡기고 MH는 로봇과 손, Skill, Calibration, 안전, 시운전에 집중합니다. '
                    '현재 파트너 계약이나 LOI는 없습니다.'))
    y = mhead(s, '12  GTM / Partner Distribution', '고객의 돈과 설치비를 먼저 검증하고, 파트너로 늘립니다',
              '초기 Mass Market 진입 없음. Premium Remodeling → 호환 주방 Retrofit → 신축 B2B2C')
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
    text(s, rx + 0.16, cy + 0.74, bw2 - 0.32, bh2 - 0.5, ['Robot · Robot Hand', 'Manipulation Skill', 'Calibration', 'Interface Standard', 'Safety · Commissioning · QA'],
         size=9.5, color='E3E5E8', line=1.0, space_after=1)
    rect(s, rx + bw2 + 0.3, cy + 0.32, bw2, bh2, fill=SOFT)
    text(s, rx + bw2 + 0.46, cy + 0.42, bw2 - 0.32, 0.28, 'Partner', size=12, bold=True)
    text(s, rx + bw2 + 0.46, cy + 0.74, bw2 - 0.32, bh2 - 0.5, ['철거 · 가구', '전기 · 배관', '일반 시공', '(신축) 건설사 · 가구사', '(Rental) 캐피탈 · 렌탈사'],
         size=9.5, color=INK2, line=1.0, space_after=1)
    text(s, rx, cy + 0.32 + bh2 + 0.1, rw, 0.42, '설치 물량 증가 ≠ 본사 현장인력 비례 증가', size=11.5, bold=True, color=ACC, anchor='m')
    note(s, '선례 (FACT, MH와 무관): 건설사 · 가전사의 구독 · 관리 번들 — LH 공공주택 5,400여 세대 · 압구정 재건축 약 7,000세대 선택지 (LG, 2026) [S41]. 현재 MH 파트너 계약 · LOI 없음.',
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 14 technology-to-economics / moat
def m14(prs):
    kl = M['kpi_links']; h3, h5 = HH('purchase_direct_Y3'), HH('purchase_direct_Y5'); sh = M['sens_household']
    s = start(prs, 'm14', pg(prs), 'R&D 성과가 설치비 · 서비스비 · 확장매출로 이어지는 구조입니다',
              visual='좌측 연결 Diagram: R&D 4개 Lever → 결과 지표 → 공통 효과 (설치시간 · Engineering 비용 ↓, 반복설치 ↑) → Installed Base → 반복 · 확장 매출. 우측 KPI ↔ 원가 표 (Y2 · Y3 · Y5) + 민감도 상위 5개 막대. 하단 Moat 정의 띠.',
              chart='연결 Diagram + 표 + Tornado 막대',
              note=('R&D가 단순 성능 향상이 아니라 Unit Economics로 연결되도록 설계했습니다. Hand가 좋아지면 다룰 수 있는 물체가 늘고, Skill이 늘면 작업 범위가 넓어지고, '
                    'Calibration이 빨라지면 새 주방에 적용하는 시간이 줄고, Interface가 맞으면 작업 신뢰성이 올라갑니다. 그 결과 설치 시간과 엔지니어링 비용이 줄고 반복 설치가 늘어 설치 기반이 커지며, Care와 소모품, Skill 매출이 쌓입니다. '
                    f"예를 들어 설치 Calibration 원가를 실증 단계 90만원에서 3년차 60만원, 5년차 38만원으로 낮추는 것이 목표이고, 이는 설치 엔지니어 약 27인시에서 12인시로 줄이는 것과 같습니다. "
                    f"한 세대 5년 기여이익에 가장 큰 영향을 주는 변수는 고객 지불의사와 로봇 BOM입니다. 방어력은 특허 하나가 아니라 Grasp 데이터, Calibration 절차와 Interface 표준, 설치 기반에서 나오며 모두 아직 구축 전입니다."))
    y = mhead(s, '13  Technology-to-Economics / Moat', 'R&D 성과가 설치비 · 서비스비 · 확장매출로 이어지는 구조입니다',
              '성능 향상 자체가 아니라 Unit Economics와 Scale 개선으로 연결')
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
    text(s, ox + 0.12, y + 0.1, ow - 0.24, 4 * rh + 0.1, ['설치시간 ↓', 'Engineering Cost ↓', '고객경험 ↑', '반복설치 ↑', '→ Installed Base ↑'],
         size=10, bold=True, color='FFFFFF', line=1.05, anchor='m', space_after=2)
    ry = y + 4 * rh + 0.45
    rect(s, MX, ry, lw, 0.46, fill=SOFT)
    text(s, MX + 0.15, ry, lw - 0.3, 0.46, [[('Installed Base → ', {'bold': True}), ('Care · Consumables · Skill Upgrade 매출 ↑', {'bold': True, 'color': ACC})]],
         size=11, anchor='m')
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y - 0.02, rw, 0.26, 'KPI ↔ 원가 연결 (Base, DERIVED)', size=10.5, bold=True, color=GREY)
    rows = [['설치 · Calibration 원가 (Remodeling)', f"{A('comm_cost')[1]}만 · {kl['inst_h'][1]:.0f}인시", f"{A('comm_cost')[2]}만 · {kl['inst_h'][2]:.0f}인시", f"{A('comm_cost')[4]}만 · {kl['inst_h'][4]:.0f}인시"],
            ['Robot System BOM', f"{kl['bom'][1]:,}만", f"{kl['bom'][2]:,}만", f"{kl['bom'][4]:,}만"],
            ['Care 원가 / 대 · 년', f"{kl['care_unit'][1]:.1f}만", f"{kl['care_unit'][2]:.1f}만", f"{kl['care_unit'][4]:.1f}만"],
            ['1세대 5년 기여이익', '-', (f"{h3['contrib5']:,.0f}만", {'bold': True}), (f"{h5['contrib5']:,.0f}만", {'bold': True, 'color': ACC})]]
    th = table(s, rx, y + 0.28, rw, ['연결 지표', 'Y2 실증', 'Y3', 'Y5'], rows, col_w=[rw - 3.15, 1.05, 1.05, 1.05], size=9.5,
               align=['l', 'r', 'r', 'r'], label='m14t', pad=0.06)
    text(s, rx, y + 0.28 + th + 0.04, rw, 0.24, f"Pad 수명 목표 ≥ 약 {kl['pad_life']:,.0f}회 파지 (분기 교체 · 하루 {kl['grasps_day']:.0f}회 가정)", size=8.5, color=INK2, check=False)
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
        rect(s, cxm, yy + 0.03, wh, 0.16, fill=ACC)
        text(s, cxm - wl - 0.5, yy, 0.46, 0.22, f'{lo:+,.0f}', size=7.5, color=INK2, align='r', anchor='m', check=False)
        text(s, cxm + wh + 0.04, yy, 0.5, 0.22, f'{hi:+,.0f}', size=7.5, color=INK2, anchor='m', check=False)
    vline(s, cxm, sy + 0.3, 5 * 0.27, color=INK)
    my = H - 0.62 - 0.3 - 0.62
    rect(s, MX, my, CW, 0.62, fill='FFFFFF', line=INK, lw=1.0)
    text(s, MX + 0.2, my, CW - 0.4, 0.62, [[('Moat = 단일 특허가 아닌 축적  ', {'bold': True}),
                                            ('① 주방 물체 Grasp Data · Skill Library  ② Calibration 절차 · Interface 표준 (설치시간)  ③ Installed Base · Care Data  ④ 출원 예정 IP', {'color': INK2}),
                                            ('   — 모두 구축 전 (TARGET)', {'color': ACC, 'bold': True})]], size=10, anchor='m')
    note(s, f"인시 = 설치 원가 ÷ 설치 엔지니어 시간당 원가 약 {kl['hour']:.1f}만원 (연 6,600만원 기준). 민감도: Remodeling 구매 1세대 · Y3 원가 · 기준 {sh['base']:,.0f}만원 (부록 D).",
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 15 IP / competition
def m15(prs):
    s = start(prs, 'm15', pg(prs), '경쟁은 이미 있습니다. 차이는 주방 적용 방식이며, 실증으로 증명합니다',
              visual='좌측 경쟁 비교표 (5개 Category + MH 목표 Position × 5개 비교 축, 공개 자료 기준). 우측 IP 후보 5개 영역 (출원 후보 · 선행기술 Risk · 우선순위). 하단 Humanoid 대응 띠.',
              chart='비교표 2개 + 결론 띠',
              note=('경쟁은 이미 있습니다. 가전사는 기기 안의 자동화와 구독, 조리 로봇은 전용 주방이나 조리대 기기, 휴머노이드와 이동형 로봇은 범용 손과 모델 학습, 협동로봇과 상용 Gripper는 부품, 주방가구사는 시공입니다. '
                    'MH의 목표 위치는 주방 물체용 손, CLEAN에서 COOK으로의 Skill 확장, Calibration과 최소 Interface, 주방 공사와 연계된 설치, Care와 소모품입니다. 이것이 더 낫다는 것은 실제 재배치 시간과 경제성으로 증명해야 합니다. '
                    '특허는 교체형 식품접촉 모듈과 가전 기준점 Calibration을 1순위로 봅니다. 식기 조작 로봇과 주방 레일 로봇 관련 선행특허가 이미 있어 넓은 청구는 어렵고, 좁고 구체적인 청구를 목표로 합니다. '
                    '휴머노이드는 위협만이 아닙니다. 공개 범용 모델은 MH의 실행층에 활용할 수 있고, MH의 Interface와 Skill은 다른 로봇에도 적용될 수 있습니다.'))
    y = mhead(s, '14  IP / Competition', '경쟁은 이미 있습니다. 차이는 주방 적용 방식이며, 실증으로 증명합니다',
              '비교는 접근 방식 설명이며 성능 우위 주장이 아님 (공개 자료 기준)')
    lw = 7.55
    hdr = ['Category', 'Object Handling', 'Task 범위', '주방 적응 · 설치', '반복매출 · 확장']
    rows = [[('Kitchen Appliance\n삼성 · LG', {'bold': True}), '기기 내부만', '세척 · 가열 · 보관', '가전 설치', '구독 · Care\n(LG 2조원+)'],
            [('Cooking Robot\nMoley · Posha', {'bold': True}), '조리 도구 · 재료', '조리 중심', '전용 주방 (£248k) · 조리대 기기 ($1,750)', '레시피 · 월 구독'],
            [('Humanoid · Mobile\n1X NEO · Figure · Sunday · LG CLOiD', {'bold': True}), '범용 손', '가사 전반 시연', '설치 불필요 · 모델 학습 중심', '구독 ($499/월) · 출시 전'],
            [('Cobot + Gripper\nUR · Doosan + Robotiq', {'bold': True}), '상용 Gripper', '산업 작업', 'Integrator 맞춤 구축', '부품 판매'],
            [('Kitchen Furniture\n한샘 · 리바트', {'bold': True}), '-', '수납 · 빌트인 가전', '주방 시공 (로봇 협업 보도 없음)', '시공 매출'],
            [('MH 목표 Position', {'bold': True, 'color': ACC}), ('Kitchen Hand\n(식기 · 도구)', {'bold': True}), ('CLEAN → ASSIST\n→ COOK', {'bold': True}),
             ('Calibration + 최소 Interface · 공사 연계', {'bold': True}), ('Care · 소모품 · Skill', {'bold': True})]]
    table(s, MX, y, lw, hdr, rows, col_w=[1.95, 1.3, 1.3, 1.6, 1.4], size=8.8, label='m15c', pad=0.055)
    rx = MX + lw + 0.3; rw = W - MX - rx
    hdr2 = ['영역', '출원 후보', '선행 Risk', '순위']
    rows2 = [[('Robot Hand', {'bold': True}), 'Replaceable Food-contact Module · Adaptive Finger · Compliance', '중~상', ('1', {'bold': True, 'color': ACC})],
             [('Calibration', {'bold': True}), 'Task Coordinate Calibration (Dock · 가전 기준점) · Kitchen Mapping', '중', ('1', {'bold': True, 'color': ACC})],
             [('Interface', {'bold': True}), 'Robot Home · Tool Dock · Appliance Interface', '상', '2'],
             [('Manipulation', {'bold': True}), '식기 Handling · Failure Recovery', '상', '2'],
             [('Safety', {'bold': True}), 'Human / Robot Zone Control', '중~상', '3']]
    th2 = table(s, rx, y, rw, hdr2, rows2, col_w=[1.05, rw - 1.05 - 0.75 - 0.5, 0.75, 0.5], size=8.8, align=['l', 'l', 'c', 'c'], label='m15ip', pad=0.055)
    text(s, rx, y + th2 + 0.06, rw, 0.62, '선행: Dishcare US 11,731,282 · Dishcraft US 10,507,584 · 주방 Rail Arm US 7,751,938 · 수납장 로봇 US 12,275,130 · Schmalz OFG. 등록 가능성 미정 · 24개월 출원 5건 + PCT 1건 목표',
         size=8.5, color=INK2, line=1.02)
    by = H - 0.62 - 0.3 - 0.66
    rect(s, MX, by, CW, 0.66, fill=INK)
    text(s, MX + 0.2, by, CW - 0.4, 0.66, [[('Humanoid는 위협만이 아님  ', {'bold': True, 'color': 'FFFFFF'}),
                                            ('공개 범용 모델 (openpi π0 · π0.5)은 MH Manipulation Layer에 활용 가능 · MH의 Interface · Skill · Calibration은 다른 Robot Platform에도 적용 · '
                                             '가격 ($20,000) · 낮은 작업점 Reach 같은 가정 설치 제약은 공간 Integration으로 보완', {'color': 'D5D8DC'})]], size=9.5, anchor='m', line=1.02)
    note(s, '공개 자료 [S19~S25 · S41 · S45 · S46 · S49~S51]. 경쟁사 성능 비교 Data 없음 → 비교 축은 접근 방식. 특허 청구항 · 권리상태는 변리사 검토 전.', y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 16 TIPS R&D / roadmap
def m16(prs):
    s = start(prs, 'm16', pg(prs), 'TIPS는 기술 위험을, Seed는 사업 위험을 줄이는 데 씁니다',
              visual='상단 좌우 비교: TIPS R&D (WP1~WP6, Technology De-risking) vs 민간 Seed (Commercial Validation). 중간 24개월 4구간 일정 (0~6 · 7~12 · 13~18 · 19~24M). 하단 Gate 4개 (M6 · M12 · M18 · M24) 판단 기준.',
              chart='2열 비교 + 4구간 로드맵 + Gate',
              note=('TIPS 자금과 민간 Seed의 역할을 나눴습니다. TIPS R&D는 기술 위험을 줄이는 데 씁니다. Adaptive Hand, Kitchen Skill, Perception과 Calibration, 최소 Interface, 안전, 통합 CLEAN 실증의 여섯 개 작업 묶음입니다. '
                    '민간 Seed는 사업 위험을 줄이는 데 씁니다. 핵심 팀, 목업 운영, 고객 검증, 실증 운영, 지불의사, 파트너 개발, 사업모델 검증입니다. '
                    '일정은 6개월 단위로 끊고 각 Gate에서 판단합니다. 6개월에는 상용 Gripper 대비 Hand 비교, 12개월에는 목업에서 CLEAN 전 과정, 18개월에는 주방 세 종 Transfer와 지불의사, 24개월에는 실제 가정 실증과 유료 전환, 원가 실측입니다.'))
    y = mhead(s, '15  TIPS R&D / 24개월 Roadmap', 'TIPS는 기술 위험을, Seed는 사업 위험을 줄이는 데 씁니다',
              'TIPS R&D = Technology De-risking · 민간 Seed = Commercial Validation (역할 중복 최소화)')
    lw = (CW - 0.3) / 2; bh = 1.32
    rect(s, MX, y, lw, bh, fill=INK)
    text(s, MX + 0.2, y + 0.1, lw - 0.4, 0.3, 'TIPS R&D  ·  Technology De-risking', size=12, bold=True, color='FFFFFF')
    wps = ['WP1 Adaptive Kitchen Robot Hand', 'WP2 Kitchen Manipulation Skill', 'WP3 Perception / Calibration',
           'WP4 Minimal Environment Interface', 'WP5 Human-Robot Safety', 'WP6 Integrated CLEAN 실증']
    for i, w_ in enumerate(wps):
        text(s, MX + 0.2 + (i % 2) * (lw / 2 - 0.1), y + 0.48 + (i // 2) * 0.27, lw / 2 - 0.2, 0.26, w_, size=9.5, color='E3E5E8', check=False)
    rx = MX + lw + 0.3
    rect(s, rx, y, lw, bh, fill=SOFT)
    text(s, rx + 0.2, y + 0.1, lw - 0.4, 0.3, '민간 Seed  ·  Commercial Validation', size=12, bold=True)
    seeds = ['Core Team (사업 · 현장 · 경영지원)', 'Prototype · Mock-up 운영', 'Customer Validation · WTP', 'Pilot 운영 · 유료 전환',
             'Partner Development', 'BM Validation · 인증 본시험 · 기관부담금']
    for i, w_ in enumerate(seeds):
        text(s, rx + 0.2 + (i % 2) * (lw / 2 - 0.1), y + 0.48 + (i // 2) * 0.27, lw / 2 - 0.2, 0.26, w_, size=9.5, color=INK2, check=False)
    gy = y + bh + 0.22
    per = [('0~6M', ['Kitchen Task 분석', 'Robot Architecture', 'Hand Prototype v1', 'Object Grasp Test (30종)', '초기 Calibration']),
           ('7~12M', ['CLEAN Skill', 'Dishwasher Interaction', 'Hand v2 · Safety', '1:1 Kitchen Mock-up', '목업 CLEAN 전 과정']),
           ('13~18M', ['다양한 Kitchen 적용', 'Task Transfer Test', 'Failure Recovery', 'Pilot 착수', 'WTP Validation']),
           ('19~24M', ['Reliability', 'Installation Standard', 'Real-home Pilot 3세대', 'BOM · 설치 · Service 원가', 'Paid Pilot · Partner 검증'])]
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
             ('M24', '가정 실증 3세대 ≥ 90% · 유료 전환 · 원가 실측')]
    for i, (g, d) in enumerate(gates):
        px = MX + i * (pw + 0.14)
        rect(s, px, ky, pw, 0.78, fill='FFFFFF', line=ACC if i == 3 else EDGE, lw=1.25 if i == 3 else 0.75)
        text(s, px + 0.12, ky + 0.06, 0.6, 0.26, g, size=11, bold=True, color=ACC)
        text(s, px + 0.12, ky + 0.32, pw - 0.24, 0.44, d, size=8.8, color=INK, line=1.0)
    mts(s, MX + CW - 0.75, ky - 0.24, ['TARGET'])
    note(s, 'TIPS 2026 일반트랙: 정부 R&D 최대 8억원 · 24개월 · 정부 75% 이내 / 기관부담 25% 이상 (FACT, 선정 미확정) [S33 · S52]. KPI 근거 · 측정 방법은 부록 A1~A3.', y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 17 founder / team
def m17(prs):
    Fd = F()
    s = start(prs, 'm17', pg(prs), '투자 판단의 첫 질문은 팀입니다. Founder 칸은 아직 비어 있습니다',
              visual='좌측 Founder 확인 항목 7행 × Founder 2인 (모두 [Founder 정보 필요]). 우측 24개월 채용 계획 표 (역할 · 시작 월 · 구분) + 인원 요약.',
              chart='확인 항목 표 + 채용 계획 표',
              note=('투자 판단의 첫 질문은 팀입니다. 현재 확인된 대표자 이력과 기술 성과는 이 자료에 쓰지 않았습니다. 왼쪽 일곱 개 항목, 즉 왜 이 문제인지, 관련 엔지니어링 경험, 하드웨어와 제품 개발, 로봇과 기계, AI 역량, '
                    '건설과 주방, 제조 지식, 고객과 파트너 네트워크, 전업 여부를 Founder 정보로 채워야 합니다. '
                    f"오른쪽은 24개월 채용 계획입니다. Founder 두 명을 포함해 24개월 차에 약 {Fd['heads_m24']:.0f}명이며, 연구개발 인력이 중심입니다. "
                    'TIPS는 대표를 포함한 창업팀 2인 이상이 지분 60% 이상을 가져야 하고, 정부지원 5억원당 청년 1명 신규 채용 요건이 있습니다.'))
    y = mhead(s, '16  Founder / Team', '투자 판단의 첫 질문은 팀입니다. Founder 칸은 아직 비어 있습니다',
              '확인되지 않은 대표자 이력 · 기술 성과는 기재하지 않음')
    lw = 6.3
    items = ['Why This Problem', 'Relevant Engineering Experience', 'Hardware / Product Development', 'Robot · Mechanical · AI Capability',
             'Construction · Kitchen · Manufacturing Knowledge', 'Customer / Partner Network', 'Full-time Commitment · 지분']
    NEED = ('[Founder 정보 필요]', {'color': ACC, 'bold': True})
    rows = [[it, NEED, NEED] for it in items]
    table(s, MX, y, lw, ['확인 항목', 'Founder 1 (대표)', 'Founder 2'], rows, col_w=[2.9, 1.7, 1.7], size=9.5, label='m17f', pad=0.075)
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
    note(s, 'TIPS 요건 (2026 공고, 원문 확인 필요): 대표 포함 창업팀 2인 이상 지분 60% 이상 · 운영사 30% 이하 · 정부지원 5억원당 청년 1명 신규 채용 [S33]. 필수 자료: 신원 · 역할 · 지분 · 고용형태 · 역량 증빙 · 특허 권리귀속.',
         y=H - 0.6 - 0.2)
    mfoot(s)


# ================================================================= 18 investment ask / value creation
def m18(prs):
    Fd = F(); TP = Fd['tips']
    s = start(prs, 'm18', pg(prs), f"24개월 {Fd['spend_total'] / 10000:.1f}억원 계획: TIPS 8억원 + Seed {Fd['seed_range'][0]}~{Fd['seed_range'][1]}억원",
              visual='좌측 24개월 사용처 표 (Spec 33 항목, 억원) + 재원 · Seed 산식. 우측 Value Creation 흐름: TODAY → Seed + TIPS → 24M TARGET (기술 · 경제성 · 시장 Evidence) → NEXT ROUND.',
              chart='사용처 표 + 4단계 흐름도',
              note=(f"투자 요청 금액은 근거 없이 정하지 않고 24개월 사용처에서 거꾸로 계산했습니다. 24개월 지출은 약 {Fd['spend_total'] / 10000:.1f}억원이고 인건비가 가장 큽니다. "
                    f"TIPS에 선정되면 정부지원 8억원이 들어오고, 나머지 지출과 Series A 협상 기간 3개월 Buffer {Fd['buffer'] / 10000:.1f}억원을 더하면 Seed 기준안은 약 {Fd['seed_base'] / 10000:.1f}억원입니다. "
                    f"팀과 목업, 실증 범위를 줄인 Lean안은 약 {Fd['seed_lean'] / 10000:.1f}억원, TIPS에 선정되지 않으면 Lean 범위로도 약 {Fd['seed_no_tips'] / 10000:.1f}억원이 필요합니다. "
                    '24개월 뒤에는 실제 주방에서 작동하는 시제품, 여러 주방 Transfer 증거, BOM과 설치, 서비스 원가 실측, 지불의사와 유료 실증, 파트너 증거, 특허 출원을 만들어 Series A를 판단받겠습니다. '
                    '후속 투자 판단 기준은 기술 성공만이 아니라 유료 전환과 원가 증거입니다.'))
    y = mhead(s, '17  Investment Ask / 24M Value Creation',
              f"24개월 {Fd['spend_total'] / 10000:.1f}억원 계획: TIPS 8억원 + Seed {Fd['seed_range'][0]}~{Fd['seed_range'][1]}억원",
              'Bottom-up 사용처 기준. Seed 범위 = Lean (팀 축소) ~ Base (기술 + 사업 검증 + 3개월 Buffer)')
    lw = 4.9
    groups = [('인건비 · 연구수당', ['인건비', '연구수당']), ('Robot HW · Hand · Mock-up', ['Robot Hardware', 'Hand Prototype', 'Kitchen Mock-up']),
              ('Software · Data', ['Software · Data']), ('Pilot · 실증 순비용', ['Pilot', '실증 순비용']), ('Customer · Partner', ['Customer · Partner']),
              ('Certification · IP', ['Certification', 'IP']), ('Space · Operating', ['Space', 'Operating']), ('예비비 (10%)', ['예비비'])]
    U = {u['cat']: u for u in Fd['uses']}
    rows = []
    for g, cats in groups:
        v = sum(sum(U[c]['y']) for c in cats); tv = sum(sum(U[c]['tips']) for c in cats)
        rows.append([g, f'{v / 10000:.2f}', f'{tv / 10000:.2f}' if tv else '-'])
    rows.append([('24개월 지출 합계', {'bold': True}), (f"{Fd['spend_total'] / 10000:.1f}", {'bold': True}), (f"{TP['total'] / 10000:.2f}", {'bold': True})])
    th = table(s, MX, y, lw, ['사용처 (억원)', '24개월', 'TIPS 편성'], rows, col_w=[lw - 1.9, 0.95, 0.95], size=9.5,
               align=['l', 'r', 'r'], label='m18u', pad=0.05)
    sy = y + th + 0.14
    srows = [['TIPS 정부지원 (선정 시)', f"{TP['gov'] / 10000:.1f}", 'FACT'],
             ['기관부담 (현금 · 현물)', f"{TP['private'] / 10000:.2f}", 'Seed 부담'],
             [('Seed Base = 지출 − TIPS + Buffer 3개월', {'bold': True}), (f"{Fd['seed_base'] / 10000:.1f}", {'bold': True, 'color': ACC}), 'DERIVED'],
             ['Seed Lean (팀 축소 · 범위 축소)', f"{Fd['seed_lean'] / 10000:.1f}", 'DERIVED'],
             ['TIPS 미선정 시 (Lean 범위)', f"{Fd['seed_no_tips'] / 10000:.1f}", 'DERIVED']]
    table(s, MX, sy, lw, None, srows, col_w=[lw - 1.9, 0.95, 0.95], size=9.5, align=['l', 'r', 'l'], label='m18s', pad=0.05)
    rx = MX + lw + 0.35; rw = W - MX - rx
    bh = H - 0.6 - 0.4 - 0.1 - 0.48 - 0.14 - y
    w1 = 1.05; w4 = 1.2; gap = 0.28; w3 = rw - w1 - w4 - 2 * gap
    rect(s, rx, y, w1, bh, fill=SOFT)
    text(s, rx + 0.12, y + 0.12, w1 - 0.24, 0.3, 'TODAY', size=12, bold=True)
    text(s, rx + 0.12, y + 0.5, w1 - 0.24, bh - 0.6, ['Concept', 'Technology Hypothesis', 'Business Hypothesis'], size=9, color=INK2, line=1.02, space_after=3)
    arrow(s, rx + w1 + 0.03, y + bh / 2, rx + w1 + gap - 0.03, y + bh / 2, color=GREY, lw=1.5)
    text(s, rx + w1 - 0.12, y + bh / 2 - 0.62, gap + 0.24, 0.55, 'Seed\n+\nTIPS', size=7.5, bold=True, color=GREY, align='c', check=False)
    x3 = rx + w1 + gap
    rect(s, x3, y, w3, bh, fill=INK)
    text(s, x3 + 0.18, y + 0.12, w3 - 0.36, 0.3, '24M TARGET', size=12, bold=True, color='FFFFFF')
    mt(s, x3 + w3 - 0.75, y + 0.14, 'TARGET', fill=INK)
    gx = x3 + 0.18; gw = (w3 - 0.36 - 0.16) / 2; gx2 = gx + gw + 0.16; yy = y + 0.5
    text(s, gx, yy, gw, 0.22, '기술', size=8.5, bold=True, color='A9AEB5', check=False)
    text(s, gx, yy + 0.24, gw, bh - 0.84, ['Working Kitchen Prototype', 'Adaptive Robot Hand', 'Skill Library', 'Calibration System',
                                           'Safety Architecture', 'Multiple Kitchen Test', 'Task Transfer Evidence'],
         size=9, color='FFFFFF', line=1.0, space_after=2)
    text(s, gx2, yy, gw, 0.22, '경제성', size=8.5, bold=True, color='A9AEB5', check=False)
    text(s, gx2, yy + 0.24, gw, 0.8, ['Robot BOM', 'Installation Cost', 'Service Cost'], size=9, color='FFFFFF', line=1.0, space_after=2)
    text(s, gx2, yy + 1.12, gw, 0.22, '시장', size=8.5, bold=True, color='A9AEB5', check=False)
    text(s, gx2, yy + 1.36, gw, bh - 1.96, ['Customer WTP', 'Pilot · Paid Pilot', 'Partner Evidence', 'Patent 출원'], size=9, color='FFFFFF',
         line=1.0, space_after=2)
    arrow(s, x3 + w3 + 0.03, y + bh / 2, x3 + w3 + gap - 0.03, y + bh / 2, color=GREY, lw=1.5)
    x4 = x3 + w3 + gap
    rect(s, x4, y, w4, bh, fill='FFFFFF', line=INK, lw=1.0)
    text(s, x4 + 0.1, y + 0.12, w4 - 0.2, 0.3, 'NEXT ROUND', size=10.5, bold=True)
    text(s, x4 + 0.12, y + 0.5, w4 - 0.24, bh - 0.6, ['Productization', 'Production', 'Distribution', 'Scale'], size=9, color=INK2, line=1.02, space_after=3)
    by = y + bh + 0.14
    rect(s, rx, by, rw, 0.48, fill=SOFT)
    text(s, rx + 0.15, by, rw - 0.3, 0.48, [[('Series A 판단 기준  ', {'bold': True}), ('기술 성공 + 유료 전환 + 설치 · 서비스 원가 실측', {'color': ACC, 'bold': True})]],
         size=11, anchor='m')
    note(s, f"Buffer = Y2 월평균 지출 × 3개월 ({Fd['buffer'] / 10000:.1f}억원). TIPS 과제 총 {TP['total'] / 10000:.2f}억원 = 정부 8억원 (75%) + 기관부담 {TP['private'] / 10000:.2f}억원 (현금 {TP['private_cash'] / 10000:.2f} · 현물 {TP['inkind'] / 10000:.2f}). "
            f"운영사 선투자 요건 (수도권 2억원 이상)은 Seed 라운드에 포함. 투자 조건 · 기업가치는 협의 (본 자료에서 제시하지 않음).", y=H - 0.6 - 0.4)
    mfoot(s)


MAIN = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, m12, m13, m14, m15, m16, m17, m18]
