# Rama B, detección directa a 794 nm

## El experimento

Es el análogo de [`../../Rama_A/Deteccion_852/`](../../Rama_A/Deteccion_852/), con el papel de los láseres de 794 y 852 nm intercambiado:

- **Entradas:** el 822 nm (bombeo, 46 mW) y la semilla de 852 nm (500 µW), copropagantes, con la celda de Cs a 60 °C. El láser de 794 nm está apagado, para que toda luz de 794 nm hacia adelante venga del medio.
- **Barrido:** el 822 está fijo en el máximo de dos fotones (desintonía nominal 0 MHz) y se barre λ852 a través de la D2. La onda triangular es de 40 mHz y la exposición del QuTau de 100 ms.
- **Detección:** la luz que sale hacia adelante pasa por los filtros ND, una fibra, el monocromador, el SPCM y el QuTau (canal B). El PMT lateral (canal A) cuenta la fluorescencia azul. Con el 822 fijo, A muestra los valles sub-Doppler F′=3, 4 y 5 de la clase $v_z \approx 0$, es decir, marca dónde el 852 es resonante con los átomos que excita el 822.
- **Ajuste de fase:** $2k_1 - k_3 = k_2$, automático en vacío con haces colineales.

**Qué se espera:** la señal es resonante en $\delta_2 = \Delta_2 - \Delta_3 = 0$. Con el 822 en $\Delta_2 = 0$, eso ocurre en las frecuencias del 852 donde están los valles del canal A. Una señal de FWM se vería en B como picos en esas frecuencias, y solo con el monocromador cerca de 8S F=4 → 6P3/2 (794.606 nm). A diferencia de la Rama A, la señal de 794 nm no se reabsorbe a primer orden, pero la semilla de 852 nm sí se atenúa en la celda.

Medidas, todas a 60 °C:

| Serie | λ monocromador (nm) | Filtros ND |
|---|---|---|
| 822 barrido solo (46 mW) | 794 | 10 |
| 852 barrido solo (500 µW) | 794 | 2, 4, 8, 10 |
| 852 barrido con el 822 fijo | 794 | 2, 4, 8, 10 |
| 852 barrido con el 822 fijo | 793.0 a 795.0, en pasos de 0.2 | 2 |

## Ajuste de datos: `FWM.ipynb`

1. **Lectura:**
   - Se descartan las filas sin lectura válida del láser barrido y las de 0 cuentas.
   - Los campos del nombre se reconocen por su sufijo, así que el orden de λ monocromador, T y ND puede variar.
   - El barrido triangular se corta en rampas en los extremos de λ.
2. **822 solo:** gaussiana más línea base sobre el promedio de las rampas. Da el máximo de la fluorescencia de dos fotones, el FWHM frente al Doppler a 60 °C y el corrimiento entre rampas de subida y de bajada.
3. **Canal A con el 822 fijo:** línea base lineal menos tres lorentzianas (F′=3, 4 y 5). Da el centro y el ancho de cada valle. La línea base relativa al máximo del 822 solo y el corrimiento de los valles respecto a lo tabulado indican si el 822 estaba en el máximo.
4. **Origen del canal B:** se normalizan los barridos de B a 1 lejos de resonancia y a 0 en el fondo del pozo, para comparar formas entre tomas. La plantilla de transmisión del 852, $T_{852}$, sale del 852 solo con ND 2. El piso del detector sale del 852 solo con ND 8 y 10.
5. **Prueba de FWM:** se ajusta

   $$B = b_0 + b_t(t - \tfrac12) + s\,T_{852}\!\left(x_c + \frac{x - x_c - \delta x}{w}\right) + \sum_{F'} b_{F'}\,L_{F'}(x).$$

   - $b_0$ es el piso más la luz del 822, y $s$ la luz del 852.
   - $\delta x$ y $w$ corren y estiran la plantilla. El pozo cambia de ancho con la potencia del 852.
   - $L_{F'}$ son lorentzianas de altura 1 con el centro y el ancho de los valles de A del mismo barrido.
   - Una señal de FWM daría $b_{F'} > 0$.
   - El error de cada $b_{F'}$ es el mayor entre el del ajuste y la dispersión entre rampas dividida entre $\sqrt n$, porque el ruido entre rampas no es blanco.
6. **Dependencias:** se grafican la luz del 822 ($b_0$ − piso), la del 852 ($s$), su cociente y las $b_{F'}$ frente a la posición del monocromador, y los niveles de B frente al filtro ND.

**Resultados:**

- **822 solo:** FWHM = 411 ± 8 MHz, frente a 413 MHz de Doppler a 60 °C. El centro está a +51 MHz de $\nu_{TP}/2$ tabulado. Las rampas de subida y de bajada se separan 31 MHz.
- **Canal A:** los valles están en ≈ −445, −252 y +11 MHz, con FWHM ≈ 160, 86 y 33 MHz.
  - Con ND 2 y ND 10 la línea base es 1.04–1.05 veces el máximo del 822 solo, así que el 822 estaba en el máximo.
  - Con ND 4 y ND 8 los valles están corridos −63 y −49 MHz y la base baja a 0.96 y 0.89. El 822 estaba ≈ 50–65 MHz por debajo del máximo.
- **Canal B:** con ND 2, B es casi todo luz de la semilla de 852 nm transmitida por la celda, con el pozo de absorción Doppler de la D2 (transmisión mínima ≈ 6 %). A eso se suman 1150–1650 cuentas/s de luz del 822.
  - La forma es la misma con y sin el 822 y en todas las posiciones del monocromador.
  - Ningún nivel tiene máximo en 794.6 nm: **el monocromador no separa el 794 de los haces de 822 y 852 nm**.
  - Con ND 8 y 10, B está en el piso del detector (231 cuentas/s).
- **FWM:** $b_4$ y $b_5$ son compatibles con cero en todas las tomas ($|z| \le 1.9$).
  - $b_3$ sale positivo en 793.0–793.4 nm. Pero el valle F′=3 cae en pleno flanco de absorción, y el exceso es más ancho que el valle y aparece donde la plantilla más se deforma. Es un desajuste de forma.
  - En 794.6 y 794.8 nm las tres amplitudes son compatibles con cero: cualquier señal es menor que ≈ 210 cuentas/s con ND 2 (2σ). **No se detecta señal de 794 nm.**
- **Ruido:** una vez ajustada la transmisión, la dispersión de B es 1.0–1.15 veces la de Poisson con 100 ms de exposición.

## Pendiente

- Calibrar el monocromador con el láser de 794 nm: transmisión frente a la posición y ancho de banda.
- Medir B con el monocromador lejos de 794 nm (por ejemplo 780 y 810 nm), para ver si la luz de 822 y 852 es luz difusa dentro del monocromador.
- Poner un filtro interferencial de 794 nm antes de la fibra para bloquear el 822 y el 852, y repetir sin los filtros ND.

## Archivos de datos (`data/`)

Texto separado por tabuladores, una fila por lectura del QuTau. La primera o las dos primeras filas tienen 0 cuentas.

| col 0 | col 1 | col 2 | col 3 | col 4 |
|---|---|---|---|---|
| — (no se usa) | λ del láser barrido (nm) | Singles A, PMT (cuentas/s) | Singles B, SPCM (cuentas/s) | ν del láser barrido (THz), = c/λ |

Nombre del archivo, con los campos entre corchetes opcionales:

```
<láser barrido>-[<desintonía del láser fijo>]-<P láser barrido>-[<P láser fijo>]-<λ monocromador>-<T celda>-<filtro ND>.txt
```

- **Láser barrido:** `822` o `852`.
- **Desintonía del láser fijo:** en MHz. `0MHz` es el 822 en el máximo de dos fotones.
- **Potencias:** en `mW` o `muW` (µW).
- **λ monocromador:** en `nm`.
- **Temperatura:** en `C` (°C).
- **Filtro ND:** con sufijo `ND`.

Los dos campos opcionales aparecen juntos cuando hay un láser fijo. En todas las tomas la exposición es de 100 ms y la frecuencia del barrido de 40 mHz.

| Serie | Archivos |
|---|---|
| 822 solo | `822-46mW-60C-10ND-794.txt` |
| 852 solo | `852-500muW-794nm-60C-{2ND, 4ND, 8ND, 10ND}.txt` |
| 852 + 822, monocromador en 794 nm | `852-0MHz-500muW-46mW-794nm-60C-{2ND, 4ND, 8ND, 10ND}.txt` |
| 852 + 822, barrido del monocromador | `852-0MHz-500muW-46mW-{793, 793.2, …, 795}nm-60C-2ND.txt` |

### Observaciones sobre los archivos

- **`822-46mW-60C-10ND-794.txt`:** el campo del monocromador va al final y sin el sufijo `nm`. El notebook lo lee igual porque reconoce los campos por su sufijo.
- **`852-0MHz-…-794nm-60C-4ND.txt` y `…-8ND.txt`:** el 822 no estaba en el máximo de dos fotones. Los valles de A están corridos ≈ −60 MHz y la línea base es más baja.
