# Logo header più grande (richiesta cliente 26/10, riferimento Sostelia)

Stato: modifiche salvate nel template header #39. Il sito live serve ancora l'HTML in cache di Elementor:
serve "Elementor › Strumenti › Rigenera CSS e dati" (+ svuotare cache), poi verifica live.

## Misure (browser headless, getBoundingClientRect)
| Breakpoint | Logo Sostelia L×H | Nostro prima L×H | Nostro dopo L×H | Altezza header prima → dopo |
|---|---|---|---|---|
| 1440 | 195 × 42,9 | 104 × 60 | 196 × 113,4 | 108 → 129,4 (Sostelia 101,6) |
| 1366 | 195 × 42,9 | 104 × 60 | 196 × 113,4 | 108 → 129,4 (Sostelia 92,9) |
| 1024 (tablet) | 195 × 42,9 | 92 × 53 | 196 × 113,4 | 105 → 129,4 |
| 390 | 195 × 42,9 (*) | 78 × 45 | 196 × 113,4 | 89 → 129,4 |
| Sticky (dopo scroll) | — | invariato (cambia solo lo sfondo) | 172 × 99,5 (88%) | → 115,5 |

(*) a 390 il header mobile di Sostelia si apre con menu a schermo intero in headless; misura = stessa SVG 195 × 42,9.

## Cosa è stato fatto
- Backup header: elementor_library 616 (bozza). Undo token dei widget aggiunti validi 72h.
- Nuovo file logo 420 px (media 618, `logo-gruppo-iride-acque-lettering-420.webp`, 7 KB, da lettering 1474 px; 2,1× a 196 px). Il vecchio media 509 (320 px) resta in libreria.
- Header #39: nuovo widget immagine (id 9d27522a, size full) + vecchio widget 36f1e375 nascosto; widget CSS 94395295 (larghezza 196, sticky 172, padding header 8, spazio hero Home ≥900px 150px, hero interne mobile `.iah2-hero .bh-copy` 92px).
- Landing BIEFFE/BIEMME: non toccate (non usano questo header).
- Il bottone "Richiedi una valutazione tecnica" è già nascosto sotto i 1700px dalla regola esistente `.iah-cta` (non modificata).
