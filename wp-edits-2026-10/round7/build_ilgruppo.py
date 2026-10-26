# -*- coding: utf-8 -*-
import json, io, re, copy, os
d = json.load(io.open('backup_live/55.json', encoding='utf8'))


def find(e, i):
    if e['id'] == i:
        return e
    for c in e.get('elements', []):
        r = find(c, i)
        if r:
            return r


def get(i):
    for e in d:
        r = find(e, i)
        if r:
            return r


def setw(i, key, val):
    get(i)['settings'][key] = val


# 1 sottotitolo (verbatim cliente)
setw('56e4cde3', 'editor', "<p>Iride Acque, Biemme Engineering e Bieffe Costruzioni, combinando esperienza, ingegneria e capacità realizzative per offrire soluzioni avanzate nel trattamento delle acque civili e industriali, seguendo ogni fase del progetto: dall'analisi alla progettazione, fino alla realizzazione, gestione e manutenzione degli impianti.</p>")

# 2 video hero (il video si sovrappone all'immagine; se il file manca resta l'immagine)
VID = """<script>
(function(){
  var wrap=document.querySelector('#bhHeroIlGruppo .bh-media'); if(!wrap) return;
  if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var v=document.createElement('video');
  v.muted=true;v.loop=true;v.autoplay=true;v.playsInline=true;v.setAttribute('playsinline','');v.setAttribute('aria-hidden','true');v.preload='auto';
  v.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;opacity:0;transition:opacity .9s ease';
  v.addEventListener('canplay',function(){v.style.opacity='1';var p=v.play();if(p&&p.catch)p.catch(function(){});});
  v.addEventListener('error',function(){if(v.parentNode)v.parentNode.removeChild(v);});
  v.src='/wp-'+'content/'+'uploads/'+'2026/10/'+'gruppo-hero-video.mp4';
  wrap.appendChild(v);
})();
</script>"""
hero = get('2b73187f')
hero['elements'].append({"id": "7a1d0c01", "elType": "widget", "widgetType": "html", "elements": [], "settings": {"html": VID, "_css_classes": "iah-global"}})

# 3 timeline
html = get('0e14533d')['settings']['html']
html = html.replace('repeat(9,minmax(0,1fr))', 'repeat(8,minmax(0,1fr))')
old = ".iah-tl2 ol::before{content:\"\";position:absolute;left:0;right:0;top:50%;height:2px;background:linear-gradient(90deg,#4AB7D5,#1A4D6A);transform:translateY(-1px);}"
assert old in html
html = html.replace(old,
    ".iah-tl2 ol::before{content:\"\";position:absolute;left:0;right:6.25%;top:50%;height:2px;background:linear-gradient(90deg,#4AB7D5,#1A4D6A);transform:translateY(-1px);}\n.iah-tl2 li:last-child::after{content:\"\";position:absolute;left:50%;width:50%;top:50%;height:0;border-top:2px dashed #1A4D6A;transform:translateY(-1px);z-index:0;}")
old = ".iah-tl2 ol::before{left:11px;right:auto;top:8px;bottom:8px;width:2px;height:auto;transform:none;background:linear-gradient(180deg,#4AB7D5,#1A4D6A);}"
assert old in html
html = html.replace(old,
    ".iah-tl2 ol::before{display:none;}\n  .iah-tl2 li::before{content:\"\";position:absolute;left:-31px;top:15px;height:calc(100% + 30px);width:0;border-left:2px solid #4AB7D5;}\n  .iah-tl2 li:last-child::before{display:none;}\n  .iah-tl2 li:last-child::after{left:-31px;top:15px;width:0;height:64px;border-top:0;border-left:2px dashed #1A4D6A;transform:none;}\n  .iah-tl2 ol{padding-bottom:64px;}")
i0 = html.index('<li class="tl-up"><span class="tl-dot"')
i1 = html.index('</ol></div>')


def li(cls, year, text):
    return '<li class="%s"><span class="tl-dot" aria-hidden="true"></span><span class="tl-stem" aria-hidden="true"></span><div class="tl-txt"><span class="tl-year">%s</span><span class="tl-text">%s</span></div></li>\n' % (cls, year, text)


items = (li('tl-up', '2015', 'Nascita Iride Acque') + li('tl-down', '2016', '1° brevetto') + li('tl-up', '2020', '2° brevetto')
         + li('tl-down', '2023', 'Nascita del Gruppo Iride Acque con acquisizione Biemme Engineering') + li('tl-up', '2024', '3° brevetto')
         + li('tl-down', '2026', 'Ingresso di Credem Euromobiliare')
         + li('tl-up', 'Maggio 2026', 'Crescita del Gruppo Iride Acque con acquisizione Bieffe Costruzioni')
         + li('tl-down', 'Agosto 2026', 'Ingresso nella nuova Sede ad Arosio'))
html = html[:i0] + items + html[i1:]
setw('0e14533d', 'html', html)

# 4 certificazioni (allineate a BIEFFE: SOA aggiornate, 5 ISO/UNI, Modello 231)
c = get('a4d7333d')['settings']['html']
old = "@media(max-width:1024px){.iah-cert ul.soa{grid-template-columns:repeat(2,minmax(0,1fr));}.iah-cert ul.iso{grid-template-columns:repeat(3,minmax(0,1fr));}"
assert old in c
c = c.replace(old,
    "@media(max-width:1024px){.iah-cert ul.soa{grid-template-columns:repeat(2,minmax(0,1fr));}.iah-cert ul.iso{grid-template-columns:repeat(2,minmax(0,1fr));}.iah-cert ul.iso li:nth-child(n){grid-column:auto;}.iah-cert ul.iso li:last-child{grid-column:span 2;}")
old = ".iah-cert ul.iso{grid-template-columns:repeat(3,minmax(0,1fr));}"
assert old in c
c = c.replace(old,
    ".iah-cert ul.iso{grid-template-columns:repeat(6,minmax(0,1fr));}\n.iah-cert ul.iso li:nth-child(-n+3){grid-column:span 2;}\n.iah-cert ul.iso li:nth-child(n+4){grid-column:span 3;}\n.iah-cert ul.mod{grid-template-columns:repeat(1,minmax(0,1fr));}\n.iah-cert .cert-cls{font:700 12px/1 'Montserrat',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#4AB7D5;}\n.iah-cert .cert-txt{font:400 16px/1.55 'Montserrat',sans-serif;color:#3D5A6C;margin-top:6px;display:block;}")
old = ".iah-cert ul.soa,.iah-cert ul.iso{grid-template-columns:1fr;}"
assert old in c
c = c.replace(old, ".iah-cert ul.soa,.iah-cert ul.iso{grid-template-columns:1fr;}.iah-cert ul.iso li:last-child{grid-column:auto;}")
for code, cls, lbl in (('OG3', 'IV-bis', 'Strade'), ('OG6', 'VII', 'Acquedotti e fognature'), ('OG7', 'III', 'Opere marittime'), ('OS22', 'VII', 'Depuratori')):
    o = '<li class="cert-soa"><span class="cert-code">%s</span><span class="cert-lbl">%s</span></li>' % (code, lbl)
    assert o in c, code
    c = c.replace(o, '<li class="cert-soa"><span class="cert-cls">Classifica %s</span><span class="cert-code">%s</span><span class="cert-lbl">%s</span></li>' % (cls, code, lbl))
j0 = c.index('<li class="cert-iso"')
j1 = c.index('</ul>', j0)


def iso(ring, top, num):
    return '<li class="cert-iso" style="--ring:%s"><span class="cert-ring"><span>%s</span></span><span class="cert-num">%s</span></li>\n' % (ring, top, num)


isos = (iso('#4AB7D5', 'ISO', '9001') + iso('#2FBF71', 'ISO', '14001:2015') + iso('#F2683C', 'ISO', '45001:2018')
        + iso('#7B61FF', 'ISO', '50001:2018') + iso('#F2B63C', 'UNI', 'PdR 125:2022'))
c = c[:j0] + isos + c[j1:]
mod = """  <div class="cert-group">
    <h3 class="cert-h"><span class="cert-n">03</span>Modello organizzativo</h3>
    <ul class="mod">
<li class="cert-iso" style="--ring:#1A4D6A"><span class="cert-ring"><span>231</span></span><span><span class="cert-num">Modello 231 e Compliance</span><span class="cert-txt">BIEFFE Costruzioni S.r.l. ha adottato un Modello di Organizzazione, Gestione e Controllo ai sensi del D.Lgs. 231/2001, a conferma del proprio impegno verso una gestione aziendale trasparente, responsabile e orientata al rispetto delle normative vigenti.</span></span></li>
    </ul>
  </div>
"""
k = c.rindex('</div>')
c = c[:k] + mod + c[k:]
setw('a4d7333d', 'html', c)

# 5 modello operativo
setw('3207083b', 'editor', '<p>IL NOSTRO MODELLO OPERATIVO</p>')
setw('212fa975', 'title', "Un metodo integrato, dall'analisi alla realizzazione e gestione")
P1 = "Gruppo Iride Acque adotta un approccio strutturato che accompagna ogni progetto lungo l'intero ciclo di vita dell'impianto, dall'analisi delle esigenze e dalla progettazione fino alla realizzazione, messa in servizio e successiva gestione."
P2 = "Il nostro modello operativo si articola in quattro fasi fondamentali, integrando competenze tecniche, ingegneristiche e gestionali per sviluppare soluzioni affidabili, efficienti e personalizzate."
P3 = "Questo approccio consente di considerare fin dalle prime valutazioni gli aspetti tecnici, normativi ed economici, ottimizzando gli investimenti, i costi di esercizio e le prestazioni dell'impianto nel tempo."
setw('dd62f1cf', 'editor', '<p>%s</p><p>%s</p><p>%s</p>' % (P1, P2, P3))
get('dd62f1cf')['settings']['custom_css'] = "selector, selector p{font-size:21px !important;line-height:1.65 !important;margin:0 0 14px !important;}\n@media(max-width:767px){ selector, selector p{font-size:18px !important;} }"
get('7c545aad')['settings']['_element_id'] = 'modello-operativo'

S_P = "color:#1A4D6A;font-weight:800;font-size:14px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 10px;font-family:Montserrat,sans-serif;"
S_H = "color:#09171F;font-weight:800;font-size:30px;margin:0 0 14px;font-family:Montserrat,sans-serif;"
S_B = "color:#3D5A6C;font-size:18px;line-height:1.7;margin:0 0 20px;font-family:Montserrat,sans-serif;"
S_LI = "position:relative;padding-left:34px;font-size:17.5px;line-height:1.5;color:#3D5A6C;font-weight:400;font-family:Montserrat,sans-serif;"
S_CK = "position:absolute;left:0;top:.15em;width:22px;height:22px;border-radius:50%;background:#4AB7D5;color:#09171F;font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center;line-height:1;"


def tab(n, title, body, its):
    h = '<p style="%s">FASE 0%d</p><h3 style="%s">%s</h3><p style="%s">%s</p>' % (S_P, n, S_H, title, S_B, body)
    if its:
        h += '<ul style="margin:0;padding:0;list-style:none;display:grid;gap:14px;">' + ''.join('<li style="%s"><span style="%s">&#10003;</span>%s</li>' % (S_LI, S_CK, t) for t in its) + '</ul>'
    return h


T = [
    ("01  Analisi di processo e studio di fattibilità", tab(1, "Analisi di processo e studio di fattibilità", "La fase preliminare comprende l'analisi delle esigenze del cliente e delle caratteristiche delle acque/acque reflue da trattare, la verifica dei requisiti normativi (AUA, AIA) e autorizzativi applicabili, la valutazione degli spazi disponibili e lo studio della fattibilità tecnico-economica delle possibili soluzioni impiantistiche.", [])),
    ("02  Progettazione e ingegneria", tab(2, "Progettazione e ingegneria", "Sulla base delle valutazioni preliminari, sviluppiamo la progettazione dell'impianto, definendo le tecnologie di trattamento, il dimensionamento delle apparecchiature, il layout impiantistico e i sistemi di automazione e controllo. Particolare attenzione viene dedicata all'efficienza energetica, all'affidabilità e alla facilità di gestione e manutenzione.", ["Progettazione di processo e dimensionamento delle sezioni di trattamento", "Progettazione meccanica, idraulica ed elettrostrumentale", "Definizione del layout, schemi P&amp;ID e specifiche tecniche", "Progettazione dell'automazione e predisposizione degli elaborati esecutivi"])),
    ("03  Realizzazione, collaudo e avviamento", tab(3, "Realizzazione, collaudo e avviamento", "La fase realizzativa comprende la fornitura delle apparecchiature, la costruzione, l'assemblaggio e l'installazione dell'impianto, secondo le specifiche del progetto esecutivo. Seguono i collaudi funzionali, l'avviamento e la regolazione dei parametri di processo, con verifica delle prestazioni rispetto agli obiettivi progettuali e preparazione alla consegna operativa dell'impianto.", ["Fornitura, costruzione e assemblaggio delle sezioni impiantistiche", "Installazione e collegamenti meccanici, idraulici ed elettrici", "Collaudi funzionali, avviamento e ottimizzazione dei parametri di processo", "Verifica delle prestazioni, formazione degli operatori e consegna della documentazione tecnica e as-built"])),
    ("04  Gestione, manutenzione e ottimizzazione", tab(4, "Gestione, manutenzione e ottimizzazione", "La fase di gestione comprende le attività di conduzione, monitoraggio e manutenzione degli impianti, con l'obiettivo di garantire continuità operativa, affidabilità e prestazioni costanti nel tempo. Attraverso controlli periodici e interventi mirati, supportiamo il cliente nell'ottimizzazione dei processi, nella riduzione dei costi di esercizio e nel rispetto dei requisiti normativi.", ["Conduzione operativa, supervisione e monitoraggio degli impianti", "Manutenzione ordinaria, straordinaria e programmata", "Controllo delle prestazioni e ottimizzazione dei consumi energetici e dei reagenti", "Assistenza tecnica, verifiche analitiche e reportistica periodica"])),
]
CSS = ("selector{margin-top:34px;}\nselector .elementor-tabs-wrapper { display:flex!important; flex-wrap:wrap; gap:12px; margin-bottom:22px; }\n"
       "selector .elementor-tab-desktop-title { padding: 18px 26px !important; border-radius: 999px !important; background:#FFFFFF !important; border:0!important; box-shadow:0 10px 30px -18px rgba(9,23,31,.35); transition: background .3s ease, color .3s ease; }\n"
       "selector .elementor-tab-desktop-title:hover { background:#DDEFF6 !important; }\nselector .elementor-tab-desktop-title.elementor-active { background:#4AB7D5 !important; }\n"
       "selector .elementor-tab-title, selector .elementor-tab-title a { color:#09171F !important; }\n"
       "selector .elementor-tab-desktop-title::before, selector .elementor-tab-desktop-title::after { display:none!important; }\n"
       "selector .elementor-tabs-content-wrapper { background:#FFFFFF !important; border-radius:28px !important; padding:56px !important; border:0!important; box-shadow:0 30px 70px -30px rgba(9,23,31,.3); }\n"
       "selector .elementor-tab-content { border:0!important; }\nselector .elementor-tab-mobile-title { color:#09171F!important; background:#EEF6FA!important; border-radius:14px; margin-bottom:8px; border:0!important; }\n"
       "selector .elementor-tab-mobile-title.elementor-active { background:#4AB7D5!important; }\n@media(max-width:767px){ selector .elementor-tabs-content-wrapper{ padding:24px !important; } }")
tabs = {"id": "7a1d0c02", "elType": "widget", "widgetType": "tabs", "elements": [], "settings": {
    "type": "horizontal",
    "tabs": [{"_id": "mo0000%d" % (n + 1), "tab_title": t[0], "tab_content": t[1]} for n, t in enumerate(T)],
    "tab_color": "#09171F", "tab_active_color": "#FFFFFF", "background_color": "transparent",
    "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
    "tab_typography_typography": "custom", "tab_typography_font_family": "Montserrat", "tab_typography_font_weight": "700", "tab_typography_font_size": {"unit": "px", "size": 17},
    "content_color": "#3D5A6C", "content_typography_typography": "custom", "content_typography_font_family": "Montserrat", "content_typography_font_weight": "400", "content_typography_font_size": {"unit": "px", "size": 17.5},
    "custom_css": CSS}}
get('86fe368f')['elements'].append(tabs)

os.makedirs('ilgruppo', exist_ok=True)
names = {'2b73187f': 't1_hero', 'e5a62aaf': 't2_intro', '6369a71d': 't3_timeline', 'c7368ede': 't4_cert', '7c545aad': 't5_metodo'}
for e in d:
    out = json.dumps([e], ensure_ascii=False, separators=(',', ':'))
    io.open('ilgruppo/%s.json' % names[e['id']], 'w', encoding='utf8').write(out)
    print(names[e['id']], len(out))
