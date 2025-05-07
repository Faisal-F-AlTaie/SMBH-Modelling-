import numpy as np
import matplotlib.pyplot as plt


# Constants
G = 6.6743e-11  # Gravitational constant (m^3/kg/s^2)
hbar = 1.0546e-34  # Reduced Planck constant (J s)
c = 2.998e8  # Speed of light (m/s)
kB = 1.381e-23  # Boltzmann constant (J/K)


# Inputs
M = float(input('input Mass (kg): '))  # Mass of the black hole (kg)
Q = 0  # Electric charge of the black hole (C)
J = 0  # Angular momentum of the black hole (kg m^2/s)
T_H = hbar*c**3/(8*np.pi*kB*G*(M + np.sqrt(M**2 - (Q**2 + J**2)/c**2)))  # Hawking temperature


# Calculate the radiation spectrum
nu = np.logspace(0, 30, num=10000)  # frequency range
B_nu = (2*hbar*nu**3/c**2)*(1/(np.exp(hbar*nu/(kB*T_H))-1))  # Planck distribution


# Plot the results
plt.loglog(nu, B_nu)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Radiance (W/m^2/Hz/sr)')
plt.show()