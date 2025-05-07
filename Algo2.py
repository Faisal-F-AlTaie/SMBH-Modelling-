import numpy as np
import matplotlib.pyplot as plt


# Constants
G = 6.6743e-11  # Gravitational constant (m^3/kg/s^2)
hbar = 1.0546e-34  # Reduced Planck constant (J s)
c = 2.998e8  # Speed of light (m/s)
kB = 1.381e-23  # Boltzmann constant (J/K)


# Inputs
M = float(input('input Mass (kg): '))  # Mass of the black hole (kg)
r_s = 2*G*M/c**2  # Schwarzschild radius of the black hole
r = np.linspace(r_s, 10*r_s, 1000)  # radial coordinate
omega = np.linspace(1e-20, 1e-19, 1000)  # frequency range
T_H = hbar*c**3/(8*np.pi*kB*G*M)  # Hawking temperature


# Calculate the potential energy
V = -G*M/r + (hbar*omega)/(np.exp(hbar*omega/(kB*T_H))-1)  # potential energy


# Calculate the probability of pair creation
P = np.exp(-2*V/(hbar*omega))  # pair creation probability


# Calculate the particle creation rate
Gamma = (hbar*omega**3)/(2*np.pi*c**2)*P  # particle creation rate


# Plot the results
plt.plot(omega, Gamma)
plt.xlabel('Frequency')
plt.ylabel('Particle creation rate')
plt.show()