\# Byggeveiledning for EMP-generator



\## Sikkerhetsregler

\- Arbeid alltid på et ryddig, isolerende underlag.

\- Bruk vernebriller og isolerende hansker ved testing.

\- Ha en brannslukker tilgjengelig.

\- Utlad alltid kondensatoren før du berører kretsen.

\- Ikke rett spolen mot personer, dyr eller elektronikk du ikke har tenkt å ødelegge.



\## Forberedelser

Skaff alle komponenter iht. BOM. Verktøy: loddebolt, multimeter, oscilloskop (minst 100 MHz), høyspenningsprobe (100:1), vernebriller, isolerende hansker, varmepistol, superlim, 3D-printer (for kabinett og spoleform).



\## PCB-montering

1\. Lodde komponentene på PCB i rekkefølge: motstander, dioder, MOSFET, LED, brytere, transformator.

2\. Vær nøye med polaritet på dioder, LED og elektrolyttkondensator (C1).

3\. Transformator T1: lim ferrittkjernen til PCB, lodde viklingene direkte til pads.

4\. Koble batteriklemmer og eksterne komponenter via skrueterminaler.



\## Transformatorvikling

\- \*\*Kjerne:\*\* E20/10/6 ferritt (N27), med spoleholder.

\- \*\*Tråd:\*\* 0.5 mm (primær), 0.1 mm (sekundær), 0.2 mm (tilbakekobling).

\- Vikle primær (10 t) med 0.5 mm tråd jevnt fordelt over spoleholderen. Legg isolasjonstape.

\- Vikle sekundær (200 t) med 0.1 mm tråd. Legg inn isolasjon hver 50. vinding.

\- Vikle tilbakekobling (5 t) med 0.2 mm tråd over sekundæren, med isolasjon.

\- Monter kjernehalvdelene og lim sammen. Mål induktans: primær \~50 µH, sekundær \~20 mH.



\## Gnistgap

1\. Kapp to 15 mm lange biter av 1.6 mm wolframelektrode. Slip endene flate.

2\. Monter dem i en holder av plexiglass med messingskruer slik at avstanden kan justeres.

3\. Still inn gapet til ca. 0.5 mm ved hjelp av et blad (følerlære). Dette kan finjusteres under testing for å oppnå gjennomslag ved \~450 V.



\## Spole

1\. 3D-print en sirkulær form med spiralrille (20 mm indre, 100 mm ytre, 2.5 mm dybde).

2\. Vikle 4 tørn 10 AWG tråd i rillen, lim med superlim underveis.

3\. La to ender stikke ut (minst 15 cm) for tilkobling. Fjern emaljen fra endene med sandpapir.



\## Sluttmontering

1\. Plasser PCB, batterier og gnistgap i håndtaket (3D-printet). Håndtaket bør ha utsparinger for brytere og LED.

2\. Koble hovedkondensator C1 mellom utgang (D1 katode) og jord. Bruk korte, tykke ledninger (minst 2.5 mm²) for å minimere induktans.

3\. Koble gnistgapet mellom C1 pluss og spole. Spolens andre ende til jord.

4\. Isoler alle høyspentforbindelser med krympestrømpe eller silikon.

5\. Monter spolen foran på hodet, og fest hodet til håndtaket.



\## Første gangs oppstart

1\. Sjekk alle loddinger og tilkoblinger visuelt.

2\. Uten batterier, mål motstand mellom høyspentutgang og jord – skal være uendelig (åpen krets).

3\. Sett i batterier, slå på S3. Hold S1 inne og mål spenningen over C1 med et voltmeter (1000 V DC). Spenningen skal stige til 450 V i løpet av 5–10 sekunder. LED skal lyse.

4\. Slipp S1. Spenningen skal holde seg. Trykk S2 for å lade ut. \*\*Hold knappen inne i minst 5 sekunder.\*\* Spenningen skal falle til under 10 V. Verifiser med voltmeter før du berører kretsen.

5\. Test selvutløsning: Hold S1 inne og observer at gnistgapet slår gjennom når spenningen når \~450 V. Du skal høre et skarpt smell og se en gnist. Hvis ikke, juster gapet.



