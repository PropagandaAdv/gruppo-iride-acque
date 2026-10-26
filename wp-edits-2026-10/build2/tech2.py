import sys, json
sys.path.insert(0, '.')
sys.path.insert(0, 'build2')
from tech import APPS, SERV, SECTORS, BASE, BG, HID

_n = [0]


def nid():
    _n[0] += 1
    return f"t{_n[0]:06d}"[-8:]


def W(t, s):
    return {"id": nid(), "elType": "widget", "widgetType": t, "settings": s, "elements": []}


def C(s, kids, inner=True):
    d = {"flex_direction": "column"}
    d.update(s)
    return {"id": nid(), "elType": "container", "isInner": inner, "settings": d, "elements": kids}


def sec(css_id, eid, bg, kids, extra=None):
    s = {"css_id": css_id, "_element_id": eid, "content_width": "full", "background_background": "classic",
         "background_color": bg, "css_classes": "iah-sec"}
    if extra:
        s.update(extra)
    return C(s, kids, inner=False)


def box_(kids, w=1240):
    return C({"content_width": "boxed", "boxed_width": {"unit": "px", "size": w}}, kids)


def eyebrow(t, dark=False):
    return W("text-editor", {"editor": f"<p>{t}</p>", "_css_classes": "iah-eyebrow" + (" iah-eyebrow-d" if dark else "")})


def h(t, tag="h2", cls="iah-h2"):
    return W("heading", {"title": t, "header_size": tag, "_css_classes": cls})


def btn(t, url):
    return W("button", {"text": t, "link": {"url": url, "is_external": "", "nofollow": ""}})


def card(title, text=None, light=False, sector=False, b=None):
    kids = [W("heading", {"title": title, "header_size": "h3"})]
    if text:
        kids.append(W("text-editor", {"editor": f"<p>{text}</p>", "_css_classes": "iah-sector-desc" if sector else "iah-card-text"}))
    if b:
        kids.append(b)
    return C({"content_width": "full", "css_classes": "iah-hcard" + (" iah-w" if light else "") + (" iah-sector" if sector else "")}, kids)


def grid(cards, three=False):
    return C({"content_width": "boxed", "boxed_width": {"unit": "px", "size": 1240}, "flex_direction": "row",
              "flex_wrap": "wrap", "css_classes": "iah-grid" + ("3" if three else "")}, cards)


def hero(kicker, title):
    return sec("sec-hero-tech", "", "#09171F", [box_([
        W("text-editor", {"editor": f"<p>{kicker}</p>", "_css_classes": "iah-hero-kicker"}),
        h(title, "h1", "iah-h1")])],
        {"background_image": {"url": BG, "id": ""}, "background_position": "center right", "background_size": "cover",
         "background_overlay_background": "classic", "background_overlay_color": "rgba(9,23,31,.82)",
         "css_classes": "iah-sec iah-hero"})


def desc():
    return sec("sec-desc", "descrizione", "#FFFFFF", [box_([
        eyebrow("Descrizione"),
        W("text-editor", {"editor": "<p>Il testo descrittivo di questa pagina è in attesa dei contenuti forniti dal cliente.</p>", "_css_classes": "iah-p"}),
        W("text-editor", {"editor": "<p>TESTO PROVVISORIO — pagina modello: testi, immagini e schede da sostituire con i contenuti forniti dal cliente. Non indicizzare.</p>", **HID}),
        W("html", {"html": '<meta name="robots" content="noindex, nofollow">', "_css_classes": "iah-global"})], 1000)])


def cards_sec(titles):
    return sec("sec-cards", "caratteristiche", "#09171F", [box_([eyebrow("Punti chiave", True),
                                                               grid([card(t, "Descrizione in arrivo.") for t in titles])])])


def settori_app():
    return sec("sec-settori", "settori-applicativi", "#FFFFFF", [box_([h("Settori applicativi"),
        grid([card(s, None, True, b=btn("Scopri di più", "#")) for s in SECTORS[1:7]], True)])])


def overview_secs():
    a = sec("sec-apps", "applicazioni", "#FFFFFF", [box_([eyebrow("Applicazioni"), grid(
        [card(t, None, True, b=btn("Scopri →", BASE + s + "/")) for t, s, _ in APPS])])])
    b = sec("sec-servizi", "servizi", "#09171F", [box_([eyebrow("Servizi", True), grid(
        [card(t, None, False, b=btn("Scopri →", BASE + s + "/")) for t, s, _ in SERV])])])
    return [a, b]


def settori_list():
    return sec("sec-settori-lista", "settori", "#FFFFFF", [box_([
        eyebrow("Ambiti di intervento"),
        W("text-editor", {"editor": "<p>Passa il mouse (o tocca) su un settore per leggerne la descrizione.</p>", "_css_classes": "iah-p"}),
        W("text-editor", {"editor": "<p>TESTO PROVVISORIO — descrizioni dei settori da fornire dal cliente.</p>", **HID}),
        grid([card(s, "Descrizione in arrivo.", sector=True) for s in SECTORS])])])


def dump(name, tree):
    js = json.dumps(tree, ensure_ascii=False, separators=(',', ':'))
    open(f'build2/u_{name}.json', 'w', encoding='utf-8').write(js)
    print(name, len(js))


dump('hero', [hero("__KICKER__", "__TITLE__")])
dump('desc', [desc()])
dump('settori_app', [settori_app()])
for t, s, c in APPS + SERV:
    dump('cards_' + s, [cards_sec(c)])
dump('overview', overview_secs())
dump('settori_list', [settori_list()])
