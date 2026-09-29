# Håndholdt EMP-generator – 10 Joule

**ADVARSEL: Dette prosjektet involverer livsfarlige spenninger (450 V DC) og svært høye strømmer (>2000 A). Den elektromagnetiske pulsen kan forstyrre elektronikk. Bygging og bruk skjer på eget ansvar. Prosjektet er kun ment for kontrollerte laboratorieforsøk med godkjent sikkerhetsopplegg. Les hele dokumentasjonen, spesielt `testing/sikkerhet.md`, før du begynner.**

## Egenskaper (teoretiske, avhengig av målte verdier)
- **Energi per puls:** 10 J (ved 450 V ladespenning)
- **Toppstrøm:** ~2600 A (estimert med antatt motstand 0,1 Ω; må måles)
- **Magnetfelt i spole sentrum:** ~0,31 T (estimert)
- **Dempet svingeperiode:** ~68,5 µs
- **Ladetid:** 5–10 s (forventet med alkaliske 9V-batterier)
- **Strømforsyning:** 5 stk. 9V-batterier i serie (45 V)
- **PCB-størrelse:** 80 × 80 mm (ladekrets)
- **Totalvekt:** ca. 0,8 kg

## Hvordan navigere i prosjektet?
- `Bygging/design.md` – Designvalg og begrunnelser
- `teori/teori.tex` – Teori og fysikk (LaTeX, kompiler til PDF)
- `teori/beregning.tex` – Detaljerte beregninger (LaTeX, kompiler til PDF)
- `Bygging/koblingsskjema.tex` – Kretsskjema (LaTeX/PDF)
- `Bygging/komponenliste.md` – Komponentliste med krav og delenumre
- `Bygging/pcb_guide.md` – PCB-layoutguide
- `Bygging/assembly.md` – Byggeveiledning
- `Bygging/prototype.md` – Steg-for-steg prototyping og feilsøking
- `testing/testing.md` – Testprosedyrer (ikke-destruktive)
- `testing/sikkerhet.md` – Sikkerhetsanalyse
- `testing/eksperimenter.tex` – Forslag til eksperimenter (LaTeX, kompiler til PDF)
- `kabinett/README.md` – 3D-printet kabinett (retningslinjer)
- `teori/verify_beregninger.py` – Skript for verifikasjon av beregninger

## Lisens
GPL-3.0
