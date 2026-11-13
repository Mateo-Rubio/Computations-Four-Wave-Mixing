# Rama B: teoría

Evaluación numérica de las expresiones de los Capítulos 2 y 3 de la monografía para la Rama B (semilla a 852 nm, señal a 794 nm), con el átomo en reposo. No hay archivos de datos: todo se calcula a partir de [`constants.py`](../../constants.py).

**Convenciones:** las tasas y desintonías van divididas por $2\pi$, en MHz. Los ejes de los mapas son las dos perillas de esta rama, $(\Delta_2, \Delta_3)$, con $\delta_2 = \Delta_2 - \Delta_3$. Las ecuaciones se citan con su número en el PDF de la monografía. Los cuadernos se ejecutan desde esta carpeta y guardan sus figuras en `figuras/`, en PDF.

## `capitulo2.ipynb`: susceptibilidades de la Rama B

Todas las figuras están normalizadas, así que no dependen de $N$, de los dipolos ni de las intensidades.

| Figura del cuaderno | Figura del PDF | Cantidad | Ecuaciones | Archivo |
|---|---|---|---|---|
| F1 | — | Población $\rho_{bb}^{(2)}$ que crea la semilla, frente a $\Delta_3$ | (2.52)–(2.53) | `figuras/F1_rhobb_vs_delta3.pdf` |
| F2 | 2.7 | $\chi_{\text{pop}}(\omega_2)$ frente a $\delta_2$, con $\rho_{bb}^{(2)}$ constante | (2.86) | `figuras/F2_chipop_vs_delta2.pdf` |
| F3 | 2.8 | Mapa de $\mathrm{Im}\,\chi^{(3)}_{\text{pop}}$ en $(\Delta_2, \Delta_3)$ | (2.87) | `figuras/F3_mapa_chipop.pdf` |
| F4 | 2.9 | $\chi_{\text{ef}}$ de la señal, término por término | (2.85) y (2.87) | `figuras/F4_chief_terminos.pdf` |
| F5 | 2.6 | Módulo y fase de $\chi^{(3)}_{P,B}$ | (2.84) | `figuras/F5_chiP_modulo_fase.pdf` |

## `capitulo3.ipynb`: propagación en la celda

Cada figura es la evaluación directa de una expresión cerrada del Capítulo 3, sin integración numérica.

| Figura | Cantidad | Ecuaciones | Archivo |
|---|---|---|---|
| 3.1 | Transmisión de la semilla, $T_3 = e^{-2\kappa_3L}$, frente a $\Delta_3$ para varias densidades $N$ | (3.26)–(3.27) | `figuras/F3-1_transmision_semilla.pdf` |
| 3.2 | $\lvert\chi^{(3)}_{P,B}\rvert^2$ normalizada en el plano $(\Delta_2, \Delta_3)$, en escala logarítmica | (2.84) | `figuras/F3-2_mapa_celda_delgada.pdf` |
| 3.3 | (a) $\lvert L_{\text{ef}}\rvert^2/L^2$ con $\Delta k = 0$; (b) intensidad de la señal con $\Delta_2 = 0$, para varias profundidades ópticas de la semilla | (3.53) y (3.56) | `figuras/F3-3_longitud_efectiva.pdf` |

La Figura 3.1 no se puede normalizar, así que usa $N$, $\lvert\mu_{ba}\rvert$ y $L$ en SI: la densidad sale de `n_Cs(T)` (presión de vapor de Steck, ec. (4.2)) y la longitud de `L_celda`.

Además, la sección 5 del cuaderno imprime, sin figura, $s_3$ y $\rho_{bb}^{(2)}$ para la semilla de la medida de detección, en resonancia y desintonizada. $\rho_{bb}^{(2)} \ll 1$ es la condición de validez del modelo perturbativo.

## Pendiente

- **Promedio Doppler** de las susceptibilidades y de la propagación de la Rama B. Todo lo de esta carpeta es para el átomo en reposo.
- **Valores marcados `PENDIENTE` en `capitulo3.ipynb`**, porque no están en el PDF ni en `constants.py`: la lista de temperaturas de la Figura 3.1 (`T_C`), la lista de profundidades ópticas de la Figura 3.3 (`OD0_LISTA`), la temperatura `T_FIG` (se cancela al normalizar), y la potencia (`P_SEMILLA`) y la desintonía (`D3_LEJOS`) de la semilla en la sección 5.
- **Longitud de la celda:** `L_celda` es el valor del PDF (71.8 mm), por confirmar con el laboratorio.
- **Magnitudes absolutas:** los momentos dipolares efectivos corresponden a un átomo de dos niveles sin degeneración. Las formas de las resonancias son correctas, pero las magnitudes absolutas llevan un factor de orden 1 por la polarización.
