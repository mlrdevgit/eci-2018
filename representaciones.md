-*- mode: markdown; coding: utf-8 -*-

# Representaciones

Notas:
Game Engine Black Book: Wolfenstein 3D
https://www.amazon.com/Game-Engine-Black-Book-Wolfenstein/dp/1539692876/ref=pd_sim_14_3/144-7675622-9017513?_encoding=UTF8&pd_rd_i=1539692876&pd_rd_r=ZE9DAPWJSAB6PFHCFH07&pd_rd_w=Tkjt7&pd_rd_wg=IYZK2&psc=1&refRID=ZE9DAPWJSAB6PFHCFH07

Tricks of the Game Programming Gurus
https://www.amazon.com/Tricks-Game-Programming-Gurus-Andre-Lamothe/dp/0672305070/ref=pd_sim_14_5/144-7675622-9017513?_encoding=UTF8&pd_rd_i=0672305070&pd_rd_r=ZE9DAPWJSAB6PFHCFH07&pd_rd_w=Tkjt7&pd_rd_wg=IYZK2&psc=1&refRID=ZE9DAPWJSAB6PFHCFH07

Tutorial 16 : Shadow mapping
http://www.opengl-tutorial.org/intermediate-tutorials/tutorial-16-shadow-mapping/#result---shadow-acne

Lode's Computer Graphics Tutorial
https://lodev.org/cgtutor/raycasting.html

The original open source release of Wolfenstein 3D
https://github.com/id-Software/wolf3d

https://docs.microsoft.com/en-us/windows/uwp/graphics-concepts/stencil-buffers

Measuring the Spectral Characteristics of a Light Therapy Lamp
http://justinmklam.com/posts/2018/01/sad-lamp/

https://photographylife.com/what-is-chromatic-aberration


## Aproximaciones

- Imposible manejar realidad
- ¿Qué criteria utilizamos? Física, percepción, diseño, complejidad, costo, ...
- Depende del objetivo, y cambia según entorno

Notas:
- La realidad es demasiado complicada para modelar completamente.
- Utilizamos aproximaciones ("engañapichanga").
- Hay varias cosas para las cuales podemos optimizar: precisión física, precisión de percepción, diseño, espacio, tiempo, complejidad, costo de contenido, etc.
- Precisión física es demasiado estricta y no hace necesariamente la diferencia.
- Percepción tampoco, piensen en mapas de rutas vs. overhead - la meta importa!
- Muchos avances son mejoras de precisión física, porque son más fáciles de medir.


## Aproximaciones

<img src='images/shading-modes.png' height='440' />

Notas:
- Hay ideas viejas que son buenas de entender por sus principios, aunque no sean las técnicas preferidas de hoy.
- Ejemplo: goroud shading
- Hay técnicas que resucitaron con el uso de disposivos móbiles, donde el hardware es menos poderoso o tiene consideraciones de batería.
- A medida que las proporciones entre distintos componentes cambian (tamaño y velocidad de memoria, cantidad y velocidad de procesadores), distintas técnicas son más convenientes.


## Números reales

- Punto fijo
- Punto fijo normalizado
- Punto flotante

Notas:
- Representaciones comunes son punto fijo, punto fijo normalizado y punto flotante.
- Prácticamente nunca se usan fracciones (con dos bigints, por ejemplo).
- Cuanto menos precisión, más problemas raros podemos encontrar.


## Efecto de imprecisión

<img src='images/acne-large.png' height='440' />

Notas:
- Por ejemplo, acné cuando un punto hace sombra sobre sí mismo - su cálculo de posición desde cámara y luz es distinto.


## Efecto de imprecisión

<img src='images/acne-bias.png' height='440' />

Notas:
- Engañapichanga! Margen de error
- Quedan cosas raras: Peter Pan en la pared, hard shadow, (sugerido: pared más gruesa, sampling alrededor del punto con valores entre 0 y 1).


## Punto fijo

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <rect width="100%" height="100%" fill="gainsboro"/>
 <use xlink:href='images/punto-fijo.svg#svg8'></use>
</svg>

Notas:
- Noten que me quedó corrido el subrayado, pero me pareción apropiado para un módulo que cubre problemas de precisión.
- Son enteros donde decidimos que cierto número de bits son 'a la derecha' del punto.
- Es similar a, por ejemplo, cambiar la unidad a centímetros en lugar de metros.
- Las decisiones de diseño son con o sin signo, normalizados o no, y cantidad de bits para enteros y fracción.
- Normalmente escrito como 24.8 por ejemplo.
- Los normalizados normalmente implican estar entre 0 y 2^b-1 o -1 a 1, con algunos yuyos, como hacer que las dos representaciones más bajas sean -1, para que -1, 0 y 1 tengan representaciones exactas.
- Hoy se usan para compactar datos (por ejemplo, GL_R8 es un número de 8 bits normalizado para cosas como parámetros de materiales tipo reflectividad), para posiciones 2D durante rasterización, o en CPU para hacer cálculos más rápidos (ya fuera de uso).


## Punto fijo

<img src='images/wolf3d.jpg' height='440' />

Notas:
- en computadoras sin punto flotante, o con unidad lento o débil, o para algorithmos tipo Brensham


## Punto flotante

<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
 <rect width="100%" height="100%" fill="gainsboro"/>
 <use xlink:href='images/float.svg#svg2'></use>
</svg>

Notas:
- IEEE 754 es el estándar relevante.
- Formato para 32 bits es como la imagen, 8:23
- Incluye NaN (signaling y non-signaling), y más menos Inf, y -0.
- Hace más difícil determinar el error en un algoritmo, porque no depende del algoritmo en sí necesariamente sino de los datos particulares que se usan.
- Lo más común es 32 bits; 64 es más preciso pero es caro que sea el doble.
- Para ML, se usa también 16 bits, y en algunos modelos se puede usar menos, 8 o menos incluso, pero en ese caso normalmente usamos valores normalizados.
- Hay un caso especial de 10 bit, que entran 10 bits en un dword de 32 bits (HLSL tiene min16 y min10).
- También hay un engañapichanga min16int, min12int (donde se usan los bits de mantisa como enteros).


## Tipos de buffers

- Colores
- Profundidad
- Stencil (figura)

Notas:

Buffers de colores: suelen ser grandes, con lo cual ahorrar espacio jugando
con el formato de pixel es común. Comúnmente RGBA es red-green-blue-alpha,
pero puede haber menos canales, o pueden haber menos bits o distinta
representación por canal.

Buffers de profundidad (depth buffer): pueden ser del mismo tamaño que el color
buffer (en elementos, no formato), guardan la distancia de la cámara al pixel,
útil para varios cálculos.

Buffers de figura (stencil buffers): utilizado como máscara para dibujar,
utilizado para varios efectos. Por ejemplo, el contorno de un objeto se puede
dibujar achicándolo un poco y usándolo com stencil. Se pueden hacer sombras
también.

Otro uso de stencil buffers puede ser dibujar líneas amarillas sobre una ruta,
si son su propia figura. Los triángulos son coplanares en principio, y pueden
'pifiar' cada tanto produciendo z-buffer.

Típicamente hay optimizaciones de hardware y software (depth buffer comprime
muy bien, por ejemplo), que se aplican de forma distinta.


## Luz

- Luz
- Emisores de luz
- Transporte de luz
- Materia
- Sensores (cámaras u ojos)

Notas:

- Para modelar cómo se maneja la luz, hay que considerar varias cosas a la vez.
- Luz, emisores de luz, transporte de luz, materia, sensores (cámaras y ojos).


## Luz

- Luz
- Rojo, verde, azul (RGB)

Notas:
- La energía de la luz real se transporta en fotones.
- Los fotones son cuantos de luz - una luz más potente tiene más fotones, no fotones más potentes.
La energía de cada fotón determina la frecuencia de su onda electromagnética; esta frecuencia la percibimos como color.
- Frecuencia baja es rojo, alta frecuencia es azul.
- El ojo hace 'aliasing' sustituyendo mezclas de frecuencias - una mezcla de fotones rojos y verdes parecen fotones amarillos.
- Modelamos entonces normalmente con tres frecuencias que mezclamos: rojo, verde y azul.


## Luz

<img src='images/fluorescent.jpg' height='440' />

Notas:
- Limitaciones de RGB:
- hay fenómenos difíciles de modelar, como diferencia de luz solar vs. fluorescente (la del sol tiene más frecuencias)
- varios dispositivos (cámaras, monitores) usan distintas frecuencias - problemas de gama (gamut)


## Transporte de luz

<img src='images/refraccion-colores.jpg' height='440' />

Notas:
- El índice de refracción de un material es la proporción de la velocidad de la luz en el vacío vs. en el material.
- La velocidad de propagación depende de la frecuencia - distintas frecuencias tienen distinto índice de refracción!
- Es pequeño, así que simplificamos modelando refracción para todo el espectro, pero entonces no podemos hacer prismas que generen arco iris.
- En el borde entre volúmenes con distinto índice de refracción, la luz se dispersa por reflección y refracción, determinado por la geometría microscópica y la química del material.


## Emisores de luz

<img src='images/fluorescent.jpg' height='440' />

Notas:
- Los fotones transmiten energía, típicamente medida en joules.
- El poder de un haz de fotones es energía sobre unidad de tiempo, medida en watts.
- En lamparitas, watts es consumo, no producción! 100W puede dar 10W de luz visible, por ejemplo.
- https://www.energy.gov/energysaver/save-electricity-and-fuel/lighting-choices-save-you-money/how-energy-efficient-light
- Otra medida de luz es la radiosidad (radiosity), poder por áreas que entra o sale de una superficie, en watts sobre metro cuadrado.
- Otra medida de luz es la radiación (radiance), poder sobre área por unidad de ángulo sólido - es la cantidad transportada de un punto a otro a otro en distintas superficies (por ejemplo, un punto sampleado al plano de la imagen).
- Típicamente terminamos representando todo con un float3 de rgb (o algún tipo común similar).


## Emisores de luz

<img src='images/espectro-lamparitas.png' height='440' />

Notas:
- Los emisores son relativemente sencillos. Crean y dispersan fotones en la escena a cierto ritmo.
- Con una distribución de probabilidades sobre estos parámeteros, podemos generar fotones 'representativos' (con unos millones se tienen buenos resultados, no hace faltan miles de millones).
- Simplificamos considerando que los fotones van en grupos representativos, que se emiten de un mismo origen, e ignorando las frecuencias no visibles, y agregando las frecuencias en rgb.


## Transporte de luz

<img src='images/luz-interferencia.png' height='440' />

Notas:
- En general, ignoramos la fase y polarización.
- Hay efectos que no se modelan entonces, como anillos de Newton en luz monocromática. Lo vemos cuando hay una capa que deja pasar (refraccion) y otra abajo que la refleja (refleccion) e interactuan.


## Transporte de luz

<img src='images/luz-interferencia-color.png' height='440' />

Notas:
- O con varias frecuencias, en pompas de jabón o aceite.
- Esta simplificación después la pagamos: las superficies con reflejos ya sean espejo o 'glossy' ocurre por la interferencia de haces de fotones casi paralelos.
- Agregamos un término de Fresnel a los materiales para modelar esto, por también podría hacerse con materiales más simples y transportes más complejos.
- Pero implicaría que un ladrillo no es un ladrillo, sino una enorme cantidad de moléculas con varias composiciones que interactúan con la luz.


## Materia

- Geometría que dispersa luz
- Sólo superficies, opacas, sin interactuar con aire, sin dispersión interna

Notas:
- El modelo más sencillo es geometría que dispersa luz, únicamente sobre superficies opacas, sin interactuar con el aire y sin dispersión debajo de la superficie.
- Sirve sólo para rendering en cuanto que no modela, por ejemplo, el interior de cuerpos (no hay peso ni fuerzas que interactúen con gravedad).
- No sirve para fenómenos como niebla o piel.
- Complicamos el modelo para agregar realismo, pero podemos hacerlo de forma selectiva, por ejemplo, con un modelo más sencillo para objetos en la distancia.


## Cámaras

<img src='images/camara-interna.png' height='440' />

Notas:
- Las cámaras tienen configuraciones de lentes y sensores complicadas, donde hay varias lentes y varios sensores, y no trabajan de forma uniforme.
- La idea es modelar lo que necesitamos; muchos elementos  no son necesarios con una descripción de la escena.


## Aberración cromática

<img src='images/camara-chromatic-aberration.png' height='440' style='background-color: gainsboro' />

Notas:
- Los lentes de verdad tienen distinto foco en distintas frecuencias, con lo cual pueden producir aberraciones cromáticas (chromatic aberrations).


## Aberración

<img src='images/camara-chromatic-focus.jpg' height='440' />

Notas:
- Verde en la parte superios, violeta en la inferior.
- Otros efectos son lens flare, bloom.


## Geometría

- Superficies (no volúmenes)
- Front face vs. back face
- También para física (colisiones)

Notas:
- Algunos objetos pueden representarse como superficies con dos lados, como las alas de una mariposa. Pero pueden desaparecer. Muy molesto en VR, sobre todo con cosas estáticas.
- La mayoría tiene una única superficie "front face". El proceso de eliminar el lado de superficie no visible es 'backface culling'.
- Los objetos con transparencias tienen que manejarse modelando las superficies interiores.
- Normalmente hay geometría que se utiliza para evitar colisiones también. A veces para simplificar modelo, a veces como diseño de modelo (por ejemplo, 'paredes' para evitar que alguien se caiga, o salte sobre una pared baja).
- Ejemplo: el sistema de Unity de colliders: https://docs.unity3d.com/Manual/CollidersOverview.html


## Meshes

- Forman geometría a partir de varios triángulos
- Indexed triangles
- Nonindexed triangles
- Quads
- Con o sin adyacencia
- Con o sin lados o semilados

Notas:
- Uno de los formatos más clásicos es indexed triangles, donde los vértices están en un buffer y los índices en otro. Viene en tres variants: triangle list, triangle strip, triangle fan.
- Otro formato es nonindexed, donde tiene que estar todo en orden, pero repite vértices - como suelen ser más grandes, repetirlos juega en contra.
- Hay algunos otros formatos que a veces son útiles, como cuadriláteros, pero los triángulos tienen un único plano, baricéntricos bien definidos, no auto-intersectan, y son irreducibles a polígonos más simples (piensen en clipping).
- Para algunos algoritmos, como por ejemplo trazas el contorno de algo, necesitamos tener información topológica de adyacencia ("sólo dibujo si no tiene caras de ambos lados de un segmento").
- La adyacencia puede precomputarse, incluso para animaciones, siempre y cuando no se "rompa" o se "junte" con otro geometría.
- Un par de variantes son guardar información por cada lado, o por cada semilado (dos entradas por cada lado interno, o usar un número negativo que sea el complemento del índice del semilado presente).


## Meshes (vértices)

- Normales, UV, tangentes
- Otros: AO, UV de otras cosas tipo radiosidad, adyacencia

Notas:
- Propiedades típicas por vértice son normales (shading normals), coordenadas en textura y bases de espacio tangentes al vértice (útil cuando hay que hacer que puntos parezcan curvos).
- Otros valores precomputados en vértices pueden ser información de adyacencia, curvatura, ambient occlusion, o lo que fuere necesario.
- Varias cosas que antes se hacían con vértices hoy se precomputan o generan a partir de geometría, como light maps con magnitud (pero no dirección) de luz incidente.


## Superficies

- Implícita: $ f(P) = 0 $ (menos dentro, más fuera)
- Implícita: $ f:bbR^3->bbR:P->(P-Q) cdot bb n $ (level de punto)
- Explícita: $ g:bbR times bbR->bbR^3:(u,v)->u bbh+v bbk+Q $ (puntos de parámetros)

Notas:
- Las superficies para algunas figuras comunes se pueden representar como ecuaciones implícitas o paramétricas explícitamente.
- Las ecuaciones implícitas son funciones que hacen una prueba en un punto dado, y lo clasifica tal que f(P) > 0, =0, etc. Los =0 definen una superficie implícita, por convención <0 es dentro de la figura y >0 afuera.
- La superficie es un 'level set cero' de la función, o isocontorno.
- Por ejemplo, un plano es la implícita, donde Q es un punto en el plano y n es la normal.
- Con una ecuación explícita o paramétrica, se define una función que 'genera' puntos a partir de parámetros.
- Por ejemplo, un plano es la explícita, done h y k sone vectores linealmente independientes

- Este tipo de representaciones se usan en ray casting, por ejemplo para buscar intersecciones para hacer hit testing or ray tracing. También en rasterización para hit testing 'a mano' (en vez de dejar object ids).

- También se puede utilizar blobby modeling.


## Splines y patches

<img src='images/spline.png' height='440' />

Notas:

- Splines son representaciones que están en el medio entre representaciones
implícitas (función de superficie) y explícitas (suma de funciones
parametrizadas).

- Históricamente, la construcción era con una madera flexible, forzada a
doblarse con dos puntos, con la madera doblándose de una forma 'smooth'.

- Las curvas de spline y patches representan cada intervalo como una combinación
lineal de cuatro funciones bases predefinidas, donde los coeficientes son
puntos; la representación entonces son estos puntos.

- Un patch de spline es la superficie que se construye análogamente en 3D,
combinando varias funciones, cada una con dos variables.

- Hay varios tipos de spline, según qué bases se usan. Comunmente se usan
polinomos de tercer grado; otra opción son NURBS (Non-Uniform Rational
B-Splines). Se pueden renderear convirtiéndose en polígonos con sampling o
directamente buscando intersecciones con algo tipo Newton-Raphson.


## Newton-Raphson

<img src='images/newton-raphson.gif' height='440' />

Notas:
- Sirve para encontrar ceros, armamos la función en esa forma. Adivinamos un
  punto, vemos su derivada (con sample), buscamos el cero de esa recta y
  seguimos hasta que el error es muy pequeño . Para funciones continuas con
  único cero funciona bastante bien.
- Hoy en día, lo más común es generar geometría a partir de definiciones de
  splines ("subdivision surfaces").
- El shader de tessellation puede hacer algo por el estilo (aunque trabaja con
  vértices inicialmente).
- http://web.mit.edu/10.001/Web/Course_Notes/NLAE/node6.html


## Campos de altura (heightfields)

- Son superficies definidas por una función $ z=f(x,y) $ -- o $y=f(x,z) $, según perspectiva.

Notas:
- Hay una única altura por punto en este caso - es una limitación.


## Campos de altura (heightfields)

<img src='images/comanche.jpg' height='440' />

Notas:
- Se pueden utilizar también como displacement maps o bump maps cuando se
  utilizan para representar displacements en superficies.
- En algunos casos también se pueden trabajar realmente como funciones, por
  ejemplo haciendo efectos de agua.
- Clásico:
- comanche-altura https://www.youtube.com/watch?v=fem3ZQ1sCO0 - comanche - 1.10-1.25
- unity-worldcomposed-altura https://www.youtube.com/watch?v=kH_UPUvTuRQ - minuto 13 a 14


## Nivel de detalle (level of detail)

- Detalle según distancia
- Geometría (y animación)
- Texturas

Notas:
- En perspectiva, la mayoría del mundo tiende a estar "lejos" nuestro, y
  necesita menos detalle.  Se puede simplificar la representación con mínimo
  daño a la calidad de imagen (o incluso mejorándola, evitando problemas de
  aliasing de detalles pequeños).
- Lo más común es generar distinta geometría para un mismo objeto ("level of
  detail"). Cada LOD tiene modelos distintos; para ocultar las transiciones,
  se puede hacer un blend de baja y alta resolución, o utilizar esquemas de
  parametrización para que el cambio de morfología sea continuo.
- Para minimizar la pérdida de detalle, muchas veces se compensa aproximando
  información con texturas (por ejemplo, usar menos polígonos y usar bump
  mapping).


## Carteles (billboards)

- Clásico engañapichanga
- Aproximaciones de objetos lejanos
- Quad con textura

Notas:

- Como los cambios de punto de vista no se perciben en objetos muy lejanos, se
  puede aproximar un objeto lejano con un 'billboard' o cartel, una imagen que
  mira a la cámara con el modelo ya rendereado. Por ejemplo, un árbol con
  ramas y hojas se puede convertir en un bitmap equivalente.

- Normalmente el billboard rota para ver la cámara, pero no siempre es lo correcto - un billboard de un árbol de costado es muy distinto a uno visto directamente desde arriba!

- Para ocultar engañapichanga, se puede usar displacement mapping o guardar normales para que interactúen con luz dinámica.

- Puede usarse un billboard cloud para tener un conjunto de billboards orientados para minimizar el error visual.

- Otra varient son billboards con animaciones para objetos especiales
- Otra variante son 'impostors', donde el billboard se dibuja en runtime cuando el error de rendering es muy grande, a distintas distancias.


## Carteles (billboards)

- Billboard con parallax, Wing Commander (Origin Systems, 1990)

Notas:
- Un caso clásico de billboard con parallax es Wing Commander:
- https://www.youtube.com/watch?v=mfRvCSBD4q0 - minuto 5 a 5.30
- wing-commander-parallax


## Carteles (billboards)

- Mal hecho: popping

Notas:
- Mal hecho, 'popping':
- https://www.youtube.com/watch?v=TGJ0yzNR0xA - minuto 1.15 a 1.25
- skyrim-popping-poor


## Cielo

<img src='images/skybox.png' height='440' />

Notas:
- Hay partes del modelo que son útiles de modelar como "infinitamente" distantes.
- El ejemplo clásico es el cielo; es como un billboard, pero está armado para que pueda cubrir el horizonte.
- Llamamos 'skybox' o 'sky sphere' a la geometría que toma el lugar en el mundo.
- Normalmente la textura se ve bastante rara, porque está deformada para simular el cielo.
- Puede incluir cosas más allá de objetos, como edificios o montañas muy lejanas.


## Cielo

- Se puede animar la textura
- Witcher 3

Notas:
- https://www.youtube.com/watch?v=shT0Y160qP4 - skybox en witcher 3, minuto 5 a 5.20 - puede ser animado!
- en este ejemplo, el piso cambia con la luz del día pero las nubes no proyectan sombra


## Modelos volumétricos y voxels

- División en polihedros
- Fuerza, presión, etc. (física)

Notas:
- Además de modelar superficies, podemos modelar volúmenes, que sirven más
  para física y para iluminación con transparencias.
- Un enfoque es el de modelos de elementos finitos, donde dividimos un objeto
  sólido en polihedros, y podemos modelar fuerzas dentro del objeto, como
  temperatura, presión y flujo de fluidos. No se usa mucho para rendering.


## Modelos volumétricos y voxels

<img src='images/minecraft-voxels.jpg' height='440' />

Notas:
- Excepto, para tetrahedros o cubos, porque la regularización permite acceso
  random en tiempo constante, y simplifica la simulación. Esta representación
  es un modelo de voxels.
- Por ejemplo, voxels en Minecraft
- Los voxels estuvieron de moda en un momento, después se fueron, ahora volvieron.
- En Minecraft en particular, cada cubo es sólo el índice de elemento, con lo
  cual puede tener mundos enormes, y además fáciles de comprimir.
- Si un cubo en Minecraft ocupa un byte (digamos), en triángulos serían 12
  triángulos (x3 vértices, x3 floats, x4 byte por float), 432 bytes por cubo.
- El rendering es más granular que cubos (pueden haber personajes entre cubos,
  pueden haber rejas que ocupan un costado de un cubo).


## Sistemas de partículas

<img src='images/scenekit-particles.png' height='440' />

Notas:
- Sistemas de partículas, como el ejemplo en SceneKit de Apple.
- Normalmente, hay un gran número de partículas, cada una con un billboard, y
  no se crean y destruyen sino que se reciclan las instancias, con un 'tiempo
  de vida'.
- Hay que tener cuidado cuando intersecta geometría para que no se note el
  borde del billobard, 'soft particles' se hacen transparentes cuando están
  cerca de geometría.
- Se modela con cantidad de partículas, origen, cada cuanto 'nacen', tiempo de
  vida, render, camino, y fuerzas sobre el grupo.
- gow4-chainsaw - https://www.youtube.com/watch?v=ptm_sH1zK7Y - chainsaw kill, particles y blobs
- skyrim-spells - https://www.youtube.com/watch?v=EWfJguFckrE - skyrim fire, billboards, particles


## Niebla

<img src='images/rainier-lejos.jpg' height='440' />

Notas:
- Las partículas y voxels son representaciones discretas de figuras amorfas, pero para volúmenes homogéneos, se puede usar una representación analítica.
- El efecto clásico es perspectiva atmosférica, donde los objetos lejanos son desaturados en paisajes por la atmósfera. Por ejemplo, en la foto de Rainier en Washington.
- Otros efectos son niebla cercana, frecuentemente haciendo blend del color de la niebla según la distancia a la cámara.


## Niebla

<img src='images/bajo-agua.jpg' height='440' />

Notas:
- También pude aplicarse para hacer el efecto de atenuación de luz bajo el agua.
- Para niebla localizada, normalmente no se hace sólo en distancia a la
  cámara, sino que se toma en cuenta el volumen del cuerpo de niebla, que
  usualmente se representa con algo fácil tipo cuboide, esfera o semiplano
  (columna de humo, por ejemplo).


## Niebla

- Alan Wake, Remedy Entertainment, 2010

Notas:
- Alan Wake - niebla, partículas, bloom, heightmaps
- alan-wake-trailer


## Grafos de escena

<img src='images/scenekit-nodes.png' height='440' />

Notas:
- Normalmente la escena está dividida en varios objetos, para que puedan usarse distintas representaciones, reducir memoria, facilitar proceso y animaciones, etc.
- Típicamente se representa como un grafo de nodos, donde los edges representan las relaciones entre objetos.
- Muchas veces su utiliza un árbol más detallado, jerárquico y profundo para modelar, y uno más chato para rendering, para utilizar mejor el proceso en paralelo.
- Hay algunos tipos de simulación física que necesitan un grafo propiamente dicho, no sólo un árbol. El grafo semántico normalmente es un DAG.
- Los grafos físicos normalmente expresan relaciones entre nodos, comúnmente articulaciones.
- También hay estructuras de datos espaciales asociadas a la escena, que la
dividen para hacer preguntas eficientes como ¿qué está cerca del jugador?
- Incluyen agregados que aproximan geometría más fina.


## BSP

- Binary space partition
- Árboles con particiones con alguna propiedad (ej, visibilidad de polígonos en orden)

Notas:
- doom-bsp-traverse - https://www.youtube.com/watch?v=e0W65ScZmQw - doom BSP demo
- Las línea formas un árbol
- Cada línea define hijos donde la mitad está delante y la otra mitad detrás (tal vez particiona).
- Muy bueno para ambientes cerrados (o, al menos, evitando todo-visible-de-todo-lugar).
- Pueden usarse otros criterios además de visiblidad, y generalmente otra información.


## Modelo de materiales

- Superficie, no volumen.
- Modelado estadístico de interacción con luz.

Notas:
Para propagar la luz, no tenemos por qué considerar el volumen dentro de un
objeto normalmente, sólo la superficie. Lo interesante ocurren en el cambio de
un medio a otro (uno es típicamente el aire, aunque no siempre).

Normalmente, cada fotón o se absorbe y se convierte en calor, o pasa a través
de la superficie, o se refleja. Hay un modelo de probabilidad que lo resuelve.

Pero complicamos la implementación para poder trabajar en grupos agregados (y
para tener control artístico además de físico).


## Modelo de materiales

Normalmente agregamos:
- reflejos especulares duros (espejos)
- reflejos 'glossy' y brillos
- disperción debajo de superficie
- disperción debajo de superficie profunda
- transmición

Notas:
Normalmente agregamos:
- reflejos especulares, tipo espejos
- reflejos 'glossy' y brillos, como en una manzana
- disperción debajo de superficie, que produce color de Lambert, independiente de orientación de la cámara
- disperción debajo de superficie profunda, donde la luz se dispersa debajo de la superficie, como en piel o mármol
- transmición, donde la luz pasa a través de material mayormente traslúcido como agua o niebla

- Como son todos tips de disperción, los describimos como un función de
disperción ("scattering"). Hay algunas variantes, como bidirectional
scattering distribution function (BSDF), BRDF para superficies puramente
opacas, BTDS para superficies puramente transmisivas, BSSDF para describir
efectos de superficie y debajo de superficie.


## BSDF

- Bidirectional scattering distribution function
- $ (P,omega_i,omega_o)->f_s(P,omega_i,omega_o) $

Notas:
- Las funciones de disperción se pueden formular como (P,omega_i,omega_o)->f_s(P,w_i,w_o)
- es la densidad de probabilidad de que la luz propagándose en dirección -w_i, se disperse en dirección w_o cuando llega a la superficie en el punto P.
- `f_s`, con 's' de 'scattering', y `w_i` es la dirección desde un punto P que evaluamos hacia la luz con vector `w_i` (con lo cual la luz va en dirección `-w_i`).
- En general, cuanto más brillante la superficie, más altos son los valores de `f_s`.
- Normalmente `f_s` no es constante sobre la superficie, ni es la misma
  fórmula. Pero es común usar la misma fórmula como material, y utilizar una
  textura con los parámetros adicionales a esa función, por ejemplo en Lambert
  el color del material en un punto.
- Podemos variar esos valors a través de la superficie para simular que tiene
  manchas o áreas más opacas, o de distinto color, en vez de ser completamente
  uniforme.
- Hay un par de variantes de diseño, por ejemplo si la función varía
  considerando el material o desde un paso previo, o si asume el plano como
  mencionamos o si trabajar directamente sobre la superficie en el mundo y
  ajusta internamente.
- Hay dos formas de generar los BSDF: medir materiales, que es un proceso
  difícil, o un modelo analítico, como el de Lambert o Blinn-Phong.


## Lambert

- $ f_"lambert"(P, omega_i, omega_o) = bb omega_i cdot bb N C I_L $
- donde $omega_i$ (o `L`) es vector a luz, `N` es vector normal, `C` es el
  color del material y `I_L` es intensidad de luz

Notas:
- Basado en que la mayoría de las superficies planas y rugosas reflejan luz
con energía proporcional al coseno del ángulo entre la superficie normal y el
ángulo de la luz que llega - ley de Lambert.

- También se la llama reflectividad difusa o perfectamente difusa.

- Termina siendo una función que toma constantes - el ángulo de salida no
  importa, y refleja determinada banda de colores.

- Se usa con algún modelo de gloss o reflejo especular

- Noten que ni el punto ni la dirección de salida (el observador) importan.


## Blinn-Phong Normalizado

$ f_"bpn"(P, omega_i, omega_o) = k_L/pi + ((8 + s) k_g)/(8 pi) max(bb N cdot omega_h, 0)^s $

donde `s` es un factor de 'smoothness', y `k_L+k_g <` en cada color, y $ omega_h $ es la dirección de $ w_i + w_o $

Notas:
- Phong introdujo un model de Lambert más highlights ajustables. Más modernamente, está formulado como BSDF, lo que ayuda a conservar energía.
- Van a ver el termino pi (a menos que en algun caso se cancele) porque conservamos energia sobre hemisferio de emision en physically based renering (PBR).
- Existen bases de datos con valores físicos, por ejemplo para oro o plata.
- La segunda es de Real Time Rendering, que tiene un tratamiento más extenso y lo describe en términos de teoría de microfacetas.
- En el modelo original, el mapa especular tiene los detalles y el glossiness es constante; en los normalizados, el nivel especular es (casi) constante y está el detalle en glossiness.
- En este modelo, las constantes de Lambert están mejor definidas, tienen que ser la probabilidad sobre todas las direcciones que contribuyen a la dispersión.
- Toma tres parámetros: constante k_L de Lambert para el color e intensidad de
la reflexión opaca, k_g para el color e intensidad de reflejos 'glossy', y un
factor 's' de smoothness; cuanto más alto, más funciona como espejo.
- s no es perceptivamente lineal; 60 es reflejo de cuero, 2000 es pintura de auto o metal.
- k_L + k_g tienen que ser menor a uno para conservar energía.
- RTR: $ f(bb l, bb v)=bb c_"diff"/pi+(m+8)/(8pi) bb c_"spec"  bar "cos"^m phi_h $


## Reflejos especulares

<img src='images/reflejo-agua.jpg' height='440' />

Notas:
- Los reflejos en el agua dependen del ángulo del sol y de quien mira, y son
  buenos candidatos para BRDFs que consideran el ángulo de reflejo y origen.
- Noten la aberración abajo a la derecha.


## Transparencias

- Vidrio, niebla, ventana

Notas:
Un medio es translúcido cuando podemos ver a través de él, como vidrio, niebla
o una ventana. Para eso, algo de luz tiene que pasar a través de él.

Van a haber varios puntos de la escena contribuyendo a la energía en un punto
en la pantalla. En nuestros modelos la luz no interfiere, con lo cual su
superpocisión hace que los podamos considerar independientemente.

En la realidad hay varios haces de luz que contribuyen a un punto, pero en el
modelo de cámara de pinhole, entra sólo uno; en este caso, el haz de luz
'sigue'.

Una aproximación es hacer rendering de objetos de atrás hacia adelante, y
hacer blending de los de adelante (en vez de simplemente cubrirar) según el
valor de transparencia.

Vamos a hablar más de blending cuando hablemos de operaciones con imágenes.


## Transparencias

- Titanic, James Cameron, 1997.

Notas:

- titanic-hand
- vean la mano - hay luz ambiente que está llegando de la izquierda, y hay luz
  que llega de costado por la disperción de las gotas de agua del otro lado de
  la ventana; además hay un efecto de halo sobre la luz, por la disperción de
  las gotas (que deja de ocurrir cuando la mano pasa), hay un efecto de
  opacidad de las gotas (que son semitransparentes), y hay un efecto del
  vidrio mismo.


## Blending

- Hablamos más en imágenes.
- Modos (aditivo, con alpha, premultipicación)
- Emisión brillante, sin afectar ambiente
- Bloom
- Lens flare

Notas:
- Hay varias cosas para hablar de blending: varios modos, uso en antialias,
  premultiplicar alphas, emisión brillante sin afectar ambiente (por ejemplo,
  luces LED de una computadora, muy brillantes pero que no iluminan su
  alrededor), y bloom (blur de pixels más brillantes y blend de nuevo sobre
  superficie original) o lens flare.


## Modelos luminarios

- Luminario (luminaire) es una fuente de luz.
- Omni light (point), hemisféricas (directional), spot light, area light,
  directional, volume (engañapichanga interferencia del medio), ambient.

Notas:
- Hay distintos tipos de luces y su configuración. Muchas luces son
  artísticas, por ejemplo en una cena con luz de vela, hay montones de luces
  ambiente que ayudan a ver. Algunas luces pueden configurarse con color, o
  para sólo afectar ciertos factores con gloss.
- Algunas configuraciones comunes son luces hemisféricas (útiles para el cielo
  o con entornos distantes, un omni-light muy lejos de la escene, donde la luz
  viene 'de un lado' con rayos paralelos), omni-light (luz omnidireccional
  desde un punto de radio insignificante, a veces 'point light', como
  lamparita), area light (donde está en la escena, como una ventana), spot
  light (conos de luz con dirección), volume (sólo un volumen en escena se
  ilumina, ejemplo cono de luz de ventana para hacer god rays).
- Hay contribuciones de luz ambiente, muchas veces para compensar
  simplificaciones.
- Vean https://docs.unity3d.com/Manual/Lighting.html para ejemplos.

## Preguntas

