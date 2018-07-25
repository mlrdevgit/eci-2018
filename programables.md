-*- mode: markdown; coding: utf-8 -*-

# Unidades programables

Notas:
http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15869-f11/www/lectures/07_gpucore.pdf
http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15869-f11/www/lectures/mantor_AMD_CMU_10_2011.pdf 32,33


## Configuración vs. programación

- Modelo de luz
- Texturas asociadas a objectos
- Tipo de sampling y mezcla de colores
- Efecto de niebla
- "Árboles" de shading: reflectividad difusa, especular, coeficientes por material

Notas:
- En las primeras APIs, era todo configuración
Configuración de una serie de operaciones comunes:
- modelo de luz
- texturas asociadas a objectos
- tipo de sampling y mezcla de colores
- efecto de niebla
- "árboles" de shading: reflectividad difusa, especular, coeficientes por material


## Limitaciones de configuración

<img src='images/ogre-fresnel.jpg' height='440' />

Notas:
- Imposible hacer efectos más raros
- fresnel reflections en OGRE
- Simulación de luz 'doblada' cuando cruza superficie


## ¿Qué cosas son programables?

- El hardware puede ser más flexible en algunos casos
- Modelo de shaders: proceso de triángulos, geometría, pixels
- Son las mismas unidades para todo (no fue el caso los primeros años programables)
- Mismas unidades para cómputo


## SGI RealityEngine (1993)

<img src='images/programables-01.png' height='440' />

Notas:
- distintas unidades para geometria, vertices, rasterizacion, pixels (fragments)
- programables pero no por aplicación, sólo a través de API de configuración


## NVIDIA GeForce 6800 (2004) 

<img src='images/programables-02.png' height='440' />

Notas:
- programables pero separados


## NVIDIA GeForce 8800 (Tesla, 2006)

<img src='images/programables-03.png' height='440' />

Notas:
- programables y unificados
- en el 2007, disponibles por CUDA
- todavía quedan unidades de función fija!


## Diferencias con CPU

- No hay data cache por unidad de ejecución
- No hay ejecución fuera de orden
- No hay branch predictor copado
- No hay prefetcher automático de memoria
- ¿Qué queda? fetch, decode, execute, execution context

Notas:
- eliminamos las cosas que ayudan a una única secuencia de ejecución


## Menos es más

- Amortizar fetch y decode, y tener un grupo de execute y execution context
- Hay un poco de execution context que también se comparte
- "SIMT" (single instruction multiple thread)
- Coherencia(s): ejecución y datos

Notas:
- Amortizar fetch y decode, y tener un grupo de execute y execution context
- Hay un poco de execution context que también se comparte
- "SIMT" (single instruction multiple thread)
- Coherencia de ejecución: no hay ramas diverentes
- Coherencia de datos: datos locales usan bien el caché
- ¡Ojo que son dos ideas distintas de coherencia!
- Coherencia de ejecución también es "ejecución uniforme"


## Uniformidad de datos

- La información puede ser la misma en cada thread o única a cada thread
- Se necesitan 'n' registros para divergentes, 1 para uniformes
- Es bueno que sea uniforme
- Ayuda a ejecución uniforme

Notas:
- Ejercicio: ¿qué es uniforme? ¿qué es divergente?


## Uniformidad de ejecución

Todos tienen que tomar la misma decisión
Datos uniformes ayudan
Es necesario usar una máscara en otros casos
Quad mode es un dolor de muelas
Ejemplo:
Ejercicio: ¿qué es uniforme? ¿qué es divergente?


## Stalls

- Latencia alta, dá fiaca esperar
- Ejecución de otro wavefront (AMD) o warp (NVidia)
- Cada warp se come algunos registros, hay que particonar el banco
- Partición de execution context

Notas:
- Acceso a memoria puede ser problemático
- Hay que esperar a que vuelvan los resultados
- Ejecución de otro wavefront (AMD) o warp (NVidia)
- Cada warp se come algunos registros, hay que particonar el banco
- El execution context se particiona (si entran, según requerimientos como registros)


## Más es más

- Paralelismo de instrucciones por unidad (tipo)
- No necesariamente corre un único warp en un procesador

Notas:
- Puede haber más de una unidad de proceso accessible a la vez para paralelismo de instrucciones
- Por ejemplo, pedir un dato de memoria y hacer una multiplicación
- Con lo cual, no necesariamente corre un único warp en un procesador
- Pueden correrse dos a la vez, por ejemplo, y tomar turnos para uso de FPU, ALU(i), mem, etc


## Preguntas

