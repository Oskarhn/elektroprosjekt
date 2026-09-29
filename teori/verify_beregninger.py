#!/usr/bin/env python3
"""
Verifikasjonsskript for EMP-generatorberegninger.
Kjør med: python3 verify_calculations.py
"""

import math

# Designparametere
C = 100e-6          # F
V0 = 450.0          # V
N = 4               # vindinger
r_i = 10e-3         # m (indre radius)
r_o = 50e-3         # m (ytre radius)
r_avg = (r_i + r_o) / 2  # m
w = r_o - r_i       # m

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

# Magnetfelt i sentrum (sum over vindinger)
# Antar jevnt fordelte radier
radii = [r_i + (r_o - r_i) * (k - 0.5) / N for k in range(1, N+1)]
B0 = sum([(4e-7 * math.pi * I_peak) / (2 * r) for r in radii])
print(f"Estimert B(0): {B0:.3f} T")

# Pickup-spenning (forenklet)
N_pickup = 5
A_pickup = 1e-4  # m^2
z = 0.2  # m
# Beregn B(z) og dB/dt
Bz = sum([(4
