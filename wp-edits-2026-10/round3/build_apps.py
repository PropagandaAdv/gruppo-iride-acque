"""Genera i JSON Elementor delle pagine 288 (primarie) e 289 (reflue) con i testi verbatim di sito.docx.
Uso (da round3): python -I -X utf8 build_apps.py"""
import json, random

random.seed(2889)
BASE = "https://gruppoirideacque.propagandaadv.com"
UP = BASE + "/wp-content/uploads/2026/10/"
BG = BASE + "/wp-content/uploads/2026/09/hero-template-bg.webp"
NAVY = "#09171F"


def nid():
    return "%07x" % random.randrange(0x1000000, 0xfffffff)


def W(wt, s):
    return {"id": nid(), "elType": "widget", "widgetType": wt, "settings": s, "elements": []}


def C(s, kids, inner=True):
    d = {"content_width": "full", "flex_direction": "column", "flex_direction_mobile": "column"}
    d.update(s)
    return {"id": nid(), "elType": "container", "isInner": inner, "settings": d, "elements": kids}


def px(n):
    return {"unit": "px", "size": n}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def te(paras, cls):
    return W("text-editor", {"editor": "".join(f"<p>{esc(p)}</p>" for p in paras), "_css_classes": cls})


def sec(anchor, bg, kids, cls="iah-sec ap-sec", extra=None):
    s = {"background_background": "classic", "background_color": bg, "css_classes": cls}
    if anchor:
        s["_element_id"] = anchor
    if extra:
        s.update(extra)
    return C(s, kids, inner=False)


def boxed(kids, w=1240):
    return C({"content_width": "boxed", "boxed_width": px(w), "flex_gap": {"unit": "px", "size": 22, "column": "22", "row": "22"}}, kids)


def head(eyebrow, title, dark=True):
    return [
        W("text-editor", {"editor": f"<p>{esc(eyebrow)}</p>", "_css_classes": "iah-eyebrow" + (" iah-eyebrow-d" if dark else "")}),
        W("heading", {"title": title, "header_size": "h2", "_css_classes": "ap-h2" + ("" if dark else " ap-h2-d")}),
    ]


def card(n, title, text, extra_cls=""):
    return C({"css_classes": "ap-card" + (" " + extra_cls if extra_cls else "")}, [
        W("text-editor", {"editor": f"<p>{n:02d}</p>", "_css_classes": "ap-n"}),
        W("heading", {"title": title, "header_size": "h3"}),
        te([text], "ap-t"),
    ])


def grid(cards, cls=""):
    return C({"content_width": "boxed", "boxed_width": px(1240), "css_classes": "ap-grid" + (" " + cls if cls else "")}, cards)


def case(img, alt, tag, title, sub, paras, pills):
    kids = [W("image", {"image": {"url": UP + img[0], "id": img[1], "alt": alt}, "image_size": "full", "_css_classes": "ap-ci"}),
            te([tag], "ap-tag"),
            W("heading", {"title": title, "header_size": "h3"})]
    if sub:
        kids.append(te([sub], "ap-sub"))
    kids.append(te(paras, "ap-t"))
    if pills:
        kids.append(te([pills], "ap-pills"))
    return C({"css_classes": "ap-card ap-case"}, kids)


def soon():
    return C({"css_classes": "ap-soon"}, [
        W("icon", {"selected_icon": {"value": "far fa-images", "library": "fa-regular"}, "primary_color": "#8AA4B4",
                   "size": px(54), "align": "center"}),
        W("heading", {"title": "Prossimi progetti", "header_size": "h3", "align": "center"}),
        te(["Nuove realizzazioni saranno presto disponibili."], "ap-t ap-center"),
    ])


CSS = """<style>
.ap-grid>.e-con-inner{display:flex!important;flex-direction:row!important;flex-wrap:wrap!important;gap:22px!important;align-items:stretch!important;}
.ap-grid>.e-con-inner>.ap-card{flex:0 0 calc(33.333% - 14.67px)!important;max-width:calc(33.333% - 14.67px)!important;}
.ap-grid.ap-g2>.e-con-inner>.ap-card,.ap-grid.ap-gw>.e-con-inner>.ap-card:nth-last-child(-n+2){flex:0 0 calc(50% - 11px)!important;max-width:calc(50% - 11px)!important;}
.ap-grid.ap-g2>.e-con-inner>.ap-soon{flex:0 0 calc(50% - 11px)!important;max-width:calc(50% - 11px)!important;}
.ap-grid>.e-con-inner>.ap-soon.ap-wide{flex:0 0 100%!important;max-width:100%!important;}
html body .elementor .e-con.ap-card{position:relative;display:flex!important;flex-direction:column!important;gap:8px!important;background:#FFFFFF;border-radius:16px!important;padding:26px 28px 86px!important;box-shadow:0 18px 44px -26px rgba(0,0,0,.55);box-sizing:border-box;transition:transform .35s ease,box-shadow .35s ease;}
html body .elementor .e-con.ap-card:hover{transform:translateY(-5px);box-shadow:0 26px 52px -26px rgba(74,183,213,.55);}
.ap-card::after{content:"→";position:absolute;right:20px;bottom:20px;width:46px;height:46px;border-radius:50%;background:#7FD6F2;color:#09171F;font:700 22px/46px Montserrat,sans-serif;text-align:center;pointer-events:none;}
.ap-n,.ap-n p{color:#1FB6E0!important;font:800 15px/1 Montserrat,sans-serif!important;letter-spacing:.06em;margin:0!important;}
.ap-card .elementor-heading-title{color:#09171F!important;font:800 22px/1.25 Montserrat,sans-serif!important;}
.ap-t,.ap-t p{color:#4B6272!important;font:400 16.5px/1.6 Montserrat,sans-serif!important;margin:0 0 .7em!important;}
.ap-t p:last-child{margin-bottom:0!important;}
.ap-h2 .elementor-heading-title{color:#FFFFFF!important;font:800 clamp(2.1rem,4.4vw,3.6rem)/1.08 Montserrat,sans-serif!important;max-width:900px;}
.ap-h2-d .elementor-heading-title{color:#09171F!important;}
.ap-lead,.ap-lead p{color:rgba(238,246,250,.88)!important;font:400 19px/1.65 Montserrat,sans-serif!important;margin:0 0 .9em!important;max-width:820px;}
.ap-lead p:last-child{margin-bottom:0!important;}
.ap-hl,.ap-hl p{color:#FFFFFF!important;font:600 22px/1.55 Montserrat,sans-serif!important;margin:0 0 .8em!important;max-width:820px;}
.ap-intro,.ap-intro p{color:#3D5A6C!important;font:400 18px/1.65 Montserrat,sans-serif!important;max-width:900px;margin:0!important;}
.ap-ci img{width:100%!important;height:auto;aspect-ratio:16/10;object-fit:cover;border-radius:12px;display:block;}
.ap-tag,.ap-tag p{color:#1A8FB0!important;font:700 13px/1.3 Montserrat,sans-serif!important;letter-spacing:.14em;text-transform:uppercase;margin:6px 0 0!important;}
.ap-sub,.ap-sub p{color:#3D5A6C!important;font:500 17px/1.45 Montserrat,sans-serif!important;margin:0!important;}
.ap-pills,.ap-pills p{display:inline-block;background:#E3F5FB;color:#09171F!important;font:600 14px/1.4 Montserrat,sans-serif!important;padding:9px 16px;border-radius:999px;margin:10px 0 0!important;max-width:calc(100% - 70px);}
html body .elementor .e-con.ap-case{padding:18px 18px 88px!important;}
html body .elementor .e-con.ap-soon{display:flex!important;flex-direction:column!important;justify-content:center;align-items:center;gap:12px!important;min-height:300px;background:rgba(238,246,250,.7);border:2px dashed rgba(26,77,106,.35);border-radius:20px!important;padding:40px 24px!important;box-sizing:border-box;}
.ap-soon .elementor-heading-title{color:#09171F!important;font:800 22px/1.25 Montserrat,sans-serif!important;text-align:center;}
.ap-center,.ap-center p{text-align:center!important;}
.ap-sec .iah-eyebrow,.ap-sec .iah-eyebrow p{text-transform:uppercase!important;letter-spacing:.16em!important;font-size:15px!important;font-weight:700!important;}
@media(max-width:1024px){.ap-grid>.e-con-inner>.ap-card,.ap-grid.ap-gw>.e-con-inner>.ap-card:nth-last-child(-n+2),.ap-grid.ap-g2>.e-con-inner>.ap-card{flex:0 0 calc(50% - 11px)!important;max-width:calc(50% - 11px)!important;}}
@media(max-width:767px){.ap-grid>.e-con-inner>.ap-card,.ap-grid.ap-gw>.e-con-inner>.ap-card:nth-last-child(-n+2),.ap-grid.ap-g2>.e-con-inner>.ap-card,.ap-grid.ap-g2>.e-con-inner>.ap-soon{flex:0 0 100%!important;max-width:100%!important;}
.ap-hl,.ap-hl p{font-size:19px!important;}.ap-lead,.ap-lead p{font-size:17px!important;}}
</style><meta name="robots" content="noindex, nofollow">"""


def hero(title, hl, plain):
    kids = [W("text-editor", {"editor": "<p>Applicazioni</p>", "_css_classes": "iah-hero-kicker"}),
            W("heading", {"title": title, "header_size": "h1", "_css_classes": "iah-h1"})]
    if hl:
        kids.append(te(hl, "ap-hl"))
    kids.append(te(plain, "ap-lead"))
    kids.append(W("html", {"html": CSS, "_css_classes": "iah-global"}))
    return sec("hero", NAVY, [boxed(kids)], "iah-sec ap-sec iah-hero",
               {"background_image": {"url": BG, "id": ""}, "background_position": "center right",
                "background_size": "cover", "background_overlay_background": "classic",
                "background_overlay_color": "rgba(9,23,31,.82)"})


def page(d):
    secs = [hero(d["h1"], d.get("hl", []), d["plain"])]
    secs.append(sec("tecnologie", NAVY, [boxed([
        W("text-editor", {"editor": "<p>Le nostre tecnologie</p>", "_css_classes": "iah-eyebrow iah-eyebrow-d"}),
        grid([card(i + 1, t, x) for i, (t, x) in enumerate(d["tech"])], d.get("techcls", ""))])]))
    v = d["vant"]
    secs.append(sec("vantaggi", NAVY, [boxed(
        head("Perché scegliere il Gruppo Iride", "I vantaggi delle nostre soluzioni") + [te(v["intro"], "ap-lead"),
        grid([card(i + 1, t, x) for i, (t, x) in enumerate(v["cards"])], "ap-g2")])]))
    s = d["sett"]
    secs.append(sec("settori", NAVY, [boxed(
        head("Dove operiamo", "Settori di applicazione") + [te(s["intro"], "ap-lead"),
        grid([card(i + 1, t, x) for i, (t, x) in enumerate(s["cards"])], s.get("cls", ""))])]))
    c = d["case"]
    secs.append(sec("case-study", "#FFFFFF", [boxed(
        head("Le nostre realizzazioni", "Case study", dark=False) + [te([c["intro"]], "ap-intro"),
        grid(c["items"], "ap-g2")])]))
    return secs


PRIM = dict(
    h1="Trattamento acque primarie e di processo",
    plain=[
        "Il Gruppo Iride progetta e realizza impianti per il trattamento delle acque primarie e di processo, sviluppando soluzioni tecnologiche su misura per le esigenze dei settori industriale, civile e tecnologico.",
        "Grazie alle competenze integrate delle società del Gruppo, offriamo soluzioni complete, dalla consulenza e progettazione fino alla costruzione e messa in servizio degli impianti, garantendo elevati standard di qualità, affidabilità ed efficienza operativa.",
        "Attraverso l'impiego di tecnologie avanzate di filtrazione, separazione, purificazione, addolcimento, demineralizzazione e disinfezione, miglioriamo le caratteristiche dell'acqua, rendendola idonea ai diversi utilizzi e promuovendo una gestione sostenibile delle risorse idriche.",
    ],
    tech=[
        ("Filtrazione e chiarificazione", "Sistemi per la rimozione di solidi sospesi, torbidità e impurità mediante diverse tecnologie di filtrazione."),
        ("Trattamenti a membrana", "Ultrafiltrazione, nanofiltrazione e osmosi inversa per la separazione di contaminanti e sali disciolti."),
        ("Addolcimento", "Soluzioni per la riduzione della durezza dell'acqua e la prevenzione delle incrostazioni."),
        ("Demineralizzazione e acqua ultrapura", "Sistemi a scambio ionico, elettrodeionizzazione (EDI) e tecnologie integrate per la produzione di acqua ad elevata purezza."),
        ("Adsorbimento e rimozione contaminanti", "Tecnologie su carboni attivi, resine selettive e altri materiali per la rimozione di sostanze organiche e contaminanti specifici."),
        ("Disinfezione e controllo microbiologico", "Sistemi UV, clorazione, dosaggio di disinfettanti e altre soluzioni per il controllo della contaminazione microbiologica."),
        ("Dosaggio e condizionamento chimico", "Impianti per il dosaggio di reagenti, la regolazione del pH e il condizionamento delle acque di processo."),
        ("Trattamenti elettrochimici", "Tecnologie elettrochimiche per la rimozione di contaminanti, la disinfezione e il condizionamento dell'acqua."),
        ("Potabilizzazione", "Impianti integrati per la produzione di acqua destinata al consumo umano, nel rispetto dei requisiti normativi."),
    ],
    vant=dict(
        intro=["Le nostre soluzioni per il trattamento delle acque offrono valore concreto e misurabile, combinando tecnologia, competenza ed esperienza per rispondere alle esigenze specifiche di ogni settore.",
               "Lavoriamo al fianco dei nostri clienti per garantire impianti affidabili, efficienti e sostenibili, capaci di migliorare la qualità dell'acqua e ottimizzare i processi produttivi."],
        cards=[
            ("Soluzioni su misura", "Ogni impianto viene progettato in funzione delle caratteristiche dell'acqua, degli obiettivi di trattamento e delle specifiche esigenze operative del cliente."),
            ("Efficienza operativa", "Le nostre soluzioni ottimizzano consumi, prestazioni e continuità di esercizio, riducendo i costi di gestione e manutenzione."),
            ("Affidabilità e qualità", "Tecnologie selezionate e competenze specialistiche garantiscono prestazioni costanti, sicurezza operativa e qualità dell'acqua trattata."),
            ("Sostenibilità e ottimizzazione delle risorse", "Promuoviamo un utilizzo più razionale dell'acqua e dell'energia, contribuendo a processi più efficienti e sostenibili."),
        ]),
    sett=dict(
        intro=["Gruppo Iride sviluppa soluzioni per il trattamento delle acque in molteplici contesti industriali, civili e pubblici, rispondendo con competenza e tecnologia alle diverse esigenze di ogni settore.",
               "La nostra esperienza ci permette di offrire sistemi affidabili, efficienti e personalizzati, con l'obiettivo di garantire qualità dell'acqua, sostenibilità e continuità operativa in ogni ambito di applicazione."],
        cards=[
            ("Industria e processi produttivi", "Soluzioni per il trattamento delle acque destinate ai processi industriali, ai sistemi di produzione e agli impianti tecnologici in diversi settori produttivi."),
            ("Settore civile, commerciale e Ho.Re.Ca.", "Sistemi per il trattamento, la purificazione e il condizionamento delle acque destinati a edifici, attività commerciali, strutture ricettive e servizi."),
            ("Servizi pubblici e infrastrutture", "Soluzioni per il trattamento delle acque destinate all'approvvigionamento idrico, ai servizi collettivi e alle infrastrutture pubbliche."),
        ]),
)

REFL = dict(
    h1="Trattamento acque reflue",
    hl=[
        "Il Gruppo Iride progetta e realizza impianti per il trattamento delle acque reflue industriali e civili, offrendo soluzioni tecnologiche avanzate e personalizzate per la depurazione, il recupero delle risorse e la gestione sostenibile degli scarichi.",
        "Grazie alle competenze integrate delle società del Gruppo, sviluppiamo sistemi in grado di trattare reflui di diversa origine e composizione, attraverso l'impiego di processi fisici, chimici, biologici e termici, finalizzati alla rimozione degli inquinanti, al recupero dell'acqua e alla valorizzazione delle materie prime e dei sottoprodotti recuperabili.",
    ],
    plain=[
        "Le nostre soluzioni comprendono sistemi di trattamento e gestione dei fanghi, tecnologie di concentrazione e recupero delle acque, fino alla realizzazione di impianti a scarico liquido zero (Zero Liquid Discharge – ZLD), progettati per eliminare gli scarichi liquidi e massimizzare il recupero delle risorse.",
        "Ogni impianto viene sviluppato considerando le caratteristiche del refluo, le specifiche esigenze produttive e i requisiti normativi applicabili, con particolare attenzione all'efficienza dei processi, all'affidabilità operativa e all'ottimizzazione dei consumi e dei costi di gestione.",
        "Dalla consulenza e dallo studio preliminare fino alla progettazione, costruzione e messa in servizio degli impianti, il Gruppo Iride affianca i propri clienti nella realizzazione di soluzioni integrate e su misura, contribuendo alla riduzione dell'impatto ambientale e alla promozione di modelli produttivi sempre più sostenibili e orientati ai principi dell'economia circolare.",
    ],
    techcls="ap-gw",
    tech=[
        ("Pretrattamenti meccanici ed equalizzazione", "Grigliatura, vagliatura, dissabbiatura, disoleazione e sistemi di equalizzazione e omogeneizzazione dei reflui."),
        ("Trattamenti chimico-fisici", "Coagulazione, flocculazione, neutralizzazione, precipitazione chimica e strippaggio dell'ammoniaca per la rimozione di contaminanti specifici."),
        ("Flottazione e sedimentazione", "Sistemi DAF, sedimentatori e chiarificatori per la separazione di solidi sospesi, oli, grassi e fanghi."),
        ("Trattamenti biologici aerobici", "Impianti a fanghi attivi, SBR, MBBR e MBR, con processi di nitrificazione e denitrificazione per la rimozione della sostanza organica e dei nutrienti."),
        ("Trattamenti biologici anaerobici", "Processi anaerobici per reflui ad elevato carico organico, con possibilità di produzione e recupero energetico del biogas."),
        ("Trattamenti a membrane", "Microfiltrazione, ultrafiltrazione, nanofiltrazione e osmosi inversa per la separazione dei contaminanti, l'affinamento e il recupero delle acque."),
        ("Filtrazione e trattamenti terziari", "Filtri a sabbia, multistrato, carbone attivo, resine a scambio ionico e materiali adsorbenti per la rimozione dei contaminanti residui."),
        ("Ossidazione avanzata e tecnologia EMER", "Processi di ossidazione chimica e avanzata, inclusa la tecnologia proprietaria EMER, per il trattamento di reflui complessi e contaminanti difficilmente biodegradabili."),
        ("Disinfezione e affinamento finale", "Sistemi UV e trattamenti chimici per il controllo microbiologico e il miglioramento della qualità delle acque trattate."),
        ("Evaporazione, cristallizzazione ed essiccamento", "Evaporatori industriali, cristallizzatori ed essiccatori per la concentrazione dei reflui, il recupero dell'acqua e la gestione dei residui solidi, anche in sistemi ZLD."),
        ("Trattamento e disidratazione fanghi", "Sistemi di ispessimento, condizionamento, centrifugazione e filtrazione meccanica per il trattamento dei fanghi e la riduzione dei volumi da gestire."),
    ],
    vant=dict(
        intro=["Progettiamo impianti di depurazione su misura, combinando competenze ingegneristiche e tecnologie di trattamento per ottimizzare le prestazioni, ridurre l'impatto ambientale e favorire il recupero delle risorse."],
        cards=[
            ("Efficacia depurativa", "Soluzioni progettate per garantire la rimozione degli inquinanti e il raggiungimento dei requisiti qualitativi richiesti, nel rispetto dei limiti di scarico e delle esigenze di processo."),
            ("Efficienza operativa", "I nostri impianti ottimizzano consumi, prestazioni e continuità di esercizio, contribuendo alla riduzione dei costi di gestione e manutenzione."),
            ("Impianti completamente automatizzati", "Sistemi di controllo e automazione evoluti consentono una gestione affidabile, continua e semplificata dell'impianto, con monitoraggio costante dei processi e rapido intervento operativo."),
            ("Sostenibilità e recupero delle risorse", "Le nostre soluzioni favoriscono il recupero dell'acqua e, ove possibile, delle materie prime, contribuendo a modelli produttivi più efficienti, sostenibili e orientati all'economia circolare."),
        ]),
    sett=dict(
        cls="ap-g2",
        intro=["Le soluzioni del Gruppo Iride per il trattamento delle acque reflue trovano applicazione in contesti industriali, civili e infrastrutturali, con impianti progettati in funzione delle caratteristiche degli scarichi, degli obiettivi di depurazione e dei requisiti normativi.",
               "Grazie a un approccio su misura e all'integrazione di diverse tecnologie, sviluppiamo sistemi affidabili ed efficienti per la gestione degli scarichi, la riduzione dell'impatto ambientale e, ove possibile, il recupero delle risorse."],
        cards=[
            ("Industria e processi produttivi", "Progettiamo impianti per il trattamento delle acque reflue provenienti da attività industriali e processi produttivi, con soluzioni personalizzate per settori come alimentare e bevande, chimica, farmaceutica e cosmetica, tessile, cartaria, metalmeccanica, galvanica, manifatturiera ed energetica."),
            ("Settore civile, commerciale e infrastrutture", "Realizziamo soluzioni per il trattamento delle acque reflue generate da edifici, strutture ricettive, attività commerciali e infrastrutture pubbliche, anche in contesti con esigenze impiantistiche specifiche, come complessi residenziali, hotel e strutture Ho.Re.Ca., campeggi, strutture sanitarie e sportive, scuole, edifici pubblici e comunità."),
        ]),
)

IMG = {"campari": ("case-study-campari-sanificazione-centralizzata-v2.webp", 403),
       "tintoria": ("case-study-tintoria-emiliana-recupero-sali-v2.webp", 404),
       "eni": ("case-study-eni-sarroch-lavaggio-v4.webp", 407)}


def img(k):
    return IMG[k]


PRIM["case"] = dict(
    intro="Ogni progetto nasce da esigenze specifiche e viene sviluppato con un approccio su misura, combinando competenze tecniche ed esperienza applicativa per garantire risultati concreti e affidabili.",
    items=[
        case(img("campari"), "Impianto di dosaggio e sanificazione centralizzata con quadro di controllo e serbatoi",
             "Industria alimentare e delle bevande", "Sistema di sanificazione centralizzata per il Gruppo Campari", None,
             ["Progettazione e realizzazione di un sistema centralizzato di dosaggio di biossido di cloro per la sanificazione delle acque di processo e dei diversi utilizzi all'interno dello stabilimento.",
              "La soluzione consente un'efficace disinfezione senza lasciare tracce di ossidanti nel prodotto finale, risultando ideale per le esigenze di un'azienda del settore alimentare."], None),
        soon(),
    ])

REFL["case"] = dict(
    intro="Gruppo Iride sviluppa soluzioni personalizzate per il trattamento delle acque reflue, con un'attenzione concreta al recupero, al riutilizzo e all'efficienza dei processi di depurazione.",
    items=[
        case(img("tintoria"), "Moduli di ultrafiltrazione ceramica dell'impianto di recupero dei sali di tintura",
             "Settore tessile", "Tintoria Emiliana", "Recupero dei sali e trattamento integrato delle acque reflue",
             ["Impianto progettato per il recupero dei sali di tintura mediante ultrafiltrazione ceramica e nanofiltrazione. I concentrati delle membrane vengono trattati con tecnologia EMER, mentre l'effluente trattato e il resto dei reflui di stabilimento confluiscono in un impianto biologico prima dello scarico in fognatura.",
              "È inoltre previsto un upgrade con osmosi inversa per il recupero delle acque in uscita dal biologico."],
             "UF ceramica • NF • EMER • biologico • upgrade RO"),
        case(img("eni"), "Serbatoi blu e filtri a sabbia dell'impianto di trattamento delle acque di lavaggio",
             "Settore energetico", "ENI | Sarroch", "Trattamento e riutilizzo delle acque di lavaggio",
             ["Impianto realizzato per il trattamento delle acque reflue provenienti dal lavaggio delle bombole di gas. Il sistema integra un reattore EMER per l'ossidazione delle acque, seguito da filtrazione a sabbia e carbone attivo per l'affinamento finale e il riutilizzo dell'acqua nel processo produttivo."],
             "EMER • filtro a sabbia • carbone attivo • riutilizzo"),
        soon(),
    ])
# il terzo elemento (placeholder) occupa l'intera riga
REFL["case"]["items"][-1]["settings"]["css_classes"] = "ap-soon ap-wide"

for key, d in (("primarie", PRIM), ("reflue", REFL)):
    tree = page(d)
    s = json.dumps(tree, ensure_ascii=False, separators=(",", ":"))
    open(f"app_{key}.json", "w", encoding="utf8").write(s)
    print(key, len(s))
