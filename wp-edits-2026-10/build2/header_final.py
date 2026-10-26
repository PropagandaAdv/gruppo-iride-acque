import json, re, subprocess, sys

subprocess.run([sys.executable, 'build2/header.py'], check=True)
d = json.load(open('build2/header-39.json', encoding='utf-8'))
css = open('build2/global2.css', encoding='utf-8').read().strip()
js_old = "    window.addEventListener('scroll', u, {passive:true});\n"
js_new = js_old + ("    document.addEventListener('click',function(e){var c=e.target.closest('.iah-sector');"
                   "if(c){c.classList.toggle('is-open');}});\n")


def walk(e, f):
    f(e)
    for c in e.get('elements', []):
        walk(c, f)


def fix(e):
    s = e['settings']
    w = e.get('widgetType')
    if w == 'html':
        h = s['html']
        h = h.replace('</style>', css + '\n</style>', 1)
        assert js_old in h
        h = h.replace(js_old, js_new)
        s['html'] = h
    if w == 'button':
        s['button_background_hover_color'] = 'rgba(74,183,213,0.8)'
    if w == 'nav-menu':
        s['dropdown_typography_font_weight'] = '400'
        s['dropdown_typography_font_size'] = {'unit': 'px', 'size': 16}
        s['padding_vertical_dropdown_item'] = {'unit': 'px', 'size': 9}


for e in d:
    walk(e, fix)
out = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
open('build2/header-final.json', 'w', encoding='utf-8').write(out)
print(len(out))
