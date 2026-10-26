"""Genera i JSON Elementor completi delle pagine Applicazioni/Servizi/Settori con i testi di partenza di sostelia.it (rebrand a Gruppo Iride Acque, nessun link esterno)
(build2/content.json, prodotto da sost_content.py). Uso (da wp-edits-2026-10): python -I -X utf8 build2/sost_pages.py"""
import sys, json, html as H

sys.path.insert(0, '.')
from lib import *
import lib as _lib


def W(t, s):
    return {"id": _lib.nid("w"), "elType": "widget", "widgetType": t, "settings": s, "elements": []}


def C(s, kids, inner=True):
    d = {"flex_direction": "column"}
    d.update(s)
    if "_css_classes" in d:
        d["css_classes"] = d.pop("_css_classes")
    return {"id": _lib.nid("c"), "elType": "container", "isInner": inner, "settings": d, "elements": kids}

BASE = 'https://gruppoirideacque.propagandaadv.com/'
BG = BASE + 'wp-content/uploads/2026/09/hero-template-bg.webp'
IMG_IND = BASE + 'wp-content/uploads/2026/09/ambito-industriale.jpg'
IMG_CIV = BASE + 'wp-content/uploads/2026/09/ambito-civile.jpg'
CONTENT = json.load(open('build2/content.json', encoding='utf-8'))
import re

GRP = 'Gruppo Iride Acque'


def rebrand(t):
    """Toglie ogni riferimento a Sostelia, riscrivendo con 'Gruppo Iride Acque' e le contrazioni italiane corrette."""
    t = t.replace('Gruppo Sostelia', GRP)
    t = re.sub(r'(?<![A-Za-z])di Sostelia', 'del ' + GRP, t)
    t = re.sub(r'(?<![A-Za-z])da Sostelia', 'dal ' + GRP, t)
    t = re.sub(r'(?<![A-Za-z])con Sostelia', 'con il ' + GRP, t)
    t = re.sub(r'(?<![A-Za-z])per Sostelia', 'per il ' + GRP, t)

    def sub(m):
        pre = t[:m.start()]
        start = (pre.strip() == '' or pre.rstrip().endswith(('.', '?', '!', '<p>', '>')))
        return ('Il ' if start else 'il ') + GRP
    return re.sub(r'Sostelia', sub, t)


def _rebrand_tree(o):
    if isinstance(o, dict):
        return {k: (v if k == 'href' else _rebrand_tree(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [_rebrand_tree(v) for v in o]
    if isinstance(o, str):
        return rebrand(o) if 'Sostelia' in o else o
    return o


CONTENT = _rebrand_tree(CONTENT)

# progetti di riferimento -> pagine interne pertinenti (principale, alternativa se coincide con la pagina corrente)
PROJ_LINK = [
    ('Potenziamento impianto trattamento reflui', ('reflue', 'progettazione')),
    ('parco industriale di Mariel', ('progettazione', 'industriale')),
    ('osmosi per il recupero di acque secondarie', ('primarie', 'zld')),
    ('riutilizzo acque depurate', ('zld', 'reflue')),
    ('trattamento rifiuti liquidi', ('progettazione', 'gestione')),
    ('trattamento acque industriali', ('industriale', 'zld')),
    ('disidratazione fanghi', ('fanghi', 'noleggio')),
    ('grotte di Postumia', ('sii', 'progettazione')),
]


def proj_url(title, cur):
    for frag, (a, b) in PROJ_LINK:
        if frag in title:
            return URL[a] if a != cur else URL[b]
    return URL['contatti']
HERO_BG = {}  # slug -> url immagine hero (opzionale, popolato da build2/hero_images.json se presente)
try:
    HERO_BG = json.load(open('build2/hero_images.json', encoding='utf-8'))
except FileNotFoundError:
    pass

URL = {
    'primarie': BASE + 'trattamento-acque-primarie-e-di-processo/',
    'reflue': BASE + 'trattamento-acque-reflue/',
    'zld': BASE + 'impianti-a-scarico-zero-zld/',
    'fanghi': BASE + 'trattamento-fanghi/',
    'progettazione': BASE + 'progettazione-e-realizzazione-impianti/',
    'gestione': BASE + 'gestione-impianti/',
    'noleggio': BASE + 'noleggio-impianti-mobili/',
    'consulenza': BASE + 'consulenza-ambientale-e-permitting/',
    'industriale': BASE + 'settori/industriale/',
    'sii': BASE + 'settori/servizio-idrico-integrato/',
    'settori': BASE + 'settori/',
    'overview': BASE + 'tecnologie-e-servizi/',
    'contatti': BASE + 'contatti/',
}
TITLE = {k: CONTENT[k]['h1'] for k in ['primarie', 'reflue', 'zld', 'fanghi', 'progettazione', 'gestione', 'noleggio',
                                       'consulenza', 'industriale', 'sii']}
APPS = ['primarie', 'reflue', 'zld', 'fanghi']
SERV = ['progettazione', 'gestione', 'noleggio', 'consulenza']
NEXT = {'primarie': 'reflue', 'reflue': 'zld', 'zld': 'fanghi', 'fanghi': 'primarie', 'progettazione': 'gestione',
        'gestione': 'noleggio', 'noleggio': 'consulenza', 'consulenza': 'progettazione', 'industriale': 'sii',
        'sii': 'industriale'}
SECTOR_TXT = {
    'industriale': 'Sosteniamo le industrie e le imprese per ridurre il consumo idrico e favorire il recupero nei processi produttivi, fornendo tecnologie all’avanguardia interamente progettate, costruite e gestite dal nostro Gruppo.',
    'sii': 'Affianchiamo i gestori del servizio idrico integrato con servizi su misura e impianti innovativi per depurare l’acqua prima di restituirla al suo ambiente naturale.',
}
ASSIST_H = 'Servizi di assistenza e manutenzione. Ci prendiamo cura dei vostri impianti.'
ASSIST_P = ['Forniamo servizi di assistenza tecnica, manutenzione programmata e predittiva e pronto intervento per i nostri clienti.',
            'Compila il modulo per contattare i nostri specialisti.']


def esc(t):
    return H.escape(t, quote=False)


def sec(css_id, eid, dark, kids, extra=None):
    s = {"css_id": css_id, "content_width": "full", "background_background": "classic",
         "background_color": NAVY if dark else "#FFFFFF", "_css_classes": "iah-sec"}
    if eid:
        s["_element_id"] = eid
    if extra:
        s.update(extra)
    return C(s, kids, inner=False)


def box_(kids, w=1240):
    return C({"content_width": "boxed", "boxed_width": px(w)}, kids)


def eyebrow(t, dark=False):
    return W("text-editor", {"editor": f"<p>{esc(t)}</p>", "_css_classes": "iah-eyebrow" + (" iah-eyebrow-d" if dark else "")})


def h2(t, dark=False, big=False):
    cls = "iah-band" if dark else ("iah-h2" if big else "iah-h2-sub")
    return W("heading", {"title": t, "header_size": "h2", "_css_classes": cls})


def p_block(items, cls="iah-p"):
    """items = [{'p':..}|{'li':..}] -> un solo text-editor con <p> e <ul>."""
    out, ul = [], []
    for it in items:
        if 'li' in it:
            ul.append(f"<li>{esc(it['li'])}</li>")
            continue
        if ul:
            out.append("<ul>" + "".join(ul) + "</ul>")
            ul = []
        out.append(f"<p>{esc(it['p'])}</p>")
    if ul:
        out.append("<ul>" + "".join(ul) + "</ul>")
    return W("text-editor", {"editor": "".join(out), "_css_classes": cls})


def btn(t, url, external=False):
    return W("button", {"text": t, "link": {"url": url, "is_external": "on" if external else "", "nofollow": ""}})


def hero(kicker, title, slug=None):
    extra = {"background_image": {"url": HERO_BG.get(slug, BG), "id": ""}, "background_position": "center right",
             "background_size": "cover", "background_overlay_background": "classic",
             "background_overlay_color": "rgba(9,23,31,.82)", "_css_classes": "iah-sec iah-hero"}
    return sec("sec-hero-tech", "", False, [box_([
        W("text-editor", {"editor": f"<p>{esc(kicker)}</p>", "_css_classes": "iah-hero-kicker"}),
        W("heading", {"title": title, "header_size": "h1", "_css_classes": "iah-h1"})])], dict(
        {"background_color": "#09171F"}, **extra))


def noindex():
    return W("html", {"html": '<meta name="robots" content="noindex, nofollow">', "_css_classes": "iah-global"})


def grid(cards, kind=''):
    return C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_wrap": "wrap",
              "_css_classes": "iah-grid" + kind}, cards)


def pcard(i, title, texts):
    kids = [W("text-editor", {"editor": f"<p>{i:02d}</p>", "_css_classes": "iah-pnum"}),
            W("heading", {"title": title, "header_size": "h3"}),
            W("text-editor", {"editor": "".join(f"<p>{esc(t)}</p>" for t in texts), "_css_classes": "iah-card-text"})]
    return C({"content_width": "full", "_css_classes": "iah-hcard iah-pcard"}, kids)


def lcard(title, dark, text=None, b=None):
    kids = [W("heading", {"title": title, "header_size": "h3"})]
    if text:
        kids.append(W("text-editor", {"editor": f"<p>{esc(text)}</p>", "_css_classes": "iah-card-text"}))
    if b:
        kids.append(b)
    return C({"content_width": "full", "_css_classes": "iah-hcard" + ("" if dark else " iah-w")}, kids)


# ---------------------------------------------------------------- sezioni (dark deciso dal chiamante)
def s_desc(d, dark):
    return sec("sec-desc", "descrizione", dark, [box_([p_block(d['lead']), noindex()], 1000)])


def s_cards(d, dark):
    return sec("sec-cards", "caratteristiche", dark, [box_([
        eyebrow("Punti chiave", dark),
        grid([pcard(i + 1, b['title'], b['text']) for i, b in enumerate(d['blocks'])], "3")])])


def s_projects(d, dark, cur):
    if not d['projects']:
        return None
    return sec("sec-progetti", "progetti", dark, [box_([
        eyebrow("Progetti di riferimento", dark),
        grid([lcard(p['title'], dark, b=btn("Scopri di più", proj_url(p['title'], cur))) for p in d['projects']], "3")])])


def s_sectors(dark):
    return sec("sec-settori", "settori-applicativi", dark, [box_([
        h2("Settori applicativi", dark, big=True),
        grid([lcard("Industriale", dark, SECTOR_TXT['industriale'], btn("Scopri di più", URL['industriale'])),
              lcard("Servizio idrico integrato", dark, SECTOR_TXT['sii'], btn("Scopri di più", URL['sii']))], "2")])])


def s_cta(d, dark):
    return sec("sec-cta", "contattaci", dark, [box_([
        h2(d['cta']['title'], dark),
        btn("Contattaci", URL['contatti'])], 1000)])


def s_assist(dark):
    return sec("sec-assistenza", "assistenza", dark, [box_([
        h2(ASSIST_H, dark),
        W("text-editor", {"editor": "".join(f"<p>{esc(t)}</p>" for t in ASSIST_P), "_css_classes": "iah-band-text" if dark else "iah-p"}),
        btn("Contattaci", "#contatti")], 1000)])


def s_next(key, dark):
    lbl = "Applicazione successiva" if key in APPS else ("Servizio successivo" if key in SERV else "Settore successivo")
    n = NEXT[key]
    return sec("sec-next", "successivo", False, [box_([
        eyebrow(lbl),
        h2(TITLE[n]),
        btn("Scopri di più", URL[n])], 1000)],
        {"border_border": "solid", "border_width": box(1, 0, 0, 0), "border_color": "rgba(9,23,31,.12)"})


def build(secs_fn, first=None):
    """secs_fn: lista di callable(dark) -> sezione|None; alterna bianco/scuro a partire dal bianco."""
    out, k = [], 0
    for fn in secs_fn:
        s = fn(k % 2 == 1)
        if s is None:
            continue
        out.append(s)
        k += 1
    return out


def page_tech(key):
    d = CONTENT[key]
    kicker = "Applicazioni" if key in APPS else "Servizi"
    fns = [lambda dk: s_desc(d, dk), lambda dk: s_cards(d, dk), lambda dk: s_projects(d, dk, key)]
    if key in APPS:
        fns.append(s_sectors)
    else:
        fns.append(lambda dk: s_cta(d, dk))
    fns += [s_assist, lambda dk: s_next(key, dk)]
    return [hero(kicker, TITLE[key], key)] + build(fns)


def page_overview():
    a, s = CONTENT['app_overview'], CONTENT['serv_overview']
    apps = sec("sec-apps", "applicazioni", False, [box_([
        eyebrow("Applicazioni"),
        h2(a['extra'][0]['h2']),
        p_block(a['lead']),
        grid([lcard(TITLE[k], False, b=btn("Scopri →", URL[k])) for k in APPS], ""),
        h2(a['cta']['title']), btn("Contattaci", URL['contatti'])])])
    svc_cards = []
    texts = {'progettazione': s['lead'][2]['p'], 'gestione': s['lead'][3]['p']}
    for k in SERV:
        svc_cards.append(lcard(TITLE[k], True, texts.get(k), btn("Scopri →", URL[k])))
    srv = sec("sec-servizi", "servizi", True, [box_([
        eyebrow("Servizi", True),
        h2(s['extra'][0]['h2'], True),
        p_block(s['lead'][:2], "iah-p iah-band-text"),
        grid(svc_cards, ""),
        h2(s['cta']['title'], True), btn("Contattaci", URL['contatti'])])])
    return [hero("Gruppo Iride Acque", "Applicazioni e Servizi", 'overview'), apps, srv]


def scard(key, img):
    return C({"content_width": "full", "flex_justify_content": "flex-end", "flex_gap": gap(14),
              "flex_gap_mobile": gap(10), "border_radius": radius(28), "padding": box(36, 28, 36, 28),
              "padding_mobile": box(26, 22, 26, 22), "min_height": px(360),
              "background_background": "classic", "background_color": "#09171F",
              "background_overlay_background": "classic", "background_overlay_image": {"url": img, "id": ""},
              "background_overlay_position": "center center", "background_overlay_size": "cover",
              "background_overlay_opacity": {"unit": "px", "size": 0.55},
              "css_classes": "iah-scard",
              "custom_css": "selector{width:calc(50% - 12px)!important;flex:0 0 calc(50% - 12px)!important;overflow:hidden;position:relative;transition:transform .45s ease,box-shadow .45s ease;}"
                            "selector:hover{transform:translateY(-8px);box-shadow:0 30px 56px -26px rgba(74,183,213,.55);}"
                            "@media(max-width:767px){selector{width:100%!important;flex:0 0 100%!important;}}"},
             [W("heading", {"title": TITLE[key], "header_size": "h3", "title_color": "#FFFFFF", **typo(30, 800, lh=1.2, mobile=24)}),
              W("text-editor", {"editor": f"<p>{esc(SECTOR_TXT[key])}</p>", "text_color": "rgba(238,246,250,.9)", **typo(17, 400, lh=1.6)}),
              btn("Scopri di più", URL[key])])


def page_settori():
    d = CONTENT['settori']
    top = sec("sec-settori-intro", "settori", False, [box_([
        h2(d['extra'][0]['h2'], False, big=True),
        p_block(d['lead']),
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_wrap": "wrap",
           "flex_direction_mobile": "column", "flex_gap": gap(24), "flex_gap_mobile": gap(20)}, [scard('industriale', IMG_IND), scard('sii', IMG_CIV)])]),
        noindex()])
    srv = sec("sec-servizi-offerti", "servizi-offerti", True, [box_([
        h2(d['extra'][1]['h2'], True), btn("Scopri di più", URL['overview'] + '#servizi'),
        h2(d['cta']['title'], True), btn("Contattaci", URL['contatti'])], 1000)])
    return [hero("Gruppo Iride Acque", "Settori", 'settori'), top, srv]


def page_sector(key):
    d = CONTENT[key]
    apps = [k for k in APPS if (key == 'industriale' or k != 'zld')]
    ap = lambda dk: sec("sec-apps-settore", "impianti", dk, [box_([
        h2(d['extra'][0]['h2'], dk),
        grid([lcard(TITLE[k], dk, b=btn("Scopri →", URL[k])) for k in apps], "3")])])
    proj = lambda dk: sec("sec-progetti", "progetti", dk, [box_([
        eyebrow("Progetti di riferimento", dk),
        grid([lcard(d['extra'][1]['h2'], dk, b=btn("Scopri di più", proj_url(d['extra'][1]['h2'], key)))], "3")])])
    fns = [lambda dk: s_desc(d, dk), ap, proj, lambda dk: s_cta(d, dk), lambda dk: s_next(key, dk)]
    return [hero("Settori", TITLE[key], key)] + build(fns)


OUT = {k: page_tech(k) for k in APPS + SERV}
OUT['overview'] = page_overview()
OUT['settori'] = page_settori()
OUT['industriale'] = page_sector('industriale')
OUT['sii'] = page_sector('sii')
for k, tree in OUT.items():
    fix_ids(tree)
    js = json.dumps(tree, ensure_ascii=False, separators=(',', ':'))
    open(f'build2/s_{k}.json', 'w', encoding='utf-8').write(js)
    print(k, len(js))
