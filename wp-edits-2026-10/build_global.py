"""Header #39 e Footer #42 (template globali Elementor) — giro modifiche call 2026-10-02."""
from lib import *

LOGO = {"url": f"{SITE}/wp-content/uploads/2026/09/logo-iride-acque.png", "id": 15}

# ---------------------------------------------------------------- HEADER
HEADER_CODE = """<style>
html{scroll-padding-top:110px;}
.elementor .e-con.e-parent + .e-con.e-parent,.elementor-location-footer .e-con.e-parent{margin-top:-1px!important;}
.iah-global{position:absolute!important;width:0!important;height:0!important;overflow:hidden!important;margin:0!important;padding:0!important;}
.iah-header{position:fixed!important;top:var(--wp-admin--admin-bar--height,0px)!important;left:0;right:0;width:100%!important;max-width:100%!important;z-index:999!important;background-color:transparent!important;transition:background-color .45s ease,box-shadow .45s ease,backdrop-filter .45s ease;}
.iah-header.iah-scrolled{background-color:rgba(9,23,31,.86)!important;-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);box-shadow:0 12px 32px -20px rgba(0,0,0,.55);}
.iah-header .elementor-nav-menu--main .elementor-item{white-space:nowrap;}
.iah-header .iah-brand-text .elementor-heading-title{white-space:nowrap;}
.iah-header .elementor-nav-menu--dropdown{border-radius:0 0 18px 18px;overflow:hidden;}
@media(max-width:1400px){.iah-header .elementor-nav-menu--main .elementor-item{padding-left:9px!important;padding-right:9px!important;font-size:14.5px!important;}.iah-header .iah-cta .elementor-button{font-size:13.5px!important;padding:12px 18px!important;}}
@media(max-width:1240px){.iah-header .iah-cta{display:none!important;}}
.brand-hero{min-height:100vh!important;}
.brand-hero .bh-copy{padding-top:120px!important;padding-bottom:64px!important;}
.brand-hero .hero-kicker{font-size:15px!important;}
.brand-hero .hero-h1{font-size:clamp(2.6rem,5.6vw,4.9rem)!important;}
.brand-hero .hero-h1 .accent{background:none!important;color:#5CCBEB!important;-webkit-text-fill-color:#5CCBEB!important;}
.brand-hero .hero-subtitle{font-size:20px!important;}
@media(max-width:767px){.brand-hero .bh-copy{padding-top:100px!important;}.brand-hero .hero-h1{font-size:clamp(2.1rem,9vw,2.8rem)!important;}}
</style>
<script>
(function(){
  function run(){
    var h=document.querySelector('.iah-header');
    if(!h) return;
    function u(){ h.classList.toggle('iah-scrolled', window.scrollY>40); }
    u();
    window.addEventListener('scroll', u, {passive:true});
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',run);}else{run();}
})();
</script>"""

header = [C({
    "css_id": "sec-header", "_css_classes": "iah-header", "content_width": "full",
    "flex_direction": "row", "flex_direction_tablet": "row", "flex_direction_mobile": "row",
    "flex_align_items": "center", "flex_justify_content": "space-between",
    "flex_gap": gap(28), "flex_gap_mobile": gap(12),
    "padding": box(22, 40, 22, 40), "padding_tablet": box(16, 24, 16, 24), "padding_mobile": box(12, 16, 12, 16),
    "z_index": 999,
}, [
    html(HEADER_CODE, {"_css_classes": "iah-global"}),
    C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "row",
       "flex_align_items": "center", "flex_gap": gap(14), "flex_gap_mobile": gap(10),
       "width": {"unit": "%", "size": ""}, "_flex_size": "none", "flex_shrink": 0,
       "custom_css": "selector{flex:0 0 auto!important;width:auto!important;}"}, [
        W("image", {"image": LOGO, "image_size": "medium", "width": px(72), "width_tablet": px(60), "width_mobile": px(48),
                    "link_to": "custom", "link": {"url": f"{SITE}/", "is_external": "", "nofollow": ""}}),
        W("heading", {"title": "IRIDE ACQUE", "header_size": "span", "title_color": "#FFFFFF", "_css_classes": "iah-brand-text",
                      "link": {"url": f"{SITE}/", "is_external": "", "nofollow": ""},
                      **typo(28, 800, lh=1, mobile=19, ls=0.3)}),
    ]),
    C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "row",
       "flex_align_items": "center", "flex_justify_content": "flex-end",
       "custom_css": "selector{flex:1 1 auto!important;width:auto!important;}"}, [
        W("nav-menu", {"menu_name": "Menu", "menu": "main", "layout": "horizontal", "align_items": "end",
                       "pointer": "underline", "animation_line": "fade", "dropdown": "tablet", "full_width": "stretch",
                       "toggle": "burger", "toggle_align": "right",
                       "color_menu_item": "#FFFFFF", "color_menu_item_hover": ACC2, "pointer_color_menu_item_hover": ACC2,
                       "color_menu_item_active": ACC2, "pointer_color_menu_item_active": ACC2,
                       "padding_horizontal_menu_item": px(13), "padding_vertical_menu_item": px(10),
                       **typo(15.5, 600, prefix="menu_typography"),
                       "color_dropdown_item": "#FFFFFF", "background_color_dropdown_item": NAVY,
                       "color_dropdown_item_hover": NAVY, "background_color_dropdown_item_hover": ACC2,
                       "color_dropdown_item_active": ACC2, "background_color_dropdown_item_active": NAVY,
                       "padding_horizontal_dropdown_item": px(24), "padding_vertical_dropdown_item": px(16),
                       **typo(17, 600, prefix="dropdown_typography"),
                       "dropdown_top_distance": px(14),
                       "toggle_color": "#FFFFFF", "toggle_background_color": "rgba(255,255,255,0.08)",
                       "toggle_size": px(24), "toggle_border_radius": px(12)}),
    ]),
    W("button", {"text": "Richiedi una valutazione tecnica", "_css_classes": "iah-cta",
                 "link": {"url": "#contatti", "is_external": "", "nofollow": ""},
                 "background_color": ACC, "button_text_color": NAVY,
                 "button_background_hover_color": ACC2, "hover_color": NAVY,
                 "border_radius": radius(999), **typo(14.5, 700, mobile=13),
                 "text_padding": box(13, 22, 13, 22), "hide_tablet": "hidden-tablet", "hide_mobile": "hidden-mobile"}),
], inner=False)]

# ---------------------------------------------------------------- FOOTER
FORM_HOME = {
    "form_name": "Valutazione tecnica Homepage",
    "form_fields": [
        {"_id": "f0000001", "custom_id": "nome", "field_label": "Nome e cognome", "required": "true", "width": "50"},
        {"_id": "f0000002", "custom_id": "azienda", "field_label": "Azienda", "required": "true", "width": "50"},
        {"_id": "f0000003", "custom_id": "email", "field_type": "email", "field_label": "Email", "required": "true", "width": "50"},
        {"_id": "f0000004", "custom_id": "telefono", "field_type": "tel", "field_label": "Telefono", "required": "false", "width": "50"},
        {"_id": "f0000005", "custom_id": "settore", "field_label": "Settore", "placeholder": "es. Manifatturiero, Food, Farmaceutico...", "required": "false"},
        {"_id": "f0000006", "custom_id": "tipologia", "field_type": "select", "field_label": "Tipologia di richiesta",
         "field_options": "Nuovo impianto\nRevamping / potenziamento\nTrattamento delle acque industriali\nRecupero e riutilizzo delle acque\nManutenzione e assistenza\nServizio Idrico Integrato\nAltro",
         "placeholder": "Seleziona...", "required": "false"},
        {"_id": "f0000007", "custom_id": "messaggio", "field_type": "textarea", "field_label": "Descrizione breve",
         "placeholder": "Tipologia di refluo, portata indicativa, obiettivo dell'intervento...", "required": "false"},
        {"_id": "f0000008", "custom_id": "privacy", "field_type": "acceptance",
         "field_label": "Dichiaro di aver letto l'informativa sulla privacy e acconsento al trattamento dei dati ai fini del contatto da parte del Gruppo Iride Acque.",
         "required": "true"},
    ],
    "button_text": "Invia la richiesta di valutazione tecnica",
    "submit_actions": ["email"],
    "email_to": "info@gruppoirideacque.it",
    "email_subject": "Nuova richiesta di valutazione tecnica dalla homepage",
    "email_content": "[all-fields]",
    "email_from": "email@gruppoirideacque.propagandaadv.com",
    "email_from_name": "Gruppo Iride Acque",
    "email_to_2": "info@propagandaadv.com",
    "email_subject_2": "Nuovo messaggio da \"\"",
    "email_content_2": "[all-fields]",
    "email_from_2": "email@gruppoirideacque.propagandaadv.com",
    "email_from_name_2": "Gruppo Iride Acque",
    "email_reply_to_2": "info@propagandaadv.com",
    "success_message": "L&#039;invio è avvenuto con successo.",
    "error_message": "L&#039;invio non è andato a buon fine a causa di un errore.",
    "server_message": "L&#039;invio non è andato a buon fine a causa di un errore del server.",
    "invalid_message": "L&#039;invio non è andato a buon fine perché il modulo non è valido.",
    "required_field_message": "Questo campo è obbligatorio.",
    "step_next_label": "Successivo", "step_previous_label": "Precedente",
}

FORM_STYLE = {
    "button_background_color": ACC, "button_text_color": NAVY,
    "button_background_hover_color": ACC2, "button_hover_color": NAVY,
    "button_border_radius": radius(999), "button_text_padding": box(17, 30, 17, 30),
    **typo(17, 700, prefix="button_typography"), "button_hover_animation": "float",
    "input_size": "lg", "column_gap": {"unit": "px", "size": 16, "sizes": []}, "row_gap": {"unit": "px", "size": 22, "sizes": []},
    "field_text_color": NAVY, "label_color": "#FFFFFF", "field_background_color": "rgba(255,255,255,.95)",
    "field_border_radius": radius(14), "field_border_width": box(0), "field_border_color": "transparent",
    **typo(17, 400, prefix="field_typography"), **typo(15, 600, prefix="label_typography"),
    "custom_css": ("selector .elementor-field-textual { padding: 15px 18px !important; }\n"
                   "selector textarea.elementor-field-textual { min-height: 120px !important; }\n"
                   "selector select.elementor-field-textual { padding: 15px 18px !important; }\n"
                   "selector .elementor-field-label { margin-bottom: 7px !important; }\n"
                   "selector .elementor-field-subgroup label { color: rgba(255,255,255,.88) !important; font-size:15px; }\n"
                   "selector .elementor-field-subgroup a { color: #8DD6E8 !important; }"),
}

STEP_CIRCLE_CSS = ("selector{width:42px!important;height:42px!important;flex:0 0 42px!important;"
                   "display:flex!important;align-items:center!important;justify-content:center!important;}\n"
                   "selector .elementor-widget-text-editor{width:auto!important;margin:0!important;}\n"
                   "selector p{margin:0!important;line-height:1!important;}")


def step_row(n, text, circle_bg=ACC2, text_color="rgba(238,246,250,.9)"):
    return C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "row",
              "flex_gap": gap(18), "flex_gap_mobile": gap(14), "flex_align_items": "center"}, [
        C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "row",
           "flex_align_items": "center", "flex_justify_content": "center",
           "background_background": "classic", "background_color": circle_bg,
           "border_radius": radius(999), "custom_css": STEP_CIRCLE_CSS}, [
            W("text-editor", {"editor": f"<p>{n}</p>", "text_color": NAVY, "align": "center", **typo(17, 800)}),
        ]),
        para(text, text_color, 17.5, 400, 1.6),
    ])


def contact_box(left_children, form_settings, box_id_form="contatti-form"):
    return C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_direction_mobile": "column",
              "flex_gap": gap(64), "flex_gap_mobile": gap(36), "flex_align_items": "flex-start",
              "background_background": "classic", "background_color": PANEL, "border_radius": radius(32),
              "padding": box(60, 60, 60, 60), "padding_mobile": box(32, 22, 36, 22)}, [
        C({"content_width": "full", "flex_gap": gap(24), "flex_gap_mobile": gap(18),
           "custom_css": ("selector { width: calc(42% - 27px) !important; flex: 0 0 calc(42% - 27px) !important; }\n"
                          "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } }")},
          left_children),
        C({"content_width": "full", "_element_id": box_id_form, "padding": box(0),
           "custom_css": ("selector { width: calc(58% - 37px) !important; flex: 0 0 calc(58% - 37px) !important; }\n"
                          "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } }")},
          [W("form", {**form_settings, **FORM_STYLE})]),
    ])


link_css = "color: rgba(238,246,250,0.78); text-decoration: none;"


def links(items):
    out = ""
    for label, url, ext in items:
        t = ' target="_blank" rel="noopener"' if ext else ""
        out += f'<p><a style="{link_css}" href="{url}"{t}>{label}</a></p>'
    return out


def footer_col(title, body_html, pct, pct_tablet=50):
    return C({"content_width": "full", "flex_gap": gap(12), "flex_gap_mobile": gap(10),
              "custom_css": (f"selector {{ width: calc({pct}% - 30px) !important; flex: 0 0 calc({pct}% - 30px) !important; }}\n"
                             f"@media(max-width:1024px){{ selector {{ width: calc({pct_tablet}% - 20px) !important; flex: 0 0 calc({pct_tablet}% - 20px) !important; }} }}\n"
                             "@media(max-width:767px){ selector { width: 100% !important; flex: 0 0 100% !important; } }")}, [
        heading(title, "#FFFFFF", 17, "h4", 700),
        W("text-editor", {"editor": body_html, **typo(16, 400, lh=2.0)}),
    ])


MAPS_EMBED = ('<iframe src="https://www.google.com/maps?q=IRIDE+ACQUE+SB+spa,+Via+Michelangelo+Buonarroti+3,+22060+Arosio+CO&output=embed" '
              'width="100%" height="300" style="border:0;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" '
              'title="Mappa: Iride Acque SB S.p.A. - Via Michelangelo Buonarroti, 3, 22060 Arosio CO"></iframe>')
MAPS_DIR = "https://www.google.com/maps/dir/?api=1&destination=IRIDE+ACQUE+SB+spa,+Via+Michelangelo+Buonarroti+3,+22060+Arosio+CO"

home_left = [
    heading("Parla con un nostro tecnico", "#FFFFFF", 27, "h3"),
    para("Descrivi il tuo contesto tecnico-produttivo: un ingegnere di processo del Gruppo prenderà in carico la richiesta e ti ricontatterà per un primo confronto tecnico.",
         "rgba(238,246,250,.85)", 18.5, 300, 1.7),
    C({"content_width": "full", "flex_gap": gap(20), "flex_gap_mobile": gap(16), "padding": box(6, 0, 0, 0)}, [
        step_row(1, "Un ingegnere di processo del Gruppo prende in carico la richiesta."),
        step_row(2, "Segue un colloquio tecnico preliminare, senza alcun impegno, per approfondire contesto e obiettivi."),
        step_row(3, "Ove utile, viene proposto un sopralluogo tecnico per il rilievo diretto delle condizioni impiantistiche."),
    ]),
    C({"content_width": "full", "flex_direction": "row", "padding": box(12, 0, 0, 0)}, [
        button("Vai alla richiesta di valutazione →", "#contatti-form", "solid", 17),
    ]),
]

footer = [
    section("sec-contatti", "contatti", NAVY, [
        inner_boxed([eyebrow("Contatti", ACC2),
                     h2("Richiedi una " + grad("valutazione tecnica"), "#FFFFFF", 46, 30)],
                    extra={"padding": box(0, 0, 52, 0), "padding_mobile": box(0, 0, 30, 0)}),
        contact_box(home_left, FORM_HOME),
    ], pad=(110, 24, 90, 24), pad_m=(70, 16, 56, 16)),
    section("sec-footer", None, NAVY, [
        inner_boxed([
            C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "column", "flex_wrap": "wrap",
               "flex_gap": gap(40), "flex_gap_mobile": gap(30)}, [
                C({"content_width": "full", "flex_gap": gap(16),
                   "custom_css": ("selector { width: calc(31% - 30px) !important; flex: 0 0 calc(31% - 30px) !important; }\n"
                                  "@media(max-width:1024px){ selector { width: calc(50% - 20px) !important; flex: 0 0 calc(50% - 20px) !important; } }\n"
                                  "@media(max-width:767px){ selector { width: 100% !important; flex: 0 0 100% !important; } }")}, [
                    W("image", {"image": LOGO, "image_size": "medium", "width": px(58), "align": "left"}),
                    para("Il Gruppo Iride Acque progetta, realizza e gestisce impianti per il trattamento, il recupero e il riuso delle acque industriali e civili.",
                         "rgba(238,246,250,0.75)", 16, 300, 1.65),
                ]),
                footer_col("Gruppo", links([
                    ("Il Gruppo", f"{SITE}/il-gruppo/", False),
                    ("Le società del Gruppo", f"{SITE}/le-societa-del-gruppo/", False),
                    ("Tecnologie e Servizi", f"{SITE}/tecnologie-e-servizi/", False),
                    ("Modello operativo", f"{SITE}/modello-operativo/", False),
                    ("News", f"{SITE}/news/", False),
                    ("Lavora con noi", f"{SITE}/lavora-con-noi/", False),
                    ("Contatti", f"{SITE}/contatti/", False),
                ]), 23),
                footer_col("Società", links([
                    ("Iride Acque", "https://irideacque.com/", True),
                    ("Biemme Engineering", "https://www.biemmeengineering.it/", True),
                    ("Bieffe Costruzioni", "https://costruzionibieffe.it/", True),
                ]), 23),
                footer_col("Documenti",
                           '<p style="color:rgba(238,246,250,0.78);margin:0;">Codice Etico <span style="display:inline-block;margin-left:6px;padding:2px 10px;border-radius:999px;background:rgba(141,214,232,.14);color:#8DD6E8;font-size:12px;font-weight:600;line-height:1.6;">documento in arrivo</span></p>'
                           '<p style="color:rgba(238,246,250,0.78);margin:0;">Condizioni Generali di Acquisto e Vendita <span style="display:inline-block;margin-left:6px;padding:2px 10px;border-radius:999px;background:rgba(141,214,232,.14);color:#8DD6E8;font-size:12px;font-weight:600;line-height:1.6;">documento in arrivo</span></p>',
                           23),
            ]),
            # Dove siamo (spostato dalla pagina Contatti)
            C({"content_width": "full", "_element_id": "dove-siamo", "flex_direction": "row", "flex_direction_mobile": "column",
               "flex_gap": gap(44), "flex_gap_mobile": gap(24), "flex_align_items": "center",
               "background_background": "classic", "background_color": PANEL, "border_radius": radius(28),
               "padding": box(40, 40, 40, 40), "padding_mobile": box(26, 20, 26, 20),
               "margin": box(48, 0, 48, 0), "margin_mobile": box(32, 0, 32, 0)}, [
                C({"content_width": "full", "flex_gap": gap(10),
                   "custom_css": ("selector { width: calc(36% - 22px) !important; flex: 0 0 calc(36% - 22px) !important; }\n"
                                  "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } }")}, [
                    W("text-editor", {"editor": "<p>Dove siamo</p>", "text_color": ACC2, **typo(16, 800, ls=1.4)}),
                    heading("Iride Acque SB S.p.A.", "#FFFFFF", 26, "h3", mobile=22),
                    para("Via Michelangelo Buonarroti, 3<br>22060 Arosio (CO)", "rgba(238,246,250,.85)", 17.5, 400, 1.6),
                    C({"content_width": "full", "flex_direction": "row", "padding": box(14, 0, 0, 0)}, [
                        button("Ottieni indicazioni →", MAPS_DIR, "outline-light", 15.5, external=True),
                    ]),
                ]),
                C({"content_width": "full", "border_radius": radius(20),
                   "custom_css": ("selector { overflow:hidden; width: calc(64% - 22px) !important; flex: 0 0 calc(64% - 22px) !important; }\n"
                                  "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } }")}, [
                    html(MAPS_EMBED),
                ]),
            ]),
            C({"content_width": "full", "flex_gap": gap(8), "border_border": "solid", "border_width": box(1, 0, 0, 0),
               "border_color": "rgba(255,255,255,0.1)", "padding": box(24, 0, 0, 0)}, [
                C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "column", "flex_wrap": "wrap",
                   "flex_justify_content": "space-between", "flex_align_items": "center", "flex_gap": gap(12)}, [
                    W("text-editor", {"editor": "<p>© 2026 Gruppo Iride Acque. Tutti i diritti riservati.</p>",
                                      "text_color": "rgba(238,246,250,0.55)", **typo(14, 300)}),
                    W("text-editor", {"editor": "<p>Privacy · Cookie · Note legali</p>",
                                      "text_color": "rgba(238,246,250,0.55)", **typo(14, 300)}),
                ]),
                W("text-editor", {"editor": "<p>Le immagini e i filmati presenti in questo sito sono realizzati con tecniche di generazione digitale a scopo illustrativo e non ritraggono impianti o strutture reali del Gruppo.</p>",
                                  "text_color": "rgba(238,246,250,0.62)", **typo(13, 300)}),
            ]),
        ], g=0, g_m=0),
    ], pad=(40, 24, 32, 24), pad_m=(24, 16, 24, 16)),
]

if __name__ == "__main__":
    dump(header, "header-39")
    dump(footer, "footer-42")
