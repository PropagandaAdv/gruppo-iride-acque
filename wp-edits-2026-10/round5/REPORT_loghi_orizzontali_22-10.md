# Sostituzione loghi con le versioni orizzontali – Gruppo Iride Acque, 22/10/2026

Sito: https://gruppoirideacque.propagandaadv.com

## Backup (fatti prima di toccare qualsiasi cosa)
Nessun plugin di backup attivo: backup = copie in bozza dei contenuti toccati.

| Elemento | ID backup |
|---|---|
| Landing BIEFFE (pagina 188) | **456** |
| Landing Biemme Engineering (pagina 204) | **458** |
| Header globale (template 39) | **460** |
| Footer globale (template 42) | **462** |

Sorgenti locali precedenti: `costruzioni-bieffe/site/src/BieffeHomepage.jsx.bak-22-10`, `wp-embed/media-map.json.bak-22-10`, `wp/lecce-bak-19-10/`. Prima/dopo degli screenshot: `shots_before/` e `shots_after/` in questa cartella.

## Nuovi file in Libreria Media (nessun file esistente è stato sovrascritto)
| ID | File | Alt |
|---|---|---|
| 464 | `logo-gruppo-iride-acque-orizzontale-420.webp` | Gruppo Iride Acque |
| 465 | `logo-biemme-engineering-orizzontale-360.webp` | Biemme Engineering |
| 466 | `logo-bieffe-costruzioni-orizzontale-360.webp` | BIEFFE Costruzioni |

Parametro usato per il Gruppo: `logo-gruppo-iride-acque-orizzontale` (non la variante "nuovo-lettering"). `lettering-gruppo-iride-acque` non usato. Mappatura dei 12 file incollati verificata per confronto pixel. Fondo scuro su tutti i punti sostituiti (i PNG hanno il testo bianco).

## Censimento (prima di sostituire)
Censimento automatico di 25 pagine/landing (tutte quelle raggiungibili dal menu e dai link interni), a 1440 px, con colore di sfondo calcolato dietro ogni logo.

| Pagina / template | Sezione | Quale logo | File attuale (prima) | Sfondo | Azione | Motivo |
|---|---|---|---|---|---|---|
| Header globale (template 39), tutte le pagine del sito | header | Gruppo | `logo-iride-acque.png` (solo simbolo + "IRIDE ACQUE" in testo HTML) | scuro `rgba(9,23,31,.86)` | **SOSTITUITO** → media 464 | Logo del Gruppo nell'header |
| Footer globale (template 42), tutte le pagine | footer | Gruppo | `logo-iride-acque.png` | scuro `#09171F` | **SOSTITUITO** → media 464 | Logo del Gruppo nel footer |
| Landing Biemme Engineering (204) | header, menu mobile, footer | Biemme | logo verticale `logo-biemme-engineering…` | scuro `#0D2B3E` | **SOSTITUITO** → media 465 | Logo della stessa società, orizzontale |
| Landing BIEFFE Costruzioni (188) | header, footer | BIEFFE | `logo-bieffe-costruzioni-gruppo.webp` (verticale) | scuro `#0E1A24` / `#0B151D` | **SOSTITUITO** → media 466 | Logo della stessa società, orizzontale |
| Landing Biemme / BIEFFE: logo del Gruppo dentro la landing | – | Gruppo | non presente | – | nessuna azione | Non presente nelle landing |
| **Le Società del Gruppo** (pagina 64) | 3 card con logo verticale | Iride Acque, BM/Biemme, BIEFFE | `logo-iride-acque-gruppo.webp`, `logo-biemme-engineering-gruppo.webp`, `logo-bieffe-costruzioni-gruppo.webp` | scuro `#00243C` | **NON TOCCATO** | Richiesta cliente: "teniamo quelli!!" |
| Home (pagina 12), sezione "Le società del Gruppo" | 3 card con gli stessi loghi | idem | idem | scuro `#00243C` | **NON TOCCATO** | Da confermare col cliente (vedi sotto) |
| Favicon / icona del sito | – | simbolo | – | – | **NON TOCCATO** | Escluso dal prompt |
| Loghi terze parti (SOA Team, DNV·GL ISO 9001, clienti) | landing BIEFFE | terze parti | media 442/443 | – | **NON TOCCATO** | Escluso dal prompt |

Altri punti con loghi trovati dal censimento: nessuno (le altre pagine mostrano solo header/footer globali).

## Cosa è stato fatto
- **Header 39:** immagine `36f1e375` sostituita con il media 464 (alt "Gruppo Iride Acque"). Aggiunto un widget HTML (`fbcdd5fa`) con le regole di dimensione: logo 133 px di larghezza (≈56 px di altezza) su desktop, 114 px tablet, 95 px mobile (≈40 px). Nascosta la scritta "IRIDE ACQUE" in HTML accanto al vecchio simbolo (`17a9d6ec`), ora ridondante: resta nel DOM, solo non visibile. L'altezza dell'header non è cambiata.
- **Footer 42:** immagine `a9b36ed6` sostituita con il media 464, 200 px di larghezza.
- **Landing Biemme (204):** header, menu mobile e footer con il logo orizzontale (header ≈56 px desktop, footer ≈72 px), regole CSS aggiunte nel widget. Modulo, hero e scroll invariati.
- **Landing BIEFFE (188):** sorgente React aggiornato (header 40/44/52 px di altezza, footer 64/80 px), `media-map.json` puntato al media 466, bundle ricompilato e reinserito (12 parti + loader). **Verifica byte per byte: tutte le 12 parti identiche al build** (sha256 `7de46d0a78747b68…`). Effetto di scorrimento dell'hero intatto (video a 5,04 s a metà e 9,88 s a fine corsa).
- Dopo ogni modifica cancellati `_elementor_css` e `_elementor_element_cache`.

## Verifiche
- Nessuna sostituzione globale di immagini; ogni punto è stato cambiato singolarmente.
- Header e footer con il nuovo logo su tutte le 25 pagine censite (ripetuto il censimento dopo le modifiche): **0 riferimenti** al vecchio `logo-iride-acque.png` nell'header/footer. Gli unici file vecchi ancora usati sono i loghi verticali delle card "Le società", lasciate di proposito.
- **"Le Società del Gruppo" identica a prima:** confronto dell'HTML renderizzato prima/dopo → le uniche differenze sono header e footer (logo + widget CSS); il corpo della pagina è identico. Stesso risultato per la Home. Screenshot prima/dopo a 1440 e 390 px in `shots_before/` e `shots_after/`.
- Desktop 1440 e mobile 390: menu su una riga, nessun accavallamento del logo con l'hamburger (header mobile e landing), nessuno scroll orizzontale. Console senza errori, nessuna richiesta fallita sulla landing BIEFFE.
- Cache Elementor svuotata; richieste verificate con query string per evitare la cache del server.

## Punti lasciati invariati perché lo sfondo è chiaro
Nessun punto *da sostituire* aveva sfondo chiaro, quindi nessun logo bianco è stato messo su fondo chiaro. Un caso va però segnalato:
- **`/privacy-policy`**: il link nel sito porta a una pagina **404** ("La pagina non può essere trovata", già così prima di questo lavoro). L'header lì sta su fondo bianco, quindi il logo bianco non si vede (come già il menu). Non ho modificato nulla. **Da fare lato cliente/noi:** creare la pagina privacy; per un header su fondo chiaro servirebbe la **versione del logo per fondi chiari** (da chiedere al cliente).

## Da confermare col cliente
1. **Home, sezione "Le società del Gruppo":** lasciata coi loghi verticali (come la pagina "Le Società"). Vanno sostituiti con quelli orizzontali o no?
2. **Pagina `/privacy-policy` inesistente** (404) e relativo header su fondo chiaro (vedi sopra).
3. **Dimensione del logo nell'header:** a 56 px di altezza il lettering "ACQUE"/"COSTRUZIONI" è piccolo ma leggibile; se si vuole più grande serve più altezza dell'header (non l'ho fatto: regola del prompt).

## Limiti tecnici / note
- I loghi sono stati caricati a 360–420 px di larghezza (webp), non alla risoluzione originale: il connettore accetta solo upload piccoli (≈16K caratteri base64). Per schermi retina andrebbe caricata la versione grande dal pannello WP (Media → Aggiungi) e sostituita al posto dei media 464–466.
- `wp_update_custom_css` è bloccato dall'impostazione "Allow AI to modify theme appearance" di Royal MCP: le regole di dimensione sono state messe in un widget HTML dell'header (e nelle landing), non nel CSS aggiuntivo del tema.
- Template di servizio creati: 467 (Biemme), 468–472, 474, 475–480 e 481/482 (parti della landing BIEFFE); 473 è un duplicato rotto, non usato. Si possono eliminare dal pannello (Modelli → Salvati).
- File dei loghi vecchi (`logo-iride-acque.png` ID 15 e gli altri verticali) lasciati nella Libreria Media: ancora usati dalle card "Le società", non cancellati.
- Il vecchio URL `/costruzioni-bieffe/` risponde ancora 404 (nessun redirect): da aggiungere un 301 se serve.
