# Revisione del 23/10 – Gruppo Iride Acque + landing BIEFFE e BIEMME (report finale)

Sito: https://gruppoirideacque.propagandaadv.com – connettore Royal MCP Iride Acque.

## Da fare subito (azioni di Giovanni, 5 minuti)
1. **Rigenerare CSS e dati di Elementor** (Elementor › Strumenti › Rigenera CSS e dati). Dopo la riconnessione il connettore non può più cancellare `_elementor_css` / `_elementor_element_cache` (chiavi "protected"): le pagine toccate dopo l'ultima rigenerazione (Settori 296, Industriale 368, Civile 574, Multi-utility 579, Consulenza 295 e la Home) possono mostrare ancora l'HTML vecchio.
2. **Caricare in Libreria Media i due video** (Royal MCP non carica video), con il nome esatto, da `round7/upload-manuale/`: `gruppo-hero-video.mp4` (Il Gruppo, Le società, News) e `applicazioni-hero-video.mp4` (Applicazioni, Servizi, Settori). Finché mancano, gli hero restano con l'immagine di sfondo (il video si rimuove da solo se non si carica).
3. **Redirect 301** (nessun plugin di redirect attivo, il connettore non può impostare gli slug): vedi "Non fatto".

## Backup
- Bozze di backup create da me: Home **568** (26/10), Biemme **527**, Bieffe **543**. I backup della revisione precedente (pagine 487, 485, 483…) sono nel cestino.
- Pulizia backup (Fase 1), nel cestino: 487, 485, 483, 458, 456, 440, 424, 422, 420, 273, 271. **Lasciata per dubbio**: 400 "Il Gruppo – proposta B". Template Elementor con nome da backup: non toccati (elenco sotto).
- Template di servizio creati oggi (eliminabili a lavoro approvato): 512–516 (Il Gruppo), 519–521 (News), 535 (card impianto, **da tenere**), 536/539/540 (sezione impianti: **540 da tenere**), 551 (CSS pagine, **da tenere**), 552/558/562/565/566/567 (applicazioni/servizi), 571 (Home), 576–578, 581 (settori), 541–548 (Biemme), 549–564 (Bieffe, loader 430).

## Fase per fase
| Fase | Esito |
|---|---|
| 0 Inventario | Fatto. |
| 1 Pulizia backup | Fatto (vedi sopra). |
| 2 Globali | Logo solo scritta in header/footer (media 509), simbolo in grande sull'hero Home, titolo ingrandito (4 righe a 1440, il limite di 3 non è raggiungibile senza rimpicciolire), footer "riutilizzo". **Variante B della Home (logo orizzontale) NON preparata.** Il video iStock non è stato toccato (va acquistato). |
| 3.1–3.2 Home | Card e tab delle 4 fasi come da testo. |
| 3.3 Il Gruppo | Video hero (da caricare), sottotitolo verbatim, timeline (Maggio 2026 / Agosto 2026, niente "Futuro", ultimo tratto tratteggiato, senza sovrapposizioni a 1440/768/390), "Il nostro modello operativo" con ancora `#modello-operativo`, certificazioni allineate a BIEFFE + Modello 231. |
| 3.4 Le società | Video hero, testo Bieffe, loghi intatti. |
| 3.5 News | Solo 2 news (Credem 15/05/2026, Ecomondo 08/10/2026) con titolo, estratto e immagine reali dai siti sorgente, link in nuova scheda. Le 4 pagine news locali (278–281) in bozza. |
| 4 Impianti | Fatto: articoli nella categoria "Impianti" (sottocategorie Applicazione: primarie/reflue, Settore: industriale/civile/multi-utility, Servizio: gestione), un solo Loop Item (535) + Loop Carousel (2 card desktop, 1 mobile, frecce), si nasconde da solo se vuoto. 6 impianti popolati. |
| 5 Applicazioni e Servizi | Rifatte: primarie (288), reflue (289), progettazione (292), gestione (293), noleggio (294), consulenza (295). Nessun numero/freccia/"Scopri di più" vuoto; card di pari altezza; sezioni "Prossimi progetti", "Servizio successivo", "Applicazione successiva" rimosse. |
| 6 Settori | Rifatte: Settori (296), Industriale (368), **Civile (574, nuova)**, **Multi-utility (579, nuova; la vecchia 369 è nel cestino)**. Menu: Industriale · Civile · Multi-utility. |
| 7 BIEFFE | Fatto (vedi sotto). |
| 8 BIEMME | Fatto (vedi sotto). |
| 9 Controllo finale | Scansione eseguita (sotto). |

## Non fatto / limiti
- **Redirect 301**: nessun plugin di redirect (né Yoast); il connettore non permette di modificare gli slug. Conseguenze: la pagina **Noleggio** ha titolo e menu "Noleggio impianti" ma **slug invariato** `noleggio-impianti-mobili`; **Multi-utility** è una pagina nuova (`/settori/multi-utility/`) e il vecchio `/settori/servizio-idrico-integrato/` ora dà 404 (nessun link interno lo usa più dopo la rigenerazione). Serve un redirect lato server/plugin se esistono link esterni.
- **Immagini dei sotto-settori** (11 industriali + 7 civili + 6 multi-utility) e delle card "soluzioni": **non generate** (il generatore Magnific si è disconnesso durante la sessione, 3 chiamate interrotte). Al loro posto tessere con icona. Immagini degli impianti: segnaposto neutro (media 526), perché il cliente vuole foto reali.
- Pagine Settori/Civile/Multi-utility create senza il template "Elementor larghezza intera" (non impostabile dal connettore): ho nascosto il titolo del tema con CSS; conviene impostare "Larghezza intera" dal pannello Pagina in Elementor.
- Hero Home: il simbolo è inserito nel flusso da un piccolo script (il testo dell'hero è un unico widget HTML).
- Footer/Form: l'opzione "Servizio Idrico Integrato" nel menu "Tipologia di richiesta" non è stata cambiata (non richiesto).

## Da far decidere al cliente
1. Hero Home: logo variante A (simbolo, attuale) o B (orizzontale) – la B non è ancora pronta.
2. Sottotitolo de Il Gruppo senza verbo principale (inserito verbatim; correzione proposta: "…Bieffe Costruzioni integrano esperienza, ingegneria…").
3. SOA BIEFFE: l'attestazione 7925/47/01 (10/06/2026) riporta solo OG3 IV-bis, OG6 VII, OG7 III, OS22 VII; il cliente dice che "mancano categorie": chiedere il PDF originale.
4. Melendugno: classificato **Civile** (reflue + civile); alternativa multi-utility.
5. Terza card "Ambiti" in Home: non aggiunta; la card PA ora punta a Multi-utility (titolo "Soluzioni per i Multi-utility e la PA").
6. Il link "News dalle Aziende › Bieffe Costruzioni" punta a costruzionibieffe.it (azienda di Giavera, non la Bieffe di Lecce).

## Materiale mancante
Foto reali degli impianti; elenco (circa 5) delle realizzazioni BIEFFE; video iStock da acquistare; i due MP4 da caricare; PDF originale SOA; pagina `/privacy-policy` (404, usata dalla landing Biemme); contatti Biemme aggiornati.

## Immagini generate con IA
Nessuna nuova. Le news usano le immagini delle pagine sorgente; gli impianti il segnaposto. Nota: le immagini case-study esistenti (Campari, Tintoria, ENI) restano in Libreria ma non sono più usate.

## Come aggiungere un impianto (mini-guida)
1. Bacheca › Articoli › Aggiungi nuovo. Titolo = nome dell'impianto; **Estratto** = testo; **Immagine in evidenza** = foto (meglio WebP, 1200 px).
2. Nella colonna Categorie spunta **solo le sottocategorie**: una di Applicazione (Acque primarie… / Acque reflue) e una di Settore (Industriale / Civile / Multi-utility). Non spuntare "Impianti".
3. In "Campi personalizzati" (se non appare: Opzioni schermo › Campi personalizzati) aggiungi `settore_label` (es. "Settore tessile"), `sottotitolo` (facoltativo) e `tag_tecnologie` (es. "UF ceramica • NF • EMER").
4. Pubblica: l'impianto compare da solo nei caroselli delle pagine collegate alle sue categorie (e in "Progettazione e realizzazione"). Per la pagina Gestione usa la categoria "Servizio – Gestione e manutenzione".

## Scansione finale (Fase 9)
- 20 pagine controllate: nessuna stringa vietata ("Prossimi progetti", "Servizio successivo", "Applicazione successiva", "Dealer Grundfos"); "riuso" nel footer e "Futuro" nella timeline assenti; ZLD/fanghi non nel menu; nessuno scroll orizzontale.
- Link: unico 404 interno = vecchio `/settori/servizio-idrico-integrato/` (ancora linkato dall'overlay della Home finché non si rigenera la cache; ho aggiunto un piccolo script di allineamento) e `/privacy-policy` (Biemme). `/biemme-engeenering/` risponde 301 verso la landing. "Scopri di più →" resta solo nelle card Settori (portano a pagine esistenti).

## Landing BIEFFE (pagina 188) – Fase 7
Tipografia allineata al Gruppo; eyebrow "Lecce · dal 2010" rimosso; sottotitolo e 1° paragrafo "Chi siamo" verbatim (il 2° non citato è invariato: ora dice 2010 vs "dal 1923" nel 1°, da far valutare); blocco "Modello organizzativo" prima di Associazioni; "Soci fondatori" tolto, Modello 231 primo, numerazione 01–05; "Realizzazioni in corso" tolto e ripristinate le 26 "Principali realizzazioni dell'ultimo ventennio" in carosello (3/2/1 card, frecce) – array `REALIZZAZIONI` in `BieffeHomepage.jsx`. Payload sha 0c55f5d7f78f6c20, 12/12 parti identiche. Backup 543.

## Landing BIEMME (pagina 204) – Fase 8
Testi più grandi (classi `bm-*`); H1 "L'acqua per un'industria più sicura" (accent azzurro); "Dealer Grundfos" → "Service Grundfos" (2 occorrenze, 0 residue). H1/H2 erano già più grandi del Gruppo e non sono stati ridotti. Payload sha 38126730…, 6/6 parti. Backup 527. Restano: contatti, "bevande"/"Parma" nel footer, foto reali.

## Home – simbolo sopra il testo (26/10)
Simbolo 130/90/68 px sopra eyebrow e titolo, allineato a sinistra, fade-in 600 ms; verificato live a 1440/1024/768/390 (screenshot `scratchpad/home26live_*.png`); backup 568.
