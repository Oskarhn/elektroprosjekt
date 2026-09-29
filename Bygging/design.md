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

\- Bruker få komponenter (MOSFET, transformator, diode, zener, motstander, kondensator, snubber).



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

\- \*\*Gatebeskyttelse:\*\* En 15 V zenerdiode (D2) og en 1N4148 (D4) i serie klemmer gate-spenningen til maksimalt \~15,7 V og hindrer negativ spenning.

\- \*\*Snubber over primærvikling:\*\* En RCD-snubber (D5, R2, C2) demper spenningstransienter når MOSFET-en slår seg av. Verdiene er veiledende og må valideres med måling av drain-spenning.



\## Sikkerhet

\- \*\*Manuell utladning:\*\* En trykknapp med 1 kΩ / 25 W motstand (pulsratet) lar brukeren lade ut kondensatoren raskt.

\- \*\*Passiv utladning:\*\* En permanent 1 MΩ motstand over C1 sørger for langsom utladning over tid.

\- \*\*LED-indikator:\*\* En grønn LED med to 110 kΩ motstander i serie lyser når kondensatoren er ladet. Lysstyrken varierer med spenningen. \*\*LED-en er ikke en pålitelig indikator for utladet tilstand.\*\*

\- \*\*Sikring:\*\* En 2 A sikring i batterikretsen beskytter mot kortslutning.



