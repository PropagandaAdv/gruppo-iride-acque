"""Le società del gruppo (64) — sezione "Le società del Gruppo" del giro modifiche 2026-10-02."""
from lib import *
import build_ilgruppo as ig

# hero: stesso template delle pagine interne (CSS identico a Il Gruppo), cambiano id/testi
hero = deep(ig.out[0])
hh = hero["elements"][0]["settings"]["html"]
start = hh.index("#bhHeroIlGruppo .hero-h1")
end = hh.index("</style>")
hh = hh[:start] + hh[end:]
hh = (hh.replace("bhHeroIlGruppo", "bhHeroSocieta")
        .replace('<span class="hero-kicker">Gruppo Iride Acque</span>', '<span class="hero-kicker">Il Gruppo</span>')
        .replace('<h1 class="hero-h1">Da specialisti verticali a<br class="iah-br"> <span class="accent">piattaforma industriale integrata</span></h1>',
                 '<h1 class="hero-h1">Le società del Gruppo</h1>'))
hh = hh[:hh.index('      <div class="hero-ctas">')] + hh[hh.index("    </div>\n  </div>\n</section>"):]
assert "bhHeroSocieta" in hh and "Le società del Gruppo</h1>" in hh and "hero-ctas\">" not in hh
hero["elements"][0]["settings"]["html"] = hh
hero["settings"]["css_id"] = "sec-societa-hero"

STATEMENT_T = ("Il Gruppo IRIDE ACQUE riunisce società con competenze specialistiche nel trattamento, gestione e riutilizzo delle acque, "
               "capaci di operare in modo integrato su progetti complessi per il settore industriale e pubblico.")
STATEMENT_S = ("Iride Acque, Biemme Engineering e Bieffe Costruzioni integrano competenze specialistiche, ingegneria e capacità esecutiva "
               "per sviluppare soluzioni avanzate per la depurazione delle acque reflue civili e industriali, il loro riutilizzo e il recupero "
               "delle materie valorizzabili in esse contenute, seguendo ogni fase del progetto: dall'analisi alla progettazione, fino alla "
               "realizzazione e manutenzione degli impianti.")

statement = section("sec-societa-intro", "statement", "#FFFFFF", [
    C({"content_width": "boxed", "boxed_width": px(1040), "flex_align_items": "center", "flex_gap": gap(26), "flex_gap_mobile": gap(18)}, [
        heading(STATEMENT_T, NAVY, 34, "h2", 800, lh=1.3, mobile=24, align="center"),
        para(STATEMENT_S, BODY, 19.5, 400, 1.7, align="center", mobile=17),
    ]),
], pad=(110, 24, 40, 24), pad_m=(64, 16, 24, 16))

IMG = lambda n, i: {"url": f"{SITE}/wp-content/uploads/2026/09/{n}", "id": i}
COMPANIES = [
    ("Iride Acque", "Iride Acque costituisce il nucleo di ingegneria di processo del Gruppo, con responsabilità primaria sulle attività di analisi, progettazione e realizzazione impiantistica per gli interventi a maggiore complessità tecnica, in particolare nell'ambito delle soluzioni a Zero Liquid Discharge (ZLD) e degli impianti di recupero e riuso delle acque di processo.",
     "https://irideacque.com/", IMG("settore-industriale-bg.webp", 68), "logo"),
    ("BM Engineering", "BM Engineering rappresenta la componente realizzativa e gestionale del Gruppo, con specializzazione in costruzione impiantistica, automazione elettrostrumentale, service O&amp;M e noleggio di impianti mobili modulari. La società garantisce continuità operativa attraverso presidio tecnico territoriale e capacità di pronto intervento.",
     "https://www.biemmeengineering.it/", IMG("pillar-costruzione-1.webp", 27), "BM Engineering"),
    ("Bieffe Costruzioni", "Bieffe Costruzioni è la società del Gruppo dedicata alla realizzazione di opere infrastrutturali idriche di grande complessità, con particolare specializzazione in cantieristica per multiutility ed enti pubblici. L'ingresso di Bieffe Costruzioni nel perimetro del Gruppo, la seconda acquisizione realizzata nell'arco di un triennio, ha ampliato in modo strutturale la capacità realizzativa disponibile per interventi su reti idriche, opere civili connesse alla gestione della risorsa idrica e commesse di grande scala.",
     "https://costruzionibieffe.it/", IMG("settore-civile-bg.webp", 69), "Bieffe Costruzioni"),
]

BADGE_CSS = ("selector{position:absolute!important;left:24px;bottom:24px;width:auto!important;max-width:calc(100% - 48px);z-index:2;"
             "box-shadow:0 16px 40px -14px rgba(0,0,0,.45);}")


def badge(kind):
    if kind == "logo":
        return C({"content_width": "full", "background_background": "classic", "background_color": "#FFFFFF",
                  "border_radius": radius(18), "padding": box(14, 22, 14, 22), "custom_css": BADGE_CSS}, [
            W("image", {"image": {"url": f"{SITE}/wp-content/uploads/2026/09/logo-iride-acque.png", "id": 15},
                        "image_size": "medium", "width": px(120)}),
        ])
    return C({"content_width": "full", "background_background": "classic", "background_color": NAVY,
              "border_radius": radius(18), "padding": box(14, 22, 14, 22), "flex_gap": gap(2), "custom_css": BADGE_CSS}, [
        W("text-editor", {"editor": f"<p>{kind}</p>", "text_color": "#FFFFFF", **typo(17, 800), "custom_css": "selector p{margin:0;}"}),
        W("text-editor", {"editor": "<p>Logo in attesa dal cliente</p>", "text_color": "rgba(238,246,250,.72)",
                          **typo(12.5, 600, ls=0.4), "custom_css": "selector p{margin:0;}"}),
    ])


def company_row(name, desc, url, img, logo):
    return C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "column",
              "flex_gap": gap(64), "flex_gap_mobile": gap(28), "flex_align_items": "center",
              "animation": "fadeInUp", "animation_duration": "slow"}, [
        C({"content_width": "full", "flex_gap": gap(20), "flex_gap_mobile": gap(16),
           "custom_css": ("selector { width: calc(46% - 32px) !important; flex: 0 0 calc(46% - 32px) !important; }\n"
                          "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; order:2; } }")}, [
            heading(name, NAVY, 40, "h2", 800, lh=1.15, mobile=29),
            para(desc, BODY, 18.5, 400, 1.75, mobile=17),
            C({"content_width": "full", "flex_direction": "row", "padding": box(8, 0, 0, 0), "padding_mobile": box(4, 0, 0, 0)}, [
                button(f"Scopri {name} →", url, "solid", 17, external=True),
            ]),
        ]),
        C({"content_width": "full", "background_background": "classic", "background_image": img,
           "background_position": "center center", "background_size": "cover", "border_radius": radius(28),
           "min_height": px(460), "min_height_mobile": px(300), "padding": box(0),
           "custom_css": ("selector { position:relative; overflow:hidden; width: calc(54% - 32px) !important; flex: 0 0 calc(54% - 32px) !important; }\n"
                          "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; order:1; } }")}, [
            badge(logo),
        ]),
    ])


companies = section("sec-societa-blocchi", "societa", "#FFFFFF", [
    C({"content_width": "boxed", "boxed_width": px(1240), "flex_gap": gap(110), "flex_gap_mobile": gap(64)},
      [company_row(*c) for c in COMPANIES]),
], pad=(70, 24, 120, 24), pad_m=(40, 16, 72, 16))

out = [hero, statement, companies]

if __name__ == "__main__":
    dump(out, "societa-64")
    for i, e in enumerate(out):
        open(f"build/societa-64.s{i}.json", "w", encoding="utf-8").write(json.dumps([e], ensure_ascii=False, separators=(",", ":")))
