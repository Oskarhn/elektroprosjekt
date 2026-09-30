\# Testprosedyre for EMP-generator



\## Sikkerhet



\- Bruk alltid vernebriller og egnet isolerende verneutstyr.

\- Ha egnet brannslukningsutstyr tilgjengelig.

\- Utlad alltid kondensatoren og verifiser spenningen med måleinstrument før du berører kretsen.

\- LED-en er kun en spenningsindikator og må aldri brukes som eneste bekreftelse på at C1 er utladet.

\- Utfør testing i et kontrollert miljø med ikke-destruktive målemetoder.



\## Funksjonstest av lader



1\. Koble fra G1/L1-pulsgrenen, men la hovedkondensator C1, bleeder, LED-gren og manuell utladningskrets være tilkoblet.



2\. Koble egnet høyspenningsmåling over C1.



3\. Slå på S3 og aktiver S1. Spenningen skal stige mot 450 V.



4\. Designmålet for ladetid er omtrent 5–10 s. Dette er ikke en verifisert verdi. Mål den faktiske tiden fra 0 V til 450 V og dokumenter resultatet.



5\. Slipp S1. Spenningen skal synke gradvis på grunn av bleeder- og LED-grenen.



6\. Aktiver S2 og hold den inne til C1 er utladet. Verifiser med voltmeter at spenningen er under 10 V før kretsen berøres.



\## Test av gnistgap med spole tilkoblet



1\. Koble til C1, G1 og L1 i den dokumenterte pulsbanen:



&#x20;  `C1+ -> G1 -> L1 -> C1-`



2\. Verifiser at likeretterdiodene D1a/D1b ikke ligger i pulsstrømbanen.



3\. Aktiver triggeren kun i kontrollert testoppsett.



4\. Etter testen skal C1 alltid kontrolleres og utlades før kretsen berøres.



\## Måling av puls med pickup-spole



1\. Plasser en kalibrert pickup-spole med 5 vindinger og 2 cm diameter 20 cm foran L1 på spoleaksen.



2\. Koble pickup-spolen til oscilloskopet med egnet probe.



3\. Registrer pickup-signalet og mål frekvens og toppspenning.



4\. For den forenklede teoretiske modellen er forventet dempet frekvens omtrent 14–15 kHz.



5\. Modellert maksimal pickup-spenning ved 20 cm er omtrent 0,28 V. Den faktiske verdien avhenger blant annet av målt L, effektiv R, geometri, orientering og måleoppsett.



\## Måling av toppstrøm



\### Rogowski-spole



Utgangen fra en Rogowski-spole er proporsjonal med strømderiverten:



\\\[

V\_\\text{Rogowski} \\propto \\frac{di}{dt}

\\]



Det kalibrerte signalet må derfor integreres for å rekonstruere strømmen.



\### Strømtransformator



En strømtransformator med korrekt burden og brukt innenfor sin båndbredde og metningsgrense gir et sekundærsignal som er tilnærmet proporsjonalt med primærstrømmen.



En vanlig strømtransformator skal derfor ikke behandles som en Rogowski-spole og signalet skal ikke integreres på samme måte.



Sammenlign den målte strømkurven med den teoretiske modellen. Verdien rundt 2,6 kA gjelder bare dersom den antatte totale seriemotstanden på 0,1 Ω er realistisk.



\## Bestemmelse av første strømtopp



Pickup-spolen måler:



\\\[

V\_\\text{pickup} \\propto -\\frac{dB}{dt}

\\]



og fordi feltet i modellen er proporsjonalt med strømmen:



\\\[

V\_\\text{pickup} \\propto -\\frac{di}{dt}

\\]



Pickup-spenningens maksimum er derfor ikke det samme tidspunktet som strømmens maksimum.



Ved første strømtopp gjelder omtrent:



\\\[

\\frac{di}{dt}=0

\\]



Strømtoppen kan derfor bestemmes ved å integrere det kalibrerte pickup-signalet eller ved å identifisere riktig nullkryssing relativt til pulsens start.



Teoretisk verdi med dagens modell er omtrent 10,8 µs.



\## Karakterisering av ladetid



1\. Start med utladet C1.

2\. Aktiver laderen og mål tiden fra 0 V til 450 V.

3\. Gjenta testen flere ganger.

4\. Registrer batterispenning før og etter hver test.

5\. Beregn gjennomsnittlig ladetid og observer eventuell økning når batteriene utlades.



Designmålet er 5–10 s, men faktisk ytelse skal bestemmes av måling.



\## Sikkerhetsverifikasjon



Etter hver test:



\- deaktiver laderen,

\- aktiver den manuelle utladningen,

\- mål spenningen over C1,

\- verifiser mindre enn 10 V før kretsen berøres.

