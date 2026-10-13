# Proyecto

## Constantes globales

`constants.py` (en la raíz del repositorio) contiene el diccionario `cte` con las constantes físicas y del sistema usadas en los análisis.

Las unidades van en el nombre de cada clave:

| Clave | Descripción |
|---|---|
| `c[m/s]` | Velocidad de la luz |
| `hbar[Js]` | Constante de Planck reducida |
| `kB[J/K]` | Constante de Boltzmann |
| `m[Kg]` | Masa atómica del Cs |
| `T[K]` | Temperatura |
| `E6P3/2[THz]`, `E8S1/2[THz]` | Energías de los niveles 6P3/2 y 8S1/2 |
| `lmd1[nm]`, `lmd2[nm]`, `lmd3[nm]` | Longitudes de onda (822, 794 y 852 nm) |
| `k1[rad/m]`, `k2[rad/m]`, `k3[rad/m]` | Números de onda correspondientes |
| `gamma_ba[1e6*rad/s]`, `gamma_ca[1e6*rad/s]` | Tasas de decaimiento |

### Uso

Desde un notebook en una subcarpeta (por ejemplo `2Lasers/` o `Suceptibilities/`):

```python
import sys
sys.path.append('..')  # carpeta raíz del repositorio
from constants import cte

k3 = cte["k3[rad/m]"]
```

En Colab, primero clonar el repositorio y trabajar dentro de él para que `constants.py` esté disponible.

Para agregar o cambiar una constante, editar `constants.py`; todos los notebooks que lo importan usarán el nuevo valor.
