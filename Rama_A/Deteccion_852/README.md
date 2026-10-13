# Rama A, etapa 2: detección directa a 852 nm

## El experimento

Sobre el montaje de la [Rama A](../README.md#montaje-común-a-las-dos-etapas), se recoge la luz que sale de la celda **hacia adelante**. Con haces colineales y $k = \omega/c$, la condición $2\omega_1 = \omega_2 + \omega_3$ da $2k_1 - k_2 = k_3$: el ajuste de fase es automático en vacío y la señal sale copropagante con los haces.

Camino de detección: filtros ND → acoplador a fibra → monocromador (852.3–852.4 nm) → SPCM → QuTau, **canal B**. Los filtros ND están antes del acoplador, así que atenúan toda la luz que sigue hacia el monocromador y protegen el SPCM. El PMT lateral sigue midiendo en el **canal A** y marca $\Delta_2 = 0$ en cada barrido.

Medida del 7 de septiembre de 2026: el 794 está fijo y se barre λ822 a través de la resonancia de dos fotones con una onda triangular (2–3 ciclos por archivo). Se usan dos ajustes del 794 y cinco filtros ND:

| λ794 (nm) | P794 (mW) | λ del monocromador (nm) | Filtros ND |
|---|---|---|---|
| 794.5301 | 18.21 | 852.4 | 2, 4, 6, 8, 10 |
| 794.6068 | 14.44 | 852.3 | 2, 4, 6, 8, 10 |

En todos los casos P822 = 41.26 mW, T = 80 °C, PMT a 45 mA y apertura del slave de 1.3 mm.

**Qué se espera:** en celda gruesa, $I_{852} \propto |\chi^{(3)}_P/\chi_{ef}|^2$ conserva solo la resonancia de dos fotones. Una señal de FWM debería verse en el canal B como una estructura con la forma del pico del canal A.

## Ajuste de datos: `FWM.ipynb`

1. **Limpieza:** descarta las filas con cuentas nulas (arranque de la adquisición) y los saltos del medidor de longitud de onda (|λ − mediana móvil de 5 puntos| > 3×10⁻⁴ nm).
2. **Canal A:** ajusta una gaussiana en la desintonía del 822, $x = \nu_{822} - \bar\nu_{822}$ (MHz), y obtiene el centro $x_0$ y el ancho $\sigma$. Compara el FWHM con el ancho Doppler esperado a la temperatura de la celda (sacada del nombre del archivo), $2\sqrt{\ln 2}\,u/\lambda_{822}$ con $u = \sqrt{2k_BT/m_{Cs}}$.
3. **Canal B:** con la forma de A fija, $g(x) = e^{-(x-x_0)^2/2\sigma^2}$, ajusta $B = b_0 + b_t(t - \tfrac12) + b_1\,g(x)$, donde $b_0$ es el fondo, $b_t$ una deriva lenta y $b_1$ la posible señal.
4. **Estadística:** calcula $z = b_1/\sigma_{b_1}$, el límite a 2σ relativo al fondo, $(\max(b_1, 0) + 2\sigma_{b_1})/b_0$, la dispersión de los residuos frente a Poisson $\sqrt{b_0/T_{exp}}$ (con $T_{exp} = 100$ ms supuesto) y la correlación de Pearson entre A y B.
5. **Figuras:** los 10 barridos (A en azul, B en rojo con bins de 30 MHz y el ajuste), el fondo $b_0$ frente al filtro ND y $b_1/b_0$ frente al filtro ND.

**Resultado:**
- $b_1$ es compatible con cero en todos los barridos ($|z| \le 2.0$, $|r| \le 0.13$). **No se detecta señal de 852 nm por encima del fondo.**
- Con ND 2, cualquier señal con la forma del pico de dos fotones es menor que el 0.3–0.4 % del fondo (2σ).
- El fondo es ≈ 650 cuentas/s con ND 8 y 10, lo que corresponde al piso del detector, y crece con la transmisión para ND ≤ 6: es luz que llega con los haces y no depende de la resonancia atómica.
- El centro del pico de A difiere en ≈ 0.0008 nm (≈ 350 MHz) entre las dos series. Conviene revisar la deriva del medidor de longitud de onda.

## Archivos de datos

`data/2026-09-07/`: archivos de texto separados por tabuladores, una fila por lectura del QuTau (≈ 225–325 filas por archivo).

| col 0 | col 1 | col 2 | col 3 | col 4 |
|---|---|---|---|---|
| — | λ822 (nm) | Singles A, PMT (cuentas/s) | Singles B, SPCM (cuentas/s) | ν822 (THz) |

La columna 0 no se usa en el análisis.

Nombre del archivo (ver `readme.txt`):

```
λ794(nm)-P794(mW)-P822(mW)-T(°C)-corrientePMT(mA)-aperturaSlave(mm)-λmonocromador(nm)-FiltroND
```

Ejemplo: `794.6068-14.44mW-41.26mW-80C-45mA-1.3mm-852.3-10ND.txt`. El notebook lee estos campos con `parse()`, así que un archivo nuevo debe respetar el mismo orden y los mismos sufijos (`mW`, `C`, `mA`, `mm`, `ND`).
