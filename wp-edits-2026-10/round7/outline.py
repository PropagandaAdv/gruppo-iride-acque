import json,io,re,sys
d=json.load(io.open(sys.argv[1],encoding='utf8'))
def walk(e,dep=0):
    s=e.get('settings',{})
    lab=e['elType']+(':'+e.get('widgetType','') if e['elType']=='widget' else '')
    extra=''
    w=e.get('widgetType')
    if w=='heading': extra=s.get('title','')[:70]
    if w=='text-editor': extra=re.sub('<[^>]+>','',s.get('editor',''))[:90]
    if w=='button': extra=s.get('text','')+' -> '+str(s.get('link',{}).get('url'))
    if w=='html': extra='HTML len=%d '%len(s.get('html',''))+re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',s.get('html','')))[:90]
    if w=='image': extra=s.get('image',{}).get('url','')[-50:]
    print('  '*dep+lab,e['id'],s.get('_element_id','') or s.get('css_id',''),s.get('_css_classes','') if w else '',extra)
    for c in e.get('elements',[]): walk(c,dep+1)
for e in d: walk(e)
