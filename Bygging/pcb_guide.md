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

\- \*\*Kjerne:\*\* E20/10/6 ferritt (N27), med spoleholder. Bruk et standard luftgap på 0.1 mm (f.eks. et lag Kapton-tape mellom kjernehalvdelene). Dette gir AL ≈ 345 nH/t² og Lp ≈ 34.5 µH med 10 tørn.

\- \*\*Tråd:\*\* 0.5 mm (primær), 0.1 mm (sekundær), 0.2 mm (tilbakekobling).

\- Vikle primær (10 t) med 0.5 mm tråd jevnt fordelt over spoleholderen. Legg isolasjonstape.

\- Vikle sekundær (200 t) med 0.1 mm tråd. Legg inn isolasjon hver 50. vinding.

\- Vikle tilbakekobling (5 t) med 0.2 mm tråd over sekundæren, med isolasjon.

\- Monter kjernehalvdelene med luftgap og lim sammen. Mål induktans: primær \~34.5 µH, sekundær \~13.8 mH. Juster gapet kun hvis nødvendig.



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

3\. Sett i batterier, slå på S3. Hold S1 inne og mål spenningen over C1 med et voltmeter (1000 V DC). Spenningen skal stige til 450 V i løpet av 5–10 sekunder. LED skal lyse.

4\. Slipp S1. Spenningen skal synke gradvis (ikke falle umiddelbart). Trykk S2 for å lade ut. \*\*Hold knappen inne i minst 5 sekunder.\*\* Spenningen skal falle til under 10 V. Verifiser med voltmeter før du berører kretsen.

5\. Test trigger: Lad opp til 450 V, trykk på piezo-knappen. Du skal høre et skarpt smell og se en gnist i gapet. Hvis ikke, juster gapet eller sjekk piezo-tilkobling.



