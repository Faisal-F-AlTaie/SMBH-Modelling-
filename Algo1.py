import numpy as np
import matplotlib.pyplot as plt

# Define constants
hbar = 1.05457e-34   # Planck constant divided by 2*pi (in J s)
c = 299792458       # Speed of light (in m/s)
kB = 1.38065e-23    # Boltzmann constant (in J/K)
G = 6.67430e-11     # Gravitational constant (in m^3/kg/s^2)
M = float(input('input Mass (kg): '))       # Mass of the black hole (in kg)
Rs = 2 * G * M / c**2  # Schwarzschild radius (in m)

# Define the radial coordinate
r = np.linspace(Rs, 10*Rs, 1000)

# Calculate the stress-energy tensor components
T00 = c**4 / (8 * np.pi * G) * (1 / r**2 - 2 * Rs / r**3)
T11 = c**4 / (8 * np.pi * G) * (1 / r**2 + 2 * Rs / r**3)
T22 = c**4 / (8 * np.pi * G) * (1 / r**2 + Rs / r**3)
T33 = c**4 / (8 * np.pi * G) * (1 / r**2 + Rs / r**3)

# Plot the stress-energy tensor components
fig, ax = plt.subplots()
ax.plot(r/Rs, T00, label='T00')
ax.plot(r/Rs, T11, label='T11')
ax.plot(r/Rs, T22, label='T22')
ax.plot(r/Rs, T33, label='T33')
ax.set_xlabel('r/Rs')
ax.set_ylabel('T')
ax.legend()
plt.show()

# Define the frequency range
nu = np.logspace(0, 20, 1000)

# Calculate the radiation spectrum
omega = 2 * np.pi * nu
T = hbar * omega / (kB * 1.5e9)  # Temperature in Kelvin
Gamma = (hbar * omega**3) / (2 * np.pi * c**2) * (1 / (np.exp(hbar * omega / (kB * T)) - 1))

# Plot the radiation spectrum
fig, ax = plt.subplots()
ax.loglog(nu, Gamma)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Spectral Radiance (W/m^2/Hz)')
plt.show()