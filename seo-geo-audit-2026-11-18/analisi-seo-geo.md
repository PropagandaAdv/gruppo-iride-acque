# Gruppo Iride Acque — Analisi SEO/GEO (18/11/2026)

Fonti: Ubersuggest (progetto `gruppoirideacque.com`, dati del 18/11/2026) e controlli diretti sulle 27 URL della sitemap (fetch del sito, non Ubersuggest).
Limiti: il crawl completo di Ubersuggest era ancora in corso al momento della stesura (29 pagine lette su ~230); non è disponibile Search Console; dominio recente → dati di traffico/keyword a zero.

## 1. GEO — visibilità nelle risposte AI (54 risposte, 20 prompt, 3 motori)

| Metrica | Valore |
|---|---|
| Visibilità brand | 5,56% (3 menzioni su 54) |
| Posizione media se citato | 2,67 |
| Share of voice | 1,16% |
| Gemini / Google AI Overviews / ChatGPT | 5,26% / 13,33% / 0% |
| Citation share del sito Iride (come fonte) | 0% (0 su 54) |
| Citation share di Sostelia (competitor) | 18,52% |
| Sostelia: visibilità | 12,96% (7 menzioni) |

Classifica brand: IDRO Group 25,93% · Veolia Water Technologies Italia 20,37% · Sostelia 12,96% · Depureco 12,96% · Gazebo 11,11% · … · Gruppo Iride Acque 5,56%.

- Le 3 menzioni del brand arrivano da pagine di terzi (veoliawatertechnologies.it, idro.net, ecosistemi.net): nessuna risposta cita una pagina del sito Iride.
- "Iride Acque" compare come brand separato (3 menzioni, pos. 1,67): le AI usano due nomi per lo stesso soggetto.
- Gap di citazione: 5 prompt su 20 in cui è citato Sostelia e non Iride — 4 sul tema ZLD (scarico zero) e 1 su "gestione e manutenzione come partner unico".
- Pagine di terzi che nominano Sostelia ma non Iride (da cui chiedere inserimento): cidgroup.it (3 pagine), stacque.com (3 pagine, DR 23), simpec.it (1 pagina, DR 19).
- Fonti più citate dalle AI nel settore: pagine tecniche di produttori (Veolia, IDRO, Eco-Techno, Sostelia, SAITA, Alfa Laval, Gazebo) e categorie Trustpilot.

## 2. SEO — dati Ubersuggest

- Dominio: DA 1, 16 backlink da 16 domini, tutti nofollow; 0 keyword organiche, 0 traffico negli ultimi 12 mesi (probabile effetto della migrazione/sito recente: da ricontrollare con Search Console).
- Opportunità keyword (stime Ubersuggest, Italia): "gestione impianti" 210/mese (CPC ~8,9 $) · "autorizzazione scarico acque reflue" 170 · "impianto potabilizzazione acqua" 110 · "trattamento acque reflue urbane" 40 · "progettazione impianti trattamento acque" 30. Volumi piccoli: nicchia B2B, il valore sta nei contatti, non nel traffico. "lavora con noi" (33.100) è generica e non porta clienti; "servizio idrico integrato" (1.600) è da valutare perché riguarda i gestori, target multi-utility.
- Velocità (PageSpeed, laboratorio): desktop LCP 0,9 s, CLS 0,069, TBT 334 ms. Mobile LCP 3,5 s (oltre la soglia di 2,5 s), FCP 2,3 s, Speed Index 10,2 s, TTI 12 s, TBT 351 ms. Opportunità: ~600 KB di JavaScript non usato, 112 KB di CSS non usato, redirect (−601 ms su mobile). Da verificare se i nuovi video hero incidono sul mobile.

## 3. SEO — controlli diretti sulle 27 URL in sitemap

Bene: tutte rispondono 200, canonical corretto, Open Graph, `lang="it-IT"`, JSON-LD su tutte, robots.txt e sitemap (All in One SEO) a posto.

Problemi:
1. **Title generici**: "Home - Gruppo Iride Acque", "Civile - …", "Industriale - …", "Gestione impianti - …". Nessuna parola chiave né beneficio.
2. **Meta description generate in automatico dal testo**: molte superano 400 caratteri (Google ne mostra ~155), uniscono i titoli senza spazio ("ApplicazioniTrattamento acque…") e alcune sono troncate a metà parola (Rifacimento rete Acquedotto Pugliese, Malpensa, Melendugno, Modello operativo, Contatti: 49–152 caratteri).
3. **Testo segnaposto pubblico**: la description di "Le società del gruppo" contiene "Logo in attesa dal cliente".
4. **Pagine di servizio non pronte, indicizzabili e in sitemap**: "Biemme Engeenering – ANTEPRIMA nuova homepage" (refuso nel titolo, 40 parole, nessuna description) e "BIEFFE Costruzioni" (6 parole, nessuna description).
5. **Articolo di prova "Ciao mondo!"** (2026/09/07) pubblicato e in sitemap.
6. **H1**: "Gestione impianti" ha come H1 lo slogan e non il nome del servizio; "Civile" e "Multi-utility" hanno 2 H1.
7. **Nessuna FAQ** e nessun dato strutturato FAQ/Service su alcuna pagina.
8. **Immagini senza alt** (1–4 per pagina).
9. `/llms.txt` assente (404). Non è un fattore di ranking: priorità bassa.

## 4. Priorità consigliate

**Alta**
1. Pagina dedicata a ZLD / scarico zero (oggi il tema è solo citato dentro altre pagine) con FAQ e "preventivo/richiesta tecnica".
2. Riscrivere title e meta description a mano (almeno le 12 pagine principali): 50–60 / 140–155 caratteri, con servizio + settore + beneficio.
3. Pulizia indicizzazione: rimuovere/mettere noindex su "Ciao mondo!", Biemme anteprima e Bieffe finché non sono complete; togliere "Logo in attesa dal cliente".
4. Pagina Gestione impianti: esplicitare l'offerta da partner unico (progettazione → gestione) — è il secondo gap di citazione.

**Media**
5. FAQ con risposte dirette su costo, scelta tecnologia, come scegliere il fornitore + dati strutturati FAQ/Service.
6. Correggere H1 (Gestione impianti, Civile, Multi-utility) e aggiungere alt alle immagini.
7. Unificare il nome in tutte le pagine e nei profili esterni ("Gruppo Iride Acque" vs "Iride Acque").
8. Mobile: ridurre JS/CSS inutilizzati, eliminare il redirect, verificare l'effetto dei video hero.
9. Fonti esterne: richiedere inserimento su elenchi/associazioni di settore e sulle pagine che nominano solo Sostelia.

**Verifica**
10. Ricontrollare GEO tra 3–4 settimane (tracking settimanale) e Search Console per confermare i dati a zero.
11. Riformulare i 5 prompt poco utili del tracking.
