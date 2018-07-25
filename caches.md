-*- mode: markdown; coding: utf-8 -*-

# Memoria y cachés


## Arquitectura de memorias

- Más ancho de banda que CPU!
- Pero relativamente escaso

Notas:
- Mucho más bandwidth (ej, 150-200GB por segundo contra 25 GB de un CPU, cerca de 10x)
- ... pero ...
- Mucho más poder de cómputo que un CPU (30x cómputo vs. 10x memoria)
- No hay ancho de banda que aguante
- Y muchísima latencia, especialmente comparada con la alternativa de seguir trabajando
- Además el clock del GPU es más lento que CPU, con lo cual la latencia relativa es maás alta (100-200 ciclos vs. 500-1000 ciclos)
- Normalmente, calcular "es gratis" comparado con el resto del trabajo necesario
- Importante optimizar el uso de memoria

Citation:

https://fgiesen.wordpress.com/2011/07/02/a-trip-through-the-graphics-pipeline-2011-part-2/

The first is that GPU memory subsystems are fast. Seriously fast. A Core i7
2600K will hit maybe 19 GB/s memory bandwidth - on a good day. With tail
wind. Downhill. A GeForce GTX 480, on the other hand, has a total memory
bandwidth of close to 180 GB/s - nearly an order of magnitude difference!
Whoa.

The second is that GPU memory subsystems are slow. Seriously slow. A cache
miss to main memory on a Nehalem (first-generation Core i7) takes about 140
cycles if you multiply the memory latency as given by AnandTech by the clock
rate. The GeForce GTX 480 I mentioned previously has a memory access latency
of 400-800 clocks. So let's just say that, measured in cycles, the GeForce GTX
480 has a bit more than 4x the average memory latency of a Core i7. Except
that Core i7 I just mentioned is clocked at 2.93GHz, whereas GTX 480 shader
clock is 1.4 GHz - that's it, another 2x right there


## PCIe

<img src='images/pcie.jpg' height='440' />

Notas:
- Peripheral Component Interconnect Express
- Es la interfaz entre el GPU y CPU.
- No es particularmente importante a menos que pifien.
- 8GB/s en PCIe 2.0 con 16 canales (común)
- CPU lee/escribe memoria de video
- GPU lee/escribe (parte) de la memoria principal
- Antes solía ser algo como AGP


## Mejoras en uso de memoria

- Usar menos (volumen)
- Pedir menos veces
- Laburar más
- Buscar changas

Notas:
- Usar menos memoria (menos precisión, packing, compresión)
- Pedir memoria menos seguido (leer en grupos, leer cuando no hay otra cosa ocurriendo)
- 'Intensidad aritmética' - noción de cuánto se usa ALU vs. memoria
- Normalmente vertex shaders son más intensos que pixel shaders (no necesitan texturar)
- Buscar problemas más grandes en uso de ALUs, para permitir ocuparlos cuando hay stalls


## BLAS y SGEMM - ejemplo práctico

- BLAS - basic linear algebra subprogram (?!?)
- LAPACK - linear algebra
- SGEMM - Single-precision GEneral Matrix Multiply

Notas:
- Subprogram? FORTRAN!
- Operaciones escalares, vectores y matrices
- Utilizado como base de otras soluciones como LAPACK (y mucho de deep learning)
- LAPACK - resolver sistemas de ecuaciones lineales, minimizar cuadrados, factorizar matrices
- Lean licencias de estas cosas!


## BLAS y SGEMM - ejemplo práctico

```
SUBROUTINE SGEMM(TRANSA,TRANSB,M,N,K,ALPHA,A,LDA,B,LDB,BETA,C,LDC)
.. Scalar Arguments ..
REAL ALPHA,BETA
INTEGER K,LDA,LDB,LDC,M,N
CHARACTER TRANSA,TRANSB
.. Array Arguments ..
REAL A(LDA,*),B(LDB,*),C(LDC,*)

 SGEMM  performs one of the matrix-matrix operations

    C := alpha*op( A )*op( B ) + beta*C,

 where  op( X ) is one of

    op( X ) = X   or   op( X ) = X**T,

 alpha and beta are scalars, and A, B and C are matrices, with op( A )
 an m by k matrix,  op( B )  a  k by n matrix and  C an m by n matrix.
```

Notas:
- SGEMM - función general, single general matrix multiply - C := alpha * A * B + beta * C
- beta es una escala de C, puede ser 0 en cuyo caso C está no inicializado
- hay códigos de letras para pedir un transpose


## BLAS y SGEMM - mejoras

- Especificación naive
- Implementaciones buscan usar mejores instrucciones (vectorizadas, fusiones) y acceso a memoria

```
// mac - multiply accumulate
for (int c = 0; c < cols; ++c)
 for (int r = 0; r < rows; ++r)
  dst[r * cols + c] += a[r * cols + c] * b[r * cols + c]
```


## Optimizaciones

- Reutilizar r * col + c en el segundo loop (reuse)
- Salta de row en row, intercambiar loops (loop rotation)
- Test despues de cada 'c', mas instrucciones, mas presion en pipeline, eliminar (loop unroll)


## Nada es gratis en la vida

- Hacer un unroll puede aumentar el numero de registros, sobre todo al reusar valores
- Y aumenta la cantidad de instrucciones para el I$
- ¿Cuánto hacer unroll? Depende del procesador
- Con varios loops, más difícil aún
- Variaciones: buscando alrededor (patrones tipo -1, 0, +1, común en filtros, reducciones)
- Casos horribles: FFT (cada elemento del bloque toca todos los otros, ya lo veremos)


## Impacto - un ejemplo práctico

<img src='images/sgemm-perf.png' height='440' />

Notas:
- Análisis de performance y cómo llegar
- clBlas (OpenCL) vs cuBlas (CUDA)
- El ejercicio muestra una serie de optimizaciones


## Impacto - un ejemplo práctico

- cuBlas: 3056 GFLOPS
- clBlas: 572 (798 'tuned')
- naive: 139
- tiling en groupshared: 373
- múltiples elementos por threads: 689
- tipos vectorizados: 729
- transpose de uno de los inputs: 740
- bloques 2d en registros: 1371
- usando el bloque de textura: 1563

Notas:
- cuBlas 3056 GFLOPS
- clBlas 572 (798 'tuned')
- naive 139
- tiling en groupshared - leer de una de forma explícita, leer de ahí - 373
- múltiples elementos por threads (y menos threads) - 689
- tipos vectorizados - 729
- transpose de uno de los inputs - 740 (460 sin padding por conflictos de banco!)
- bloques 2d en registros - 1371 (pero con problemas de registros y occupancy)
- usando el bloque de textura (CUDA y Kepler) - 1563


## Mejoras que requieren assembler

- Mejor uso de registros
- Prefetching entre bloques
- Mejor paralelismo de instrucciones (ILP)

Notas:
- Mejor uso de registros
- Prefetching de un bloque a otro (usa la mitad de threads)
- Mejor paralelismo de instrucciones (ILP) con un order específico de instrucciones


## Autotuning

- Búsqueda de parámetros en el programa
- OpenCL permite hacer esto
- Fast Computation of General Fourier Transforms on GPUs (MSFT)

Notas:
- https://www.microsoft.com/en-us/research/publication/fast-computation-of-general-fourier-transforms-on-gpus/
- Llegan (como esperado) a saturar el ancho de banda


## Coherencia de unidades

<img src='images/conexion-memoria.png' height='440' />

Notas:
- No todo está conectado directamente!
- Detalles escasos y específicos de hardware, pero aquí hay un ejemplo
- Color y profundidad no pasan por L2, pero las unidades de textura, comandos y control sí!
- Y por supuesto, DMA que le importa un bledo
- En D3D12 y Vulkan, es un grafo de dependencias que informa cómo y cuándo hacer flushes


## Coherencia en shaders

- Varias primitivas de sincronización
- ¿Puede ver datos coherentes mi threadgroup? A veces
- ¿Puede ver datos coherentes mi warp? Siempre

Notas:
- Ejercicio: por qué?

Referencias:
https://cnugteren.github.io/tutorial/pages/page1.html
https://mynameismjp.wordpress.com/2018/03/06/breaking-down-barriers-part-1-whats-a-barrier/
https://fgiesen.wordpress.com/2017/08/14/papers-i-like-part-2/


## Preguntas

