# Rama B: se siembra 852 nm, se genera 794 nm

**Estado:** hay datos y análisis de fluorescencia en [`Fluorescencia/`](Fluorescencia/) y de la detección directa a 794 nm en [`Deteccion_794/`](Deteccion_794/), donde no se detecta señal porque el fondo es luz de 852 y 822 nm que el monocromador no rechaza. [`Teoria/`](Teoria/) solo tiene la estructura, con la misma organización que la [Rama A](../Rama_A/).

El bombeo de 822 nm lleva los átomos de 6S1/2 a 8S1/2 por absorción de dos fotones, y la semilla de 852 nm (6S1/2 ↔ 6P3/2) cierra el lazo. El medio radía el campo de 794 nm (8S1/2 → 6P3/2) en la dirección de ajuste de fase, $2k_1 - k_3 = k_2$, hacia adelante.

- Coherencia que radía: $\rho_{cb}^{(3)}$. Término paramétrico: $\propto \tilde E_1^2\tilde E_3^*$.
- Susceptibilidad paramétrica:

$$\chi^{(3)}_B = -\frac{N|\mu_{ba}|^2|\mu_{cb}|^2}{\varepsilon_0\hbar^3\,(\Delta_1 - i\gamma_{ba})(\Delta_2 - i\gamma_{ca})(\delta_2 - i\gamma_{cb})}$$

- **Resonancia de la señal:** $\delta_2 - i\gamma_{cb} = (\Delta_2 - \Delta_3) - i\gamma_{cb}$.
- **Absorción:** a primer orden la señal de 794 nm no se absorbe, porque acopla dos niveles vacíos. Quien se absorbe es la semilla de 852 nm, con $\chi^{(1)}(\omega_3) \propto 1/(\Delta_3 - i\gamma_{ba})$, de modo que $\tilde E_3$ decae a lo largo de la celda.
- Perillas del laboratorio: $\omega_1$ (822) y $\omega_3$ (852). Con ellas, $\Delta_2 = \omega_{ca} - 2\omega_1$, $\Delta_3 = \omega_{ba} - \omega_3$, $\omega_2 = 2\omega_1 - \omega_3$ y $\delta_2 = \Delta_2 - \Delta_3$.

La derivación está en el [README principal](../README.md#rama-b-se-genera-794-nm).

## Carpetas

| Carpeta | Contenido | Estado |
|---|---|---|
| [`Teoria/`](Teoria/) | Evaluación numérica de $\chi^{(3)}_B$, propagación con semilla absorbida y promedio Doppler | Pendiente |
| [`Fluorescencia/`](Fluorescencia/) | Fluorescencia azul (PMT): barridos del 822 solo, del 852 solo y del 852 con el 822 fijo | Hecho |
| [`Deteccion_794/`](Deteccion_794/) | Detección directa hacia adelante a 794 nm (monocromador + SPCM), con el 852 barrido y el 822 fijo | Medido: sin señal por encima del fondo de 852 y 822 nm |

## Pendiente

- Agregar $\gamma_{cb}$ a [`constants.py`](../constants.py). En el límite puramente radiativo, $\gamma_{cb} = \gamma_{ba} + \gamma_{ca}$.
- Calibrar el monocromador en 794 nm y bloquear el 822 y el 852 antes de la fibra con un filtro interferencial (ver [`Deteccion_794/`](Deteccion_794/)).
- Tener en cuenta el efecto abierto de una semilla resonante con la D2, que puebla 6P3/2 y va más allá del orden perturbativo usado.
