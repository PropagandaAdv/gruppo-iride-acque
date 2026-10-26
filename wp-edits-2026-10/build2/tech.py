import sys, json
sys.path.insert(0, '.')
from lib import *

BASE = 'https://gruppoirideacque.propagandaadv.com/'
BG = BASE + 'wp-content/uploads/2026/09/hero-template-bg.webp'
SECTORS = ['Agricoltura', 'Food & Beverage', 'Chimico-farmaceutico', 'Hospitality', 'Carta', 'Detergenti e cosmetici',
           'Acque reflue', 'Ospedaliero', 'Percolato', 'Tessile', 'Oil & Gas', 'Multiutilities']
APPS = [
    ('Trattamento acque primarie e di processo', 'trattamento-acque-primarie-e-di-processo',
     ['Sistemi di filtrazione avanzata', 'Sistemi di disinfezione', 'Controllo automatico',
      'Qualità dell’acqua e qualità dell’impianto', 'Efficienza operativa', 'Design su misura e modulare',
      'Gestione semplificata']),
    ('Trattamento acque reflue', 'trattamento-acque-reflue',
     ['Impianti biologici', 'Impianti chimico-fisici', 'Impianti a scarico zero ZLD']),
    ('Impianti a scarico zero (ZLD)', 'impianti-a-scarico-zero-zld',
     ['Processo avanzato', 'Controllo automatico', 'Trattamento antibatterico', 'Zero impatto', 'Sicurezza idrica',
      'Efficienza energetica', 'Riduzione dei costi', 'Conformità normativa']),
    ('Trattamento fanghi', 'trattamento-fanghi',
     ['Sistema di pressatura avanzato', 'Autonomia operativa', 'Sistema di lavaggio integrato',
      'Benefici economici e di esercizio', 'Efficienza operativa', 'Affidabilità e flessibilità',
      'Recupero delle risorse']),
]
SERV = [
    ('Progettazione e realizzazione impianti', 'progettazione-e-realizzazione-impianti',
     ['Studio preliminare', 'Ingegneria di processo', 'Progettazione e costruzione meccanica, idraulica ed elettrica',
      'Costruzione impianti chiavi in mano', 'Revamping e ampliamento impianti esistenti',
      'Integrazione di apparecchiature speciali', 'Referente unico', 'Software avanzati di modellazione 3D',
      'Costruzione interna specializzata', 'Documentazione e formazione']),
    ('Gestione impianti', 'gestione-impianti',
     ['Gestione tecnico-operativa', 'Assistenza e manutenzione', 'Pronto intervento e magazzini ricambi',
      'Controllo da remoto', 'Digital Management', 'Esperienza e competenza tecnica', 'Gestione integrata',
      'Velocità d’intervento', 'Ottimizzazione dei costi']),
    ('Noleggio impianti mobili', 'noleggio-impianti-mobili',
     ['Disidratazione fanghi mobile', 'Flottazione DAF mobile', 'MBR pilota', 'Noleggio per test pilota propedeutici',
      'Flessibilità operativa', 'Supporto specializzato', 'Rapidità d’intervento', 'Efficienza energetica']),
    ('Consulenza ambientale e permitting', 'consulenza-ambientale-e-permitting',
     ['Valutazione di sostenibilità', 'Gestione autorizzazioni ambientali', 'Audit ambientali',
      'Consulenza normativa', 'Conformità normativa', 'Ottimizzazione processi', 'Supporto specialistico',
      'Responsabilità ambientale']),
]
HID = {"hide_desktop": "hidden-desktop", "hide_tablet": "hidden-tablet", "hide_mobile": "hidden-mobile"}


def eyebrow2(t, color):
    return W("text-editor", {"editor": f"<p>{t}</p>", "text_color": color, **typo(19, 800, ls=1.4, mobile=17)})


def hero(kicker, title):
    kids = [W("text-editor", {"editor": f"<p>{kicker}</p>", "text_color": "#8DD6E8", **typo(16, 700, ls=2.2, mobile=14)}),
            W("heading", {"title": title, "header_size": "h1", "title_color": "#FFFFFF", **typo(52, 800, lh=1.12, mobile=32),
                          "_max_width": px(980)})]
    return C({"css_id": "sec-hero-tech", "content_width": "full", "background_background": "classic",
              "background_image": {"url": BG, "id": ""}, "background_position": "center right",
              "background_size": "cover", "background_overlay_background": "classic",
              "background_overlay_color": "rgba(9,23,31,.82)", "padding": box(190, 24, 90, 24),
              "padding_mobile": box(130, 16, 56, 16), "margin": box(0)},
             [C({"content_width": "boxed", "boxed_width": px(1240), "flex_gap": gap(18), "flex_gap_mobile": gap(14)}, kids)],
             inner=False)


def card(title, text=None, light=False, extra=None, btn=None):
    kids = [W("heading", {"title": title, "header_size": "h3"})]
    if text:
        s = {"editor": f"<p>{text}</p>"}
        if extra == 'sector':
            s["_css_classes"] = "iah-sector-desc"
        kids.append(W("text-editor", s))
    if btn:
        kids.append(btn)
    cls = "iah-hcard" + (" iah-w" if light else "") + (" iah-sector" if extra == 'sector' else "")
    return C({"content_width": "full", "css_classes": cls}, kids)


def grid(cards, cols=4):
    return C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_wrap": "wrap",
              "css_classes": "iah-grid" + ("3" if cols == 3 else "")}, cards)


def sect(css, eid, bg, kids):
    return section(css, eid, bg, kids, pad=(90, 24, 100, 24), pad_m=(56, 16, 64, 16))


def inner(kids, g=28):
    return C({"content_width": "boxed", "boxed_width": px(1240), "flex_gap": gap(g)}, kids)


def tech_page(kicker, title, cards_titles):
    note = W("text-editor", {"editor": "<p>TESTO PROVVISORIO — pagina modello: testi, immagini e schede da sostituire con i contenuti forniti dal cliente. Non indicizzare.</p>", **HID})
    meta = W("html", {"html": '<meta name="robots" content="noindex, nofollow">', "_css_classes": "iah-global"})
    desc = sect("sec-desc", "descrizione", "#FFFFFF", [C({"content_width": "boxed", "boxed_width": px(1000), "flex_gap": gap(20)}, [
        eyebrow2("Descrizione", BLUE),
        W("text-editor", {"editor": "<p>Il testo descrittivo di questa pagina è in attesa dei contenuti forniti dal cliente.</p>",
                          "text_color": BODY, "_css_classes": "iah-p", **typo(23, 400, lh=1.65, mobile=19)}),
        note, meta])])
    cards = sect("sec-cards", "caratteristiche", NAVY, [inner([
        eyebrow2("Punti chiave", "#8DD6E8"),
        grid([card(t, "Descrizione in arrivo.") for t in cards_titles])])])
    sets = sect("sec-settori", "settori-applicativi", "#FFFFFF", [inner([
        W("heading", {"title": "Settori applicativi", "header_size": "h2", "title_color": NAVY, **typo(44, 800, lh=1.15, mobile=28)}),
        grid([card(s, None, light=True, btn=button("Scopri di più", "#", size=15.5)) for s in SECTORS[1:7]], cols=3)])])
    return [hero(kicker, title), desc, cards, sets]


def overview():
    a = sect("sec-apps", "applicazioni", "#FFFFFF", [inner([
        eyebrow2("Applicazioni", BLUE),
        grid([card(t, None, light=True, btn=button("Scopri →", BASE + s + '/', size=15.5)) for t, s, _ in APPS])])])
    b = sect("sec-servizi", "servizi", NAVY, [inner([
        eyebrow2("Servizi", "#8DD6E8"),
        grid([card(t, None, light=False, btn=button("Scopri →", BASE + s + '/', size=15.5)) for t, s, _ in SERV])])])
    return [hero("Gruppo Iride Acque", "Applicazioni e Servizi"), a, b]


def settori():
    g = sect("sec-settori-lista", "settori", "#FFFFFF", [inner([
        eyebrow2("Ambiti di intervento", BLUE),
        W("text-editor", {"editor": "<p>Passa il mouse (o tocca) su un settore per leggerne la descrizione.</p>",
                          "text_color": BODY, "_css_classes": "iah-p", **typo(23, 400, lh=1.65, mobile=19)}),
        W("text-editor", {"editor": "<p>TESTO PROVVISORIO — descrizioni dei settori da fornire dal cliente.</p>", **HID}),
        grid([card(s, "Descrizione in arrivo.", extra='sector') for s in SECTORS])])])
    return [hero("Gruppo Iride Acque", "Settori"), g]


out = {}
for t, s, c in APPS:
    out[s] = tech_page("Applicazioni", t, c)
for t, s, c in SERV:
    out[s] = tech_page("Servizi", t, c)
out['overview'] = overview()
out['settori'] = settori()
for k, tree in out.items():
    fix_ids(tree)
    js = json.dumps(tree, ensure_ascii=False, separators=(',', ':'))
    open(f'build2/t_{k}.json', 'w', encoding='utf-8').write(js)
    print(k, len(js))
