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
    # ---------- Momento dipolar de la D2 ----------
    "d_D2[C*m]":    3.7971e-29,               # elemento reducido <J=1/2||er||J'=3/2> (Steck, Cesium D Line Data)
    # ---------- Celda ----------
    "L_celda[m]":   0.075,                    # longitud de la celda de Cs (VERIFICAR con la celda del laboratorio)
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

# Momento dipolar efectivo del sistema de dos niveles |a> <-> |b> (D2)  [C*m]
# |mu_ba|^2 = (2J+1)/(2J'+1) |<J||er||J'>|^2 = |<J||er||J'>|^2/2: con él, la emisión
# espontánea w_ba^3 |mu_ba|^2/(3 pi eps0 hbar c^3) reproduce Gamma_D2 = 2 g_ba.
mu_ba = cte["d_D2[C*m]"]/np.sqrt(2)

# Longitud de la celda  [m]
L_celda = cte["L_celda[m]"]

def n_Cs(T):
    """Densidad de Cs [m^-3], Cs líquido. Alcock, Itkin y Horrigan,
    Can. Metall. Q. 23, 309 (1984). T en °C, válida de 28.44 °C a ~277 °C."""
    T_K = T + 273.15
    log_p_atm = 8.232 - 4062/T_K - 1.3359*np.log10(T_K)
    p = 101325 * 10**log_p_atm        # Pa
    return p/(kB*T_K)                  # m^-3
