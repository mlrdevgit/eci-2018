-*- mode: markdown; coding: utf-8 -*-

# Cámaras

Notas:

The Direct3D Transformation Pipeline
https://msdn.microsoft.com/en-us/library/windows/desktop/ee418867(v=vs.85).aspx

Transforms (Direct3D 9)
https://docs.microsoft.com/en-us/windows/desktop/direct3d9/transforms

Learn OpenGL - Getting Started - Camera
https://learnopengl.com/Getting-started/Camera


## Introducción

- ¿De dónde miramos?
- Posicion, dirección, 'arriba', plano cercano, plano lejano, campo de visión
  (FOV)

Notas:

Para dibujar necesitamos tener un modelo de la cámara que está observando una
escena.

La cámara tiene una posición, una dirección en la que mira, una dirección que
orienta dónde es "arriba", un plano cercano y lejano, y un campo de visión
(field of view o FOV).


## Perspectiva

- Ángulo de visión
- Sin visión periférica, mucho más acotada
- Distorción (cosas más cerca parecen más grandes)

Notas:

En la práctica, hay visión periférica, pero podemos ver bien unos 120
grados. Pero aparece muy distorcionado, en parte porque lo que vemos en una
pantalla ocupa sólo un poco de nuestra visión, con lo cual usamos un ángulo
bastante modesto, como una fotografía.


## Cámara pinhole

- Posición es punto, apertura es instantánea
- No hay distancia focal ni profunidad de campo

Notas:

En el modelo de cámara de pinhole, la cámara es un único punto - su posición,
y la apertura es instantánea. Con lo cual todo está en perfecto foco; en una
cámara real, la distancia focal (la distancia  de los puntos que están más en
foco) o profundidad de campo (cuánto delante y detrás de la distancia focal
van a haber cosas en foco) permite ajustar estos parámetros.


## Ventanas

- Pixels en coordenadas normalizadas
- Mapa de coordenadas normalizadas de `(-1;-1):(1;1)` a `(0;0):(r;k)`

$ bbM_"ventana" = 1/2 [[r, 0, r], [0, -k, k]] $

Notas:

A veces en vez de construir la transformación 'a mano', podemos tener algunos
valores que sabemos de dónde a dónde tienen que ir, con lo cual podemos
resolver el sistema de ecuaciones o usar alguna función de una librería de
geometría para conseguir la transformación.

En el caso de transformaciones a ventanas, por ejemplo, sabemos que tenemos
puntos de 'arriba-izquierda' y 'abajo-derecha' sobre el área a dibujar, y si
tenemos las correspondencias en el mundo podmemos conseguir su ecuación.

Para ventanas, por ejemplo, la generalización es una transformación de ventana
para 'r' filas y 'k' columnas, de (-1;-1) abajo-izquierda a (1;1)
arriba-derecha.


## Ventanas

Aspect ratio: proporción horizontal vs. vertical

Notas:

Para definir proyecciones, el 'aspect ratio' suele calcularse a partir de las
dimensiones de la ventana (en vez de utilizar una cámara cuadrada).


## Ventanas

- Ojo con signo vertical
- Ojo con eje (z es profunidad o altura?)

Notas:

La definición de arriba suele ser (0,1,0), es decir, un vector que mira en la
direccón y. Ojo que algunos programas de CAD consideran que el plano
horizontal es xy, y 'z' es la altura en vez de la profundidad, con lo cual
¿´como es el vector de arriba? (el vector de arriba es 0;0;1). Imaginen casos
donde tienen planos de pisos, por ejemplo.


## Geometría de cámara

<img src='images/camaras-frustum.jpg' height='440' />

Notas:

- El punto de visión, más la orientación, más los ángulos, más los planos de
cerca y lejos, entre todos definen un frustrum.
- Los objetos pueden ser descartado si están completamente afuera, renderados
si están adentro, o 'clippeados' si están parcialmente adentro.


## Geometría de cámara

- Clip lejano? Niebla (atmosférica o real). O level design.
- Videos: Silent Hill

Notas:
Lo que solía utilizarse antes era asumir niebla para objetos lejanos; un caso
particular fue Silent Hill que terminó incorporando el efecto como parte
esencial de diseño.

clip: silent hill - con niebla
clip: silent hill - sin niebla

Hay otros juegos que hacían algo similar con una niebla más sutil para cosas
que se acercaban desde el horizonte. O, como el caso de muchos juegos de
aventura, con oscuridad. O, como en el caso de juegos dentro de lugares
cerrados, con decisiones de diseño.

Hoy en día, se utiliza mucho una técnica de level of detail donde hay modelos
"de lejos" que reemplazan a los "normales" y que se utilizan para renderar con
menos costo de performance.


## Transformaciones

- Convertimos al mundo en una pirámide que empieza en cero y va hasta uno.
- "Standard perspective view volume"

Notas:
- z=1 es el plano lejano.
- Después podemos proyectar linealmente al plano diviendo por z por ejemplo, x/z,y/z,1.


## Transformaciones

- Convertimos la pirámide en un paralelepípedo que 'abre' el origen.
- "Standard parallel view volume"

Notas:
- Los puntos más cerca se 'abren'.
- Más útil para ver, desde un punto de vista con perspectiva, qué está detrás
  de qué (único valor comparado).
- La transformación es proyectiva y rompe las paralelas (creando puntos de fuga).
- Las líneas no se curvan, pero se juntan.


## Ejemplo

- perspectiva.hlsl

Notas:

Coordenadas raras porque empecé con un triángulo armado ya con perspectiva.

Probar cambiar field-of-view, mostrar matrices con transformaciones, empujar 'z' en punto.

Ojo con signo de 'z' en OpenGL y DirectX.

Hay transformaciones que pueden hacerse para que la distancia quede entre 0 y
1 en vez de -1 a 1, lo cual ayuda dando más precisión a las cosas que están
"cerca" (hay más valores cerca del 0 que del 1).


## Transformaciones y rasterización

- Clipping ocurre antes de las transformaciones finales.
- Primero volument estándar, después clipping, después homogeneizamos
  (dividimos por w).
- Después proyectamos contra el plano de la cámara
- Transformamos para el dispositivo 2d

Notas:

Clipping ocurre antes de las transformaciones finales. Ponemos todos los
puntos en un volumen estándar, hacemos clipping ahí (donde termina siendo
AABB), luego homogeneziamos (dividimos por w, y después podemos descartarlo),
luego proyectamos contra el plano de la cámara y transformamos las coordenadas
para el dispositivo 2d.


## Transformaciones

<img src='images/camara-transformaciones.png' height='440' />


## World Transform

<img src='images/world-transform.png' height='440' />

Notas:
La transformación de mundo puede obtenerse caminando el 'stack' de objetos.


## View Transform

<img src='images/view-transform.png' height='440' />

Notas:
La transformación de view puede obtenerse combinando matrices de rotación y
traslación (con la inversa, porque queremos que el mundo se ajuste para que la
cámara quede en el centro).

V = T Rz Ry Rx


## Projection Transform

<img src='images/projection-transform.png' height='440' />

Notas:
Matrices en: https://msdn.microsoft.com/en-us/library/windows/desktop/bb147302(v=vs.85).aspx
https://msdn.microsoft.com/dynimg/IC511469.png


## Cámaras Ortográficas

- Podemos hacer render sin perspectiva - proyección ortográfica o paralela
- Útil para entender mejor

Notas:

ejemplo: blender '5'

Quad mode en blender, Ctrl Alt Q

Hay algunas variantes para dibujos de diseño tipo arquitectura o modelos particulares.

Es como si el ojo retrocediera al infinito, donde todas las líneas tienden a hacerse paralelas.

Es una proyección directa contra el plano del film.

Lo vemos mucho para examinar planos, edificios, o estructuras más bien rectangulares. Muy útil en combinación.


## Field of View

- En cámara de 35mm (36mm x 24mm):
- 18mm son 67 grados - super-wide
- 28mm son 46 grados - wide
- 50mm son 27 grados - normal
- 100mm son 14 grados - narrow ("telephoto")

Notas:

Es el ángulo entre los rayos de los bordes opuestos de la imagen en perspectiva.

En cámaras, determinado por focal length (la distancia de foco).


## Distorciones

- Líneas que deberían estar derechas pero se curvan
- Hacia afuera: barrel
- Hacia adentro: pincushion


## Distorciones

<img src='images/fisheye.png' height='440' />

Notas:
Curvas en líneas rectas.

Hay distorciones que encontramos que líneas que debieran estar derechas están curvas, normalmente hacia los bordes.


## Distorciones

<img src='images/pincushion.jpg' height='440' />

Notas:
Cuando se curvan hacia adentro, las llamamos de pincushion, imaginando un pincushion o almohada vista de arriba.


## Distorciones

<img src='images/barrel.jpg' height='440' />

Notas:

Cuando se curvan hacia afuera, las llamamos de barrel por su forma.

La mayoría de los zooms en fotografía tienen problema con esto; pueden buscar
una línea recta en la distancia como el horizonte en el mar, y cambiar el
grado de zoom. Normalmente van a ver un poco de distorción de barril en un
extremo y de pincushion en el otro.

Hay otro tipo de distorciones, llamadas aberraciones cromáticas, casuadas porque distintas ondas de luz caen en distintos puntos de foco.

Recuerden que en la realidad, la refracción no es uniforme con respecto a la frecuencia de ondas.

Otro tipo de distorciones mecánicas incluyen flares (cuando una luz fuerte como el sol se dispersa sobre el lente y deja parte en blanco) y ghosting (cuando la luz se refleja dentro del las lentes y aparece repetida).

http://av.jpn.support.panasonic.com/support/global/cs/dsc/knowhow/knowhow15.html

En cámaras, se aplican capas sobre el lente (una o varias, o ninguna en cámaras deshechables).

http://av.jpn.support.panasonic.com/support/global/cs/dsc/knowhow/knowhow17.html

Coatings:
https://www.kenrockwell.com/tech/lenstech.htm


## Foco y apertura

https://photographylife.com/what-is-aperture-in-photography


## Preguntas
