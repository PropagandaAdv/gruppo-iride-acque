# Censimento codice personalizzato: script/CSS obsoleti (29/10/2026)

Metodo: lettura del DOM renderizzato (Chrome, 1440 px) di 22 pagine pubbliche e dei template che vi compaiono (header 39, template 551 e 612, footer 42), con selettori e ID confrontati tra tutte le pagine. Non letti: Elementor > Custom Code, CSS personalizzato del sito, snippet, tema/child theme (nessun plugin snippet attivo), popup, post singoli del loop "impianti". Nulla e' stato marcato o cancellato: il connettore non puo' modificare ne' rinominare elementi esistenti.

## Come trovare un blocco in Elementor
1. **Pagina**: Pagine > passa il mouse sulla pagina > *Modifica con Elementor* (oppure `wp-admin/post.php?post=ID&action=elementor`).
2. **Template** (header 39, 551, 612): Modelli > Theme Builder > *Header* (39); Modelli > *Sezioni salvate* (551 e 612). Si modificano con lo stesso editor.
3. Apri il **Navigatore** (icona a livelli in basso a sinistra, o Ctrl+I): mostra l'albero dei contenitori. I blocchi HTML non hanno nome, compaiono come "HTML": usa il percorso della colonna "Dove" e conta i blocchi dall'alto. In alternativa clic destro sul blocco > *Ispeziona* mostra `data-id` = ID elemento.
4. Nelle pagine di servizio il **contenitore hero** e' il 2° contenitore dall'alto (il 1° contiene solo i template CSS richiamati dall'intestazione); in Home, Il Gruppo e Le societa' e' il 1°. Dentro il contenitore hero i blocchi sono nell'ordine: contenitore con il video YouTube, blocchi CSS/script aggiunti (sopra), **blocco HTML dell'hero** (quello con eyebrow e titolo), e subito sotto lo **script del vecchio video MP4**.

## A. Obsoleti certi: video MP4 hero (sostituiti da YouTube)
| Pagina (ID) | Tipo | ID elemento | Dove in Elementor | Cosa fa | Perche' obsoleto |
|---|---|---|---|---|---|
| Progettazione e realizzazione impianti (292) | JS | e458885a | 2° contenitore (id 3e4f2321) > ultimo blocco HTML, subito sotto il blocco hero (4ccad9c1) | Aggiunge `<video>` MP4 a `#bhHeroProgettazione .bh-media` | Video ora YouTube |
| Gestione impianti (293) | JS | d17b5f5d | 2° contenitore (667d41ef) > ultimo blocco HTML, sotto il blocco hero (35c5e6f8) | idem su `#bhHeroGestione` | idem |
| Noleggio impianti (294) | JS | 4c2856e3 | 2° contenitore (0fe34339) > ultimo blocco HTML, sotto il blocco hero (24930a61) | idem su `#bhHeroNoleggio` | idem |
| Consulenza ambientale (295) | JS | 54faccd4 | 2° contenitore (1f27329f) > ultimo blocco HTML, sotto il blocco hero (e9467547) | idem su `#bhHeroConsulenza` | idem |
| Settori (296) | JS | 106edbdb | 2° contenitore (5a357a56) > ultimo blocco HTML, sotto il blocco hero (6eb0023f) | idem su `#bhHeroSettori` | idem |
| Industriale (368) | JS | 731c6f7f | 2° contenitore (e38771b3) > ultimo blocco HTML, sotto il blocco hero (9f8f4587) | idem su `#bhHeroIndustriale` | idem |
| Civile (574) | JS | 7525ada6 | 2° contenitore (8bd8f791) > ultimo blocco HTML, sotto il blocco hero (4ff1f772) | idem su `#bhHeroCivile` | idem |
| Multi-utility (579) | JS | 709e09e2 | 2° contenitore (93974d68) > ultimo blocco HTML, sotto il blocco hero (d617887e) | idem su `#bhHeroMultiutility` | idem |
| Trattamento acque primarie (288) | JS | 6f51a3d3 | 2° contenitore (d77f2ef6) > ultimo blocco HTML, sotto il blocco hero (4aa98ac6) | idem su `#bhHeroPrimarie` | idem |
| Trattamento acque reflue (289) | JS | b999f819 | 2° contenitore (46755b21) > ultimo blocco HTML, sotto il blocco hero (910cd218) | idem su `#bhHeroReflue` | idem |
| Il Gruppo (55) | JS | f9970223 | 1° contenitore (af93ebc9) > blocco HTML dopo il blocco hero (bccb5ff4) e dopo il blocco CSS 47c48c6a | idem su `#bhHeroIlGruppo` (gruppo-hero-video.mp4) | idem |
| Le societa' del Gruppo (64) | JS | 734a5702 | 1° contenitore (b39dd761) > blocco HTML subito sotto il blocco hero (0e5f068c) | idem su `#bhHeroSocieta` | idem |
| Home (12) | JS (parte di un blocco) | 37c4aa2e | 1° contenitore (53ff6d63, "sec-hero") > blocco HTML hero (4° dall'alto: dopo il contenitore video e due blocchi CSS). Modifica il codice: togli la riga `<video id="iahHeroVideo" ...></video>` e il `<script>` finale | Ferma `#iahHeroVideo` con "riduci animazioni" | Il `<video>` MP4 non serve piu' |
| Home (12) | CSS (parte dello stesso blocco) | 37c4aa2e | stesso blocco; solo le regole `.hero-media video` e `.hero-media` | Stile del vecchio video | Video MP4 sostituito (non cancellare il resto del CSS) |

## B. Da cancellare solo dopo A (aggiunti da me, servono solo finche' esiste A)
| Pagina | Tipo | ID elemento | Dove in Elementor | Cosa fa | Note |
|---|---|---|---|---|---|
| Home (12) | JS | 41ddb22a | 1° contenitore (53ff6d63) > 2° elemento dall'alto, sopra il blocco hero | Blocca il caricamento dell'MP4 | Inutile dopo aver tolto il `<video>` |
| 288, 289, 292-296, 368, 574, 579 | JS (parte `<script>` di un blocco CSS) | 13553b5a, 82362588, 28414f12, 1adf7544, 51921439, 6c3cd2ec, 1943cf58, 30cd00bc, f923a1f0, 2422aaf4 | Contenitore hero > blocchi HTML in cima, sopra il blocco hero (2° o 3° dall'alto) | Blocca la proprieta' `src` per gli MP4 | Togliere solo il `<script>`; il CSS dello stesso blocco serve |
| 288, 289, 292-296, 368, 574, 579, 55 | JS | a3d54f20, 15ba2b6d, 1007c356, c4c5c602, 10470ea7, 29a3c487, 3a1f71d4, 140239af, cc659a64, 2a058fe7, faf77565 | Contenitore hero > blocchi HTML in cima, sopra il blocco hero | Impedisce ai caricatori condivisi di creare i video MP4 | Serve finche' i caricatori 39/612 esistono (vedi D) |

## C. Probabilmente obsoleti (da confermare)
| Pagina | Tipo | ID elemento | Dove in Elementor | Cosa fa | Perche' |
|---|---|---|---|---|---|
| Home (12) | HTML+CSS | 219eeb71 | 1° contenitore (53ff6d63) > blocco HTML subito sotto il blocco hero (classe CSS `iah-brand-overlay`) | Overlay del logo in basso a sinistra | Nascosto da `.iah-brand-overlay{display:none!important}` (blocco 95b3f59e) |
| Home (12) | CSS | f9f68d60, 2c599952 | 1° contenitore (53ff6d63) > blocchi HTML dopo il blocco 219eeb71 (3° e 4° dopo l'hero) | Regole 23/10 su overlay simbolo e altezza hero | In parte superate da 95b3f59e e cf24a130 |
| Header (template 39) | CSS | 4dd331fb | Contenitore unico (e850cb70) > 1° blocco HTML in alto (classe `iah-global`), sopra il logo | CSS globale (9,3 KB) | 21 selettori su 108 senza elementi: `.elementor-element-7a1439b`, `-5575c202`, `-2ab48b93`, `.iah-sector*`, `.iah-hcard .iah-sector-desc`, `#il-gruppo .iah-tl-lbl`, `#posizioni-aperte ...::after` |
| Header (39) | CSS | 63848238 | stesso contenitore > blocco HTML dopo il bottone "Richiedi una valutazione tecnica" | Griglie/schede | 16 selettori su 24 senza elementi (`.iah-grid2`, `.iah-hcard.iah-pcard`, `.iah-pnum`, `.iah-next*`) |
| Header (39) | CSS | 8ea86d03 | stesso contenitore > blocco HTML subito dopo 63848238 | Fasce e schede | 6 su 9 senza elementi (`.iah-scard*`) |
| Template 551 | CSS | 911a1dc9 | Sezioni salvate > "CSS pagine Applicazioni, Servizi e Settori (iah2)" > contenitore 8febc6f0 > 1° blocco HTML | CSS comune `.iah2` (15 KB) | Contiene ancora le regole per `.iah2-hero .bh-media` e per l'immagine di riserva `hero-template-bg.webp`; il resto serve |

## D. Dubbi (non marcati)
| Pagina | Tipo | ID elemento | Dove in Elementor | Perche' dubbio |
|---|---|---|---|---|
| Header (39) | JS+CSS | 783c88ec | Contenitore e850cb70 > blocco HTML tra 94395295 e 451ccbf5 (il 9° blocco HTML) | Caricatore condiviso dei video MP4 hero; serve ancora a News. Obsoleto quando News passa a YouTube |
| Template 612 | JS | 1928185a | Sezioni salvate > "Hero video - loader condiviso" > contenitore db2b3192 > unico blocco HTML | Secondo caricatore MP4 (duplica 783c88ec). Stessa condizione |
| News (131) | JS | 893c0125 | 1° contenitore (8e3b91cb) > blocco HTML subito sotto il blocco hero (fd8078ba) | Script MP4 di News; usato finche' News resta con MP4 |
| Modello operativo (130), News (131), Lavora con noi (132), Le societa' (64), Il Gruppo (55) | CSS | 06596a85 (130), fd8078ba (131), 030196f5 (132), 0e5f068c (64), bccb5ff4 (55) | 1° contenitore, blocco HTML dell'hero (ef7f0474 / 8e3b91cb / d086d701 / b39dd761 / af93ebc9) | Stesso CSS `.brand-hero` (~2 KB) duplicato 5 volte | Duplicato ma nello stesso blocco del markup dell'hero: non si puo' cancellare da solo |
| 130, 131, 132, 55 | JS | 06596a85, fd8078ba, 030196f5, bccb5ff4 | stesso blocco hero | Script `setH` (altezza hero) duplicato | Ancora in uso |
| Home (12) | JS | 52c5a09c | Ultimo contenitore (8dc6f5a1) > 2° blocco HTML | Corregge i link `/settori/servizio-idrico-integrato` in `/settori/multi-utility` | Il vecchio indirizzo e' ancora presente 2 volte nel codice: corregger i link alla fonte, poi cancellare |
| BIEFFE Costruzioni (188) | JS (bundle) | feca9ee4 | Blocco HTML della landing (React 87 KB) | Contiene l'URL dello staging `gruppoirideacque.propagandaadv.com/.../bieffe-hero-scrub.mp4`; da verificare. Pagina da non toccare |
| BIEFFE / BIEMME (188, 204) | JS | 3bbc529b, 987668f3 | Blocchi HTML della landing | Correzioni del bundle; `KEY="biemmeengineering.it"` e' un identificativo, non un link |
| Landing 188 / 204 | JS (base64) | blocchi da 4000 car. | Landing | Codice dell'applicazione, non analizzabile: non toccare |
| Modello operativo (130) | JS | 037c6ce3 | 2° contenitore (b336b3df) > contenitore 035f91e1 > blocco HTML sotto le schede | Apre la fase da `#fase-N`; in uso |
| Home (12) | CSS+JS | 0495c73c, 61a5038a, 625dc787 (in fondo al contenitore "Settori" e8b1cdc9), 6dcab102 (contenitore Numeri 1e776207), 86f943ea, c93f0c82, 95b3f59e (ultimo contenitore 8dc6f5a1), cf24a130 | Vedi ID | In uso (effetti card, contatori, simbolo hero) |
| Landing 188 / 204 | CSS | 35853d3b, b8ba46cb | Blocchi HTML della landing | Pochi selettori assenti: probabilmente in uso |
| Pagine con loop impianti | CSS | 9931bb8a, cc2e1532, 67ad8216, 22b33ca6, a61e2d1b, 9ec7884a | Widget "Carosello loop" | CSS generato da Elementor: non e' codice personalizzato |
| Elementor > Custom Code, CSS del sito, WPCode/Code Snippets, tema | - | - | Impostazioni sito / Custom Code | Non accessibili dal connettore: da controllare a mano |
