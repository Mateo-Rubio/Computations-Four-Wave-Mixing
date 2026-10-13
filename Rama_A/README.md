# Rama A: se siembra 794 nm, se genera 852 nm

El bombeo de 822 nm lleva los átomos de 6S1/2 a 8S1/2 por absorción de dos fotones. La semilla de 794 nm estimula la bajada 8S1/2 → 6P3/2, y el medio radía el campo de 852 nm (6P3/2 → 6S1/2) en la dirección de ajuste de fase, $2k_1 - k_2 = k_3$, es decir, hacia adelante con haces copropagantes.

- Coherencia que radía: $\rho_{ba}^{(3)}$. Término paramétrico: $\propto \tilde E_1^2\tilde E_2^*$.
- Susceptibilidad paramétrica:

$$\chi^{(3)}_A = \frac{N|\mu_{ba}|^2|\mu_{cb}|^2}{\varepsilon_0\hbar^3\,(\Delta_1 - i\gamma_{ba})(\Delta_2 - i\gamma_{ca})(\Delta_3 - i\gamma_{ba})}$$

- **Resonancia de la señal:** $\Delta_3 - i\gamma_{ba}$. Es el mismo denominador de $\chi^{(1)}(\omega_3)$, así que la señal de 852 nm se reabsorbe. En celda gruesa ese factor se cancela y solo queda la resonancia de dos fotones, $I_{852} \propto 1/[(\Delta_1^2+\gamma_{ba}^2)(\Delta_2^2+\gamma_{ca}^2)]$.
- Perillas del laboratorio: $\omega_1$ (822) y $\omega_2$ (794). Con ellas, $\Delta_2 = \omega_{ca} - 2\omega_1$, $\delta_2 = \omega_{cb} - \omega_2$ y $\Delta_3 = \Delta_2 - \delta_2$.

La derivación completa está en el [README principal](../README.md#rama-a-se-genera-852-nm).

## Carpetas

| Carpeta | Contenido | Estado |
|---|---|---|
| [`Teoria/`](Teoria/) | χ⁽¹⁾ y χ⁽³⁾ del átomo en reposo y con promedio Doppler | Hecho; falta χ̄⁽³⁾ completa con Doppler e hiperfina |
| [`Fluorescencia/`](Fluorescencia/) | Etapa 1: fluorescencia azul (PMT) con el 822 solo y con 822 + 794 | Hecho: pico de dos fotones y tres valles hiperfinos |
| [`Deteccion_852/`](Deteccion_852/) | Etapa 2: detección directa hacia adelante a 852 nm (monocromador + SPCM) | Medido: sin señal por encima del fondo |

Las medidas usan los haces caracterizados en [`../Caracterizacion_Haces/`](../Caracterizacion_Haces/).

## Montaje común a las dos etapas

- Láser de 822 nm (L820P100) y de 794 nm (L785P090, con aislador óptico y filtrado espacial con pinhole), combinados en un PBS. Los haces son copropagantes y tienen polarizaciones lineales ortogonales.
- La λ822 se monitorea con un medidor de longitud de onda, que es el que aparece en las columnas de λ y ν de los archivos.
- Celda de Cs a 80 °C.
- PMT a 90° del haz conectado al contador QuTau (canal A). Cuenta la fluorescencia azul (455/459 nm) de la cascada 8S → 7P → 6S, que es proporcional a la población de 8S1/2 y por eso marca $\Delta_2 = 0$.

## Pendiente

- Identificar el origen del fondo del canal B: bloquear cada láser por separado y medir con ambos apagados.
- Calibrar el monocromador y medir su ancho de banda en 852 nm.
- Hacer espectroscopía de absorción en la D2 a la temperatura de trabajo, para medir la reabsorción κ de la señal.
- Barrer Δ794 y la temperatura buscando la señal.
