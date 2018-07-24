# Lenguajes de programación: GLSL, MetalSL, HLSL

Notas:
- ¿Qué lenguajes de programación hay en uso?
- ¿Qué diferencia tienen?
- ¿Cuáles son los elementos de cada lenguaje?


## Tipos de lenguaje

- Lenguajes para tareas gráficas.
- Lenguajes para tareas de cómputo.
- Diferencias: funciones fijas, punteros, memoria, integración con código de CPU.


## HLSL

- El lenguaje de DirectX.
- El lenguaje es más expresivo que los programas que pueden ejecutarse.
- Originalmente reemplazaba a configuraciones de rendering con efectos fijos,
  como texturas sobre polígonos o efectos de niebla.
- El principio de diseño es que todo lo expresable en HLSL puede correr en cualquier
  dispositivo de gráficos, sólo limitado por la capacidad del dispositivo.


## GLSL

- El lenguaje de OpenGL y WebGL.
- Muy parecido a HLSL, pero con algunas diferencias históricas.
- Tiene extensiones comunes (ARB) y específicas de fabricante.


## MetalSL

- Derivado de C++, no tan integrado como CUDA pero muy parecido a código de CPU.
- Específico de Apple y Metal, inicialmente iOS y después MacOS.
- Soporte de punteros.
- Mucho más flexible que lenguajes gráficos, pero a veces la implementación no ha soportado bien.


## OpenCL, CUDA

- Variantes de C o C++.
- Integración de código de CPU 'host' o GPU 'device'.
- Más flexibles que lenguajes gráficos.
- Soporte de punteros, muchas veces integrando distintos tipos de memoria.
- Poco soporte para unidades de función fija de gráficos.
- Menos eficientes en cuanto no reflejan arquitectura de GPU.


## Tipos fundamentales

- Preferencia por punto flotante
- float, double
- int, uint, bool
- A veces: float16, int16, int8; variantes min
- Muy raro: float8, float4 


## Vectores

- Son siempre un número fijo de tipos fundamentales
- Accesso de valores por `xyzw` o `rgba`, o por operador []
- 'Swizzle': `a.xwz = b.yyw;`
- `vector<float, 4>`, `float4`, `vec4`
- El tipo más común
- Legado histórico pero mantiene vigencia por practicidad
- Muchas conversiones implícitas


## Matrices

- `row_major`, `col_major`, pero sólo en memoria
- HLSL es row major, GLSL es column major
- Accesso de valores por [], _m00 o 11
- Swizzle suele no ser usado tan comúnmente
- matrix<float, 4, 4>, float4x4, mat4
- operadores son por componente, mul() funciona como dot()


## Precisión numérica

- Rara vez IEEE
- No hay signaling NaNs
- Problemas con NaN, INFs
- Manejo de números subnormales (denorms): normalización de entrada o salida
- Precisión y ordenamiento de operaciones: problemas con z-fighting


## Recursos y tipos de memorias

- Tipos de recursos fundamentales: constant buffers, texturas, buffers
- Algunos tipos especializados: `AppendBuffer`, `ConsumeBuffer`
- Algunos tipos mezclados: `TextureBuffers`, `TypedBuffers`


## Samplers

- Recurso accesorio para uso de texturas
- Configuración de operación de sampling, lectura de textura
- Parte de recursos a veces, a veces parte del programa, típicamente parte de
  unidades fijas pero fáciles de configurar


## Funciones de entrada

- Una unidad de compilación por función en el modelo clásico
- Dependientes de punto de proceso gráfico
- Determinan cómo encajan con otras partes del pipeline, sobre todo para datos de usuario
- Más flexible en cómputo, aunque es más opaco al distribuidor de tareas (triángulos vs. pixels)


## Valores de sistema

- Datos que normalmente son producidos por hardware o coordinados con un driver
- También usados para variables de escritura, como color de salida
- Ejemplos: posición de vértices, posición de pixels, valores de profunidad
- En cómputo, identificadores de thread y grupo, usados para manejar tareas


## Anotaciones

- Información estática sobre el programa
- Asociados comúnmente a funciones, a veces bloques
- Asociados a variables (distinta sintaxis en HLSL)

Notas:
- Por ejemplo: el tipo de primitivo geométrico, la configuración de grupos en
  un shader de cómputo, el registro o binding que se usa para encontrar
  recursos


## Funciones intrínsicas

- Librería básica de funciones matemáticas
- Funciones adicionales para memoria: interlocked
- En CUDA, manejo dinámico de recursos y ejecución


## Generación de código

- Optimización agresiva
- Inlining
- Unrolling
- Flattening
- Lectura de memoria especulativa y anticipada al uso
- Cuidado: presión de registros, desborde de caches

