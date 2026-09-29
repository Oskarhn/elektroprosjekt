\# Steg-for-steg prototyping og feilsøking



\## 1. Breadboard-test av flyback-omformer (lavspent)

Før du bygger hele kretsen, test flyback-omformeren på et breadboard med en lavspent kondensator (f.eks. 10 µF, 100 V) for å verifisere at den lader.



\### Oppsett

\- Bruk en 12 V strømforsyning i stedet for 45 V batteri.

\- Koble opp flyback-kretsen (Q1, T1, D1, D2, D4, R1, snubber) på breadboard.

\- Koble en 10 µF kondensator på utgangen.

\- Mål utgangsspenningen med multimeter.



\### Forventet resultat

\- Spenningen skal stige til 50–100 V i løpet av noen sekunder.

\- Hvis ingenting skjer: bytt polaritet på tilbakekoblingsviklingen.

\- Hvis MOSFET blir varm: sjekk at zener og diode er riktig koblet, og at snubberen er på plass.



\## 2. Test med hovedkondensator (100 µF, 450 V)

Når flyback-omformeren fungerer, bytt til 45 V batteri og 100 µF kondensator.



\### Oppsett

\- Koble alt på et isolerende underlag (ikke breadboard – bruk stripboard eller direkte lodding).

\- Inkluder utladningskretsen (S2, R11) og LED-indikator (D3, R12).

\- Koble et voltmeter over C1.



\### Test

\- Hold S1 inne og se at spenningen stiger til 450 V. LED skal lyse ved \~200 V.

\- Slipp S1 og trykk S2 for å lade ut. Spenningen skal falle raskt.

\- Gjenta flere ganger for å sikre stabil drift.



\## 3. Test av gnistgap og spole

Koble til gnistgap og spole.



\### Justering av gnistgap

\- Start med et gap på 0.3 mm og øk gradvis til gjennomslag skjer ved \~450 V.

\- Bruk et oscilloskop med høyspenningsprobe for å se spenningsforløpet over C1 under utladning.



\### Måling av puls

\- Plasser en pickup-spole (5 vindinger, 2 cm diameter) 20 cm foran spolen.

\- Koble pickup-spolen til oscilloskop (1 MΩ, 10x probe).

\- Fyr og observer en dempet sinus. Frekvensen bør være rundt 10 kHz.



\## 4. Feilsøking



| Problem | Mulig årsak | Løsning |

|---------|-------------|---------|

| Gnistgap slår ikke gjennom | For stort gap, for lav spenning | Reduser gapet til 0.3–0.4 mm; sjekk at C1 faktisk lades til 450 V |

| Gnistgap slår gjennom for tidlig | For lite gap, fuktighet | Øk gapet; tørk elektrodene |

| Svak eller ingen puls i pickup-spole | Dårlig kontakt, spole frakoblet | Sjekk loddinger; mål motstand i spole (skal være <0.1 Ω) |

| Oscilloskop viser støy | Dårlig jording, lang jordledning | Bruk kort jordfjær på proben; plasser pickup-spole nærmere |

| LED lyser ikke | Feil polaritet, R12 for høy | Sjekk polaritet; mål spenning over LED (skal være \~2 V ved 400 V inngang) |



\## 5. Overgang til PCB

Når prototypen fungerer pålitelig på stripboard, kan du designe og bestille PCB. Følg `pcb\_guide.md` for layout. Test PCB-en med de samme stegene som over.





