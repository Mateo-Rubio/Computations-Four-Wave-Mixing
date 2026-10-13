# Rama B, fluorescencia (pendiente)

**Todavía no hay datos.**

## El experimento previsto

El 822 nm y la semilla de 852 nm atraviesan copropagantes la celda de Cs, y el PMT lateral (canal A del QuTau) cuenta la fluorescencia azul de la cascada 8S → 7P → 6S, igual que en [`../../Rama_A/Fluorescencia/`](../../Rama_A/Fluorescencia/):

1. **Barrido del 822 con el 852 fijo:** localiza la resonancia de dos fotones $\Delta_2 = 0$ en las condiciones de esta rama.
2. **Barrido del 852 con el 822 fijo en el máximo:** muestra cómo la semilla resonante con la D2 modifica la población de 8S, al poblar 6P3/2 (estructura hiperfina de la D2).

## Archivos de datos (`data/`)

Se propone conservar el formato de exportación del QuTau que se usa en la Rama A: texto separado por tabuladores, con las columnas

| col 0 | col 1 | col 2 | col 3 | col 4 |
|---|---|---|---|---|
| — | λ del láser barrido (nm) | Singles A (cuentas/s) | Singles B (cuentas/s) | ν (THz) |

y nombres con el formato `Barrido<láser>-Filtro<ND>-P822(mW)-P852(mW)-T(°C)-exposición(ms).txt`. Hay que documentar en un `readme.txt` dentro de cada subcarpeta de fecha cualquier cambio a este formato.
