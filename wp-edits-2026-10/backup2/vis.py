import re,html,os,sys
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'<body.*',s,re.S).group(0)
m=re.sub(r'<(style|script|noscript|svg)[^>]*>.*?</\1>','',m,flags=re.S)
m=re.sub(r'<(div|section|p|h\d|a|li|button)[ >]','\n<\1 ',m)
tx=html.unescape(re.sub(r'<[^>]+>',' ',m))
lines=[' '.join(l.split()) for l in tx.split('\n')]
print('\n'.join(l for l in lines if l)[:int(sys.argv[2]) if len(sys.argv)>2 else 4000])
