import json, copy, random, re
random.seed(1013)
BASE = "https://gruppoirideacque.propagandaadv.com"
t = json.load(open("p12_current.json", encoding="utf8"))


def nid():
    return "%07x" % random.randrange(0x1000000, 0xfffffff)


def find(n, i):
    if isinstance(n, list):
        for x in n:
            r = find(x, i)
            if r:
                return r
        return None
    if n.get("id") == i:
        return n
    for c in n.get("elements", []) or []:
        r = find(c, i)
        if r:
            return r


def W(wt, settings):
    return {"id": nid(), "elType": "widget", "settings": settings, "elements": [], "widgetType": wt}


def C(settings, children, inner=True):
    return {"id": nid(), "elType": "container", "settings": settings, "elements": children, "isInner": inner}


# ---------- 1.1 pillars: image height + aria label + alt
for i in ("4d9df052", "f59f6710", "cee19cb9", "94ac610b"):
    w = find(t, i)
    assert w
    w["settings"]["height"] = {"unit": "px", "size": 210}
    w["settings"]["height_mobile"] = {"unit": "px", "size": 200}
    w["settings"]["image_size"] = "full"
b = find(t, "b07c2b37")
b["settings"]["html"] = b["settings"]["html"].replace('aria-label="Costruzione"', 'aria-label="Produzione"')
alts = {
    "4d9df052": "Progettazione: mani su un disegno tecnico di un impianto di trattamento acque",
    "f59f6710": "Produzione: tecnico con felpa Iride Acque al lavoro su un impianto",
    "cee19cb9": "Gestione: operatore in tuta protettiva davanti a un quadro elettrico di impianto",
    "94ac610b": "Ottimizzazione e rendicontazione: operatore davanti al monitor con il sinottico dell'impianto",
}
for k, v in alts.items():
    find(t, k)["settings"]["image"]["alt"] = v

# ---------- 1.2 intro paragraph justified
p = find(t, "249f38b8")
p["settings"]["align"] = "justify"
p["settings"]["custom_css"] = "selector, selector .elementor-widget-container, selector p{ text-align:justify !important; text-justify:inter-word; hyphens:auto; }"

# ---------- 1.3 societa logos
LOGOS = {
    "c1afe94b": (382, "logo-iride-acque-gruppo.webp", "Logo Iride Acque"),
    "176efebf": (383, "logo-biemme-engineering-gruppo.webp", "Logo BIEMME Engineering"),
    "78f4b881": (384, "logo-bieffe-costruzioni-gruppo.webp", "Logo BIEFFE Costruzioni"),
}
ZERO = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
for card, (mid, fn, alt) in LOGOS.items():
    c = find(t, card)
    assert c
    s = c["settings"]
    s["background_color"] = "#00243C"
    s["padding"] = dict(ZERO)
    s["padding_mobile"] = dict(ZERO)
    s["border_color"] = "rgba(255,255,255,.08)"
    s["flex_align_items"] = "stretch"
    s["flex_justify_content"] = "center"
    wrapper = [e for e in c["elements"] if e["elType"] == "container"][0]
    wrapper["settings"] = {
        "content_width": "full", "flex_direction": "column", "flex_direction_mobile": "column",
        "padding": dict(ZERO), "flex_align_items": "stretch", "flex_justify_content": "center",
        "width": {"unit": "%", "size": 100},
    }
    wrapper["elements"] = [{
        "id": nid(), "elType": "widget", "widgetType": "image", "elements": [],
        "settings": {
            "image": {"url": f"{BASE}/wp-content/uploads/2026/10/{fn}", "id": mid, "alt": alt},
            "image_size": "full", "width": {"unit": "%", "size": 100}, "align": "center",
            "_element_width": "initial", "_element_custom_width": {"unit": "%", "size": 100},
            "_css_classes": "soc-logo",
        },
    }]

# ---------- 1.4 ambiti
amb = find(t, "8196a7d4")
amb["settings"]["custom_css"] = """selector .amb-card{position:relative !important;overflow:hidden;border-radius:28px;min-height:410px;cursor:pointer;}
selector .amb-panel{position:relative;z-index:2;width:60% !important;max-width:100% !important;padding:34px 38px 30px !important;margin:0 !important;
  background:linear-gradient(90deg,rgba(7,43,76,.90) 0%,rgba(7,43,76,.78) 72%,rgba(7,43,76,0) 100%);
  transition:width .38s ease, background .38s ease;}
selector .amb-card:hover .amb-panel, selector .amb-card:focus-within .amb-panel{width:94% !important;
  background:linear-gradient(90deg,rgba(7,43,76,.96) 0%,rgba(7,43,76,.88) 78%,rgba(7,43,76,.18) 100%);}
selector .amb-desc{max-height:4.9em;overflow:hidden;transition:max-height .38s ease;}
selector .amb-card:hover .amb-desc, selector .amb-card:focus-within .amb-desc{max-height:14em;}
selector .amb-desc p, selector .amb-link p{margin:0 !important;}
selector .amb-link a{color:#8DD6E8 !important;text-decoration:none;font-weight:600;transition:color .25s ease;}
selector .amb-card:hover .amb-link a{color:#FFFFFF !important;}
@media (max-width:767px){
  selector .amb-card{min-height:0;}
  selector .amb-panel{width:100% !important;padding:26px 22px 24px !important;background:linear-gradient(90deg,rgba(7,43,76,.92),rgba(7,43,76,.80));}
  selector .amb-desc{max-height:none;}
}
@media (hover:none){
  selector .amb-panel{width:100% !important;}
  selector .amb-desc{max-height:none;}
}"""

AMB = [
    dict(card="73eedd54", img=("ambito-industriale-membrane-osmosi-inversa.webp", 393),
         alt="Membrane di osmosi inversa in acciaio di un impianto per il trattamento delle acque industriali",
         icon="fas fa-industry",
         title="Trattamento delle acque industriali",
         desc="Recupero acque di processo, trattamenti completi, abbattimento fanghi, impianti a Scarico Zero (ZLD) e soluzioni ingegnerizzate per la riduzione di OPEX e il rispetto dei limiti autorizzativi.",
         link="Scopri le soluzioni per il settore industriale",
         url=BASE + "/settori/industriale/"),
    dict(card="ab03f0fd", img=("ambito-sii-vasche-depurazione-cielo-aperto.webp", 392),
         alt="Vasche circolari di depurazione a cielo aperto di un impianto per il servizio idrico integrato",
         icon="fas fa-home",
         title="Soluzioni per il Servizio Idrico Integrato e la PA",
         desc="Potabilizzazione, depurazione reflui urbani, riuso irriguo, tutela dei corpi idrici recettori, supporto tecnico ai gestori del SII e agli enti pubblici in materia di compliance autorizzativa.",
         link="Scopri le soluzioni per il civile",
         url=BASE + "/settori/servizio-idrico-integrato/"),
]
row = find(t, "d6db4876")
new_cards = []
for a in AMB:
    old = find(t, a["card"])
    assert old
    oid = old["id"]
    s = {
        "content_width": "full", "flex_direction": "column", "flex_direction_mobile": "column",
        "width": {"unit": "%", "size": 50}, "width_tablet": {"unit": "%", "size": 50}, "width_mobile": {"unit": "%", "size": 100},
        "border_radius": {"unit": "px", "top": "28", "right": "28", "bottom": "28", "left": "28", "isLinked": True},
        "padding": dict(ZERO),
        "flex_justify_content": "flex-end", "flex_align_items": "flex-start",
        "border_border": "solid", "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
        "border_color": "rgba(141,214,232,.28)",
        "box_shadow_box_shadow_type": "yes",
        "box_shadow_box_shadow": {"horizontal": 0, "vertical": 24, "blur": 50, "spread": -20, "color": "rgba(0,0,0,.45)"},
        "min_height": {"unit": "px", "size": 410},
        "background_background": "classic", "background_color": "#09171F",
        "background_image": {"url": f"{BASE}/wp-content/uploads/2026/10/{a['img'][0]}", "id": a["img"][1], "alt": a["alt"]},
        "background_position": "center center", "background_repeat": "no-repeat", "background_size": "cover",
        "css_classes": "amb-card",
        "custom_css": "selector { width: calc(50.0000% - 12.00px) !important; flex: 0 0 calc(50.0000% - 12.00px) !important; }\n@media(max-width:1024px){ selector { width: calc(50.0000% - 12.00px) !important; flex: 0 0 calc(50.0000% - 12.00px) !important; } }\n@media(max-width:767px){ selector { width: 100% !important; flex: 0 0 100% !important; } }",
    }
    anchor = W("html", {
        "html": f'<a href="{a["url"]}" aria-label="{a["title"]}" style="position:absolute;inset:0;z-index:10;display:block;"></a>',
        "custom_css": "selector{ position:static !important; }"})
    iconbox = C({
        "content_width": "full", "flex_direction": "row", "flex_direction_mobile": "row",
        "flex_align_items": "center", "flex_justify_content": "center",
        "width": {"unit": "px", "size": 48}, "height": {"unit": "px", "size": 48},
        "min_width": {"unit": "px", "size": 48}, "max_width": {"unit": "px", "size": 48},
        "background_background": "classic", "background_color": "rgba(255,255,255,.14)",
        "border_radius": {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True},
        "flex_shrink": 0,
        "custom_css": "selector { width:48px!important;height:48px!important;flex:0 0 48px!important; backdrop-filter:blur(4px); }"},
        [W("icon", {"selected_icon": {"value": a["icon"], "library": "fa-solid"},
                    "primary_color": "#8DD6E8", "size": {"unit": "px", "size": 20}})])
    title = W("heading", {
        "title": a["title"], "header_size": "h3", "title_color": "#FFFFFF", "typography_typography": "custom",
        "typography_font_family": "Montserrat", "typography_font_weight": "700",
        "typography_font_size": {"unit": "px", "size": 23}, "typography_font_size_mobile": {"unit": "px", "size": 20},
        "typography_line_height": {"unit": "em", "size": 1.3}})
    desc = W("text-editor", {
        "editor": f"<p>{a['desc']}</p>", "text_color": "rgba(238,246,250,.92)", "typography_typography": "custom",
        "typography_font_family": "Montserrat", "typography_font_weight": "400",
        "typography_font_size": {"unit": "px", "size": 16.5}, "typography_font_size_mobile": {"unit": "px", "size": 15.5},
        "typography_line_height": {"unit": "em", "size": 1.6}, "_css_classes": "amb-desc"})
    link = W("text-editor", {
        "editor": f'<p><a href="{a["url"]}">{a["link"]} &#8594;</a></p>', "typography_typography": "custom",
        "typography_font_family": "Montserrat", "typography_font_size": {"unit": "px", "size": 16.5},
        "_css_classes": "amb-link"})
    panel = C({"content_width": "full", "flex_direction": "column", "flex_direction_mobile": "column",
               "css_classes": "amb-panel", "flex_align_items": "flex-start",
               "flex_gap": {"unit": "px", "size": 12, "column": "12", "row": "12"}},
              [iconbox, title, desc, link])
    card = C(s, [anchor, panel])
    card["id"] = oid
    new_cards.append(card)
row["elements"] = new_cards

json.dump(t, open("p12_new.json", "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
s = json.dumps(t, ensure_ascii=False, separators=(",", ":"))
print(len(s))
for k in ("Costruzione", "pillar-progettazione", "logo-iride-acque.png", "Logo in attesa"):
    print(k, s.count(k))
