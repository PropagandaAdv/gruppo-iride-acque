# Numeri del Gruppo – modifica del 27/10/2026 (richiesta Paola Mezzacapo, mail del 26/10)

Sito verificato: gruppoirideacque.propagandaadv.com (connettore Royal MCP Iride Acque).
Revisione Home prima della modifica: **570** (backup precedente: 568).

## Fase 1 – Individuazione
- "impianti costruiti" (qualsiasi maiuscola): **una sola occorrenza**, Home (12), sezione "Numeri", widget `c9d3c8e9`. Nessuna in altre pagine, header (39), footer (42), né nei meta SEO (Yoast non è attivo).
- La sezione numeri esiste **solo nella Home**. Non è presente in Il Gruppo né in Le società del Gruppo.
- I contatori sono widget HTML personalizzati (non il widget Contatore di Elementor).

## Fase 2 – Modifiche (Home, sezione Numeri)
| Elemento | Prima | Dopo |
|---|---|---|
| Etichetta 1 (`c9d3c8e9`) | Impianti costruiti | Realizzazioni |
| Contatore 1 | 120 | Oltre 200 |
| Etichetta 2 (`f17ef620`) | Risorse umane | Risorse Umane |
| Contatore 2 | 85 | 40 |
| Etichetta 3 (`491edb65`) | Ricavi | Ricavi (invariata) |
| Contatore 3 | 12 | 12 milioni |

Come: le etichette sono cambiate sul posto. I vecchi contatori (`c93f0c82`, `d37ad2e1`, `49fa8970`) non sono modificabili dal connettore, quindi sono nascosti via CSS e affiancati da tre nuovi widget HTML con prefisso/suffisso (`6dcab102` Oltre 200, `74917923` 40, `86f943ea` 12 milioni). Animazione identica (1,6 s, parte a vista).
Il valore numerico "120/85/12" resta nel markup dei vecchi widget nascosti (non visibile).

Undo (72 h): etichette `5cfbe05d681e1c5e60f4993c611129e8`, `5e06b2f95bb93aef71ce0a74831fb585`; widget `11ba66f1be301f7e654ed9fc80a4c51d`, `763248092487684b6da67704527142ab`, `42b05aa3625efca29d4c47c03baa596e`.

## Verifica (browser, live)
Desktop 1440 e mobile 390: testo finale "Oltre 200 / 40 / 12 milioni", etichette corrette, nessun errore in console, zero occorrenze di "impianti costruiti".
Tablet 768–820: "12 milioni" usciva dalla scheda. Corretto con una regola solo per 768–1024 px (font 44 px sui tre numeri), nel widget `86f943ea`. **Da riverificare dopo la rigenerazione della cache** (il live serviva ancora l'HTML precedente).
Screenshot: `screens/numeri_dopo_{desktop,tablet,mobile}.png` (il tablet mostra il difetto prima della correzione). Lo "prima" è lo screenshot nella mail del cliente.

## Da confermare col cliente
Nessun altro numero presente nella sezione: nulla da togliere.
