"""Pagine landing Biemme Engineering (186) e Costruzioni Bieffe (188).

Hero = template "Hero Pagine Interne — Brand Template" (library ID 63, letto live il 2026-10-06, navy #09171F).
Contenuti = SOLO testo letto sui siti ufficiali delle società (vedi SOURCES nel report).
"""
from lib import *

HERO_T63 = """<style>
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
</style>
<section class="brand-hero" id="bhHeroIlGruppo">
  <div class="bh-media"><img src="https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/09/hero-template-bg.webp" alt=""></div>
  <div class="bh-scrim"></div>
  <div class="bh-copy">
    <div class="bh-copy-inner">
      <span class="hero-kicker">Gruppo Iride Acque</span>
      <h1 class="hero-h1">Da specialisti verticali a <span class="accent">piattaforma industriale integrata</span></h1>
      <div class="hero-ctas"><a href="https://gruppoirideacque.propagandaadv.com/home/#societa" class="btn-cta">Scopri le società del Gruppo →</a></div>
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

SUBTITLE_CSS = (".brand-hero .hero-subtitle{color:rgba(238,246,250,.86);font-size:20px;line-height:1.65;max-width:760px;"
                "margin:26px 0 0;font-family:'Montserrat',sans-serif;font-weight:300;}\n")


def make_hero(hid, h1, subtitle):
    hh = HERO_T63.replace("bhHeroIlGruppo", hid)
    hh = hh.replace('<span class="hero-kicker">Gruppo Iride Acque</span>', '<span class="hero-kicker">Società del Gruppo</span>')
    old_h1 = '<h1 class="hero-h1">Da specialisti verticali a <span class="accent">piattaforma industriale integrata</span></h1>'
    assert old_h1 in hh
    hh = hh.replace(old_h1, f'<h1 class="hero-h1">{h1}</h1>\n      <p class="hero-subtitle">{subtitle}</p>')
    a = hh.index('      <div class="hero-ctas">')
    b = hh.index("\n", a) + 1
    hh = hh[:a] + hh[b:]
    hh = hh.replace("</style>", SUBTITLE_CSS + "</style>", 1)
    assert hid in hh and "hero-ctas\">" not in hh and "0D2B3E" not in hh
    return C({"css_id": f"sec-{hid}", "content_width": "full", "padding": box(0), "padding_mobile": box(0), "margin": box(0)},
             [W("html", {"html": hh})], inner=False)


def checklist(items):
    return W("icon-list", {
        "icon_list": [{"_id": f"il{i:05d}", "text": t,
                       "selected_icon": {"value": "fas fa-check", "library": "fa-solid"}}
                      for i, t in enumerate(items, start=1)],
        "space_between": px(14), "icon_self_vertical_align": "flex-start", "icon_color": BLUE, "icon_size": px(18),
        "text_color": BODY, "text_indent": px(14),
        **typo(17.5, 400, lh=1.6, prefix="icon_typography"),
    })


def width_css(pct, extra=""):
    return ("selector { width: calc(" + pct + ") !important; flex: 0 0 calc(" + pct + ") !important; }\n"
            "@media(max-width:900px){ selector { width: 100% !important; flex: 0 0 100% !important; } }" + extra)


def white_card(children, pct):
    return C({"content_width": "full", "flex_gap": gap(16), "flex_gap_mobile": gap(14),
              "background_background": "classic", "background_color": "#FFFFFF", "border_radius": radius(28),
              "padding": box(40, 38, 40, 38), "padding_mobile": box(28, 22, 28, 22),
              "box_shadow_box_shadow_type": "yes",
              "box_shadow_box_shadow": {"horizontal": 0, "vertical": 24, "blur": 60, "spread": -28, "color": "rgba(9,23,31,.28)"},
              "custom_css": width_css(pct)}, children)


def cta_band(prefix_text):
    return section("sec-cta-societa", "cta-societa", NAVY, [
        C({"content_width": "boxed", "boxed_width": px(1040), "flex_align_items": "center",
           "flex_gap": gap(26), "flex_gap_mobile": gap(20)}, [
            para(prefix_text, "rgba(238,246,250,.9)", 21, 300, 1.6, align="center", mobile=18),
            button("Scopri tutte le società del Gruppo", f"{SITE}/le-societa-del-gruppo/", "solid", 17.5),
        ]),
    ], pad=(96, 24, 96, 24), pad_m=(64, 16, 64, 16))


# ============================================================ BIEMME ENGINEERING (fonte: biemmeengineering.it, /it/ e /it/chisiamo/ /it/applicazioni/ /it/disinfezione/)
BIEMME_SUB = ("Acqua di processo, disinfezione, misura, controllo e dosaggio delle sostanze chimiche "
              "per gli stabilimenti del beverage.")
BIEMME_P1 = ("L'acqua pura e l'igiene totale sono indispensabili nell'industria delle bevande. Biemme Engineering garantisce la gestione "
             "ottimale dell'acqua di processo unitamente alla certezza della sterilizzazione e disinfezione. La misura, il controllo e il "
             "dosaggio delle sostanze chimiche liquide a tutti i livelli del processo di produzione e di riempimento completano il portafoglio.")
BIEMME_P2 = ("Biemme Engineering segue i suoi clienti con soluzioni integrate: dal progetto di un impianto efficiente, adattato alle esigenze "
             "del cliente, all'installazione e alla messa in funzione, fino alla manutenzione e all'assistenza tecnica. Come fornitore di tutti "
             "i processi e i componenti, offre un sistema modulare con strumentazioni di misura, controllo e dosaggio complete.")
BIEMME_LIST = [
    "Soluzioni universali per tutti i processi di produzione e riempimento, dal trattamento dell'acqua di produzione al trattamento dell'acqua di scarico",
    "Disinfezione ad ampio raggio con il biossido di cloro",
    "Sistemi di dosaggio con pompe dosatrici, serbatoi di stoccaggio e strutture su misura dotate di vasca di contenimento con sensori",
    "Scelta ottimale della tecnologia: Biemme Engineering assembla e produce tutte le tipologie migliori presenti sul mercato",
    "Bassi costi di investimento grazie a una tecnologia universale e al progetto su misura",
    "Sistemi chiavi in mano con strumentazioni integrate di controllo e di dosaggio",
]

biemme_page = [
    make_hero("bhHeroBiemme", 'Biemme <span class="accent">Engineering</span>', BIEMME_SUB),
    section("sec-biemme-chisiamo", "chi-siamo", LIGHT, [
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_direction_mobile": "column",
           "flex_align_items": "flex-start", "flex_gap": gap(56), "flex_gap_mobile": gap(32)}, [
            C({"content_width": "full", "flex_gap": gap(20), "flex_gap_mobile": gap(16), "custom_css": width_css("50% - 28px")}, [
                eyebrow("Chi siamo", BLUE),
                h2("Esperienza e competenza al servizio del cliente", NAVY, 44, 28),
                para(BIEMME_P1, BODY, 18.5, 400, 1.75),
                para(BIEMME_P2, BODY, 18.5, 400, 1.75),
            ]),
            white_card([
                heading("Cosa facciamo", NAVY, 26, "h3", 800, lh=1.25, mobile=22),
                checklist(BIEMME_LIST),
            ], "50% - 28px"),
        ]),
    ], pad=(110, 24, 110, 24)),
    cta_band("Biemme Engineering fa parte del Gruppo Iride Acque."),
]

# ============================================================ COSTRUZIONI BIEFFE (fonte: costruzionibieffe.it, home + /chi-siamo/ + /contatti/)
BIEFFE_SUB = "Impresa di costruzioni dal 2007, in provincia di Treviso"
BIEFFE_P1 = ("Costruzioni Bieffe srl è nata nel 2007 e ha sviluppato la propria attività in provincia di Treviso. L'intenzione fondante dei due soci "
             "è stata convogliare la propria pluriennale esperienza nel settore delle costruzioni in una nuova impresa, per offrire prodotti e "
             "servizi che si distinguessero da quelli del mercato.")
BIEFFE_P2 = ("Fin dall'inizio l'impresa si occupa di costruzioni e manutenzioni edili, investendo sul territorio e garantendo alti standard "
             "qualitativi, con attenzione ai dettagli e alla soddisfazione del cliente. Le squadre sono guidate sul campo dai due soci titolari, "
             "sempre presenti in cantiere e a disposizione del cliente.")
BIEFFE_SECTORS = [
    ("Edilizia residenziale",
     "Ville, abitazioni abbinate, appartamenti e condomini, curati dalla progettazione all'edificazione in un unico servizio «chiavi in mano», con la capacità gestionale del General Contractor."),
    ("Edilizia industriale",
     "Per conto di primarie aziende del territorio, l'impresa gestisce l'intero iter, dal progetto generale alla gestione degli impianti e dei sub-appaltatori."),
    ("Restauri e ristrutturazioni",
     "Progetti di costruzione e restauro, anche molto diversi tra loro, eseguiti con competenza e flessibilità operativa."),
    ("Movimento terra",
     "L'impresa segue in proprio ogni fase di edificazione di un fabbricato, a partire dagli sbancamenti iniziali, grazie all'importante parco mezzi di proprietà."),
    ("Manutenzioni edili",
     "Costruzioni e manutenzioni edili sono l'attività dell'impresa fin dall'inizio; nell'edilizia industriale si abbina spesso la manutenzione ordinaria post-edificazione degli stabilimenti costruiti."),
]


def sector_card(i, title, text):
    return white_card([
        W("text-editor", {"editor": f"<p>0{i}</p>", "text_color": BLUE, **typo(14, 800, ls=1.2)}),
        heading(title, NAVY, 26, "h3", 800, lh=1.25, mobile=22),
        para(text, BODY, 17.5, 400, 1.7),
    ], "33.333% - 19px")


bieffe_page = [
    make_hero("bhHeroBieffe", 'Costruzioni <span class="accent">Bieffe</span>', BIEFFE_SUB),
    section("sec-bieffe-chisiamo", "chi-siamo", "#FFFFFF", [
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_gap": gap(20), "flex_gap_mobile": gap(16)}, [
            eyebrow("Chi siamo", BLUE),
            h2("L'esperienza al vostro servizio", NAVY, 44, 28),
            para(BIEFFE_P1, BODY, 18.5, 400, 1.75, maxw=920),
            para(BIEFFE_P2, BODY, 18.5, 400, 1.75, maxw=920),
        ]),
    ], pad=(110, 24, 70, 24), pad_m=(70, 16, 40, 16)),
    section("sec-bieffe-settori", "settori", LIGHT, [
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_gap": gap(18), "flex_gap_mobile": gap(14)}, [
            eyebrow("Settori di intervento", BLUE),
            h2("Cosa realizza Costruzioni Bieffe", NAVY, 44, 28, maxw=900),
        ]),
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_direction": "row", "flex_direction_mobile": "column",
           "flex_wrap": "wrap", "flex_justify_content": "center", "flex_gap": gap(28), "flex_gap_mobile": gap(20),
           "padding": box(48, 0, 0, 0), "padding_mobile": box(28, 0, 0, 0)},
          [sector_card(i, *s) for i, s in enumerate(BIEFFE_SECTORS, start=1)]),
        C({"content_width": "boxed", "boxed_width": px(1240), "flex_align_items": "center",
           "padding": box(44, 0, 0, 0), "padding_mobile": box(28, 0, 0, 0)}, [
            para("Certificazioni: SOA · ISO 9001:2015", NAVY, 17, 700, 1.5, align="center"),
        ]),
    ], pad=(80, 24, 110, 24), pad_m=(60, 16, 70, 16)),
    cta_band("Costruzioni Bieffe fa parte del Gruppo Iride Acque."),
]

if __name__ == "__main__":
    dump(biemme_page, "biemme-page")
    dump(bieffe_page, "bieffe-page")
