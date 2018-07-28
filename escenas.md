-*- mode: markdown; coding: utf-8 -*-

# Escenas

Notas:
https://www.3dgep.com/forward-plus/

http://www.adriancourreges.com/blog/2017/12/15/mgs-v-graphics-study/


## Problema

- Tengo un grafo de escena
- ¿Cómo los dibujo?
- Pases, técnicas

Notas:
- Pases son una única operación, usualmente que camina el grafo
- Técnicas son combinaciones de pases para ejecutar algo.


## Forward Rendering

<img src='images/escenas-forward.png' height='440' />

Notas:
Caso clásico, dibujamos geometría de a una hasta terminar.

Para cada vértice y pixel, calculamos luz con respecto a cada emisor de luz.

Es proporcional a la geometría por la cantidad de emisores.

Engañapichanga: culling, combinación de luces, light maps.


## Forward Rendering

- Pase de figuras opaca
- Pase de figuras transparente

Notas:
- Opaco de adelante para atrás para minimizar overdraw.
- Transparente de atrás para adelante para componer bien.


## Deferred Lighting

<img src='images/escenas-deferred.png' height='440' />

Notas:
No hacemos el cálculo de la luz, que es muy caro, hasta saber qué hay en cada pixel.

Es proporcional a la cantidad de pixels por la cantidad de emisores.

Rendering desde el punto de vista de cada luz sobre estos pixels.

Llamamos a la combinación de render targets un 'g-buffer' (por geometría).


## Deferred Lighting

<img src='images/escenas-deferred-buffers.png' height='440' />

Notas:
Las tres imágenes son color, profunidad y normales.

Necesita una placa con múltiples 'render targets'.

O se usan varios pases para por ejemplo cambiar resolución de gbuffers.

Dificultades que quedan: sombras; transparencias; antialias.


## Deferred Lighting

- Pase de geometría
- Pase de luz
- Pase de figuras transparente

Notas:
- El pase transparente es como en forward.


## Ubershader

- Otra dificultad de deferred: shaders fijos en los pases de luz
- Solución: todo en uno


## Forward Plus

<img src='images/escenas-forward-plus.jpg' height='440' />

Notas:
- Hacemos un render buscando qué luces pegan en dónde
- Permite hacer técnicas más coherentes de valores


## Forward Plus

- Pase de cálculo de luz
- Pase de figuras opacas
- Pase de figuras transparentes

Notas:
- Hacemos un render buscando qué luces pegan en qué pixels
- Después hacemos algo tipo forward, pero no consideramos todas las luces.
- Hace la diferencia con un número alto de luces dinámicas.


## Ejemplo

<img src='images/escenas-mgs.jpg' height='440' />

Notas:
- Metal Gear Solid (2015)
- Vamos a ver el ejemplo de cómo se hace.


### Ejemplo

- Depth pre-pass
- G-buffer
- Velocity map - caracteres (blur)
- Velocity map - meshes estáticos


### Ejemplo

- SSAO (screen-space ambien occlusion)
- Iluminación global (difusa)
- Luces sin sombra
- Generación de shadow maps
- Luces dinámicas


### Ejemplo

- Tone-mapping (?!?)
- Objetos con emisión y transparencias (y reflejos)
- Reflejos en pantalla (screen space)
- Partículas, carteles


### Ejemplo

- Bloom
- Profundidad de campo
- Suciedad en el lente
- Blur
- Ajustes de colores (LUT de 16x16)


### Ejemplo

- Antialias
- Retoques finales
- 2331 draw calls, 623 texturas, 73 render targets


### Depth pre-pass

<img src='images/escenas-heightmap.jpg' height='440' />

Notas:
- Heightmap con tiles, generan geometría
- Buenos si ocultaran mas cosas, pero no aqui.


### Depth pre-pass

<img src='images/escenas-piso.jpg' height='440' />


### G-buffer

<img src='images/escenas-mgs-gbuffer.png' height='440' />

Notas:
- Profundidad al reves (1 es camara)
- Albedo es el color antes de aplicar luz
- Roughness es para materiales
- SSS es sub-surface scaterring
- También escribe un depth buffer


### Velocity map - caracteres (blur)

<img src='images/escenas-mgs-vel.png' height='440' />


### Velocity map - meshes estáticos

<img src='images/escenas-mgs-vels.jpg' height='440' />

Notas:
- Es por movimiento de camara.


### SSAO (screen-space ambien occlusion)

<img src='images/escenas-mgs-ssao.jpg' height='440' />

Notas:
- En realidad combina dos tipos de SSAO.
- Consiste en ver pixels cercanos, comparando normales y profundidades.
- Después blur y combinación por compute.


### Iluminación global (difusa)

<img src='images/escenas-mgs-gi.jpg' height='440' />

Notas:
- Combina mapas precomputados de una esfera de iluminacion por area, normales,
  y profunidad.
- Corre en mitad de resolucion, hace upscale, pero saca los pesos del depth
  map que esta en resolucion completa.


### Luces sin sombra

<img src='images/escenas-mgs-luces-1.jpg' height='440' />

Notas:
- Point lights y spot lights.
- Muchas son luces 'ambientales', no reales.


### Generación de shadow maps

<img src='images/escenas-mgs-shadow-maps.jpg' height='440' />

Notas:
- Indica qué ven las luces.


### Luces dinámicas

<img src='images/escenas-mgs-luces-2.jpg' height='440' />

Notas:
- Buffer de luz difusa; hay otro de especular


### Combinación de luz

<img src='images/escenas-luz-combinacion.png'  height='440' />

Notas:
- Tonemap ajusta de HDR (alta gama) a LDR y aplica gamma.
- Hay bastante trabajo despues que ocurre en LDR.


### Objetos con emisión y transparencias (y reflejos)

<img src='images/escenas-mgs-trans.jpg' height='440' />

Notas:
- Por ejemplo, la luz sobre el personaje del fondo y su 'fuego'
- Para objetos como el vidrio que funcionan como espejos, hay una cubemap precalculado


### Reflejos en pantalla (screen space)

<img src='images/escenas-mgs-ssr.jpg' height='440' />

Notas:
- Una especie de ray casting trucho en baja resolución, a partir de pixels (dada su normal y profundidad).
- Si toca algo, ése pixel contribuye un poco.
- Mucho blur y retoque para engañar.
- Pero bueno para cosas que no reflejan bien, y es dinámico.


### Partículas, carteles

<img src='images/escenas-mgs-particulas.jpg' height='440' />

Notas:
- Distorción por calor haciendo 'stretch' de pixels.
- Carteles son partes rojas en el piso
- Humo y fuego por partículas


### Profundidad de campo

<img src='images/escenas-mgs-profundidad.jpg' height='440' />

Notas:
- Tomamos pixels cercanos, lejanos, y hacemos blur y combinamos.


### Suciedad en el lente

<img src='images/escenas-mgs-suciedad.jpg' height='440' />

Notas:
- Sprites!
- Mas que nada se ven las lineas verticales


### Ajustes de colores (LUT de 16x16)

- Bajo el control del artista
- En esta escena, des-satura un poco y tira a oscuro


### Antialias

- En forward render, se puede usar algo como modo MSAA para hacer.
- En deferred, cada pixel hace los suyo.
- Hay un pase de post-proceso para buscar aliasing y tratar quitar.


### Retoques finales

- Sprites o regiones extras que puede poner el artista.
- Probablemente parte del script de animacion.


## Video


## Preguntas

