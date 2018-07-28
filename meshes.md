-*- mode: markdown; coding: utf-8 -*-

# Meshes (mallas)


## Introducción

<img src='images/meshes-chichen-itza.jpg' height='440' />

Notas:

Las mallas son la unidad de representación dominante hoy en día.

Son estructuras donde representamos muchos triángulos unidos por sus aristas
(edges) para representar una figura. Hay otras opciones, como uso de quads,
pero tienen algunas desventajas.


## Render vs. model

<img src='images/meshes-dolphin.png' height='440' />

Notas:

Las mallas de triángulos se utilizan en la gran mayoría de los casos, porque
son automáticamente, convexos y planares y tienen una única forma de
interpolación.

A la hora de modelar es conveniente usar mallas de polígonos, donde cada cara
puede tener un número arbitrario de vértices, para evitar tener que trabajar
con múltiple triángulos que no tienen significado. Son más difíciles de
trabajar, con todas las complicaciones de quads, pero ayuda cuando es
importante trabajar con intención artísitca o cuando la estructura tiene
semántica.


## Generación

- Directa
- Aproximación
- Subdivisión

Notas:

Para generar meshes, podemos usar información de la figura, como por ejemplo
un cuadrado, o podemos generar aproximaciones para figuras más complejas.

Una de las operaciones más sencillas es la subdivisión, donde generamos varios
triángulos a partir de uno, por ejemplo para aproximar el límite de una
superficie y evitar 'bordes'.


# Bordes

<img src='images/meshes-ff7.jpg' height='440' />


# Bordes

<img src='images/meshes-ff7-real.jpg' height='440' />


# Decimation

- Reemplazo con similaridad geométrica (o topológica)
- aka reduction
- Por ejemplo para cosas lejanas

Notas:
Otra es la simplificación donde reemplazamos una malla por otra,
topológicamente o geométricamente similar. También conocido como 'decimation'
o 'reduction'. A medida que se repite, se pueden formar mallas que son útiles
para objetos lejanos donde no es necesario tener tanto detalle.


# Cosas Raras

- Ej: pelo

Notas:

Hay algunas figuras que no se representan bien pero son importantes, y en esos
casos tenemos alguna representación especializada. Un ejemplo clásico es el
pelo, que es una estructura tubular deformada, y que es muy cara de
representar bien con un malla de triángulos.


## Polilíneas

- Por analogía en 2d con 3d
- Vértices y aristas (edges)
- Queda tabla de geometría y aristas

Notas:

Una buena forma de introducir meshes es trabajar con una dimensión menos, en
2D, usando el plano en lugar del espacio y segmentos de líneas en lugar de
triángulos.

Una de las representaciones clásicas es la de vértices y edges o aristas; las
aristas son segmentos de línea que unen vértices. Tenemos entonces dos tablas:
una de vértices, donde está la posición de cada punto, y una de lados, donde
tenemos dos valores, uno por cada segmento.

Una consecuencia interesante de este formato es que la topología está en la
tabla de lados y la geometría está en la tabla de vértices.


## Topología

- Boundary (¿es forma cerrada?)
- Otras propiedades (manifold, smooth, auto-intersección)

Notas:

Definimos el 'boundary' como la suma formal de vértices en la malla, donde el
coeficiente de cada vértice se incrementa por uno cuando el vértice 'recibe'
un lado, y se decrementa cuando está del lado del origen (i->j).

Cuando el boundary es cero, la forma es cerrada, y es fácil definir 'dentro' y
'afuera'.

Cuando el grado de cada vértice es dos (cada uno tiene un lado que llega y
otro que sale), es un 'manifold mesh'. No lo vamos a definir, pero
informalmente, hay un 'neighborhood' donde cada punto corresponde a un punto
dentro de una unidad esfera en R^n de forma continua.

Una figura como un cubo, donde las aristas pueden ser manifolds pero no
'smooth', que es lo que muchas veces queremos decir informalmente - un mapa
continuo que toma una región cerca de un punto.

Las figuras que se auto-intersectan, como un ocho, no tienen esta propiedad -
donde se cruzan no hay un mapeo bicontinuo sobre la esfera. Pero es raro de
ver en nuestro campo.

También hay meshes donde los edges no son orientados ("unoriented meshes"),
donde 'boundary' no está definido, pero no lo utilizamos mucho - es importante
saber qué lado está dentro y cuál fuera.


## Vecinos (neighbors)

- Tabla de lista de vecinos (ordenados antihorarios)
- Sólo calienta para regiones
- Estructura de datos! (array o lista, orden, cálculo parcial)

Notas:

Además de las tablas de vértices y edges, podemos formar una tabla de
neighor-lists, donde tenemos para cada vértice una lista de arista, típicamente
ordenados en sentido antihorario.

Acá es donde terminan aplicando todo lo que aprendieron en estructuras de
datos. Tienen varias representaciones posibles para toda esta información,
normalmente van a terminar haciendo arrays con algunas variantes según qué
tipo de preguntas necesiten hacer de sus datos. Por ejemplo, si no van a
trabajar con regiones a las que pertenece un punto, pueden no necesitar tener
la lista de vecinos, o pueden relajar el requerimientos de que los vecinos
estén en sentido antihorario.


## 3D

- Más o menos lo mismo
- Triángulos en vez de edges
- O ambas (estructura de datos)
- Jueguen con DirectXMesh y modelos .obj

Notas:

En 3D, las cuestiones básicas de puntos y aristas se mantienen, pero es común no
tener una tabla de aristas explícita, sino tener también una tabla de triángulos
(o caras) con tres vértices, e inferimos las aristas a partir de ahí. Las
opiniones varían, ojo - hay cosas que se pueden hacer más rápidas con aristas,
pero cuesta más memoria.

Con estas estructuras en mano, podemos hacer bastante trabajo, el resto de las
técnicas es para cuando empiezan a tener problemas.

Si quieren jugar con esto, sugiero agregar
https://github.com/Microsoft/DirectXMesh/wiki/DirectXMesh a alguna aplicación
para importar vértices. Pueden bajarse modelos .obj de montones de edges (y
hay incluso una especie de mercado negro), o armar cosas en Blender.


## Formatos de meshes

- RAW - medio porquería
- OBJ - simple
- STL - impresoras 3D
- collada - modelos con esqueltos
- fbx - binario, animaciones
- gltf - Khronos https://www.khronos.org/gltf/

Notas:
- RAW - medio porquería, ASCII de tres floats por línea, no hay atributos ni normales
- OBJ - wavefront, vértices, normales de vértice, coordenadas texture de vértice, caras de 3 o 4
- STL - binario, utilizado para impresoras 3D
- collada - modelos con esqueletos
- fbx - binario
- gltf - Khronos https://www.khronos.org/gltf/


## DirectXMesh (o algo así)

- Cálculo de normales, parametrizados
- Cálculo de tangente y bitangente
- Cálculo de adyacencia
- Simplificaciones (decimación)
- Optimizaciones (orden)
- Uso, no edición (falta primitivas, intersecciones, manipulación, generación)

Notas:

Facilidades de la librería:
- cálculo de normales (que normalmente pasamos con vértices), parameterizados
  por cuánto importan los triángulos (igualmente o proporcional al área), y
  el orden de vértices (el default es antihorario)
- cálculo de tangente y bi-tangente (que con normal definen un sistema de
  coordenadas sobre la cara)
- cálculo de adyacencia
- simplifcaciones (obvias, pero puede haber más interesantes)
- optimizaciones - reordenando por algún atributo, o para intentar mejorar el
  uso de caché de vértices


## Manifold Meshes

- Propiedad es que puede ser mappeado localmente a un espacio Euclideano.
- Texturas!
- Cada arista de triángulos es contenida por dos caras, se puede enumerar en
  orden cíclico sin repetir.

Notas:

Un mesh es un manifold mesh si los edges y triángulos que incluyen un vértice
v pueden arreglarse en un orden cíclico t1, e1, t2... sin repeticiones tal que
el borde e_i es un borde de triángulos t_i y t_(i+1) (con los índices haciendo
'wraparound'). Es decir que en cada arista, hay dos caras que lo continene.


## Uso de Topología

- Cosas varias en depth-first o breadth-first
- Grupo de vértices (por índice), grupo de aristas que los conectan, grupo de
  caras (tríos de índices). 0-simple, 1-simplex, 2-simplex.
- Grado vert: cantidad de aristas que lo contienen (a veces 'valencia')
- Grado arista: cantidad de ¿adivinen?

Notas:

La topología de meshes (qué está conectado con qué otra cosa) se usa en varios
algoritmos, que están definidos haciendo cosas como depth-first o
breadth-first.

Para especificar la topolgía de un mesh, normalmente elegimos un grupo de
vértices, usualmente nominados por su índice, un grupo de aristas que conectan
esos índices, y grupo de caras, donde cada cara es un trío de índices de
vértice.

Ahora, como un vértice es un índice, una arista dos, y un triángulo tres, a veces
generalizamos y decimos que un vértices es un 0-simple, arist 1-simplex, cara
2-simplex.

El grado de un vértice es la cantidad de edgess que lo contienen (a veces
'valencia' por analogía con átomos en moléculas). Los vértices son adyacentes
a los edges que los contienen y vice-versa (y los edges son adyacentes con
caras y vice-versa). El grado de un edge es un ¿qué? la cantidad de caras que
lo contienen. Vamos a restringirnos a casos comunes donde el edge tiene un
grado uno, en cuyo caso es un 'boundary edge', o dos, en cuyo caso es un
'interior edge'.


## Uso de Topología

- Usualmente grado es uno (boundary) o dos (interior)
- Casos degenerados: dangling (arista sin caras)
- Winged edges: cada edge tiene vértices, caras, y cuatro edges, primero y
  último de cada vértice

Notas:
Un edge sin caras es un 'dangling edge' y no lo consideramos.
Cada cara aparece a lo sumo una vez (es decir, dos caras pueden compartir a lo sumo dos vértices).
El grado de cada vértice es al menos tres.

Se puede mantener una estructura de winged edges, donde caja edge guarda sus
vértices, caras, y también cuatro edges, el primero y el última conectado a
cada vértice; los otros se pueden encontrar 'caminando' esta estructura de
butterfly.


## Winged Edges

<img src='images/meshes-winged.jpg' height='440' style='background-color: gainsboro' />


## Uso de Topología

- Encontrar bordes: hash tables y recorrer vértices ordenados
- Cuentitas (y algunas otras variantes): tablita de (wikipedia)[https://en.wikipedia.org/wiki/Polygon_mesh#Summary_of_mesh_representation]

Notas:

Varias operaciones que requieren presencia o recorrer todos los edges pueden
hacer lo siguiente - ir ordenando edges por ejemplo generándolos como pares de
vértices ordenados por índice, y usar ese par como entrada de hash
table. Ejemplo, para encontrar bordes, recorremos todas las caras, y evaluamos
cada edge, agregándolo o quitándolo; al terminar, los edges que quedan son los
bordes de la malla.


## Más

<img src='images/meshes-konigsberg.png' height='440' />

Notas:

Puentes de Konigsberg.

El estudio de todas las cosas interesantes que se pueden hacer con estas
estructuras, incluyendo trabajo con más dimensiones, lo pueden encontrar como
operaciones de topología. Hay un mundo del estudio de topología que va más
allá de lo geométrico, donde hablamos más abstractamente de grafos, nodos y
aristas.

A la hora de usar strips o fans, no hace mucho diferencia en lo abstracto,
aunque sí puede importar si el tamaño de datos afecta la transmición.


## Duplicación

- Misma posición, distintos atributos (color, normal)
- Topológicamente distinto
- Puede ser geométricamente 'watertight' pero no topológicamente
- Ojo con sombras o animaciones

Notas:

Para hacer una pirámide o cubo, donde cada lado del cubo tiene un color
distinto, tenemos problemas de expresión cuando asignamos un único color a
cada vértice. Si el vértice tiene un único color, vamos a hacer rendering
incorrecto.

Lo que hacemos en esos casos es duplicar los vértices, de forma tal que aunque
tengan la misma posición, sean topológicamente distintos y tengan atributos
como normales y color distinto (qué desastre tratar de hacer que las normales
funcionen!)

Ahora, el problema va a ser que la malla ya no es 'watertight' en el sentido
topológico. Pueden haber problemas de precisión en lo geométrico, pero en
general no. Lo que sí se dificulta son cosas como animaciones o cálculo de
sombras.


## Nivel de detalle

- Ahorro de memoria, ancho de banda, proceso, etc.
- Representación interna, por ej. por objetos
- ¿Cuál es representación a esta distancia de cámara?
- ¿Cuál es mejor pero menos de 5000 triángulos?
- ¿Cuál es con este bounding box?
- ¿Qué es lo que hay?

Notas:

El trabajo con mallas es una de las áreas donde tenemos que considerar la idea
de nivel de detalle o level of detail. Tener una malla detallada para una
persona que está a lo lejos no tienen sentido, vamos a procesar cientos o
miles de triángulos para pintar ocho pixels; podemos decimar la malla, de
forma automatizada, a mano o con una combinación.

En la arquitectura de un programa, el uso de nivel de detalle implica un
cambio que puede ser sustancial, porque la pregunta ya no es '¿cuál es el
modelo de este objeto?', sino '¿cuál es el modelo de este objeto a esta
distancia de la cámara?' o '¿cuál es el modelo de este objeto de mayor
resolución pero menor a 10.000 triángulos?'. Otra estrategia es determinar
cuál es el 'bounding box' del objeto proyectado en la cámara, y utilizar esta
información para elegir el modelo.

Para mayor complicación, consideren los casos donde los modelos de mayor
detalle no están siempre disponibles sino que tiene que leerse de disco. 


## Nivel de detalle - Ejemplo

<img src='images/meshes-unreal-level.png' height='440' />

Notas:

Vamos a hablar de levels en un minuto. Ojo que 'level' en Unreal es otra cosa, pero relacionado.


## Nivel de detalle - Ejemplo

Simplygon Reduction / Remeshing (video)


## Nivel de detalle - Ejemplo

- Ejemplo de Unreal
- Dos mecanismos - level streaming volumes (cámara está dentro) y scripted
  streaming (por API)
- Persistent Level (base), y otros que entran on-demand
- Parte de esta definición es el LOD
- También afecta texturas y materiales

Notas:

Consideren también el manejo de texturas en streaming (por ejemplo, dejar
espacio en VM map para hacer stream in and out de la mayor resolución de
texturas). O considerar la geometría de disco o DVD, por ejemplo en casos de
muy baja latencia.

Además de eficiencia, el nivel de detalle es importante para ser correctos. Si
vamos a dibujar una puerta con tres pixels, tener cosas de poca precisión como
la manija de la puerta o detalles de madera no ayudan y sólo terminan
generando problemas de aliasing. Mismo con valores de normales o BRDF.


## Representación vs. proceso

- Dos representaciones de hoja de papel metalizado
- Muchos triángulos con reflejos simples
- Quad simple con mapa de normales y tal vez bump map

Notas:

A veces podemos hacer tradeoffs. Un pedazo de papel metalizado pueden ser
muchos triángulos con reflexión simple, o a lo lejos puede ser un quad simple
con un mapa de normales y tal vez un bump map.

Dos notas más para considerar cuando simplificamos. No hay que confundir
simplificar el mundo que representamos con simplificar nuestra
representación. Las dos cosas son válidas, pero para aplicar la opción
correcta tenemos que entender qué hacemos y para qué. Una esfera puede
representarse de varias formas con más o menos polígonos; un polígono puede
simplificarse reduciendo su malla; los resultados pueden diferir.

La segunda nota es que para entender cómo preservar detalle, cuando hay
representaciones en valores reales definidas sobre un intervalo o un
rectángulo, podemos siempre hace un análisis de Fourier, con lo cual tenemos
la opción de filtrar.


# Simplifación de mallas

- Técnica clásica es tomar dos vértices de una arista, colapsarlos, minimizar
  función de energía.

Notas:

Para simplificar mallas de forma progresiva, la técnica clásica consiste en
tomar dos vértices de un edge, que comparten triángulos a ambos lados de ese
edge, y colapsarlos eliminando esos triángulos, ya sea sobre un vértice, sobre
el otro, o sobre un punto entre ellos, normalmente minimizando una función de
energía que mide qué tan bien la nueva representación se aproxima a la
anterior.


# Otras cosas divertidas

- Tesselation
- Marching cubes
- Mesh repair
- Mesh improvement
- Triangle order optimizacion
- Deformation transfer

Notas:

También hay otras aplicaciones, como usar tesselation con distintos factores.

Aplicaciones: marching cubes, mesh repair, mesh improvements, triangle order
optimization, deformation transfer

