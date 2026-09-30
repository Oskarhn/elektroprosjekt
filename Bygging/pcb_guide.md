\# PCB-layoutguide for ladekrets



\## Spesifikasjoner



\- \*\*Størrelse:\*\* 80 × 80 mm, dobbeltsidig FR4, 1.6 mm tykkelse, 35 µm kobber.



\- \*\*Isolasjonsavstand:\*\* Minst 2 mm krypestrøm for spor >100 V, men endelig avstand må velges iht. gjeldende standard (f.eks. IPC-2221) for 450 V arbeidsspenning.



\- \*\*Sporbredde for høye strømmer:\*\* Minst 2 mm for primærkretsen (batteri, MOSFET, transformator).



\- \*\*Jordplan:\*\* Solid jordplan på bunnsiden for ladekretsen, med utsparinger under høyspentkomponenter.



\## Komponentplassering



1\. \*\*Strøminngang:\*\* Plasser skrueterminal for batteri (45 V) i nedre venstre hjørne. Rett ved siden av: sikring F1 og hovedbryter S3 (kan også monteres på panelet).



2\. \*\*Flyback-kjerne:\*\* MOSFET Q1, transformator T1, dioder D1a/D1b, zener D2, diode D4, og snubber-komponenter (D5, R2, C2) plasseres i en tett klynge midt på kortet for å minimere sløyfearealet for høyfrekvente strømmer.



&#x20;  - Q1: TO-247, stående med kjøleribbe (valgfritt). Plasser slik at drain, source og gate er lett tilgjengelige.

&#x20;  - T1: Ferrittkjerne limes til kortet. Primær- og sekundærviklinger loddes direkte til pads.

&#x20;  - D1a/D1b: Stående montering nær transformatorens sekundær.



3\. \*\*Høyspentutgang:\*\* Katoden til D1b går til en stor, isolert pad (minst 3 mm bredde) som går til en skrueterminal for tilkobling av ekstern hovedkondensator C1. Denne terminalen bør være i øvre høyre hjørne.



4\. \*\*Kontrollkomponenter:\*\* Ladeknapp S1, utladningsknapp S2, LED D3 og motstander R12a/R12b plasseres langs høyre kant for enkel tilgang gjennom kabinettet.



5\. \*\*Testpunkter:\*\* Legg inn følgende loddeøyer:



&#x20;  - TP1: Gate på Q1 (for oscilloskopmåling av svitsjeforløp).

&#x20;  - TP2: Utgangsspenning (katode D1b) for voltmetertilkobling.

&#x20;  - TP3: Jord for ladekretsen (stjernejordpunkt).

&#x20;  - TP4: Valgfri spenningsdeler for sikker høyspentmåling (se under).



\## Spenningsdeler for høyspentmåling (valgfri)



For å måle utgangsspenningen trygt med et vanlig multimeter, kan du legge til en spenningsdeler:



\- R13: 10 MΩ, 1 W (høyspentmotstand, f.eks. Vishay VR68)

\- R14: 100 kΩ, 0.25 W

\- Koble R13 mellom HV-utgang (katode D1b) og TP4.

\- Koble R14 mellom TP4 og GND.

\- Spenningen på TP4 er V\_ut / 101. Ved 450 V vil TP4 vise \~4.46 V.



\## Sporingsregler



\- \*\*Høyspentnett:\*\* Alle spor som er koblet til D1b's katode, C1, gnistgap og utladningskrets må ha minst 2 mm klaring til jordplan og andre signaler. Bruk 2.5 mm spor der det er mulig.



\- \*\*Primærkrets:\*\* Sporene mellom batteri, S1, primærvikling og MOSFET må være korte og tykke (≥2 mm) for å minimere induktans og resistive tap.



\- \*\*Jord for ladekrets:\*\* Alle jordforbindelser for lade- og kontrollkretsen (batteri minus, source Q1, sekundærvikling retur, C1 minus, utladningskrets, LED) samles i ett stjernepunkt nær batteriets minuspol. Unngå sløyfer.



\- \*\*Pulsstrøm:\*\* \*\*Den høye pulsstrømmen (C1 → G1 → L1 → C1) må ikke gå gjennom PCB-spor.\*\* Disse forbindelsene skal være eksterne, tykke ledninger direkte mellom komponentene. C1- er referansepunktet; ladekretsen kan koble seg til C1- i ett punkt, men pulsstrømmen må gå direkte fra L1 til C1- utenom PCB.



\## Termisk design



\- MOSFET Q1 kan bli varm under kontinuerlig lading. Fest en liten kjøleribbe (f.eks. 20 × 20 mm) med varmeledende lim. Sørg for luftstrøm i kabinettet.



\- Utladningsmotstand R11 (1 kΩ / 25 W) monteres utenfor PCB på en metallplate eller kjøleprofil, da den kan bli varm under utladning.



\## Tilkoblinger til eksterne komponenter



\- \*\*Hovedkondensator C1:\*\* Bruk en snap-in kondensator og koble den med korte, tykke ledninger (minst 2.5 mm²) direkte til skrueterminalene på PCB.



\- \*\*Gnistgap G1:\*\* Monteres på et separat brett nær spolen. Koble den ene siden til C1 pluss (via tykk ledning) og den andre til spolen.



\- \*\*Spole L1:\*\* Loddes direkte til gnistgapets utgangselektrode og jord (C1 minus) med tykke ledninger.



\- \*\*Piezo-trigger:\*\* To ledninger trekkes fra piezo-elementet i håndtaket til triggerelektroden i gnistgapet. Hold triggerkretsen isolert fra PCB-jord for å unngå støy.



\## Produksjon



\- Design PCB-en i KiCad (eller tilsvarende) og generer Gerber-filer.

\- Bestill fra f.eks. JLCPCB eller et annet prototyping-firma.

\- Alternativt kan du bruke et stripboard (veroboard) og lodde komponentene for hånd, men da må du være ekstra nøye med isolasjonsavstander.

