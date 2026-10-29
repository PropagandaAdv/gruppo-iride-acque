# Censimento codice personalizzato: script/CSS obsoleti (29/10/2026)

Metodo: lettura del DOM renderizzato (Chrome, 1440 px) di 22 pagine pubbliche e dei template che vi compaiono (header 39, template 551 e 612, footer 42), con selettori e ID confrontati tra tutte le pagine. Non letti: Elementor › Custom Code, CSS personalizzato del sito (Aspetto/Site Settings), snippet, tema/child theme (nessun plugin snippet attivo), popup, post singoli del loop "impianti". Nessun elemento e' stato marcato o cancellato: il connettore non puo' modificare ne' rinominare elementi esistenti.
"Nome nel Navigatore": i blocchi non hanno un nome personalizzato (appaiono come "HTML"); si trovano dall'ID elemento (nell'editor: clic destro > Navigatore, oppure Ispeziona `data-id`).

## A. Obsoleti certi: video MP4 hero (sostituiti da YouTube)
| Posizione | Tipo | ID elemento | Cosa fa | Perche' obsoleto |
|---|---|---|---|---|
| Progettazione e realizzazione impianti (292) | JS | e458885a | Aggiunge `<video>` MP4 a `#bhHeroProgettazione .bh-media` | Video ora YouTube |
| Gestione impianti (293) | JS | d17b5f5d | idem su `#bhHeroGestione` | idem |
| Noleggio impianti (294) | JS | 4c2856e3 | idem su `#bhHeroNoleggio` | idem |
| Consulenza ambientale (295) | JS | 54faccd4 | idem su `#bhHeroConsulenza` | idem |
| Settori (296) | JS | 106edbdb | idem su `#bhHeroSettori` | idem |
| Industriale (368) | JS | 731c6f7f | idem su `#bhHeroIndustriale` | idem |
| Civile (574) | JS | 7525ada6 | idem su `#bhHeroCivile` | idem |
| Multi-utility (579) | JS | 709e09e2 | idem su `#bhHeroMultiutility` | idem |
| Trattamento acque primarie (288) | JS | 6f51a3d3 | idem su `#bhHeroPrimarie` | idem |
| Trattamento acque reflue (289) | JS | b999f819 | idem su `#bhHeroReflue` | idem |
| Il Gruppo (55) | JS | f9970223 | idem su `#bhHeroIlGruppo` (gruppo-hero-video.mp4) | idem |
| Le societa' del Gruppo (64) | JS | 734a5702 | idem su `#bhHeroSocieta` | idem |
| Home (12), blocco hero | JS (parte del blocco 37c4aa2e) | 37c4aa2e | Ferma `#iahHeroVideo` con "riduci animazioni" | Il `<video>` MP4 non serve piu': cancellare anche la riga `<video id="iahHeroVideo" ...>` e il `<script>` finale, non il CSS |
| Home, blocco hero | CSS (parte di 37c4aa2e) | 37c4aa2e | Regole `.hero-media video`, `.hero-media` | Video MP4 sostituito (parte del blocco, non tutto) |

## B. Da cancellare solo dopo A (ho aggiunto io, servono solo finche' A esiste)
| Posizione | Tipo | ID elemento | Cosa fa | Note |
|---|---|---|---|---|
| Home | JS | 41ddb22a | Blocca il caricamento dell'MP4 della Home | Inutile dopo aver tolto il `<video>` da 37c4aa2e |
| 288, 289, 292-296, 368, 574, 579 | JS (parte di blocchi CSS "Hero con video YouTube...") | 13553b5a, 82362588, 28414f12, 1adf7544, 51921439, 6c3cd2ec, 1943cf58, 30cd00bc, f923a1f0, 2422aaf4 | Blocca la proprieta' `src` per gli MP4 | Solo la parte `<script>`; il CSS dello stesso blocco serve |
| 288, 289, 292-296, 368, 574, 579, 55 | JS | a3d54f20, 15ba2b6d, 1007c356, c4c5c602, 10470ea7, 29a3c487, 3a1f71d4, 140239af, cc659a64, 2a058fe7, faf77565 | Impedisce ai caricatori condivisi di creare i video MP4 | Serve finche' i template 39/612 esistono (vedi D) |

## C. Probabilmente obsoleti (da confermare)
| Posizione | Tipo | ID elemento | Cosa fa | Perche' |
|---|---|---|---|---|
| Home | HTML+CSS | 219eeb71 | Overlay logo del Gruppo in basso a sinistra sul video | Nascosto da `.iah-brand-overlay{display:none!important}` in 95b3f59e (il simbolo e' ora inserito nel flusso dei testi) |
| Home | CSS | f9f68d60, 2c599952 | Regole 23/10 sull'overlay del simbolo e sull'altezza hero | In parte superate da 95b3f59e/cf24a130; controllare prima di cancellare |
| Header 39 | CSS | 4dd331fb | CSS globale di sezioni (9,3 KB) | 21 selettori su 108 non trovano elementi: `.elementor-element-7a1439b`, `-5575c202`, `-2ab48b93`, `.iah-sector*`, `.iah-hcard .iah-sector-desc`, `#il-gruppo .iah-tl-lbl`, `#posizioni-aperte ...::after` |
| Header 39 | CSS | 63848238 | Griglie/schede | 16 selettori su 24 senza elementi: `.iah-grid2`, `.iah-hcard.iah-pcard`, `.iah-pnum`, `.iah-next*` |
| Header 39 | CSS | 8ea86d03 | Fasce e schede | 6 selettori su 9 senza elementi: `.iah-scard*` |
| Template 551 | CSS | 911a1dc9 | CSS comune `.iah2` (15 KB) | Contiene ancora le regole `.iah2-hero .bh-media` e l'immagine di riserva `hero-template-bg.webp`; il resto serve |

## D. Dubbi (non marcati)
| Posizione | Tipo | ID elemento | Perche' dubbio |
|---|---|---|---|
| Header 39 | JS+CSS | 783c88ec | Caricatore condiviso dei video MP4 hero. Serve ancora a News (`bhHeroNews`); Contatti, Metodo e Lavora sono esclusi. Obsoleto quando News passa a YouTube |
| Template 612 | JS | 1928185a | Secondo caricatore MP4 (duplica 783c88ec). Stessa condizione; titolo del template: "Hero video – loader condiviso" |
| News (131) | JS | 893c0125 | Script MP4 di News; usato finche' News resta con il video MP4 |
| 130, 131, 132, 64, 55 | CSS | 06596a85, fd8078ba, 030196f5, 0e5f068c, bccb5ff4 | Stesso CSS `.brand-hero` (circa 2 KB) duplicato in 5 pagine, con regole video/immagine; duplicati ma legati al markup dell'hero |
| 130 / 131 / 132 / 55 | JS | 06596a85, fd8078ba, 030196f5, bccb5ff4 | Stesso script `setH` (altezza hero) duplicato; ancora in uso |
| Home | JS | 52c5a09c | Corregge i link `/settori/servizio-idrico-integrato` in `/settori/multi-utility`. Il vecchio indirizzo e' ancora presente 2 volte nel codice della Home: ancora utile; conviene correggere i link alla fonte e poi cancellare lo script |
| BIEFFE Costruzioni (188) | JS (bundle React 87 KB) | feca9ee4 | Contiene l'URL dello staging `https://gruppoirideacque.propagandaadv.com/wp-content/uploads/2026/10/bieffe-hero-scrub.mp4`: video che dipende dallo staging, da verificare. Pagina da non toccare |
| BIEFFE / BIEMME (188, 204) | JS | 3bbc529b, 987668f3 | Correzioni del bundle; `KEY="biemmeengineering.it"` e' un identificativo, non un link |
| Landing 188 / 204 | JS (base64) | molti blocchi da 4000 car. | Codice dell'applicazione landing, non analizzabile: non toccare |
| Modello operativo (130) | JS | 037c6ce3 | Apre la fase da `#fase-N`; in uso |
| Home | CSS+JS | 0495c73c, 61a5038a, 625dc787, 6dcab102, 86f943ea, c93f0c82, 95b3f59e, cf24a130, 52c5a09c | In uso (effetti card, contatori, simbolo hero) |
| Landing/altre pagine | CSS | 35853d3b (188), b8ba46cb (204) | Pochi selettori assenti (3/7 e 1/5): probabilmente in uso |
| Tutte le pagine con loop impianti | CSS | 9931bb8a, cc2e1532, 67ad8216, 22b33ca6, a61e2d1b, 9ec7884a | CSS generato da Elementor per il carosello: non e' codice personalizzato |
| Elementor › Custom Code, CSS del sito, WPCode/Code Snippets, tema | - | - | Non accessibili dal connettore (nessun plugin snippet attivo): da controllare a mano |
