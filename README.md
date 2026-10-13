# Mezclado de cuatro ondas en vapor de cesio

Cálculos y análisis de datos del proyecto *Estudio teórico y experimental del mezclado de cuatro ondas en vapor de cesio a través de la absorción de dos fotones* (Mateo Rubio Hernández; directora: Mayerlin Nuñez, Ph.D.; Departamento de Física, Universidad de los Andes).

## El experimento en breve

El cesio se modela como una escalera de tres niveles:

| Nivel | Estado | Transición | Láser |
|---|---|---|---|
| \|a⟩ | 6S1/2 | a → c (dos fotones) | 822 nm, bombeo (E1) |
| \|b⟩ | 6P3/2 | c ↔ b | 794 nm (E2) |
| \|c⟩ | 8S1/2 | b ↔ a (línea D2) | 852 nm (E3) |

Con la conservación de la energía 2ω822 = ω794 + ω852, el proceso puede seguir dos ramas:

- **Rama A** (la que se monta hoy): se siembra el 794 y se genera el 852.
- **Rama B**: se siembra el 852 y se genera el 794.

En la teoría se resuelve la ecuación de Liouville para la matriz de densidad orden por orden. La coherencia de dos fotones ρca⁽²⁾ es común a ambas ramas, y a tercer orden aparece la susceptibilidad paramétrica

χ⁽³⁾ ∝ 1 / [(Δ1 − iγba)(Δ2 − iγca)(resonancia de la señal)]

donde Δ1 es la desintonía del bombeo frente a 6P3/2 (≈ 12.8 THz), Δ2 la de dos fotones 6S → 8S, Δ3 la del 852 frente a la D2 y δ2 = Δ2 − Δ3 la del 794 frente a 8S → 6P3/2. En la Rama A la señal de 852 nm se reabsorbe (χ⁽¹⁾ ∝ 1/(Δ3 − iγba)). En una celda ópticamente gruesa esa reabsorción cancela el realce en Δ3 y solo queda la resonancia de dos fotones.

En el laboratorio, el 822 y el 794 se combinan copropagantes en un PBS y atraviesan una celda de Cs a 80 °C:

1. **Etapa 1, fluorescencia:** un PMT lateral (canal A del QuTau) cuenta la fluorescencia azul (455/459 nm) de la cascada 8S → 7P → 6S, que es proporcional a la población de \|c⟩. Al barrer el 822 aparece el pico gaussiano (ensanchado por Doppler) de dos fotones. Al barrer el 794 aparecen tres valles, que corresponden a 8S F″=4 → 6P3/2 F′=3, 4, 5.
2. **Etapa 2, detección directa a 852 nm:** la luz que sale hacia adelante pasa por filtros ND, una fibra, un monocromador (852.3 nm) y un SPCM (canal B). Hasta ahora el canal B es plano frente a λ822: no hay señal de 852 nm por encima del fondo.

## Estructura del repositorio

```
.
├── constants.py                 # única fuente de constantes físicas (ver abajo)
├── Susceptibilities/            # teoría: χ(1) y χ(3), en reposo y con promedio Doppler
├── Laser Characterization/      # cintura e intensidad de los haces 822 y 852 nm
├── 2Lasers/                     # experimento etapa 1: fluorescencia (PMT)
└── Experiments_FWM/             # experimento etapa 2: búsqueda del 852 nm (SPCM)
```

### `constants.py`

Define las constantes del problema en SI: el diccionario `cte` y las variables derivadas (frecuencias de transición, longitudes de onda, números de onda, tasas de decaimiento y velocidad térmica). Ningún notebook define constantes propias; todos importan de aquí. La sección [Constantes globales](#constantes-globales) lo describe en detalle.

### `Susceptibilities/` (teoría)

| Archivo | Qué ejecuta | Figuras que guarda |
|---|---|---|
| `Susceptibilidades.ipynb` | Susceptibilidades del átomo **en reposo**: pasa de las perillas del laboratorio (Δ2, δ2) a las desintonías (Δ1, Δ3); comprueba el ajuste de fase 2k1 − k2 − k3 = 0, la identidad Δ3 = Δ2 − δ2 y el tamaño de Δ1; grafica χ⁽¹⁾(ω3) (absorción y dispersión), cortes de \|χ⁽³⁾\|² al barrer un solo láser, el mapa de \|χ⁽³⁾\|² en el plano (Δ2, δ2) y la intensidad de la celda ópticamente gruesa. | `chi1_natural.pdf`, `chi3_squared.pdf`, `map_chi3_squared.png`, `thick_cell.png` |
| `Suceptibilidades_Doppler.ipynb` | **Promedio Doppler** con la función de dispersión del plasma Z(ζ): χ̄⁽¹⁾(ω3) ∝ Z(ζb) y el mapa de \|χ̄⁽³⁾\| ∝ \|(Z(ζa) − Z(ζb))/(ζa − ζb)\| en el plano (Δ2, Δ3), con la cresta Δ3 = (k3/2k1)Δ2. | `chi-1.png`, `figuras/fig4_2_chi3_doppler.pdf` |

N, \|μba\| y \|μcb\| están fijados provisionalmente en 1. Solo cambian la escala de las susceptibilidades, así que las gráficas normalizadas no se ven afectadas.

### `Laser Characterization/` (haces)

Scripts de Python que leen los perfiles del perfilador de haz (archivos `z*mm.xlsx` de BeamMaster, con la posición z en el nombre) y ajustan la propagación gaussiana w(z) = w0·√(1 + ((z − z0)/zR)²) en las direcciones W y V.

| Archivo | Qué ejecuta | Salida |
|---|---|---|
| `822.py` | Ajuste del haz de 822 nm. Pide la potencia (mW) por consola y calcula la intensidad pico en el foco, I0 = 2P/(π·wW·wV). | `822nm_beam_waist_fit.png` |
| `852.py` | Lo mismo para el haz de 852 nm. | `852nm_beam_waist_fit.png` |
| `waist_both.py` | Compara ambos haces (cinturas y evolución de los centroides) y exporta las tablas de parámetros a LaTeX. | `comparacion_haces_852_822.png`, `evolucion_centroides_852_822.png`, `caracteristicas_haces.tex` |

Los scripts buscan los datos en `Laser Characterization/data4/822nm/` y `data4/852nm/`. **Esa carpeta no está en el repositorio** y hay que copiarla aparte. Las figuras se guardan en el directorio desde donde se ejecuta el script.

### `2Lasers/` (etapa 1: fluorescencia)

`2Lasers.ipynb` analiza la fluorescencia que cuenta el PMT (Singles A) frente a la longitud de onda:

- Corta el barrido triangular en rampas (ciclos), promedia los últimos 3 ciclos en bins de frecuencia y convierte λ a desintonía en MHz.
- Ajusta una gaussiana al pico de dos fotones del 822 nm y 3 lorentzianas con línea base común a los valles del 794 nm. De ahí salen las separaciones hiperfinas de 6P3/2 (≈ 260 y 200 MHz, frente a las tabuladas de 251.0 y 201.2 MHz).
- Grafica todos los barridos con un eje secundario en MHz e imprime una tabla con λ0, la desintonía, el FWHM y la línea base de cada archivo.

| Carpeta de datos | Contenido | Formato del nombre (ver `readme.txt`) |
|---|---|---|
| `data/` | Barridos del 822 solo y del 822 + 794 (columnas: —, λ, Singles A, ν). | `P822-[P794-]frecBarrido-amplitud-exposición-T` |
| `data/2026-09-08/` | Medida del 8 de septiembre de 2026. | `P822-P794-T-FiltroND` |
| `newdata/` | Barridos del 794 o del 822 con los dos canales (columnas: —, λ, Singles A, Singles B, ν). | `Barrido<láser>-Filtro<ND>-P822-P794-T-exposición` |

### `Experiments_FWM/` (etapa 2: búsqueda del 852 nm)

- `data/2026-09-07/`: barridos de λ822 con el canal A (PMT) y el canal B (SPCM tras el monocromador) para dos ajustes del 794 (794.5301 nm / 18.21 mW y 794.6068 nm / 14.44 mW) y filtros ND = 2, 4, 6, 8 y 10. El nombre sigue el formato `λ794-P794-P822-T-corrientePMT-aperturaSlave-λ852-FiltrosND`. Las columnas son las mismas que en `2Lasers/newdata/`.
- `FWM.ipynb`: **todavía es un esqueleto** (solo importa numpy). Aquí va el análisis del canal B frente al canal A.

## Cómo ejecutar

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install numpy scipy matplotlib pandas openpyxl jupyter
```

Los notebooks se abren **desde su propia carpeta** (`cd Susceptibilities`, `cd 2Lasers`, …). Cada uno agrega la raíz del repositorio a `sys.path` para importar `constants.py` y lee sus datos con rutas relativas. En Colab, primero hay que clonar el repositorio y luego hacer `%cd` a la subcarpeta.

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
| `gamma_ba[rad/s]`, `gamma_ca[rad/s]` | Tasas de decaimiento de las coherencias |
| `tau_8S[s]` | Vida media del nivel 8S1/2 |

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
sys.path.append('..')  # carpeta raíz del repositorio
from constants import k3, g_ba, u
```
