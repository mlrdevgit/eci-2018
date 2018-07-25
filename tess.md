-*- mode: markdown; coding: utf-8 -*-

# Tessellation

Notas:
- DirectX 11 Tessellation - NVidia: http://www.nvidia.com/object/tessellation.html
- Tessellation Stages: https://msdn.microsoft.com/en-us/library/windows/desktop/ff476340(v=vs.85).aspx
- More: http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15869-f11/www/lectures/moreton_talk.pdf


## Tessellation

<img src='images/tess-prog.png' height='440' />


## Técnica

- "Tessella" eran pequeños piezas utilizadas para mosaicos.
- La idea es generar muchos "tiles" de un polígono, cubriéndolo.
- Teselar (no confundir con "texels") no es útil sin hacer más trabajo.

Notas:
- Se puede utilizar con 'displacement maps', que indican cómo empujar los triángulos
- La alternativa más barata, sin teselar, es 'bump mapping', pero no genera geometría
- Sin geometría, no hay intersecciones para luces por ejemplo, no hay sombras


## Técnica

<img src='images/model-comparison.jpg' height='440' />

Notas:
- Viendo el contorno del modelo del medio, con bump mapping, vemos que nada sobresale, porque no hay geometría ahí
- Viendo displacement mapping, además de contorno, vemos que hay más sombras


## Implementación

- Hay tres partes: hull shader, tesselator, domain shader
- Hull shader - recibe patches y produce patches de geometría
- Tessellator - función fija, genera samples
- Domain shader - calcula vértices en base a samples


## Hull shader

<img src='images/d3d11-hull-shader.png' height='440' />

Notas:
- Recibe puntos de control
- Emite puntos de control, factor de teselación (cuántos producir) y constantes por patch
- Las constantes pueden usarse en el domain shader
- En HLSL escrito como dos funciones, una para los puntos de control que generan un patch,
  otra que puede correr en paralelo generando constantes para ese patch


## Tessellator

- Crea más geometría en base a los puntos de control y cuánto teselarlos
- Se encarga de eliminar patches con NaNs, factor de teselación cero
- Ciertos cálculos hechos en menor precisión (pero un detalle, realmente)


## Domain shader

<img src='images/d3d11-domain-shader.png' height='440' />

Notas:
- Parecido a un vertex shader, pero con más detalles
- Tiene acceso a cada coordenada sobre geometría, sus puntos, constantes de patch y factores de teselación
- Produce la posición final de vértice


## Usos

- Displacement mapping
- Pelo: hairworks (en contraste con TressFX)
- Competencia

Notas:
- https://scalibq.files.wordpress.com/2011/12/hd-7970-dx11-tessellation.png?w=640


## Geometría

- Se encuentra después de tessellation
- Toma geometría entera, es decir, puntos, líneas, triángulos
- Opcionalmente, geometría adyacente también
- Permite emitir geometría y topología, emitiendo un vértice a la vez
- PointStream, LineStream, TriangleStream


## Geometría

<img src='images/d3d11-gsinputs2.png' height='440' />

Notas:
- https://msdn.microsoft.com/en-us/library/windows/desktop/bb509609(v=vs.85).aspx


## Utilización

- Deformar 'viendo' múltiples vértices a la vez
- Simplificar geometría, eliminarla, hacer cálculos por triángulo en vez de vértice
- Cuando hay valores de sistema que tienen que ser consistentes, típicamente usa el primero
- La cantidad de vértices es dinámica pero el número máximo se declara en tiempo de compilación


## Técnicas en shaders de geometría

- Point Sprite Expansion
- Dynamic Particle Systems
- Fur/Fin Generation
- Shadow Volume Generation
- Single Pass Render-to-Cubemap
- Per-Primitive Material Swapping
- Per-Primitive Material Setup

Notas:
- material setup including generation of barycentric coordinates as primitive data so that a pixel shader can perform custom attribute interpolation (for an example of higher-order normal interpolation, see CubeMapGS Sample).


## Sistema de partículas

- Número limitado
- Comportamiento limitado
- Facil de manejar, pero tiene que ser renderizado con el pipeline normal
- Normalmente no cuenta para varios efectos (sombras y demás)

Notas:
- Normalmente no se crean y destruyen, se reciclan instancias.
- No tienen geometría normal, pero se puede generar a partir de buffers de puntos.

## Preguntas

