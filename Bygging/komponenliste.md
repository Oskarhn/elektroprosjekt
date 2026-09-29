\# Komponentliste (BOM)



| Ref | Komponent | Verdi | Footprint | Antall | Formål | Status |

|-----|-----------|-------|-----------|--------|--------|--------|

| C1 | Elektrolytisk kondensator | 100 µF, 450 V | Snap-in | 1 | Energilager; må tåle høy pulsstrøm | Må verifiseres |

| C2 | Keramisk kondensator | 10 nF, 500 V | Radial | 1 | Snubber | OK |

| Q1 | MOSFET | IRFP450 | TO-247 | 1 | Flyback-svitsj | OK |

| D1a, D1b | Diode | UF4007 | DO-41 | 2 | Likeretter (to i serie) | OK |

| D2 | Zenerdiode | 15 V, 0.5 W | DO-35 | 1 | Gate-beskyttelse | OK |

| D3 | LED | Grønn 5 mm | 5 mm | 1 | Spenningsindikator | OK |

| D4 | Diode | 1N4148 | DO-35 | 1 | Hindrer negativ gate | OK |

| D5 | Diode | UF4007 | DO-41 | 1 | Snubber | OK |

| R1 | Motstand | 1 kΩ, 1 W | AXIAL-0.5 | 1 | Gate-motstand | OK |

| R2 | Motstand | 10 kΩ, 0.25 W | AXIAL-0.3 | 1 | Snubber | OK |

| R11 | Motstand | 1 kΩ, 25 W | Trådviklet | 1 | Utladning (puls) | Må verifiseres |

| R12a, R12b | Motstand | 110 kΩ, 1 W | AXIAL-0.5 | 2 | LED-strømbegrenser | OK |

| R\_bleed | Motstand | 1 MΩ, 1 W | AXIAL-0.5 | 1 | Passiv utladning | OK |

| S1 | Trykknapp | SPST momentan | Panel | 1 | Ladeknapp (lavspent) | OK |

| S2 | Trykknapp | SPST momentan, min. 450 V DC, 0.5 A | Panel | 1 | Utladningsknapp | Må spesifiseres |

| S3 | Vippebryter | SPST, 50 V DC | Panel | 1 | Hovedstrøm | OK |

| F1 | Sikring | 2 A, 250 V | 5×20 mm | 1 | Batteribeskyttelse | OK |

| T1 | Transformator | E20/10/6, N27, luftgap | Custom | 1 | 10:200:5 viklinger | Må bygges/måles |

| G1 | Gnistgap | Wolframelektroder, trigget | Custom | 1 | \~0,5 mm gap | Må bygges |

| L1 | Spole | 10 AWG emaljert tråd | Custom | 1 | Flat spiral, 4 vindinger | Må måles |

| Batteri | 9V batteriklemmer | Snap-kontakt | - | 5 | 5×9V i serie (45 V) | OK |



\*\*Merk:\*\* Alle delenumre er TBD inntil verifisert mot gjeldende kataloger.



