import json,sys,glob,os
f=sys.argv[1]; pid=sys.argv[2]
d=json.load(open(f,encoding='utf-8'))
v=d['_elementor_data'][0] if isinstance(d['_elementor_data'],list) else d['_elementor_data']
data=json.loads(v)
json.dump(data,open('backup2/p%s.data.json'%pid,'w',encoding='utf-8'),ensure_ascii=False)
print(pid,len(v),'elements',len(data))
