import numpy as np
cte = {
    # ---------- Constantes fundamentales ----------
    "c[m/s]":       299792458,
    "hbar[J*s]":    1.054571817e-34,
    "kB[J/K]":      1.380649e-23,
    "eps0[F/m]":    8.8541878188e-12,
    "m_Cs[kg]":     2.20693935795e-25,
    "T[K]":         296,
    # ---------- Frecuencias de transición (centroides, sin hiperfina) ----------
    "nu_ba[Hz]":    351.72571847490013e12,    # 6S1/2 -> 6P3/2 (línea D2)
    "nu_ca[Hz]":    729.0097990179224e12,     # 6S1/2 -> 8S1/2
    # ---------- Decaimientos ----------
    "gamma_ba[rad/s]": np.pi*5.2227e6,        # Gamma_D2/2, Gamma_D2 = 2pi x 5.2227 MHz
    "tau_8S[s]":       104e-9,
}
cte["gamma_ca[rad/s]"] = 1/(2*cte["tau_8S[s]"])

c, hbar, kB, eps0 = cte["c[m/s]"], cte["hbar[J*s]"], cte["kB[J/K]"], cte["eps0[F/m]"]
g_ba, g_ca = cte["gamma_ba[rad/s]"], cte["gamma_ca[rad/s]"]

# Frecuencias angulares de transición  [rad/s]
w_ba = 2*np.pi*cte["nu_ba[Hz]"]
w_ca = 2*np.pi*cte["nu_ca[Hz]"]
w_cb = w_ca - w_ba                       # 8S1/2 -> 6P3/2

# Longitudes de onda (vacío) y vectores de onda en resonancia
lmd1 = 2*np.pi*c/(w_ca/2)                # 822 nm: cada fotón lleva la mitad de w_ca
lmd2 = 2*np.pi*c/w_cb                    # 794 nm
lmd3 = 2*np.pi*c/w_ba                    # 852 nm
k1, k2, k3 = 2*np.pi/lmd1, 2*np.pi/lmd2, 2*np.pi/lmd3

# Velocidad térmica más probable de los átomos de Cs  [m/s]
u = np.sqrt(2*kB*cte["T[K]"]/cte["m_Cs[kg]"])
