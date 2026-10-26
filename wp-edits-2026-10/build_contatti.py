"""Contatti (78) — giro modifiche call 2026-10-02."""
from lib import *
import build_global as g
import build_societa as soc

# hero: template pagine interne, senza sottotitolo
hero = deep(soc.out[0])
hh = hero["elements"][0]["settings"]["html"]
hh = (hh.replace("bhHeroSocieta", "bhHeroContatti")
        .replace('<span class="hero-kicker">Il Gruppo</span>', '<span class="hero-kicker">Contatti</span>')
        .replace('<h1 class="hero-h1">Le società del Gruppo</h1>', '<h1 class="hero-h1">Richiedi una <span class="accent">valutazione tecnica</span></h1>'))
assert "bhHeroContatti" in hh and "valutazione tecnica</span></h1>" in hh and "hero-subtitle\">" not in hh
hero["elements"][0]["settings"]["html"] = hh
hero["settings"]["css_id"] = "sec-contatti-hero"

FORM_CONTATTI = {
    "form_name": "Valutazione tecnica - Pagina Contatti",
    "form_fields": [
        {"_id": "cf000001", "custom_id": "ragione_sociale", "field_type": "text", "field_label": "Ragione Sociale/Referente",
         "placeholder": "Ragione sociale e nominativo del referente tecnico", "required": "true", "width": "100"},
        {"_id": "cf000002", "custom_id": "ruolo", "field_type": "select", "field_label": "Ruolo aziendale",
         "field_options": "Direttore di Stabilimento\nIngegnere di Processo\nHSE Manager\nResponsabile Acquisti\nGestore SII-PA\nDirezione Hospitality\nAltro",
         "placeholder": "Seleziona...", "required": "true", "width": "50"},
        {"_id": "cf000003", "custom_id": "settore", "field_type": "text", "field_label": "Settore",
         "placeholder": "Settore industriale o ambito di attività", "required": "true", "width": "50"},
        {"_id": "cf000004", "custom_id": "descrizione", "field_type": "textarea", "field_label": "Descrizione tecnica",
         "placeholder": "Descrivi sinteticamente l'esigenza tecnica (tipologia di refluo, portata indicativa, parametri di scarico target, criticità normativa in essere, obiettivo dell'intervento)",
         "required": "true", "width": "100", "rows": 5},
        {"_id": "cf000005", "custom_id": "privacy", "field_type": "acceptance",
         "field_label": "Dichiaro di aver letto <a href=\"#\" style=\"color:#8DD6E8;text-decoration:underline;\" target=\"_blank\" rel=\"noopener\">l'informativa sulla privacy</a> e acconsento al trattamento dei dati ai fini del contatto da parte del Gruppo Iride Acque",
         "required": "true", "width": "100"},
    ],
    "button_text": "Invia la richiesta di valutazione tecnica",
    "button_width": "100",
    "submit_actions": ["email"],
    "email_to": "info@gruppoirideacque.it",
    "email_subject": "Nuova richiesta di valutazione tecnica dalla pagina Contatti",
}

ICONS = {
    "clock": '<path d="M12 7v5l3.5 2"/><circle cx="12" cy="12" r="9"/>',
    "chat": '<path d="M4 5h16v11H8l-4 4V5Z"/>',
    "pin": '<path d="M19 10c0 5.5-7 12-7 12s-7-6.5-7-12a7 7 0 1 1 14 0Z"/><circle cx="12" cy="10" r="2.3"/>',
}


def step(n, icon, text):
    tile = ('<div style="width:48px;height:48px;border-radius:14px;background:rgba(141,214,232,.14);display:flex;'
            'align-items:center;justify-content:center;color:#8DD6E8;">'
            f'<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</svg></div>')
    return C({"content_width": "full", "flex_direction": "row", "flex_direction_mobile": "row",
              "flex_gap": gap(16), "flex_gap_mobile": gap(14), "flex_align_items": "flex-start"}, [
        html(tile, {"custom_css": "selector{flex:0 0 48px!important;width:48px!important;}"}),
        para(f'<p><strong style="color:#8DD6E8;font-weight:800;">{n}.</strong> {text}</p>', "rgba(238,246,250,.9)", 17.5, 400, 1.6),
    ])


left = [
    heading("Parla con un nostro tecnico", "#FFFFFF", 30, "h2", 800, mobile=25),
    para("Descrivi il tuo contesto tecnico-produttivo: ecco cosa succede dopo l'invio della richiesta.",
         "rgba(238,246,250,.82)", 18.5, 300, 1.65),
    C({"content_width": "full", "flex_gap": gap(22), "flex_gap_mobile": gap(18), "padding": box(6, 0, 0, 0), "padding_mobile": box(4, 0, 0, 0)}, [
        step(1, "clock", "Un ingegnere di processo del Gruppo prende in carico la richiesta entro 24 ore lavorative."),
        step(2, "chat", "Segue un colloquio tecnico preliminare, finalizzato all'approfondimento del contesto impiantistico e degli obiettivi dell'intervento."),
        step(3, "pin", "Ove necessario ai fini della valutazione, viene proposto un sopralluogo tecnico senza impegno per il rilievo diretto delle condizioni impiantistiche."),
    ]),
    para("<em>Il colloquio preliminare non comporta alcun impegno contrattuale ed è finalizzato esclusivamente alla verifica tecnica di fattibilità dell'intervento.</em>",
         "rgba(238,246,250,.6)", 15, 400, 1.6),
    C({"content_width": "full", "flex_direction": "row", "padding": box(6, 0, 0, 0), "padding_mobile": box(4, 0, 0, 0)}, [
        button("Vai alla richiesta di valutazione →", "#contatti-form", "outline-light", 16.5),
    ]),
]

HIDE_FOOTER_FORM = html("<style>.elementor-location-footer #contatti{display:none!important;}</style>",
                        {"_css_classes": "iah-global"})

main = section("sec-contatti-form", "contatti", NAVY, [
    HIDE_FOOTER_FORM,
    g.contact_box(left, FORM_CONTATTI),
], pad=(110, 24, 110, 24))

out = [hero, main]

if __name__ == "__main__":
    dump(out, "contatti-78")
