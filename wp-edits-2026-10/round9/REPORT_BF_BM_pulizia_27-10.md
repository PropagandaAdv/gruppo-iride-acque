# BF bianca, allineamento BM, pulizia backup – 27/10/2026

Sito: gruppoirideacque.propagandaadv.com (connettore Royal MCP Iride Acque, verificato).

## Backup completo del sito: NON ESEGUITO
Nessun plugin di backup è attivo (SiteVault, UpdraftPlus, Duplicator: "non attivo"; Performance Cache disattivato). Plugin attivi: Elementor, Elementor Pro, Imagify, one.com, Royal MCP. Il backup file + database va fatto dal pannello one.com. Prima di ogni modifica ho creato copie di sicurezza di pagina: BF 621 (stato rotto), BM 623, più i vecchi 590 (BF integro del 26/10), 592, 543, 527, 568, 613.
Revisioni di partenza: BF 188 = 437 (16/10, vuota) e 189; BM 204 = nessuna revisione salvata.

## 1. Pagina BF (188) – bianca
Causa: il contenuto della landing è un unico flusso gzip+base64 spezzato in 12 blocchi `<script type="text/x-bieffe" data-i="0..11">` e ricostruito nel browser (DecompressionStream). Dal rifacimento del 26/10 (10:12–10:13: scrittura di `_elementor_data` + inserimento dei 12 pezzi "BF 26-10 part 00–11" + loader 430) due blocchi sono corrotti: il 01 (4.003 caratteri invece di 4.000) e il 07 (5.357 invece di 4.000). Il flusso non si decomprime (zlib: "invalid distance too far back" dopo 13.849 byte; console: `Bieffe embed TypeError: Failed to fetch`) e la pagina resta bianca, anche da non loggato. Gli stessi blocchi corrotti sono nei pezzi sorgente 594–611, non solo nella pagina. Nessun errore PHP (debug log disattivato), pagina pubblicata, template Elementor Canvas, nessuna password. Altre pagine: nessun errore JS su 20 pagine.
Soluzione: annullati nell'ordine i 13 inserimenti del 26/10, poi riapplicati i pezzi integri "BF 23-10 part 00–11" (549, 550, 553–557, 559–561, 563, 564) e il loader 430. I dati salvati sono identici byte per byte al backup 590 (12 blocchi da 4.000 caratteri, gunzip OK 120.331 byte). Verificato live: testo 8.463 caratteri, console pulita, nessuno scroll orizzontale a 1440/768/390.
Perso: le modifiche del rifacimento del 26/10 (probabilmente tipografia e correzioni testi dopo la verifica documenti): non recuperabili perché il flusso è corrotto. Da riapplicare dopo aver ricostruito i pezzi 26/10 da una sorgente integra. Pezzi 594–611: da non riusare.
Undo (72 h): 5b7d2f3e…, deb8f061…, 263ef57c…, 2d4e9351…, 334eb6df…, 65af8bd1…, 4002d6a1…, 4dec236d…, f8152c14…, f5b18142…, a1384d0e…, 583306b6…, loader 046497b0….

## 2. Pagina BM (204)
| Voce | Esito |
|---|---|
| BM/BF maiuscolo | OK: la pagina usa i nomi per esteso ("Biemme Engineering"), nessun "Bm/Bf" |
| "impianti costruiti" | OK: assente |
| Paragrafo sotto la griglia | Corretto in "Settori diversi, soluzioni su misura" (regola CSS, testo invariato, widget `db85787a`, undo `7c1710751e9fe33d864aa8f93471c810`). Da decidere: "Seguiamo l'acqua in ogni stazione" (la griglia è la timeline sticky, il paragrafo finirebbe dopo 5 stazioni) e "Tutto ciò che serve…" (paragrafo affiancato al titolo) |
| Linea del metodo | OK: già presente (Fase 01–04 collegate) |
| Header/footer/menu/logo | È una landing autonoma con header, menu e footer propri (BIEMME, font Josefin Sans), non quelli del Gruppo: coerente con la landing BF; da confermare se deve uniformarsi |
| Effetto scroll "immagine che si apre" | Assente; c'è solo la timeline a scorrimento delle stazioni, specifica di questa pagina |
| Link/pulsanti | OK (ancore, tel, mailto, LinkedIn); `/privacy-policy` = 404 |
| Form | Presente (7 campi, privacy obbligatoria, Elementor Form): invio reale non provato per non generare richieste |
| Console / mobile | Pulita; nessuno scroll orizzontale a 1440/768/390 |
| Pagina in uso? | NO: non è nel menu e non è linkata. Home e società puntano a https://www.biemmeengineering.it/; "Le società del Gruppo" ha un link a `/biemme-engeenering/` che reindirizza (301) alla pagina. Noindex attivo (staging). Versioni precedenti: solo backup bozza 592 e 527 |
| Titolo | "Biemme Engeenering – ANTEPRIMA nuova homepage" (errore e "anteprima" anche nel `<title>`) |
Slug proposto: `/biemme-engineering/`. Aggiornare: link in "Le società del Gruppo" (oggi `/biemme-engeenering/`), eventuali menu/pulsanti futuri. Redirect 301: `/biemme-engeenering-anteprima-nuova-homepage/` → `/biemme-engineering/` (il vecchio `/biemme-engeenering/` oggi è un redirect automatico di WordPress e ora andrebbe anch'esso al nuovo). Il plugin Redirection non è attivo: serve attivarlo o configurare il redirect dal pannello. Non modificato, decide l'utente.

## 3. Pulizia: NON ESEGUITA (condizioni non soddisfatte)
Non ho eliminato né cestinato nulla: manca il backup completo richiesto come prerequisito. Inventario (sola lettura):
- Pagine bozza (15): backup 623, 621, 613, 592, 590, 543, 527, 568; "Il Gruppo – proposta B" 400; bozze vuote 291, 290, 281, 280, 279, 278 (news). Nel cestino già 17 pagine.
- Libreria Elementor: 143 pubblicati + 4 bozze + 32 nel cestino. Candidati dal nome: pezzi BF 26-10 corrotti 594–611, parti BIEFFE/BIEMME 19/22/23-10 (455–507, 541–548), backup header 616 e 619. NON toccare: pezzi BF 23-10 (549–564, ora in uso nella pagina), loader 430, 507, template 551 (CSS), 612, 39 e 42.
- Archivi plugin di backup: nessuno (plugin non attivi). Media: 80 file, 7 video.
- Revisioni: nessuna da potare (poche per pagina).
Prima di cestinare serve: backup completo dal pannello one.com e verifica che nessun ID sia usato nei dati Elementor.
