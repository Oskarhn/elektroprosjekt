# Sikkerhetsanalyse for EMP-generator

## 1. Innledning

Dette dokumentet identifiserer farer, risikoreduserende tiltak og gjenværende risiko ved bygging og bruk av den håndholdte EMP-generatoren. Analysen er basert på det teoretiske designet; fysisk verifikasjon er ikke utført. **Dette er ikke en fullstendig sikkerhetssertifisering.**

## 2. Identifiserte farer

### 2.1 Høyspenning (450 V DC)

- **Fare:** Livsfarlig elektrisk støt. Strøm gjennom kroppen kan forårsake hjertestans.

- **Risikoreduserende tiltak:**
  - Manuell utladningskrets (1 kΩ / 25 W) med trykknapp.
  - Passiv bleeder-motstand (1 MΩ) for langsom utladning.
  - LED-indikator for spenning (ikke pålitelig som eneste indikator).
  - Sikring (2 A) i batterikretsen.
  - Anbefalt bruk av isolerende hansker (klasse 0, minimum 1000 V) og vernebriller.
  - C1-spenningen skal overvåkes med egnet høyspenningsmåling mens laderen er aktiv.

- **Gjenværende risiko:** Kondensatoren kan holde farlig spenning i timevis hvis bleederen svikter og manuell utladning ikke utføres. LED kan svikte. Brukerfeil kan føre til støt. Sikringen beskytter kun batterikretsen, ikke mot utladning fra kondensatoren. Nåværende ladekrets har ingen automatisk cutoff ved 450 V; dersom S1 holdes inne for lenge, finnes ingen dokumentert automatisk funksjon som hindrer videre opplading.

### 2.2 Høye strømmer og lysbue

- **Fare:** Brannskader, brann, eksplosjon ved kortslutning.

- **Risikoreduserende tiltak:**
  - Gnistgapet er bygget av wolfram for å tåle høye temperaturer.
  - Spolen er dimensjonert for pulsstrømmer.
  - Sikring beskytter batterikretsen.

- **Gjenværende risiko:** Feil på kondensator (intern kortslutning) kan føre til eksplosjon. Lysbuen kan antenne brennbare materialer. Sikringen gir ingen beskyttelse mot kondensatorens lagrede energi.

### 2.3 Elektromagnetisk puls

- **Fare:** Forstyrrelse av nærliggende elektronikk, inkludert medisinsk utstyr (pacemakere).

- **Risikoreduserende tiltak:**
  - Operer kun i kontrollerte omgivelser, helst i et Faraday-bur eller utendørs på trygg avstand fra personer og utstyr.
  - Advar alle tilstedeværende.

- **Gjenværende risiko:** Utilsiktet påvirkning av elektronikk utenfor kontrollsonen. Ingen dokumentert skjerming.

### 2.4 Termisk belastning

- **Fare:** Overoppheting av komponenter ved gjentatte pulser.

- **Risikoreduserende tiltak:**
  - Temperaturberegninger viser moderat oppvarming per puls, men lokale varmepunkter kan oppstå.
  - Anbefalt kjøling av utladningsmotstand og MOSFET.

- **Gjenværende risiko:** Beregningene er forenklede. Langvarig drift uten kjøling kan skade komponenter. Ingen termisk validering er utført.

### 2.5 Komponentfeil

- **Fare:** Kondensator kan eksplodere ved overbelastning eller feil. MOSFET kan svikte og forårsake kortslutning.

- **Risikoreduserende tiltak:** Komponenter er valgt med marginer, men transienter og feiltilstander er ikke fullstendig analysert.

- **Gjenværende risiko:** Ingen feilanalyse (FMEA) er gjennomført.

### 2.6 Måleutstyr

- **Fare:** Feil bruk av multimeter eller oscilloskop på høyspentkrets kan ødelegge utstyr og gi støt.

- **Risikoreduserende tiltak:** Anbefalt bruk av 100:1 probe og spenningsdeler.

- **Gjenværende risiko:** Måleoppsettet er ikke validert for de aktuelle transientene.

### 2.7 Restenergi etter frakobling

- **Fare:** Kondensatoren kan holde 10 J i timevis. Utladningsveier er den manuelle kretsen, bleederen (1 MΩ) og LED-grenen (høy impedans, ikke sikker).

- **Risikoreduserende tiltak:** Prosedyre for utladning og spenningsmåling.

- **Gjenværende risiko:** Hvis utladningsbryter eller motstand svikter, finnes ingen rask utladningsvei. Bleederen tømmer kondensatoren over tid (tidskonstant ~100 s), men dette er ikke en pålitelig sikkerhetsmekanisme alene.

### 2.8 Svikt i utladningsbryter

- **Fare:** Bruker kan tro at kondensatoren er utladet og berøre spenningsførende deler.

- **Risikoreduserende tiltak:** Visuell inspeksjon og dobbeltsjekk med multimeter.

- **Gjenværende risiko:** Multimeter kan være feilinnstilt eller defekt.

### 2.9 Termisk svikt ved gjentatte pulser

- **Fare:** Utladningsmotstand og spole kan overopphetes ved rask repetisjon.

- **Risikoreduserende tiltak:** Anbefalt pause mellom skudd.

- **Gjenværende risiko:** Ingen automatisk termisk beskyttelse.

### 2.10 Elektromagnetisk interferens

- **Fare:** Forstyrrelse eller skade på medisinsk utstyr (pacemakere, insulinpumper) i nærheten.

- **Risikoreduserende tiltak:** Operer i avskjermet rom eller på betryggende avstand.

- **Gjenværende risiko:** Utilstrekkelig skjerming; rekkevidde for interferens er ukjent.

## 3. Sikkerhetsprosedyrer

Se `Bygging/assembly.md` og `testing/testing.md` for detaljerte instruksjoner. Følgende overordnede regler gjelder:

- Alltid utlad kondensatoren manuelt før berøring (hold utladningsknappen i minst 5 sekunder, verifiser med multimeter).
- Bruk aldri LED-en som eneste indikator på utladet tilstand.
- Overvåk C1-spenningen kontinuerlig mens S1 holdes inne, og stopp ladingen ved eller før 450 V.
- Ikke forlat kretsen mens laderen er aktiv.
- Bruk personlig verneutstyr.
- Ha en brannslukker (CO2) tilgjengelig.
- Operer med en partner (buddy system).

## 4. Mangler og videre arbeid

- Fysisk prototype må bygges og testes for å validere sikkerheten.
- Nåværende lader har ingen automatisk 450 V-cutoff; en uavhengig overvoltage-beskyttelse bør vurderes før designet betraktes som selvstendig sikkert.
- Bleeder-motstanden gir passiv utladning, men en raskere automatisk utladningsmekanisme kan vurderes.
- Kapsling må designes og verifiseres for å hindre berøring av spenningsførende deler.
- Måleoppsett for høyspenning må kvalifiseres (prober, isolasjon).
- Full feilanalyse (FMEA) bør utføres.
- Termisk validering ved gjentatte pulser må gjennomføres.

**Konklusjon:** Designet har iboende farer som krever streng disiplin og kompetanse. Det anbefales ikke for uerfarne personer.