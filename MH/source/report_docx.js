// Render the MH report spec (JSON from report.py) into a Word document with docx-js.
// usage: NODE_PATH=$(npm root -g) node report_docx.js <spec.json> <out.docx>
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle, HeadingLevel, LevelFormat, PageBreak, Header, Footer, PageNumber,
  VerticalAlign, TableLayoutType, TableOfContents,
} = require('docx');

const [specPath, outPath] = process.argv.slice(2);
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));

const FONT = '맑은 고딕';
const INK = '15171A', INK2 = '4A4F57', GREY = '8C9198', EDGE = 'C9CDD2', SOFT = 'F4F5F6', HEAD = 'ECEEF0', ACC = 'E2571B';
const PAGE_W = 11906, PAGE_H = 16838, MAR_LR = 1134, MAR_T = 1247, MAR_B = 1134;
const CONTENT_W = PAGE_W - 2 * MAR_LR;       // 9638 DXA
const TAGS = new Set(['FACT', 'DERIVED', 'ASSUMPTION', 'TARGET', 'CONCEPT', 'TBV', 'FUTURE']);

// ---------------------------------------------------------------- inline markup: **bold**, [[TAG]] (small grey), {{key number}} (orange)
function runs(text, o = {}) {
  const size = o.size || 21, color = o.color || INK, bold = !!o.bold;
  const out = [];
  const re = /(\*\*[^*]+\*\*|\[\[[^\]]+\]\]|\{\{[^}]+\}\})/g;
  let last = 0, m;
  const push = (t, extra = {}) => { if (t) out.push(new TextRun({ text: t, font: FONT, size, color, bold, ...extra })); };
  while ((m = re.exec(text)) !== null) {
    push(text.slice(last, m.index));
    const tok = m[0];
    if (tok.startsWith('**')) push(tok.slice(2, -2), { bold: true });
    else if (tok.startsWith('[[')) push(tok.slice(2, -2), { size: Math.max(13, size - 6), color: GREY, bold: true });
    else push(tok.slice(2, -2), { bold: true, color: ACC });
    last = m.index + tok.length;
  }
  push(text.slice(last));
  return out;
}

const thin = { style: BorderStyle.SINGLE, size: 4, color: EDGE };
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };

function cellParas(val, o) {
  return String(val ?? '').split('\n').map(line => new Paragraph({
    keepNext: !!o.keepNext,
    alignment: o.align === 'r' ? AlignmentType.RIGHT : o.align === 'c' ? AlignmentType.CENTER : AlignmentType.LEFT,
    spacing: { before: 0, after: 0, line: 252 },
    children: TAGS.has(line.trim())
      ? [new TextRun({ text: line.trim(), font: FONT, size: Math.max(13, o.size - 4), bold: true, color: GREY })]
      : runs(line, { size: o.size, bold: o.bold, color: INK }),
  }));
}

function table(b) {
  const n = b.widths.length;
  const tw = Math.round(CONTENT_W * (b.width_pct || 100) / 100);
  const ws = b.widths.map(p => Math.floor(tw * p / 100));
  ws[n - 1] += tw - ws.reduce((a, c) => a + c, 0);
  const size = b.size || 17;
  const align = b.align || Array(n).fill('l');
  const nRows = (b.rows || []).length;
  const keep = b.keep ?? nRows <= 8;
  const mk = (cells, isHead, rowBold, keepRow) => new TableRow({
    tableHeader: isHead,
    cantSplit: true,
    children: cells.map((v, i) => new TableCell({
      width: { size: ws[i], type: WidthType.DXA },
      shading: isHead ? { fill: HEAD, type: ShadingType.CLEAR, color: 'auto' }
        : (rowBold ? { fill: 'F7F8F9', type: ShadingType.CLEAR, color: 'auto' }
          : (b.fill_first && i === 0 ? { fill: SOFT, type: ShadingType.CLEAR, color: 'auto' } : undefined)),
      margins: { top: 45, bottom: 45, left: 85, right: 85 },
      verticalAlign: VerticalAlign.CENTER,
      borders: { top: thin, bottom: thin, left: none, right: none },
      children: cellParas(v, { size, align: isHead ? 'c' : align[i], bold: isHead || rowBold || (b.bold_first && i === 0), keepNext: keepRow }),
    })),
  });
  const rows = [];
  if (b.header) rows.push(mk(b.header, true, false, true));
  (b.rows || []).forEach((r, ri) => rows.push(mk(r, false, (b.bold_rows || []).includes(ri), keep && ri < nRows - 1)));
  return new Table({ width: { size: tw, type: WidthType.DXA }, columnWidths: ws, layout: TableLayoutType.FIXED,
                     alignment: AlignmentType.CENTER, rows });
}

function caption(text) {
  return new Paragraph({ spacing: { before: 180, after: 60 }, keepNext: true, keepLines: true, children: runs(text, { size: 19, bold: true }) });
}
function note(text) {
  return new Paragraph({ spacing: { before: 40, after: 140 }, children: runs(text, { size: 16, color: GREY }) });
}

function box(b) {
  const children = [];
  if (b.title) children.push(new Paragraph({ spacing: { before: 0, after: 80 }, children: runs(b.title, { size: 21, bold: true }) }));
  (b.items || []).forEach(it => children.push(new Paragraph({
    numbering: { reference: 'gaejo', level: it.lv ?? 1 }, spacing: { before: it.lv === 0 ? 40 : 0, after: 40, line: 300 },
    children: runs(it.text, { size: 20, bold: it.lv === 0 }),
  })));
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W], layout: TableLayoutType.FIXED,
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { fill: SOFT, type: ShadingType.CLEAR, color: 'auto' },
      margins: { top: 140, bottom: 120, left: 220, right: 220 },
      borders: { top: none, bottom: none, right: none, left: { style: BorderStyle.SINGLE, size: 24, color: INK } },
      children,
    })] })],
  });
}

function tiles(b) {
  const n = b.items.length, gap = 120;
  const w = Math.floor((CONTENT_W - gap * (n - 1)) / n);
  const cells = [], ws = [];
  b.items.forEach((it, i) => {
    if (i) { ws.push(gap); cells.push(new TableCell({ width: { size: gap, type: WidthType.DXA }, borders: { top: none, bottom: none, left: none, right: none }, children: [new Paragraph({ children: [] })] })); }
    ws.push(w);
    cells.push(new TableCell({
      width: { size: w, type: WidthType.DXA },
      shading: { fill: SOFT, type: ShadingType.CLEAR, color: 'auto' },
      margins: { top: 140, bottom: 130, left: 160, right: 120 },
      borders: { top: { style: BorderStyle.SINGLE, size: 12, color: it.accent ? ACC : INK }, bottom: none, left: none, right: none },
      children: [
        new Paragraph({ spacing: { before: 0, after: 40 }, children: [new TextRun({ text: it.value, font: FONT, size: 30, bold: true, color: it.accent ? ACC : INK })] }),
        new Paragraph({ spacing: { before: 0, after: 0, line: 250 }, children: [new TextRun({ text: it.label, font: FONT, size: 16, color: INK2 })] }),
      ],
    }));
  });
  ws[ws.length - 1] += CONTENT_W - ws.reduce((a, c) => a + c, 0);
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: ws, layout: TableLayoutType.FIXED,
                     rows: [new TableRow({ cantSplit: true, children: cells })] });
}

function figure(b) {
  const maxW = CONTENT_W / 1440 * 96 * (b.w_pct || 100) / 100;   // px at 96 dpi
  const w = Math.round(maxW), h = Math.round(maxW * b.h_px / b.w_px);
  const ext = path.extname(b.path).toLowerCase() === '.png' ? 'png' : 'jpg';
  const out = [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 140, after: 50 }, keepNext: true,
      children: [new ImageRun({ type: ext, data: fs.readFileSync(b.path), transformation: { width: w, height: h },
                                altText: { title: b.caption || 'figure', description: b.caption || 'figure', name: 'fig' } })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: b.note ? 20 : 180 }, keepNext: !!b.note,
                    children: runs(b.caption || '', { size: 18, color: INK2 }) }),
  ];
  if (b.note) out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 180 }, children: runs(b.note, { size: 16, color: GREY }) }));
  return out;
}

// ---------------------------------------------------------------- blocks -> docx children
const body = [];
let firstH1 = true;
spec.blocks.forEach((b, idx) => {
  const nextIsPage = (spec.blocks[idx + 1] || {}).t === 'h1';
  switch (b.t) {
    case 'cover': {
      body.push(new Paragraph({ spacing: { before: 600, after: 120 }, children: [new TextRun({ text: b.kicker, font: FONT, size: 22, bold: true, color: GREY })] }));
      body.push(new Paragraph({ spacing: { before: 0, after: 100 }, children: [new TextRun({ text: b.title, font: FONT, size: 44, bold: true, color: INK })] }));
      body.push(new Paragraph({ spacing: { before: 0, after: 300 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: INK, space: 8 } },
                                children: [new TextRun({ text: b.subtitle, font: FONT, size: 32, bold: true, color: INK2 })] }));
      if (b.image) body.push(...figure({ path: b.image.path, w_px: b.image.w_px, h_px: b.image.h_px, w_pct: b.image.w_pct || 86, caption: b.image.caption }));
      (b.lines || []).forEach((l, i) => body.push(new Paragraph({ spacing: { before: i ? 40 : 200, after: 40 }, children: runs(l, { size: i ? 20 : 24, bold: !i, color: i ? INK2 : INK }) })));
      body.push(new Paragraph({ children: [new PageBreak()] }));
      break;
    }
    case 'toc': {
      body.push(new Paragraph({ spacing: { before: 0, after: 240 }, children: [new TextRun({ text: '목 차', font: FONT, size: 32, bold: true, color: INK })] }));
      body.push(new TableOfContents('목차', {
        hyperlink: true, headingStyleRange: '1-2',
        cachedEntries: (b.entries || []).map(e => ({ title: e.title, level: e.level, page: e.page ? String(e.page) : '' })),
      }));
      body.push(new Paragraph({ children: [new PageBreak()] }));
      break;
    }
    case 'h1':
      body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: !firstH1 && b.newpage !== false, keepNext: true,
        border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: INK, space: 6 } }, spacing: { before: 0, after: 240 },
        children: [new TextRun({ text: b.text, font: FONT, size: 32, bold: true, color: INK })] }));
      firstH1 = false;
      break;
    case 'h2':
      body.push(new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, keepLines: true, spacing: { before: 320, after: 120 },
        children: [new TextRun({ text: b.text, font: FONT, size: 26, bold: true, color: INK })] }));
      break;
    case 'h3':
      body.push(new Paragraph({ heading: HeadingLevel.HEADING_3, keepNext: true, keepLines: true, spacing: { before: 220, after: 80 },
        children: [new TextRun({ text: b.text, font: FONT, size: 22, bold: true, color: INK2 })] }));
      break;
    case 'b':
      body.push(new Paragraph({ numbering: { reference: 'gaejo', level: b.lv || 0 }, keepNext: !!b.keep,
        spacing: { before: (b.lv || 0) === 0 ? 110 : 20, after: 30, line: 312 },
        children: runs(b.text, { size: (b.lv || 0) === 0 ? 21 : 20, bold: (b.lv || 0) === 0 && b.bold !== false }) }));
      break;
    case 'p':
      body.push(new Paragraph({ spacing: { before: 60, after: 60, line: 312 }, children: runs(b.text, { size: 20 }) }));
      break;
    case 'table':
      if (b.caption) body.push(caption(b.caption));
      body.push(table(b));
      if (b.note) body.push(note(b.note)); else if (!nextIsPage) body.push(new Paragraph({ spacing: { before: 0, after: 120 }, children: [] }));
      break;
    case 'fig':
      body.push(...figure(b));
      break;
    case 'box':
      body.push(new Paragraph({ spacing: { before: 120, after: 0 }, children: [] }));
      body.push(box(b));
      if (!nextIsPage) body.push(new Paragraph({ spacing: { before: 0, after: 140 }, children: [] }));
      break;
    case 'tiles':
      body.push(new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }));
      body.push(tiles(b));
      body.push(new Paragraph({ spacing: { before: 0, after: 100 }, children: [] }));
      break;
    case 'pb':
      body.push(new Paragraph({ children: [new PageBreak()] }));
      break;
    default:
      throw new Error('unknown block ' + b.t);
  }
});

const doc = new Document({
  creator: 'MH Robotics', title: spec.title, description: spec.subject,
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: FONT, size: 21, color: INK } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 32, bold: true }, paragraph: { outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 26, bold: true }, paragraph: { outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 22, bold: true }, paragraph: { outlineLevel: 2 } },
      { id: 'TOC1', name: 'toc 1', basedOn: 'Normal', next: 'Normal', run: { font: FONT, size: 21, bold: true, color: INK }, paragraph: { spacing: { before: 150, after: 30 } } },
      { id: 'TOC2', name: 'toc 2', basedOn: 'Normal', next: 'Normal', run: { font: FONT, size: 19, color: INK2 }, paragraph: { indent: { left: 400 }, spacing: { before: 0, after: 20 } } },
    ],
  },
  numbering: { config: [{ reference: 'gaejo', levels: [
    { level: 0, format: LevelFormat.BULLET, text: '□', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 360 } }, run: { font: FONT } } },
    { level: 1, format: LevelFormat.BULLET, text: '○', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 760, hanging: 340 } }, run: { font: FONT } } },
    { level: 2, format: LevelFormat.BULLET, text: '-', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1120, hanging: 280 } }, run: { font: FONT } } },
    { level: 3, format: LevelFormat.BULLET, text: '·', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1440, hanging: 240 } }, run: { font: FONT } } },
  ] }] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MAR_T, bottom: MAR_B, left: MAR_LR, right: MAR_LR, header: 600, footer: 500 } },
                  titlePage: true },
    headers: {
      default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: spec.header, font: FONT, size: 16, color: GREY })] })] }),
      first: new Header({ children: [new Paragraph({ children: [] })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: ['- ', PageNumber.CURRENT, ' -'], font: FONT, size: 18, color: INK2 })] })] }),
      first: new Footer({ children: [new Paragraph({ children: [] })] }),
    },
    children: body,
  }],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(outPath, buf); console.log('wrote', outPath, buf.length, 'bytes'); });
