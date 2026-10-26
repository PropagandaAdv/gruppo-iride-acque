import json
def walk(e,f):
    f(e)
    for c in e.get('elements',[]): walk(c,f)
def normalize_buttons(tree):
    def f(e):
        if e.get('widgetType')=='button':
            s=e['settings']
            for k in ('border_border','border_width','border_color'): s.pop(k,None)
            s.update({'background_color':'#4AB7D5','button_text_color':'#09171F','button_background_hover_color':'rgba(74,183,213,0.8)','hover_color':'#09171F'})
    for e in tree: walk(e,f)
def find(tree,i):
    for e in tree:
        if e['id']==i: return e
        r=find(e.get('elements',[]),i)
        if r: return r
