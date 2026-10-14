# Mezclado de cuatro ondas en vapor de cesio

Cálculos y análisis de datos de la monografía *Estudio teórico y experimental del mezclado de cuatro ondas en vapor de cesio a través de la absorción de dos fotones* (Mateo Rubio Hernández; directora: Mayerlin Nuñez, Ph.D.; Departamento de Física, Universidad de los Andes).

## El sistema

El cesio se modela como una escalera de tres niveles excitada por tres campos:

| Nivel | Estado | Campo | Transición |
|---|---|---|---|
| \|a⟩ | 6S1/2 | E1, 822 nm (bombeo) | a → c por absorción de dos fotones |
| \|b⟩ | 6P3/2 | E2, 794 nm | c ↔ b |
| \|c⟩ | 8S1/2 | E3, 852 nm (línea D2) | b ↔ a |

La conservación de la energía, $2\omega_1 = \omega_2 + \omega_3$, y el ajuste de fase con haces copropagantes en vacío, $2k_1 = k_2 + k_3$, permiten dos procesos de FWM. El proyecto implementa ambos, uno como **Rama A** y otro como **Rama B**:

| | **Rama A** | **Rama B** |
|---|---|---|
| Campos de entrada | 822 (bombeo) + 794 (semilla) | 822 (bombeo) + 852 (semilla) |
| Señal generada | 852 nm | 794 nm |
| Coherencia que radía | $\rho_{ba}^{(3)}$ | $\rho_{cb}^{(3)}$ |
| Término paramétrico | $\propto \tilde E_1^2\,\tilde E_2^*$ | $\propto \tilde E_1^2\,\tilde E_3^*$ |
| Resonancia de la señal | $\Delta_3 - i\gamma_{ba}$ | $\delta_2 - i\gamma_{cb}$ |
| Absorción lineal | la **señal** de 852 nm se reabsorbe | la señal de 794 nm no se absorbe a primer orden; se absorbe la **semilla** de 852 nm |
| Perillas del laboratorio | $\omega_1$ (822) y $\omega_2$ (794) | $\omega_1$ (822) y $\omega_3$ (852) |
| Estado | teoría y experimento en curso | teoría derivada; falta implementarla numérica y experimentalmente |

## Teoría

### Desintonías

$$\Delta_1 = \omega_{ba} - \omega_1, \qquad \Delta_2 = \omega_{ca} - 2\omega_1, \qquad \Delta_3 = \omega_{ba} - \omega_3, \qquad \delta_2 = \omega_{cb} - \omega_2 = \Delta_2 - \Delta_3 .$$

- $\Delta_1$: el bombeo frente a 6P3/2. Está muy lejos de resonancia ($\Delta_1/2\pi \approx -12.8$ THz), así que $(\Delta_1 - i\gamma_{ba})$ es grande, casi real y casi constante.
- $\Delta_2$: la resonancia de dos fotones 6S → 8S, con ancho $\gamma_{ca}$.
- $\Delta_3$: el campo de 852 nm frente a la D2, con ancho $\gamma_{ba}$.
- $\delta_2$: el campo de 794 nm frente a 8S → 6P3/2, con ancho $\gamma_{cb}$.

### Segundo orden: la parte común

La ecuación de Liouville se resuelve perturbativamente desde $\rho^{(0)}_{aa} = 1$. A segundo orden, los dos caminos hacia \|c⟩ (822 + 822 y 852 + 794) oscilan a $2\omega_1$, así que sus amplitudes se suman:

$$\rho_{ca}^{(2)} = \frac{\mu_{cb}\mu_{ba}}{\hbar^2}\left[\frac{\tilde E_1^2}{(\Delta_1 - i\gamma_{ba})(\Delta_2 - i\gamma_{ca})} + \frac{\tilde E_2\tilde E_3}{(2\Delta_1 - \Delta_3 - i\gamma_{ba})(\Delta_2 - i\gamma_{ca})} + \frac{\tilde E_2\tilde E_3}{(\Delta_3 - i\gamma_{ba})(\Delta_2 - i\gamma_{ca})}\right] e^{-i2\omega_1 t}$$

Esta coherencia alimenta ambas ramas. A tercer orden, las dos susceptibilidades paramétricas comparten los factores del bombeo y de dos fotones, y solo cambia el último factor, que es la resonancia de la señal generada:

$$\chi^{(3)} \propto \frac{1}{\underbrace{(\Delta_1 - i\gamma_{ba})}_{\text{bombeo}}\ \underbrace{(\Delta_2 - i\gamma_{ca})}_{\text{dos fotones}}\ \underbrace{(\text{resonancia de la señal})}_{\text{cambia con la rama}}}$$

### Rama A: se genera 852 nm

Coherencia a tercer orden a la frecuencia $\omega_3$:

$$\rho_{ba}^{(3)}\Big|_{\omega_3} = \frac{|\mu_{cb}|^2\mu_{ba}}{\hbar^3}\,\frac{1}{(\Delta_2 - i\gamma_{ca})(\Delta_3 - i\gamma_{ba})}\left[\frac{\tilde E_1^2\tilde E_2^*}{\Delta_1 - i\gamma_{ba}} + \frac{|\tilde E_2|^2\tilde E_3}{2\Delta_1 - \Delta_3 - i\gamma_{ba}} + \frac{|\tilde E_2|^2\tilde E_3}{\Delta_3 - i\gamma_{ba}}\right] e^{-i\omega_3 t}$$

**Término de resonancia de la señal:** $\Delta_3 - i\gamma_{ba}$. El primer término es el paramétrico, la fuente del FWM:

$$\chi^{(3)}_A(\omega_3;\omega_1,\omega_1,-\omega_2) = \frac{N|\mu_{ba}|^2|\mu_{cb}|^2}{\varepsilon_0\hbar^3\,(\Delta_1 - i\gamma_{ba})(\Delta_2 - i\gamma_{ca})(\Delta_3 - i\gamma_{ba})}$$

Los términos $\propto |\tilde E_2|^2\tilde E_3$ son la reacción del medio sobre su propia señal ($\chi^{(3)}_X$).

**Absorción de la señal.** A primer orden, el 852 nm acopla el fundamental poblado y se reabsorbe con el mismo denominador que realza la generación:

$$\chi^{(1)}(\omega_3) = \frac{N|\mu_{ba}|^2}{\varepsilon_0\hbar\,(\Delta_3 - i\gamma_{ba})}$$

**Propagación.** Con envolvente lenta y bombeo no agotado,

$$\frac{d\tilde E_3}{dz} = \frac{ik_3}{2}\chi_{ef}\tilde E_3 + \frac{ik_3}{2}\chi^{(3)}_P\tilde E_1^2\tilde E_2^*, \qquad \chi_{ef} \equiv \chi^{(1)}(\omega_3) + \chi^{(3)}_X|\tilde E_2|^2 ,$$

$$|\tilde E_3(L)|^2 = \left|\frac{\chi^{(3)}_P}{\chi_{ef}}\right|^2 |\tilde E_1|^4|\tilde E_2|^2\left[1 + e^{-2\kappa L} - 2e^{-\kappa L}\cos\beta L\right], \qquad \kappa = \frac{k_3\chi''}{2},\ \ \beta = \frac{k_3\chi'}{2}.$$

- Celda delgada ($\kappa L \ll 1$): $I_{852} \propto |\chi^{(3)}_P|^2 L^2$, que crece con $L^2$ y $N^2$.
- Celda gruesa ($\kappa L \gg 1$): $I_{852} \propto |\chi^{(3)}_P/\chi_{ef}|^2$. Satura (no depende de $L$ ni de $N$) y el factor $\Delta_3$ se cancela:

$$|\tilde E_3(L)|^2 \approx \frac{|\mu_{cb}|^4|\tilde E_1|^4|\tilde E_2|^2}{\hbar^4\,(\Delta_1^2 + \gamma_{ba}^2)(\Delta_2^2 + \gamma_{ca}^2)}$$

  En celda gruesa solo sobrevive la resonancia de dos fotones.

**Promedio Doppler.** Con $W(v) = e^{-v^2/u^2}/(\sqrt\pi\,u)$ y la función de dispersión del plasma $Z(\zeta)$:

$$\bar\chi^{(1)}(\omega_3) = \frac{N|\mu_{ba}|^2}{\varepsilon_0\hbar\,k_3u}Z(\zeta_b), \qquad \bar\chi^{(3)}_A = \frac{N|\mu_{ba}|^2|\mu_{cb}|^2}{\varepsilon_0\hbar^3(\Delta_1 - i\gamma_{ba})}\,\frac{1}{2k_1k_3u^2}\,\frac{Z(\zeta_a) - Z(\zeta_b)}{\zeta_a - \zeta_b},$$

$$\zeta_a = \frac{-\Delta_2 + i\gamma_{ca}}{2k_1u}, \qquad \zeta_b = \frac{-\Delta_3 + i\gamma_{ba}}{k_3u}.$$

### Rama B: se genera 794 nm

Coherencia a tercer orden a la frecuencia $\omega_2$:

$$\rho_{cb}^{(3)}\Big|_{\omega_2} = -\frac{|\mu_{ba}|^2\mu_{cb}}{\hbar^3}\,\frac{1}{(\delta_2 - i\gamma_{cb})(\Delta_2 - i\gamma_{ca})}\left[\frac{\tilde E_1^2\tilde E_3^*}{\Delta_1 - i\gamma_{ba}} + \frac{|\tilde E_3|^2\tilde E_2}{2\Delta_1 - \Delta_3 - i\gamma_{ba}} + \frac{|\tilde E_3|^2\tilde E_2}{\Delta_3 - i\gamma_{ba}}\right] e^{-i\omega_2 t}$$

**Término de resonancia de la señal:** $\delta_2 - i\gamma_{cb} = (\Delta_2 - \Delta_3) - i\gamma_{cb}$. Del término paramétrico $\propto \tilde E_1^2\tilde E_3^*$ sale la susceptibilidad

$$\chi^{(3)}_B(\omega_2;\omega_1,\omega_1,-\omega_3) = -\frac{N|\mu_{ba}|^2|\mu_{cb}|^2}{\varepsilon_0\hbar^3\,(\Delta_1 - i\gamma_{ba})(\Delta_2 - i\gamma_{ca})(\delta_2 - i\gamma_{cb})}$$

Los términos $\propto |\tilde E_3|^2\tilde E_2$ son la reacción del medio sobre la señal de 794 nm.

**Absorción.** A este orden, el 794 nm acopla dos niveles vacíos (c ↔ b), así que la señal **no se absorbe**. Quien se absorbe es la semilla de 852 nm, con el mismo $\chi^{(1)}(\omega_3) \propto 1/(\Delta_3 - i\gamma_{ba})$ de la Rama A. Por eso $\tilde E_3$ deja de ser constante a lo largo de la celda.

**Abierto:** la propagación de la Rama B (generación con una semilla que se atenúa), su promedio Doppler y el efecto de una semilla resonante que puebla 6P3/2, que va más allá de este orden perturbativo.

## Hoja de ruta por rama

### Rama A

| Parte | Estado | Dónde |
|---|---|---|
| χ⁽¹⁾ y χ⁽³⁾ del átomo en reposo, mapa en (Δ2, δ2), celda gruesa | Hecho | [`Rama_A/Teoria/`](Rama_A/Teoria/) |
| χ̄⁽¹⁾ con Doppler y factor Doppler de χ̄⁽³⁾ en (Δ2, Δ3) | Hecho | [`Rama_A/Teoria/`](Rama_A/Teoria/) |
| Evaluación completa de χ̄⁽³⁾ con Doppler y estructura hiperfina | Pendiente | — |
| Caracterización de los haces 822 y 852 nm | Hecho | [`Caracterizacion_Haces/`](Caracterizacion_Haces/) |
| Etapa 1, fluorescencia: pico de dos fotones y tres valles hiperfinos con el 794 | Hecho | [`Rama_A/Fluorescencia/`](Rama_A/Fluorescencia/) |
| Etapa 2, detección directa a 852 nm | Medido: sin señal por encima del fondo | [`Rama_A/Deteccion_852/`](Rama_A/Deteccion_852/) |
| Origen del fondo del canal B, calibración del monocromador, absorción en D2 (κ), barridos de Δ794 y de T | Pendiente | — |

### Rama B

| Parte | Estado | Dónde |
|---|---|---|
| $\rho_{cb}^{(3)}$ y $\chi^{(3)}_B$ | Derivados (expresiones de arriba) | [`Rama_B/`](Rama_B/) |
| Evaluación numérica de $\chi^{(3)}_B$ en el plano de las perillas (Δ2, Δ3) | Pendiente | [`Rama_B/Teoria/`](Rama_B/Teoria/) |
| Propagación con semilla de 852 nm absorbida y promedio Doppler | Pendiente | [`Rama_B/Teoria/`](Rama_B/Teoria/) |
| $\gamma_{cb}$ en `constants.py` | Pendiente. En el límite puramente radiativo, $\gamma_{cb} = \gamma_{ba} + \gamma_{ca}$ | — |
| Montaje: 822 + semilla de 852 nm copropagantes; detección hacia adelante a 794 nm (monocromador en 794 nm → SPCM), con el PMT lateral marcando Δ2 = 0 | Pendiente | [`Rama_B/Fluorescencia/`](Rama_B/Fluorescencia/), [`Rama_B/Deteccion_794/`](Rama_B/Deteccion_794/) |

## Estructura del repositorio

```
.
├── README.md
├── constants.py                    # única fuente de constantes físicas (ver abajo)
├── Caracterizacion_Haces/          # común: cintura e intensidad de los haces de 822 y 852 nm
│   ├── 822.py, 852.py, waist_both.py
│   └── data/{822nm,852nm}/         # perfiles z<pos>mm.xlsx del BeamMaster (se copian aparte)
├── Rama_A/                         # semilla 794 → señal 852
│   ├── Teoria/                     # χ(1) y χ(3) en reposo y con Doppler
│   ├── Fluorescencia/              # etapa 1: PMT con 822 solo y con 822 + 794
│   │   ├── 2Lasers.ipynb
│   │   ├── data/                   # canal A (6 columnas)
│   │   └── newdata/                # canales A y B (5 columnas)
│   └── Deteccion_852/              # etapa 2: monocromador a 852 nm + SPCM
│       ├── FWM.ipynb
│       └── data/2026-09-07/
└── Rama_B/                         # semilla 852 → señal 794 (todavía sin datos)
    ├── Teoria/
    ├── Fluorescencia/data/
    └── Deteccion_794/data/
```

Cada carpeta tiene su propio `README.md`. Ahí se explica en qué consiste el experimento o el cálculo, cómo se ajustan los datos, la estructura interna de los archivos de medida y el formato de sus nombres:

| Carpeta | README |
|---|---|
| Caracterización de haces | [`Caracterizacion_Haces/README.md`](Caracterizacion_Haces/README.md) |
| Rama A | [`Rama_A/README.md`](Rama_A/README.md) · [Teoría](Rama_A/Teoria/README.md) · [Fluorescencia](Rama_A/Fluorescencia/README.md) · [Detección a 852 nm](Rama_A/Deteccion_852/README.md) |
| Rama B | [`Rama_B/README.md`](Rama_B/README.md) · [Teoría](Rama_B/Teoria/README.md) · [Fluorescencia](Rama_B/Fluorescencia/README.md) · [Detección a 794 nm](Rama_B/Deteccion_794/README.md) |

## Cómo ejecutar

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install numpy scipy matplotlib pandas openpyxl ipykernel
```

Los notebooks se abren **desde su propia carpeta** (por ejemplo `cd Rama_A/Deteccion_852`). Cada uno agrega la raíz del repositorio a `sys.path` con `sys.path.append('../..')` para importar `constants.py`, y lee sus datos con rutas relativas (`data/...`). En Colab, primero hay que clonar el repositorio y luego hacer `%cd` a la subcarpeta. Los scripts de `Caracterizacion_Haces/` buscan sus datos en `data/` junto al script.

## Constantes globales

`constants.py` es la única fuente de las constantes. Para cambiar un valor (por ejemplo la temperatura `T[K]`), se edita ahí y todos los notebooks usan el nuevo valor.

### Diccionario `cte`

Las unidades van en el nombre de cada clave (todo en SI):

| Clave | Descripción |
|---|---|
| `c[m/s]` | Velocidad de la luz |
| `hbar[J*s]` | Constante de Planck reducida |
| `kB[J/K]` | Constante de Boltzmann |
| `eps0[F/m]` | Permitividad del vacío |
| `m_Cs[kg]` | Masa atómica del Cs |
| `T[K]` | Temperatura |
| `nu_ba[Hz]`, `nu_ca[Hz]` | Frecuencias de transición 6S1/2 → 6P3/2 (D2) y 6S1/2 → 8S1/2 |
| `gamma_ba[rad/s]`, `gamma_ca[rad/s]` | Tasas de decaimiento de las coherencias ba y ca |
| `tau_8S[s]` | Vida media del nivel 8S1/2 |

$\gamma_{cb}$, que necesita la Rama B, todavía no está definida.

### Variables derivadas

| Variable | Descripción |
|---|---|
| `c`, `hbar`, `kB`, `eps0` | Atajos de las constantes fundamentales |
| `g_ba`, `g_ca` | Atajos de `gamma_ba` y `gamma_ca` [rad/s] |
| `w_ba`, `w_ca`, `w_cb` | Frecuencias angulares de transición [rad/s] |
| `lmd1`, `lmd2`, `lmd3` | Longitudes de onda en resonancia: 822, 794 y 852 nm [m] |
| `k1`, `k2`, `k3` | Números de onda correspondientes [rad/m] |
| `u` | Velocidad térmica más probable del Cs [m/s] |

### Uso

```python
import sys
sys.path.append('../..')  # carpeta raíz del repositorio, vista desde Rama_X/<subcarpeta>/
from constants import k3, g_ba, u
```
