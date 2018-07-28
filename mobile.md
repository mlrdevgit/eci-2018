-*- mode: markdown; coding: utf-8 -*-

# Dispositivos Móbiles

Notas:
https://static.docs.arm.com/100959/0100/arm_guide_for_unreal_engine_4_optimizing_mobile_gaming_graphics_100959_0100_00_en.pdf

Qualcomm Snapdragon Mobile Platform OpenCL General Programming and Optimization Guide
https://developer.qualcomm.com/qfile/33472/80-nb295-11_a.pdf


## Líneas populares

- Qualcomm Adreno (Sony Xperia, Motorola Moto X, HTC One, ZTE, Lenovo)
- PowerVR con Apple y Samsung, PS Vita
- ARM Mali (Samsung Nexus, Samsung Chromebook)
- Tegra de NVidia (Zune, Switch)


## Diferencias

- Menos espacio físico para el GPU
- Integrados en un SoC
- Limitaciones de batería
- Limitaciones de disipación de calor

Notas:
- Menos espacio físico para el GPU
- Integrados en un SoC, con lo cual son menos genéricos a veces, o muy
  afinitizados a alguna plataforma
- Limitaciones de batería
- Limitaciones de disipación de calor. Esto es crítico en dispositivos para
  usuarios finales, utilizándolos en todo tipo de entornos. Hay políticas de
  manejo del dispositivo muy agresivas para mantener esto, porque termina
  siendo un tema de seguridad.


## Consideraciones

- Tile-based rendering, una grilla óptica
- Menos tráfico con memoria principal
- Menos data hazards, menos stalls
- Memoria inmediata más grande, rápida, ayuda, pero menos total
- Requiere order triángulos en el medio del pipeline
- Los tiles son pequeños
- Early-Z (no te queda otra)

Notas:
- Tile-based rendering, una grilla óptica
- Menos tráfico con memoria principal, terminando cada tile en memoria local antes de coordinar con memoria principal, más rápido y menos energía
- Menos data hazards, menos stalls
- Memoria inmediata más grande, rápida (L2 en Tegras, GMEM en Adreno), ayuda con transparencias y antialiasing; menos total
- Requiere order triángulos en el medio del pipeline
- Los tiles son pequeños, 16x16 o 32x32, y se hacen en paralelo
- Early-Z (no te queda otra)


## Limitaciones

- Efectos de pantalla completa (filtros y post-processing)
- Se puede deshabilitar tile-based rendering
- Engañapichanga

Notas:
- Filtros locales funcionan (pero rara vez), pero se puede combinar con frame anterior


## Adreno

- Fibras (threads) de un wave son de 8,16,32,64,128
- Usa latency hiding
- En serie A3x, A4x, no hace coalesce, en la A5x sí, puede agrupar de cuatro
- Soporte de context switches para trabajo de UI
- Límites por tiempo (similar a Windows)
- Cambia voltaje y frecuencia

Notas:
- Fibras (threads) de un wave son de 8,16,32,64,128
- Latency hiding clásico, en el sentido de cambiar wave activo cuando hay
  memoria pendiente.
- Muchas variaciones entre generaciones - avances rápidos, acercándose a PC en
  funcionalidad
- Soporte de context switches para trabajo de UI
- Límites por tiempo (similar a Windows)
- Cambia voltaje y frecuencia; entra en "performance mode" cuando hay mucho trabajo por hacer


## Adreno

- Uso de float16
- float16 es choto en muchos casos, hay que tener cuidado
- Muchas variantes introduces cierta complejidad
- Accesos a través de vectores tienen mejor performance
- Muchas reglas para optimizar, oportunidades de saber todo en SoC

Notas:
- Uso de float16 (común)
- float16 es choto (0-2048 de enteros), pero puede usarse para guardar, y convertir a 32 para operar
- Es malo compilar en tiempo de ejecución, pero también es malo desaprovechar particularidades;
  recomendación es varios binarios, pero también impacta apliación!
- Accesos a través de vectores tienen mejor performance (algo "viejo" para PC)
- Muchas reglas para optimizar, oportunidades de saber todo en SoC


## Alta resolución y HDR

- Uso de celulares de muy cerca
- Muchos pixels! (pero pequeños)
- HDR, mucho mucho HDR, importante para post-processing sobre todo
- Usar MSAA, que es barato por la arquitectura (en Mali, 4x es "casi gratis" según Unreal)
- Usar mipmapping ayuda, a costo de más memoria


## Generalidades

- Muy importante comprimir las texturas que sean soportadas por hardware (ASTC)
- Formato de video correcto, tamaño correcto, para poder usar hardware
- Menos dinamismo y más pre-baking (menos luces que se mueven, por ejemplo)
- Clocks más bajos, tipo 800 MHz
- Evalúen en low clock

Notas:
- Para evaluar performance, intentar correr en low clock continuo, porque el pico de performance no puede mantenerse por mucho tiempo (por calor y batería)


## Preguntas
