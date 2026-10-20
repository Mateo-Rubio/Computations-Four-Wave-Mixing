# Rama B, fluorescencia

## El experimento

El 822 nm y la semilla de 852 nm atraviesan copropagantes la celda de Cs, a 80 °C y, para parte de las series, también a 50, 60 y 70 °C. El PMT lateral cuenta la fluorescencia azul de la cascada 8S → 7P → 6S, igual que en [`../../Rama_A/Fluorescencia/`](../../Rama_A/Fluorescencia/). Todos los barridos usan una onda triangular de 20 mHz sobre el láser barrido y 200 ms de exposición. Cada rampa monótona de λ es un *ciclo*.

1. **Solo el 822 nm (45 mW), barriendo λ822:** aparece el pico de absorción de dos fotones 6S F=4 → 8S F=4 ($\Delta_2 = 0$), ensanchado por Doppler.
2. **Solo el 852 nm, barriendo λ852** a 0.2, 0.5, 1, 3.5, 5, 10.1 y 14.4 mW: la línea D2 desde 6S F=4 vista por el PMT, sin el 822.
3. **El 822 fijo (46 mW, desintonía nominal 0 MHz) y el 852 barrido**, a las mismas potencias: cómo la semilla resonante con la D2 modifica la población de 8S de la clase de velocidad que selecciona el 822.

## Ajuste de datos a 80 °C: `fluorescencia.ipynb`

Este cuaderno usa solo las tomas a 80 °C.

1. **Lectura:** se descartan las filas sin lectura válida del láser barrido (λ a más de 1 nm del láser del nombre) y las de 0 cuentas.
2. **Rampas y promedio:** el barrido triangular se corta en los extremos de λ suavizada. Se promedian todas las rampas en bins de 10 MHz (media ± desviación estándar).
3. **Eje de frecuencia absoluto:**
   - **822:** $\nu_{822} - \nu_{TP}/2$, con $\nu_{TP}$ la transición 6S F=4 → 8S F=4.
   - **852:** $\nu_{852} - \nu(F{=}4 \to F'{=}5)$.

   Las frecuencias salen de [`constants.py`](../../constants.py) más la estructura hiperfina tabulada.
4. **Ajustes:**
   - **822 solo:** gaussiana más línea base. Se compara el FWHM con el Doppler a 80 °C y se mide el corrimiento entre rampas de subida y de bajada.
   - **852 solo:** modelo de autoabsorción $S = c + a\,g\,e^{-b g}$, donde $g$ es la suma de las tres componentes Doppler F=4 → F′=3, 4, 5 con sus separaciones e intensidades tabuladas. Da el ancho, la profundidad óptica efectiva $b$ y la señal integrada en función de la potencia.
   - **852 con el 822 fijo, P ≤ 1 mW:** línea base lineal menos 2 lorentzianas, o menos 1 si el segundo valle no es significativo. Da la posición, el ancho y la profundidad de los valles F′=3 y F′=4.
   - **852 con el 822 fijo, P ≥ 3.5 mW:** no se ajusta. Se le resta el barrido del 852 solo de la misma potencia sobre el eje de frecuencia común.

**Resultados:**

- **822 solo:** FWHM = 424 ± 2 MHz, frente a 425.6 MHz de Doppler: el perfil es enteramente Doppler. El centro queda a +47 MHz de $\nu_{TP}/2$ tabulado (λ0 = 822.468822 nm).
- **852 solo:**
  - Hasta 1 mW el perfil tiene dos jorobas y un hueco en el centro de la línea, por autoabsorción en la celda ópticamente gruesa. $b$ baja de ≈ 7 a ≈ 3 al subir la potencia.
  - Desde 3.5 mW la transición se satura ($b = 0$) y el ancho crece de 474 a 677 MHz.
  - La señal integrada crece como $P^{2.0}$ hasta 1 mW.
- **852 con el 822 fijo, baja potencia:**
  - Hay valles sub-Doppler en F′=3 y F′=4, por bombeo óptico de F=4 a F=3. En F′=5, que es cíclica, no hay valle.
  - La separación entre valles es 195 ± 3 MHz (510 µW) y 202 ± 4 MHz (1 mW), frente a 201.3 MHz tabulados.
  - A 200 µW solo se resuelve F′=3, corrido −108 MHz, probablemente porque el 822 no estaba en el máximo de dos fotones (ver abajo).
- **852 con el 822 fijo, alta potencia:** la fluorescencia de dos fotones queda casi suprimida entre ≈ −700 y −250 MHz.

**Precisión del eje de frecuencia:** el PMT integra 200 ms mientras el medidor de onda da un solo valor de λ, así que las rampas de subida y de bajada se separan ≈ 21 MHz en el barrido del 822. Al promediar las dos direcciones el efecto se cancela.

## Efecto de la temperatura: `fluorescencia_temperatura.ipynb`

Compara 50, 60, 70 y 80 °C en el 822 solo, el 852 solo a 0.2, 0.5 y 1 mW, y el 852 con el 822 fijo a 0.2, 0.5 y 1 mW. El 852 solo a 3.5 mW tiene 60, 70 y 80 °C, y el 852 con el 822 fijo a 3.5 mW solo 60 y 80 °C (ver archivos descartados abajo). Usa las mismas funciones de lectura y los mismos modelos que `fluorescencia.ipynb`, con estos cambios:

- **Densidad:** se calcula $n(T)$ con la presión de vapor del Cs líquido (Steck): ×9.3 entre 50 y 80 °C.
- **822 solo:** el ancho se mide rampa por rampa, para no mezclar el corrimiento entre subida y bajada.
- **852 solo:** el corrimiento $\nu_0$ del modelo de autoabsorción se acota a ±250 MHz, porque a 60 °C y 1 mW el ajuste sin cota cae en un mínimo sin sentido. La toma de 200 µW no se ajusta, porque la señal es del orden del ruido.
- **852 + 822, P ≤ 1 mW:** hasta 3 lorentzianas (F′=3, 4 y 5) con centros acotados a ±60 MHz de las separaciones tabuladas. La profundidad de cada valle se da relativa a la línea base.

**Resultados:**

- **822 solo:**
  - El perfil es Doppler a todas las temperaturas, con FWHM de 405 a 421 MHz por rampa. No se resuelve el aumento con $\sqrt{T}$.
  - La altura crece como $n^{0.73}$ (×5.2 entre 50 y 80 °C). La línea base de la serie 852 + 822 muestra que la potencia o la alineación del 822 cambian entre tomas hasta un factor 2, así que la altura absoluta no mide bien $n$.
  - A 50 °C el centro del pico, y con él el cero del medidor de onda, está ≈ 40 MHz más abajo que en las demás tomas.
- **852 solo:**
  - La autoabsorción aparece entre 60 y 70 °C: a 500 µW, $b$ = 0, 0, 2.9 y 4.9 a 50, 60, 70 y 80 °C. A 50 y 60 °C no hay hueco a ninguna potencia.
  - A 3.5 mW, sin autoabsorción, la señal integrada crece como $n^{1.2}$ entre 60 y 80 °C, más rápido que la del 822.
  - A 500 µW y 1 mW no crece entre 50 y 60 °C, pese a que no hay autoabsorción y $n$ se multiplica por 2.2: la señal del 852 solo también varía entre tomas.
- **852 + 822, baja potencia:** la razón principal es que a mayor T el 852 se absorbe más antes de llegar a la región observada.
  - El valle en F′=5 (cíclica) aparece por saturación con menos potencia cuanto más fría está la celda: a 50 °C a las tres potencias, a 60 °C desde 500 µW, a 70 °C solo a 1 mW y a 80 °C nunca.
  - El valle F′=4 se ensancha al enfriar (a 1 mW, 62, 90, 119 y 155 MHz de 80 a 50 °C). F′=3 se ensancha de 80 a 60 °C (195, 241 y 318 MHz a 1 mW), pero a 50 °C queda en 261 MHz.
  - A 60 °C y 1 mW se funden los valles F′=3 y F′=4, y a 50 °C casi.
  - A 50 °C los valles se corren ≈ −45 MHz. La línea base está al ≈ 100 % del máximo del 822 solo, así que se explica por el corrimiento del medidor de onda y no por una desintonía del 822.
- **852 + 822, 3.5 mW:** al restar el 852 solo, la zona sin fluorescencia de dos fotones es más ancha a 60 °C. En F′=4 queda al 14 % de su valor lejos de resonancia (38 % a 80 °C), y en F′=5 al 33 % (75 % a 80 °C).

## Archivos de datos (`data/`)

Texto separado por tabuladores, una fila por lectura del QuTau:

| col 0 | col 1 | col 2 | col 3 |
|---|---|---|---|
| — (no se usa) | λ del láser barrido (nm) | cuentas/s del PMT | ν del láser barrido (THz), = c/λ |

Nombre del archivo, con los campos entre corchetes opcionales:

```
<láser barrido>-[<desintonía del láser fijo>]-<P láser barrido>-[<P láser fijo>]-<frec. barrido>-<exposición>-<T celda>.txt
```

- **Láser barrido:** `822` o `852`.
- **Desintonía del láser fijo:** en MHz. `0MHz` es el 822 en el máximo de dos fotones.
- **Potencias:** en `mW` o `muW` (µW).
- **Resto de campos:** frecuencia del barrido en `mHz`, tiempo de exposición en `ms` y temperatura de la celda en `C` (°C).
Los dos campos opcionales aparecen juntos cuando hay un láser fijo, por lo que el archivo tiene 7 campos. Sin láser fijo tiene 5.

| Serie | Archivos | Láser fijo |
|---|---|---|
| 822 solo | `822-45mW-20mHz-200ms-{50C, 60C, 70C, 80C}.txt` | — |
| 852 solo, 80 °C | `852-{200muW, 503muW, 1mW, 3.5mW, 5mW, 10.1mW, 14.42mW}-20mHz-200ms-80C.txt` | — |
| 852 solo, 50, 60 y 70 °C | `852-{200muW, 500muW, 1mW, 3.5mW}-20mHz-200ms-{50C, 60C, 70C}.txt` | — (salvo 3.5 mW a 50 °C, ver abajo) |
| 852 + 822, 80 °C | `852-0MHz-{200muW, 510muW, 1mW, 3.5mW, 5mW, 10.1mW, 14.42mW}-46mW-20mHz-200ms-80C.txt` | 822 a 46 mW, 0 MHz |
| 852 + 822, 60 y 70 °C | `852-0MHz-{200muW, 500muW, 1mW, 3.5mW}-46mW-20mHz-200ms-{60C, 70C}.txt` | 822 a 46 mW, 0 MHz |
| 852 + 822, 50 °C | `852-0MHz-{200muW, 500muW, 1mW}-46mW-20mHz-200ms-50C.txt` | 822 a 46 mW, 0 MHz |

### Observaciones sobre los archivos

- **Primera fila de cada archivo:** tiene 0 cuentas, y hay algunos ceros aislados más. El análisis los descarta.
- **`852-0MHz-200muW-46mW-20mHz-200ms-80C.txt`:** el valle F′=3 está corrido −108 MHz respecto a las tomas de 510 µW y 1 mW. Es compatible con que el 822 estuviera ≈ 110 MHz por debajo del máximo de dos fotones, pero no hay registro de la frecuencia del 822 durante las tomas. La "desintonía 0 MHz" del nombre es, por tanto, nominal.
- **Potencia más cercana a 0.5 mW:** a 80 °C la serie 852 solo usa 503 µW y la serie con el 822 usa 510 µW. A 50, 60 y 70 °C ambas usan 500 µW. Se comparan entre sí como la misma potencia.
- **`852-0MHz-3.5mW-46mW-20mHz-200ms-70C.txt`:** no tiene ninguna lectura del 852. El medidor de onda registra un barrido del 822 (λ de 822.4642 a 822.4695 nm, 136 filas, pico de ≈ 5800 cuentas/s). No se sabe si el 852 estaba encendido, así que no se usa.
- **`852-3.5mW-20mHz-200ms-50C.txt`:** el nombre dice 852 solo, pero el 822 estaba encendido.
  - Lejos de resonancia (ν852 > +450 MHz) tiene ≈ 2300 cuentas/s, el nivel de la fluorescencia de dos fotones a 50 °C. Los demás barridos del 852 solo están entre 20 y 700.
  - Tiene la forma del barrido 852 + 822 a 3.5 mW y 60 °C.

  Probablemente es la toma 852 + 822 a 3.5 mW de 50 °C con el nombre equivocado. No se usa, porque falta el 852 solo correspondiente para restarle.
- **Desintonía del 822 a 50, 60 y 70 °C:** a 60 y 70 °C los valles dan |δ1| ≤ 31 MHz, así que el 822 estuvo cerca del máximo de dos fotones. Aun así, la línea base de las tomas 852 + 822 a 60 °C es solo el 45–66 % del máximo del 822 solo a la misma temperatura, lo que indica que la potencia o la alineación del 822 cambiaron entre tomas.
- **Medidor de onda a 50 °C:** el pico del 822 solo y los valles del 852 están ≈ 40–45 MHz por debajo de las demás temperaturas. Como la línea base de las tomas 852 + 822 está al ≈ 100 % del máximo del 822 solo, el 822 estaba en el máximo de dos fotones y lo que se corrió fue el cero del medidor de onda.
- **`852-0MHz-5mW-46mW-...`:** el barrido está corrido hacia frecuencias menores (−1495 a +175 MHz) respecto a los demás (≈ −900 a +900 MHz).
