# Steg-for-steg prototyping og feilsøking

## 1. Breadboard-test av flyback-omformer (lavspent)

Før du bygger hele kretsen, test flyback-omformeren med en lavere inngangsspenning og en egnet testkondensator for å verifisere grunnleggende funksjon.

### Oppsett

- Bruk en 12 V strømforsyning i stedet for 45 V batteri.
- Koble opp flyback-kretsen (Q1, T1, D1a/D1b, D2, D4, R_start=100k, R3=10k, C3=100nF/100V, snubber).
- Koble en 10 µF, 100 V testkondensator på utgangen.
- Koble et egnet voltmeter over testkondensatoren før kretsen aktiveres.
- Kretsen har ingen automatisk spenningsgrense. Testkondensatoren må derfor overvåkes kontinuerlig under testen.

### Forventet resultat

- Verifiser at utgangsspenningen begynner å stige.
- Stopp testen ved en konservativ testspenning godt under testkondensatorens 100 V merkespenning; omtrent 50 V er tilstrekkelig for å bekrefte at omformeren fungerer.
- Ikke la testkondensatoren nærme seg eller overskride sin merkespenning.
- Hvis ingenting skjer: verifiser tilbakekoblingsviklingens polaritet mot koblingsskjemaet før koblinger endres.
- Hvis MOSFET blir varm: slå av strømforsyningen og sjekk gatebeskyttelse, snubber, viklingspolaritet og koblinger før videre testing.

## 2. Test med hovedkondensator (100 µF, 500 V)

Når flyback-omformeren fungerer ved redusert spenning, kan fullversjonen testes med 45 V inngang og 100 µF / 500 V hovedkondensator.

### Oppsett

- Koble alt på et isolerende underlag. Ikke bruk breadboard på høyspentsiden.
- Inkluder utladningskretsen (S2, R11), bleeder (1 MΩ) og LED-indikator (D3, R12a/R12b).
- Koble egnet høyspenningsmåling over C1 før laderen aktiveres.
- Husk at ladekretsen ikke har automatisk cutoff ved 450 V.

### Test

- Slå på S3.
- Aktiver S1 bare mens C1-spenningen observeres kontinuerlig.
- Slipp S1 ved eller før 450 V.
- Ikke bruk kondensatorens 500 V merkespenning som normal operativ spenning.
- Slipp S1 og trykk S2 for å lade ut.
- Verifiser med voltmeter at spenningen er under 10 V før kretsen berøres.
- Gjenta testen ved behov for å kontrollere stabil drift og faktisk ladetid.

## 3. Test av gnistgap og spole

Koble til gnistgap og spole i henhold til koblingsskjemaet.

### Kontroll av gnistgap

- Kontroller at gnistgapets mekaniske avstand stemmer med den dokumenterte konstruksjonen.
- Kontroller piezo-tilkobling og elektrodeoverflater hvis trigging ikke fungerer.
- Ikke endre gapet som en metode for å øke pulsytelsen.
- Bruk egnet høyspenningsmåling for å observere C1-spenningen før og etter testen.

### Måling av puls

- Plasser pickup-spolen i den dokumenterte måleposisjonen.
- Koble pickup-spolen til oscilloskop med egnet probe.
- Observer den dempede bølgeformen og sammenlign med den teoretiske modellen.
- For dagens forenklede modell forventes en dempet frekvens rundt 14–15 kHz, avhengig av faktisk målt L og total motstand.

## 4. Feilsøking

| Problem | Mulig årsak | Løsning |
|---------|-------------|---------|
| Flyback starter ikke | Feil polaritet eller feil i feedbackkrets | Verifiser feedbackviklingens polaritet mot koblingsskjemaet, C3, R_start, R3 og gatekoblingene |
| MOSFET blir svært varm | Feil gate-drive, snubberproblem eller feil kobling | Slå av kretsen og kontroller D2/D4, R3, feedbackpolaritet, D5/R2/C2 og drain-waveform før videre testing |
| Utgangsspenning for lav | Feil viklingstall, polaritet, kjerne/gap, lav primærinduktans eller koblingsfeil | Verifiser 10:200:5-viklingene, dot-polaritet, faktisk Lp mot målverdien ~34,5 µH, kjerne/gap og alle koblinger. Ikke endre viklingstall eller gap uten å oppdatere beregninger og dokumentasjon |
| Gnistgap trigger ikke | Feil gap, lav spenning, dårlig trigger eller skitne elektroder | Kontroller gapet mot dokumentert konstruksjon, piezo-tilkobling og elektrodeoverflater |
| Svak eller ingen puls i pickup-spole | Dårlig kontakt, feil plassering eller spole frakoblet | Sjekk loddinger, kontinuitet og måleoppsett |
| Oscilloskop viser støy | Dårlig måleoppsett eller lang jordledning | Bruk egnet probeoppsett og korte måleforbindelser |
| LED lyser ikke | Feil polaritet eller feil i LED-grenen | Sjekk D3, R12a/R12b og spenningen over LED-grenen |

## 5. Overgang til PCB

Når lavspentdelen er verifisert og nødvendige målinger er gjennomført, kan PCB-en testes etter samme trinnvise prinsipp.

Følg `pcb_guide.md` for layout, isolasjonsavstander og testpunkter. Start med redusert inngangsspenning og verifiser gate-drive, transformatorpolaritet og drain-transienter før fullspenningstesting.