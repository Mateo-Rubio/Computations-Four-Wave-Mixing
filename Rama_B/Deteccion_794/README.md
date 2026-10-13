# Rama B, detección directa a 794 nm (pendiente)

**Todavía no hay datos.**

## El experimento previsto

Es el análogo de [`../../Rama_A/Deteccion_852/`](../../Rama_A/Deteccion_852/), con el papel de los láseres de 794 y 852 nm intercambiado:

- **Entradas:** el 822 nm (bombeo) y la semilla de 852 nm, copropagantes. El láser de 794 nm está apagado, para que toda luz de 794 nm hacia adelante venga del medio.
- **Detección:** la luz que sale hacia adelante pasa por filtros ND, una fibra, un monocromador en 794 nm, el SPCM y el QuTau (canal B). El PMT lateral (canal A) marca $\Delta_2 = 0$.
- **Ajuste de fase:** $2k_1 - k_3 = k_2$, automático en vacío con haces colineales.

**Qué se espera:** la señal está resonante cuando $\delta_2 = \Delta_2 - \Delta_3 = 0$. A diferencia de la Rama A, la señal de 794 nm no se reabsorbe a primer orden, pero la semilla de 852 nm sí se atenúa en la celda.

## Ajuste de datos

Se puede reutilizar el método de `Rama_A/Deteccion_852/FWM.ipynb`: ajustar el pico de dos fotones en el canal A y buscar en el canal B una componente con esa forma, por encima de un fondo con deriva. Antes de medir conviene caracterizar el fondo a 794 nm con cada láser bloqueado por separado.

## Archivos de datos (`data/`)

Se propone el mismo formato de la Rama A, con una subcarpeta por fecha (`data/AAAA-MM-DD/`) y un `readme.txt` en cada una. Las columnas serían:

| col 0 | col 1 | col 2 | col 3 | col 4 |
|---|---|---|---|---|
| — | λ822 (nm) | Singles A, PMT (cuentas/s) | Singles B, SPCM (cuentas/s) | ν822 (THz) |

Y el nombre de cada archivo, análogo al de la Rama A:

```
λ852(nm)-P852(mW)-P822(mW)-T(°C)-corrientePMT(mA)-aperturaSlave(mm)-λmonocromador(nm)-FiltroND
```
