"""Sostituzione colore Primario #0D2B3E -> #09171F su tutte le pagine/template Elementor (2026-10-06).

Fonte: gli stessi JSON pubblicati il 2026-10-05 (nessun salvataggio da editor dopo, verificato sulle revisioni),
piu' la copia live di Tecnologie e Servizi (mai ricostruita) e l'hero template 63.
Sostituisce anche la forma rgba(13,43,62,a) dello stesso colore (scrim, vetro header, ombre) -> rgba(9,23,31,a).
"""
import json
import os
import re

from lib import fix_ids, find

OLD_HEX = re.compile(r"#0d2b3e", re.I)
OLD_RGBA = re.compile(r"rgba\(\s*13\s*,\s*43\s*,\s*62\s*,")
NEW_HEX = "#09171F"
NEW_RGBA = "rgba(9,23,31,"


def load(path):
    return json.load(open(path, encoding="utf-8"))


def heading_from_text(el, size_key="typography_font_size"):
    """Converte un text-editor 'titolo' in widget heading h2 (come pubblicato a mano il 2026-10-05)."""
    s = el["settings"]
    title = re.sub(r"<[^>]+>", "", s["editor"]).strip()
    new = {"title": title, "header_size": "h2", "title_color": s["text_color"]}
    for k, v in s.items():
        if k.startswith("typography_"):
            new[k] = v
    el["widgetType"] = "heading"
    el["settings"] = new


SOURCES = {
    # post_id: (file, nome)
    39: ("build/header-39.json", "Header (template globale)"),
    42: ("build/footer-42.json", "Footer (template globale)"),
    12: ("build/home-12.json", "Home"),
    55: ("build/ilgruppo-55.json", "Il Gruppo"),
    64: ("build/societa-64.json", "Le società del gruppo"),
    66: ("backup/tecnologie-66.json", "Tecnologie e Servizi"),
    78: ("build/contatti-78.json", "Contatti"),
    130: ("build/metodo-new.json", "Modello operativo"),
    131: ("build/news-new.json", "News"),
    132: ("build/lavora-new.json", "Lavora con noi"),
    63: (None, "Hero Pagine Interne — Brand Template (libreria)"),
}

os.makedirs("build/recolor", exist_ok=True)
report = []
for pid, (path, name) in SOURCES.items():
    if pid == 63:
        data = [load("backup/ilgruppo-55.json")[0]]
    else:
        data = load(path)
    # allineamento con quanto pubblicato a mano (H2 veri su News e Lavora con noi)
    if pid == 131:
        for t in ("Le novità del Gruppo Iride Acque", "Dalle società del"):
            for e in data:
                stack = [e]
                while stack:
                    x = stack.pop()
                    if x.get("widgetType") == "text-editor" and t in x["settings"].get("editor", ""):
                        heading_from_text(x)
                    stack.extend(x.get("elements", []))
    if pid == 132:
        for e in data:
            stack = [e]
            while stack:
                x = stack.pop()
                if x.get("widgetType") == "text-editor" and x["settings"].get("editor") == "<p>Posizioni aperte</p>":
                    heading_from_text(x)
                stack.extend(x.get("elements", []))
    fix_ids(data)
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    n_hex = len(OLD_HEX.findall(raw))
    n_rgba = len(OLD_RGBA.findall(raw))
    # occorrenze dentro widget HTML / custom_css (per il report)
    html_hits = sum(len(OLD_HEX.findall(m)) + len(OLD_RGBA.findall(m))
                    for m in re.findall(r'"(?:html|custom_css)":"((?:[^"\\]|\\.)*)"', raw))
    new = OLD_RGBA.sub(NEW_RGBA, OLD_HEX.sub(NEW_HEX, raw))
    if pid == 42:  # nota AI nel footer: 4.20:1 anche col nuovo fondo -> opacita' 0.62 (6.6:1, WCAG AA)
        assert new.count('"text_color":"rgba(238,246,250,0.45)"') == 1
        new = new.replace('"text_color":"rgba(238,246,250,0.45)"', '"text_color":"rgba(238,246,250,0.62)"')
    assert not OLD_HEX.search(new) and not OLD_RGBA.search(new)
    json.loads(new)
    open(f"build/recolor/{pid}.json", "w", encoding="utf-8").write(new)
    report.append((pid, name, n_hex, n_rgba, html_hits, len(new)))

print(f"{'ID':>4}  {'pagina':48} {'#0D2B3E':>8} {'rgba':>6} {'in HTML/CSS':>11} {'KB':>6}")
for pid, name, h, r, x, size in report:
    print(f"{pid:>4}  {name:48} {h:>8} {r:>6} {x:>11} {size/1024:>6.1f}")
print("totale", sum(r[2] for r in report), "hex +", sum(r[3] for r in report), "rgba")
json.dump([dict(id=p, name=n, hex=h, rgba=r, in_html_css=x) for p, n, h, r, x, _ in report],
          open("build/recolor/report.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
