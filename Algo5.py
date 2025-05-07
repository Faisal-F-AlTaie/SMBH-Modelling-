import numpy as np
import matplotlib.pyplot as plt


# Constants
G = 6.6743e-11  # Gravitational constant (m^3/kg/s^2)
hbar = 1.0546e-34  # Reduced Planck constant (J s)
c = 2.998e8  # Speed of light (m/s)
kB = 1.381e-23  # Boltzmann constant (J/K)


# Inputs
M = float(input('input Mass (kg): '))  # Mass of the black hole (kg)
t = np.linspace(0, 1e50, num=1000)  # time range
T_H = hbar*c**3/(8*np.pi*kB*G*M)  # Hawking temperature


# Calculate the black hole evaporation rate
dMdt = -(1/(2560*np.pi**2))*(hbar*c**4/(G**2*M**2))  # Stefan-Boltzmann law
t_evap = (5120*np.pi*G**2*M**3)/(hbar*c**4)  # evaporation time


# Plot the results
plt.plot(t, dMdt*np.ones(len(t)))
plt.xlabel('Time (s)')
plt.ylabel('Evaporation rate (kg/s)')
plt.show()


print("Black hole evaporation time: ", t_evap, "s")