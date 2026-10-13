# Rama A: teoría

Evaluación numérica de las susceptibilidades de la Rama A. No hay archivos de datos: todo se calcula a partir de [`constants.py`](../../constants.py).

**Convenciones:** todo en SI. Las frecuencias angulares y las desintonías están en rad/s, y las gráficas muestran $\Delta/2\pi$ en MHz. Niveles: $|a\rangle = 6S_{1/2}$, $|b\rangle = 6P_{3/2}$, $|c\rangle = 8S_{1/2}$.

**Parámetros provisionales:** $N$, $|\mu_{ba}|$ y $|\mu_{cb}|$ valen 1. Solo multiplican toda la expresión, así que no cambian la forma de las curvas, y todas las gráficas se muestran normalizadas.

## `Susceptibilidades.ipynb`: átomo en reposo

1. **Constantes:** importa de `constants.py` las frecuencias, longitudes de onda, números de onda y decaimientos.
2. **De las perillas a las desintonías:** a partir de $(\Delta_2, \delta_2)$ obtiene $\omega_1 = (\omega_{ca} - \Delta_2)/2$, $\omega_2 = \omega_{cb} - \delta_2$ y $\omega_3 = 2\omega_1 - \omega_2$, y de ahí $\Delta_1$ y $\Delta_3 = \Delta_2 - \delta_2$.
3. **Comprobaciones:** ajuste de fase en vacío $2k_1 - k_2 - k_3 \approx 0$; la identidad $\Delta_3 = \Delta_2 - \delta_2$ con desintonías al azar; y que $\Delta_1/2\pi \approx -12.8$ THz, con $|\Delta_1|/\gamma_{ba} \gg 1$, es casi constante al mover $\Delta_2$.
4. **χ⁽¹⁾(ω3)**, ec. (2.49): absorción y dispersión, una lorentziana de ancho natural $\gamma_{ba}$.
5. **Cortes de |χ⁽³⁾|²**, ec. (2.54): (a) se barre el 822 con $\delta_2 = 0$, que da el producto de dos lorentzianas; (b) se barre el 794 con $\Delta_2 = 0$, que da una lorentziana de ancho $\gamma_{ba}$.
6. **Mapa de |χ⁽³⁾|²** en el plano $(\Delta_2, \delta_2)$: una línea vertical en $\Delta_2 = 0$ (dos fotones) y una diagonal en $\Delta_3 = 0$ (señal resonante con la D2).
7. **Celda ópticamente gruesa:** $|\tilde E_3(L)|^2 \propto 1/[(\Delta_1^2+\gamma_{ba}^2)(\Delta_2^2+\gamma_{ca}^2)]$; solo sobrevive la línea $\Delta_2 = 0$.

Figuras que guarda en esta carpeta: `chi1_natural.pdf`, `chi3_squared.pdf`, `map_chi3_squared.png`, `thick_cell.png`.

## `Suceptibilidades_Doppler.ipynb`: promedio Doppler

Promedia sobre la distribución de velocidades $W(v) = e^{-v^2/u^2}/(\sqrt\pi u)$ usando la función de dispersión del plasma $Z(\zeta) = i\sqrt\pi\,w(\zeta)$ (`scipy.special.wofz`):

- $\bar\chi^{(1)}(\omega_3) \propto Z(\zeta_b)$, con $\zeta_b = (-\Delta_3 + i\gamma_{ba})/(k_3u)$. Su ancho es Doppler (≈ 376 MHz) y no natural.
- El factor Doppler de $\bar\chi^{(3)}_A$, $\left|\dfrac{Z(\zeta_a) - Z(\zeta_b)}{\zeta_a - \zeta_b}\right|$, con $\zeta_a = (-\Delta_2 + i\gamma_{ca})/(2k_1u)$, mapeado en el plano $(\Delta_2, \Delta_3)$. La cresta queda en $\Delta_3 = (k_3/2k_1)\,\Delta_2$, la clase de velocidad resonante a la vez con los dos fotones y con la D2.

Figuras: `chi-1.png` y `figuras/fig4_2_chi3_doppler.pdf`. La subcarpeta `figuras/` tiene que existir antes de ejecutar.

**Ojo:** `u` se calcula con `T[K]` de `constants.py` (296 K), no con los 80 °C de la celda.
