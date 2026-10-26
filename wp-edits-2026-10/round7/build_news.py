import json, os
OUT = os.path.join(os.path.dirname(__file__), 'news')
os.makedirs(OUT, exist_ok=True)

M = lambda v: {"unit": "px", "top": str(v[0]), "right": str(v[1]), "bottom": str(v[2]), "left": str(v[3]), "isLinked": False}
def te(id_, text, color, size, weight='400', lh=None, extra=None, msize=None, ls=None):
    s = {"editor": "<p>%s</p>" % text, "text_color": color, "typography_typography": "custom",
         "typography_font_family": "Montserrat", "typography_font_weight": weight,
         "typography_font_size": {"unit": "px", "size": size}}
    if lh: s["typography_line_height"] = {"unit": "em", "size": lh}
    if msize: s["typography_font_size_mobile"] = {"unit": "px", "size": msize}
    if ls: s["typography_letter_spacing"] = {"unit": "px", "size": ls}
    if extra: s.update(extra)
    return {"id": id_, "elType": "widget", "widgetType": "text-editor", "settings": s, "elements": []}
def hd(id_, text, color, size, msize, tag='h3', lh=1.25):
    return {"id": id_, "elType": "widget", "widgetType": "heading", "elements": [], "settings": {
        "title": text, "header_size": tag, "title_color": color, "typography_typography": "custom",
        "typography_font_family": "Montserrat", "typography_font_weight": "800",
        "typography_font_size": {"unit": "px", "size": size}, "typography_line_height": {"unit": "em", "size": lh},
        "typography_font_size_mobile": {"unit": "px", "size": msize}}}
def btn(id_, text, url, size=16, ext=False):
    return {"id": id_, "elType": "widget", "widgetType": "button", "elements": [], "settings": {
        "text": text, "link": {"url": url, "is_external": "on" if ext else "", "nofollow": ""},
        "border_radius": {"unit": "px", "top": "999", "right": "999", "bottom": "999", "left": "999", "isLinked": True},
        "typography_typography": "custom", "typography_font_family": "Montserrat", "typography_font_weight": "700",
        "typography_font_size": {"unit": "px", "size": size}, "text_padding": M((17, 30, 17, 30)),
        "background_color": "#4AB7D5", "button_text_color": "#09171F",
        "button_background_hover_color": "rgba(74,183,213,0.8)", "hover_color": "#09171F"}}
def cont(id_, settings, elements, inner=True):
    return {"id": id_, "elType": "container", "isInner": inner, "settings": settings, "elements": elements}

# ---------- t1 hero (html + video) ----------
hero_html = """<style>
.brand-hero{position:relative;overflow:hidden;background:#09171F;display:flex;flex-direction:column;min-height:100vh;}
.brand-hero .bh-media{position:absolute;inset:0;width:100%;height:100%;}
.brand-hero .bh-media img{width:100%;height:100%;object-fit:cover;object-position:right center;}
.brand-hero .bh-scrim{position:absolute;inset:0;background:linear-gradient(100deg, rgba(9,23,31,.94) 0%, rgba(9,23,31,.86) 38%, rgba(9,23,31,.55) 65%, rgba(9,23,31,.35) 100%);pointer-events:none;}
.brand-hero .bh-copy{position:relative;z-index:5;flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 16px;box-sizing:border-box;}
.brand-hero .bh-copy-inner{width:100%;max-width:1240px;margin:0 auto;}
.brand-hero .hero-kicker{color:#8DD6E8;font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin-bottom:18px;font-family:'Montserrat',sans-serif;display:block;}
.brand-hero .hero-h1{color:#fff;font-weight:800;letter-spacing:-.01em;line-height:1.08;font-size:clamp(2.2rem,5.2vw,4.4rem);max-width:900px;text-shadow:0 4px 30px rgba(0,0,0,.35);font-family:'Montserrat',sans-serif;margin:0;}
.brand-hero .hero-h1 .accent{background:linear-gradient(90deg,#8DD6E8,#4AB7D5);-webkit-background-clip:text;background-clip:text;color:transparent;}
.brand-hero .hero-ctas{display:flex;gap:16px;flex-wrap:wrap;margin-top:38px;}
.brand-hero .btn-cta{display:inline-flex;align-items:center;gap:8px;padding:17px 30px;border-radius:999px;font-size:15px;font-weight:700;letter-spacing:.02em;background:#4AB7D5;color:#09171F;box-shadow:0 8px 24px rgba(74,183,213,.35);transition:transform .35s cubic-bezier(.22,.61,.36,1), box-shadow .35s cubic-bezier(.22,.61,.36,1), background .35s cubic-bezier(.22,.61,.36,1);border:none;cursor:pointer;font-family:'Montserrat',sans-serif;text-decoration:none;}
.brand-hero .btn-cta:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(74,183,213,.45);background:#8DD6E8;}
.brand-hero .hero-subtitle{color:rgba(238,246,250,.86);font-size:20px;line-height:1.65;max-width:760px;margin:26px 0 0;font-family:'Montserrat',sans-serif;font-weight:300;}
</style>
<section class="brand-hero" id="bhHeroNews">
  <div class="bh-media"><img src="https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/09/hero-template-bg.webp" alt=""></div>
  <div class="bh-scrim"></div>
  <div class="bh-copy">
    <div class="bh-copy-inner">
      <span class="hero-kicker">News</span>
      <h1 class="hero-h1">Media &amp; <span class="accent">Awards</span></h1>
    </div>
  </div>
</section>
<script>
(function(){
  var hero = document.getElementById('bhHeroNews');
  if(!hero) return;
  function setH(){
    var header = document.querySelector('header.elementor-location-header');
    var hh = header ? header.getBoundingClientRect().height : 0;
    hero.style.minHeight = 'calc(100vh - ' + hh + 'px)';
  }
  setH();
  window.addEventListener('resize', setH);
  window.addEventListener('load', setH);
})();
</script>
"""
video_js = """<script>
(function(){
  var wrap=document.querySelector('#bhHeroNews .bh-media'); if(!wrap) return;
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
t1 = [cont("918fe10d", {"flex_direction": "column", "flex_direction_mobile": "column", "css_id": "sec-bhHeroNews",
        "content_width": "full", "padding": M((0, 0, 0, 0)), "margin": M((0, 0, 0, 0))},
        [{"id": "64ee17d2", "elType": "widget", "widgetType": "html", "settings": {"html": hero_html}, "elements": []},
         {"id": "64ee17d3", "elType": "widget", "widgetType": "html", "settings": {"html": video_js, "_css_classes": "iah-global"}, "elements": []}],
        inner=False)]

# ---------- t2 news (2 cards) ----------
def card(cid, n, date, title, excerpt, url, media_id, media_url, alt):
    cs = {"flex_direction": "column", "flex_direction_mobile": "column", "content_width": "full",
          "flex_gap": {"unit": "px", "size": 16, "column": "16", "row": "16"},
          "flex_gap_mobile": {"unit": "px", "size": 14, "column": "14", "row": "14"},
          "background_background": "classic", "background_color": "#FFFFFF",
          "border_radius": {"unit": "px", "top": "28", "right": "28", "bottom": "28", "left": "28", "isLinked": True},
          "padding": M((0, 0, 38, 0)), "padding_mobile": M((0, 0, 26, 0)),
          "box_shadow_box_shadow_type": "yes",
          "box_shadow_box_shadow": {"horizontal": 0, "vertical": 24, "blur": 60, "spread": -28, "color": "rgba(9,23,31,.28)"},
          "custom_css": "selector { width: calc(50% - 14px) !important; flex: 0 0 calc(50% - 14px) !important; overflow:hidden; }\nselector img{aspect-ratio:3/2;object-fit:cover;width:100%;display:block;}\nselector .iah-news-body{padding-left:38px;padding-right:38px;}\n@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } selector .iah-news-body{padding-left:22px;padding-right:22px;} }",
          "border_border": "solid", "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
          "border_color": "rgba(9,23,31,.10)"}
    img = {"id": cid + "01", "elType": "widget", "widgetType": "image", "elements": [], "settings": {
        "image": {"url": media_url, "id": media_id, "alt": alt}, "image_size": "large",
        "width": {"unit": "%", "size": 100}, "image_border_radius": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}}}
    body = lambda w, i: dict(w, settings=dict(w["settings"], _css_classes="iah-news-body"))
    return cont(cid, cs, [
        img,
        body(te(cid + "02", "News di Gruppo · " + date, "#4AB7D5", 14, '800', ls=1.2), 0),
        body(hd(cid + "03", title, "#09171F", 26, 22), 0),
        body(te(cid + "04", excerpt, "#3D5A6C", 17.5, '400', lh=1.7), 0),
        cont(cid + "05", {"flex_direction": "row", "flex_direction_mobile": "column", "content_width": "full",
                          "padding": M((6, 38, 0, 38)), "padding_mobile": M((4, 22, 0, 22))},
             [btn(cid + "06", "Leggi la news →", url, 16, True)])])

cards = [
    card("c3e1a001", 1, "15 maggio 2026", "Novità: 3 milioni da Credem e seconda acquisizione in tre anni",
         "Investimento da 3 milioni di Credem e nuova acquisizione: Iride Acque copre tutta la filiera. Obiettivo 2026: 13 milioni di fatturato",
         "https://www.irideacque.com/iride-acque-3-milioni-da-credem-e-seconda-acquisizione-in-tre-anni/", 517,
         "https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/10/news-credem-3-milioni-investimento.webp",
         "Foto di gruppo con i rappresentanti di Credem e del Gruppo Iride Acque dopo l'annuncio dell'investimento"),
    card("c3e1a002", 2, "8 ottobre 2026", "Ecomondo 2026 a Rimini: date, programma e novità sull’acqua",
         "Ecomondo 2026 a Rimini: programma, novità e cosa cambia per il trattamento delle acque reflue, dal riuso al Circular Economy Act",
         "https://www.irideacque.com/ecomondo-2026-date-programma-e-novita/", 518,
         "https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/10/news-ecomondo-2026-rimini.webp",
         "Installazione Ecomondo, The green technology expo, nel padiglione fieristico di Rimini"),
]
t2 = [cont("9753bd21", {"flex_direction": "column", "flex_direction_mobile": "column", "css_id": "sec-news-gruppo",
        "content_width": "full", "background_background": "classic", "background_color": "#FFFFFF",
        "padding": M((110, 24, 110, 24)), "padding_mobile": M((70, 16, 70, 16)), "margin": M((0, 0, 0, 0)),
        "_element_id": "news-gruppo"},
        [cont("2080c163", {"flex_direction": "column", "flex_direction_mobile": "column", "content_width": "boxed",
                           "boxed_width": {"unit": "px", "size": 1240},
                           "flex_gap": {"unit": "px", "size": 18, "column": "18", "row": "18"},
                           "flex_gap_mobile": {"unit": "px", "size": 14, "column": "14", "row": "14"}},
              [te("04e47fa4", "News di Gruppo", "#1A4D6A", 19, '800', msize=17, ls=1.4),
               hd("470724c8", "Le novità del Gruppo Iride Acque", "#09171F", 46, 29, 'h2', 1.15)]),
         cont("985ef45b", {"flex_direction": "row", "flex_direction_mobile": "column", "content_width": "boxed",
                           "boxed_width": {"unit": "px", "size": 1240}, "flex_wrap": "wrap",
                           "flex_gap": {"unit": "px", "size": 28, "column": "28", "row": "28"},
                           "flex_gap_mobile": {"unit": "px", "size": 20, "column": "20", "row": "20"},
                           "padding": M((48, 0, 0, 0)), "padding_mobile": M((28, 0, 0, 0))}, cards)],
        inner=False)]

# ---------- t3 news dalle aziende (as before) ----------
def az(cid, title, text, label, url):
    return cont(cid, {"flex_direction": "column", "flex_direction_mobile": "column", "content_width": "full",
                      "flex_gap": {"unit": "px", "size": 16, "column": "16", "row": "16"},
                      "flex_gap_mobile": {"unit": "px", "size": 14, "column": "14", "row": "14"},
                      "background_background": "classic", "background_color": "#123852",
                      "border_radius": {"unit": "px", "top": "28", "right": "28", "bottom": "28", "left": "28", "isLinked": True},
                      "padding": M((38, 34, 38, 34)), "padding_mobile": M((28, 22, 28, 22)),
                      "custom_css": "selector { width: calc(33.333% - 16px) !important; flex: 0 0 calc(33.333% - 16px) !important; }\n@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } }"},
                [hd(cid + "01", title, "#FFFFFF", 26, 22),
                 te(cid + "02", text, "rgba(238,246,250,.85)", 17, '300', lh=1.7),
                 cont(cid + "03", {"flex_direction": "row", "flex_direction_mobile": "column", "content_width": "full",
                                   "padding": M((6, 0, 0, 0)), "padding_mobile": M((4, 0, 0, 0)),
                                   "custom_css": "selector{margin-top:auto;}"},
                      [btn(cid + "04", label, url, 15.5, True)])])
t3 = [cont("36f706c5", {"flex_direction": "column", "flex_direction_mobile": "column", "css_id": "sec-news-aziende",
        "content_width": "full", "background_background": "classic", "background_color": "#09171F",
        "padding": M((110, 24, 110, 24)), "padding_mobile": M((70, 16, 70, 16)), "margin": M((0, 0, 0, 0)),
        "_element_id": "news-aziende"},
        [cont("216c2a15", {"flex_direction": "column", "flex_direction_mobile": "column", "content_width": "boxed",
                           "boxed_width": {"unit": "px", "size": 1240},
                           "flex_gap": {"unit": "px", "size": 18, "column": "18", "row": "18"},
                           "flex_gap_mobile": {"unit": "px", "size": 14, "column": "14", "row": "14"}},
              [te("f6fb18de", "News dalle Aziende", "#8DD6E8", 19, '800', msize=17, ls=1.4),
               hd("8cf5365e", "Dalle società del Gruppo", "#FFFFFF", 46, 29, 'h2', 1.15)]),
         cont("4f895ce9", {"flex_direction": "row", "flex_direction_mobile": "column", "content_width": "boxed",
                           "boxed_width": {"unit": "px", "size": 1240}, "flex_wrap": "wrap",
                           "flex_gap": {"unit": "px", "size": 24, "column": "24", "row": "24"},
                           "flex_gap_mobile": {"unit": "px", "size": 18, "column": "18", "row": "18"},
                           "padding": M((48, 0, 0, 0)), "padding_mobile": M((28, 0, 0, 0))},
              [az("228a8ae8", "Iride Acque", "Approfondimenti su trattamento delle acque industriali, tecnologie proprietarie, Ricerca &amp; Sviluppo, recupero e riutilizzo delle acque, contaminanti emergenti e Case Studies applicativi.", "Scopri le news di Iride Acque →", "https://irideacque.com/"),
               az("d5eabbaf", "Biemme Engineering", "News e approfondimenti su trattamento delle acque di processo, potabilizzazione, disinfezione, sistemi di dosaggio e controllo, Food &amp; Beverage e hospitality.", "Scopri le news di Biemme Engineering →", "https://www.biemmeengineering.it/"),
               az("1c1288cf", "Bieffe Costruzioni", "Aggiornamenti su cantieri, infrastrutture idriche, reti acquedottistiche e fognarie, impianti di depurazione, manutenzione e progetti per multiutility ed enti pubblici.", "Scopri le news di Bieffe Costruzioni →", "https://costruzionibieffe.it/")])],
        inner=False)]

for name, data in (('t1_hero', t1), ('t2_news', t2), ('t3_aziende', t3)):
    with open(os.path.join(OUT, name + '.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    print(name, os.path.getsize(os.path.join(OUT, name + '.json')))
