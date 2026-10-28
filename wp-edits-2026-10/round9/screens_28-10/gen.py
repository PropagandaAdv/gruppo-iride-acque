import json
WRAP = r'''(function(){
var KEY=__KEY__;
var RULES=[
__RULES__
];
var o=Response.prototype.text;
Response.prototype.text=function(){return o.call(this).then(function(t){
if(typeof t==="string"&&t.length>20000&&t.indexOf(KEY)>-1){
RULES.forEach(function(x,n){
if(x.a){var i=t.indexOf(x.a),j=i<0?-1:t.indexOf(x.b,i);if(j<0){console.warn("lp-patch non applicata",n);return}t=t.slice(0,i)+x.r+t.slice(j+x.b.length)}
else{var k=t.indexOf(x.f);if(k<0){console.warn("lp-patch non applicata",n);return}t=t.slice(0,k)+x.r+t.slice(k+x.f.length)}
});}
return t;});};
})();'''
def tl(s):
    assert '`' not in s and '${' not in s and chr(92) not in s, s
    return '`'+s+'`'
def rule(f=None,r='',a=None,b=None):
    if a is not None: return '{a:%s,b:%s,r:%s}'%(tl(a),tl(b),tl(r))
    return '{f:%s,r:%s}'%(tl(f),tl(r))

BACK_CSS = '''.lp-back{display:inline-flex;align-items:center;white-space:nowrap;margin-right:auto;margin-left:.75rem;font-size:1rem;font-weight:500;line-height:1;color:#F4F2EE!important;border:1px solid rgba(244,242,238,.35)!important;padding:.6rem 1.1rem;text-decoration:none;transition:color .3s,border-color .3s,background .3s}
.lp-back:hover{color:#fff!important;border-color:rgba(244,242,238,.8)!important;background:rgba(244,242,238,.1)}
.lp-back,.lp-back span{white-space:nowrap!important;flex-shrink:0}
.lp-back .lp-back-s{display:none}
@media(max-width:639px){.lp-back .lp-back-l{display:none}.lp-back .lp-back-s{display:inline}.lp-back{font-size:.9375rem;padding:.5rem .8rem;margin-left:.5rem}}
@media(min-width:1024px) and (max-width:1279px){.lp-back .lp-back-l{display:none}.lp-back .lp-back-s{display:inline}}'''

# ---------------- BM ----------------
bm_rules=[
 rule(f='legal:"Strada della Repubblica 41, 43121 Parma",operative:"Via Montello 43, 20831 Seregno (MB)",phone:"0362 244145",phoneHref:"tel:+390362244145",fax:"0362 240467",',
      r='legal:"Milano",operative:"Via Michelangelo Buonarroti, 3, 22060 Arosio (CO)",phone:"",phoneHref:"",fax:"",'),
 rule(f='{icon:Le,label:"Telefono",value:h.phone,href:h.phoneHref},',r=''),
 rule(a='e.jsx("li",{children:e.jsxs("a",{href:h.phoneHref,',b='e.jsxs("li",{children:["Fax ",h.fax]}),',r=''),
 rule(f='e.jsx("nav",{"aria-label":"Navigazione principale",className:"hidden lg:block"',
      r='e.jsxs("a",{href:"/",className:"lp-back",children:[e.jsx("span",{className:"lp-back-l",children:"← Torna al Gruppo Iride Acque"}),e.jsx("span",{className:"lp-back-s",children:"← Gruppo"})]}),e.jsx("nav",{"aria-label":"Navigazione principale",className:"hidden lg:block"'),
 rule(f='all\'attrezzatura di dosaggio."}],Ze=[',
      r='all\'attrezzatura di dosaggio."},{icon:Se,title:"Antilegionella",text:"",className:"hidden"}],Ze=['),
]
bm_js = WRAP.replace('__KEY__','"biemmeengineering.it"').replace('__RULES__',',\n'.join(bm_rules))
bm_css = BACK_CSS + '''
#biemme-root header>div:first-child{height:5.5rem!important}
#biemme-root header.backdrop-blur-md>div:first-child{height:4.75rem!important}
#biemme-root header>div:first-child a[href='#top'] img{width:10.5rem!important}
#biemme-root header>div:first-child{gap:1rem!important}
#biemme-root header nav a{font-size:1.0625rem!important;white-space:nowrap;padding-left:.625rem!important;padding-right:.625rem!important}
#biemme-root header .lp-back{font-size:.9375rem;padding:.5rem .9rem;margin-left:.25rem}
#biemme-root header div.items-center.gap-3 a[href='#contatti']{font-size:1.0625rem!important;padding:.6rem 1.1rem!important;white-space:nowrap!important}
@media(min-width:640px){#biemme-root header>div:first-child a[href='#top'] img{width:12rem!important}}
@media(min-width:1024px) and (max-width:1279px){#biemme-root header div.items-center.gap-3 a[aria-label*='LinkedIn']{display:none!important}#biemme-root header nav a{padding-left:.4rem!important;padding-right:.4rem!important;font-size:1rem!important}#biemme-root header>div:first-child a[href='#top'] img{width:9.5rem!important}}
@media(min-width:1024px){#biemme-root header>div:first-child{height:6.75rem!important}#biemme-root header.backdrop-blur-md>div:first-child{height:5.5rem!important}#biemme-root header>div:first-child a[href='#top'] img{width:11.5rem!important}}'''
# ---------------- BF ----------------
bf_rules=[
 rule(f='i("nav",{"aria-label":"Navigazione principale",className:"hidden md:block"',
      r='i("a",{href:"/",className:"lp-back",children:[i("span",{className:"lp-back-l",children:"← Torna al Gruppo Iride Acque"}),i("span",{className:"lp-back-s",children:"← Gruppo"})]}),i("nav",{"aria-label":"Navigazione principale",className:"hidden md:block"'),
 rule(a='.mp4",poster:"',b='bytes:8624591',r='.mp4",poster:"data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",bytes:0'),
 rule(f='await fetch(se.src,{signal:fe.signal,priority:"low"})',r='{ok:!1}'),
]
bf_js = WRAP.replace('__KEY__','"/*BF-JS*/"').replace('__RULES__',',\n'.join(bf_rules))
bf_css = BACK_CSS.replace('.lp-back{','.lp-back{border-radius:2px;') + '''
@media(min-width:768px) and (max-width:1023px){.lp-back .lp-back-l{display:none}.lp-back .lp-back-s{display:inline}}
header.fixed>div.relative a[href='#top']{flex-shrink:0}
header.fixed>div.relative{height:4.75rem!important}
header.fixed>div.relative a[href='#top'] img{height:3rem!important}
header.fixed nav[aria-label='Navigazione principale'] a{font-size:1.125rem!important}
header.fixed div.items-center.gap-3 a[href='#contatti']{font-size:1.125rem!important;min-height:3rem!important;padding-left:1.5rem!important;padding-right:1.5rem!important}
#menu-mobile{top:4.75rem!important}
@media(min-width:640px){header.fixed>div.relative a[href='#top'] img{height:3.375rem!important}}
@media(min-width:1024px){header.fixed>div.relative{height:5.5rem!important}header.fixed>div.relative a[href='#top'] img{height:3.875rem!important}}'''
for name,js,css in (('bm',bm_js,bm_css),('bf',bf_js,bf_css)):
    assert chr(92) not in js and chr(92) not in css, name
    html='<style>\n/* 27/10 landing: header piu grande, pulsante Torna al Gruppo Iride Acque, correzioni contenuti */\n'+css+'\n</style>\n<script>\n'+js+'\n</script>'
    open(name+'_widget.html','w',encoding='utf8').write(html)
    open(name+'_wrap.js','w',encoding='utf8').write(js)
    open(name+'.css','w',encoding='utf8').write(css)
    print(name,len(html),'caratteri; backslash:',html.count(chr(92)))
