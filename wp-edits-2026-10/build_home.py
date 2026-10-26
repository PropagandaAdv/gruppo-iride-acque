"""Home (12) — giro modifiche call 2026-10-02."""
import re
from lib import *

d = load_backup("home-12")
scale_fonts(d)

# ------------------------------------------------------------ A) HERO
hero = find(d, "her0h01")["settings"]
h = hero["html"]
h = re.sub(r'\s*<div class="hero-ctas">.*?</div>\r?\n', "\n", h, flags=re.S)  # via la CTA: solo video + titolo
h = h.replace("font-size:clamp(2.2rem,5.2vw,4.4rem);max-width:900px;", "font-size:clamp(2.8rem,6.2vw,5.4rem);max-width:1080px;")
h = h.replace(".iah-hero .hero-h1 .accent{background:linear-gradient(90deg,#8DD6E8,#4AB7D5);-webkit-background-clip:text;background-clip:text;color:transparent;}",
              ".iah-hero .hero-h1 .accent{color:#5CCBEB;-webkit-text-fill-color:#5CCBEB;text-shadow:0 2px 24px rgba(9,23,31,.55);}")
h = h.replace("color:#8DD6E8;font-size:13px;letter-spacing:.22em", "color:#8DD6E8;font-size:15px;letter-spacing:.22em")
h = h.replace(".iah-hero .hero-copy{position:relative;z-index:5;min-height:92vh;display:flex;flex-direction:column;justify-content:center;padding:0 16px;",
              ".iah-hero .hero-copy{position:relative;z-index:5;min-height:92vh;display:flex;flex-direction:column;justify-content:center;padding:110px 16px 40px;")
assert "hero-ctas\">" not in h and "#5CCBEB" in h and "6.2vw" in h
hero["html"] = h

# ------------------------------------------------------------ B) CHI SIAMO: 4 box con hover "immagine che sale"
chs = find(d, "chs0001")
PILLAR_CSS = (
    "selector { width: calc(25% - 15px) !important; flex: 0 0 calc(25% - 15px) !important; height:470px; overflow:hidden; }\n"
    "@media(max-width:1024px){ selector { width: calc(50% - 10px) !important; flex: 0 0 calc(50% - 10px) !important; } }\n"
    "@media(max-width:767px){ selector { width: 100% !important; flex: 0 0 100% !important; } }\n"
    "selector{ position:relative!important; cursor:pointer; }\n"
    "selector .pillar-img img{ width:100%!important; height:290px!important; object-fit:cover!important; display:block; transition:height .65s cubic-bezier(.22,.61,.36,1); }\n"
    "selector:hover .pillar-img img{ height:150px!important; }\n"
    "selector .pillar-desc{ max-height:0; opacity:0; transform:translateY(14px); overflow:hidden; transition:max-height .65s cubic-bezier(.22,.61,.36,1), opacity .45s ease .12s, transform .65s cubic-bezier(.22,.61,.36,1); }\n"
    "selector:hover .pillar-desc{ max-height:170px; opacity:1; transform:none; }\n"
    "@media (hover:none){ selector{ height:auto; } selector .pillar-img img{ height:210px!important; } selector .pillar-desc{ max-height:none; opacity:1; transform:none; } }"
)
for card_id, link_id, num_id, title_id, desc_id in [
        ("p000007", "p000001", "p000004", "p000005", "p000006"),
        ("p000014", "p000008", "p000011", "p000012", "p000013"),
        ("p000021", "p000015", "p000018", "p000019", "p000020"),
        ("p000028", "p000022", "p000025", "p000026", "p000027")]:
    card = find(d, card_id)["settings"]
    card["custom_css"] = PILLAR_CSS
    card.pop("hover_animation", None)
    card["link"]["url"] = f"{SITE}/tecnologie-e-servizi/"
    lk = find(d, link_id)["settings"]
    lk["html"] = lk["html"].replace(f"{SITE}/servizi/", f"{SITE}/tecnologie-e-servizi/")
    find(d, num_id)["settings"]["typography_font_size"] = px(15)
    find(d, title_id)["settings"]["typography_font_size"] = px(23)
    ds = find(d, desc_id)["settings"]
    ds["_css_classes"] = "pillar-desc"
    ds["typography_font_size"] = px(17)

# box "Il Gruppo integra..." + bottone: via il testo, resta solo il bottone (centrato)
remove(d, "chs0061")
c60 = find(d, "chs0060")["settings"]
c60["flex_align_items"] = "center"
c60["padding"] = box(56, 0, 0, 0)
b62 = find(d, "chs0062")["settings"]
b62["link"]["url"] = f"{SITE}/modello-operativo/"
b62["typography_font_size"] = px(17)
b62["text_padding"] = box(17, 30, 17, 30)

# ------------------------------------------------------------ C) MODELLO OPERATIVO -> sezione propria a sfondo blu scuro
mod = find(d, "chs0070")
chs["elements"] = [e for e in chs["elements"] if e["id"] != "chs0070"]
remove([mod], "chs0080")  # bottone doppione: ora ogni fase ha "Scopri il metodo completo"
find([mod], "chs0071e")["settings"]["text_color"] = ACC2
find([mod], "chs0072h")["settings"].update({"text_color": "#FFFFFF"})
find([mod], "chs0073")["settings"].update({"text_color": "rgba(238,246,250,.82)", "typography_font_weight": "300"})
mod["settings"]["padding"] = box(0)
mod["settings"]["padding_mobile"] = box(0)

tabs = find([mod], "chs0ta1")["settings"]
BTN_BASE = ("display:inline-flex;align-items:center;gap:8px;padding:16px 28px;border-radius:999px;font-size:16px;"
            "font-weight:700;font-family:Montserrat,sans-serif;text-decoration:none;line-height:1.2;")
for i, t in enumerate(tabs["tabs"], start=1):
    c = scale_inline_px(t["tab_content"], {12.0: 14, 24.0: 30, 15.0: 17.5})
    c += ('<div style="display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:34px;">'
          f'<a href="{SITE}/modello-operativo/#fase-{i}" style="{BTN_BASE}color:#09171F;border:1.5px solid rgba(9,23,31,.4);background:transparent;">Scopri il metodo completo →</a>'
          f'<a href="#contatti" style="{BTN_BASE}color:#09171F;background:#4AB7D5;border:1.5px solid #4AB7D5;">Richiedi un\'analisi preliminare →</a>'
          '</div>')
    t["tab_content"] = c
    t["_id"] = f"ph0001{i}"
tabs.update({
    "tab_color": "rgba(238,246,250,.78)", "tab_active_color": NAVY,
    "custom_css": (
        "selector .elementor-tab-title { padding: 22px 24px !important; border-radius: 16px !important; margin-bottom: 10px !important; background: rgba(255,255,255,.06) !important; border:0!important; transition: background .3s ease; }\n"
        "selector .elementor-tab-desktop-title:hover { background: rgba(255,255,255,.12) !important; }\n"
        "selector .elementor-tab-title.elementor-active { background: #4AB7D5 !important; }\n"
        "selector .elementor-tabs-content-wrapper { background: #FFFFFF !important; border-radius: 24px !important; padding: 48px !important; border:0!important; }\n"
        "selector .elementor-tab-content { border:0!important; }\n"
        "selector .elementor-tab-mobile-title { color:#09171F!important; background:#EEF6FA!important; }\n"
        "selector .elementor-tab-mobile-title.elementor-active { background:#4AB7D5!important; }\n"
        "@media(max-width:767px){ selector .elementor-tabs-content-wrapper{ padding:22px !important; } }"),
})
tabs["tab_typography_font_size"] = px(18)

modello = section("sec-modello", "modello-operativo", NAVY, [mod])

# ------------------------------------------------------------ D) NUMERI
num = find(d, "num0001")
for card_id, row_id, html_id, badge_id, label_id, value in [
        ("n000038", "n000036", "n000033", "n000035", "n000037", 120),
        ("n000044", "n000042", "n000039", "n000041", "n000043", 85),
        ("n000050", "n000048", "n000045", "n000047", "n000049", 12)]:
    cs = find(d, card_id)["settings"]
    cs.update({"flex_align_items": "center", "flex_justify_content": "center", "padding": box(44, 28, 44, 28),
               "flex_gap": gap(14), "background_color": PANEL, "border_border": "", "border_width": box(0)})
    rs = find(d, row_id)["settings"]
    rs.update({"flex_direction": "column", "flex_direction_mobile": "column", "flex_align_items": "center",
               "flex_justify_content": "center", "flex_gap": gap(12)})
    hs = find(d, html_id)["settings"]
    hs["html"] = (hs["html"].replace('data-finalcount="XXX"', f'data-finalcount="{value}"')
                  .replace(">XXX</span>", f">{value}</span>")
                  .replace("font-size:40px", "font-size:64px")
                  .replace('class="iah-counter"', 'class="iah-counter" ', 1)
                  .replace('style="font-family', 'style="display:block;text-align:center;font-family', 1))
    find(d, badge_id.replace("35", "34").replace("41", "40").replace("47", "46"))["settings"]["custom_css"] = "selector{width:auto!important;flex:0 0 auto!important;align-self:center;}"
    bs = find(d, badge_id)["settings"]
    bs["editor"] = "<p>Valore indicativo</p>"
    bs["typography_font_size"] = px(12)
    bs["align"] = "center"
    ls = find(d, label_id)["settings"]
    ls.update({"align": "center", "typography_font_size": px(19)})
find(d, "num0031")["settings"]["typography_font_size"] = px(17)
num["settings"]["padding"] = box(100, 24, 110, 24)

# ------------------------------------------------------------ E) LE SOCIETÀ (home)
for card_id, link_id, ov_id, url in [("s000033", "s000035", "s000036", "https://irideacque.com/"),
                                     ("s000038", "s000042", "s000043", "https://www.biemmeengineering.it/"),
                                     ("s000045", "s000049", "s000050", "https://costruzionibieffe.it/")]:
    ls = find(d, link_id)["settings"]
    ls["html"] = re.sub(r'href="[^"]+"', f'href="{url}" target="_blank" rel="noopener"', ls["html"], count=1)
    ov = find(d, ov_id)["settings"]
    ov["html"] = ov["html"].replace("font-size:16px", "font-size:19px").replace("font-size:13.5px", "font-size:16px")
# BM Engineering e Bieffe: sfondo scuro, i loghi definitivi saranno chiari
for card_id, ph_id, name_id, note_id in [("s000038", "s000039", "s000040", "s000041"),
                                         ("s000045", "s000046", "s000047", "s000048")]:
    cs = find(d, card_id)["settings"]
    cs.update({"background_color": NAVY, "border_color": "rgba(9,23,31,.0)"})
    find(d, ph_id)["settings"]["border_color"] = "rgba(255,255,255,.35)"
    find(d, name_id)["settings"].update({"text_color": "#FFFFFF", "typography_font_size": px(20)})
    find(d, note_id)["settings"].update({"text_color": "rgba(238,246,250,.72)", "typography_font_size": px(13.5)})
find(d, "s000034")["settings"]["width"] = px(210)

# ------------------------------------------------------------ F) AMBITI: zoom leggero sull'immagine, link corretti
for card_id, link_id, cta_id in [("a000039", "a000036", "a000035"), ("a000046", "a000043", "a000042")]:
    cs = find(d, card_id)["settings"]
    cs["custom_css"] = (cs["custom_css"] + "\nselector{ overflow:hidden; }\n"
                        "selector::before{ transition: transform 1.1s cubic-bezier(.22,.61,.36,1) !important; }\n"
                        "selector:hover::before{ transform: scale(1.07); }")
    for wid in (link_id, cta_id):
        st = find(d, wid)["settings"]
        key = "html" if "html" in st else "editor"
        st[key] = re.sub(rf'{re.escape(SITE)}/(settore-industriale|ambito-civile-pa)/', f"{SITE}/tecnologie-e-servizi/", st[key])

# ------------------------------------------------------------ assemblaggio: Hero, Chi siamo, Modello (scuro), Numeri (scuro), Società, Ambiti
order = ["her0001", "chs0001", "MOD", "num0001", "soc0001", "amb0001"]
by_id = {e["id"]: e for e in d}
by_id["MOD"] = modello
out = [by_id[k] for k in order]
# nessun bordo/margine residuo tra sezioni adiacenti
for e in out:
    e["settings"]["margin"] = box(0)
    e["settings"].pop("border_border", None)

if __name__ == "__main__":
    dump(out, "home-12")
