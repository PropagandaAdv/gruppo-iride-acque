"""Helper condivisi per costruire _elementor_data (Flexbox Container) del sito Gruppo Iride Acque."""
import copy
import itertools
import json
import re

SITE = "https://gruppoirideacque.propagandaadv.com"
NAVY = "#09171F"
BLUE = "#1A4D6A"
ACC = "#4AB7D5"
ACC2 = "#8DD6E8"
VIVID = "#5CCBEB"  # azzurro brand ravvivato per gli accenti sopra i video
LIGHT = "#EEF6FA"
BODY = "#3D5A6C"
PANEL = "#123852"  # box su sfondo scuro: un tono sopra il navy, senza bordo
FONT = "Montserrat"

_ids = itertools.count(1)


def nid(prefix="x"):
    """ID univoco 7 caratteri (apply_template li rigenera comunque)."""
    return f"{prefix}{next(_ids):06d}"[-7:].lower()


def px(n):
    return {"unit": "px", "size": n}


def box(t, r=None, b=None, l=None, unit="px"):
    r = t if r is None else r
    b = t if b is None else b
    l = r if l is None else l
    return {"unit": unit, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l),
            "isLinked": t == r == b == l}


def gap(n):
    return {"unit": "px", "size": n, "column": str(n), "row": str(n)}


def radius(n):
    return box(n)


def typo(size, weight="400", lh=None, mobile=None, ls=None, prefix="typography"):
    s = {f"{prefix}_typography": "custom", f"{prefix}_font_family": FONT,
         f"{prefix}_font_weight": str(weight), f"{prefix}_font_size": px(size)}
    if lh:
        s[f"{prefix}_line_height"] = {"unit": "em", "size": lh}
    if mobile:
        s[f"{prefix}_font_size_mobile"] = px(mobile)
    if ls is not None:
        s[f"{prefix}_letter_spacing"] = px(ls)
    return s


def W(widget_type, settings, wid=None):
    return {"id": wid or nid("w"), "elType": "widget", "widgetType": widget_type,
            "settings": settings, "elements": []}


def C(settings, children, inner=True, cid=None):
    s = {"flex_direction": "column", "flex_direction_mobile": "column"}
    s.update(settings)
    if "_css_classes" in s:  # sui container la chiave Elementor è css_classes
        s["css_classes"] = s.pop("_css_classes")
    return {"id": cid or nid("c"), "elType": "container", "isInner": inner,
            "settings": s, "elements": children}


def section(css_id, element_id, bg, children, pad=(110, 24, 110, 24), pad_m=(70, 16, 70, 16), extra=None):
    s = {"css_id": css_id, "content_width": "full",
         "background_background": "classic", "background_color": bg,
         "padding": box(*pad), "padding_mobile": box(*pad_m),
         "margin": box(0)}
    if element_id:
        s["_element_id"] = element_id
    if extra:
        s.update(extra)
    return C(s, children, inner=False)


def inner_boxed(children, width=1240, g=18, g_m=14, extra=None):
    s = {"content_width": "boxed", "boxed_width": px(width), "flex_gap": gap(g), "flex_gap_mobile": gap(g_m)}
    if extra:
        s.update(extra)
    return C(s, children)


def eyebrow(text, color):
    return W("text-editor", {"editor": f"<p>{text}</p>", "text_color": color,
                             **typo(19, 800, ls=1.4, mobile=17)})


def grad(text):
    return ('<span style="background:linear-gradient(90deg,#8DD6E8,#4AB7D5);-webkit-background-clip:text;'
            'background-clip:text;-webkit-text-fill-color:transparent;">' + text + '</span>')


def h2(html_text, color, size=48, mobile=30, maxw=None, tag="text"):
    s = {"editor": f"<p>{html_text}</p>", "text_color": color, **typo(size, 800, lh=1.15, mobile=mobile)}
    if maxw:
        s["_max_width"] = px(maxw)
    return W("text-editor", s)


def heading(title, color, size, tag="h3", weight=800, lh=1.25, mobile=None, align=None):
    s = {"title": title, "header_size": tag, "title_color": color, **typo(size, weight, lh=lh, mobile=mobile)}
    if align:
        s["align"] = align
    return W("heading", s)


def para(html, color=BODY, size=18, weight=400, lh=1.7, maxw=None, align=None, mobile=None):
    s = {"editor": html if html.startswith("<") else f"<p>{html}</p>", "text_color": color,
         **typo(size, weight, lh=lh, mobile=mobile)}
    if maxw:
        s["_max_width"] = px(maxw)
    if align:
        s["align"] = align
    return W("text-editor", s)


def button(text, url, style="solid", size=16.5, external=False, align=None):
    s = {"text": text, "link": {"url": url, "is_external": "on" if external else "", "nofollow": ""},
         "border_radius": radius(999), **typo(size, 700),
         "text_padding": box(17, 30, 17, 30)}
    if style == "solid":
        s.update({"background_color": ACC, "button_text_color": NAVY,
                  "button_background_hover_color": ACC2, "hover_color": NAVY})
    elif style == "outline":
        s.update({"background_color": "rgba(0,0,0,0)", "button_text_color": NAVY,
                  "border_border": "solid", "border_width": box(1.5), "border_color": "rgba(9,23,31,.35)",
                  "button_background_hover_color": NAVY, "hover_color": "#FFFFFF"})
    elif style == "outline-light":
        s.update({"background_color": "rgba(0,0,0,0)", "button_text_color": "#FFFFFF",
                  "border_border": "solid", "border_width": box(1.5), "border_color": "rgba(255,255,255,.45)",
                  "button_background_hover_color": "#FFFFFF", "hover_color": NAVY})
    if align:
        s["align"] = align
    return W("button", s)


def html(code, extra=None):
    s = {"html": code}
    if extra:
        s.update(extra)
    return W("html", s)


# ---------- scaling tipografico ("il mantra": testi più grandi ovunque) ----------

def _r(x):
    return round(x * 2) / 2


def bigger(s):
    if s <= 11:
        return _r(s + 2)
    if s <= 15.5:
        return _r(s * 1.18)
    if s <= 19:
        return _r(s * 1.15)
    if s <= 26:
        return _r(s * 1.18)
    return _r(s * 1.2)


def scale_fonts(tree):
    def walk(e):
        st = e.get("settings", {})
        for k, v in list(st.items()):
            if not isinstance(v, dict) or "size" not in v or v.get("unit") != "px":
                continue
            if not isinstance(v["size"], (int, float)):
                continue
            if k.endswith("font_size"):
                v["size"] = bigger(v["size"])
            elif k.endswith("font_size_mobile") or k.endswith("font_size_tablet"):
                v["size"] = _r(v["size"] * 1.1)
        for c in e.get("elements", []):
            walk(c)
    for e in tree:
        walk(e)
    return tree


def find(tree, eid):
    for e in tree:
        if e["id"] == eid:
            return e
        r = find(e.get("elements", []), eid)
        if r:
            return r
    return None


def remove(tree, eid):
    for i, e in enumerate(tree):
        if e["id"] == eid:
            del tree[i]
            return True
        if remove(e.get("elements", []), eid):
            return True
    return False


def scale_inline_px(htmlstr, mapping):
    def rep(m):
        v = float(m.group(1))
        nv = mapping.get(v)
        if nv is None:
            nv = bigger(v)
        return f"font-size:{nv:g}px"
    return re.sub(r"font-size:\s*([\d.]+)px", rep, htmlstr)


def load_backup(name):
    return json.load(open(f"backup/{name}.json", encoding="utf-8"))


def fix_ids(tree):
    """Normalizza gli ID non conformi (7-8 char [a-z0-9]) ereditati dalle pagine originali."""
    seen = set()
    def walk(e):
        if not re.match(r"^[a-z0-9]{7,8}$", e["id"]) or e["id"] in seen:
            e["id"] = nid("r")
        seen.add(e["id"])
        for c in e.get("elements", []):
            walk(c)
    for e in tree:
        walk(e)
    return tree


def dump(tree, name):
    fix_ids(tree)
    out = json.dumps(tree, ensure_ascii=False, separators=(",", ":"))
    open(f"build/{name}.json", "w", encoding="utf-8").write(out)
    # copia leggibile riga-per-riga per l'import manuale (stesso JSON, solo a capo tra i token)
    open(f"build/{name}.paste.json", "w", encoding="utf-8").write(json.dumps(tree, ensure_ascii=False, indent=0, separators=(",", ":")))
    print(f"build/{name}.json  {len(out)/1024:.1f} KB")
    return out


def deep(x):
    return copy.deepcopy(x)
