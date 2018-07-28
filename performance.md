-*- mode: markdown; coding: utf-8 -*-

# Performance

Notas:

Referencias

The Peak-Performance Analysis Method for Optimizing Any GPU Workload
https://devblogs.nvidia.com/the-peak-performance-analysis-method-for-optimizing-any-gpu-workload/


## Medidas de performance

- Latencia y throughput
- Energía

Notas:
- Latencia
- Los diagrmas de 'lanes' son comunes cuando hay varios procesos que pueden
  ocurrir en paralelo para ver latencia.
- Energía es más importante en dispositivos móbiles


## Metodología

- No sabemos nada a priori
- Objetivos (percepción!)
- Presupuesto de performance
- Medidas
- Cambios

Notas:
- Es importante no asumir
- Un pequeño defecto puede destruir performance, con lo cual es crítico medir
- Para cargas de juego, la percepción es fundamental
- Presupuesto - hablamos hace momentos


## Presupuestos

- Número de triángulos
- Ciclos de proceso en CPU
- Ciclos de proceso por vértices
- Ciclos de proceso por pixel (ojo con overdraw)
- Ancho de banda
- Cantidad de memoria

Notas:
- Algunos de éstos se pueden usar como una muy cruda aproximación.
- Por ejemplos, número de triángulos depende de dónde están y cuánto trabajo
  de pixel generan.
- A la hora de modelar, sin embargo, es útil como proxy.
- Y también para cosas como tamaño de memoria para buffers de vértices e índices.


## Herramientas

- Configuración del sistema operativo
- Configuración de hardware y drivers
- Captura dentro del programa
- Captura desde fuera del programa
- Análisis de capturas
- Profilers de CPU, GPU, memoria, batería

Notas:
- En el sistema operativo, buscamos estabilidad
- Hardware puede operar con distintos voltajes
- El driver normalmente va a cambiar performance
- A veces viene con optimizaciones ya incorporadas
- A la vez, tienen la opción de pedirle medidas de performance (DX queries)


## Estabilidad

- Calidad en programa
- Ojo con técnicas dinámicas, ahorro de energía, async compute y copy

Notas:
- Configuración estable de calidad en el programa: repetir y mejorar
- Cuidado con técnicas de adaptación, como bajar resolución o bajar calidad
- SetStablePowerState(TRUE) en dev mode
- Ojo con async compute y async copy, no siempre bien soportado


## Capturas

- Contienen todos los comandos y datos
- Muchas veces con anotaciones del programa
- Producidas por herramienta de hardware (ej NSight) o generales (PIX y RenderDoc)
- Corre el programa en un modo especial (según qué componente hace instrumentación)
- Funcionan por re-ejecución

Notas:
- Las capturas pueden ser bastante grandes.
- Una buena captura vale oro.
- Buenas para investigación, y para hacer baselining contra cambios que no
  controlan, por ejemplo versiones de driver o de sistema operativo.


## Vistas de capturas

<img src='images/perf-timing-capture.png' height='440' />

Notas:
- Muestra detallada de sistema
- Línea de tiempo con actividades
- Eventos incluyen comandos de aplicación, eventos internos de driver o del sistema operativo

## Vistas de capturas


<img src='images/perf-gpu-memory.png' height='440' />

Notas:
- Manejo de recursos
- Assembler


## Estrategia

- Baja utilización en general? Buscamos aumentar
- Alta utilización? Si actuá como cuello de botella, mover trabajo


# Estrategia

<img src='images/perf-sol-guia.png' height='440' />

Notas:
- La herramienta de NVidia usa (SOL %) como guía
- SOL = 'speed of light', el maximo teorico


# Estrategia

<img src='images/perf-sol-ranking.png' height='440' />

Notas:
- Tiene un ranking, con porcentajes por recurso
- Alta utilización más del 80%, menos de 60% es baja


## Ejemplos

- Alta utilización de ALU
- Cuello de botella en texturas
- Input Assembler o vertex shaders
- Mucho trabajo en pixel shaders
- Baja utilización en general
- Global

Notas:
- Alta utilización de ALU ("SM" en NVidia): lookups, mejoras algorítmicas, saltear trabajo
- Cuello de botella en texturas: menos taps (bajar calidad), formatos más pequeños de pixels (sacar alfa antes, otro frame, o CPU)
- Input Assembler o vertex shaders: usar CPU para enviar menos geometría, índices más pequeños, datos más compresos
- Mucho trabajo en pixels: anticipar o aproximar trabajo en vértices, ajustar después, usar modelos con menos detalles y LOD
- Baja utilización en general: stalls de memoria (menos, más pequeño, leer menos y compartir, leer menos y estimar o recalcular)
- Global: combinar trabajos de distintos tipos, partir trabajo y hacer scheduling de a partes


## Utilización

- El CPU envía suficiente trabajo?
- Hay un cuello en algún componente?
- Hay burbujas?

Notas:
- Con burbujas: cambio de trabajo o dependencias, evaluar necesidad, evaluar rescheduling
- GPU Idle % en NVidia para utilización
- En d3d12, la aplicación tiene más control sobre 
- Fundamentalmente, en 12, la aplicación puede hacer adaptaciones predictivas
  que un driver jamás puede hacer.


## Utilización

<img src='images/perf-sol-registros.png' height='440' />

Notas:
- Para esconder latencia, más waves, pero limitado por recursos (normalmente registros)


## Utilización

<img src='images/perf-sol-ratios.png' height='440' />

Notas:
- Cuánto trabajo de textura vs. cuánto trabajo de ALU.


## Utilización

- Context rolls, pre-12 (donde se reconfigura cómo VS y PS interaccionan)
- Límite en cantidad de atributos, si se comen todo el espacio de scratch entre fases
- El tamaño de groupshared en compute shaders


## Energía

- El mayor impacto es poder apagar partes
- Memoria, unidades de cómputo
- Bajar la frecuencia del reloj es lo más común


## Recap

- Empiecen de presupuesto
- Midan lo que necesitan
- Busquen sus cuellos de botella y dónde tienen recursos disponibles
- Reduzcan el problema total o muevan trabajo de sistemas saturados a sistemas disponibles


## Preguntas

