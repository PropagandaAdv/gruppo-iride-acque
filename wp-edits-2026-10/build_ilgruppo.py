"""Il Gruppo (55) — giro modifiche call 2026-10-02."""
import re
from lib import *

d = load_backup("ilgruppo-55")


def text_of(eid):
    return find(d, eid)["settings"]["editor"]


T_ORIGINI = text_of("evotxt1")
T_CREDEM = text_of("evotxt2")
T_STRATEGIA = text_of("evotxt3")
T_HQ = text_of("ig1042")

scale_fonts(d)

# ------------------------------------------------------------ HERO
hs = find(d, "igh0h01")["settings"]
h = hs["html"]
h = h.replace('<h1 class="hero-h1">Da specialisti verticali a <span class="accent">piattaforma industriale integrata</span></h1>',
              '<h1 class="hero-h1">Da specialisti verticali a<br class="iah-br"> <span class="accent">piattaforma industriale integrata</span></h1>')
h = h.replace(f'href="{SITE}/home/#societa"', f'href="{SITE}/le-societa-del-gruppo/"')
h = h.replace("</style>",
              "#bhHeroIlGruppo .hero-h1{font-size:clamp(2.3rem,4.1vw,3.7rem)!important;max-width:none!important;}\n"
              "#bhHeroIlGruppo .hero-kicker{font-size:16px!important;}\n"
              "@media(max-width:900px){#bhHeroIlGruppo .iah-br{display:none;}#bhHeroIlGruppo .hero-h1{font-size:clamp(2rem,8.4vw,2.8rem)!important;}}\n"
              "</style>", 1)
assert 'class="iah-br"' in h and "le-societa-del-gruppo" in h
hs["html"] = h

# ------------------------------------------------------------ TIMELINE orizzontale (sostituisce timeline verticale, Missione/Visione e blocco HQ)
TL_CSS = """<style>
.iah-tl-row{position:relative;}
.iah-tl-row::before{content:"";position:absolute;left:0;right:0;top:50%;height:2px;background:linear-gradient(90deg,#4AB7D5,#1A4D6A);transform:translateY(-1px);z-index:0;}
.iah-tl-row > .iah-tl-pt{flex:1 1 0!important;width:auto!important;}
.iah-tl-pt{position:relative;height:400px;display:flex!important;align-items:center!important;justify-content:center!important;}
.iah-tl-mark{position:relative;z-index:3;width:22px!important;height:22px!important;min-width:22px;flex:0 0 22px!important;transition:transform .3s ease;}
.iah-tl-pt:hover .iah-tl-mark{transform:scale(1.3);}
.iah-tl-pt::after{content:"";position:absolute;left:50%;width:2px;height:36px;background:#B7C3CB;transform:translateX(-1px);z-index:1;}
.iah-tl-up::after{bottom:calc(50% + 11px);}
.iah-tl-down::after{top:calc(50% + 11px);}
.iah-tl-lbl{position:absolute!important;left:50%;transform:translateX(-50%);width:240px!important;max-width:240px;}
.iah-tl-up .iah-tl-lbl{bottom:calc(50% + 50px);}
.iah-tl-down .iah-tl-lbl{top:calc(50% + 50px);}
.iah-tl-hint{display:inline-block;margin-top:6px;font:600 13px/1.4 Montserrat,sans-serif;color:#4AB7D5;letter-spacing:.04em;}
.iah-tl-pop{position:absolute!important;left:50%;width:400px!important;max-width:400px;z-index:30;opacity:0;visibility:hidden;transform:translate(-50%,10px);transition:opacity .3s ease,transform .3s ease,visibility .3s;background:#FFFFFF;border-radius:20px;padding:24px 26px!important;box-shadow:0 26px 60px -18px rgba(9,23,31,.38);}
.iah-tl-up .iah-tl-pop{top:calc(50% + 28px);}
.iah-tl-down .iah-tl-pop{bottom:calc(50% + 28px);}
.iah-tl-pt:hover .iah-tl-pop{opacity:1;visibility:visible;transform:translate(-50%,0);}
.iah-tl-row > .iah-tl-pt:first-child .iah-tl-pop{left:0;transform:translate(0,10px);}
.iah-tl-row > .iah-tl-pt:first-child:hover .iah-tl-pop{transform:translate(0,0);}
.iah-tl-row > .iah-tl-pt:last-child .iah-tl-pop{left:auto;right:0;transform:translate(0,10px);}
.iah-tl-row > .iah-tl-pt:last-child:hover .iah-tl-pop{transform:translate(0,0);}
.iah-tl-pop p{margin:0;}
@media(max-width:900px){
.iah-tl-row{flex-direction:column!important;gap:34px!important;padding-left:34px!important;}
.iah-tl-row::before{left:10px;right:auto;top:6px;bottom:6px;width:2px;height:auto;transform:none;background:linear-gradient(180deg,#4AB7D5,#1A4D6A);}
.iah-tl-pt{height:auto;flex-direction:column!important;align-items:flex-start!important;justify-content:flex-start!important;}
.iah-tl-pt::after,.iah-tl-hint{display:none;}
.iah-tl-mark{position:absolute!important;left:-34px;top:4px;}
.iah-tl-lbl,.iah-tl-pop{position:static!important;transform:none!important;width:100%!important;max-width:none!important;opacity:1!important;visibility:visible!important;}
.iah-tl-lbl{text-align:left!important;}
.iah-tl-lbl .elementor-widget-container{text-align:left!important;}
.iah-tl-pop{box-shadow:none;background:transparent;padding:8px 0 0!important;}
}
</style>"""

POINTS = [
    ("Le origini", "Crescita per acquisizioni mirate", T_ORIGINI, "up", ACC),
    ("2026", "Investimento Credem Euromobiliare", T_CREDEM, "down", BLUE),
    ("Nuova sede", "Il nuovo Headquarter di Arosio", T_HQ, "up", ACC),
    ("L'obiettivo", "Una piattaforma industriale integrata", T_STRATEGIA, "down", BLUE),
]


def tl_point(label, caption, body_html, side, color):
    return C({"content_width": "full", "_css_classes": f"iah-tl-pt iah-tl-{side}",
              "padding": box(0), "padding_mobile": box(0)}, [
        C({"content_width": "full", "_css_classes": "iah-tl-lbl", "flex_gap": gap(4), "flex_gap_mobile": gap(4),
           "flex_align_items": "center", "padding": box(0)}, [
            heading(label, NAVY if color == BLUE else BLUE, 28, "h3", 800, lh=1.15, mobile=24, align="center"),
            W("text-editor", {"editor": f'<p>{caption}</p><span class="iah-tl-hint">Passa il mouse per approfondire</span>',
                              "text_color": BODY, "align": "center", **typo(16.5, 500, lh=1.45)}),
        ]),
        C({"content_width": "full", "_css_classes": "iah-tl-mark", "background_background": "classic",
           "background_color": color, "border_radius": radius(4), "padding": box(0)}, []),
        C({"content_width": "full", "_css_classes": "iah-tl-pop", "padding": box(0)}, [
            W("text-editor", {"editor": body_html, "text_color": BODY, **typo(15.5, 400, lh=1.65)}),
        ]),
    ])


timeline = C({"content_width": "boxed", "boxed_width": px(1240), "css_id": "sec-evoluzione-timeline",
              "_element_id": "evoluzione", "flex_gap": gap(10), "flex_gap_mobile": gap(10),
              "padding": box(72, 0, 0, 0), "padding_mobile": box(44, 0, 0, 0)}, [
    heading("Evoluzione industriale del Gruppo", NAVY, 36, "h2", 800, lh=1.2, mobile=27),
    C({"content_width": "full", "_css_classes": "iah-tl-row", "flex_direction": "row", "flex_direction_mobile": "column",
       "flex_gap": gap(24), "flex_gap_mobile": gap(34), "padding": box(10, 0, 10, 0), "padding_mobile": box(18, 0, 0, 34)},
      [tl_point(*p) for p in POINTS]),
    html(TL_CSS),
])

sec1 = find(d, "ig1001")
btn_wrap = find(d, "ig1050")
btn = find(d, "ig1051")["settings"]
btn["link"]["url"] = f"{SITE}/le-societa-del-gruppo/"
btn_wrap["settings"].update({"flex_align_items": "center", "flex_justify_content": "center",
                             "padding": box(24, 0, 0, 0), "padding_mobile": box(18, 0, 0, 0)})
btn_wrap["settings"]["flex_direction"] = "row"
sec1["elements"] = [find(d, "ig1010"), timeline, btn_wrap]

# ------------------------------------------------------------ CERTIFICAZIONI E ATTESTATI (bozza con placeholder)
def cert_card(n):
    return C({"content_width": "full", "flex_align_items": "center", "flex_gap": gap(14), "flex_gap_mobile": gap(12),
              "background_background": "classic", "background_color": "#FFFFFF", "border_radius": radius(24),
              "padding": box(34, 22, 30, 22), "padding_mobile": box(28, 18, 24, 18),
              "box_shadow_box_shadow_type": "yes",
              "box_shadow_box_shadow": {"horizontal": 0, "vertical": 20, "blur": 50, "spread": -26, "color": "rgba(9,23,31,.22)"},
              "custom_css": ("selector { width: calc(25% - 18px) !important; flex: 0 0 calc(25% - 18px) !important; }\n"
                             "@media(max-width:1024px){ selector { width: calc(50% - 12px) !important; flex: 0 0 calc(50% - 12px) !important; } }\n"
                             "@media(max-width:600px){ selector { width: 100% !important; flex: 0 0 100% !important; } }")}, [
        C({"content_width": "full", "flex_align_items": "center", "flex_justify_content": "center",
           "border_radius": radius(999), "border_border": "dashed", "border_width": box(2), "border_color": "#B7C3CB",
           "background_background": "classic", "background_color": LIGHT,
           "custom_css": "selector{width:124px!important;height:124px!important;flex:0 0 124px!important;}"}, [
            W("icon", {"selected_icon": {"value": "fas fa-award", "library": "fa-solid"}, "primary_color": BLUE, "size": px(34)}),
            W("text-editor", {"editor": "<p>Badge in arrivo</p>", "text_color": "#7A8C98", "align": "center",
                              **typo(11.5, 700, ls=0.6), "custom_css": "selector p{margin:0;}"}),
        ]),
        heading(f"Certificazione {n:02d}", NAVY, 19, "h3", 800, lh=1.3, align="center"),
        W("text-editor", {"editor": "<p>Placeholder — nome e logo definitivi forniti dal cliente</p>",
                          "text_color": "#7A8C98", "align": "center", **typo(14, 500, lh=1.5)}),
    ])


certs = section("sec-certificazioni", "certificazioni", "#FFFFFF", [
    inner_boxed([eyebrow("Qualità e conformità", BLUE),
                 h2("Certificazioni e " + grad("Attestati"), NAVY, 48, 30, maxw=820),
                 para("Gli attestati e le certificazioni di sistema che accompagnano l'attività delle società del Gruppo.",
                      BODY, 18.5, 300, 1.6, maxw=720)]),
    C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_direction_mobile": "column",
       "flex_wrap": "wrap", "flex_gap": gap(24), "flex_gap_mobile": gap(18),
       "padding": box(52, 0, 0, 0), "padding_mobile": box(30, 0, 0, 0)}, [cert_card(i) for i in range(1, 5)]),
], pad=(110, 24, 110, 24))

# ------------------------------------------------------------ assemblaggio: hero, il gruppo + timeline, certificazioni, metodo (invariato salvo testi)
out = [find(d, "igh0001"), sec1, certs, find(d, "ig2001")]
for e in out:
    e["settings"]["margin"] = box(0)
find(d, "ig2031")["settings"]["link"]["url"] = "#contatti"
import build_home as _bh  # stesso stile schede della Home (sezioni scure coerenti)
_ts = find(d, "ig2ta1")["settings"]
_hs = find(_bh.out, "chs0ta1") or None
_ts.update({"tab_color": "rgba(238,246,250,.78)", "tab_active_color": NAVY,
            "custom_css": find([_bh.modello], "chs0ta1")["settings"]["custom_css"]})
for t in find(d, "ig2ta1")["settings"]["tabs"]:
    t["tab_content"] = scale_inline_px(t["tab_content"], {12.0: 14, 24.0: 30, 15.5: 18, 15.0: 17.5})

if __name__ == "__main__":
    dump(out, "ilgruppo-55")
    for i, e in enumerate(out):
        open(f"build/ilgruppo-55.s{i}.json", "w", encoding="utf-8").write(json.dumps([e], ensure_ascii=False, separators=(",", ":")))
