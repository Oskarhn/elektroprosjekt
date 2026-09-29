\# Testprosedyre for EMP-generator



\## Sikkerhet

\- Bruk alltid vernebriller og isolerende hansker.

\- Ha en brannslukker tilgjengelig.

\- Utlad alltid kondensatoren før du berører kretsen.

\- Utfør tester i et kontrollert miljø, helst utendørs eller i et Faraday-bur.



\## Funksjonstest av lader

1\. Koble fra gnistgap og spole, men la hovedkondensator C1 være tilkoblet.

2\. Koble et voltmeter (1000 V DC) mellom utgang (katode D1b) og jord.

3\. Slå på S3, hold S1. Spenningen skal stige til 450 V i løpet av 5–10 sek. LED skal lyse.

4\. Slipp S1; spenningen skal synke gradvis (ikke falle umiddelbart). Trykk S2 og hold i minst 5 sekunder; spenningen skal falle til under 10 V.



\## Test av gnistgap (med spole tilkoblet)

1\. Koble til hovedkondensator, gnistgap og spole.

2\. Lad til 450 V. Trykk på piezo-knappen. Du skal høre et skarpt smell og se en gnist.

3\. Hvis ikke, juster gapet eller sjekk piezo-tilkobling.

4\. \*\*Merk:\*\* Spolen må være tilkoblet for å gi en lukket utladningsbane. Test aldri gnistgapet med åpen krets.



\## Måling av puls med pickup-spole

1\. Plasser en kalibrert pickup-spole (5 vindinger, 2 cm diameter) 20 cm foran spolen, på aksen.

2\. Koble pickup-spolen til oscilloskop (1 MΩ, 10x probe).

3\. Lad og fyr. Du skal se en dempet sinus. Mål frekvens og toppspenning.

4\. Forventet frekvens: 14–15 kHz (avhengig av faktisk L). Forventet toppspenning: \~280 mV (estimert fra forenklet modell; faktisk verdi avhenger av geometri, L, R, og oscilloskopinnstillinger).



\## Måling av toppstrøm (valgfritt)

1\. Bruk en Rogowski-spole eller en strømtransformator rundt en av ledningene til spolen.

2\. Koble til oscilloskop og integrer signalet for å finne strømmen.

3\. Sammenlign med teoretisk verdi (\~2600 A med antatt R=0.1 Ω).



\## Karakterisering av ladetid og skuddtakt

1\. Med fulladet batteri, mål tiden det tar å lade C1 fra 0 V til 450 V mens S1 holdes inne.

2\. Gjenta flere ganger og beregn gjennomsnittlig ladetid.

3\. Maksimal skuddtakt er begrenset av ladetiden pluss tiden for å trykke på piezo-triggeren.



\## Sikkerhetsverifikasjon

\- Etter hver test, trykk S2 og verifiser med voltmeter at spenningen er under 10 V før du berører noe.

\- Kontroller at LED-en slukker når spenningen faller, men stol aldri på LED-en alene.

