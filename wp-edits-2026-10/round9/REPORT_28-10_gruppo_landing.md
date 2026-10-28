# Modifiche del 27/10 (call con Paola) – gruppo e landing BM/BF (report del 28/10)

Sito: gruppoirideacque.propagandaadv.com (connettore Royal MCP Iride Acque, verificato). Nessuna pubblicazione sul dominio definitivo, nessun cambio di noindex/DNS. Nessun backup completo (nessun plugin attivo): copie di pagina/template: Header #39 → 627, BF → 625, BM → 623; revisioni di partenza: Header #39 = 245, Applicazioni e Servizi (66) = 310, BF 188 = 437, BM 204 = 243.

## Materiale ricevuto / mancante
Ricevute: solo le 5 foto (in versione ridotta: 2000×1500 / 1125×1500 / 1500×2000). MANCANO: i due PDF (Condizioni di Vendita, Garanzia e Assistenza), immagine statica della vasca, testo antilegionella, impianti-depurazione_vista-aerea.jpg, i 7 loghi clienti. La cartella indicata non è arrivata.

| Punto | Prima | Dopo | Stato |
|---|---|---|---|
| A1 footer: PDF | nel footer "Codici Etico / Condizioni Generali di Acquisto e Vendita – documento in arrivo" | non toccato | IN ATTESA (PDF assenti) |
| A2 hero uniforme | Il Gruppo titolo 46 px, Applicazioni e Servizi alto 423 px, altre pagine 78/53 px, altezze diverse | desktop: altezza 100svh, titolo 91 px (come Home) su 13 pagine con hero; tablet 48 px, mobile 45 px; stessa posizione di partenza (150 px). Widget `451ccbf5` in Header #39 (undo `03f48d74c2ef337e0853d7b8881036c4`) | FATTO, verificato live desktop |
| A3 Applicazioni e Servizi (66) | paragrafo lungo tra titolo e card ("Applicazioni", "Servizi") | paragrafo sotto le card, prima della CTA; widget `ff816feb` (undo `5e8cea3a85245094a3c04511eb00bf7d`). Le altre pagine servizi/settori erano già a posto (27/10) | FATTO |
| A3 immagini da Chiara | — | non arrivate | IN ATTESA |
| A4 numero fisso Iride | nessun numero fisso di Iride sul sito del gruppo (Contatti: solo indirizzo Arosio) | — | N/A |
| B1 BM contatti | sede legale Parma, operativa Seregno, tel. 0362 244145, fax 0362 240467 | sede operativa "Via Michelangelo Buonarroti, 3, 22060 Arosio (CO)" (copiata dal sito); sede legale "Milano" (indirizzo completo non presente sul sito); tel. e fax rimossi da contatti e footer; email invariate | PARZIALE: manca l'indirizzo completo della sede legale di Milano |
| B2 BM antilegionella | assente | box "Antilegionella" con solo titolo, nascosto su tutti i dispositivi (nei dati della pagina). Per attivarlo servono testo e rimozione di `className:"hidden"` | IN ATTESA del testo |
| B3 titolo BM | — | non toccato | OK |
| C1 BF hero | immagine/video generato dell'edificio | edificio rimosso (poster sostituito con pixel trasparente, video non scaricato): hero scuro, titolo leggibile | FATTO (da vedere dopo la cache); vasca IN ATTESA |
| C2 BF "Principali realizzazioni" | sezione "I nostri principali clienti" con 7 box di testo, nessuno scorrimento | non modificata: mancano i loghi, e il titolo "Principali realizzazioni" duplicherebbe quello della sezione "Realizzazioni" | IN ATTESA (loghi) + da decidere |
| C3 BF foto "Ingegneria civile" | 4 card con icona, senza foto (il rifacimento del 26/10 con foto è andato perso) | ritagli 4:3 WebP pronti (miniature prima/dopo in `screens_28-10/C3_ritagli_prima_dopo.png`), NON inseriti: nessuno slot immagine e caricamento in Libreria da concordare | PARZIALE/IN ATTESA |
| C4 BF indirizzo | — | non toccato | OK |
| D1 "Torna al Gruppo Iride Acque" | assente | link a `/` accanto al logo: testo esteso su desktop largo e tablet verticale, "← Gruppo" su 768–1279 e mobile. BF widget `c98bbad0`, BM widget `6bdac2a6` | FATTO (verificato con prova locale; live dopo cache) |
| D2 header più grande | BM barra 80/96 px, logo 144–176; BF barra 64/72, logo 40–52 | BM 88–108 px, logo 168–184 px, menu 17 px; BF 76/88 px, logo 48–62 px, menu 18 px; nessun overflow tra 1024 e 1440 | FATTO (live dopo cache) |

## C3 – ritagli e scelte
| Card | Foto usata | Scartata | Ritaglio |
|---|---|---|---|
| Opere marittime | opere-marittime_sub (1600×1200) | — | stretto su sommozzatore, mani e flangia, meno acqua in alto |
| Opere stradali | asfalto-piazzale-rullo (1600×1200) | asfalto-strada | rullo e asfalto nuovo, tolta parte del primo piano |
| Acquedotti e fognature | scavo-tubo-arancione (1350×1012) | scavo-tubi-gialli | tubo centrato, ridotto il cumulo a destra |
| Impianti di depurazione | vista aerea mancante | — | IN ATTESA |
Alternative già ritagliate: asfalto-strada (cruscotto e ghiaia tolti), tubi gialli (camion escluso). Lavorato su versioni ridotte inviate in chat, non sugli originali: nessun ritocco generativo, solo contrasto lieve uniforme.

## Tecnica (landing)
Le landing sono app compilate e compresse. Le correzioni sono un piccolo script (prima dei dati) che sostituisce frammenti di testo prima dell'esecuzione, più un CSS: si annullano con i token undo. Il sito riscrive gli indirizzi dentro gli script (`usercontent.one`): le regole non devono contenere URL.

## Da confermare / chiedere al cliente
- Indirizzo completo sede legale Milano; testo antilegionella; i due PDF; foto vasca; vista aerea depuratori; 7 loghi e i nomi dei 3 stemmi (alt "Stemma ente cliente"); foto di Chiara per le pagine servizi.
