"""Generatore delle pagine Applicazioni e Servizi / Settori (23/10).
CSS condiviso -> pages/site.css (va in Aspetto > CSS aggiuntivo). Pagine -> pages/<nome>.json (template sezione)."""
import json, os, html as H
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'pages'); os.makedirs(OUT, exist_ok=True)
SITE = 'https://gruppoirideacque.propagandaadv.com'
HERO_IMG = SITE + '/wp-content/uploads/2026/09/hero-template-bg.webp'

# ---------------------------------------------------------------- icone
ICONS = {
 'docsearch': '<path d="M6 3h8l4 4v5M6 3v18h6M14 3v4h4"/><circle cx="16" cy="17" r="3"/><path d="M18.2 19.2L21 22"/>',
 'chart': '<path d="M6 20v-7M12 20V5M18 20v-10"/>',
 'monitor': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 'crane': '<path d="M4 21V3M4 6h16M12 6v6M10 12h4v4h-4zM20 6v3"/>',
 'gear': '<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>',
 'headset': '<path d="M4 14v-2a8 8 0 0116 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/><path d="M19 20c0 1.5-2 2-5 2"/>',
 'wrench': '<path d="M21 7a5 5 0 01-7 5L6 20a2 2 0 01-3-3l8-8a5 5 0 017-5l-3 3 1 2 2 1z"/>',
 'leaf': '<path d="M5 19c0-9 5-14 15-14 0 10-5 15-13 15M5 19l8-8"/>',
 'drop': '<path d="M12 3s6 6.5 6 11a6 6 0 01-12 0c0-4.5 6-11 6-11z"/>',
 'clip': '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 14l2 2 4-4"/>',
 'db': '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3 3 7 3s7-1.3 7-3V6M5 12v6c0 1.7 3 3 7 3s7-1.3 7-3v-6"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'flask': '<path d="M9 3h6M10 3v6l-5 9a2 2 0 002 3h10a2 2 0 002-3l-5-9V3"/>',
 'recycle': '<path d="M20 12a8 8 0 00-14-5M4 12a8 8 0 0014 5M6 3v4h4M18 21v-4h-4"/>',
 'scale': '<path d="M12 4v16M6 20h12M4 8h16M6 8l-3 7a3 3 0 006 0zM18 8l-3 7a3 3 0 006 0z"/>',
 'truck': '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 'hands': '<path d="M3 11l5-4 4 2 4-2 5 4M7 15l3 3M10 13l4 4M13 11l5 5"/>',
 'docs': '<rect x="8" y="3" width="11" height="14" rx="1.5"/><path d="M5 7v14h11M11 8h5M11 12h5"/>',
 'plant': '<rect x="4" y="9" width="7" height="12" rx="1.5"/><rect x="13" y="5" width="7" height="16" rx="1.5"/><path d="M3 21h18"/>',
 'alert': '<circle cx="12" cy="12" r="9"/><path d="M12 7v6M12 16.5v.5"/>',
 'tools': '<path d="M14 6a4 4 0 005 5l-9 9a2 2 0 01-3-3zM4 4l5 5M9 4L4 9"/>',
 'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/>',
 'factory': '<path d="M3 21V9l6 4V9l6 4V6h6v15zM3 21h18"/>',
 'building': '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2M10 21v-3h4v3"/>',
 'network': '<circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M12 7v5M12 12l-6 5M12 12l6 5"/>',
}
def icon_css():
    out = []
    for k, v in ICONS.items():
        svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#1A4D6A" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % v
        enc = svg.replace('%', '%25').replace('"', "'").replace('<', '%3C').replace('>', '%3E').replace('#', '%23')
        out.append('.iah2-i-%s{--i:url("data:image/svg+xml,%s")}' % (k, enc))
    return '\n'.join(out)

CSS = r"""/* ===== Gruppo Iride Acque - pagine Applicazioni, Servizi, Settori (23/10/2026) ===== */
.iah2-hero{position:relative;overflow:hidden;background:#09171F;display:flex;flex-direction:column;min-height:calc(100vh - 90px);font-family:'Montserrat',sans-serif}
.iah2-hero .bh-media{position:absolute;inset:0}.iah2-hero .bh-media img{width:100%;height:100%;object-fit:cover;object-position:right center}
.iah2-hero .bh-scrim{position:absolute;inset:0;background:linear-gradient(100deg,rgba(9,23,31,.94) 0%,rgba(9,23,31,.86) 38%,rgba(9,23,31,.6) 65%,rgba(9,23,31,.45) 100%);pointer-events:none}
.iah2-hero .bh-copy{position:relative;z-index:5;flex:1;display:flex;flex-direction:column;justify-content:center;padding:90px 16px;box-sizing:border-box}
.iah2-hero .bh-in{width:100%;max-width:1240px;margin:0 auto}
.iah2-hero .kick{display:block;color:#8DD6E8;font-size:16px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin:0 0 18px}
.iah2-hero h1{margin:0;color:#fff;font-weight:800;letter-spacing:-.01em;line-height:1.1;font-size:clamp(2.1rem,3.7vw,3.4rem);max-width:980px;text-shadow:0 4px 30px rgba(0,0,0,.35)}
.iah2-hero .sub p{margin:22px 0 0;max-width:880px;color:rgba(238,246,250,.92);font-size:21px;line-height:1.65;font-weight:300}
.iah2-hero .sub a{color:#8DD6E8;text-decoration:underline;text-underline-offset:3px}
@media(max-width:767px){.iah2-hero .sub p{font-size:18px}.iah2-hero .bh-copy{padding:60px 16px}}
.iah2-sec{font-family:'Montserrat',sans-serif;padding:110px 24px;box-sizing:border-box}
.iah2-sec.wh{background:#fff}.iah2-sec.lt{background:#EEF6FA}.iah2-sec.dk{background:#09171F}
.iah2-in{max-width:1240px;margin:0 auto}
.iah2-eb{margin:0;font-weight:800;font-size:19px;line-height:1.3;letter-spacing:.08em;text-transform:uppercase;color:#1A4D6A}
.dk .iah2-eb{color:#8DD6E8}
.iah2-h2{margin:14px 0 0;font-weight:800;font-size:46px;line-height:1.15;color:#09171F}
.dk .iah2-h2{color:#fff}
.iah2-h2 .ac{background:linear-gradient(90deg,#4AB7D5,#1A4D6A);-webkit-background-clip:text;background-clip:text;color:transparent}
.dk .iah2-h2 .ac{background:linear-gradient(90deg,#8DD6E8,#4AB7D5);-webkit-background-clip:text;background-clip:text}
.iah2-lead{margin:20px 0 0;max-width:880px;font-size:21px;line-height:1.65;font-weight:400;color:#3D5A6C}
.dk .iah2-lead{color:rgba(238,246,250,.86)}
.iah2-lead a,.iah2-card a.in{color:#1A4D6A;font-weight:700}
.iah2-grid{display:grid;gap:24px;margin-top:52px}
.iah2-grid.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.iah2-grid.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.iah2-grid.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.iah2-card{display:flex;flex-direction:column;gap:12px;background:#fff;border:1px solid rgba(9,23,31,.1);border-radius:24px;padding:34px 30px;box-shadow:0 18px 44px -28px rgba(9,23,31,.4);box-sizing:border-box}
.iah2-card h3{margin:0;font-weight:800;font-size:23px;line-height:1.25;color:#09171F}
.iah2-card p{margin:0;font-size:17.5px;line-height:1.65;font-weight:400;color:#3D5A6C}
.iah2-card .go{margin-top:auto;padding-top:10px;font-weight:700;font-size:17px;color:#1A4D6A;text-decoration:none}
.iah2-card .go:hover{text-decoration:underline}
.iah2-card.hz{flex-direction:row;align-items:center;gap:22px}
.iah2-card.hz .iah2-ic{margin:0;flex:0 0 64px}
.iah2-ic{flex:0 0 auto;display:block;width:64px;height:64px;border-radius:50%;background:#DDEFF6 var(--i) center/30px 30px no-repeat;margin-bottom:8px}
.iah2-steps{display:grid;gap:24px;margin-top:56px}
.iah2-steps.c3{grid-template-columns:repeat(3,minmax(0,1fr))}.iah2-steps.c4{grid-template-columns:repeat(4,minmax(0,1fr))}
.iah2-step{position:relative;text-align:center}
.iah2-step .iah2-ic{width:88px;height:88px;background-size:40px 40px;margin:0 auto 22px;border:2px solid #4AB7D5;background-color:#fff;position:relative;z-index:2}
.iah2-step .box{background:#fff;border:1px solid rgba(9,23,31,.08);border-radius:24px;padding:28px 24px;box-shadow:0 18px 44px -28px rgba(9,23,31,.35);height:calc(100% - 110px);box-sizing:border-box}
.iah2-step h3{margin:0 0 10px;font-weight:800;font-size:22px;line-height:1.25;color:#09171F}
.iah2-step p{margin:0;font-size:17.5px;line-height:1.6;color:#3D5A6C}
.iah2-steps:not(.ar) .iah2-step::before{content:"";position:absolute;top:43px;left:-12px;right:-12px;height:2px;background:#4AB7D5;z-index:1}
.iah2-steps.c3:not(.ar) .iah2-step:nth-child(3n+1)::before,.iah2-steps.c4:not(.ar) .iah2-step:nth-child(4n+1)::before{left:50%}
.iah2-steps.c3:not(.ar) .iah2-step:nth-child(3n)::before,.iah2-steps.c4:not(.ar) .iah2-step:nth-child(4n)::before{right:50%}
.iah2-steps.ar .iah2-step:not(:nth-child(4n))::after{content:"\2192";position:absolute;top:30px;right:-24px;width:24px;font-size:30px;line-height:1;color:#4AB7D5}
.iah2-set{position:relative;overflow:hidden;background:#09171F;font-family:'Montserrat',sans-serif;padding:110px 24px 90px;box-sizing:border-box}
.iah2-set .bgi{position:absolute;inset:0}.iah2-set .bgi img{width:100%;height:100%;object-fit:cover}
.iah2-set .bgi::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(9,23,31,.82) 0%,rgba(9,23,31,.7) 55%,rgba(9,23,31,.92) 100%)}
.iah2-set .iah2-in{position:relative;z-index:2}
.iah2-set .iah2-h2{color:#fff}
.iah2-set .iah2-grid{margin-top:150px}
.iah2-sub-row{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr);gap:48px;align-items:center;margin-top:56px}
.iah2-sub-row:nth-child(even) .pic{order:2}
.iah2-sub-row .pic{aspect-ratio:3/2;border-radius:24px;overflow:hidden;background:#123852 var(--ph) center/cover no-repeat}
.iah2-sub-row h3{margin:0;font-weight:800;font-size:30px;line-height:1.2;color:#09171F}
.iah2-sub-row p{margin:14px 0 0;font-size:19px;line-height:1.65;color:#3D5A6C}
.iah2-sub-row .go{display:inline-block;margin-top:18px;font-weight:700;font-size:17px;color:#1A4D6A;text-decoration:none}
.iah2-sub-row .go:hover{text-decoration:underline}
.iah2-ind{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 28px;margin-top:48px}
.iah2-ind .it{display:flex;gap:20px;align-items:center;background:#fff;border:1px solid rgba(9,23,31,.1);border-radius:20px;padding:16px;box-shadow:0 14px 36px -26px rgba(9,23,31,.4)}
.iah2-ind .pic{flex:0 0 120px;height:90px;border-radius:14px;background:#123852 var(--ph) center/cover no-repeat}
.iah2-ind h3{margin:0;font-weight:800;font-size:20px;line-height:1.25;color:#09171F}
.iah2-ind p{margin:6px 0 0;font-size:16px;line-height:1.5;color:#3D5A6C}
.iah2-vid{display:none}
@media(max-width:1180px){.iah2-grid.g4{grid-template-columns:repeat(2,minmax(0,1fr))}.iah2-steps.c4{grid-template-columns:repeat(2,minmax(0,1fr))}.iah2-steps.c4 .iah2-step::before,.iah2-steps.c4 .iah2-step::after{display:none!important}.iah2-steps.c3{grid-template-columns:repeat(2,minmax(0,1fr))}.iah2-steps.c3 .iah2-step::before{display:none}}
@media(max-width:1024px){.iah2-grid.g3{grid-template-columns:repeat(2,minmax(0,1fr))}.iah2-sub-row{grid-template-columns:1fr}.iah2-sub-row:nth-child(even) .pic{order:0}.iah2-set .iah2-grid{margin-top:90px}}
@media(max-width:767px){.iah2-sec{padding:70px 16px}.iah2-set{padding:70px 16px}.iah2-h2{font-size:29px}.iah2-lead{font-size:18px}.iah2-eb{font-size:17px}.iah2-grid{margin-top:36px;gap:18px}.iah2-grid.g2,.iah2-grid.g3,.iah2-grid.g4,.iah2-steps.c3,.iah2-steps.c4,.iah2-ind{grid-template-columns:1fr}.iah2-card{padding:26px 22px}.iah2-card.hz{flex-direction:column;align-items:flex-start}.iah2-card h3{font-size:21px}.iah2-card p,.iah2-step p{font-size:16.5px}.iah2-steps{gap:18px}.iah2-step .box{height:auto}.iah2-step:not(:last-child)::after{content:"";display:block!important;position:absolute;left:50%;bottom:-18px;width:2px;height:18px;background:#4AB7D5;margin-left:-1px;top:auto;right:auto;font-size:0}.iah2-sub-row h3{font-size:25px}.iah2-sub-row p{font-size:17px}.iah2-ind .pic{flex-basis:84px;height:70px}}
"""

# ---------------------------------------------------------------- helper
_n = [0x1000]
def nid():
    _n[0] += 1
    return '%08x' % (0x5a000000 + _n[0] * 37)

def esc(t):  # testo gia' pronto in HTML: non toccare; per testo semplice usare H.escape
    return t

def wrap(html_str, cls=None, css_id=None, anchor=None):
    s = {"content_width": "full", "flex_direction": "column",
         "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
         "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}}
    if css_id: s["css_id"] = css_id
    return {"id": nid(), "elType": "container", "isInner": False, "settings": s, "elements": [
        {"id": nid(), "elType": "widget", "widgetType": "html", "elements": [], "settings": {"html": html_str}}]}

def video_widget(hero_id, fname='applicazioni-hero-video.mp4'):
    js = ("<script>\n(function(){\n  var wrap=document.querySelector('#%s .bh-media'); if(!wrap) return;\n"
          "  if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;\n"
          "  var v=document.createElement('video');\n"
          "  v.muted=true;v.loop=true;v.autoplay=true;v.playsInline=true;v.setAttribute('playsinline','');v.setAttribute('aria-hidden','true');v.preload='auto';\n"
          "  v.style.cssText='position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:center;opacity:0;transition:opacity .9s ease';\n"
          "  v.addEventListener('canplay',function(){v.style.opacity='1';var p=v.play();if(p&&p.catch)p.catch(function(){});});\n"
          "  v.addEventListener('error',function(){if(v.parentNode)v.parentNode.removeChild(v);});\n"
          "  v.src='/wp-'+'content/'+'uploads/'+'2026/10/'+'%s';\n  wrap.appendChild(v);\n})();\n</script>") % (hero_id, fname)
    return {"id": nid(), "elType": "widget", "widgetType": "html", "elements": [],
            "settings": {"html": js, "_css_classes": "iah-global"}}

def hero(hero_id, kicker, h1, paras):
    ps = ''.join('<p>%s</p>' % p for p in paras)
    h = ('<section class="iah2-hero" id="%s"><div class="bh-media"><img src="%s" alt=""></div><div class="bh-scrim"></div>'
         '<div class="bh-copy"><div class="bh-in"><span class="kick">%s</span><h1>%s</h1><div class="sub">%s</div></div></div></section>') % (hero_id, HERO_IMG, kicker, h1, ps)
    c = wrap(h, css_id='sec-' + hero_id)
    c['elements'].append(video_widget(hero_id))
    return c

def head(eb, h2, leads=(), dark=False):
    s = ''
    if eb: s += '<p class="iah2-eb">%s</p>' % eb
    s += '<h2 class="iah2-h2">%s</h2>' % h2
    for l in leads: s += '<p class="iah2-lead">%s</p>' % l
    return s

def sec(tone, inner, extra=''):
    return '<section class="iah2-sec %s"%s><div class="iah2-in">%s</div></section>' % (tone, extra, inner)

def card(title, text='', ic=None, link=None, cls=''):
    s = '<div class="iah2-card %s">' % cls
    if ic: s += '<i class="iah2-ic iah2-i-%s"></i>' % ic
    s += '<h3>%s</h3>' % title
    if text: s += '<p>%s</p>' % text
    if link: s += '<a class="go" href="%s">Scopri di più →</a>' % link
    return s + '</div>'

def grid(n, cards): return '<div class="iah2-grid g%d">%s</div>' % (n, ''.join(cards))

def steps(n, items, arrows=False):
    s = '<div class="iah2-steps c%d%s">' % (n, ' ar' if arrows else '')
    for ic, t, p in items:
        s += '<div class="iah2-step"><i class="iah2-ic iah2-i-%s"></i><div class="box"><h3>%s</h3><p>%s</p></div></div>' % (ic, t, p)
    return s + '</div>'

def setsec(title_html, cards_html, anchor=None):
    return ('<section class="iah2-set"><div class="bgi"><img src="%s" alt=""></div><div class="iah2-in">'
            '<h2 class="iah2-h2">%s</h2>%s</div></section>') % (HERO_IMG, title_html, cards_html)

def three_settori(texts):
    ind, civ, mu = texts
    return grid(3, [card('Industriale', ind, None, SITE + '/settori/industriale/'),
                    card('Civile', civ, None, SITE + '/settori/civile/'),
                    card('Multi-utility', mu, None, SITE + '/settori/multi-utility/')])

def page(*items): return list(items)

def save(name, data):
    p = os.path.join(OUT, name + '.json')
    json.dump(data, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    return os.path.getsize(p)
