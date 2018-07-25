-*- mode: markdown; coding: utf-8 -*-

# Unidades de función fijas


## Generalidades

- Las unidades de función "fija" son las que configuramos en vez de escribir shaders
- Suelen utilizar hardware dedicado
- Servicios o bloques entre etapas

Notas:
- Las unidades de función "fija" son las que configuramos en vez de escribir shaders
- Algunas son de hecho programables, pero es un detalle de implementación del IHV o de la plataforma
- Suelen utilizar hardware dedicado
- Aparecen como bloques entre unidades programables en el pipeline, o para servicios en particular


## Generalidades

<img src='images/pipeline.png' height='440' />

Notas:
- Fijas: input assembler, tesselator, stream output, rasterizer, output merger


## Input Assembler

- Alimenta a las unidad de vertex shading
- Según descripción
- "Masaje" de índices
- Si no hay índices, los "inventa"

Notas:
- Función es alimentar a las unidad de vertex shading
- Según descripción (configuración), lee datos, provee índices
- "Masaje" de índices para reutilizar datos si es necesario, por ejemplo porque algunos vértices son compartidos
- Normalmente con su propio cache para "masajes" y por coherencia (los índices suelen apuntar a vértices cercanos)
- Si no hay índices, los "inventa"


## Tesselation

- Genera patches (grupos de triángulos)
- Elimina casos degenerados
- Ocurre antes de rasterización
- Importante definir hasta cuánto pueden multiplicarse los patches, porque
  puede influir implementación.
- Dentro de la misma unidad de cómputo, "cerca", en memoria

Notas:
- Ejemplo de implementación - en banco dedicado, en banco compartido, en memoria


## Rasterization

- Pila de configuración: viewports, scissors, perspectiva, profundidad, multisampling
- Corta trabajo oportunísticamente como teselización
- Algoritmo general es generar ecuaciones para cada línea del triángulo y
  hacer loops por cada pixel.
- Testeo de Z.

Notas:
- De nuevo, pila de configuración: viewports, scissors, perspectiva, profundidad, multisampling
- Como en teselización, aprovecha para eliminar geometría innecesaria
- Como en teselización, está atado a cuánta información se genera (aunque de manera más transparente)
- Por ejemplo, triángulos muy grandes pueden partirse en triángulos más pequeños, para que al
  rasterizar se puedan correr todos los pixels con buena utilización
- Algoritmo general es generar ecuaciones para cada línea del triángulo y hacer loops por cada pixel,
  donde hay un test de que cada punto esté del lado correcto de las tres líneas.
- Testeo de Z para no enviar pixels al shader si están detrás de algo. Variante early y late.


## Procesador de comandos

- CP - command processor
- Interrupción o registros
- Sincronización por barreras
- Los comandos incluyen instrucciones de ejecución, barreras, mantenimiento de estado

Notas:
- CP - command processor
- Se maneja por interrupciones de la CPU o (más comúnmente) escribiendo registros
- La secuencia de comando de CPU incluye barreras (fences)
- Las barreras 'aparecen' cuando se escribe un valor particular a un registro, que aparece en memoria por PCIe
- Tiene un prefetcher para mantenerse ocupado
- Los comandos incluyen instrucciones de ejecución, barreras, mantenimiento de estado


## Texture samplers

- Configurados por tres cosas:
 - sampler state (modo de filtrado, direccionamiento, grado de anisotropía máxima)
 - qué textura utilizar (memoria)
 - SRV (configuración de cómo interpretar la memoria, ej `PIXEL_FORMAT_R8G8B8_SNORM`
- Operación depende de la instrucción (distintas formas) y el recurso (1d, 2d, cubo, etc)

Notas:
- SRV es la información que vemos por ejemplo en la configuación de un shader
  resource view en d3d11, [`D3D11_SHADER_RESOURCE_VIEW_DESC` structure](https://docs.microsoft.com/en-us/windows/desktop/api/d3d11/ns-d3d11-d3d11_shader_resource_view_desc)

## Texture samplers

- Varias entradas para 2d: coordenadas normalizadas u,v, y derivadas parciales de u y v en "x" de pantalla, y en "y" (6 floats)
- Salida: valores numéricos (en registros o memoria compartida)
- Anisotropic: mejor para ángulos oblicuos
- En pixel shaders, las derivadas tiene truco

Notas:
- Entrada para 2d: coordenadas normalizadas u,v, y derivadas parciales de u y v en "x" de pantalla, y en "y" (6 floats)
- Las derivadas se utilizan para elegir mip levels y el tamaño del kernel de filtro
- Salida: valores numéricos (en registros o memoria compartida)
- Anisotropic (no - mismo - trópico): el filtro no es el mismo en todas las direcciones - mejor para ángulos oblicuos
- En pixel shaders, las derivadas tiene truco


## Texture samplers

<img src='images/anisotropic.png' height='440' />


## Texture samplers

- Capaz de comerse todo el ancho de banda!
- Buen punto para hacer tradeoff de calidad vs. performance

Notas:

Se pueden comer varios GB/s sólo en texturas (con 0.9 millones de pixels en
720p, unos 10 samples por pixel con un poco de overdraw y post-proceso), son
unos 10 millones de samples en un frame. A 30fps, son unos 300 millones de
samples. A 10 bytes por sample (asumiendo que las derivadas no van y que hay 2
o 3 floats), son 3GB/s. Este es el tránsito, sin overhead, de cores a unidades
de textura.

Pero las lecturas no son individuales, es todo el wave - entre 16 y 64.


## Texture samplers

- Clásica unidad fija
- Cálculo de gradientes, mip, direccionamiento, cubemaps, cálculo de
  direcciones, manejo de bordes, etc... todo lo que configuramos!

Notas:

La unidad tiene que calcular los gradients si no los tiene, el nivel de mip si
no los tiene, aplicar el modo de direccionamiento (wrap, clamp, etc.),
calcular la cara del cubemap si necesario, calcular puntos en la textura, y
calcular dónde están en memoria. Y cosas raras con bordes y otros yuyos.

Tiene un par de niveles de cache, donde el más próximo puede descomprimir
datos de a bloques. Bilinear consiste en tomar cuatro muestras y multiplicar
para tener la razón correcta de cada uno (MACs!); trilinear hace dos bilinears
e interpola; en un loop modificado en los casos que necesita tocar más de un
mip porque está en ángulo.


## DMA

- Direct Memory Access
- "Move Engine"
- Para no usar cores en copiar memoria de acá para allá


## MMU

<img src='images/gpu-memory.jpg' height='440' />

Notas:
- Memory Management Unit
- Para configurar acceso a memoria
- Entre bus de PCIe y los controladores internos


## Vestigios

- Soporte de modo VGA
- Soporte de modo texto

Notas:
- Cero necesidad de programación - enteramente configurable


## Más indirecciones

- Proceso de comandos
- Control de scheduling


## Preguntas

