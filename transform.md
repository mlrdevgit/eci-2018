-*- mode: markdown; coding: utf-8 -*-

## Transformaciones

<img src='images/transformers.jpg' height='440' />


## Introducción

- Movimiento de puntos y vectores.
- Rotación, traslación y cambio de escala

Notas:
- Necesario para que las cosas no sean puramente estáticas
- Necesario para poder hacer modelos no triviales
- Consiste en mover, cambiar el tamaño y rotarlo para que mira para el lado correcto.
- Rotación y escalar transformaciones lineales; en la práctica, la
  consecuencia es que no mueven el origen, y las líneas continúan siendo
  líneas.
- Para una matriz de misma dimensionalidad, la función f(v)->Mv es una
  transformación lineal, y la llamamos matriz de transformación.


## Puntos y vectores

- Vectores son $ [[x,y,z]]^T $
- Normalmente encapsulado en librería matemática.
- Convención de orientación de ejes (positivo y negativo), rotación.

Notas:
- La T es 'transpose' sobre la matriz.
- Bueno saber para tener una intuición de valores a la hora de encontar
  errores, o por si tienen que hacer algo para una plataforma nueva, o si
  necesitan hacer una librería propia.
- Presten atención a las dimensiones de matrices, orientación de valores,
  orientación de ejes (sentido antihorario o sentido horario).


## Traslación

- Operación más sencilla.
- Consiste en mover cada coordenada; se mueven de forma independiente.
- Independiente del origen.
- Las paralelas siguien siendo paralelas.
- Código! Por fin!

Notas:
- transformaciones.hlsl:traslaciones
- Operación más sencilla.
- Consiste en mover cada coordenada; se mueven de forma independiente.
- Es independiente del origen.
- Las líneas paralelas siguien siendo paralelas.


## Escala ("scale")

- También bastante sencilla.
- Multiplicamos cada componente por un valor.
- Uniforme o no uniforme.
- Las líneas paralelas siguien siendo paralelas.

Notas:
- transformaciones.hlsl:escala
- Si es el mismo valor, se mantienen las relaciones, si no, "estiran" la figure.
- Lo llamamos escala uniforme o escala no uniforme.


## Inclinación ("shearing")

- Le sumamos a cada componente un factor del otro.
- Cambian los ángulos entre los lados, pero se mantienen las paralelas.

Notas:
- transformaciones.hlsl:shearing
- Presten atención a estas cosas a la hora de hacer debugging - si no esperan
  una deformación particular, según el efecto pueden ver lo que están
  aplicando en la práctica.


## Rotación

- La rotación no es independiente por coordenada, es alrededor de un eje, con
  lo cual todas las otras coordenadas están involucradas.
- No es conmutativo con otras operaciones.

Notas:
- transformaciones.hlsl:rotacion


## Rotación 2D

$ [[cos, -sin], [sin, cos]] times [[x], [y]] $

resulta en:

$ [[x'], [y']] $

donde

$ x' = x * cos - y * sin $

$ y' = x * sin + y * cos $

Notas:
- Hagamos en 2d una rotación para buscar una intuición de cómo se
  comporta.
- Si `y` es 0, entonces girar convierte el vector al punto en la hipotenusa de
  un triangulo rectangulo!!


## Rotación 2D - valores

Suponemos (3,0) y 20 deg ("un poquito")

$ x' = 3 * 0.94 = 2.82 $
$ y' = 3 * 0.34 = 1.02 $

Notas:
- Un poco para el medio en x, un poco para arriba en y
- Noten que 0.94 + 0.34 es mas de uno, porque el arco pasa "por afuera" de una diagonal
- Hay partes del circulo donde 'x' se mueve poco x y se mueve mucho, y vice-versa
- Ahora, le damos 20 grados mas, estamos en (2.82,1.02)

formula es

x' = x * cos     - y * sin
   = 2.82 * 0.94 - 1.02 * 0.34
   = 2.6508      - 0.3468
   = 2.304

Otra intuicion: cuando el angulo es 0, x se proyecta completamente sobre x, e
y sobre y, y no hay cambio. Bueno para acordarse si sin o cos empieza en 1.

seno y coseno estan relacionados de forma tal que no pueden cambiar la
magnitud del vector. A medida que uno crece, el otro tiene que disminuir.

x^2+y^2 = x'^2+y'^2 (y la raiz de cada lado)


## Transformaciones singulares

- Transformaciones degeneradas, con determinante cero
- Colapsan vértices sobre una línea, con lo cual se pierde la posibilidad de
  invertir la transformación.

Notas:
- transformaciones.hlsl:degenerado


## Composición de funciones y matrices

- Cada una de estas transformaciones se puede expresar $ f(v)->Mv $
- Se pueden componer $ x->Tm(Tk(x)) $, y las matrices se convierten en $ MKx $.
- La aplicación semántica es de derecha a izquierda.

Notas:
- Tomamos el punto x, la aplicamos la operación K, luego la operación M.
- transformaciones.hlsl:composicion


## Matrices y funciones inversas

- Una matriz M es invertible si hay una matriz B tal que `BM = MB = I`, y la
  escribimos $ M^-1 $.
- Si $ S(x) = M^-1x $, S es la inversa de $ T_M $, es decir,
  $ S(T_M(x)) = x $, y $ T_M(S(x)) = x $.
- En general, para una matriz de 2x2, la inversa es

$ [[a, b], [c, d]]^1 = (1/(ad-bc)) [ [d, -b], [-c, a] ] $

Notas:
- I se refiere a una matriz identidad.
- Es decir, si aplicamos una matriz y su inversa, tenemos la matriz original.
- Encontrar matrices puede hacerse con un par de puntos, resolviendo como un
  sistema de ecuaciones.


## Matrices especiales

- Matrices identidad no producen cambios.
- Matrices diagonales, donde hay ceros excepto en la diagonal, escalan todos
  los ejes (o lo invierten si es negativo).


## Transformaciones inversas

- Dualidad entre transformaciones y mover el sistema de coordenadas.
- Puede convenir por precisión o para operaciones sobre centro como rotación.
- Uso intensivo integrando modelos, frameworks, herramientas, AR.

Notas:
- Hay una dualidad con las transformaciones que cambian puntos y mover el
  sistema de coordenadas.
- No hay diferencia algebraicamente, pero numéricamente puede ser más útil
  trabajar en espacios con mayor precisión.
- Se ve mucho cuando hay que trabajar con el origen en cero, como rotación con
  respecto a un punto.
- Se ve mucho en cosas tipo realidad aumentada, donde pueden tener varios
  sistemas de coordenadas, locales a distintos puntos; o cambiando según la
  calidad de ubicación (tipo ARCore?) o según el punto de vista para el
  programador (dispositivo o 'mundo'), tipo ARKit.


## Una dimensión extra

- Traslación no se puede representar directamente como una matriz.
- Intuición: no hay constantes "sueltas" en los factores.
- Agregamos una nueva dimensión, con valor 0 o 1 en un nuevo vector, para
  homogenerizar.
- Análogo en 2D, es "elevar" el plano en espacio x,y,w con w=1; si w sigue
  siendo 1, la transformación es homogénea, si no hay que proyectar contra
  este plano.

Notas:
- Fijamos su valor en uno en el nuevo elemento, y podemos agregar factores que
  actuán como constantes para traslado en la matriz.
- Cuando el vector resultado también es w=1, la transformación es afín.
- Haciendo distinciones entre puntos y vectores, en una dimensión
  adicional, w resulta 1 para puntos, y 0 para vectores.
- Importante para entender que punto más vector es punto, y que combinaciones
  como puntos centrales sólo tienen significado cuando la suma de coeficients
  es correcta (y w es 1 en el caso de representación como matriz).
- transformaciones.hlsl:traslacion con dimension extra


## Aplicación SceneKit

- SceneKit es un framework de Apple para aplicaciones en 3D
- Es un "retained mode", es decir, 'con memoria' en lugar de 'inmediate'
- Abstracción principal es un grafo de nodos: SCNScene (o árbol)
- Manejado a nivel de vista como SCNView en algun lugar de la pantalla
  (probablemente entongado con compositor).

Notas:
- https://developer.apple.com/documentation/scenekit/organizing_a_scene_with_nodes


## Aplicación SceneKit

<img src='images/scenekit.png' height='440' />

Notas:
De la documentacion:

A fog effect causes scene contents to become less visible the farther they are
from the pointOfView node currently used for rendering. At distances less than
the value of the fogStartDistance property, scene contents are fully
visible. At greater distances, SceneKit blends the rendered scene contents
with a constant color (specified by the fogColor property). At distances
greater than the fogEndDistance property, the scene contents fade away
completely and only the fog color is visible. Use fog to add atmospheric
effects to your app or game, or to improve rendering performance by hiding
parts of the scene that are far away from the current point of view.


## Aplicación SceneKit

- Cada nodo tiene las siguientes propiedades:
 - position, rotation, scale
 - transform (supercede las anteriores)
 - geometry (con material indicando su apariencia: )
 - light (para luces dinámicas, si no pueden hacer 'baked lighting' y un 'lightmap'): type, color, temperature, intensity 
 - camera: zNear, zFar, fieldOfView, focalLength, sensorHeight, projectionDirection


## Aplicación SceneKit

- Otros yuyos: animación, sombras, filtros, física, partículas

- Dibujar la escena consiste en caminar el árbol de transformaciones

- Hay varios espacios conocidos como object space, world space, image space y
  screen space.

- Se puede hacer prebaking, donde ponemos las coordenadas, o agregar efectos
  de post-proceso.


## SceneKit Bokeh

<img src='images/aperture-blades.png' height='440' />


## Retained Mode

```
draw(scene):
 s = empty stack
 s.push(identity matrix)
 explore(scene.root, s)

explore(node n, stack s):
 if n is transformation
  push n.tranformation_matrix * s.top onto s
 else if n is geometry
  drawPolygon(s.top * n.coordinate_array)

 for each child of n:
  explore(k, s)

 if n is transformation:
  pop top
```


## Transformaciones proyectivas

- Con matrices que no preservan w, en dos dimensiones, nos estamos saliendo del plano.
- Podemos reproyectar al plano dividiendo por w. [x y w] se proyecta a [x/w
  y/w w/w]. Se llama homogenización.
- La transformación de homogenización luego de una multplicación por M se
  llama 'transformación proyectiva'.
- Se usa para convertir proyecciones radiales en paralelas.

Notas:
- Con matrices que no preservan w, en dos dimensiones, nos estamos saliendo del plano.
- Podemos reproyectar al plano dividiendo por w. [x y w] se proyecta a [x/w
  y/w w/w]. Geometricamente, equivale a enviar a todos los puntos a w. Esta
  función se llama homogenización.
- La transformación de homogenización luego de una multplicación por M se
  llama 'transformación proyectiva'. Con transformaciones lineales o afines,
  no tiene efecto, pero se usa en transformaciones más generales.
- Se usa para convertir proyecciones radiales en paralelas, por ejemplo en
  modelos de cámara, lo cual permite comparar valores de profundiad para ver
  qué figuras están detrás de cuáles otras.
- Ojo que rompe interpolación, por el efecto de que los puntos se 'amuchan'
  hacia el centro a medida que se alejan.


## Transformaciones e interpolacion

- Las matrices de transformación no interpolan bien - importante para animación!
- La matriz es la relación entre un punto y otro, no 'el camino'; por ejemplo,
  una rotación por 180 es indistinta de escalar por -1
- No se puede interpolar la matriz final, es necesaria la descripción.


## Por ahora

- Tres tipos de transformaciones: lineales, afines (incluyen traslación en
  R^3) y proyectivas (normalizando w).


## Transformaciones en 3D

- Mayormente análogas en 3D y en 2D.

- Hay simetrías sobre puntos, líneas o planos en algunas operaciones (en lugar
  de sólo puntos y líneas).

- Mayor diferencia es en rotaciones.


## Ojo de buen cubero

- Si el bloque de 3x3 de arriba a la izquierda son valores entre -1 y 1, y la
  suma de los cuadrados en una columna es más o menos uno, es probablemente una
  rotación.

- Si la fila de abajo no es 0 0 0 1, la transformación es proyectiva en vez de
  afín.

Notas:
- Reglas útiles a la hora de hacer debugging.
- Ojo con la orientación de matriz al ver datos en memoria, si es row major o
  no.


## Rotaciones en 3D

- La primer representación de rotaciones es como en 2d, pero en cada plano (la
  dimensión que no cambia es el "eje").

$ R_(xy)(theta) = [[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]] $

Notas:
- Noten por las matrices que rotar en xy no tiene efecto sobre z, etc.


## Rotaciones en 3D

$ R_(yz)(theta) = [[1, 0, 0], [0, cos(theta), -sin(theta)], [0, sin(theta), cos(theta)]] $


## Rotaciones en 3D

$ R_(zx)(theta) = [[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]] $


## Ángulos de Euler

<img src='images/plane-axis.png' height='440' style='background-color: gainsboro' />

Notas:
- Los ángulos de Euler hacen la rotación en un orden predeterminado (ojo que
  distintas disciplinas cambias el orden según convenciones propias). Una
  común es pitch/yaw/roll.


## Ángulos de Euler

Combinamos las rotaciones en una única matriz.

$ bbM = R_(yz)(alpha) R_(zx)(theta) R_(xy)(gamma) $

- alpha es roll, theta es yaw y gamma es pitch

Notas:
- Un problema es gimbal lock, cuando uno de los ejes se alinea con el otro. Un
  ejemplo en dos dimensiones de mecánica es utilizar un telescopio para seguir
  un avión que pasa por arriba; una vez que pasa, el telescopio tiene que
  girar 180 rápido (y en cualquier sentido) para 'bajar' por el otro lado,
  compensando por un grado de libertad perdido.
- Cuando dos ejes de orientación están alineados, perdemos un grado de
  flexibilidad, y no puede utilizarse la representación para moverse en
  determinado eje de coordenadas.


## Gimbal Lock

<img src='images/gimbal-lock.png' height='440' />

Notas:
- El ejemplo clásico es un avión, pero el gimbal es mejor, porque el avión se
  mueve físicamente como se le da la gana.


## Eje y ángulo

<img src='images/eje-angulo.png' height='440' />

Notas:
- Otra representación es de eje y ángulo; tomamos un vector como eje y un
  ángulo con respecto a él. Más flexible (pero más complicado) que fijar el
  eje de rotación a un eje del sistemad e coordenads.
- No vamos a cubrir mucho, traducible por fórmula de Rodrigues, donde podemos
  rotar sobre cualquier eje y ángulo, y podemos recuperar el eje y ángulo a
  partir de la matriz.


## Eje y ángulo

$ omega=[[omega_x],[omega_y],[omega_z]] $
$ bb J_omega = [[0, -w_z, w_y],[w_z, 0, -w_z],[-w_y, w_x, 0]] $

$ bb M = bb I + sin(theta)bb J_w + (1-cos(theta)bb J_w^2) $

donde:
- omega es vector de eje, y theta ángulo de rotación
- $ J_omega $ ayuda a simplificar expansión

Notas:
- Se pueden determinar los valores a partir de una matriz de rotación también.
- Esto se puede expandir un par de veces, pero el punto es mostrar que es
  equivalente en cuanto a información y operación.


## Cuaternones (quaternions)

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <use xlink:href='images/cuaternones-2d.svg#svg3931'></use>
</svg>

Notas:

El espacio de matrices de 3x3 que usamos para rotaciones es un punto en R^9,
lo cual es una representación más complicada para muchas operaciones.

Una de las herramientas para simplificar SO(3) y mejorar la calidad de cálculo
es trabajar en S^3, la esfera en tres dimensiones en [w x y z]^T con
distancia 1 al origen.

Vamos a trabajar mucho por analogía porque son cálculos en cuatro dimensiones.

Se puede envolver un círculo con una línea, o una esfera con un disco, donde
todos los puntos del borde terminan en el polo norte.

- ejemplo de hilo con tubo
- ejemplo de panuelo con manzana


## Cuaternones (quaternions)

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <use xlink:href='images/cuaternones-sincos.svg#svg3931'></use>
</svg>

Notas:

Con dos vectores perpendiculares w y v, podemos construir todos los puntos cos
alpah(w) y sin alpha(v), y formar un círculo, que es la intersección de un
plano con el centro de una esfera. Mismo con la esfera-3. Y el arco en esta
superficie es la distancia más corta, igual que con menos dimensiones.


## Cuaternones (quaternions)

$ K:bb "S"^3 ->bb "SO"(3): $

$ [[a],[b],[c],[d]]->[[a^2+b^2-c^2-d^2, 2(bc-ad), 2(ac+bd)],[2(ad+bc), a^2-b^2+c^2-d^2, 2(cd-ab)], [2(bd-ac),2(ab+cd), a^2-b^2-c^2+d^2]] $

Notas:

K es un mapa de S^3 (la esfera de cuatro dimensiones) a SO(3) (el espacio de
matrices de 3x3).

K tiene tres propiedadas interesantes:
- es dos a uno, por cada q en S^3, K(q)=K(-q), es decir, se come el signo
- los grandes círculos en s^3 van a geodesics en SO(3) - caminos más cortos
- K([[1, 0, 0, 0 ]]^T) = I

Esta función es parecida a una multiplicación en R^4, análoga a considerar
puntos en R^2 como números complejos y multiplicarlos. Siempre se pueden
agregar dimensiones, pero si no importan, no hacen diferencia. La
multiplicación en R^4 no es conmutativa, pero es aproximadamente
análoga. Llamamos cuaternones al conjunto R^4 junto con esta multiplicación.


## Cuaternones (usos)

- Para interpolar entre rotaciones en SO(3) (matrices), interpolamos en cambio
  entre puntos de $ S^3 $ (cuaternones).


## Interpolación esférica

$ bbv=(bbq_2-(bbq_2 cdot bbq_1)bbq_1)/norm(bbq_2-(bbq_2 cdot bbq_1)bbq_1) $

$ gamma(t)=cos(t)bbq+sin(t)bbv $

Notas:

Supongamos que tenemos dos puntos en la esfera unidad, que no son antípodas
(entonces hay un único camino más corto - de lo contrario, hay infinitos
caminos más cortos). Vamos a construir el camino que va a velocidad
constante por el gran arco más corto; llamamos a esto interpolación esférica
lineal, ocurre entre dos cuaternones.

1. Encontramos el vector v en S^3 que está en el plano de q1-q2 y es
   perpendicular a q1. Para eso proyectamos q2 sobre q1 y restamos q2 sobre
   este punto, y normalizamos. (primera ecuacion arriba)

2. Buscamos el camino en el circulo de q1 a través de v (sin/cos en segunda)

3. Ajustamos para que llegue en 1 en vez de gamma multiplicando t por gamma.

Esta función varía de q1 a q2 a medida que el argumento va de 0 al ángulo.

Visualmente, tenemos dos puntos sobre una esfera, y la cortamos con un plano
que pasa por los puntos (de ahí la normal), con lo cual nos queda un
círculo. Vamos a ir moviéndonos sobre ese círculo interpolando el ángulo.

Con estos elementos, podemos interpolar rotaciones convirtiéndolas en
cuaternones, haciendo una interpolación esférica, y proyectando a matrices con
K.

En la práctica, es mucho menos trabajo ir representando como cuaterniones para
ir haciendo integraciones de Euler (donde empezamos de cero y calculamos
progresivamente 'de a cachitos', como pequeñas adiciones) que con matrices,
que hay que ajustar para que los ejes sean perpendiculares entre sí
(normalizar el primero, perpendicular el segundo al primero, perpendicular el
tercero a los primeros dos). Los cuaterniones sólo necesitan ser normalizados
para corregirse.

