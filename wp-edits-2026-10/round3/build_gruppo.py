import json, random, re
random.seed(55)
BASE = "https://gruppoirideacque.propagandaadv.com"
UP = BASE + "/wp-content/uploads/2026/10/"
t = json.load(open("backup_live/p55_tree.json", encoding="utf8"))


def nid():
    return "%07x" % random.randrange(0x1000000, 0xfffffff)


def find(n, i):
    if isinstance(n, list):
        for x in n:
            r = find(x, i)
            if r:
                return r
        return None
    if n.get("id") == i:
        return n
    for c in n.get("elements", []) or []:
        r = find(c, i)
        if r:
            return r


def HTML(html, extra=None):
    s = {"html": html}
    if extra:
        s.update(extra)
    return {"id": nid(), "elType": "widget", "settings": s, "elements": [], "widgetType": "html"}


# ---------------------------------------------------------------- 2.1 hero (client animation, 3 key frames)
hero_html = """<style>
.brand-hero{position:relative;overflow:hidden;background:#09171F;display:flex;flex-direction:column;min-height:100vh;}
.brand-hero .bh-media{position:absolute;inset:0;width:100%;height:100%;}
.brand-hero .bh-media img{width:100%;height:100%;object-fit:cover;object-position:right center;}
.brand-hero .bh-scrim{position:absolute;inset:0;background:linear-gradient(100deg, rgba(9,23,31,.94) 0%, rgba(9,23,31,.86) 38%, rgba(9,23,31,.62) 65%, rgba(9,23,31,.45) 100%);pointer-events:none;}
.brand-hero .bh-copy{position:relative;z-index:5;flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 16px;box-sizing:border-box;}
.brand-hero .bh-copy-inner{width:100%;max-width:1240px;margin:0 auto;}
.brand-hero .hero-kicker{color:#8DD6E8;font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin-bottom:18px;font-family:'Montserrat',sans-serif;display:block;}
.brand-hero .hero-h1{color:#fff;font-weight:800;letter-spacing:-.01em;line-height:1.08;font-size:clamp(2.2rem,5.2vw,4.4rem);max-width:900px;text-shadow:0 4px 30px rgba(0,0,0,.35);font-family:'Montserrat',sans-serif;margin:0;}
.brand-hero .hero-h1 .accent{background:linear-gradient(90deg,#8DD6E8,#4AB7D5);-webkit-background-clip:text;background-clip:text;color:transparent;}
.brand-hero .hero-ctas{display:flex;gap:16px;flex-wrap:wrap;margin-top:38px;}
.brand-hero .btn-cta{display:inline-flex;align-items:center;gap:8px;padding:17px 30px;border-radius:999px;font-size:15px;font-weight:700;letter-spacing:.02em;background:#4AB7D5;color:#09171F;box-shadow:0 8px 24px rgba(74,183,213,.35);transition:transform .35s cubic-bezier(.22,.61,.36,1), box-shadow .35s cubic-bezier(.22,.61,.36,1), background .35s cubic-bezier(.22,.61,.36,1);border:none;cursor:pointer;font-family:'Montserrat',sans-serif;text-decoration:none;}
.brand-hero .btn-cta:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(74,183,213,.45);background:#8DD6E8;}
#bhHeroIlGruppo .hero-h1{font-size:clamp(2.1rem,3.7vw,3.4rem)!important;max-width:none!important;}
#bhHeroIlGruppo .hero-kicker{font-size:16px!important;}
#bhHeroIlGruppo .bh-grid{display:grid;grid-template-columns:minmax(0,1.08fr) minmax(0,.92fr);gap:56px;align-items:center;}
#bhHeroIlGruppo .bh-anim{position:relative;aspect-ratio:720/413;border-radius:28px;overflow:hidden;background:#C9CED3;border:1px solid rgba(255,255,255,.22);box-shadow:0 44px 90px -34px rgba(0,0,0,.7);}
#bhHeroIlGruppo .bh-anim img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;animation:bhFrame 9s ease-in-out infinite;}
#bhHeroIlGruppo .bh-anim img:nth-child(2){animation-delay:3s;}
#bhHeroIlGruppo .bh-anim img:nth-child(3){animation-delay:6s;}
@keyframes bhFrame{0%{opacity:0;transform:scale(1.04);}7%{opacity:1;}33%{opacity:1;transform:scale(1);}41%{opacity:0;}100%{opacity:0;}}
@media (prefers-reduced-motion:reduce){#bhHeroIlGruppo .bh-anim img{animation:none;opacity:0;}#bhHeroIlGruppo .bh-anim img:nth-child(3){opacity:1;}}
@media(max-width:900px){#bhHeroIlGruppo .iah-br{display:none;}#bhHeroIlGruppo .bh-grid{grid-template-columns:1fr;gap:34px;}#bhHeroIlGruppo .hero-h1{font-size:clamp(2rem,8.4vw,2.8rem)!important;}#bhHeroIlGruppo .bh-anim{border-radius:22px;}}
</style>
<section class="brand-hero" id="bhHeroIlGruppo">
  <div class="bh-media"><img src="https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/09/hero-template-bg.webp" alt=""></div>
  <div class="bh-scrim"></div>
  <div class="bh-copy">
    <div class="bh-copy-inner">
      <div class="bh-grid">
        <div class="bh-text">
          <span class="hero-kicker">Gruppo Iride Acque</span>
          <h1 class="hero-h1">Da specialisti verticali a<br class="iah-br"> <span class="accent">piattaforma industriale integrata</span></h1>
          <div class="hero-ctas"><a href="https://gruppoirideacque.propagandaadv.com/le-societa-del-gruppo/" class="btn-cta">Scopri le società del Gruppo →</a></div>
        </div>
        <div class="bh-anim" role="img" aria-label="Animazione del Gruppo Iride Acque: nastri blu che si compongono nel marchio">
          <img src="https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/10/gruppo-animazione-frame-1.webp" alt="" width="720" height="413" loading="eager">
          <img src="https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/10/gruppo-animazione-frame-2.webp" alt="" width="720" height="413" loading="lazy">
          <img src="https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/10/gruppo-animazione-frame-4.webp" alt="" width="720" height="413" loading="lazy">
        </div>
      </div>
    </div>
  </div>
</section>
<script>
(function(){
  var hero = document.getElementById('bhHeroIlGruppo');
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
find(t, "735dc908")["settings"]["html"] = hero_html

# ---------------------------------------------------------------- 2.2 subtitle widgets: keep the sizing that was keyed on element IDs
SUB_CSS = "selector, selector p{font-size:23px !important;line-height:1.65 !important;}\n@media(max-width:767px){ selector, selector p{font-size:19px !important;} }"
for wid in ("7a1439b", "5575c202", "2ab48b93"):
    w = find(t, wid)
    assert w, wid
    w["settings"]["custom_css"] = SUB_CSS

# ---------------------------------------------------------------- 2.3 timeline
EVENTS = [
    ("2015", "Nascita Iride Acque"),
    ("2016", "1° brevetto"),
    ("2020", "2° brevetto"),
    ("2023", "Nascita del Gruppo Iride Acque con acquisizione Biemme Engineering"),
    ("2024", "3° brevetto"),
    ("2026", "Ingresso di Credem Euromobiliare"),
    ("2026", "Crescita del Gruppo Iride Acque con acquisizione Bieffe Costruzioni"),
    ("Nuova sede", "Il nuovo Headquarter di Arosio"),
    ("Futuro", "L'obiettivo: crescita del Gruppo<br>Piattaforma integrata"),
]
items = []
for i, (lbl, txt) in enumerate(EVENTS):
    side = "up" if i % 2 == 0 else "down"
    items.append(
        f'<li class="tl-{side}"><span class="tl-dot" aria-hidden="true"></span><span class="tl-stem" aria-hidden="true"></span>'
        f'<div class="tl-txt"><span class="tl-year">{lbl}</span><span class="tl-text">{txt}</span></div></li>'
    )
tl_html = """<style>
.iah-tl2{position:relative;width:100%;max-width:1240px;margin:0 auto;font-family:'Montserrat',sans-serif;}
.iah-tl2 ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(9,minmax(0,1fr));position:relative;}
.iah-tl2 ol::before{content:"";position:absolute;left:0;right:0;top:50%;height:2px;background:linear-gradient(90deg,#4AB7D5,#1A4D6A);transform:translateY(-1px);}
.iah-tl2 li{position:relative;height:360px;margin:0;padding:0;}
.iah-tl2 .tl-dot{position:absolute;left:50%;top:50%;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:6px;background:#1A4D6A;border:2px solid #4AB7D5;z-index:3;transition:transform .3s ease,background .3s ease;}
.iah-tl2 li.tl-up .tl-dot{background:#4AB7D5;border-color:#8DD6E8;}
.iah-tl2 li:hover .tl-dot{transform:scale(1.25);}
.iah-tl2 .tl-stem{position:absolute;left:50%;width:2px;height:40px;margin-left:-1px;background:#B7C3CB;z-index:1;}
.iah-tl2 li.tl-up .tl-stem{bottom:calc(50% + 10px);}
.iah-tl2 li.tl-down .tl-stem{top:calc(50% + 10px);}
.iah-tl2 .tl-txt{position:absolute;left:50%;width:226px;transform:translateX(-50%);text-align:center;}
.iah-tl2 li.tl-up .tl-txt{bottom:calc(50% + 58px);}
.iah-tl2 li.tl-down .tl-txt{top:calc(50% + 58px);}
.iah-tl2 .tl-year{display:block;margin:0 0 8px;font:800 26px/1.1 'Montserrat',sans-serif;color:#8DD6E8;letter-spacing:-.005em;}
.iah-tl2 .tl-text{display:block;font:600 16px/1.4 'Montserrat',sans-serif;color:rgba(255,255,255,.94);}
@media(max-width:1180px){.iah-tl2 .tl-txt{width:190px;}.iah-tl2 .tl-year{font-size:23px;}.iah-tl2 .tl-text{font-size:15px;}}
@media(max-width:900px){
  .iah-tl2 ol{display:block;padding-left:40px;}
  .iah-tl2 ol::before{left:11px;right:auto;top:8px;bottom:8px;width:2px;height:auto;transform:none;background:linear-gradient(180deg,#4AB7D5,#1A4D6A);}
  .iah-tl2 li{height:auto;margin:0 0 30px;}
  .iah-tl2 li:last-child{margin-bottom:0;}
  .iah-tl2 .tl-dot{left:-40px;top:5px;margin:0;}
  .iah-tl2 li.tl-up .tl-dot,.iah-tl2 li.tl-down .tl-dot{margin:0;}
  .iah-tl2 .tl-stem{display:none;}
  .iah-tl2 .tl-txt,.iah-tl2 li.tl-up .tl-txt,.iah-tl2 li.tl-down .tl-txt{position:static;width:auto;transform:none;text-align:left;top:auto;bottom:auto;}
  .iah-tl2 .tl-year{font-size:24px;margin-bottom:4px;}
  .iah-tl2 .tl-text{font-size:17px;}
}
</style>
<div class="iah-tl2" role="region" aria-label="Le tappe del Gruppo Iride Acque"><ol>
""" + "\n".join(items) + "\n</ol></div>"

ev = find(t, "fa99c487")
ev["elements"] = [HTML(tl_html, {"_element_width": "initial", "_element_custom_width": {"unit": "%", "size": 100}})]

# ---------------------------------------------------------------- 2.4 certifications
SOA = [("OG3", "Strade"), ("OG6", "Acquedotti e fognature"), ("OG7", "Opere marittime"), ("OS22", "Depuratori")]
ISO = [("9001:2015", "#4AB7D5"), ("14001:2015", "#2FBF71"), ("45001:2015", "#F2683C")]
soa_li = "\n".join(f'<li class="cert-soa"><span class="cert-code">{c}</span><span class="cert-lbl">{l}</span></li>' for c, l in SOA)
iso_li = "\n".join(
    f'<li class="cert-iso" style="--ring:{col}"><span class="cert-ring"><span>ISO</span></span><span class="cert-num">{n}</span></li>'
    for n, col in ISO
)
cert_html = """<style>
.iah-cert{width:100%;font-family:'Montserrat',sans-serif;display:grid;gap:44px;}
.iah-cert .cert-h{display:flex;align-items:center;gap:14px;margin:0 0 20px;font:800 22px/1.2 'Montserrat',sans-serif;color:#09171F;letter-spacing:.02em;}
.iah-cert .cert-h .cert-n{display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:44px;padding:0 10px;border-radius:12px;background:#09171F;color:#8DD6E8;font:800 16px/1 'Montserrat',sans-serif;letter-spacing:.08em;}
.iah-cert ul{list-style:none;margin:0;padding:0;display:grid;gap:20px;}
.iah-cert ul.soa{grid-template-columns:repeat(4,minmax(0,1fr));}
.iah-cert ul.iso{grid-template-columns:repeat(3,minmax(0,1fr));}
.iah-cert li{margin:0;border:1px solid rgba(9,23,31,.1);border-radius:22px;background:#fff;box-shadow:0 18px 44px -28px rgba(9,23,31,.4);transition:transform .35s ease,box-shadow .35s ease,border-color .35s ease;}
.iah-cert li:hover{transform:translateY(-6px);border-color:rgba(74,183,213,.65);box-shadow:0 30px 56px -28px rgba(9,23,31,.5);}
.iah-cert li.cert-soa{display:flex;flex-direction:column;gap:10px;padding:30px 26px;position:relative;overflow:hidden;}
.iah-cert li.cert-soa::before{content:"";position:absolute;left:0;top:0;width:100%;height:4px;background:linear-gradient(90deg,#4AB7D5,#1A4D6A);}
.iah-cert .cert-code{font:800 40px/1 'Montserrat',sans-serif;color:#1A4D6A;letter-spacing:-.01em;}
.iah-cert .cert-lbl{font:600 17px/1.4 'Montserrat',sans-serif;color:#3D5A6C;}
.iah-cert li.cert-iso{display:flex;align-items:center;gap:20px;padding:24px 26px;}
.iah-cert .cert-ring{flex:0 0 76px;width:76px;height:76px;border-radius:50%;border:4px solid var(--ring);display:inline-flex;align-items:center;justify-content:center;box-shadow:inset 0 0 0 5px rgba(9,23,31,.04);}
.iah-cert .cert-ring span{font:800 20px/1 'Montserrat',sans-serif;color:#09171F;letter-spacing:.04em;}
.iah-cert .cert-num{font:800 26px/1.15 'Montserrat',sans-serif;color:#09171F;}
@media(max-width:1024px){.iah-cert ul.soa{grid-template-columns:repeat(2,minmax(0,1fr));}.iah-cert ul.iso{grid-template-columns:repeat(3,minmax(0,1fr));}.iah-cert li.cert-iso{flex-direction:column;text-align:center;gap:14px;}}
@media(max-width:640px){.iah-cert ul.soa,.iah-cert ul.iso{grid-template-columns:1fr;}.iah-cert li.cert-iso{flex-direction:row;text-align:left;}.iah-cert .cert-code{font-size:34px;}}
</style>
<div class="iah-cert">
  <div class="cert-group">
    <h3 class="cert-h"><span class="cert-n">01</span>Attestato SOA</h3>
    <ul class="soa">
""" + soa_li + """
    </ul>
  </div>
  <div class="cert-group">
    <h3 class="cert-h"><span class="cert-n">02</span>Certificati di qualità</h3>
    <ul class="iso">
""" + iso_li + """
    </ul>
  </div>
</div>"""
cc = find(t, "f6de91a7")
cc["elements"] = [HTML(cert_html, {"_element_width": "initial", "_element_custom_width": {"unit": "%", "size": 100}})]

json.dump(t, open("home/p55_new.json", "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
for i, x in enumerate(t):
    s = json.dumps(x, ensure_ascii=False, separators=(",", ":"))
    open(f"home/g{i}.json", "w", encoding="utf8").write(s)
    print(i, x["id"], len(s))
