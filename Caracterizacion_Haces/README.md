# Caracterización de los haces

Común a las dos ramas: perfiles de los haces de 822 nm (bombeo) y 852 nm (la señal de la Rama A y la semilla de la Rama B) cerca del foco en la celda. Con ellos se obtienen la cintura, la posición focal, el rango de Rayleigh y la intensidad pico.

## El experimento

Un perfilador de haz (BeamMaster) se coloca en varias posiciones z a lo largo del haz. En cada posición se registran N = 20 lecturas consecutivas del ancho del haz en las dos direcciones transversales, W y V, y de la posición del centroide.

## Ajuste de datos

| Script | Qué hace | Salida |
|---|---|---|
| `822.py` | Ajusta el haz de 822 nm. Pide la potencia (mW) por consola y calcula la intensidad pico en el foco, $I_0 = 2P/(\pi w_{0W} w_{0V})$, en mW/cm² y W/cm². | `822nm_beam_waist_fit.png` |
| `852.py` | Lo mismo para el haz de 852 nm. | `852nm_beam_waist_fit.png` |
| `waist_both.py` | Ajusta ambos haces, los compara en una sola figura, grafica la evolución de los centroides y exporta las tablas de parámetros a LaTeX. | `comparacion_haces_852_822.png`, `evolucion_centroides_852_822.png`, `caracteristicas_haces.tex` |

Procedimiento común a los tres:
1. El radio en cada posición es el ancho del perfilador dividido entre 2 (de µm a m). Se toma la media ± desviación estándar de las 20 lecturas.
2. Se descartan las últimas posiciones medidas (`CORTAR_AL_FINAL = 2`).
3. Se ajusta la propagación gaussiana $w(z) = w_0\sqrt{1 + \left((z - z_0)/z_R\right)^2}$ por separado en W y V. Se reportan $w_0$, $z_0$ y $z_R$ con sus incertidumbres.

Las figuras y la tabla se guardan en el directorio desde donde se ejecuta el script.

## Archivos de datos

```
data/
├── 822nm/   z<posición>mm.xlsx
└── 852nm/   z<posición>mm.xlsx
```

- **Nombre:** `z<posición en mm>mm.xlsx`, por ejemplo `z12.5mm.xlsx`. El script extrae la posición con la expresión regular `z(\d+(\.\d+)?)mm\.xlsx`.
- **Estructura interna** (exportación de BeamMaster):
  - 21 filas de metadatos.
  - La fila de encabezados.
  - Una fila de unidades, por ejemplo `(micron)`, que el script descarta.
  - Las lecturas. Solo se usan las primeras 20.
- **Columnas usadas:** `W Width I` y `V Width I` (anchos en µm) y, en `waist_both.py`, `Pos.X` y `Pos.Y` (centroide en µm). Los decimales vienen con coma y el script los convierte.

**Las carpetas `data/822nm/` y `data/852nm/` están vacías en el repositorio:** hay que copiar ahí los archivos del perfilador antes de ejecutar.
