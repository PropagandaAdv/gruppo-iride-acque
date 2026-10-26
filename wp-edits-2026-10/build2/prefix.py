import re,sys
P='body.page-template-elementor_header_footer '
src=open(sys.argv[1],encoding='utf-8').read()
src=re.sub(r'/\*.*?\*/','',src,flags=re.S)
out=[]
def pre(sel): return ','.join(P+s.strip() for s in sel.split(',') if s.strip())
i=0
while i<len(src):
    m=re.compile(r'\s*([^{}]+)\{').match(src,i)
    if not m: break
    head=m.group(1).strip(); j=m.end()
    if head.startswith('@media'):
        depth=1;k=j
        while depth:
            c=src[k]; depth+= (c=='{')-(c=='}'); k+=1
        inner=src[j:k-1]
        inn=''.join(pre(a.strip())+'{'+b.strip()+'}' for a,b in re.findall(r'([^{}]+)\{([^{}]*)\}',inner))
        out.append(head+'{'+inn+'}')
        i=k
    else:
        k=src.index('}',j)
        out.append(pre(head)+'{'+src[j:k].strip()+'}')
        i=k+1
open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(out))
print(len('\n'.join(out)))
