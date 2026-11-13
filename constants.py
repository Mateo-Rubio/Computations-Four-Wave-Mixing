import warnings

import numpy as np

e_a0 = 8.4783536198e-30   # unidad atómica de momento dipolar, e*a0 [C*m] (CODATA 2022)

cte = {
    # ---------- Constantes fundamentales ----------
    "c[m/s]":       299792458,
    "hbar[J*s]":    1.054571817e-34,
    "kB[J/K]":      1.380649e-23,
    "eps0[F/m]":    8.8541878188e-12,
    "m_Cs[kg]":     2.20693935795e-25,
    "T[K]":         296,                      # temperatura de la velocidad térmica u (cálculos con Doppler)
    "e_a0[C*m]":    e_a0,                     # unidad atómica de momento dipolar, e*a0 (CODATA 2022)
    # ---------- Frecuencias de transición (centroides, sin hiperfina) ----------
    "nu_ba[Hz]":    351.72571847490013e12,    # 6S1/2 -> 6P3/2 (línea D2). Fuente: D. A. Steck, Cesium D Line Data
    "nu_ca[Hz]":    729.0097990179224e12,     # 6S1/2 -> 8S1/2, centroide. Fuente: Wu et al., Opt. Lett. 38, 3186 (2013)
    # Líneas hiperfinas de dos fotones 6S1/2 -> 8S1/2 (solo como referencia, no se usan en ningún cálculo).
    # La transición de dos fotones S -> S solo tiene líneas con ΔF = 0. El modelo usa el centroide nu_ca,
    # de modo que en el experimento Δ2 se mide respecto de la línea en la que se trabaja.
    # Fuente: Wu et al., Opt. Lett. 38, 3186 (2013) (ver el bloque de líneas hiperfinas al final del archivo).
    #   F=3 -> F=3:  729.014477 THz
    #   F=4 -> F=4:  729.006161 THz
    # ---------- Decaimientos ----------
    "gamma_ba[rad/s]": np.pi*5.2227e6,        # Gamma_D2/2, Gamma_D2 = 2pi x 5.2227 MHz. Fuente: D. A. Steck, Cesium D Line Data
                                              # Hipótesis: gamma_ba = Gamma_D2/2 es el límite radiativo, sin colisiones.
    "tau_8S[s]":       104e-9,                # Fuente: G. Alessandretti, F. Chiarini, G. Gorini y F. Petrucci,
                                              # Opt. Commun. 20, 289 (1977)
    # ---------- Momento dipolar de la D2 ----------
    "d_D2[C*m]":    6.324*e_a0,               # <6S1/2||er||6P3/2> = 6.324 e a0, valor medido por Rafac et al., tomado de
                                              # Sieradzan et al., arXiv:physics/0308092, Tabla I.
                                              # Elemento reducido en la convención simétrica, la misma de d_8S_6P32.
    # ---------- Momento dipolar 8S1/2 <-> 6P3/2 (794 nm) ----------
    "d_8S_6P32[C*m]": 1.4618*e_a0,              # <8S1/2||er||6P3/2> = 1.4618 e a0, cálculo SD all-order
                                                # (Sieradzan et al., arXiv:physics/0308092, Tabla III, columna SD).
                                                # Elemento reducido en la convención simétrica, igual que d_D2.
    # ---------- Celda ----------
    "L_celda[m]":   0.0718,                   # longitud de la celda de Cs: valor del PDF, por confirmar con el laboratorio
}
# gamma_ca = Gamma_c/2 = 1/(2 tau_8S): límite radiativo. La coherencia c-a decae a la mitad de la tasa
# total de |c>, porque |a> no decae.
cte["gamma_ca[rad/s]"] = 1/(2*cte["tau_8S[s]"])
# Límite radiativo: gamma_cb = (Gamma_c + Gamma_b)/2 = gamma_ca + gamma_ba.
cte["gamma_cb[rad/s]"] = cte["gamma_ca[rad/s]"] + cte["gamma_ba[rad/s]"]

c, hbar, kB, eps0 = cte["c[m/s]"], cte["hbar[J*s]"], cte["kB[J/K]"], cte["eps0[F/m]"]
g_ba, g_ca, g_cb = cte["gamma_ba[rad/s]"], cte["gamma_ca[rad/s]"], cte["gamma_cb[rad/s]"]

# Tasa de decaimiento de población |b> -> |a>  [rad/s]
# En el límite radiativo Gamma_ab = Gamma_D2 = 2 gamma_ba, de modo que el factor 2 gamma_ba/Gamma_ab
# de rho_bb^(2) vale 1.
G_ab = 2*g_ba

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
# |mu_ba|^2 = |<6S1/2||er||6P3/2>|^2/(2J_b+1) = |<...>|^2/4, con J_b = 3/2 el nivel superior: con él, la emisión
# espontánea w_ba^3 |mu_ba|^2/(3 pi eps0 hbar c^3) reproduce Gamma_D2 = 2 g_ba.
mu_ba = cte["d_D2[C*m]"]/2

# Momento dipolar efectivo de |b> <-> |c> (8S1/2 <-> 6P3/2, 794 nm)  [C*m]
# Misma convención que mu_ba: |mu_cb|^2 = |<8S1/2||er||6P3/2>|^2/(2J_c+1), con J_c = 1/2 el nivel superior,
# de modo que w_cb^3 |mu_cb|^2/(3 pi eps0 hbar c^3) es la tasa parcial A(8S1/2 -> 6P3/2).
mu_cb = cte["d_8S_6P32[C*m]"]/np.sqrt(2)

# Longitud física de la celda  [m]
# Se usa para la absorción lineal de la semilla a lo largo de toda la celda. La longitud de la región de
# interacción (del orden del parámetro confocal de los haces) es otra cantidad y no se define aquí.
L_celda = cte["L_celda[m]"]

T_FUSION_CS = 28.44   # punto de fusión del Cs [°C]

def n_Cs(T):
    """Densidad del vapor saturado de Cs [m^-3], con T en °C.

    Usa la presión de vapor sobre cesio LÍQUIDO de D. A. Steck, Cesium D Line Data,
    tal como aparece en la ec. (4.2) de la monografía:

        log10(Pv) = 8.22127 - 4006.048/T - 0.00060194 T - 0.19623 log10(T),

    con Pv en Torr y T en kelvin, y la densidad del gas ideal n = Pv/(kB T), ec. (4.3).
    Solo vale por encima del punto de fusión, 28.44 °C. Por debajo de 28.44 °C hace
    falta la expresión de la fase sólida, que no está implementada."""
    if np.any(np.asarray(T) < T_FUSION_CS):
        warnings.warn(
            f"n_Cs: hay temperaturas por debajo de {T_FUSION_CS} °C (punto de fusión del Cs). "
            "La expresión usada es la del Cs líquido; por debajo de ese valor hace falta "
            "la expresión de la fase sólida.", stacklevel=2)
    T_K = T + 273.15
    log_p_torr = 8.22127 - 4006.048/T_K - 0.00060194*T_K - 0.19623*np.log10(T_K)
    p = (101325/760) * 10**log_p_torr  # Pa; 1 Torr = 101325/760 Pa
    return p/(kB*T_K)                  # m^-3


if __name__ == "__main__":
    # Comprobación: la emisión espontánea con mu_ba, dividida entre 2, debe reproducir g_ba.
    g_mu = w_ba**3 * mu_ba**2 / (3*np.pi*eps0*hbar*c**3) / 2
    print(f"w_ba^3 |mu_ba|^2/(3 pi eps0 hbar c^3)/2 = {g_mu:.6e} rad/s")
    print(f"g_ba                                    = {g_ba:.6e} rad/s")
    print(f"diferencia relativa                     = {(g_mu - g_ba)/g_ba:.3e}")

# ---------- Líneas hiperfinas en las que se trabaja (identificación experimental) ----------
# El modelo usa centroides, pero en el laboratorio cada láser se sintoniza a una
# línea hiperfina concreta. Longitudes de onda en el vacío; el medidor resuelve
# 0.0001 nm (~44 MHz a 822 nm, ~41 MHz a 852 nm).
#
# Bombeo (822 nm), dos fotones, solo DeltaF = 0:
#   6S1/2 F=4 -> 8S1/2 F=4 : 822.46893 nm (calculada)  |  medida: 822.4689 nm
#   6S1/2 F=3 -> 8S1/2 F=3 : 822.45955 nm (calculada)  |  no se usa
#   Calculadas como c/nu, con nu = frecuencia del láser (la mitad de la de dos fotones)
#   de Wu et al., Opt. Lett. 38, 3186 (2013).
#
# Semilla (852 nm), línea D2 desde 6S1/2 F=4 (los tres picos del barrido):
#   F=4 -> F'=5 : 852.3564 nm (calculada)  |  medida: 852.3565 nm
#   F=4 -> F'=4 : 852.3570 nm (calculada)  |  medida: PENDIENTE
#   F=4 -> F'=3 : 852.3575 nm (calculada)  |  medida: 852.3575 nm
#   (Las líneas desde F=3 estarían en ~852.335 nm, lejos de lo medido.)
#   Calculadas con el centroide de la D2 y los desplazamientos hiperfinos de
#   6S1/2 y 6P3/2 de Steck, Cesium D Line Data.
#
# Escalera efectiva: |a> = 6S1/2 F=4,  |b> = 6P3/2 F',  |c> = 8S1/2 F=4.
# F=4 -> F'=5 es la transición más conveniente para la semilla: desde F'=5 el átomo
# solo decae a F=4 (transición cerrada), mientras que desde F'=4 o F'=3 puede caer a
# F=3 y dejar de interactuar con los láseres (bombeo óptico hiperfino).
# En el experimento, Delta2 = 0 corresponde a 822.4689 nm, y Delta3 = 0 a la línea de
# la semilla que se use (preferiblemente F=4 -> F'=5, 852.3564 nm).