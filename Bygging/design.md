\# Designvalg og begrunnelser



\## Overordnet topologi

Vi har valgt en enkel kondensatorbank (én stor kondensator) med et selvutløsende gnistgap (relaksasjonsoscillator). Dette gir:

\- \*\*Enkelhet:\*\* Færre komponenter – ingen separat triggerkrets.

\- \*\*Automatisk repetisjon:\*\* Når ladeknappen holdes inne, lades kondensatoren til \~450 V, gnistgapet slår gjennom, og pulsen fyres. Syklusen gjentar seg automatisk.

\- \*\*Høy strøm:\*\* En enkelt 100 µF kondensator gir \~3000 A ved moderat spenning, noe som er ideelt for magnetfeltgenerering.

\- \*\*Håndholdbarhet:\*\* Komponentene er kompakte og lette.



\## Valg av ladekrets

En selvoscillerende flyback-omformer er valgt fordi den:

\- Er enkel og krever ingen mikrokontroller.

\- Kan lade kondensatoren fra et lavspent batteri (45 V) til 450 V.

\- Bruker få komponenter (MOSFET, transformator, diode, zener, motstander, snubber).



\## Gnistgap – selvutløsende

I stedet for et trigget gnistgap bruker vi et enkelt gnistgap med fast avstand (\~0,5 mm). Når spenningen over kondensatoren når gjennomslagsspenningen for gapet (ca. 450 V for 0,5 mm i tørr luft), ioniseres luften og en gnist dannes spontant. Dette kobler kondensatoren til spolen og utløser pulsen. Etter utladning faller spenningen til null, gnisten slukker, og ladingen starter på nytt. Dette gir en selvregulerende oscillator uten ekstra elektronikk.



\## Spoledesign

En flat spiralspole (pancake coil) med 4 vindinger er valgt fordi den:

\- Gir et konsentrert magnetfelt foran spolen.

\- Har lav induktans (\~2,5 µH), noe som gir høy di/dt og dermed høy indusert spenning.

\- Er enkel å lage med 3D-printet form.



\## Komponentvalg

\- \*\*Kondensator:\*\* 100 µF, 450 V, fotoflash-type. Disse er spesielt designet for høye pulsstrømmer og har lav ESR.

\- \*\*MOSFET:\*\* IRFP450 (500 V, 14 A) er en robust MOSFET med lav Rds(on) og høy strømtåleevne.

\- \*\*Diode:\*\* UF4007 er en rask diode med 1000 V sperrespenning.

\- \*\*Gnistgap:\*\* Wolframelektroder fra TIG-sveising er ideelle på grunn av høy smeltetemperatur og god erosjonsmotstand.

\- \*\*Spole:\*\* 10 AWG emaljert kobbertråd gir lav motstand og høy strømtåleevne.



\## Beskyttelseskretser

\- \*\*Gatebeskyttelse:\*\* En 15 V zenerdiode (D2) og en 1N4148 (D4) i serie klemmer gate-spenningen til maksimalt \~15,7 V og hindrer negativ spenning.

\- \*\*Snubber over primærvikling:\*\* En RCD-snubber (D5, R2, C2) demper spenningstransienter når MOSFET-en slår seg av, og beskytter den mot overspenning fra lekkinduktans.



\## Sikkerhet

\- \*\*Manuell utladning:\*\* En trykknapp med 1 kΩ / 10 W motstand lar brukeren lade ut kondensatoren trygt på \~1 sekund.

\- \*\*LED-indikator:\*\* En grønn LED med 220 kΩ / 1 W motstand lyser når spenningen overstiger ca. 200 V.

\- \*\*Sikring:\*\* En 2 A sikring i batterikretsen beskytter mot kortslutning.



