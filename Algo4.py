import numpy as np
import matplotlib.pyplot as plt


# Constants
G = 6.6743e-11  # Gravitational constant (m^3/kg/s^2)
hbar = 1.0546e-34  # Reduced Planck constant (J s)
c = 2.998e8  # Speed of light (m/s)
kB = 1.381e-23  # Boltzmann constant (J/K)


# Inputs
M = float(input('input Mass (kg): '))# Mass of the black hole (kg)
r_s = 2*G*M/c**2  # Schwarzschild radius of the black hole
t = np.linspace(0, 1e20, num=1000)  # time range
phi_out = lambda t: np.sin(2*np.pi*t*1e-15)  # outgoing wave function
phi_in = lambda r: np.exp(-r/r_s)/(np.sqrt(4*np.pi*r**3))  # ingoing wave function


# Calculate the inner product of the outgoing and ingoing wave functions
inner_prod = lambda r, t: np.abs(np.conj(phi_in(r))*phi_out(t))**2


# Calculate the mutual information
I = lambda r, t: -(kB/hbar)*inner_prod(r, t)*np.log(inner_prod(r, t))


# Plot the results
R, T = np.meshgrid(np.linspace(r_s, 10*r_s, num=100), t)
I_vals = I(R, T)
plt.contourf(R, T, I_vals, levels=50)
plt.colorbar()
plt.xlabel('r')
plt.ylabel('t')
plt.show()