# Håndholdt EMP-generator – 10 Joule

**ADVARSEL: Dette prosjektet involverer livsfarlige spenninger (450 V DC) og ekstremt høye strømmer (>3000 A). Den elektromagnetiske pulsen kan permanent ødelegge elektronikk, forstyrre medisinsk utstyr og forårsake brann. Bygging og bruk skjer på eget ansvar. Prosjektet er kun ment for kontrollerte laboratorieforsøk med godkjent sikkerhetsopplegg. Les hele dokumentasjonen, spesielt `safety.md`, før du begynner.**

## Egenskaper (teoretiske)
- **Energi per puls:** 10 J (ved 450 V ladespenning)
- **Toppstrøm:** ~3 000 A
- **Magnetfelt i spole sentrum:** ~0,13 T
- **Pulsvarighet:** ~100 µs (dempet sinus)
- **Repetisjonsrate:** 1–2 skudd per sekund (hold ladeknappen inne)
- **Strømforsyning:** 5 stk. 9V-batterier i serie (45 V) – LiPo anbefales for bedre ytelse
- **PCB-størrelse:** 80 × 80 mm (ladekrets)
- **Totalvekt:** ca. 0,8 kg

## Hvordan navigere i prosjektet?
- `design.md` – Designvalg og begrunnelser
- `theory.tex` – Teori og fysikk (LaTeX, kompiler til PDF)
- `calculations.tex` – Detaljerte beregninger (LaTeX, kompiler til PDF)
- `schematic/` – Kretsskjema (LaTeX/PDF)
- `bom.md` – Komponentliste med delenumre og formål
- `pcb_guide.md` – PCB-layoutguide
- `assembly.md` – Byggeveiledning
- `prototyping.md` – Steg-for-steg prototyping og feilsøking
- `testing.md` – Testprosedyrer
- `safety.md` – Sikkerhetsanalyse
- `experiments.tex` – Forslag til eksperimenter (LaTeX, kompiler til PDF)
- `enclosure/` – 3D-printet kabinett (retningslinjer)

## Lisens
GPL-3.0
