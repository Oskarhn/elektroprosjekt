# Håndholdt EMP-generator – 10 Joule

**ADVARSEL: Dette prosjektet involverer livsfarlige spenninger (450 V DC) og svært høye strømmer (>2000 A). Den elektromagnetiske pulsen kan forstyrre eller skade elektronikk. Bygging og bruk skjer på eget ansvar. Prosjektet er kun ment for kontrollerte laboratorieforsøk med godkjent sikkerhetsopplegg. Les hele dokumentasjonen, spesielt `safety.md`, før du begynner.**

## Egenskaper (teoretiske, avhengig av målte verdier)
- **Energi per puls:** 10 J (ved 450 V ladespenning)
- **Toppstrøm:** ~2600 A (estimert med antatt motstand 0,1 Ω; må måles)
- **Magnetfelt i spole sentrum:** ~0,3 T (estimert)
- **Pulsvarighet:** ~70 µs (dempet sinus)
- **Repetisjonsrate:** 0,2–0,5 Hz med alkaliske 9V-batterier (avhengig av ladestrøm)
- **Strømforsyning:** 5 stk. 9V-batterier i serie (45 V) – LiPo anbefales for bedre ytelse
- **PCB-størrelse:** 80 × 80 mm (ladekrets)
- **Totalvekt:** ca. 0,8 kg

## Hvordan navigere i prosjektet?
- `design.md` – Designvalg og begrunnelser
- `theory.tex` – Teori og fysikk (LaTeX, kompiler til PDF)
- `calculations.tex` – Detaljerte beregninger (LaTeX, kompiler til PDF)
- `schematic/` – Kretsskjema (LaTeX/PDF)
- `bom.md` – Komponentliste med krav og delenumre (mange TBD)
- `pcb_guide.md` – PCB-layoutguide
- `assembly.md` – Byggeveiledning
- `prototyping.md` – Steg-for-steg prototyping og feilsøking
- `testing.md` – Testprosedyrer (ikke-destruktive)
- `safety.md` – Sikkerhetsanalyse
- `experiments.tex` – Forslag til eksperimenter (LaTeX, kompiler til PDF)
- `enclosure/` – 3D-printet kabinett (retningslinjer)
- `tools/verify_calculations.py` – Skript for verifikasjon av beregninger
- `ENGINEERING_REVIEW.md` – Full gjennomgang av rettelser

## Lisens
GPL-3.0
