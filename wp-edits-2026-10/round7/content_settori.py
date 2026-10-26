from build_pages import *
import content_pages as cp   # per cssinc / nid

def tile(ic, big=False):
    return ('<div class="pic" style="background:linear-gradient(135deg,#123852,#1A4D6A);display:grid;place-items:center">'
            '<i class="iah2-ic iah2-i-%s" style="margin:0;%s"></i></div>') % (ic, 'width:96px;height:96px;background-size:44px 44px' if big else '')

def ind_list(items):
    s = '<div class="iah2-ind">'
    for ic, t, p in items:
        s += '<div class="it">%s<div><h3>%s</h3><p>%s</p></div></div>' % (tile(ic).replace('class="pic"', 'class="pic"'), t, p)
    return s + '</div>'

def subrows(items):
    s = ''
    for ic, t, p, url in items:
        s += '<div class="iah2-sub-row">%s<div><h3>%s</h3><p>%s</p><a class="go" href="%s">Scopri di più ↗</a></div></div>' % (tile(ic, True), t, p, url)
    return s

def page_set(hid, kick, h1, paras, list_head, list_html, sol_title, sols, sol_icons):
    return [cp.cssinc(),
        hero(hid, kick, h1, paras),
        wrap(sec('wh', list_head + list_html, ' id="sotto-settori"')),
        wrap(sec('lt', head('', sol_title) + grid(3 if len(sols) == 3 else 4 if False else 3, [card(t, p, ic) for (t, p), ic in zip(sols, sol_icons)]) if len(sols) == 3 else head('', sol_title) + grid(2, [card(t, p, ic) for (t, p), ic in zip(sols, sol_icons)]), ' id="soluzioni"'))]

pages = {}
# ---------------- 6.0 Settori principale
pages['settori'] = [cp.cssinc(),
  hero('bhHeroSettori', 'Dove operiamo', 'Settori diversi, soluzioni su misura', [
    'Ogni settore presenta esigenze specifiche nella gestione della risorsa idrica, dalla qualità dell’acqua destinata ai diversi utilizzi fino al trattamento, alla depurazione e al recupero delle acque reflue.',
    'Gruppo Iride Acque sviluppa soluzioni personalizzate per i settori industriale, civile e multi-utility, rispondendo alle differenti necessità operative, ai requisiti normativi e agli obiettivi di ogni cliente.',
    'Grazie a competenze tecniche specialistiche e all’integrazione di tecnologie innovative e consolidate, realizziamo sistemi di trattamento affidabili ed efficienti, con particolare attenzione all’ottimizzazione delle risorse, alla continuità operativa e alla sostenibilità ambientale.']),
  wrap(sec('wh', subrows([
    ('factory', 'Industriale', 'Soluzioni per il trattamento delle acque destinate ai processi produttivi e per la depurazione e il recupero dei reflui industriali, rispondendo alle esigenze di qualità, efficienza e continuità operativa dei diversi settori manifatturieri.', SITE + '/settori/industriale/'),
    ('building', 'Civile', 'Sistemi per il trattamento, la depurazione e il riutilizzo delle acque a servizio di edifici residenziali, strutture commerciali, complessi turistico-ricettivi e attività Ho.Re.Ca., con soluzioni adattate alle specifiche esigenze di utilizzo.', SITE + '/settori/civile/'),
    ('network', 'Multi-utility', 'Soluzioni per gestori dei servizi pubblici e delle infrastrutture idriche, con interventi dedicati alla potabilizzazione, al trattamento delle acque reflue, al riutilizzo della risorsa e all’efficientamento dei sistemi di trattamento.', SITE + '/settori/multi-utility/')]), ' id="elenco-settori"')),
]

# ---------------- 6.1 Industriale
pages['industriale'] = page_set('bhHeroIndustriale', 'Settore industriale', 'Soluzioni per il trattamento delle acque nell’industria', [
  'Gruppo Iride Acque sviluppa soluzioni personalizzate per il trattamento delle acque primarie, di processo e reflue nei diversi comparti industriali, rispondendo alle specifiche esigenze produttive, qualitative e ambientali di ogni settore.',
  'Ogni processo industriale presenta caratteristiche differenti in termini di consumo idrico, tipologia degli inquinanti e requisiti di trattamento. Grazie a competenze tecniche specialistiche e all’integrazione di tecnologie innovative e consolidate, progettiamo e realizziamo impianti affidabili ed efficienti, orientati all’ottimizzazione dei processi, alla riduzione dei costi operativi e al rispetto dei requisiti normativi.',
  'Particolare attenzione viene dedicata al recupero delle acque e delle risorse, favorendo la riduzione dei consumi e una gestione più sostenibile dei cicli produttivi.'],
  head('Applicazioni', 'Settori industriali', ['Soluzioni per il trattamento delle acque di processo e delle acque reflue, studiate per le specifiche esigenze di ogni settore. Dalla depurazione al recupero e riutilizzo delle risorse idriche, con tecnologie affidabili e sostenibili.']),
  ind_list([
   ('drop', 'Food &amp; Beverage', 'Trattamento delle acque di processo e delle acque reflue di lavaggio, con rimozione del carico organico e recupero delle acque per il riutilizzo, nel rispetto degli standard di qualità e sicurezza alimentare.'),
   ('flask', 'Chimico-farmaceutico', 'Produzione di acque di processo, anche ultrapure o demineralizzate, per cicli produttivi critici. Trattamento di reflui complessi con rimozione di contaminanti specifici e possibilità di recupero e riutilizzo dell’acqua.'),
   ('clip', 'Acque reflue ospedaliere', 'Trattamento delle acque di processo e delle acque reflue provenienti da strutture sanitarie, con rimozione di contaminanti specifici (farmaci, disinfettanti, agenti biologici) e conformità ai requisiti normativi.'),
   ('recycle', 'Detergenti e cosmetici', 'Trattamento delle acque di processo e dei reflui contenenti tensioattivi, emulsioni e sostanze organiche, con soluzioni di recupero e riutilizzo dell’acqua.'),
   ('wrench', 'Metalmeccanico', 'Trattamento delle acque di processo e delle acque reflue derivanti da lavorazioni meccaniche, inclusi reflui contenenti emulsioni oleose e lubrorefrigeranti. Soluzioni dedicate per separazione, depurazione e possibile riutilizzo dell’acqua.'),
   ('network', 'Tessile', 'Condizionamento delle acque di processo, rimozione del colore e delle sostanze organiche dai reflui, con soluzioni per il recupero dei sali di tintura e il riutilizzo delle acque.'),
   ('factory', 'Oil &amp; Gas', 'Trattamento robusto delle acque di processo e delle acque reflue di lavaggio, con rimozione di idrocarburi e composti organici, e soluzioni per il recupero e il riutilizzo delle acque dove possibile.'),
   ('docs', 'Carta', 'Trattamento delle acque di processo e dei reflui di produzione, con rimozione di fibre, sostanze organiche e additivi, e possibilità di recupero e riutilizzo dell’acqua.'),
   ('db', 'Percolato', 'Trattamento di percolato e reflui complessi caratterizzati da elevati carichi inquinanti, con soluzioni dedicate e possibilità di recupero delle acque.'),
   ('leaf', 'Agricoltura', 'Trattamento delle acque impiegate nelle attività agricole e nei processi di lavaggio dei prodotti, con soluzioni dedicate alla rimozione dei contaminanti e al recupero dell’acqua per il riutilizzo.'),
   ('monitor', 'Data center', 'Produzione di acque di processo ad elevata qualità, anche demineralizzate, per sistemi di raffreddamento. Trattamento delle acque di scarico e soluzioni per il riutilizzo e l’efficientamento idrico.')]),
  'Le nostre soluzioni per l’industria',
  [('Acque di processo', 'Produzione, trattamento e condizionamento di acque di processo, anche demineralizzate o ultrapure, per lavaggi, raffreddamento, utilities e linee produttive.'),
   ('Acque reflue', 'Trattamento dei reflui industriali con soluzioni dedicate alla rimozione di inquinanti, per garantire il rispetto dei limiti di scarico previsti dalla normativa vigente.'),
   ('Recupero e riutilizzo', 'Sistemi per il recupero dell’acqua, il riutilizzo nei processi e il recupero di risorse, con riduzione dei consumi, dei costi di approvvigionamento e degli oneri di smaltimento.')],
  ['drop', 'recycle', 'leaf'])

# ---------------- 6.2 Civile
pages['civile'] = page_set('bhHeroCivile', 'Settore civile', 'Soluzioni per il trattamento delle acque nel settore civile', [
  'Gruppo Iride Acque sviluppa soluzioni personalizzate per il trattamento delle acque primarie e reflue nel settore civile, rispondendo alle esigenze di edifici residenziali, strutture commerciali, complessi turistico-ricettivi e attività Ho.Re.Ca.',
  'Ogni struttura presenta necessità specifiche legate alla qualità dell’acqua, ai consumi idrici e alla gestione degli scarichi. Attraverso l’integrazione di tecnologie di filtrazione, disinfezione e depurazione, progettiamo e realizziamo impianti affidabili ed efficienti, garantendo soluzioni adeguate alle diverse condizioni di utilizzo e ai requisiti normativi applicabili.',
  'Particolare attenzione viene dedicata alla sicurezza e alla qualità dell’acqua, all’ottimizzazione dei consumi e al recupero delle acque reflue, favorendo il riutilizzo della risorsa idrica per applicazioni compatibili e una gestione più sostenibile delle strutture.'],
  head('Applicazioni', 'Settore civile', ['Soluzioni per il trattamento delle acque primarie, delle acque di servizio e delle acque reflue, progettate per le esigenze di strutture residenziali, ricettive, commerciali e collettive. Dalla filtrazione e disinfezione al recupero e riutilizzo della risorsa idrica, con sistemi affidabili e sostenibili.']),
  ind_list([
   ('building', 'Residenziale e condomini', 'Sistemi di filtrazione, addolcimento e disinfezione per migliorare la qualità dell’acqua negli edifici residenziali, con soluzioni per la depurazione delle acque reflue e il loro eventuale riutilizzo.'),
   ('drop', 'Hotel e strutture ricettive', 'Trattamento e disinfezione delle acque a servizio di hotel, resort e strutture turistico-ricettive, con sistemi per garantire qualità dell’acqua, continuità di servizio ed efficienza gestionale.'),
   ('flask', 'Ristoranti e catering', 'Soluzioni per il trattamento delle acque destinate a cucine professionali, ristoranti e servizi di catering, con sistemi di filtrazione, addolcimento e gestione delle acque reflue.'),
   ('building', 'Edifici commerciali e direzionali', 'Sistemi per il trattamento e il condizionamento delle acque utilizzate in uffici, centri commerciali e complessi direzionali, con soluzioni per l’ottimizzazione dei consumi e la gestione degli scarichi.'),
   ('drop', 'Centri sportivi e benessere', 'Trattamento, filtrazione e disinfezione delle acque per piscine, centri sportivi, palestre e strutture wellness, con sistemi per il controllo della qualità dell’acqua e la gestione dei reflui.'),
   ('clip', 'Strutture sanitarie e assistenziali', 'Soluzioni per il trattamento e la disinfezione delle acque a servizio di cliniche, strutture assistenziali e residenze sanitarie, con particolare attenzione alla qualità igienico-sanitaria e alla gestione degli scarichi.'),
   ('building', 'Edifici pubblici e strutture collettive', 'Sistemi di trattamento delle acque per scuole, università, edifici pubblici e strutture collettive, con soluzioni dedicate alla qualità dell’acqua, alla depurazione e al recupero della risorsa idrica.')]),
  'Le nostre soluzioni per il settore civile',
  [('Trattamento acque primarie e di servizio', 'Filtrazione, addolcimento, osmosi e disinfezione per garantire acqua di qualità per usi civili e tecnologici.'),
   ('Depurazione acque reflue civili', 'Impianti per il trattamento dei reflui civili con scarico conforme ai limiti normativi e gestione affidabile dell’impianto.'),
   ('Filtrazione e disinfezione', 'Sistemi dedicati all’affinamento finale e alla sicurezza igienico-sanitaria dell’acqua, anche per reti interne e accumuli.'),
   ('Recupero e riutilizzo delle acque', 'Soluzioni per il riuso delle acque trattate in irrigazione, scarichi, lavaggi e altri usi compatibili, con riduzione dei consumi idrici.')],
  ['drop', 'recycle', 'clip', 'leaf'])

# ---------------- 6.3 Multi-utility
pages['multiutility'] = page_set('bhHeroMultiutility', 'Settore multi-utility', 'Soluzioni per il trattamento delle acque nel settore Multi-utility', [
  'Gruppo Iride Acque sviluppa soluzioni personalizzate per il trattamento delle acque primarie e reflue a servizio di gestori del servizio idrico, enti pubblici e operatori delle infrastrutture idriche, con interventi dedicati alla potabilizzazione, distribuzione, e depurazione.',
  'Le infrastrutture idriche richiedono elevati standard di affidabilità, continuità operativa e qualità dell’acqua. Grazie a competenze tecniche specialistiche e all’integrazione di tecnologie innovative e consolidate, progettiamo e realizziamo impianti e sistemi di trattamento efficienti, rispondendo alle specifiche esigenze operative e ai requisiti normativi applicabili.',
  'Particolare attenzione viene dedicata all’ammodernamento e all’efficientamento degli impianti esistenti, all’ottimizzazione dei consumi energetici e alla riduzione dei costi di gestione, favorendo il recupero e il riutilizzo delle acque trattate e una gestione più sostenibile della risorsa idrica.'],
  head('Applicazioni', 'Settore Multi-utility', ['Soluzioni per il trattamento delle acque primarie e delle acque reflue a servizio delle infrastrutture idriche pubbliche e dei gestori del servizio idrico integrato, con tecnologie affidabili ed efficienti per garantire qualità, sicurezza e sostenibilità ambientale.']),
  ind_list([
   ('drop', 'Acquedotti e potabilizzazione', 'Soluzioni per la potabilizzazione delle acque destinate al consumo umano, con sistemi di filtrazione, disinfezione e controllo finalizzati a garantire qualità, sicurezza e continuità di servizio.'),
   ('network', 'Reti di distribuzione idrica', 'Interventi per la realizzazione, l’estensione e la manutenzione delle reti di distribuzione idrica, con soluzioni affidabili per garantire continuità, efficienza e sicurezza del servizio.'),
   ('recycle', 'Depurazione acque reflue urbane', 'Progettazione e realizzazione di impianti di depurazione per acque reflue civili, con tecnologie biologiche, fisico-chimiche e avanzate, per garantire il rispetto dei limiti di scarico e la tutela dell’ambiente.'),
   ('gear', 'Sollevamenti e reti fognarie', 'Trattamento e gestione delle acque reflue provenienti dalle reti fognarie, con sistemi di grigliatura, sollevamento, misurazione e controllo, per garantire l’efficienza e la protezione delle infrastrutture.'),
   ('leaf', 'Impianti biologici anaerobici', 'Sistemi di digestione anaerobica per il trattamento dei fanghi e dei reflui ad alto carico organico, con produzione di biogas per il recupero energetico e la valorizzazione dei residui.'),
   ('db', 'Trattamento dei fanghi', 'Sistemi per l’ispessimento, la disidratazione, la stabilizzazione e la gestione dei fanghi provenienti dagli impianti di trattamento, con soluzioni finalizzate alla riduzione dei volumi e alla corretta gestione dei residui.')]),
  'Le nostre soluzioni per i Multi-utility',
  [('Progettazione e realizzazione', 'Nuovi impianti di potabilizzazione, depurazione e infrastrutture idriche, dalla progettazione alla fornitura, installazione e messa in servizio.'),
   ('Revamping e potenziamento', 'Ammodernamento e adeguamento degli impianti esistenti, con interventi mirati per migliorare le prestazioni, l’efficienza energetica e la conformità normativa.'),
   ('Gestione, manutenzione e pronto intervento', 'Servizi di assistenza tecnica, manutenzione programmata, monitoraggio degli impianti e pronto intervento, per garantire affidabilità, continuità operativa e ottimizzazione dei costi di esercizio.')],
  ['plant', 'tools', 'headset'])

if __name__ == '__main__':
    for k, v in pages.items():
        print(k, save(k, v))
