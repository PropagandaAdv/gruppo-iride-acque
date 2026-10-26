"""Struttura i testi estratti da sostelia.it (JSON di sost_extract.py) in content.json.
Uso: python -I -X utf8 build2/sost_content.py <cartella_json>"""
import sys, json, os, re

SRC = sys.argv[1]
PAGES = {
    'primarie': 'impianti-trattamento-acque_impianti-trattamento-acque-primarie',
    'reflue': 'impianti-trattamento-acque_impianti-trattamento-acque-reflue',
    'zld': 'impianti-trattamento-acque_impianti-a-scarico-zero-zld',
    'fanghi': 'impianti-trattamento-acque_trattamento-fanghi-da-depurazione',
    'progettazione': 'servizi-depurazione-trattamento-acque_progettazione-e-realizzazione-impianti-trattamento-acque',
    'gestione': 'servizi-depurazione-trattamento-acque_gestione-impianti-depurazione-acque',
    'noleggio': 'servizi-depurazione-trattamento-acque_noleggio-impianti-mobili-trattamento-acque-e-fanghi',
    'consulenza': 'servizi-depurazione-trattamento-acque_consulenza-permitting-ambientale',
    'app_overview': 'impianti-trattamento-acque',
    'serv_overview': 'servizi-depurazione-trattamento-acque',
    'settori': 'trattamento-delle-acque',
    'industriale': 'trattamento-delle-acque_impianti-trattamento-acque-industriali',
    'sii': 'trattamento-delle-acque_servizio-idrico-integrato',
}
FORM = {'Nome e cognome*', 'Società*', 'Email*', 'Telefono', 'Messaggio',
        'Dichiaro di aver preso visione dell’informativa privacy*'}


def clean(t):
    return re.sub(r"\s*\n\s*", " ", t).strip()


def parse(name):
    d = json.load(open(os.path.join(SRC, PAGES[name] + '.json'), encoding='utf-8'))
    i = [k for k, t in enumerate(d) if t[0] == '@/header'][0]
    j = [k for k, t in enumerate(d) if t[0] == '@footer'][0]
    d = [t for t in d[i + 1:j] if t[0] != '@id' and not (t[0] == 'p' and t[1] in FORM)]
    k = [n for n, t in enumerate(d) if t[0] == 'h1'][0]
    d = d[k:]
    out = {'h1': clean(d[0][1]), 'lead': [], 'blocks': [], 'projects': [], 'cta': None, 'next': None, 'extra': []}
    mode = 'lead'
    cur = None
    n = 1
    while n < len(d):
        tag, txt, href = d[n]
        txt = txt.strip()
        n += 1
        if tag in ('img', 'a') and not (tag == 'a' and href and mode == 'proj_wait'):
            if tag == 'a' and txt.lower() in ('contattaci',) and out['cta'] is not None and 'href' not in out['cta']:
                out['cta']['href'] = href
            continue
        if tag == 'h4':
            mode = 'blocks'
            cur = {'title': clean(txt), 'text': []}
            out['blocks'].append(cur)
            continue
        if tag == 'h2':
            t2 = clean(txt)
            if t2.startswith('Vuoi '):
                out['cta'] = {'title': t2}
                mode = 'cta'
                continue
            if t2.startswith('Settori') and 'applicativi' in t2:
                mode = 'settori_app'
                continue
            if t2.startswith('La sostenibilità') or t2.startswith('Servizi di assistenza'):
                mode = 'skip'
                continue
            if mode == 'next':
                out['next'] = t2
                continue
            if mode in ('blocks', 'lead') and name not in ('app_overview', 'serv_overview', 'settori', 'industriale', 'sii') or mode == 'projects':
                # progetto collegato: h2 + link "Scopri di più"
                href2 = ''
                if n < len(d) and d[n][0] == 'a':
                    href2 = d[n][2]
                    n += 1
                out['projects'].append({'title': t2, 'href': href2})
                mode = 'projects'
                continue
            out['extra'].append({'h2': t2})
            continue
        if tag == 'p':
            if txt.endswith('successivo') or txt.endswith('successiva'):
                mode = 'next'
                continue
            if mode == 'lead':
                out['lead'].append({'p': clean(txt)})
            elif mode == 'blocks' and cur is not None:
                cur['text'].append(clean(txt))
            elif mode in ('settori_app', 'skip', 'cta'):
                pass
            else:
                out['extra'].append({'p': clean(txt)})
            continue
        if tag == 'li':
            if mode == 'lead':
                out['lead'].append({'li': clean(txt)})
            continue
    return out


res = {k: parse(k) for k in PAGES}
json.dump(res, open('build2/content.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in res.items():
    print(k, '| h1:', v['h1'], '| lead:', len(v['lead']), '| blocks:', len(v['blocks']), '| projects:', len(v['projects']),
          '| cta:', bool(v['cta']), '| next:', v['next'], '| extra:', len(v['extra']))
