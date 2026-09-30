#!/usr/bin/env python3
"""Valida y sincroniza las páginas del sitio contra el estándar de guías.

Uso (desde la raíz del repo):
  python3 .claude/skills/guia-arquitectura/scripts/check_guide.py check [web/x.html ...]
  python3 .claude/skills/guia-arquitectura/scripts/check_guide.py sync web/x.html [...]

check  sin archivos revisa todas las guías de web/ (todo .html salvo index.html y
       tomasulo.html), el chrome de tomasulo.html y los enlaces del home.
sync   reemplaza los bloques STD:* de la página por los del template (la página
       tiene que tener ya los marcadores; si no, primero hay que migrarla a mano).

Sale con código 1 si hay algún ERROR. Los AVISO no bloquean.
Solo usa la biblioteca estándar.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "assets" / "guide-template.html"
TITLE_SUFFIX = " | Computer Architecture Lab"
APP_PAGES = {"tomasulo.html"}  # apps con bundle de Vite: solo se valida el chrome
HOME = "index.html"

# (nombre, marcador de apertura, marcador de cierre)
BLOCKS = [
    ("STD:TOKENS", "/* ==== STD:TOKENS", "/* ==== /STD:TOKENS ==== */"),
    ("STD:SHELL", "/* ==== STD:SHELL", "/* ==== /STD:SHELL ==== */"),
    ("STD:COMPONENTS", "/* ==== STD:COMPONENTS", "/* ==== /STD:COMPONENTS ==== */"),
    ("STD:SCRIPT", "/* ==== STD:SCRIPT", "/* ==== /STD:SCRIPT ==== */"),
]

TUTEO = re.compile(
    r"\b(Prueba|Pulsa|Haz|Mira|Elige|Fíjate|Cambia al|Sube el|Baja el|puedes|tienes|quieres|verás|Recuerda)\b"
)


def find_repo_root():
    for base in [Path.cwd(), *Path.cwd().parents, SKILL_DIR, *SKILL_DIR.parents]:
        if (base / "web" / "vite.config.ts").exists():
            return base
    sys.exit("No se encuentra web/vite.config.ts: correr el script desde el repo.")


def rel(path, root):
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def extract_block(text, start, end):
    i = text.find(start)
    if i < 0:
        return None
    j = text.find(end, i)
    if j < 0:
        return None
    return i, j + len(end)


def norm(s):
    return "\n".join(line.rstrip() for line in s.strip().splitlines())


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.stack = []
        self.title = ""
        self._in_title = False
        self.backlink = False
        self.toggle = False
        self.skip = False
        self.sidenav = False
        self.main = False
        self.nav_links = []
        self.sections = []  # dicts: id, has_h2, has_num
        self._section = None
        self._h2 = False
        self._in_nav = 0
        self.external = []
        self.onclick = 0
        self.inline_colors = 0
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if tag not in ("br", "img", "input", "meta", "link", "hr", "source"):
            self.stack.append(tag)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "title":
            self._in_title = True
        if tag == "a" and "backlink" in cls and a.get("href") == "index.html":
            self.backlink = True
        if tag == "a" and "skip-link" in cls:
            self.skip = True
        if a.get("id") == "theme-toggle":
            self.toggle = True
        if a.get("id") == "main":
            self.main = True
        if tag == "nav" and "side" in cls and a.get("id") == "sidenav":
            self.sidenav = True
            self._in_nav = len(self.stack)
        if tag == "a" and self._in_nav and (a.get("href") or "").startswith("#"):
            self.nav_links.append(a["href"][1:])
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])
        if tag == "section" and "block" in cls:
            self._section = {"id": a.get("id") or "", "has_h2": False, "has_num": False, "depth": len(self.stack)}
            self.sections.append(self._section)
        if tag == "h2" and self._section is not None:
            self._section["has_h2"] = True
            self._h2 = True
        if tag == "span" and self._h2 and "num" in cls:
            self._section["has_num"] = True
        if tag in ("link", "script", "img", "iframe"):
            src = a.get("href") or a.get("src") or ""
            if re.match(r"(https?:)?//", src):
                self.external.append(f"<{tag}> {src}")
        if "onclick" in a:
            self.onclick += 1
        if re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(\s*\d", a.get("style") or ""):
            self.inline_colors += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "h2":
            self._h2 = False
        if tag == "nav" and self._in_nav and len(self.stack) == self._in_nav:
            self._in_nav = 0
        if tag == "section" and self._section is not None and len(self.stack) == self._section["depth"]:
            self._section = None
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def scan(text):
    s = Scan()
    s.feed(text)
    return s


class Report:
    def __init__(self, name):
        self.name = name
        self.errors = []
        self.warns = []

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warns.append(msg)

    def show(self):
        status = "OK" if not self.errors else "FALLA"
        print(f"\n== {self.name}: {status} ({len(self.errors)} errores, {len(self.warns)} avisos)")
        for m in self.errors:
            print(f"  ERROR  {m}")
        for m in self.warns:
            print(f"  AVISO  {m}")


def check_chrome(r, s, text):
    if not s.title.strip().endswith(TITLE_SUFFIX.strip()):
        r.err(f"el <title> tiene que terminar en '{TITLE_SUFFIX.strip()}' (hoy: '{s.title.strip()}')")
    if not s.backlink:
        r.err('falta <a class="backlink" href="index.html">&larr; Inicio</a> en el header')
    if not s.toggle:
        r.err("falta el botón #theme-toggle")
    if not s.skip:
        r.err('falta el skip-link (<a class="skip-link" href="#main">)')
    if not s.main:
        r.err("falta <main id=\"main\">")
    if "localStorage.getItem('tw-theme')" not in text:
        r.err("falta el script de <head> que aplica el tema guardado (tw-theme) antes del render")
    if 'class="kicker"' not in text:
        r.err('falta <p class="kicker">Arquitectura de Computadoras — …</p> en el header')
    for e in s.external:
        r.err(f"recurso externo (las páginas son autocontenidas): {e}")
    if "fonts.googleapis" in text or re.search(r"@import\s+url\(\s*['\"]?https?:", text):
        r.err("fuentes o CSS externos: hay que sacarlos")
    dups = sorted({i for i in s.ids if s.ids.count(i) > 1})
    if dups:
        r.err(f"ids duplicados: {', '.join(dups)}")


def check_guide(root, path, tpl):
    text = path.read_text(encoding="utf-8")
    r = Report(rel(path, root))
    s = scan(text)
    check_chrome(r, s, text)

    for name, start, end in BLOCKS:
        span = extract_block(text, start, end)
        tspan = extract_block(tpl, start, end)
        if span is None:
            r.err(f"falta el bloque {name} (copiarlo del template o migrar la página)")
        elif norm(text[span[0]:span[1]]) != norm(tpl[tspan[0]:tspan[1]]):
            r.err(f"el bloque {name} difiere del template: correr `check_guide.py sync {rel(path, root)}`")
    if "/* ==== PAGE" not in text:
        r.warn("no hay marcador /* ==== PAGE ==== */ para el CSS/JS propio de la página")

    if not s.sidenav:
        r.err('falta <nav class="side" id="sidenav">')
    ids = set(s.ids)
    for h in s.nav_links:
        if h not in ids:
            r.err(f"el nav apunta a #{h}, que no existe")
    for sec in s.sections:
        sid = sec["id"]
        if not sid.startswith("s-"):
            r.err(f"section.block sin id 's-<slug>' (id='{sid}')")
        if not (sec["has_h2"] and sec["has_num"]):
            r.err(f"#{sid}: el <h2> tiene que llevar <span class=\"num\">…</span>")
        if sid and sid not in s.nav_links:
            r.warn(f"#{sid} no aparece en el nav lateral")
    if not s.sections:
        r.err("no hay ninguna <section class=\"block\">")

    left = sorted(set(re.findall(r"\{\{[^}]*\}\}", text)))
    if left:
        r.err(f"quedan placeholders del template sin completar: {', '.join(left[:5])}")
    check_colors(r, text)
    if s.onclick:
        r.warn(f"{s.onclick} handlers onclick inline (lo nuevo va con addEventListener dentro de un IIFE)")
    if s.inline_colors:
        r.warn(f"{s.inline_colors} atributos style= con colores literales (usar var(--token))")
    hits = sorted(set(TUTEO.findall(strip_code(text))))
    if hits:
        r.warn(f"posible tuteo (el sitio usa voseo): {', '.join(hits)}")

    check_registration(root, r, path.name, set(s.ids), [h for h in s.nav_links if h in {x['id'] for x in s.sections}])
    return r


def strip_code(text):
    text = re.sub(r"<style>.*?</style>", "", text, flags=re.S)
    return re.sub(r"<script>.*?</script>", "", text, flags=re.S)


def check_colors(r, text):
    """Colores literales en el CSS fuera de los bloques de tokens: no siguen el toggle de tema."""
    css = "".join(re.findall(r"<style>(.*?)</style>", text, flags=re.S))
    for start, end in [BLOCKS[0][1:], ("/* ==== PAGE:TOKENS", "/* ==== PAGE ====")]:
        span = extract_block(css, start, end)
        if span:
            css = css[:span[0]] + css[span[1]:]
    count = 0
    for line in css.splitlines():
        if re.match(r"\s*--[\w-]+\s*:", line):
            continue  # definición de token (p. ej. en un bloque de tokens heredado)
        if re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(\s*\d", line):
            count += 1
    if count:
        r.warn(f"{count} líneas de CSS con colores literales fuera de los tokens (revisar en modo claro y oscuro)")


def check_registration(root, r, page, page_ids, section_links):
    """section_links: entradas del nav que apuntan a una section.block (no a sub-anclas h3)."""
    vite = (root / "web" / "vite.config.ts").read_text(encoding="utf-8")
    if f"'{page}'" not in vite and f'"{page}"' not in vite:
        r.err(f"{page} no está en rollupOptions.input de web/vite.config.ts (no se despliega)")
    home = (root / "web" / HOME).read_text(encoding="utf-8")
    links = re.findall(r'href="' + re.escape(page) + r'(?:#([\w-]+))?"', home)
    if not links:
        r.err(f"el home ({HOME}) no tiene ninguna tarjeta que enlace a {page}")
        return
    anchors = {a for a in links if a}
    for a in sorted(anchors):
        if a not in page_ids:
            r.err(f"el home enlaza {page}#{a}, que no existe en la página")
    missing = [h for h in section_links if h not in anchors]
    if missing:
        r.warn(f"secciones del nav sin enlace en la tarjeta del home: {', '.join('#' + m for m in missing)}")


def check_app(root, path):
    text = path.read_text(encoding="utf-8")
    r = Report(rel(path, root) + " (app: solo chrome)")
    check_chrome(r, scan(text), text)
    home = (root / "web" / HOME).read_text(encoding="utf-8")
    if f'href="{path.name}' not in home:
        r.err(f"el home no enlaza {path.name}")
    return r


def check_home(root):
    path = root / "web" / HOME
    text = path.read_text(encoding="utf-8")
    r = Report(f"web/{HOME} (home)")
    s = scan(text)
    if not s.toggle:
        r.err("falta el botón #theme-toggle")
    if not s.title.strip().endswith("Computer Architecture Lab"):
        r.err("el <title> del home tiene que ser/terminar en 'Computer Architecture Lab'")
    for href in s.hrefs:
        m = re.match(r"([\w-]+\.html)(?:#([\w-]+))?$", href)
        if not m:
            continue
        target = root / "web" / m.group(1)
        if not target.exists():
            r.err(f"enlace roto: {href}")
        elif m.group(2) and f'id="{m.group(2)}"' not in target.read_text(encoding="utf-8"):
            r.err(f"ancla inexistente: {href}")
    return r


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("check", "sync"):
        print(__doc__)
        sys.exit(2)
    root = find_repo_root()
    tpl = TEMPLATE.read_text(encoding="utf-8")
    files = [Path(f).resolve() for f in sys.argv[2:]]
    for f in files:
        if not f.exists():
            sys.exit(f"No existe: {f}")

    if sys.argv[1] == "sync":
        if not files:
            sys.exit("sync necesita al menos un archivo")
        for f in files:
            text = f.read_text(encoding="utf-8")
            for name, start, end in BLOCKS:
                span, tspan = extract_block(text, start, end), extract_block(tpl, start, end)
                if span is None:
                    sys.exit(f"{f.name}: no tiene el bloque {name}; hay que migrarla primero (ver references/standard.md)")
                text = text[:span[0]] + tpl[tspan[0]:tspan[1]] + text[span[1]:]
            f.write_text(text, encoding="utf-8")
            print(f"sincronizado: {rel(f, root)}")
        return

    web = root / "web"
    if not files:
        files = sorted(p for p in web.glob("*.html") if p.name != HOME)
        reports = [check_home(root)]
    else:
        reports = []
    for f in files:
        if f.name == HOME:
            reports.append(check_home(root))
        elif f.name in APP_PAGES:
            reports.append(check_app(root, f))
        else:
            reports.append(check_guide(root, f, tpl))
    for r in reports:
        r.show()
    sys.exit(1 if any(r.errors for r in reports) else 0)


if __name__ == "__main__":
    main()
