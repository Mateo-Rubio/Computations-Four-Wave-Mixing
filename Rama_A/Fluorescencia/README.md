# Rama A, etapa 1: fluorescencia

## El experimento

Con el montaje de la [Rama A](../README.md#montaje-común-a-las-dos-etapas) (822 + 794 copropagantes, celda a 80 °C), el PMT lateral cuenta la fluorescencia azul de la cascada 8S → 7P → 6S. Contar fotones azules equivale a contar átomos que llegaron a 8S1/2. Es emisión espontánea, sin dirección privilegiada: mide **poblaciones, no coherencias**.

Se hacen dos tipos de barrido, ambos con una onda triangular sobre el láser; cada rampa monótona de λ es un *ciclo*:

1. **Solo el 822 nm (≈ 42 mW), barriendo λ822:** aparece el pico de absorción de dos fotones 6S → 8S ($\Delta_2 = 0$), cerca de 822.4687 nm. El perfil es gaussiano y mucho más ancho que $\gamma_{ca}$, porque refleja la distribución de velocidades (ensanchamiento Doppler).
2. **El 822 fijo en el máximo (clase $v_z \approx 0$) y el 794 nm barrido (≈ 19.7 mW):** aparecen tres valles en la fluorescencia. Cuando el 794 es resonante con 8S1/2 F″=4 → 6P3/2 F′=3, 4, 5, induce c → b, y los átomos salen de 8S por ese peldaño en vez de por la cascada que ve el PMT. Esto muestra que el 794 se acopla a c ↔ b, una condición necesaria para la Rama A. No es todavía una señal de FWM, porque es un efecto de poblaciones que aparecería aun sin ajuste de fase.

## Ajuste de datos: `2Lasers.ipynb`

1. **Rampas:** corta el barrido triangular en los extremos de λ (máximos y mínimos de λ suavizada).
2. **Promedio:** toma los últimos 3 ciclos, convierte ν a desintonía en MHz respecto a una referencia redondeada y promedia en bins de 5 MHz (media ± desviación estándar).
3. **Ajustes:**
   - Pico del 822: una gaussiana más línea base. Da el centro λ0 y el FWHM.
   - Valles del 794: 3 lorentzianas con línea base común. Las semillas salen de `find_peaks` sobre la señal invertida. Da el centro, el FWHM y la profundidad de cada valle.
4. **Salida:** la figura del barrido del 794 con los tres valles ajustados, todos los barridos con un eje secundario en MHz y una tabla con λ0, la desintonía, el FWHM y la línea base de cada archivo. El canal B no se ajusta, porque no muestra estructura espectral.

**Resultado:** las separaciones entre valles son 260 ± 2 MHz (F′=5↔4) y 200 ± 3 MHz (F′=4↔3), frente a las tabuladas de 251.00(2) y 201.24(2) MHz. Desde F″=3 se verían F′=2, 3, 4, separados 201 y 151 MHz, así que los datos indican F″ = 4.

## Archivos de datos

Archivos de texto separados por tabuladores, una fila por lectura del QuTau. Las columnas que no aparecen en las tablas no se usan en el análisis.

### `data/`: canal A solamente (6 columnas)

| col 0 | col 1 | col 2 | col 3 | col 4 | col 5 |
|---|---|---|---|---|---|
| — | λ (nm) | Singles A (cuentas/s) | ν (THz), = c/λ | — | — |

Nombre del archivo (ver `data/readme.txt`). Todas las medidas se hicieron con el PMT a 15 V y 40 mA.

- 5 campos: `P822(mW)-frecBarrido(mHz)-amplitudBarrido-exposición(ms)-T(°C)`. Ejemplo: `42-30-6-150-80.txt`, barrido del 822 solo.
- 6 campos: `P822(mW)-P794(mW)-frecBarrido(mHz)-amplitudBarrido-exposición(ms)-T(°C)`. Ejemplo: `42-19.73-30-6-150-80.txt`, barrido del 794 con el 822 fijo.

### `data/2026-09-08/`: medida del 8 de septiembre de 2026 (6 columnas, mismo formato)

Formato del nombre según `readme.txt`: `P822(mW)-P794(mW)-T(°C)-FiltroND`, con el PMT a 15 V y 45 mA. El archivo `41.26mW-10mW-80C.txt` no incluye el campo del filtro ND.

### `newdata/`: canales A y B (5 columnas)

| col 0 | col 1 | col 2 | col 3 | col 4 |
|---|---|---|---|---|
| — | λ (nm) | Singles A (cuentas/s) | Singles B (cuentas/s) | ν (THz) |

Nombre del archivo: `Barrido<láser barrido>-Filtro<ND>-P822(mW)-P794(mW)-T(°C)-exposición(ms)`. Ejemplo: `Barrido794-Filtro4-42.9mW-3.72mW-80C-100ms.txt`.

`newdata/borrar.txt` no contiene datos (solo el texto `aa`) y se puede eliminar.
