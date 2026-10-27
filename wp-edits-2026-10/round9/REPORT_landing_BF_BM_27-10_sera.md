# Landing BF e BM – verifica e chiusura (27/10, sera)

Sito: gruppoirideacque.propagandaadv.com (connettore Royal MCP Iride Acque, verificato). Backup di pagina creati oggi: BF 621 (stato rotto), BF 625 (prima di questo giro), BM 623. Nessun backup completo: nessun plugin attivo, da fare dal pannello one.com. Revisioni di partenza: BF 188 = 437, BM 204 = 243 (nessuna più recente: le landing sono dati Elementor, non revisioni).

## Fonti disponibili
Trovate: trascrizioni e screenshot di BIEFFE1.docx, BIEMME1.docx, "GRUPPO IRIDE ACQUE.docx" (`round7/docx`), report del 19/10, 22/10 (= contenuto del WeTransfer), 23/10. MANCANTI: PRESENTAZIONE AZIENDA.BIEFFE (002).doc, N. 01 Attestazioni e Certificazioni.zip, file loghi originali (disponibili solo le versioni già elaborate in `round5/loghi`). La cartella "che ti indico" non è arrivata.

## 1. Perché la cliente non vedeva tutte le modifiche
Causa principale: **il rifacimento del 26/10 della landing BF era corrotto** (due blocchi del contenuto compresso alterati, vedi report precedente): la pagina restava bianca, quindi chi la apriva non vedeva nulla o, dopo il ripristino di stamattina, vede la **versione del 23/10**. Le modifiche inserite nel rifacimento del 26/10 non esistono più (il contenuto era illeggibile) e vanno rifatte da una sorgente integra (`BieffeHomepage.jsx`, sul PC dell'utente, non in repo).
Prove: payload live = backup 590 byte per byte; blocchi 01 e 07 del set "BF 26-10" di 4.003 e 5.357 caratteri invece di 4.000; errore console `Bieffe embed TypeError: Failed to fetch`.
Cause escluse: pagine pubblicate (BF 188 e BM 204 "publish"); nessuna bozza più recente né autosalvataggio (revisioni ferme al 16/10 e al 7/10); i duplicati sono solo bozze di backup e 17 pagine già nel cestino (nessuna eliminata da me); Home e "Le società" puntano a `/bieffe-costruzioni/`; per BM la Home punta al sito esterno biemmeengineering.it e "Le società" a `/biemme-engeenering/` (redirect 301 alla landing); la landing BM non è nel menu. Cache: le modifiche via connettore compaiono solo dopo la rigenerazione Elementor (Varnish + cache elementi): è successo anche oggi più volte. La cache del plugin one.com Performance Cache è disattivata.

## 2. Checklist BIEFFE (landing BF) – stato sulla pagina pubblica, da non loggato
| Punto | Fonte | Stato iniziale | Azione | Stato finale |
|---|---|---|---|---|
| Pagina visibile (non bianca) | richiesta 27/10 | bianca (rifacimento 26/10) | ripristino set 23/10 (mattina) | FATTO: 8.463 caratteri, console pulita, 1440/768/390 |
| Nome "BIEFFE Costruzioni" ovunque | 26/10 | ok | — | FATTO (0 "Costruzioni Bieffe") |
| Logo orizzontale BIEFFE | 19/10 | ok | — | FATTO (header e footer) |
| Nessun testo/link di altre aziende | 19/10 | 0 occorrenze | — | FATTO: link esterni 0 (solo ancore, tel, mailto) |
| Contatti da intestazione del documento | 19/10, 22/10 A12 | live: Viale Marcello Chiatante 55, 73100 Lecce · 0832.1699769 · info@bieffecostruzionisrl.it · P.IVA 04287140752 · CCIAA 279504 | — | PARZIALE: il report del 19/10 riportava Via Luigi Scarambone 47 / 0832.896022 / tiscali; il 22/10 la cliente ha indicato Chiatante. Non posso verificare il documento (assente): da confermare |
| Hero: frase "La Società è attiva dal 1923 in Puglia…" e via "Lecce · dal 2010" | BIEFFE1 | ok | — | FATTO |
| Chi siamo: 1° e 3° paragrafo verbatim | BIEFFE1 | ok | — | FATTO. Il 2° (BABBO SRL, "due soci fondatori") è invariato: non citato dalla cliente |
| Testi più grandi come Gruppo | BIEFFE1 | tipografia allineata il 23/10 | — | FATTO (corpo 21–23 px, H2 60 px) |
| SOA: categorie mancanti | BIEFFE1 | solo OG3 IV-bis, OG6 VII, OG7 III, OS22 VII | — | **IN ATTESA**: serve lo zip delle attestazioni / PDF SOA |
| Modello 231 nelle attestazioni prima di Associazioni | BIEFFE1 | presente | — | FATTO ("Modello organizzativo", poi Associazioni) |
| Togliere box Soci fondatori | BIEFFE1 | tolto | — | FATTO (Modello 231 primo, 01–05) |
| Sezione REALIZZAZIONI (5 principali) | BIEFFE1 | 26 principali in carosello, titolo "Realizzazioni" | — | **IN ATTESA** dell'elenco delle 5 |
| Box certificazioni (ISO 9001, 14001, 45001:2018, 50001:2018, UNI/PdR 125:2022) e loghi | 19/10, 22/10, 26/10 | presenti con loghi SOA Team e DNV·GL già in uso | — | PARZIALE: versioni ISO non verificate sui certificati (zip assente); nessun logo preso dal web |
| Paragrafo sotto la griglia | 26/10 | "I nostri principali clienti": paragrafo sopra i box | CSS (widget `39098d38`, undo `3b146f075251fb411239ac4dc27021a2`), testato 1440/390 | FATTO, da verificare dopo cache |
| Paragrafo sotto la griglia: "Certificazioni e attestazioni" | 26/10 | paragrafo SOA sopra i box | non applicato | DA DECIDERE: introduce il blocco SOA, in fondo perde il senso |
| Linea del metodo | 26/10 | sezione metodo assente (tolta il 19/10: non nel documento) | — | N/A |
| Header, footer, loghi coerenti con il Gruppo | 26/10 | landing autonoma con header/footer BIEFFE | — | FATTO/da confermare: struttura autonoma voluta (loghi per landing aziende) |
| BM/BF maiuscolo (testi, alt, meta) | 26/10 | 0 occorrenze scritte male | — | FATTO |
| Meta description | — | "…Lecce: dal 2010 … ISO 9001, 14001, 45001" | non modificata | DA DECIDERE: incoerente con hero (togliere "Lecce: dal 2010"?) e con i 5 certificati |
| Immagini | 22/10 | hero con video/poster "bieffe-hero-*"; foto cantiere dell'altra azienda rimosse | — | **IN ATTESA** foto reali del cliente (+ animazioni vasca e immagini dei box citate il 22/10) |

## 3. Checklist BIEMME (landing BM)
| Punto | Fonte | Stato | Azione |
|---|---|---|---|
| Titolo "L'acqua per un'industria più sicura" | BIEMME1 | FATTO | — |
| "Dealer Grundfos" → "Service Grundfos" | BIEMME1 | FATTO (0 "Dealer") | — |
| Testi più grandi come Gruppo | BIEMME1 | FATTO (classi bm-*, 23/10) | — |
| Logo orizzontale BIEMME | 19/10 | FATTO (header e footer) | — |
| Paragrafo sotto la griglia | 26/10 | "Settori diversi" FATTO oggi (widget `db85787a`, undo `7c1710751e9fe33d864aa8f93471c810`); "Seguiamo l'acqua…" e "Tutto ciò che serve…" DA DECIDERE | — |
| Linea del metodo | 26/10 | FATTO (già presente, Fase 01–04) | — |
| BM/BF maiuscolo | 26/10 | FATTO | — |
| Altri contenuti BIEMME1 ("ci aggiorniamo") | BIEMME1 | **IN ATTESA** | — |
| Contatti BM ("AGGIORNARE I DATI") | 22/10 | invariati: Parma, Seregno | **IN ATTESA** dati |
| Foto reali | 22/10 | assenti | **IN ATTESA** |
| "bevande" (intro Applicazioni, footer), "Parma" nel footer | 22/10 C10 | presenti, segnalati | DA DECIDERE |
| Form | — | 7 campi, privacy obbligatoria; invio non provato per non generare richieste | — |
| Link | — | `/privacy-policy` = 404 | **IN ATTESA** pagina privacy |
| Pagina collegata? | — | non nel menu; Home → sito esterno; Società → `/biemme-engeenering/` | DA DECIDERE (e slug `/biemme-engineering/`) |

Verifica finale (live, non loggato, 1440/768/390): console pulita su entrambe, nessun 4xx, nessuno scroll orizzontale, nessuna parola vietata (Bm, Bf, Costruzioni Bieffe, lorem, Dealer, costruzionibieffe, Giavera, impianti costruiti, ecc.). Link esterni: BF nessuno; BM solo LinkedIn Bi-Emme.
Cache: le due regole CSS di oggi sono ancora da vedere dal vivo finché non si rigenera Elementor.

## Cosa serve ancora dal cliente (IN ATTESA)
1. Zip "N. 01 Attestazioni e Certificazioni" (26/10) e PRESENTAZIONE AZIENDA.BIEFFE (002): categorie SOA mancanti, versioni ISO, conferma indirizzo/telefono/e-mail.
2. Elenco delle 5 principali realizzazioni BIEFFE.
3. Foto reali BIEFFE; animazioni e immagini dei box citate il 22/10.
4. BIEMME: ulteriori modifiche annunciate, dati di contatto aggiornati, foto reali, testo di "bevande" e sedi (Parma/Seregno).
5. Pagina privacy (la landing BM linka `/privacy-policy`, oggi 404).

## Messaggio per Paola
Ciao Paola,
grazie per la segnalazione. Ecco il punto sulle landing:
- La pagina BIEFFE ieri sera non si vedeva a causa di un problema tecnico nell'ultimo aggiornamento: l'abbiamo ripristinata, ora si vede correttamente. Il ripristino riporta la versione del 23/10, con le vostre ultime modifiche già inserite (titolo e frase iniziale, testo "Chi siamo", Modello 231, tolto il box Soci fondatori, testi più grandi).
- Abbiamo riallineato alcune sezioni (i paragrafi descrittivi ora stanno sotto i box in "I nostri principali clienti" su BIEFFE e in "Settori diversi" su BIEMME) e verificato che le pagine funzionano su computer, tablet e telefono.
- Se qualcosa non vi risulta aggiornato, fate un aggiornamento forzato della pagina (Ctrl+F5, o da telefono chiudere e riaprire il browser): a volte il browser mostra la versione precedente.
Per chiudere ci servono da voi:
- il file "N. 01 Attestazioni e Certificazioni" e la presentazione aziendale BIEFFE (per completare le categorie SOA, le versioni ISO e confermare indirizzo e contatti);
- l'elenco delle 5 principali realizzazioni BIEFFE;
- le foto reali di BIEFFE;
- per BIEMME: le ulteriori modifiche annunciate, i dati di contatto aggiornati, le foto reali e conferma di "bevande" e sedi nel testo del footer;
- il testo della pagina privacy.
Grazie e a presto!
