<?php
/**
 * Gruppo Iride Acque - Title e meta description SEO (AIOSEO).
 * Imposta title e description per ID di pagina/articolo.
 * Per modificare un testo basta cambiare la riga corrispondente.
 */
function iride_seo_map() {
	return array(
	12 => array('Trattamento acque civili e industriali | Gruppo Iride Acque', 'Un unico partner per il trattamento e la gestione delle acque civili e industriali: analisi, progettazione, costruzione, gestione e ottimizzazione.'),
	55 => array('Il Gruppo: soluzioni integrate | Gruppo Iride Acque', 'Iride Acque, Biemme Engineering e Bieffe Costruzioni: competenze integrate nel trattamento, gestione e riutilizzo delle acque per industria e pubblico.'),
	64 => array('Le società del Gruppo | Gruppo Iride Acque', 'Le società del Gruppo Iride Acque: Iride Acque, Biemme Engineering e Bieffe Costruzioni. Progettazione, costruzione, gestione e service O&M degli impianti.'),
	130 => array('Modello operativo in quattro fasi | Gruppo Iride Acque', 'Dal progetto alla gestione: progettazione, costruzione, gestione e manutenzione, supervisione e ottimizzazione degli impianti acque in un unico processo.'),
	66 => array('Applicazioni e servizi | Gruppo Iride Acque', 'Recupero delle acque di processo, trattamento di reflui complessi con MBR, UF e RO e altre applicazioni: le soluzioni del Gruppo per l\'industria.'),
	289 => array('Impianti trattamento acque reflue | Gruppo Iride Acque', 'Impianti per il trattamento delle acque reflue industriali e civili: depurazione, recupero delle risorse e gestione sostenibile degli scarichi.'),
	288 => array('Acque primarie e di processo | Gruppo Iride Acque', 'Impianti per acque primarie e di processo su misura per industria, civile e tecnologico: dalla consulenza alla costruzione e messa in servizio.'),
	296 => array('Settori: industria, civile, utility | Gruppo Iride Acque', 'Soluzioni per il trattamento delle acque su misura per i settori industriale, civile e multi-utility, nel rispetto dei requisiti normativi.'),
	368 => array('Trattamento acque per l\'industria | Gruppo Iride Acque', 'Trattamento di acque primarie, di processo e reflue nei comparti industriali, con soluzioni su misura per esigenze produttive e ambientali.'),
	574 => array('Trattamento acque per il settore civile | Gruppo Iride Acque', 'Soluzioni per il trattamento di acque primarie e reflue per edifici residenziali, strutture commerciali, complessi turistico-ricettivi e Ho.Re.Ca.'),
	579 => array('Soluzioni per gestori idrici | Gruppo Iride Acque', 'Trattamento di acque primarie e reflue per gestori del servizio idrico ed enti pubblici: potabilizzazione, distribuzione e depurazione affidabili.'),
	295 => array('Consulenza ambientale e permitting | Gruppo Iride Acque', 'Consulenza tecnico-ambientale e supporto nei procedimenti autorizzativi per trattamento, scarico e riutilizzo delle acque, per aziende ed enti pubblici.'),
	294 => array('Noleggio impianti mobili acque | Gruppo Iride Acque', 'Noleggio di impianti mobili e modulari per il trattamento delle acque primarie, di processo e reflue: soluzioni flessibili per esigenze temporanee.'),
	293 => array('Gestione e manutenzione impianti acque | Gruppo Iride Acque', 'Gestione, assistenza tecnica e manutenzione di impianti di trattamento acque primarie, di processo e reflue: prestazioni costanti e continuità operativa.'),
	292 => array('Progettazione impianti acque | Gruppo Iride Acque', 'Progettazione e realizzazione chiavi in mano di impianti per il trattamento delle acque primarie, di processo e reflue, dall\'analisi delle esigenze.'),
	131 => array('News e progetti | Gruppo Iride Acque', 'Le novità del Gruppo Iride Acque: notizie, progetti e riconoscimenti dal mondo del trattamento e della gestione delle acque.'),
	78 => array('Contatti e consulenza tecnica | Gruppo Iride Acque', 'Contatta il Gruppo Iride Acque: un ingegnere di processo prende in carico la richiesta entro 24 ore lavorative e fissa un colloquio tecnico preliminare.'),
	132 => array('Lavora con noi: posizioni aperte | Gruppo Iride Acque', 'Scopri le posizioni aperte nelle società del Gruppo Iride Acque o invia una candidatura spontanea con il tuo CV.'),
	534 => array('Sanificazione centralizzata Campari | Gruppo Iride Acque', 'Sistema centralizzato di dosaggio di biossido di cloro per sanificare le acque di processo dello stabilimento, senza ossidanti residui nel prodotto.'),
	533 => array('Rifacimento rete Acquedotto Pugliese | Gruppo Iride Acque', 'Rifacimento e potenziamento della rete di distribuzione idrica per migliorare l\'affidabilità del servizio, ridurre le perdite e garantire continuità.'),
	532 => array('Potabilizzazione aeroporto di Malpensa | Gruppo Iride Acque', 'Container attrezzato per la potabilizzazione dell\'acqua per i servizi aeroportuali, con due linee indipendenti di biossido di cloro per la disinfezione.'),
	531 => array('Depuratore di Melendugno | Gruppo Iride Acque', 'Impianto per il trattamento dei reflui civili di Melendugno e comuni limitrofi, con trattamento terziario e recapito finale tramite fitodepurazione.'),
	530 => array('ENI Sarroch: trattamento acque reflue | Gruppo Iride Acque', 'Impianto per le acque di lavaggio delle bombole di gas con reattore EMER, filtrazione a sabbia e carbone attivo e riutilizzo dell\'acqua di processo.'),
	529 => array('Tintoria Emiliana: recupero sali | Gruppo Iride Acque', 'Recupero dei sali di tintura con ultrafiltrazione ceramica e nanofiltrazione, concentrati trattati con tecnologia EMER e upgrade con osmosi inversa.'),
	);
}

add_filter( 'aioseo_title', function ( $title ) {
	if ( is_singular() ) {
		$map = iride_seo_map();
		$id  = get_queried_object_id();
		if ( isset( $map[ $id ] ) ) {
			return $map[ $id ][0];
		}
	}
	return $title;
}, 99 );

add_filter( 'aioseo_description', function ( $description ) {
	if ( is_singular() ) {
		$map = iride_seo_map();
		$id  = get_queried_object_id();
		if ( isset( $map[ $id ] ) ) {
			return $map[ $id ][1];
		}
	}
	return $description;
}, 99 );
