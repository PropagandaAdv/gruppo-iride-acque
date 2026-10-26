import json,sys,re,html
d=json.load(open(sys.argv[1],encoding='utf-8'))
data=json.loads(d['value']) if isinstance(d,dict) else d
json.dump(data,open(sys.argv[1].replace('.meta.json','.data.json'),'w',encoding='utf-8'),ensure_ascii=False)
def txt(s): return ' '.join(html.unescape(re.sub(r'<[^>]+>',' ',s or '')).split())
def walk(e,dep=0):
    s=e.get('settings',{})
    w=e.get('widgetType')
    info=''
    if w=='html':
        h=s.get('html','')
        info='HTML len=%d | %s'%(len(h),txt(re.sub(r'<style.*?</style>|<script.*?</script>','',h,flags=re.S))[:140])
    elif w=='heading': info=s.get('title','')[:100]
    elif w=='text-editor': info=txt(s.get('editor'))[:100]
    elif w=='button': info=s.get('text','')+' -> '+str((s.get('link') or {}).get('url'))
    bg=s.get('background_color','')
    print('  '*dep+f"{e['elType']}{'/'+w if w else ''} {e['id']} {s.get('css_id','') or s.get('_element_id','')} bg={bg} {info}")
    for c in e.get('elements',[]): walk(c,dep+1)
for e in data: walk(e)
