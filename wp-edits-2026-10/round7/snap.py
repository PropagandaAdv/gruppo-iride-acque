import json,sys,io,glob,os
# uso: python snap.py <post_id> <file_tool_result>
pid,src=sys.argv[1],sys.argv[2]
d=json.load(io.open(src,encoding='utf8'))
data=d['_elementor_data'][0] if isinstance(d['_elementor_data'],list) else d['_elementor_data']
io.open(f'backup_live/{pid}.json','w',encoding='utf8').write(data)
print(pid,len(data))
