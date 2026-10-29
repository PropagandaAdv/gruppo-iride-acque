# Backup per-pagina — hero Servizi (sito definitivo www.gruppoirideacque.com), 2026-10-28

Backup completo non eseguibile (SiteVault, UpdraftPlus e Duplicator non attivi via connettore).
Concordato: salvataggio per pagina. Qui lo stato ORIGINALE dei widget modificati (hero, widget HTML
`iah2-hero`). Ripristino: incollare l'HTML nel widget indicato, oppure `mcp_undo_last_operation`
con il token (72h) riportato nel report.

Elementi toccati: widget hero (pagina → id widget) e, per ogni pagina, nuovo container introduttivo
inserito subito dopo il container dell'hero.
- 292 Progettazione → 4ccad9c1 (container hero 3e4f2321)
- 293 Gestione → 35c5e6f8 (container hero 667d41ef)
- 294 Noleggio → 24930a61 (container hero 0fe34339)
- 295 Consulenza → e9467547 (container hero 1f27329f)

Originale: in ogni hero il blocco `<div class="sub">…</div>` contiene i paragrafi poi spostati sotto
l'hero. Kicker e h1 invariati (kicker = nome del servizio; h1 = titolo concordato).
Gli hero originali sono recuperabili anche da `_elementor_data` (meta) via undo.

## Token di undo (72h, scadenza 2026-10-31) — da annullare in ordine inverso
- 294: meta `aea64355ee3c58493720619dabd1063d`, poi widget video `19a58f2297d9ad9f71538a9dcbc23b61`
- 293: meta `07232e9163bd1ed3a35a58a712253a96`, widget video `e3765e98cd23bb1052a7b624c9439df0`, widget style `e3cbda6a53e3784a8e422f3a82d2ec1a`
- 295: meta `0f8ddd9902ad5e708ba45f63d49b0504`, widget video `b41860a1fafc0fa51e938ef2f335a48e`, widget style `89d0b8d2323cd84065f1cf09ec053876`
- 292: meta `594106d4b3c05f50cd4fed937f026b5b`, widget video `57dec72d30588cc87d58cc438cd15f38`, widget style `6fcd97eb5cf396fbb3eb379bf31c5795`

Nota tecnica: `wp_update_post_meta` toglie `<script>`/`<style>` dai widget HTML; dopo ogni scrittura i widget
di video e stile sono stati reinseriti con `elementor_add_widget` (che li conserva). Non riscrivere
`_elementor_data` con quello strumento senza rifare lo stesso passaggio.

## Parte 2 — foto (2026-10-29)
Pagine toccate: 368 Industriale, 574 Civile, 579 Multi-utility (righe sotto-settori), 289 Reflue e 288 Primarie (box tecnologie).
Undo (72h, ordine inverso): 368 meta `e6cb22afd60c59655b87ebf3afe208c4`; 574 meta `ea287058583835f77a72d7536a558252`;
579 meta `ac14847d98cdfa12fb2945113ecc1eaa`; 289 meta `f6aa7aec3fc8c18099d6232fc223bb8a`; 288 meta `2bb828c9d56b16c6494096e79f1761a7`.
Media: 44 WebP caricati (ID 673-716) da PNG ID 629-672 (PNG originali del cliente lasciati in libreria).
Nota: Elementor tiene una cache del render (`_elementor_element_cache`) non cancellabile dal connettore; dopo ogni scrittura può servire la versione vecchia fino alla scadenza.
