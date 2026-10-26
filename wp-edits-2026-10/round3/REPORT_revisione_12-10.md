# Gruppo Iride Acque – Revisione sito, giro modifiche del 12/10/2026 (report del 13/10/2026)

Sito: https://gruppoirideacque.propagandaadv.com – connettore Royal MCP dedicato (non quello di siti.propagandaadv.com).

## 1. Fatto (pagina per pagina)

**Home** – https://gruppoirideacque.propagandaadv.com/
- 1.1 Card "Cosa facciamo" rinominate: 01 Progettazione · 02 Produzione · 03 Gestione · 04 Ottimizzazione e rendicontazione, con le 4 foto reali del cliente (alt text aggiornati).
- 1.2 Paragrafo introduttivo di "Che cosa significa gestione integrata del ciclo idrico?" giustificato. I testi delle fasi non sono stati toccati (in attesa).
- 1.3 "Le società del Gruppo Iride Acque": inseriti i 3 loghi ufficiali. I loghi sono bianchi su fondo blu → le card hanno lo stesso blu (#00243C).
- 1.4 "Ambiti di intervento": 2 card ridisegnate come da riferimento (nuove immagini, velo più leggero, icona/titolo/testo/link in basso a sinistra, hover con testo e fondo blu che si espandono in ~0,4 s, su touch/mobile il testo è sempre aperto). Tutta la card è cliccabile: Settori > Industriale / Servizio idrico integrato.

**Il Gruppo** – /il-gruppo/
- 2.1 Animazione nell'hero: il video non è caricabile in libreria (solo immagini) → animazione a dissolvenza tra 4 fotogrammi estratti da ANIMAZIONE.mp4. **Proposta B** (acqua: onde, gocce e cerchi, solo CSS) sulla bozza non pubblicata "Il Gruppo – proposta B" (ID 400): modifica https://gruppoirideacque.propagandaadv.com/wp-admin/post.php?post=400&action=edit (il link di anteprima pubblica dà 404, usare l'editor).
- 2.2 Titolo invariato. Sottotitolo NON modificato (testo del cliente incompleto) → vedi proposte al punto 2.
- 2.3 Timeline sostituita: niente popup al passaggio, alternata, in ordine cronologico, su mobile verticale. "Nuova sede" subito dopo Bieffe, senza anno.
- 2.4 Certificazioni e attestati: SOA (OG3, OG6, OG7, OS22) e ISO 9001, 14001, 45001:2015.
- 2.5 "Un processo strutturato in quattro fasi": non toccato (in attesa).

**Le società del gruppo** – /le-societa-del-gruppo/
- 3 card con i 3 loghi (Iride Acque, BIEMME Engineering, BIEFFE Costruzioni); struttura pronta per gli sfondi che arriveranno.
- Immagine hero NON sostituita (file non ricevuto).

**Applicazioni e Servizi**
- /trattamento-acque-primarie-e-di-processo/ e /trattamento-acque-reflue/ ricostruite con i testi di sito.docx (verificati uno per uno sulla pagina renderizzata: 71 + 82 testi, 0 differenze). Struttura: Hero → Le nostre tecnologie → Vantaggi → Settori di applicazione → Case study → Contattaci. Primarie: 9 tecnologie, 4 vantaggi, 3 settori. Reflue: 5 paragrafi hero (primi 2 evidenziati), 11 tecnologie (3+3+3 e le ultime 2 più larghe), 4 vantaggi, 2 settori, case study Tintoria Emiliana ed ENI | Sarroch con tag, più riquadro "Prossimi progetti".
- Rimosse "Servizi di assistenza e manutenzione" e "Applicazione successiva" dalle pagine Applicazioni. "Contattaci" = il modulo di contatto globale del footer, identico in tutte le pagine (nessuna fascia aggiuntiva).
- Frecce delle card solo decorative (nessun link).
- ZLD (290) e Trattamento fanghi (291): passate a **bozza** (non eliminate), tolte dal menu (voci 316/317), dalla panoramica /tecnologie-e-servizi/, dalle pagine Settori e dai link dei progetti (ora puntano a "Trattamento acque reflue"). Controllo sul sito: 0 riferimenti rimasti.
- Settori: /settori/industriale/ e /settori/servizio-idrico-integrato/ mostrano solo le 2 applicazioni rimaste.
- Voci di menu "Applicazioni" e "Servizi" non sono più `#` ma puntano a /tecnologie-e-servizi/#applicazioni e #servizi.

**Contatti** – /contatti/: "Dove siamo" (mappa + indirizzo) sotto il modulo, come confermato.

## 2. In attesa del cliente
- Testi delle fasi in Home ("Che cosa significa gestione integrata del ciclo idrico?") e "Un processo strutturato in quattro fasi".
- Contenuti della pagina Settori (in revisione dei tecnici).
- Immagini hero di: Le società, Applicazioni e Servizi, Settori, News, Contatti ("nel solito link": nello zip ricevuto non ci sono).
- Immagini di sfondo delle 3 società.
- Pagine progetto per i link "Scopri il progetto" dei case study (il link è stato omesso perché non esiste la pagina).
- Anno della nuova sede di Arosio (la timeline lo mostra senza anno).
- Sottotitolo Il Gruppo – due proposte, entrambe costruite solo con parole già presenti nel sito:
  1. «Iride Acque, Biemme Engineering e Bieffe Costruzioni integrano progettazione, ingegneria e capacità esecutiva avanzate per il trattamento delle acque reflue civili e industriali, il loro riutilizzo e il recupero delle materie valorizzabili, dall'analisi alla realizzazione e manutenzione degli impianti.»
  2. «Iride Acque, Biemme Engineering e Bieffe Costruzioni integrano progettazione, ingegneria e realizzazione per offrire soluzioni avanzate nel trattamento, nella gestione e nel riutilizzo delle acque industriali e civili.»

## 3. Da decidere
1. **Proposta B dell'animazione** (bozza ID 400): tenere A (dissolvenza fotogrammi) o passare a B? Il video originale si può usare solo se caricato come file/hosting video.
2. **Foto case study**: le 3 immagini sono ritagli dei mockup del documento (ID media 403, 404, 407, ~460 px): vanno sostituite con foto reali.
3. **Testi hero Applicazioni**: nel documento il testo scritto e il mockup differiscono; ho usato il testo scritto. Nel mockup "Promuovi amo" → corretto in "Promuoviamo".
4. **Pagine Servizi (292–295)**: il cliente ha chiesto di togliere "assistenza" e "successiva" dalle *applicazioni*; nei Servizi le due fasce sono rimaste. Le tolgo anche lì?
5. **Redirect 301 ZLD/Fanghi → Reflue**: impossibile, nessun plugin redirect attivo (Redirection non attivo, Yoast Premium assente). Le due URL ora danno 404; per i 301 serve attivare un plugin o una regola lato server.
6. **noindex**: le pagine Applicazioni/Servizi/Settori hanno ancora il meta noindex (residuo della fase di copia); da togliere alla messa online.
7. **Link esterni in Home** (card società): puntano ai siti delle aziende; biemmeengineering.it ha certificato SSL scaduto (avviso nel browser) e costruzionibieffe.it è un'impresa edile di Treviso. Esistono le pagine interne /biemme-engeenering/ e /costruzioni-bieffe/: le usiamo?
8. **Logo**: versione usata = quella del cliente (bianco su blu). Se serve su fondo chiaro, serve la versione a colori/vettoriale.
9. **Biemme Engineering**: nome come da cliente; l'indirizzo sul loro sito è Seregno, non Arosio.

## 4. Verifiche (fase QA)
- 17 pagine × 1440 / 768 / 390 px: nessun overflow orizzontale, nessun errore console, nessuna richiesta fallita.
- 27 link unici verificati: tutti ok tranne il sito esterno Biemme (SSL scaduto). Nessun 404, nessun `#` residuo (menu corretto).
- ZLD/Fanghi assenti da menu, footer, griglie e link interni.
- Hover card "Ambiti di intervento" e timeline mobile verificati nei round precedenti con screenshot.

## 5. Backup / ripristino
- Nessun plugin di backup attivo: snapshot JSON locali delle pagine in `wp-edits-2026-10/round3/backup_live/` + token di undo del connettore (validi 72 h dall'operazione, ogni scrittura di pagina e ogni voce di menu eliminata ne ha uno: pagine 288, 289, 66, 368, 369, 292, 12, 55, 64, 78; voci menu 316 e 317). Per ripristinare una pagina: `mcp_undo_last_operation` con il token registrato nella sessione di lavoro.
- Template in libreria Elementor creati in questo giro: 394, 398, 399, 401, 402, 408–415.
