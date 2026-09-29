\# Komponentliste (BOM) med krav og delenumre



\*\*Merk:\*\* Mange delenumre er TBD eller må verifiseres. Ikke stol blindt på oppgitte numre; sjekk alltid mot gjeldende datablader og leverandørkataloger.



| Ref | Komponent | Verdi | Footprint | Antall | Farnell | RS | Formål | Status |

|-----|-----------|-------|-----------|--------|---------|----|--------|--------|

| C1 | Elektrolytisk kondensator | 100 µF, 450 V | Snap-in | 1 | TBD | TBD | Energilager; må tåle høy pulsstrøm (lav ESR) | Må verifiseres |

| C2 | Keramisk kondensator | 10 nF, 500 V | Radial | 1 | TBD | TBD | Snubber-kondensator | OK |

| Q1 | MOSFET | IRFP450 | TO-247 | 1 | TBD | TBD | Svitsjer flyback; 500 V, 14 A | OK |

| D1a, D1b | Diode | UF4007 | DO-41 | 2 | TBD | TBD | Likeretter; to i serie for 1500 V rating | OK |

| D2 | Zenerdiode | 15 V, 0.5 W | DO-35 | 1 | TBD | TBD | Gate-beskyttelse | OK |

| D3 | LED | Grønn 5 mm | 5 mm | 1 | TBD | TBD | Spenningsindikator (>200 V) | OK |

| D4 | Diode | 1N4148 | DO-35 | 1 | TBD | TBD | Hindrer negativ gate-spenning | OK |

| D5 | Diode | UF4007 | DO-41 | 1 | TBD | TBD | Snubber-diode | OK |

| R1 | Motstand | 1 kΩ, 0.25 W | AXIAL-0.3 | 1 | TBD | TBD | Gate-motstand | OK |

| R2 | Motstand | 10 kΩ, 0.25 W | AXIAL-0.3 | 1 | TBD | TBD | Snubber-motstand | OK |

| R11 | Motstand | 1 kΩ, 25 W | Trådviklet | 1 | TBD | TBD | Utladningsmotstand; må tåle puls (10 J) | Må verifiseres |

| R12a, R12b | Motstand | 110 kΩ, 1 W | AXIAL-0.5 | 2 | TBD | TBD | LED-strømbegrenser (spenningsdeling) | OK |

| S1 | Trykknapp | SPST momentan | Panel | 1 | TBD | TBD | Ladeknapp (lavspent) | OK |

| S2 | Trykknapp | SPST momentan | Panel | 1 | TBD | TBD | Utladningsknapp (min. 450 V DC, 0.5 A) | Må spesifiseres |

| S3 | Vippebryter | SPST | Panel | 1 | TBD | TBD | Hovedstrømbryter (min. 50 V DC) | OK |

| F1 | Sikring | 2 A, 250 V | 5×20 mm | 1 | TBD | TBD | Batteribeskyttelse | OK |

| T1 | Transformator | E20/10/6 kjerne, N27, luftgap | Custom | 1 | - | - | Viklinger: 10:200:5; primærinduktans \~50 µH (med gap) | Må bygges/måles |

| G1 | Gnistgap | Wolframelektroder, trigget | Custom | 1 | - | - | 1.6 mm TIG-elektroder, \~0.5 mm gap, triggerelektrode | Må bygges |

| L1 | Spole | 10 AWG emaljert tråd | Custom | 1 | - | - | Flat spiral, 4 vindinger, \~0.83 µH (estimert) | Må måles |

| Batteri | 9V batteriklemmer | Snap-kontakt | - | 5 | TBD | TBD | For 5 stk. 9V-batterier i serie (45 V) | OK |



\*\*Viktige merknader:\*\*

\- Alle delenumre er TBD inntil verifisert mot gjeldende kataloger.

\- R11 må ha pulsenergi-rating; en 25 W trådviklet motstand kan være egnet, men sjekk datablad.

\- S2 må være spesifisert for DC-spenning og strøm; vanlige panelbrytere er ofte kun ratet for AC.

\- C1 må være egnet for pulsutladning; "fotoflash"-type anbefales, men verifiser ESR og pulsstrøm.



