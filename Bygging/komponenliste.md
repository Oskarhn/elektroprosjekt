\# Komponentliste (BOM) med delenumre og formål



| Ref | Komponent | Verdi | Footprint | Antall | Farnell | RS | Formål |

|-----|-----------|-------|-----------|--------|---------|----|--------|

| C1 | Elektrolytisk kondensator | 100 µF, 450 V | Snap-in | 1 | 184-8404 | 136-6285 | Energilager for pulsen; fotoflash-type tåler høy pulsstrøm |

| C2 | Keramisk kondensator | 10 nF, 500 V | Radial | 1 | 123-6654 | 711-1245 | Snubber-kondensator for å dempe spenningstopper |

| Q1 | MOSFET | IRFP450 | TO-247 | 1 | 146-3412 | 700-4322 | Svitsjer strømmen i flyback-omformeren; 500 V, 14 A |

| D1 | Diode | UF4007 | DO-41 | 1 | 146-7590 | 700-4287 | Likeretter høyspentpulsene fra transformatoren |

| D2 | Zenerdiode | 15 V, 0.5 W | DO-35 | 1 | 170-0750 | 544-3245 | Klemmer gate-spenningen til maks 15 V for å beskytte MOSFET |

| D3 | LED | Grønn 5 mm | 5 mm | 1 | 102-4030 | 228-5608 | Indikerer at kondensatoren er ladet >200 V |

| D4 | Diode | 1N4148 | DO-35 | 1 | 146-7600 | 700-4290 | Hindrer negativ gatespenning (beskytter MOSFET) |

| D5 | Diode | UF4007 | DO-41 | 1 | 146-7590 | 700-4287 | Snubber-diode; leder lekkinduktansenergi til snubber-nettverket |

| R1 | Motstand | 1 kΩ, 0.25 W | AXIAL-0.3 | 1 | 933-1520 | 707-7694 | Begrenser strømmen fra tilbakekoblingsvikling til gate |

| R2 | Motstand | 10 kΩ, 0.25 W | AXIAL-0.3 | 1 | 933-1520 | 707-7694 | Snubber-motstand; demper oscillasjoner |

| R11 | Motstand | 1 kΩ, 10 W | Trådviklet | 1 | 247-8500 | 160-2160 | Utladningsmotstand; trygg utlading av kondensator |

| R12 | Motstand | 220 kΩ, 1 W | AXIAL-0.5 | 1 | 933-1560 | 707-7740 | Strømbegrenser for LED |

| S1, S2 | Trykknapp | SPST momentan | Panel | 2 | 108-2240 | 734-7221 | S1: ladeknapp, S2: utladningsknapp |

| S3 | Vippebryter | SPST | Panel | 1 | 108-2260 | 734-7243 | Hovedstrømbryter |

| F1 | Sikring | 2 A, 250 V | 5×20 mm | 1 | 123-4567 | 700-1234 | Beskytter batterikretsen mot kortslutning |

| T1 | Transformator | E20/10/6 kjerne | Custom | 1 | - | - | Ferrittkjerne, 0.5/0.2/0.1 mm tråd; viklinger 10:200:5 |

| G1 | Gnistgap | Wolframelektroder | Custom | 1 | - | - | 1.6 mm TIG-elektroder; selvutløsende ved \~450 V |

| L1 | Spole | 10 AWG emaljert tråd | Custom | 1 | - | - | Flat spiral, 4 vindinger, \~2.5 µH |

| Batteri | 9V batteriklemmer | Snap-kontakt | - | 5 | 165-0672 | 455-8300 | For 5 stk. 9V-batterier i serie (45 V) |



\*\*Merk:\*\* For høyere repetisjonsrate kan du bytte til en 5S LiPo-pakke (18.5 V) og justere transformatorens viklingsforhold tilsvarende.



