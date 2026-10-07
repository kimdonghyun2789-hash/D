# PPTX -> PDF preview without LibreOffice's Asian/Latin auto-spacing.
# LibreOffice inserts extra space between Hangul and Latin letters/punctuation ("Hand 가", "자동화 ,"),
# which PowerPoint does not. We round-trip through ODP and switch that paragraph property off.
import os, re, sys, shutil, subprocess, tempfile, zipfile
try:  # sandbox helper (adds a socket shim where AF_UNIX is blocked); optional
    sys.path.insert(0, os.environ.get('SOFFICE_HELPER_DIR', ''))
    from soffice import run_soffice
except Exception:
    def run_soffice(args, **kw):
        prof = tempfile.mkdtemp(prefix='lo_profile_')
        try:
            return subprocess.run(['soffice', f'-env:UserInstallation=file://{prof}'] + list(args), **kw)
        finally:
            shutil.rmtree(prof, ignore_errors=True)


def _fix_xml(x):
    x = x.replace('style:text-autospace="ideograph-alpha"', 'style:text-autospace="none"')
    # add the attribute to paragraph-properties that lack it
    x = re.sub(r'<style:paragraph-properties(?![^>]*text-autospace)', '<style:paragraph-properties style:text-autospace="none"', x)
    # default styles without paragraph-properties get one
    def add_pp(m):
        blk = m.group(0)
        if '<style:paragraph-properties' in blk: return blk
        if blk.endswith('/>'):
            return blk[:-2] + '><style:paragraph-properties style:text-autospace="none"/></style:default-style>'
        return blk.replace('>', '><style:paragraph-properties style:text-autospace="none"/>', 1)
    x = re.sub(r'<style:default-style[^>]*/>|<style:default-style[^>]*>.*?</style:default-style>', add_pp, x, flags=re.S)
    return x


def convert(pptx, pdf_out):
    tmp = tempfile.mkdtemp(prefix='topdf_', dir=os.path.dirname(os.path.abspath(pdf_out)))
    try:
        base = os.path.splitext(os.path.basename(pptx))[0]
        run_soffice(['--headless', '--convert-to', 'odp', '--outdir', tmp, os.path.abspath(pptx)], capture_output=True, timeout=900)
        odp = os.path.join(tmp, base + '.odp')
        fixed = os.path.join(tmp, base + '_fixed.odp')
        with zipfile.ZipFile(odp) as zin, zipfile.ZipFile(fixed, 'w') as zout:
            names = zin.namelist()
            zout.writestr(zipfile.ZipInfo('mimetype'), zin.read('mimetype'), compress_type=zipfile.ZIP_STORED)
            for n in names:
                if n == 'mimetype': continue
                data = zin.read(n)
                if n.split('/')[-1] in ('content.xml', 'styles.xml'):
                    data = _fix_xml(data.decode('utf-8')).encode('utf-8')
                zout.writestr(n, data, compress_type=zipfile.ZIP_DEFLATED)
        run_soffice(['--headless', '--convert-to', 'pdf', '--outdir', tmp, fixed], capture_output=True, timeout=900)
        shutil.move(os.path.join(tmp, base + '_fixed.pdf'), pdf_out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return pdf_out


if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2])
    print('pdf', sys.argv[2])
