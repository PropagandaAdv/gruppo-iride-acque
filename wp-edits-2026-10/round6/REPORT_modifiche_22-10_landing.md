# Modifiche del 22/10 – landing BIEFFE, scheda Biemme in "Le società", landing Biemme

Sito: https://gruppoirideacque.propagandaadv.com — fatto con il connettore Royal MCP Iride Acque.

## Backup (prima di toccare nulla)
Nessun plugin di backup: copie in bozza dei contenuti toccati.

| Pagina | ID backup |
|---|---|
| Landing BIEFFE (188) | **483** |
| Landing Biemme (204) | **485** |
| Le società del gruppo (64) | **487** |

Sorgenti locali precedenti: `BieffeHomepage.jsx.bak-22-10b`, `media-map.json.bak-22-10b`, `wp/lecce-bak-22-10/`, `biemme-engineering/wp-import/bundle-bak-22-10/`, `BiemmeHomepage.jsx.bak-22-10`.
Screenshot desktop 1440 / tablet 768 / mobile 390 delle tre pagine: cartella `round6/shots/` (`*_top.png` = apertura, `*_full.png` = pagina intera).

## BLOCCANTI / DA CHIEDERE AL CLIENTE (leggere per primi)
1. **Mancano i file multimediali citati.** Nella cartella `Modifiche 22.10` ci sono solo: i due .docx, i loghi, la cartella "da usare come immagine-video iniziale" (6 PNG: opzione 1.a–1.e e 2) e i file della sezione "gruppo" (altro giro). **Non ci sono**: le 3 animazioni (*vasca sedimentazione / equalizzazione / ossidazione*), le 4 immagini dei box "Acquedotti e fognature / Impianti di depurazione / Opere stradali / Opere marittime", i PDF/JPG dei certificati ISO, e il file con i contatti Biemme. Ricercati anche nel resto di `Documenti/Iride Acque`: nessuna corrispondenza. → **A3 (animazione) e A4 (immagini nei box) NON fatti** (restano la struttura in acciaio e i box scuri con icona). Chiedere i file. Nota: le 6 PNG "da usare come immagine-video iniziale" mostrano un cantiere che diventa vasca di sedimentazione: non sono citate nel prompt, **non le ho usate**; se servono come fotogramma iniziale dell'hero o per generare l'animazione, dirmelo.
2. **Contatti Biemme (C8): bloccante.** Il cliente scrive "AGGIORNARE I DATI!" ma non ha mandato i dati nuovi. Lasciati invariati: tel. 0362 244145, fax 0362 240467, info@ / sales@biemmeengineering.it, sede legale Parma, sede operativa Via Montello 43, Seregno. **Nota**: il badge nell'hero ora dice "Milano · Arosio" (come richiesto), ma il footer dice ancora Seregno (MB) e Parma: incoerenza finché non arrivano i dati.
3. **Foto reali Biemme (C9): blocco non presente.** La landing non contiene il blocco con le 4 voci a foto circolari (Disinfezione con biossido di cloro / Trattamento dell'acqua di processo / Dosaggio e monitoraggio automatico / Sanificazione e sistemi centralizzati): lo screenshot del cliente è un mockup. **Non l'ho creato.** Foto reali disponibili (non in "Modifiche 22.10"): `Documenti/Iride Acque/2026.09.03_materiale digitale/BIEMME ENGINEERING/foto impianto Malpensa/` — 32 foto WhatsApp 11/07/2025 + 15 video. Sul mio PC risultano file da 0 byte (solo su OneDrive, non scaricati): se si vuole usarle vanno scaricati. Dove potrebbero sostituire immagini generate: la landing non ha oggi immagini nelle card; potrebbero entrare nelle "Stazioni" o nei "Casi applicativi" (da decidere).
4. **ISO 9001: versione non verificata.** Il PDF `ISO-9001-CERT-06767-2000-AQ-BRI-SINCERT…pdf` non c'è, quindi **non ho scritto la versione**: il box dice "ISO 9001" (prima c'era ":2015"). Dal solo attestato SOA risulta una certificazione di qualità DNV Business Assurance valida fino al 14/07/2027 (non indica la norma). Le versioni degli altri box (14001:2015, 45001:2018, 50001:2018, UNI/PdR 125:2022) sono quelle del prompt/dei nomi file dello screenshot del cliente: **non ho potuto controllare intestatario e versione sui certificati** (file assenti). 45001 corretto da :2015 a :2018.

## A – Landing BIEFFE (`/bieffe-costruzioni/`, pagina 188)
| Punto | Esito |
|---|---|
| A1 sottotitolo hero | Fatto, testo verbatim |
| A2 "Opere pubbliche." + riga sotto | Fatto |
| A3 titolo "Tempi rispettati, obiettivi raggiunti." + testo senza ingegneria naturalistica | Testi fatti. **Animazione al posto della struttura in acciaio: NON fatta (file mancanti, vedi bloccante 1)** |
| A4 elimina "Ingegneria naturalistica", 4 box | Box eliminato, griglia 4 in riga (desktop), 2×2 (tablet), 1 colonna (mobile). **Immagini di sfondo nei box: NON fatte (file mancanti)** |
| A5 "Chi siamo" (1° e 3° paragrafo) | Fatto, verbatim; 2° invariato |
| A6 fascia numeri | Eliminata |
| A7 SOA | OG3 IV-bis · OG6 VII · OG7 III · OS22 VII (attestazione SOATEAM 7925/47/01 del 10/06/2026, coincide con lo screenshot) |
| A7 ISO | 5 box (3+2 desktop, 2 colonne tablet, 1 mobile): ISO 9001 (+logo DNV) · ISO 14001:2015 · ISO 45001:2018 · ISO 50001:2018 · **UNI/PdR 125:2022** (non "ISO"). Vedi bloccante 4 |
| A8 6° box | "Modello 231 e Compliance", icona bilancia, testo verbatim, griglia 3×2 |
| A9 clienti | Tolti Integra / Doronzo / Saceccav; aggiunta Provincia di Lecce dopo Provincia di Brindisi; 7 box (4+3 desktop) |
| A10 tag | Salice Salentino: tolto "In fase di conclusione"; Casarano: aggiunto "Progettazione esecutiva ed esecuzione"; Porto Cesareo (ultimo): tolto l'importo a base d'asta |
| A11 "Principali realizzazioni dell'ultimo ventennio" | Eliminata con il bottone "Mostra tutte". Il menu punta a "Realizzazioni" (resta "Realizzazioni in corso"): nessun link da aggiornare |
| A12 contatti (sezione + footer) | Viale Marcello Chiatante 55, 73100 Lecce (LE) · "Telefono" 0832.1699769 (`tel:+3908321699769`) · info@bieffecostruzionisrl.it (`mailto:`). Il modulo ora scrive a info@bieffecostruzionisrl.it. Nessuna mappa presente |
| A13 modulo | Opzione "Ingegneria naturalistica" tolta |
| A14 controllo finale | Su HTML renderizzato (desktop/tablet/mobile): naturalistica, settore privato, tiscali, Scarambone, 896022, Maltauro, Doronzo, Saceccav, 9.861.373 → **0 occorrenze**. Title: `BIEFFE Costruzioni \| Gruppo Iride Acque` (senza "naturalistica"). **Meta description**: diceva "opere pubbliche e private" → ora "opere pubbliche" (incoerente con A2/A5; unica modifica non esplicitamente richiesta) |

Verifiche: 11 parti dell'incorporamento identiche byte per byte al build (sha `894211a9f34ccaf2`); effetto di scorrimento dell'hero intatto (video a 5,04 s a metà e 9,88 s a fine corsa); nessun errore console, nessuna richiesta fallita, nessuno scroll orizzontale a 1440/768/390; logo orizzontale (22/10 mattina) invariato.

## B – "Le società del gruppo", scheda Biemme (pagina 64)
Fatto: titolo "Biemme Engineering", bottone "Scopri Biemme Engineering →", testo ricomposto verbatim. **Logo non toccato** (restano i loghi verticali delle 3 card). Il link del bottone (`/biemme-engeenering/`) invariato.
"BM Engineering" nel resto del sito: ricerca nell'HTML renderizzato di Home, Il Gruppo, Le società, Contatti, Applicazioni e Servizi, News, Settori, Modello operativo, Lavora con noi e landing Biemme → **ora non compare più da nessuna parte** (compariva solo in questa scheda; la ricerca interna del sito segnalava anche la pagina "Il Gruppo" nei dati ma senza occorrenza visibile nel render). Nessun'altra sostituzione fatta.

## C – Landing Biemme (pagina 204, `/biemme-engeenering-anteprima-nuova-homepage/`)
La landing è la pagina **204**: `/biemme-engeenering/` fa redirect lì; `/biemme-engineering/` dà 404 (il refuso "engeenering" è del cliente); la vecchia pagina 186 è nel cestino.
| Punto | Esito |
|---|---|
| C1 hero | Eyebrow "TRATTAMENTO ACQUE E DISINFEZIONE"; titolo "Acqua pura. Igiene sotto controllo." (sfumatura mantenuta); testo verbatim; badge "Milano · Arosio" |
| C2 "Perché conta" | "…stabilimento alimentare…" |
| C3 card | "Sistemi di dosaggio" nuovo testo; "Strutture in moplen" + nuovo testo; "Stoccaggio…" nuovo testo; card "Dall'acqua di produzione all'acqua di scarico" **eliminata**, la card rimasta ("Misura, controllo e dosaggio integrati") ora occupa tutta la riga: nessun buco |
| C4 Stazione 03 | "Eliminiamo i problemi microbiologici e la formazione di biofilm nella zona dell'acqua fredda." |
| C5 casi applicativi | Eyebrow, titolo e intro nuovi; le due card sostituite con titolo/intro/sfida/soluzione/benefici verbatim ("Nei migliori", refuso corretto); la seconda è più lunga: le due card restano affiancate e allineate in alto, nessun testo tagliato |
| C6 fasi | 4 testi nuovi; fase 03 "Avviamento e collaudo" |
| C7 a chi ci rivolgiamo | Titolo nuovo; sottotesto Dealer Grundfos; 3 card con testi nuovi |
| C8 modulo | Opzione "Trattamento dell'acqua di processo o di scarico" **eliminata** (era l'unica che nominava lo scarico; se il cliente voleva tenere "Trattamento dell'acqua di processo" va rimessa). Contatti: **bloccante 2** |
| C9 foto reali | Blocco non presente: **bloccante 3** |
| C10 controllo finale | Rimossi: "beverage", "limo", "ProMinent", "vetro temperato", "acqua di scarico", "Due sfide concrete"; "Parma" nel badge. **Restano (non coperti dal prompt, segnalati senza modificarli)**: (1) "bevande" nell'intro delle Applicazioni: "Per birra, acqua minerale e bevande."; (2) "bevande" nel footer: "…dosaggio chimico per l'industria delle bevande."; (3) "Parma" nell'indirizzo della sede legale nel footer |

Come è stato fatto: la landing è un'app React incorporata. Ricompilata (la build di partenza era identica byte per byte a quella online), testi cambiati nel sorgente `BiemmeHomepage.jsx`; il nuovo JS è inserito in 6 widget HTML (template 501–506) con un caricatore (template 507) al posto del vecchio file `.txt` rovesciato. Il CSS non è cambiato (uso lo stesso file). Modulo Elementor nascosto, header/menu, logo orizzontale e CSS delle dimensioni logo (22/10 mattina) invariati. Verifiche: 6 parti identiche al build (sha `68240486…`), nessun errore console, nessuno scroll orizzontale a 1440/768/390, menu mobile e hero ok.

## Media usati
| File | Dove |
|---|---|
| — | **Nessun nuovo file multimediale inserito** (i file richiesti non erano presenti: vedi bloccanti) |
| Animazione scelta per A3 | — (nessuna: file assenti) |

## Note tecniche
- Template di servizio creati: 483/485/487 (backup, bozze), 489–500 (landing BIEFFE; 497 è la parte 08 sbagliata, non usata), 501–507 (landing Biemme). Eliminabili dal pannello una volta approvato il lavoro.
- Il testo del tag "Progettazione esecutiva ed esecuzione" ora compare sulle card: Salice Salentino, Lizzanello, Ugento, Porto Cesareo (estendimenti), Carovigno, Galatina, Casarano.
- Cache Elementor svuotata (`_elementor_css`, `_elementor_element_cache`) su 188, 204, 64.
