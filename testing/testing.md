\# Testprosedyre for EMP-generator



\## Sikkerhet

\- Bruk alltid vernebriller og isolerende hansker.

\- Ha en brannslukker tilgjengelig.

\- Utlad alltid kondensatoren før du berører kretsen.

\- Utfør tester i et kontrollert miljø, helst utendørs eller i et Faraday-bur.



\## Funksjonstest av lader

1\. Koble fra gnistgap og spole, men la hovedkondensator C1 være tilkoblet.

2\. Koble et voltmeter (1000 V DC) mellom utgang (D1 katode) og jord.

3\. Slå på S3, hold S1. Spenningen skal stige til 450 V i løpet av 5–10 sek. LED skal lyse.

4\. Slipp S1; spenningen skal holde seg. Trykk S2 og hold i minst 5 sekunder; spenningen skal falle til under 10 V.



\## Test av gnistgap

1\. Koble til hovedkondensator og gnistgap, men la spolen være frakoblet (åpen krets).

2\. Lad til 450 V. Gnistgapet skal slå gjennom automatisk. Du skal høre et skarpt smell og se en gnist.

3\. Hvis ikke, juster gapet mindre eller sjekk at spenningen faktisk når 450 V.



\## Test med spole

1\. Koble spolen til gnistgapets utgang.

2\. Plasser en målespole (5 vindinger, 2 cm diameter) 20 cm foran.

3\. Koble målespolen til oscilloskop (1 MΩ, 10x probe).

4\. Lad og fyr. Du skal se en dempet sinus med amplitude 10–50 V.

5\. Mål frekvens og toppspenning. Frekvensen bør være rundt 10 kHz.



\## Ødeleggelsestest

1\. Plasser en offer-enhet (f.eks. Arduino, kalkulator) 5–10 cm fra spolen.

2\. Lad og fyr. Enheten skal slutte å fungere.

3\. Gjenta med økende avstand for å finne effektiv rekkevidde.



\## Måling av toppstrøm (valgfritt)

1\. Bruk en Rogowski-spole eller en strømtransformator rundt en av ledningene til spolen.

2\. Koble til oscilloskop og integrer signalet for å finne strømmen.

3\. Sammenlign med teoretisk verdi (\~3000 A).



