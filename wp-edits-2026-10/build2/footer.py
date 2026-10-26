import json
d=json.load(open('backup2/p42-live.data.json',encoding='utf-8'))
def find(es,i):
    for e in es:
        if e['id']==i: return e
        r=find(e.get('elements',[]),i)
        if r: return r
def P(t,r=None,b=None,l=None): 
    return {'unit':'px','top':str(t),'right':str(r if r is not None else 0),'bottom':str(b if b is not None else 0),'left':str(l if l is not None else 0),'isLinked':False}
sec=find(d,'da781518')
sec['settings']['padding']=P(64,24,56,24); sec['settings']['padding_mobile']=P(44,16,40,16)
sec['settings']['css_classes']='iah-contact'
head=find(d,'4507230f')
head['settings']['padding']=P(0,0,26,0); head['settings']['padding_mobile']=P(0,0,18,0)
head['settings']['flex_gap']={'unit':'px','size':10,'column':'10','row':'10'}
t=find(d,'3b7847ab')['settings']
t['typography_font_size']={'unit':'px','size':36}; t['typography_font_size_mobile']={'unit':'px','size':26}
panel=find(d,'c402aa71')['settings']
panel['background_color']='#09171F'
panel.update({'border_border':'solid','border_width':{'unit':'px','top':'1','right':'1','bottom':'1','left':'1','isLinked':True},'border_color':'rgba(141,214,232,.28)'})
panel['padding']={'unit':'px','top':'40','right':'44','bottom':'40','left':'44','isLinked':False}
panel['padding_mobile']=P(26,20,28,20)
panel['flex_gap']={'unit':'px','size':48,'column':'48','row':'48'}
find(d,'74fe1c6a')['settings']['typography_font_size']={'unit':'px','size':26}
x=find(d,'6182ffc3')['settings']; x['typography_font_size']={'unit':'px','size':17}
find(d,'dbcc8bed')['settings']['flex_gap']={'unit':'px','size':16,'column':'16','row':'16'}
find(d,'9361fb10')['settings']['flex_gap']={'unit':'px','size':12,'column':'12','row':'12'}
for i in ['a93bb855','90748948','6d6f0be9']:
    s=find(d,i)['settings']; s['typography_font_size']={'unit':'px','size':16.5}; s['typography_line_height']={'unit':'em','size':1.5}
# remove the 'Vai alla richiesta di valutazione' button container
left=find(d,'dbcc8bed')
left['elements']=[c for c in left['elements'] if c['id']!='fb9a61ad']
f=find(d,'ea59a847')['settings']
f['input_size']='md'; f['row_gap']={'unit':'px','size':14,'sizes':[]}; f['column_gap']={'unit':'px','size':14,'sizes':[]}
f['button_background_hover_color']='rgba(74,183,213,0.8)'
f['button_text_padding']={'unit':'px','top':'14','right':'28','bottom':'14','left':'28','isLinked':False}
f['custom_css']=f['custom_css'].replace('padding: 15px 18px','padding: 12px 16px').replace('min-height: 120px','min-height: 84px').replace('margin-bottom: 7px','margin-bottom: 5px')
json.dump(d,open('build2/footer-42.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(json.dumps(d,ensure_ascii=False,separators=(',',':'))))
