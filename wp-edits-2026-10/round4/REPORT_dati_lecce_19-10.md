# Landing BIEFFE Costruzioni – aggiornamento dati (presentazione ufficiale di Lecce), 19/10/2026

Pagina: https://gruppoirideacque.propagandaadv.com/bieffe-costruzioni/ (pagina WP 188)

## Backup
- Nessun plugin di backup attivo. **Backup = pagina clonata in bozza, ID 440** ("BACKUP 19-10 BIEFFE landing (prima dati Lecce)"), con il contenuto della landing prima di questo giro.
- Sorgenti locali precedenti: `costruzioni-bieffe/site/src/BieffeHomepage.jsx.bak-19-10`, `wp-embed/media-map.json.bak-19-10`.

## Come è stato fatto
La landing è un'applicazione React incorporata (non Elementor nativo). Ho cambiato solo i contenuti nel sorgente (layout, stile, palette, font e logo invariati), ricompilato e reinserito in 12 widget HTML (template 444–455 + loader 430). Controllo byte per byte del payload live contro il build: **tutte le 12 parti identiche** (sha256 `1d2bfccf…`). Nuovi file in Libreria: logo SOA Team (ID 442) e logo DNV·GL ISO 9001 (ID 443), estratti dal .doc e verificati per hash.

## Sezione per sezione
**Contatti + footer** – Ragione sociale BIEFFE Costruzioni s.r.l.; Via Luigi Scarambone, 47 – 73100 Lecce (LE); Tel./Fax 0832.896022 (`tel:+390832896022`); e-mail `bieffecostruzionisrl@tiscali.it` e PEC `bieffecostruzionisrl@pec.it` (link `mailto:`); Cod. Fisc. e P. IVA 04287140752; C.C.I.A.A. n. 279504. Nessuna mappa presente (nessuna aggiunta). Footer: stessi dati + link interni alle sezioni (tolti i link al sito dell'altra azienda e "Privacy e cookie").

**Hero** – "BIEFFE Costruzioni", etichetta "Lecce · dal 2010", sottotitolo = prima frase del documento. Le didascalie dell'animazione a scorrimento ora usano solo frasi del documento ("Opere pubbliche e settore privato.", "Tutti conclusi nei tempi assegnati." + elenco delle 5 aree). Sullo schermo piccolo non c'è più la foto di cantiere dell'altra azienda: viene usato il fotogramma generato (non attribuibile). Bottoni: "Contatti" / "Realizzazioni".

**Attività** (titolo "Ingegneria Civile") – 5 card solo titolo, senza descrizioni: Acquedotti e fognature · Impianti di depurazione · Opere stradali · Opere marittime · Ingegneria naturalistica (card scure con icona, senza foto).

**Azienda / Chi siamo** – i tre paragrafi del documento, testo fedele (solo "SRL" scritto "srl"). I due paragrafi sulla gestione di attività ricettive nel settore turistico **non sono stati inseriti** (come da indicazione).

**Numeri** – solo dati del documento: 2010 (anno di costituzione), 4 (categorie SOA), 3 (certificazioni ISO).

**Certificazioni e attestazioni** – intro verbatim; 4 box SOA (OG3 III bis Strade, OG6 VI Acquedotti e fognature, OG7 III Opere marittime, OS22 VI Depuratori) con logo SOA Team; 3 box ISO 9001/14001/45001:2015, logo DNV·GL accanto a ISO 9001; testo "Rilasciati da un Ente terzo…"; box "Iscrizione a Confindustria / ANCE Puglia" (nessun logo creato).

**Struttura organizzativa** – 5 box (Soci fondatori, Organizzazione interna, Maestranze, Parco macchine, Rete di consulenti) con testo verbatim.

**Clienti** – 9 nomi in box di solo testo (nessun logo).

**Realizzazioni** – "Realizzazioni in corso" (10 card, con etichette "progettazione esecutiva ed esecuzione" / "in fase di conclusione" / importo a base d'asta dove indicato) e "Principali realizzazioni dell'ultimo ventennio" (26 card compatte, 9 visibili + pulsante "Mostra tutte"). Riferimenti burocratici (CIG, CUP, gare, articoli di legge) esclusi come da indicazione. Foto rimosse.

**SEO** – titolo `BIEFFE Costruzioni | Gruppo Iride Acque` e meta description come da brief, impostati dalla pagina via script. Limite: sul sito non c'è plugin SEO, quindi nell'HTML statico il `<title>` resta "BIEFFE Costruzioni – Gruppo Iride Acque" (formato WordPress) e la meta description non è nel sorgente statico (i motori che eseguono JavaScript la leggono; per averla statica serve un plugin SEO).

## Eliminato (dati dell'altra azienda)
Tutti i testi, numeri (23 lavori, "2 soci"…), slogan, claim, citazione, clienti e progetti (Hausbrandt, Superbeton, Ecma, Latteria Montello, Parco Cavallino, ecc.), foto di cantieri e della sede, indirizzo di Giavera del Montello, tel. 0422 775223, P.IVA 04184870261, e-mail info@costruzionibieffe.it, link a costruzionibieffe.it (footer, schede lavori, privacy), logo e box CQOP SOA.

## Sezioni nascoste / rimosse perché senza contenuto nel documento
- **"Tre punti fermi"** (Mezzi / Regia / Presenza): testi inventati, sezione tolta.
- **"Metodo" in 4 passaggi** (Sopralluogo, Progetto, Cantiere, Manutenzione): non nel documento, sezione tolta (sostituita da "Struttura organizzativa").
- **Citazione dei soci** e foto della sede nella sezione Azienda: tolte.
- Filtri per settore e foto nelle realizzazioni: tolti (card solo testo).

## Contenuti esclusi di proposito
- Paragrafi sulla gestione di attività ricettive nel settore turistico.
- Lista "Partnership e subappaltatori".

## Modulo di contatto
Non c'è un servizio di invio: il modulo apre il programma di posta dell'utente con un messaggio precompilato (mailto). **Prima** il destinatario era `info@costruzionibieffe.it` (dell'altra azienda). Non potendo lasciare quell'indirizzo, ora il destinatario è `bieffecostruzionisrl@tiscali.it`: da confermare col cliente. Il testo del consenso privacy ora non ha il link all'informativa (quella linkata era del sito dell'altra azienda): per la nuova serve una pagina privacy di BIEFFE Costruzioni.

## Verifiche
- Ricerca nel render finale di: costruzionibieffe, 0422, 04184870261, Giavera, Treviso, Via Costa, info@, Superbeton/Hausbrandt/Latteria/Cantina Montelliana, CQOP, 2007, sopralluogo, `/assets/`: **0 risultati**. Link presenti: solo ancore interne, `tel:+390832896022`, `mailto:` e PEC.
- Immagini caricate (logo, hero, SOA Team, DNV·GL) senza errori; nessun errore console, nessuna richiesta fallita; nessuno scroll orizzontale a 1440, 820 e 390 px; animazione dell'hero a scorrimento verificata (video a 5,04 s a metà e 9,88 s a fine corsa).
- Svuotata la cache Elementor della pagina; richieste con query string.

## Da fare / da segnalare
- **File dell'altra azienda ancora nella Libreria Media** (non più usati dalla pagina, ma raggiungibili via URL): ID 206, 210–237 (foto dei lavori, hero reali, sede, servizi, logo vecchio e CQOP). Non cancellati; dimmi se eliminarli.
- Footer del sito e card Bieffe in Home/Le società: invariati rispetto al giro precedente.
- La scheda cliente interna riporta "Non citare SOA e ISO 9001: validità non confermata": riguardava i dati dell'altra azienda; ora SOA e ISO sono quelli forniti dal cliente nella presentazione ufficiale, quindi la regola è da aggiornare.
- Titolo/descrizione SEO statici: richiedono un plugin SEO (vedi sopra).
