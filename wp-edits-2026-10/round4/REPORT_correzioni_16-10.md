# Gruppo Iride Acque – Correzioni urgenti del 16/10/2026 (report)

Sito: https://gruppoirideacque.propagandaadv.com – connettore Royal MCP dedicato.

## 0. Backup (prima di toccare nulla)
Nessun plugin di backup attivo (UpdraftPlus / SiteVault non attivi), quindi:
- **Copie in bozza** (cloni Elementor, ID): **420** = landing BIEFFE (pagina 188), **422** = Le società (64), **424** = Home (12).
- Footer (template 42): nessun clone; token di undo del connettore (72 h) sull'operazione `d309f2df…`.
- Copia locale dei widget HTML originali della landing: `costruzioni-bieffe/backup-bieffe-html.json`; sorgenti locali con suffisso `.bak-16-10`.
- Snapshot HTML renderizzati: `round4/snap/`.
- Token di undo (72 h) per ogni scrittura, registrati nella sessione di lavoro.

## 1. Timeline "Il Gruppo" – https://gruppoirideacque.propagandaadv.com/il-gruppo/
- "1° brevetto" è **già 2016** sul sito pubblicato (nessun "2010" presente). Non ho modificato nulla.
- Ricerca "2010" su tutte le 25 pagine pubbliche raggiungibili (testo renderizzato, quindi anche template Elementor, header, footer, widget HTML): **0 occorrenze**.
- Unico "2010" trovato altrove: **solo nei sorgenti locali** della landing BIEFFE, voce lavoro "Ferrobeton, 2008-2010" (anni di un cantiere, non c'entra con il brevetto). Non toccato.
- Ordine verificato su pagina renderizzata: 2015 Nascita Iride Acque → 2016 1° brevetto → 2020 2° brevetto → 2023 Nascita del Gruppo con acquisizione Biemme Engineering → 2024 3° brevetto → 2026 Ingresso di Credem Euromobiliare → 2026 acquisizione Bieffe Costruzioni → Nuova sede → Futuro. (La voce Bieffe si legge "Crescita del Gruppo Iride Acque con acquisizione Bieffe Costruzioni": testo preesistente, non toccato.)

## 2. Landing BIEFFE Costruzioni – https://gruppoirideacque.propagandaadv.com/bieffe-costruzioni/
**Come è costruita:** la landing è l'applicazione React in un unico bundle compresso, inserito in 8+1 widget HTML Elementor (non è Elementor nativo). Per questo la modifica è stata fatta nel sorgente, ricompilata e reinserita (controllo byte per byte del payload: sha256 identico al build).

### 2a. Nome e slug
- Nome → **BIEFFE Costruzioni** in: titolo pagina (WP), `<title>` ("BIEFFE Costruzioni – Gruppo Iride Acque"), header landing (alt logo), footer landing (alt logo, "BIEFFE Costruzioni srl", copyright), testo del blocco sede/storia, alt immagini.
- Slug → `bieffe-costruzioni` (era `costruzioni-bieffe`).
- Link interni aggiornati al nuovo URL: card "Scopri Bieffe Costruzioni" in Le società (https://gruppoirideacque.propagandaadv.com/le-societa-del-gruppo/), card Bieffe in Home (https://gruppoirideacque.propagandaadv.com/), link "Bieffe Costruzioni" nel footer di tutto il sito. Nel menu non c'era nessuna voce verso la landing. Verifica a crawl (25 pagine): nessun link rimasto al vecchio slug. Click reale sulla card Home → atterra sul nuovo URL.
- **301 dal vecchio URL: NON attivo.** Sul sito non c'è plugin di redirect (Redirection non attivo, nessun Yoast Premium) e il meccanismo di WordPress sul vecchio slug (`_wp_old_slug`, che ho impostato) non scatta per le pagine: `/costruzioni-bieffe/` dà ora **404**. Per il 301 serve attivare un plugin di redirect oppure una regola sul server, ad esempio in `.htaccess`:
  `Redirect 301 /costruzioni-bieffe/ /bieffe-costruzioni/`
- Meta description / Open Graph: sul sito non c'è plugin SEO e la landing non ha meta description né og:*; nulla da correggere. Pagina ancora `noindex` (staging).

### 2b. Logo
- Sostituito il logo errato con quello corretto di BIEFFE Costruzioni (monogramma "bf" nei cerchi concentrici + BIEFFE / COSTRUZIONI, file già in Libreria: media 384 `logo-bieffe-costruzioni-gruppo.webp`, lo stesso usato nelle card). Versione con fondo blu brand, senza ricolorazione né distorsione.
- Dove: header (52×58 px desktop, 47×52 mobile), footer (86×96 px). Nessun altro punto della landing lo usava (nessuna favicon propria: la favicon è quella del sito Iride Acque; nessuna immagine con il logo incorporato).
- Vecchio logo (file tipo `Logo_costruzioni_bieffe_200`, media 237 e 206): **rimosso dalla landing, NON cancellato dalla Libreria**. Crawl: nessuna pagina lo usa più.
- Nota: nell'header (52 px) la scritta "COSTRUZIONI" del monogramma è piccola; se il cliente vuole il logo più grande è una modifica di una riga nel sorgente.

## 3. Riferimenti ad ALTRA azienda ancora presenti (non toccati, come richiesto)
Nella landing (testi provvisori che il cliente conosce):
| Dove | Contenuto |
|---|---|
| Contatti (sezione form + footer) | e-mail **info@costruzionibieffe.it** (anche come destinatario del form: il form apre un mailto) |
| Contatti / footer "Dati societari" | indirizzo **Via Costa, 12 – 31040 Giavera del Montello (TV)**; telefono **0422 775223**; **P.IVA e C.F. 04184870261**; "Giavera del Montello · Treviso" |
| Footer, colonna "Sito" | link a costruzionibieffe.it: Chi siamo, Realizzazioni, Photogallery, Contatti, **Privacy e cookie** (informativa privacy collegata al form) |
| Sezione Realizzazioni | schede lavori con link a costruzionibieffe.it/portfolio/… e "tutte le realizzazioni" → costruzionibieffe.it/realizzazioni/; clienti/lavori reali dell'altra azienda (Superbeton, Ecma, Latteria Montello, Parco Cavallino, Comune di Giavera… ) |
| Numeri / Footer | logo e attestazione **CQOP SOA** (+ nota: la scheda cliente chiede di non citare SOA/ISO perché la validità non è confermata) |
| Storia / hero | "General contractor dal 2007", "nasce nel 2007 da due soci", sede "costruita nel 2016", fondatori/titolari |
| Foto | molte foto provengono dal sito dell'altra azienda (alcune accreditate a un fotografo esterno: diritti d'uso da confermare) |

Altrove nel sito:
- **Home**: la card Bieffe ora punta alla landing, ma il vecchio link sovrapposto verso https://costruzionibieffe.it/ (widget `fa26abd9`) **resta nella pagina sotto il nuovo** (il connettore non permette di modificare/eliminare il widget HTML esistente). Il click arriva alla landing, ma conviene eliminare il vecchio widget dall'editor Elementor (1 click).
- **News** (https://gruppoirideacque.propagandaadv.com/news/): bottone "Scopri le news di Bieffe Costruzioni" → https://costruzionibieffe.it/ (sito dell'altra azienda). Non toccato: da decidere dove deve puntare.
- Nome scritto "Bieffe Costruzioni" (non maiuscolo) in testi del cliente di altre 20 pagine (Home, Il Gruppo, Le società – titolo, paragrafo e bottone "Scopri Bieffe Costruzioni", News e articoli, pagine Applicazioni/Settori, Contatti, ecc.): **non modificati** perché fuori dall'elenco delle correzioni. Se vuoi che diventi ovunque "BIEFFE Costruzioni" lo faccio in un passaggio.

## 4. Verifiche
- Landing su nuovo URL, desktop 1440 e mobile 390: nessun overflow, nessun errore console, nessuna richiesta fallita; video hero a scorrimento invariato (currentTime 5,04 s a metà sezione, 9,88 s a fine); logo corretto in header e footer.
- Le società e Home verificate dopo la modifica (desktop + mobile); Le società: confronto HTML prima/dopo → unica differenza l'href del bottone.
- Cache: svuotata la cache Elementor (CSS ed element cache) di 188, 64, 12 e del footer; verificati con richieste con query string.

## 5. Incidenti durante il lavoro (risolti)
- Trascrizione errata di due blocchi del bundle compresso: rilevata dal controllo sha, blocchi rifatti in parti più piccole e verificati (sha finale = build).
- Una scrittura diretta dei dati di Le società (64) ha fatto togliere i tag `<style>`/`<script>` dal widget hero; ripristinata subito e ricostruita la pagina da un nuovo template di libreria (439). Verificato: render identico a prima, salvo l'href.

## 6. Template di libreria creati (inutilizzati/di supporto)
426–430 (bundle landing, 428 e 429 sono le versioni errate, non più usate), 431–436 (parti corrette), 439 (Le società 16/10).
