import sys,json
sys.path.insert(0,'.')
from lib import *
BG='https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/09/hero-template-bg.webp'
hero=C({"css_id":"sec-article-hero","content_width":"full","background_background":"classic","background_image":{"url":BG,"id":""},"background_position":"center right","background_size":"cover",
        "background_overlay_background":"classic","background_overlay_color":"rgba(9,23,31,.82)",
        "padding":box(190,24,90,24),"padding_mobile":box(130,16,56,16),"margin":box(0)},
  [C({"content_width":"boxed","boxed_width":px(1240),"flex_gap":gap(18),"flex_gap_mobile":gap(14)},[
     W("text-editor",{"editor":"<p>News di Gruppo</p>","text_color":"#8DD6E8",**typo(16,700,ls=2.2,mobile=14)}),
     W("heading",{"title":"__TITLE__","header_size":"h1","title_color":"#FFFFFF",**typo(52,800,lh=1.12,mobile=32),"_max_width":px(980)}),
  ])],inner=False)
body=section("sec-article-body","news-articolo","#FFFFFF",[
  C({"content_width":"boxed","boxed_width":px(1000),"flex_gap":gap(26),"flex_gap_mobile":gap(20)},[
     W("text-editor",{"editor":"<p>__P1__</p>","text_color":BODY,"_css_classes":"iah-p",**typo(23,400,lh=1.65,mobile=19)}),
     W("text-editor",{"editor":"<p>__P2__</p>","text_color":BODY,"_css_classes":"iah-p",**typo(23,400,lh=1.65,mobile=19)}),
     C({"flex_direction":"row","flex_direction_mobile":"column","content_width":"full","flex_gap":gap(16),"padding":box(18,0,0,0),"flex_wrap":"wrap"},[
        button("Leggi la news completa →","https://www.irideacque.com/news/",external=True),
        button("← Tutte le news","https://gruppoirideacque.propagandaadv.com/news/"),
     ]),
  ])
],pad=(90,24,100,24),pad_m=(56,16,64,16))
tree=[hero,body]
fix_ids(tree)
out=json.dumps(tree,ensure_ascii=False,separators=(',',':'))
open('build2/article.json','w',encoding='utf-8').write(out)
print(len(out))
