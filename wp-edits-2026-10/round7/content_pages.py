from build_pages import *

pages = {}

# ================= 5.1 PRIMARIE =================
tech1 = [
 ('Filtrazione e chiarificazione', 'Sistemi per la rimozione di solidi sospesi, torbidità e impurità mediante diverse tecnologie di filtrazione.'),
 ('Trattamenti a membrana', 'Ultrafiltrazione, nanofiltrazione e osmosi inversa per la separazione di contaminanti e sali disciolti.'),
 ('Addolcimento', 'Soluzioni per la riduzione della durezza dell’acqua e la prevenzione delle incrostazioni.'),
 ('Demineralizzazione e acqua ultrapura', 'Sistemi a scambio ionico, elettrodeionizzazione (EDI) e tecnologie integrate per la produzione di acqua ad elevata purezza.'),
 ('Adsorbimento e rimozione contaminanti', 'Tecnologie su carboni attivi, resine selettive e altri materiali per la rimozione di sostanze organiche e contaminanti specifici.'),
 ('Disinfezione e controllo microbiologico', 'Sistemi UV, clorazione, dosaggio di disinfettanti e altre soluzioni per il controllo della contaminazione microbiologica.'),
 ('Dosaggio e condizionamento chimico', 'Impianti per il dosaggio di reagenti, la regolazione del pH e il condizionamento delle acque di processo.'),
 ('Trattamenti elettrochimici', 'Tecnologie elettrochimiche per la rimozione di contaminanti, la disinfezione e il condizionamento dell’acqua.'),
 ('Potabilizzazione', 'Impianti integrati per la produzione di acqua destinata al consumo umano, nel rispetto dei requisiti normativi.'),
]
tech2 = [
 ('Pretrattamenti meccanici ed equalizzazione', 'Grigliatura, vagliatura, dissabbiatura, disoleazione e sistemi di equalizzazione e omogeneizzazione dei reflui.'),
 ('Trattamenti chimico-fisici', 'Coagulazione, flocculazione, neutralizzazione, precipitazione chimica e strippaggio dell’ammoniaca per la rimozione di contaminanti specifici.'),
 ('Flottazione e sedimentazione', 'Sistemi DAF, sedimentatori e chiarificatori per la separazione di solidi sospesi, oli, grassi e fanghi.'),
 ('Trattamenti biologici aerobici', 'Impianti a fanghi attivi, SBR, MBBR e MBR, con processi di nitrificazione e denitrificazione per la rimozione della sostanza organica e dei nutrienti.'),
 ('Trattamenti biologici anaerobici', 'Processi anaerobici per reflui ad elevato carico organico, con possibilità di produzione e recupero energetico del biogas.'),
 ('Trattamenti a membrane', 'Microfiltrazione, ultrafiltrazione, nanofiltrazione e osmosi inversa per la separazione dei contaminanti, l’affinamento e il recupero delle acque.'),
 ('Filtrazione e trattamenti terziari', 'Filtri a sabbia, multistrato, carbone attivo, resine a scambio ionico e materiali adsorbenti per la rimozione dei contaminanti residui.'),
 ('Ossidazione avanzata e tecnologia EMER', 'Processi di ossidazione chimica e avanzata, inclusa la tecnologia proprietaria EMER, per il trattamento di reflui complessi e contaminanti difficilmente biodegradabili.'),
 ('Disinfezione e affinamento finale', 'Sistemi UV e trattamenti chimici per il controllo microbiologico e il miglioramento della qualità delle acque trattate.'),
 ('Evaporazione, cristallizzazione ed essiccamento', 'Evaporatori industriali, cristallizzatori ed essiccatori per la concentrazione dei reflui, il recupero dell’acqua e la gestione dei residui solidi, anche in sistemi ZLD.'),
 ('Trattamento e disidratazione fanghi', 'Sistemi di ispessimento, condizionamento, centrifugazione e filtrazione meccanica per il trattamento dei fanghi e la riduzione dei volumi da gestire.'),
]
S1 = ('Soluzioni per il trattamento delle acque primarie e delle acque di processo destinate ai cicli produttivi, ai servizi di stabilimento e agli impianti tecnologici, con applicazioni nei principali settori industriali.',
      'Sistemi per il trattamento, la filtrazione e il condizionamento delle acque primarie e di processo destinati a edifici, complessi residenziali e commerciali, strutture ricettive, Ho.Re.Ca. e servizi.',
      'Soluzioni per il trattamento delle acque primarie e delle acque di processo dedicate a gestori del servizio idrico e infrastrutture collettive, con applicazioni in approvvigionamento, distribuzione, trattamento e recupero delle acque.')
S2 = ('Soluzioni per il trattamento delle acque reflue provenienti dai processi produttivi, dai servizi di stabilimento e dagli impianti tecnologici, con applicazioni nei principali settori industriali e obiettivi di conformità allo scarico, riuso e ottimizzazione dei consumi.',
      'Sistemi per il trattamento delle acque reflue civili destinati a edifici, complessi residenziali e commerciali, strutture ricettive, Ho.Re.Ca. e servizi, con soluzioni orientate alla depurazione, al rispetto dei limiti di scarico e al possibile recupero della risorsa idrica.',
      'Soluzioni per il trattamento delle acque reflue dedicate a gestori del servizio idrico e infrastrutture collettive, con applicazioni in depurazione, adeguamento impiantistico, riqualificazione delle reti e miglioramento della qualità ambientale e della continuità del servizio.')

pages['primarie'] = page(
 hero('bhHeroPrimarie', 'Applicazioni', 'Trattamento acque primarie e di processo', [
  'Il Gruppo Iride progetta e realizza impianti per il trattamento delle acque primarie e di processo, sviluppando soluzioni tecnologiche su misura per le esigenze dei settori industriale, civile e tecnologico.',
  'Grazie alle competenze integrate delle società del Gruppo, offriamo soluzioni complete, dalla consulenza e progettazione fino alla costruzione e messa in servizio degli impianti, garantendo elevati standard di qualità, affidabilità ed efficienza operativa.',
  'Attraverso l’impiego di tecnologie avanzate di filtrazione, separazione, purificazione, addolcimento, demineralizzazione e disinfezione, miglioriamo le caratteristiche dell’acqua, rendendola idonea ai diversi utilizzi e promuovendo una gestione sostenibile delle risorse idriche.']),
 wrap(sec('wh', head('', 'Le nostre tecnologie') + grid(3, [card(t, p) for t, p in tech1]), ' id="tecnologie"')),
 wrap(sec('lt', head('Perché scegliere il Gruppo Iride', 'I vantaggi delle nostre soluzioni', [
   'Le nostre soluzioni per il trattamento delle acque offrono valore concreto e misurabile, combinando tecnologia, competenza ed esperienza per rispondere alle esigenze specifiche di ogni settore.',
   'Lavoriamo al fianco dei nostri clienti per garantire impianti affidabili, efficienti e sostenibili, capaci di migliorare la qualità dell’acqua e ottimizzare i processi produttivi.']) +
   grid(4, [card('Soluzioni su misura', '', 'target', None, 'sm'), card('Efficienza operativa', '', 'chart', None, 'sm'),
            card('Affidabilità e qualità', '', 'clip', None, 'sm'), card('Sostenibilità e ottimizzazione delle risorse', '', 'leaf', None, 'sm')]), ' id="vantaggi"')),
 wrap(setsec('Settori di applicazione', three_settori(S1))),
)

# ================= 5.2 REFLUE =================
pages['reflue'] = page(
 hero('bhHeroReflue', 'Applicazioni', 'Trattamento acque reflue', [
  'Il Gruppo Iride progetta e realizza impianti per il trattamento delle acque reflue industriali e civili, offrendo soluzioni tecnologiche avanzate e personalizzate per la depurazione, il recupero delle risorse e la gestione sostenibile degli scarichi.',
  'Grazie alle competenze integrate delle società del Gruppo, sviluppiamo sistemi in grado di trattare reflui di diversa origine e composizione, attraverso l’impiego di processi fisici, chimici, biologici e termici, finalizzati alla rimozione degli inquinanti, al recupero dell’acqua e alla valorizzazione delle materie prime e dei sottoprodotti recuperabili.',
  'Le nostre soluzioni comprendono sistemi di trattamento e gestione dei fanghi, tecnologie di concentrazione e recupero delle acque, fino alla realizzazione di impianti a scarico liquido zero (Zero Liquid Discharge – ZLD), progettati per eliminare gli scarichi liquidi e massimizzare il recupero delle risorse.',
  'Ogni impianto viene sviluppato considerando le caratteristiche del refluo, le specifiche esigenze produttive e i requisiti normativi applicabili, con particolare attenzione all’efficienza dei processi, all’affidabilità operativa e all’ottimizzazione dei consumi e dei costi di gestione.',
  'Dalla consulenza e dallo studio preliminare fino alla progettazione, costruzione e messa in servizio degli impianti, il Gruppo Iride affianca i propri clienti nella realizzazione di soluzioni integrate e su misura, contribuendo alla riduzione dell’impatto ambientale e alla promozione di modelli produttivi sempre più sostenibili e orientati ai principi dell’economia circolare.']),
 wrap(sec('wh', head('', 'Le nostre tecnologie') + grid(3, [card(t, p) for t, p in tech2]), ' id="tecnologie"')),
 wrap(sec('lt', head('Perché scegliere il Gruppo Iride', 'I vantaggi delle nostre soluzioni', [
   'Progettiamo impianti di depurazione su misura, combinando competenze ingegneristiche e tecnologie di trattamento per ottimizzare le prestazioni, ridurre l’impatto ambientale e favorire il recupero delle risorse.']) +
   grid(4, [card('Efficacia depurativa', 'Soluzioni progettate per garantire la rimozione degli inquinanti e il raggiungimento dei requisiti qualitativi richiesti, nel rispetto dei limiti di scarico e delle esigenze di processo.', 'drop'),
            card('Efficienza operativa', 'I nostri impianti ottimizzano consumi, prestazioni e continuità di esercizio, contribuendo alla riduzione dei costi di gestione e manutenzione.', 'chart'),
            card('Impianti completamente automatizzati', 'Sistemi di controllo e automazione evoluti consentono una gestione affidabile, continua e semplificata dell’impianto, con monitoraggio costante dei processi e rapido intervento operativo.', 'monitor'),
            card('Sostenibilità e recupero delle risorse', 'Le nostre soluzioni favoriscono il recupero dell’acqua e, ove possibile, delle materie prime, contribuendo a modelli produttivi più efficienti, sostenibili e orientati all’economia circolare.', 'recycle')]), ' id="vantaggi"')),
 wrap(setsec('Settori di applicazione', three_settori(S2))),
)

# ================= 5.3 PROGETTAZIONE =================
pages['progettazione'] = page(
 hero('bhHeroProgettazione', 'Progettazione e realizzazione impianti', 'Soluzioni su misura, dalla progettazione alla realizzazione chiavi in mano', [
  'Gruppo Iride Acque è specializzato nella progettazione e realizzazione di impianti per il trattamento delle acque <a href="%s/trattamento-acque-primarie-e-di-processo/">primarie, delle acque di processo</a> e delle <a href="%s/trattamento-acque-reflue/">acque reflue</a>, offrendo soluzioni tecnologiche personalizzate per applicazioni industriali, civili e pubbliche.' % (SITE, SITE),
  'Seguiamo ogni fase del progetto, dall’analisi delle esigenze del cliente e dallo studio di fattibilità fino alla progettazione, costruzione, installazione, collaudo e messa in servizio dell’impianto.',
  'Attraverso l’integrazione di tecnologie innovative e consolidate, sviluppiamo sistemi affidabili ed efficienti, con particolare attenzione alla qualità dell’acqua trattata, all’ottimizzazione dei consumi energetici e dei costi operativi, al rispetto dei requisiti normativi e alla valorizzazione della risorsa idrica.',
  'Realizziamo sia nuovi impianti chiavi in mano sia interventi di ampliamento, revamping e potenziamento di sistemi esistenti, adattando ogni soluzione alle specifiche esigenze produttive e ambientali del cliente.']),
 wrap(sec('lt', head('', 'Il nostro metodo', ['Un percorso completo, dalla progettazione alla gestione']) + steps(3, [
   ('docsearch', 'Analisi preliminare', 'Raccolta delle esigenze, dei dati disponibili e degli obiettivi di progetto.'),
   ('chart', 'Studio di fattibilità', 'Valutazione tecnica, economica e operativa delle soluzioni possibili.'),
   ('monitor', 'Progettazione', 'Sviluppo del processo, del layout e delle specifiche funzionali dell’impianto.'),
   ('crane', 'Realizzazione e installazione', 'Costruzione, fornitura delle apparecchiature e montaggio in sito.'),
   ('gear', 'Collaudo e messa in servizio', 'Avviamento dell’impianto, verifiche funzionali e ottimizzazione iniziale.'),
   ('headset', 'Assistenza post-avviamento', 'Supporto tecnico e affiancamento operativo nelle fasi successive alla partenza.')]), ' id="metodo"')),
 wrap(setsec('Le nostre <span class="ac">soluzioni</span> impiantistiche', grid(3, [
   card('Impianti chiavi in mano', 'Realizzazione di nuovi sistemi completi', 'plant'),
   card('Revamping e ampliamenti', 'Adeguamento e potenziamento di impianti esistenti', 'tools'),
   card('Integrazione tecnologica', 'Inserimento di nuovi processi e apparecchiature', 'gear')]))),
)

# ================= 5.4 GESTIONE =================
pages['gestione'] = page(
 hero('bhHeroGestione', 'Gestione impianti', 'Efficienza, affidabilità e continuità operativa nel tempo', [
  'Gruppo Iride Acque offre servizi di gestione, assistenza tecnica e manutenzione degli impianti di trattamento delle acque primarie, di processo e reflue, con l’obiettivo di garantire prestazioni costanti, continuità operativa e rispetto dei requisiti normativi.',
  'Attraverso attività di monitoraggio, manutenzione programmata e interventi di ottimizzazione, supportiamo i nostri clienti nella gestione quotidiana degli impianti, prevenendo le anomalie di funzionamento, riducendo il rischio di fermo e migliorando l’efficienza dei processi di trattamento.',
  'Il nostro approccio prevede soluzioni personalizzate in funzione delle caratteristiche dell’impianto e delle esigenze operative del cliente, dalla semplice assistenza tecnica periodica fino a servizi di gestione continuativa, con particolare attenzione alla qualità dell’acqua trattata, alla durata delle apparecchiature e all’ottimizzazione dei costi di esercizio.']),
 wrap(sec('wh', head('', 'I nostri servizi di gestione') + grid(3, [
   card('Gestione operativa degli impianti', 'Supporto tecnico per la conduzione quotidiana e il corretto funzionamento dei sistemi di trattamento.', 'gear'),
   card('Manutenzione ordinaria e straordinaria', 'Interventi programmati e correttivi per preservare efficienza, sicurezza e continuità di esercizio.', 'wrench'),
   card('Monitoraggio e controllo delle prestazioni', 'Verifica dei parametri di processo e delle performance impiantistiche per mantenere standard costanti.', 'chart'),
   card('Ottimizzazione dei processi e dei consumi', 'Analisi e regolazioni mirate per migliorare l’efficienza operativa e ridurre i costi di esercizio.', 'leaf'),
   card('Assistenza tecnica e risoluzione anomalie', 'Supporto specialistico per individuare criticità e ripristinare rapidamente le corrette condizioni di funzionamento.', 'headset'),
   card('Analisi e verifiche della qualità delle acque', 'Controlli analitici e verifiche tecniche per assicurare la conformità delle acque trattate alle esigenze di processo o di scarico.', 'drop')]), ' id="servizi"')),
 wrap(sec('lt', head('', 'I vantaggi di una gestione efficiente') + grid(4, [
   card('Continuità operativa', 'Prevenzione dei guasti e riduzione dei fermi impianto attraverso controlli periodici e interventi mirati.', 'gear'),
   card('Riduzione dei costi di esercizio', 'Ottimizzazione dei consumi energetici, dei reagenti e delle risorse necessarie al funzionamento dell’impianto.', 'db'),
   card('Conformità normativa', 'Controllo costante della qualità delle acque trattate per favorire il rispetto dei limiti di scarico e dei requisiti applicabili.', 'clip'),
   card('Maggiore durata degli impianti', 'Manutenzione preventiva e corretta gestione delle apparecchiature per preservarne l’efficienza e prolungarne la vita utile.', 'clock')]), ' id="vantaggi"')),
)

# ================= 5.5 NOLEGGIO =================
pages['noleggio'] = page(
 hero('bhHeroNoleggio', 'Noleggio impianti', 'Soluzioni flessibili, modulari e pronte a rispondere a ogni esigenza temporanea', [
  'Gruppo Iride Acque offre soluzioni per il noleggio di impianti mobili e modulari destinati al trattamento delle acque primarie, di processo e reflue, rispondendo alle esigenze di aziende, stabilimenti industriali e infrastrutture pubbliche e private.',
  'Il servizio rappresenta una soluzione flessibile per garantire la continuità operativa durante interventi di manutenzione, ampliamento o revamping degli impianti esistenti, affrontare situazioni di emergenza, gestire incrementi temporanei delle portate o effettuare campagne di prova e trattamenti di durata limitata.',
  'Grazie a un approccio tecnico personalizzato, individuiamo le soluzioni più adatte in funzione delle caratteristiche delle acque, delle portate richieste e delle specifiche condizioni operative, privilegiando sistemi compatti, modulari e facilmente integrabili nelle infrastrutture esistenti.',
  'Il noleggio consente di ridurre gli investimenti iniziali, ottimizzare i tempi di intervento e garantire flessibilità operativa, offrendo un’alternativa efficace alla realizzazione di impianti permanenti per esigenze temporanee.']),
 wrap(sec('wh', head('', 'Quando scegliere un impianto a noleggio?') + grid(4, [
   card('Emergenze operative', 'Soluzioni temporanee per garantire la continuità del trattamento in caso di guasti, fermo impianto o criticità improvvise.', 'alert'),
   card('Manutenzioni programmate', 'Supporto durante interventi di manutenzione, revamping o adeguamento di impianti esistenti.', 'wrench'),
   card('Incrementi temporanei di portata', 'Impianti mobili per gestire picchi produttivi, esigenze stagionali o necessità straordinarie di trattamento.', 'chart'),
   card('Campagne prova e esigenze temporanee', 'Sistemi modulari per test applicativi, trattamenti provvisori e attività di durata limitata.', 'flask')]), ' id="quando"')),
 wrap(sec('lt', head('', 'Dal fabbisogno alla soluzione operativa') + steps(4, [
   ('docsearch', 'Analisi delle esigenze', 'Valutiamo le caratteristiche dell’acqua, le portate richieste, i tempi di utilizzo e le condizioni di installazione.'),
   ('gear', 'Scelta dell’impianto', 'Proponiamo la soluzione più adatta tra le nostre unità mobili, configurandola in base alle specifiche tecniche e operative.'),
   ('truck', 'Consegna e avviamento', 'Ci occupiamo del trasporto, del posizionamento e del collegamento dell’impianto, garantendo un avviamento rapido e sicuro.'),
   ('headset', 'Assistenza durante il noleggio', 'Forniamo supporto tecnico per tutto il periodo di utilizzo, con interventi programmati e assistenza in caso di necessità.')], True), ' id="fabbisogno"')),
)

# ================= 5.6 CONSULENZA =================
pages['consulenza'] = page(
 hero('bhHeroConsulenza', 'Consulenza ambientale e permitting', 'Competenze tecniche e supporto specialistico per una gestione ambientale efficiente e conforme alle normative', [
  'Gruppo Iride Acque offre servizi di consulenza tecnico-ambientale e supporto nei procedimenti autorizzativi, affiancando aziende, enti pubblici e operatori industriali nella gestione delle problematiche ambientali legate al trattamento, allo scarico e al riutilizzo delle acque.',
  'Attraverso un approccio multidisciplinare, sviluppiamo studi di fattibilità, valutazioni tecnico-economiche e analisi delle prestazioni ambientali, individuando soluzioni personalizzate per migliorare l’efficienza dei processi, ottimizzare l’utilizzo delle risorse idriche e rispondere ai requisiti normativi applicabili.',
  'Forniamo inoltre assistenza nella predisposizione della documentazione tecnica necessaria per le procedure autorizzative, inclusi i procedimenti relativi agli scarichi idrici e alle autorizzazioni ambientali, accompagnando il cliente nelle diverse fasi del percorso tecnico e amministrativo, in collaborazione con gli enti competenti.']),
 wrap(sec('wh', head('', 'I nostri ambiti di consulenza') + grid(3, [
   card('Analisi e caratterizzazione delle acque', 'Valutazione delle caratteristiche delle acque e degli inquinanti presenti per individuare criticità e opportunità di trattamento.', 'flask'),
   card('Audit tecnici e ambientali', 'Verifica dello stato degli impianti, delle prestazioni e dei requisiti ambientali, con individuazione degli interventi migliorativi.', 'clip'),
   card('Studi di fattibilità', 'Analisi delle alternative tecnologiche e valutazioni tecnico-economiche per definire le soluzioni più adatte a ogni esigenza.', 'chart'),
   card('Ottimizzazione dei processi', 'Individuazione di interventi per migliorare l’efficienza dei trattamenti e ridurre consumi energetici, reagenti e costi operativi.', 'gear'),
   card('Recupero e riutilizzo delle acque', 'Studi e soluzioni per favorire il recupero della risorsa idrica e ridurre il consumo di acqua primaria nei processi produttivi.', 'recycle'),
   card('Valutazione dei requisiti normativi', 'Analisi dei limiti di scarico e degli obblighi ambientali applicabili, a supporto delle scelte tecniche e gestionali.', 'scale')]), ' id="ambiti"')),
 wrap(sec('dk', head('Supporto tecnico e autorizzativo', 'Permitting e autorizzazioni ambientali', ['Competenze tecniche al servizio della conformità ambientale e della gestione dei procedimenti autorizzativi.']) + grid(2, [
   card('Autorizzazioni agli scarichi idrici', 'Supporto tecnico per nuove autorizzazioni e modifiche degli scarichi in fognatura, acque superficiali e altri recapiti consentiti.', 'drop', None, 'hz'),
   card('Autorizzazione Unica Ambientale (AUA)', 'Assistenza tecnica nei procedimenti di rilascio, rinnovo e modifica dell’AUA, con particolare riferimento alla gestione delle acque.', 'docs', None, 'hz'),
   card('Autorizzazione Integrata Ambientale (AIA)', 'Supporto specialistico nella predisposizione degli elaborati tecnici relativi al trattamento delle acque, alle prestazioni ambientali e al monitoraggio.', 'gear', None, 'hz'),
   card('Rinnovi e modifiche autorizzative', 'Assistenza nell’aggiornamento delle autorizzazioni esistenti, nella valutazione delle modifiche impiantistiche e nell’adeguamento ai requisiti applicabili.', 'leaf', None, 'hz')]), ' id="permitting"')),
 wrap(sec('lt', head('Il nostro approccio', 'Un supporto tecnico in ogni fase', ['Affianchiamo i nostri clienti attraverso un percorso strutturato e personalizzato, dall’analisi iniziale delle esigenze fino al supporto nei procedimenti autorizzativi.']) + steps(4, [
   ('docsearch', 'Analisi preliminare', 'Raccolta delle informazioni, valutazione delle esigenze e identificazione delle principali criticità ambientali.'),
   ('scale', 'Valutazione tecnico-normativa', 'Analisi dei requisiti normativi applicabili e individuazione delle soluzioni tecniche più appropriate.'),
   ('docs', 'Sviluppo della documentazione', 'Predisposizione di studi, relazioni tecniche ed elaborati necessari alle valutazioni e alle procedure autorizzative.'),
   ('hands', 'Assistenza e supporto', 'Affiancamento del cliente nei procedimenti ambientali e supporto tecnico anche nelle fasi successive.')], True), ' id="approccio"')),
)

CSS_TPL = 551
def cssinc():
    return {"id": nid(), "elType": "container", "isInner": False,
            "settings": {"content_width": "full", "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}},
            "elements": [{"id": nid(), "elType": "widget", "widgetType": "template", "elements": [], "settings": {"template_id": str(CSS_TPL)}}]}
for _k in list(pages):
    pages[_k] = [cssinc()] + pages[_k]

if __name__ == '__main__':
    open(os.path.join(OUT, 'site.css'), 'w', encoding='utf-8').write(CSS + '\n' + icon_css() + '\n')
    print('site.css', os.path.getsize(os.path.join(OUT, 'site.css')))
    for k, v in pages.items():
        print(k, save(k, v))
