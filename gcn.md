-*- mode: markdown; coding: utf-8 -*-

# Arquitectura de ejemplo: GCN


## Motivación

- Comportamiento
- Performance
- Utilización
- Bloques y sus interfaces

Notas:
- Es importante entender cómo funciona para poder razonar sobre comportamiento, performance y utilización.
- Cubre bloques de funcionalidad, interfaces internas, interfaces externas, programación.
- Otras cosas que importan menos: formato de código.


## Diagrama de bloques

<img src='images/amd-gcn3-blocks.png' height='440' />

Notas:

Empecemos por las interfaces con el mundo exterior: acceso a memoria por DMAs,
que entran por L2 o proceso de comandos.

Las conexiones son con bancos de memoria locales o compartidos con el sistema;
en casos de acceso uniforme de memoria (UMA) tipo consolas, todo es
compartido, aunque pueden tener distintos tipos de canales con distintas
características de performance y coherencia.

Uno de los canales de información es por MMIO, memory-mapped IO.

Noten que faltan cosas importantes, como el controlador de video.

Luego hay una jerarquía de memorias, L1, Global Data Share, y finalmente
LDS. Es importante ver que la jerarquía no es estricta.

La ejecución va por cuenta de las unidades en los 'compute units'. Noten que
hay un único 'program counter', cuatro grupos de valu y vgprs, y un salu y
sgpr. Los vectores pueden considerarse un hilo de ejecución, pero se agrupan
por eficiencia.

Otros bancos especiales son el de constantes, que no puede ser modificado
(evidentemente falta algo acá) y el caché de instrucciones, que es distinto
que el de datos, con lo cual de nuevo coherencia e invalidación va a ser algo
distinto.


## Datos Compartidos

<img src='images/amd-gcn3-mem.png' height='440' />

Notas:

Este diagrama tiene más detalles. Cada compute unit tiene 64KB propios de LDS,
comparte 64KB de GDS con los otros. Cada SIMD tiene 32x256 registros vector, y
32x800 escalares compartidos entre todo el CU.


## Estado de procesadores

- Contador de programa
- Máscara de ejecución
- Yuyos varios

Notas:

Yuyos varios:

- bitmask de resultados booleanos (uno por lane)
- bit compartido de resultados
- prioridad de wave
- variables para manejar traps
- exportación


## Flujo de control

<img src='images/flujo-control.png' height='440' />

Notas:
- DAG de flujo, ejemplo típico diamante
- Más fácil manejarlo de forma estructurada (concepto de reducibilidad)
- Es necesario linearizarlo y lidiar con divergencia


## Flujo de control

<img src='images/flujo-control-flat.png' height='440' />

Notas:
- Es necesario linearizarlo y lidiar con divergencia
- Manejo de máscara de ejecución, escalar
- Saltos escalares, directo o como optimización
- Asignaciones condicionales
- Mucho cuidado con interferencia de valores!


## Flujo de control - complicaciones de pixels

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <use xlink:href='images/derivadas-pixels.svg#svg8'></use>
</svg>

Notas:
- Uso de deltas en lugar de derivadas, ddx, sampling.
- Requiere instrucciones especiales para manejo de quads.
- Puede causar problemas con lanes que no deberían correr.
- El compilador puede quejarse, pero a veces es ambiguo porque depende de
  valores en tiempo de ejecución.


## Scheduling

- Input assembler
- Shader de vértices
- Rasterización
- Shader de píxeles

Notas:
- Input assembler
- Shader de vértices, cuántos CUs reservar
- Rasterización, exportación de vértices, interpolación, coordenadas baricéntricas
- Sin saber el tamaño de pixels por triángulo, difícil de arreglar de antemano
- Shader de píxeles, exportación de pixels
- Trucos de driver: empezar vértices antes de la reservación, reservar un CU para pixels


## Operaciones

- Aritmética, movimiento, comparaciones
- Trascendentales
- Lectura o escritura fuera de rango con comportamiento definido
- Operaciones de memoria 'planas'
- Operaciones de textura, con conversiones de tipos o patrones de memoria
- Control de flujo, máscaras de ejecución

Notas:
- Aritmética, movimiento, comparaciones
- Aproximación de funciones trascendentales, completadas con Taylor o algo por el estilo
- Lectura o escritura fuera de rango con comportamiento definido
- Operaciones de memoria 'planas'
- Operaciones de textura, con conversiones de tipos o patrones de memoria
- Control de flujo, máscaras de ejecución


## Presión de registros

- Registros escalares (rara vez)
- Registros de vector

Notas:
- Dentro de un CU, pueden estar corriendo varios waves a la vez
- El límite, 'ocupación' (occupancy), típicamente está dado por la cantidad de
  registros de vector
- Puede ser escalares, pero es más raro - casi todo es vector, y puede ser
  reemplazado por vector


## Unicornios

- Shaders que andan más lentos cuando tienen más ocupación.

Notas:
- Suelen ser problemas de patrones de acceso a memoria aleatorios, donde los
  cachés hacen trashing y termina todo siendo más lento.


## Otras cosas que faltan

- Rasterizador.
- Programación de samplers.
- Programación de output blends (exports).

Notas:
- Esto lo termina haciendo internamente la placa.
- Depende mucho del vendor, y va cambiando a medida que cambian los formatos
  de imagen y de compresión - cómo van poniendo pixels sobre memoria.


## Preguntas

