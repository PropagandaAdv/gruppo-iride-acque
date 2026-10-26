import json,re
d=json.load(open('build/header-39.json',encoding='utf-8'))
s=json.dumps(d,ensure_ascii=False)
s=s.replace('#0D2B3E','#09171F').replace('rgba(13,43,62','rgba(9,23,31')
d=json.loads(s)
def walk(e,f):
    f(e)
    for c in e.get('elements',[]): walk(c,f)
def fix(e):
    st=e['settings']; w=e.get('widgetType')
    if w=='html':
        h=st['html']
        h=re.sub(r'@media\(max-width:1400px\)\{.*?\}\}\n','',h,flags=re.S)
        h=re.sub(r'@media\(max-width:1240px\)\{.*?\}\}\n','',h,flags=re.S) if '1240px' in h and False else h
        h=h.replace('@media(max-width:1240px){.iah-header .iah-cta{display:none!important;}}\n','')
        h=h.replace('.brand-hero .hero-subtitle{font-size:20px!important;}','.brand-hero .hero-subtitle{font-size:23px!important;line-height:1.6!important;}')
        h=h.replace('@media(max-width:767px){.brand-hero .bh-copy','@media(max-width:767px){.brand-hero .hero-subtitle{font-size:19px!important;}.brand-hero .bh-copy')
        h=h.replace('.iah-header .elementor-nav-menu--main .elementor-item{white-space:nowrap;}','.iah-header .elementor-nav-menu--main .elementor-item{white-space:nowrap;text-transform:none;}')
        st['html']=h
    if w=='nav-menu':
        st['menu_typography_font_size']={'unit':'px','size':19}
        st['menu_typography_font_weight']='400'
        st['padding_horizontal_menu_item']={'unit':'px','size':9}
    if w=='image':
        st['width']={'unit':'px','size':76}
    if e['elType']=='container' and e['id']=='c000004':
        st['css_classes']='iah-logo'
        st['custom_css']='selector{flex:0 0 auto!important;width:auto!important;min-width:300px;min-height:76px;}\n@media(max-width:1024px){selector{min-width:0;min-height:0;}}'
    if e['id']=='c000008':
        st['padding']={'unit':'px','top':'14','right':'40','bottom':'14','left':'40','isLinked':False}
for e in d: walk(e,fix)
json.dump(d,open('build2/header-39.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(json.dumps(d,ensure_ascii=False,separators=(',',':'))))
