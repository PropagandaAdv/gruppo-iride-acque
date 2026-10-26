"""Nuove pagine: Modello operativo, News, Lavora con noi."""
import re
from lib import *
import build_societa as soc
import build_ilgruppo as ig

BASE_HERO = soc.out[0]["elements"][0]["settings"]["html"]


def make_hero(hid, kicker, h1, subtitle=None):
    hh = BASE_HERO.replace("bhHeroSocieta", hid)
    hh = hh.replace('<span class="hero-kicker">Il Gruppo</span>', f'<span class="hero-kicker">{kicker}</span>')
    hh = hh.replace('<h1 class="hero-h1">Le società del Gruppo</h1>',
                    f'<h1 class="hero-h1">{h1}</h1>' + (f'\n      <p class="hero-subtitle">{subtitle}</p>' if subtitle else ""))
    hh = hh.replace("</style>", ".brand-hero .hero-subtitle{color:rgba(238,246,250,.86);font-size:20px;line-height:1.65;max-width:760px;"
                                "margin:26px 0 0;font-family:'Montserrat',sans-serif;font-weight:300;}\n</style>", 1)
    assert hid in hh and kicker in hh
    return C({"css_id": f"sec-{hid}", "content_width": "full", "padding": box(0), "margin": box(0)},
             [W("html", {"html": hh})], inner=False)


# ======================================================================= MODELLO OPERATIVO
# i contenuti delle 4 fasi arrivano dal blocco metodo de Il Gruppo (testi già approvati)
metodo_sec = ig.out[3]
tabs_src = None
for e in [metodo_sec]:
    def walk(x):
        global tabs_src
        if x.get("widgetType") == "tabs":
            tabs_src = x
        for c in x.get("elements", []):
            walk(c)
    walk(e)
intro = metodo_sec["elements"][0]["elements"][2]["settings"]["editor"]
intro_text = re.sub(r"</?p>", "", intro)

CHECK = ('<span style="position:absolute;left:0;top:.15em;width:22px;height:22px;border-radius:50%;background:#4AB7D5;color:#09171F;'
         'font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center;line-height:1;">&#10003;</span>')
SHORT = ["Analisi di processo", "Progettazione e ingegneria", "Construction &amp; Commissioning", "Operation &amp; Maintenance"]
new_tabs = []
for i, t in enumerate(tabs_src["settings"]["tabs"], start=1):
    c = t["tab_content"]
    c = re.sub(r'<span style="position:absolute;left:0;top:\.5em;width:8px;height:8px;border-radius:2px;background:linear-gradient\(135deg,#4AB7D5,#1A4D6A\);"></span>', CHECK, c)
    c = c.replace("padding-left:26px", "padding-left:34px").replace("display:grid;gap:12px;", "display:grid;gap:14px;")
    c = c.replace('<p style="color:#4AB7D5;font-weight:700;font-size:14px;letter-spacing:.12em;text-transform:uppercase;margin:0 0 10px;font-family:Montserrat,sans-serif;">',
                  '<p style="color:#1A4D6A;font-weight:800;font-size:14px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 10px;font-family:Montserrat,sans-serif;">')
    new_tabs.append({"_id": f"mo{i:05d}", "tab_title": f"0{i}  {SHORT[i-1]}", "tab_content": c})

DEEPLINK = """<script>
(function(){
  function go(scroll){
    var m=(location.hash||'').match(/fase-([1-4])/); if(!m) return;
    var w=document.getElementById('metodo-fasi'); if(!w) return;
    var sel='[data-tab="'+m[1]+'"]';
    var t=w.querySelector('.elementor-tab-desktop-title'+sel), tm=w.querySelector('.elementor-tab-mobile-title'+sel);
    var target=(window.innerWidth>767?t:tm)||t;
    if(target && !target.classList.contains('elementor-active')) target.click();
    if(scroll) setTimeout(function(){ window.scrollTo({top: w.getBoundingClientRect().top + window.pageYOffset - 70, behavior:'smooth'}); },150);
  }
  window.addEventListener('load',function(){ setTimeout(function(){go(true);},350); });
  window.addEventListener('hashchange',function(){go(true);});
})();
</script>"""

TABS_H_CSS = (
    "selector .elementor-tabs-wrapper { display:flex!important; flex-wrap:wrap; gap:12px; margin-bottom:22px; }\n"
    "selector .elementor-tab-desktop-title { padding: 18px 26px !important; border-radius: 999px !important; background:#FFFFFF !important; border:0!important; box-shadow:0 10px 30px -18px rgba(9,23,31,.35); transition: background .3s ease, color .3s ease; }\n"
    "selector .elementor-tab-desktop-title:hover { background:#DDEFF6 !important; }\n"
    "selector .elementor-tab-desktop-title.elementor-active { background:#09171F !important; }\n"
    "selector .elementor-tab-title .iah-tabnum { color:#4AB7D5; font-weight:800; margin-right:6px; }\n"
    "selector .elementor-tab-desktop-title::before, selector .elementor-tab-desktop-title::after { display:none!important; }\n"
    "selector .elementor-tabs-content-wrapper { background:#FFFFFF !important; border-radius:28px !important; padding:56px !important; border:0!important; box-shadow:0 30px 70px -30px rgba(9,23,31,.3); }\n"
    "selector .elementor-tab-content { border:0!important; }\n"
    "selector .elementor-tab-mobile-title { color:#09171F!important; background:#EEF6FA!important; border-radius:14px; margin-bottom:8px; border:0!important; }\n"
    "selector .elementor-tab-mobile-title.elementor-active { background:#4AB7D5!important; }\n"
    "@media(max-width:767px){ selector .elementor-tabs-content-wrapper{ padding:24px !important; } }"
)

metodo_page = [
    make_hero("bhHeroMetodo", "Modello operativo", 'Un processo strutturato in <span class="accent">quattro fasi</span>', intro_text),
    section("sec-metodo-fasi", "metodo-fasi", LIGHT, [
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_gap": gap(0), "flex_gap_mobile": gap(0)}, [
            W("tabs", {"type": "horizontal", "tabs": new_tabs, "tab_color": NAVY, "tab_active_color": "#FFFFFF",
                       "background_color": "transparent", "border_width": box(0),
                       **typo(17, 700, prefix="tab_typography"), "content_color": BODY,
                       **typo(17.5, 400, prefix="content_typography"), "custom_css": TABS_H_CSS}),
            html(DEEPLINK, {"_css_classes": "iah-global"}),
            C({"content_width": "full", "flex_direction": "row", "flex_justify_content": "center",
               "padding": box(48, 0, 0, 0), "padding_mobile": box(30, 0, 0, 0)}, [
                button("Richiedi un'analisi tecnica preliminare del tuo impianto →", "#contatti", "solid", 17.5),
            ]),
        ]),
    ], pad=(100, 24, 110, 24)),
]

# ======================================================================= NEWS
NEWS_GROUP = [
    ("Credem Euromobiliare Private Asset SGR investe 3 milioni di euro in Iride Acque",
     "L'investimento sostiene il percorso di crescita industriale del Gruppo e accompagna l'acquisizione di Bieffe Costruzioni, ampliando ulteriormente le competenze e la capacità realizzativa nel settore delle infrastrutture idriche.",
     "L'operazione rappresenta una nuova tappa nel percorso di sviluppo del Gruppo, già avviato con l'ingresso di Biemme Engineering."),
    ("Bieffe Costruzioni entra nel Gruppo Iride Acque",
     "Con l'acquisizione di Bieffe Costruzioni, il Gruppo amplia il proprio perimetro operativo verso acquedotti, reti idriche e fognarie, impianti di depurazione e opere infrastrutturali per multiutility ed enti pubblici.",
     "L'integrazione rafforza la capacità del Gruppo di seguire il progetto dalla fase di ingegneria fino alla realizzazione, al revamping e alla manutenzione delle infrastrutture."),
    ("EMER – Dropnet vince il PMI Award 2026",
     "Il progetto EMER – Dropnet di Iride Acque è stato premiato nell'ambito del PMI Award 2026, promosso dall'Osservatorio Innovazione Digitale nelle PMI della School of Management del Politecnico di Milano.",
     "Il riconoscimento valorizza l'integrazione tra tecnologia di trattamento, economia circolare e digitalizzazione della gestione degli impianti attraverso un software proprietario di telecontrollo e telegestione da remoto."),
    ("Il Gruppo Iride Acque apre la nuova sede operativa di Arosio",
     "Iride Acque e Biemme Engineering si trasferiscono nella nuova sede operativa di Via Buonarroti 3 ad Arosio, con spazi dedicati anche alle attività di Bieffe Costruzioni.",
     "La sede, con una superficie complessiva di circa 2.200 m², comprende ampi uffici, magazzino e officina ed è stata progettata per accompagnare la crescita del Gruppo e favorire una collaborazione sempre più integrata tra le diverse competenze."),
]
NEWS_COMPANIES = [
    ("Iride Acque", "Approfondimenti su trattamento delle acque industriali, tecnologie proprietarie, Ricerca &amp; Sviluppo, recupero e riutilizzo delle acque, contaminanti emergenti e Case Studies applicativi.",
     "Scopri le news di Iride Acque →", "https://irideacque.com/"),
    ("Biemme Engineering", "News e approfondimenti su trattamento delle acque di processo, potabilizzazione, disinfezione, sistemi di dosaggio e controllo, Food &amp; Beverage e hospitality.",
     "Scopri le news di Biemme Engineering →", "https://www.biemmeengineering.it/"),
    ("Bieffe Costruzioni", "Aggiornamenti su cantieri, infrastrutture idriche, reti acquedottistiche e fognarie, impianti di depurazione, manutenzione e progetti per multiutility ed enti pubblici.",
     "Scopri le news di Bieffe Costruzioni →", "https://costruzionibieffe.it/"),
]

CARD = lambda pct, extra="": ("selector { width: calc(" + pct + ") !important; flex: 0 0 calc(" + pct + ") !important; }\n"
                              "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } }" + extra)


def news_card(i, title, p1, p2):
    return C({"content_width": "full", "flex_gap": gap(16), "flex_gap_mobile": gap(14),
              "background_background": "classic", "background_color": "#FFFFFF", "border_radius": radius(28),
              "padding": box(40, 38, 40, 38), "padding_mobile": box(28, 22, 28, 22),
              "box_shadow_box_shadow_type": "yes",
              "box_shadow_box_shadow": {"horizontal": 0, "vertical": 24, "blur": 60, "spread": -28, "color": "rgba(9,23,31,.28)"},
              "custom_css": CARD("50% - 14px")}, [
        W("text-editor", {"editor": f"<p>News di Gruppo · 0{i}</p>", "text_color": ACC, **typo(14, 800, ls=1.2)}),
        heading(title, NAVY, 26, "h3", 800, lh=1.25, mobile=22),
        para(p1, BODY, 17.5, 400, 1.7),
        para(p2, BODY, 17.5, 400, 1.7),
        C({"content_width": "full", "flex_direction": "row", "padding": box(6, 0, 0, 0), "padding_mobile": box(4, 0, 0, 0)}, [
            button("Leggi la news →", "#", "outline", 16),
        ]),
    ])


def company_card(name, desc, cta, url):
    return C({"content_width": "full", "flex_gap": gap(16), "flex_gap_mobile": gap(14),
              "background_background": "classic", "background_color": PANEL, "border_radius": radius(28),
              "padding": box(38, 34, 38, 34), "padding_mobile": box(28, 22, 28, 22),
              "custom_css": CARD("33.333% - 16px")}, [
        heading(name, "#FFFFFF", 26, "h3", 800, lh=1.25, mobile=22),
        para(desc, "rgba(238,246,250,.85)", 17, 300, 1.7),
        C({"content_width": "full", "flex_direction": "row", "padding": box(6, 0, 0, 0), "padding_mobile": box(4, 0, 0, 0),
           "custom_css": "selector{margin-top:auto;}"}, [
            button(cta, url, "outline-light", 15.5, external=True),
        ]),
    ])


news_page = [
    make_hero("bhHeroNews", "News", 'Media &amp; <span class="accent">Awards</span>'),
    section("sec-news-gruppo", "news-gruppo", LIGHT, [
        inner_boxed([eyebrow("News di Gruppo", BLUE),
                     h2("Le novità del Gruppo Iride Acque", NAVY, 46, 29, maxw=900)]),
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_direction_mobile": "column",
           "flex_wrap": "wrap", "flex_gap": gap(28), "flex_gap_mobile": gap(20),
           "padding": box(48, 0, 0, 0), "padding_mobile": box(28, 0, 0, 0)},
          [news_card(i, *n) for i, n in enumerate(NEWS_GROUP, start=1)]),
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_justify_content": "center",
           "padding": box(48, 0, 0, 0), "padding_mobile": box(30, 0, 0, 0)}, [
            button("Scopri tutte le News di Gruppo →", "#", "solid", 17),
        ]),
    ], pad=(110, 24, 110, 24)),
    section("sec-news-aziende", "news-aziende", NAVY, [
        inner_boxed([eyebrow("News dalle Aziende", ACC2),
                     h2("Dalle società del " + grad("Gruppo"), "#FFFFFF", 46, 29, maxw=900)]),
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_direction_mobile": "column",
           "flex_wrap": "wrap", "flex_gap": gap(24), "flex_gap_mobile": gap(18),
           "padding": box(48, 0, 0, 0), "padding_mobile": box(28, 0, 0, 0)},
          [company_card(*c) for c in NEWS_COMPANIES]),
    ], pad=(110, 24, 110, 24)),
]

# ======================================================================= LAVORA CON NOI
POSTS = {
    "_skin": "cards", "posts_post_type": "post", "posts_include": ["terms"], "posts_include_term_ids": ["7"],
    "posts_orderby": "post_date", "posts_order": "desc",
    "cards_columns": "3", "cards_columns_tablet": "2", "cards_columns_mobile": "1", "cards_posts_per_page": 9,
    "cards_thumbnail": "none", "cards_show_title": "yes", "cards_title_tag": "h3",
    "cards_show_excerpt": "yes", "cards_excerpt_length": 32, "cards_apply_to_custom_excerpt": "yes",
    "cards_meta_data": ["date"], "cards_show_read_more": "yes", "cards_read_more_text": "Scopri la posizione →",
    "cards_show_badge": "", "cards_show_avatar": "",
    "cards_column_gap": px(24), "cards_row_gap": px(24),
    "cards_card_bg_color": "#FFFFFF", "cards_card_border_radius": px(24), "cards_card_padding": px(34),
    "cards_title_color": NAVY, **typo(22, 800, prefix="cards_title_typography"),
    "cards_excerpt_color": BODY, **typo(16.5, 400, lh=1.65, prefix="cards_excerpt_typography"),
    "cards_read_more_color": BLUE, **typo(15.5, 700, prefix="cards_read_more_typography"),
    "cards_meta_color": "#7A8C98",
    "nothing_found_message": "Al momento non ci sono posizioni aperte.",
    "custom_css": ("selector .elementor-post__card{ box-shadow:0 24px 60px -28px rgba(9,23,31,.28)!important; border:0!important; }\n"
                   "selector .elementor-posts-nothing-found{ font:600 19px/1.6 Montserrat,sans-serif; color:#09171F; background:#FFFFFF; "
                   "border-radius:24px; padding:34px 36px; text-align:center; }"),
}

FORM_CV = {
    "form_name": "Candidatura spontanea",
    "form_fields": [
        {"_id": "cv000001", "custom_id": "nome", "field_type": "text", "field_label": "Nome e cognome", "required": "true", "width": "50"},
        {"_id": "cv000002", "custom_id": "email", "field_type": "email", "field_label": "Email", "required": "true", "width": "50"},
        {"_id": "cv000003", "custom_id": "cv", "field_type": "upload", "field_label": "Curriculum vitae (PDF o Word, max 5 MB)",
         "file_types": "pdf,doc,docx", "file_sizes": "5", "attachment_type": "attach", "required": "true", "width": "100"},
        {"_id": "cv000004", "custom_id": "messaggio", "field_type": "textarea", "field_label": "Messaggio",
         "placeholder": "Raccontaci in breve il tuo profilo e l'area in cui ti piacerebbe lavorare", "required": "false", "width": "100", "rows": 5},
        {"_id": "cv000005", "custom_id": "privacy", "field_type": "acceptance",
         "field_label": "Dichiaro di aver letto l'informativa sulla privacy e acconsento al trattamento dei dati ai fini della selezione del personale.",
         "required": "true", "width": "100"},
    ],
    "button_text": "Invia la candidatura", "button_width": "100", "submit_actions": ["email"],
    "email_to": "info@gruppoirideacque.it", "email_subject": "Nuova candidatura spontanea dal sito",
    "email_content": "[all-fields]", "email_from": "email@gruppoirideacque.propagandaadv.com", "email_from_name": "Gruppo Iride Acque",
    "success_message": "Grazie, abbiamo ricevuto la tua candidatura.",
}
import build_global as g

lavora_page = [
    make_hero("bhHeroLavora", "Carriere", 'Lavora <span class="accent">con noi</span>'),
    section("sec-posizioni", "posizioni-aperte", LIGHT, [
        inner_boxed([eyebrow("Opportunità", BLUE), h2("Posizioni aperte", NAVY, 46, 29),
                     para("Le posizioni attualmente aperte nelle società del Gruppo.", BODY, 18.5, 300, 1.6, maxw=720)]),
        C({"content_width": "boxed", "boxed_width": px(1240), "padding": box(44, 0, 0, 0), "padding_mobile": box(26, 0, 0, 0)}, [
            W("posts", POSTS),
        ]),
    ], pad=(110, 24, 110, 24)),
    section("sec-candidatura", "candidatura", NAVY, [
        inner_boxed([eyebrow("Candidatura spontanea", ACC2),
                     h2("Non trovi la posizione adatta? " + grad("Scrivici"), "#FFFFFF", 44, 28, maxw=900)],
                    extra={"padding": box(0, 0, 48, 0), "padding_mobile": box(0, 0, 28, 0)}),
        g.contact_box([
            heading("Inviaci il tuo CV", "#FFFFFF", 28, "h3", 800, mobile=24),
            para("Se non trovi una posizione in linea con il tuo profilo, inviaci una candidatura spontanea: "
                 "la valuteremo per le future opportunità nelle società del Gruppo.",
                 "rgba(238,246,250,.85)", 18, 300, 1.7),
        ], FORM_CV, box_id_form="candidatura-form"),
    ], pad=(110, 24, 110, 24)),
]

if __name__ == "__main__":
    dump(metodo_page, "metodo-new")
    dump(news_page, "news-new")
    dump(lavora_page, "lavora-new")
