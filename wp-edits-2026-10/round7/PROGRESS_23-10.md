# Progresso revisione 23/10 (aggiornato in corso d'opera)

Connettore: Royal MCP Iride (b8293492). Parametro chiave meta = `key` (non `meta_key`); svuotare `_elementor_data` con value `[]`.

## Fatto
- Fase 0/1: inventario, backup, pulizia (cestino: 487, 485, 483, 458, 456, 440, 424, 422, 420, 273, 271; tenuta 400 = proposta B).
- Fase 2: logo "solo scritta" header 39/footer 42 (media 509), Home hero simbolo (media 511) + titolo, footer riutilizzo.
- Fase 3.1 Home: card 4 fasi + tab.
- Fase 3.3 Il Gruppo (55): ricostruita con template 512–516 (hero+video, intro, timeline 8 voci, certificazioni, modello operativo #modello-operativo). Verificata 1440/768/390.
- Fase 3.4 Le società (64): testo Bieffe nuovo (replace_text), widget video 734a5702 (selettore #bhHeroSocieta).
- Fase 3.5 News (131): ricostruita con template 519–521: hero+video, 2 news (Credem 15/05/2026 media 517, Ecomondo 08/10/2026 media 518, link esterni nuova scheda a irideacque.com), sezione "News dalle Aziende" invariata. Pagine figlie 278–281 in bozza.

## File video da caricare a mano (Royal MCP non carica video)
- `round7/upload-manuale/gruppo-hero-video.mp4` -> Media Library, nome esatto (usato da Il Gruppo, Le società, News)
- `round7/upload-manuale/applicazioni-hero-video.mp4` -> idem (Applicazioni e Servizi)
Finché non caricati: il JS rimuove il <video> in errore e resta l'immagine di sfondo (nessun buco).

## Da fare
Fase 4 impianti, Fase 5 pagine applicazioni/servizi, Fase 6 settori, Fase 7 BIEFFE, Fase 8 BIEMME, Fase 9 scan finale, variante B hero Home, report finale.

## Segnalazioni per il report
- Link "Scopri le news di Bieffe Costruzioni" in News punta a costruzionibieffe.it (azienda di Giavera, NON la Bieffe di Lecce): da chiarire con il cliente.
- Template di servizio (eliminabili a lavoro approvato): 512–516 (Il Gruppo), 519–521 (News).
- Immagini news portate da wsrv.nl (proxy per convertire in WebP 1200px) dalle URL pubbliche di irideacque.com.
