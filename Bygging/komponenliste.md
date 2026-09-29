\# Komponentliste (BOM)



| Ref | Komponent | Verdi | Footprint | Antall | Formål | Status |

|-----|-----------|-------|-----------|--------|--------|--------|

| C1 | Elektrolytisk kondensator | 100 µF, 500 V | Snap-in | 1 | Energilager; må tåle høy pulsstrøm | Må verifiseres |

| C2 | Keramisk kondensator | 10 nF, 500 V | Radial | 1 | Snubber | TBD |

| C3 | Keramisk kondensator | 100 nF, 100 V | Radial | 1 | DC-blokkering gate | TBD |

| Q1 | MOSFET | IRFP450 | TO-247 | 1 | Flyback-svitsj | TBD |

| D1a, D1b | Diode | UF4007 | DO-41 | 2 | Likeretter (to i serie) | TBD |

| D2 | Zenerdiode | 15 V, 0.5 W | DO-35 | 1 | Gate-beskyttelse | TBD |

| D3 | LED | Grønn 5 mm | 5 mm | 1 | Spenningsindikator | TBD |

| D4 | Diode | 1N4148 | DO-35 | 1 | Hindrer negativ gate | TBD |

| D5 | Diode | UF4007 | DO-41 | 1 | Snubber | TBD |

| R\_start | Motstand | 100 kΩ, 0.25 W | AXIAL-0.3 | 1 | Oppstart gate | TBD |

| R2 | Motstand | 10 kΩ, 0.25 W | AXIAL-0.3 | 1 | Snubber | TBD |

| R3 | Motstand | 10 kΩ, 0.25 W | AXIAL-0.3 | 1 | Gate-utladning | TBD |

| R11 | Motstand | 1 kΩ, 25 W | Trådviklet | 1 | Utladning (puls) | Må verifiseres |

| R12a, R12b | Motstand | 110 kΩ, 1 W | AXIAL-0.5 | 2 | LED-strømbegrenser | Må verifiseres (arbeidsspenning) |

| R\_bleed | Motstand | 1 MΩ, 1 W | AXIAL-0.5 | 1 | Passiv utladning | Må verifiseres (arbeidsspenning) |

| S1 | Trykknapp | SPST momentan | Panel | 1 | Ladeknapp (lavspent) | TBD |

| S2 | Trykknapp | SPST momentan, min. 450 V DC, 0.5 A | Panel | 1 | Utladningsknapp | Må spesifiseres |

| S3 | Vippebryter | SPST, 50 V DC | Panel | 1 | Hovedstrøm | TBD |

| F1 | Sikring | 2 A, 250 V | 5×20 mm | 1 | Batteribeskyttelse | TBD |

| T1 | Transformator | E20/10/6, N27, 0.1 mm luftgap | Custom | 1 | 10:200:5 viklinger | Må bygges/måles |

| G1 | Gnistgap | Wolframelektroder, trigget | Custom | 1 | \~0,5 mm gap | Må bygges |

| L1 | Spole | 10 AWG emaljert tråd | Custom | 1 | Flat spiral, 4 vindinger | Må måles |

| Batteri | 9V batteriklemmer | Snap-kontakt | - | 5 | 5×9V i serie (45 V) | TBD |



\*\*Merk:\*\* Alle delenumre er TBD inntil verifisert mot gjeldende kataloger.

