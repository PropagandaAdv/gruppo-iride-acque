import sys,json
sys.path.insert(0,'.')
from lib import *
import re
# hero html live (pagina 64) come base
_p64=json.load(open('backup2/p64.data.json',encoding='utf-8')) if False else None
HERO_BASE = open('build2/hero_base.html',encoding='utf-8').read()
def hero(hid,kicker,h1_html,subtitle=None):
    h=HERO_BASE.replace('bhHeroSocieta',hid).replace('<span class="hero-kicker">Il Gruppo</span>','<span class="hero-kicker">%s</span>'%kicker)
    h=h.replace('<h1 class="hero-h1">Le società del Gruppo</h1>','<h1 class="hero-h1">%s</h1>'%h1_html)
    if subtitle:
        h=h.replace('</h1>\n','</h1>\n      <p class="hero-subtitle">%s</p>\n'%subtitle,1)
        h=h.replace('</style>',".brand-hero .hero-subtitle{color:rgba(238,246,250,.86);font-size:20px;line-height:1.65;max-width:760px;margin:26px 0 0;font-family:'Montserrat',sans-serif;font-weight:300;}\n</style>",1)
    return C({"css_id":"sec-"+hid,"content_width":"full","padding":box(0),"padding_mobile":box(0),"margin":box(0)},[W("html",{"html":h})],inner=False)
