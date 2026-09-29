#!/usr/bin/env python3
"""
Verifikasjon av EMP-generatorberegninger.
Kjør: python3 verify_beregninger.py
"""
import math

# Designparametere
C = 100e-6          # F
V0 = 450.0          # V
N = 4               # vindinger
# Spolegeometri: diametre til senter av innerste/ytterste vinding
d_i = 20e-3         # m
d_o = 100e-3        # m
r_i = d_i / 2       # 10 mm
r_o = d_o / 2       # 50 mm
r_avg = (r_i + r_o) / 2
w = r_o - r_i

# Wheelers formel (tommer)
r_inch = r_avg * 39.3701
w_inch = w * 39.3701
L_wheeler = (r_inch**2 * N**2) / (8*r_inch + 11*w_inch) * 1e-6  # H
print(f"Estimert induktans (Wheeler): {L_wheeler*1e6:.2f} µH")

# Energi
E = 0.5 * C * V0**2
print(f"Lagret energi: {E:.2f} J")

# Karakteristisk impedans
Z0 = math.sqrt(L_wheeler / C)
print(f"Karakteristisk impedans: {Z0:.3f} Ohm")

# Ideell toppstrøm
I_peak_ideal = V0 / Z0
print(f"Ideell toppstrøm: {I_peak_ideal:.0f} A")

# Dempet RLC (antatt R)
R_assumed = 0.1  # Ohm
alpha = R_assumed / (2 * L_wheeler)
omega0 = 1 / math.sqrt(L_wheeler * C)
omega_d = math.sqrt(omega0**2 - alpha**2)
f_d = omega_d / (2 * math.pi)
print(f"Antatt R: {R_assumed} Ohm")
print(f"alpha: {alpha:.0f} 1/s")
print(f"omega0: {omega0:.0f} rad/s")
print(f"omega_d: {omega_d:.0f} rad/s")
print(f"f_d: {f_d:.1f} Hz")

# Første topptid
t_p = math.atan(omega_d / alpha) / omega_d
print(f"Første topptid: {t_p*1e6:.1f} µs")

# Toppstrøm
I_peak = (V0 / (omega_d * L_wheeler)) * math.exp(-alpha * t_p) * math.sin(omega_d * t_p)
print(f"Estimert toppstrøm (R=0.1): {I_peak:.0f} A")

# Periode og envelope
T_d = 1 / f_d
tau = 1 / alpha
print(f"Periode: {T_d*1e6:.1f} µs")
print(f"Envelope tidskonstant: {tau*1e6:.1f} µs")

# Magnetfelt i sentrum (sum over vindinger)
# Jevnt fordelte radier (senter av hver vinding)
radii = [r_i + (r_o - r_i) * (k - 0.5) / N for k in range(1, N+1)]
print(f"Vindingsradier (mm): {[r*1e3 for r in radii]}")
B0 = sum([(4e-7 * math.pi * I_peak) / (2 * r) for r in radii])
print(f"Estimert B(0): {B0:.3f} T")

# Pickup-spenning (analytisk derivert)
N_pickup = 5
d_pickup = 0.02  # m diameter
A_pickup = math.pi * (d_pickup/2)**2
z = 0.2  # m avstand
# Beregn B(z) og dB/dt
Bz = sum([(4e-7 * math.pi * I_peak * r**2) / (2 * (r**2 + z**2)**1.5) for r in radii])
print(f"Estimert B(z={z} m): {Bz*1e3:.2f} mT")

# Maksimal di/dt (initial)
di_dt_max = V0 / L_wheeler  # t=0
print(f"Maks |di/dt| (initial): {di_dt_max:.2e} A/s")
# dB/dt = (mu0/2) * sum(r_k^2/(r_k^2+z^2)^1.5) * di/dt
geom_factor_z = sum([r**2 / (r**2 + z**2)**1.5 for r in radii]) * (4e-7 * math.pi / 2)
max_dB_dt = geom_factor_z * di_dt_max
print(f"Maks dB/dt ved z={z} m: {max_dB_dt:.2e} T/s")
# Pickup-spenning
V_pickup_max = N_pickup * A_pickup * max_dB_dt
print(f"Estimert pickup-spenning (z={z} m): {V_pickup_max*1e3:.1f} mV")

# Utladningsmotstand
R_discharge = 1000.0  # Ohm
tau_rc = R_discharge * C
print(f"Utladnings RC-tid: {tau_rc:.2f} s")
# Initial effekt
P_initial = V0**2 / R_discharge
print(f"Initial effekt i R11: {P_initial:.1f} W")

# Bleeder
R_bleed = 1e6
P_bleed = V0**2 / R_bleed
print(f"Bleeder effekt: {P_bleed:.3f} W")

# LED-gren
R_led = 220e3
I_led = V0 / R_led
P_led_total = V0 * I_led
print(f"LED-gren strøm: {I_led*1e3:.2f} mA, effekt: {P_led_total:.3f} W")

# Total kontinuerlig last
P_cont = P_bleed + P_led_total
print(f"Total kontinuerlig last ved 450V: {P_cont:.3f} W")

# Transformator (E20/10/6, 0.1 mm gap)
AL = 345e-9  # H/t^2
Np = 10
Ns = 200
Lp = AL * Np**2
Ls = AL * Ns**2
print(f"Transformator Lp: {Lp*1e6:.1f} µH, Ls: {Ls*1e3:.1f} mH")

# Diodespenning
V_rev = V0 + (Ns/Np) * 45
print(f"Diodespenning (revers): {V_rev:.0f} V")
