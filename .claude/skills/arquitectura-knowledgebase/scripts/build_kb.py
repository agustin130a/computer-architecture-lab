"""Arma la knowledge base: un .md por unidad + index.md, a partir de pdftotext -layout y el TOC."""
import json, re, sys, unicodedata, os

SP, OUT = sys.argv[1], sys.argv[2]
pages = open(f"{SP}/all.txt", encoding="utf-8").read().split("\f")
toc = json.load(open(f"{SP}/toc.json"))

NOISE = re.compile(r"^\s*(UNC - FCEFyN - IComp.*|Cabrera, Augusto Gabriel.*|Apuntes NO oficiales de la c.tedra|\d{1,3})\s*$")

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", s)

def clean(lines):
    out, blank = [], 0
    for l in lines:
        l = l.rstrip()
        if NOISE.match(l):
            continue
        if not l.strip():
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(l)
    return out

# cada página como lista de líneas limpias
P = {i + 1: clean(pages[i].split("\n")) for i in range(len(pages))}

# insertar encabezados del TOC en su página
missing = []
for lvl, title, pg in toc:
    key = norm(title)
    lines = P.get(pg, [])
    hit = None
    for i, l in enumerate(lines):
        if l.startswith("#"):
            continue
        n = norm(re.sub(r"^\s*[\d.]+\s+", "", l))
        if n and (n == key or (len(n) > 6 and key.startswith(n)) or (len(key) > 6 and n.startswith(key))):
            hit = i
            break
    head = "#" * (lvl + 1) + " " + title.strip()
    if hit is None:
        missing.append((lvl, title, pg))
        lines.insert(0, head)
    else:
        # títulos que ocupan dos líneas: si la siguiente completa el título, se descarta
        nxt = lines[hit + 1] if hit + 1 < len(lines) else ""
        lines[hit] = head
        if nxt.strip() and norm(nxt) and norm(nxt) in key and not norm(nxt) == key:
            lines.pop(hit + 1)
    P[pg] = lines

units = [(t, p) for l, t, p in toc if l == 1]
os.makedirs(f"{OUT}/apuntes", exist_ok=True)
files = []
for k, (title, start) in enumerate(units):
    end = units[k + 1][1] - 1 if k + 1 < len(units) else len(pages)
    slug = "anexo-dlp" if title.startswith("ANEXO") else f"unidad-{k + 1}"
    fname = f"apuntes/{slug}.md"
    body = []
    for pg in range(start, end + 1):
        if not "".join(P.get(pg, [])).strip():
            continue
        body.append(f"<!-- p. {pg} -->")
        body += P[pg]
    text = "\n".join(body).strip() + "\n"
    open(f"{OUT}/{fname}", "w", encoding="utf-8").write(text)
    files.append((fname, title, start, end, text.split("\n")))

# index.md: cada entrada del TOC con archivo, línea y página
idx = ["# Índice de los apuntes", "",
       "Fuente: *Apuntes Teóricos de Arquitectura de Computadoras* (UNC, FCEFyN), de Augusto Gabriel Cabrera.",
       "Son apuntes **no oficiales** de la cátedra (versión del 6 de marzo de 2024).",
       "Columnas: `archivo:línea` para leer con Read (offset = línea) y página del PDF original.", ""]
for fname, title, start, end, lines in files:
    idx += [f"## {title}", "", f"Archivo: `{fname}` · páginas {start}–{end} · {len(lines)} líneas", ""]
    for i, l in enumerate(lines, 1):
        m = re.match(r"^(#{3,4}) (.+)$", l)
        if m:
            pg = next((int(x.group(1)) for x in (re.match(r"<!-- p\. (\d+) -->", lines[j]) for j in range(i - 1, -1, -1)) if x), start)
            ind = "  " * (len(m.group(1)) - 3)
            idx.append(f"{ind}- {m.group(2)} — `{fname}:{i}` (p. {pg})")
    idx.append("")
open(f"{OUT}/index.md", "w", encoding="utf-8").write("\n".join(idx))
print("faltantes:", len(missing))
for m in missing: print("  ", m)
