\# Designvalg og begrunnelser



\## Overordnet topologi



Vi har valgt en kondensatorbank (én stor kondensator) med et trigget gnistgap. Dette gir:



\- \*\*Kontrollert utløsning:\*\* En piezoelektrisk tenner ioniserer gapet uavhengig av spenningen, slik at vi kan fyre når vi vil.



\- \*\*Høy strøm:\*\* En 100 µF kondensator gir \~2600 A ved 450 V, noe som gir et kraftig magnetfelt.



\- \*\*Repeterbarhet:\*\* Ladekretsen lader kondensatoren på noen sekunder; skuddtakten bestemmes av ladetiden.



\- \*\*Håndholdbarhet:\*\* Komponentene er kompakte og lette.



\## Valg av ladekrets



En selvoscillerende flyback-omformer (blocking-oscillator) er valgt fordi den:



\- Er enkel og krever ingen mikrokontroller.

\- Kan lade kondensatoren fra et lavspent batteri (45 V) til 450 V.

\- Bruker få komponenter (MOSFET, transformator, diode, zener, motstander, kondensator og snubber).



Utgangen er ikke lukket-sløyfe-regulert, og kretsen har ingen automatisk avkobling ved 450 V. 450 V er derfor en øvre operativ grense som må overvåkes under testing. S1 må slippes manuelt ved eller før denne spenningen.



\### Transformatorpolaritet



T1 har tre viklinger med definert polaritet:



\- Primær P: prikkmerket terminal til +45 V.

\- Feedback FB: prikkmerket terminal mot C3/gate.

\- Sekundær S: prikkmerket terminal mot C1-/GND.



Feedback- og sekundærviklingen er dermed koblet med motsatt polaritet relativt til primærviklingen. Dette gir positiv gate-feedback under Q1 turn-on og sørger for at sekundærlikeretteren er sperret under ON-perioden og leder ved flyback-turn-off.



\## Gnistgap – trigget



Et trigget gnistgap med piezotennmekanisme er valgt fordi:



\- Det gir full kontroll over avfyringstidspunktet.

\- Piezotennere genererer >10 kV uten ekstern strømforsyning.

\- Gapet kan ha en avstand på \~0,5 mm, som er praktisk å lage, og likevel trigges pålitelig selv om spenningen er lavere enn den naturlige gjennomslagsspenningen.



\## Spoledesign



En flat spiralspole (pancake coil) med 4 vindinger er valgt fordi den:



\- Gir et konsentrert magnetfelt foran spolen.

\- Har lav induktans (\~0,83 µH), noe som gir høy di/dt og dermed høy indusert spenning.

\- Er enkel å lage med 3D-printet form. Spesifikasjon: senterdiametre 20 mm (innerste) og 100 mm (ytterste), 10 AWG tråd.



\## Komponentvalg



\- \*\*Kondensator:\*\* 100 µF, 500 V. Må ha lav ESR og tåle høye pulsstrømmer. Fotoflash-type anbefales, men egnethet må verifiseres.



\- \*\*MOSFET:\*\* IRFP450 (500 V, 14 A) er en robust MOSFET. Drain-transient må måles for å bekrefte margin.



\- \*\*Diode D1:\*\* To UF4007 i serie for å oppnå nødvendig sperrespenning (>1350 V). Transientdeling må verifiseres.



\- \*\*Gnistgap:\*\* Wolframelektroder fra TIG-sveising er ideelle på grunn av høy smeltetemperatur og god erosjonsmotstand.



\- \*\*Spole:\*\* 10 AWG emaljert kobbertråd gir lav motstand og høy strømtåleevne.



\## Beskyttelseskretser



\*\*Gatebeskyttelse:\*\* Gate og source på Q1 har to separate beskyttelsesgrener.



D2 er en 15 V zenerdiode med katode mot gate og anode mot source. Den begrenser positiv \\(V\_{GS}\\) til omtrent zenerspenningen.



D4 er en 1N4148 med anode mot source og katode mot gate. Den begrenser negativ \\(V\_{GS}\\) til omtrent ett vanlig diodefall.



D2 og D4 skal altså ikke stå i serie.



\*\*Gate-utladning:\*\* R3 = 10 kΩ gir gate en definert retur til source når positiv feedback forsvinner.



\*\*Oppstart:\*\* R\_start = 100 kΩ er koblet fra +45 V-forsyningen til gate. Motstanden gir kun initial bias. Den skal ikke alene betraktes som tilstrekkelig til å drive Q1 fullt på; videre gate-drive kommer fra feedbackviklingen.



\*\*RCD-clamp:\*\* D5 leder drain-transienter inn i et clamp-nettverk der R2 og C2 ligger parallelt mot +45 V-forsyningen. Verdiene 10 kΩ og 10 nF er foreløpige og må valideres ved måling av drain-spenning.



\## Sikkerhet



\- \*\*Manuell utladning:\*\* En trykknapp med 1 kΩ / 25 W motstand (pulsratet) lar brukeren lade ut kondensatoren raskt.



\- \*\*Passiv utladning:\*\* En permanent 1 MΩ motstand over C1 sørger for langsom utladning over tid.



\- \*\*LED-indikator:\*\* En grønn LED med to 110 kΩ motstander i serie lyser når kondensatoren er ladet. Lysstyrken varierer med spenningen. \*\*LED-en er ikke en pålitelig indikator for utladet tilstand.\*\*



\- \*\*Sikring:\*\* En 2 A sikring i batterikretsen beskytter mot kortslutning.



\- \*\*Manglende automatisk spenningsgrense:\*\* Nåværende versjon stopper ikke automatisk ladingen ved 450 V. Ladespenningen må derfor overvåkes kontinuerlig under testing.

