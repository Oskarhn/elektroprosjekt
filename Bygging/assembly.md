\# Byggeveiledning for EMP-generator



\## Sikkerhetsregler



\- Arbeid alltid på et ryddig, isolerende underlag.

\- Bruk vernebriller og isolerende hansker ved testing.

\- Ha en brannslukker tilgjengelig.

\- Utlad alltid kondensatoren før du berører kretsen.

\- Ikke rett spolen mot personer, dyr eller elektronikk du ikke har tenkt å påvirke.



\## Forberedelser



Skaff alle komponenter iht. BOM. Verktøy: loddebolt, multimeter, oscilloskop (minst 100 MHz), høyspenningsprobe (100:1), vernebriller, isolerende hansker, varmepistol, superlim, 3D-printer (for kabinett og spoleform).



\## PCB-montering



1\. Lodde komponentene på PCB i rekkefølge: motstander, dioder, MOSFET, LED, brytere, transformator.

2\. Vær nøye med polaritet på dioder, LED og elektrolyttkondensator (C1).

3\. Transformator T1: lim ferrittkjernen til PCB, lodde viklingene direkte til pads.

4\. Koble batteriklemmer og eksterne komponenter via skrueterminaler.



\## Transformatorvikling



\- \*\*Kjerne:\*\* E20/10/6 ferritt (N27) med spoleholder. Bruk helst en fabrikkgappet kjerne som tilsvarer omtrent \\(A\_L = 345\\,\\text{nH/t}^2\\). Hvis gapet lages manuelt med spacer/Kapton, er 0,1 mm kun en startverdi. Mål alltid faktisk primærinduktans etter montering.



\- \*\*Målverdi:\*\* Med 10 primærvindinger og \\(A\_L \\approx 345\\,\\text{nH/t}^2\\) er forventet primærinduktans omtrent 34,5 µH. Sekundærens beregnede induktans er omtrent 13,8 mH.



\- \*\*Tråd:\*\* 0,5 mm primær, 0,1 mm sekundær og 0,2 mm tilbakekobling.



\### Viklingspolaritet



Marker startenden på hver vikling under vikling. Startenden brukes som prikkmerket terminal i koblingsskjemaet.



For koblingen i dette prosjektet:



\- \*\*Primær P, 10 vindinger:\*\* prikkmerket terminal kobles til +45 V. Den andre terminalen kobles mot Q1 drain.

\- \*\*Feedback FB, 5 vindinger:\*\* prikkmerket terminal kobles mot C3/gate. Den andre terminalen kobles til +45 V.

\- \*\*Sekundær S, 200 vindinger:\*\* prikkmerket terminal kobles til C1-/GND. Den andre terminalen kobles mot D1a.



Feedback- og sekundærviklingen er dermed elektrisk koblet med motsatt polaritet relativt til primæren.



Vikle primær 10 vindinger jevnt over spoleholderen og legg et isolasjonslag over den.



Vikle sekundær 200 vindinger. Legg inn egnet isolasjon mellom lagene og ekstra isolasjon mellom primær og sekundær.



Vikle feedbackviklingen 5 vindinger og merk begge endene tydelig.



Monter kjernehalvdelene. Mål primærinduktansen før kretsen spenningssettes. Ikke anta at et bestemt spacermål automatisk gir riktig \\(A\_L\\).



\## Gnistgap



1\. Kapp to 15 mm lange biter av 1.6 mm wolframelektrode. Slip endene flate.

2\. Monter dem i en holder av plexiglass med messingskruer slik at avstanden kan justeres.

3\. For trigger: bor et 1 mm hull midt mellom elektrodene. Lim inn en tynn, isolert ledning (0.2 mm emaljert) med 0.5 mm klaring til begge hovedelektroder. Denne ledningen er triggerelektroden.

4\. Still inn gapet til ca. 0.5 mm ved hjelp av et blad (følerlære). Dette kan finjusteres under testing.



\## Spole



1\. 3D-print en sirkulær form med spiralrille. Sporet skal ha senterdiametre: innerste vinding 20 mm, ytterste vinding 100 mm, med 4 jevnt fordelte vindinger. Rilledybde 2.5 mm.

2\. Vikle 4 tørn 10 AWG tråd i rillen, lim med superlim underveis.

3\. La to ender stikke ut (minst 15 cm) for tilkobling. Fjern emaljen fra endene med sandpapir.



\## Sluttmontering



1\. Plasser PCB, batterier og gnistgap i håndtaket (3D-printet). Håndtaket bør ha utsparinger for brytere og LED.

2\. Koble piezo-tenneren til trigger-elektroden. Den ene ledningen fra piezo går til triggerelektroden, den andre til gnistgapets jordside (ikke PCB-jord). Hold triggerkretsen isolert fra resten av elektronikken.

3\. Koble hovedkondensator C1 mellom utgang (katode D1b) og jord. Bruk korte, tykke ledninger (minst 2.5 mm²) for å minimere induktans.

4\. Koble gnistgapet mellom C1 pluss og spole. Spolens andre ende til jord (C1 minus). \*\*Disse forbindelsene må være korte og tykke – de fører pulsstrømmen.\*\*

5\. Isoler alle høyspentforbindelser med krympestrømpe eller silikon.

6\. Monter spolen foran på hodet, og fest hodet til håndtaket.



\## Første gangs oppstart



1\. Sjekk alle loddinger og tilkoblinger visuelt.



2\. Uten batterier, mål motstand mellom høyspentutgang (C1+) og jord. Det skal ikke være kortslutning (0 Ω). Forventet motstand avhenger av målemetode; sjekk at bleeder (1 MΩ) og LED-gren (220 kΩ) er tilkoblet, men ikke forvent en eksakt verdi.



3\. Sett i batterier og slå på S3. Koble egnet høyspenningsmåling over C1 før S1 aktiveres. Kretsen har ingen automatisk avkobling ved 450 V. Hold derfor S1 inne bare under kontinuerlig overvåking og slipp S1 ved eller før 450 V. Designmålet for ladetid er 5–10 s, men faktisk ladetid må måles. Laderen skal aldri stå aktivert uten overvåking.



4\. Slipp S1. Spenningen skal synke gradvis (ikke falle umiddelbart). Trykk S2 for å lade ut. \*\*Hold knappen inne i minst 5 sekunder.\*\* Spenningen skal falle til under 10 V. Verifiser med voltmeter før du berører kretsen.



5\. Test trigger: Lad opp til maksimalt 450 V under kontinuerlig spenningsmåling, trykk på piezo-knappen. Du skal høre et skarpt smell og se en gnist i gapet. Hvis ikke, avbryt ladingen, lad ut C1 og kontroller oppsettet før videre testing.

