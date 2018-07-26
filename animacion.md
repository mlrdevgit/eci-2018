-*- mode: markdown; coding: utf-8 -*-

# Animación

Notas:

Principios de animacion
https://www.evl.uic.edu/ralph/508S99/contents.html


## Arte y Producción

Juan Manuel Martelli


## Introducción

<img src='images/animacion.gif' height='440' />

Notas:
Animación es el proceso de mostrar varias imágenes que llamamos frames en rápida sucesión, dando la ilusión de movimiento.
La secuencia se llama animación.

Vamos a ver algunos métodos básicos para describir el movimiento de objetos en un mundo 3D a través del tiempo.
Principalmente dependen de interpolar entre posiciones clave (key positions), o simulaciones físicas.

Hay un importante componente de arte en la animación, ya sea tanto en producciones artificales como en producciones realistas (el efecto 'Hollywood physics').

Hacer una simulación perfecta no es necesariamente el objetivo.


## Ejemplo - poses de caminar

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <rect width="100%" height="100%" fill="gainsboro"/>
 <use xlink:href='images/animacion.svg#svg8'></use>
</svg>

Notas:
Digamos que queremos tener una figura de persona caminando.
Tenemos una malla de triángulos, representada para una lista de vértices y una lista de caras.
Preparamos de antemano la figura en varias posiciones, con el mismo número de vértices pero en distintas coordenadas; llamamos a cada una de esta poses una key pose o key frame.

La terminología viene de animación a mano, donde artistas hacián los key frames y los animadores asistentes hacían 'tweening', o los frame 'in between'.
Hoy tenemos un artista que hace las poses y un algoritmo que hace la interpolación.
Muchas veces el animador no es el que hace las mallas.

Para movimientos repetitivos, hacemos un ciclo (cycle), donde repetimos un número finito de poses.


## Ejemplo - poses de caminar

$ t_0 = floor(t/p)p $

$ bb (x) = bb x^**(t_0) $

Notas:
 `t_0` redondea a un entero múltiplo de p. p es un período de tiempo entre keyframes. x asterisco es un valor definido por un keyframe en un tiempo determinado.
 
Para hacer la animación, asociamos un período de tiempo entre cada key frame, que normalmente va a ser mucho más largo que nuestro framerate, con lo cual tenemos que hacer una estrategia de qué mostrar en el medio.
La más fácil es 'sample and hold', donde mantenemos la pose hasta que llegue el siguiente momento de actualización.

Una variante casi idéntica es nearest-neighbor, donde usamos el keyframe más cercano en tiempo.


## Ejemplo - poses de caminar

$ t_0 = floor(t/p)p $

$ t_1 = t_0 + p $

$ alpha = (t - t_0)/p $

$ bb x(t) = (1 - alpha) x^star(t_0) + alpha x^star(t_1)$

Notas:
Más común es una interpolación lineal entre poses. Es decir: buscar un keyframe,m el siguiente, ver dónde estás, e interpolar desde donde estás al siguiente.

Para hacerlo en varios vértices, podemos hacerlo de un vértice por vez, o considerar cada valor en cada vértice de toda la malla e interpolar entre todos los valores.

Algunos problemas con este equema:

- La animación no preserva volumen. Un giro de 180 puede achatar al personaje en una línea y extenderlo en otra dirección en vez de girarlo.
- El ciclo de caminar no se adapta a la superficie, el pie flota sobre el aire o se hunde en el piso si está inclinado.
- Dentro de la animación, el vértice no tiene movimiento en keyframe, y tiene aceleración infinita entre keyframes.
- Las animaciones son smooth pero la transición entre animaciones es abrupta. Ejemplo de mover un brazo en el aire.
- La animación es completa, no podemos atar el movimiento de los brazos con el de las piernas como animaciones independientes. Si quiero llevar una caja, tengo que volver a modelar las piernas. Si es completamente independiente, ahora tengo que coordinar brazos y piernas en balance.
- No hay control de mayor nivel, está todo expresado en vértices, en vez de brazos o piernas.
- La animación lleva mucho tiempo de hacer, y no hay forma de reusar esta animación para otra malla.


## Ejemplo - disparo de cañon

- Sea of Thieves, Rare, 2018

Notas:
Para considerar una bola de cañón, van a haber varias animaciones que entran en juego, la bola rota se desplaza por el aire, y podemos considerar el efecto del viento. Pero hay una animación principal, 'root animation', que determina el disparo y en la cual nos concentramos.

Para este tipo de animación, agarramos el libro de física y buscamos la aceleración que otorga la gravedad, consideramos la masa de la bola, la velocidad con la cual sale del cañón, y lo demás es aritmética.

https://www.youtube.com/watch?time_continue=847&v=jt8xRaZkxwE - min 14:20 a 14:40

Hay algunas cosas que faltan en este esquema:

- No hay colisión contra objetos, lo cual normalmente produce una respuesta - algo se rompe, se desacelera, rebota.
- ¿Cómo hacemos la ecuación de rotación sobre su centro?
- ¿Qué hacemos para especificar algo más complejo, como una persona bailando? Es demasiado difícil o costoso definir una ecuación para cada movimiento.


## Ejemplo - robot en edificio

- Warcraft: Orcs &amp; Humans, Blizzard Entertainment, 1994
- El problema del mudador de piano

Notas:
En este caso, no hay un artista definiendo poses, sino que un actor (normalmente por alguna forma de inteligencia artifical) decide cuál es el objetivo que quiere alcanzar, y cuáles son los pasos intermedios.

Esto se soluciona con motion planning, relacionado con path finding, algoritmos para encontrar un camino entre dos puntos. Clásicos algoritmos de Dijkstra para esto, el más común es A*.

- Path finding en warcraft: warcraft-walk: https://www.youtube.com/watch?time_continue=42&v=fbfaBJ4nOBI
- Otra formulación es piano mover's problem: piano-mover-first https://www.youtube.com/watch?v=HdfAzUXvmOQ

Es campo de estudio también en robótica, donde por ejemplo hay que considerar cambios locales y más incertidumbre sobre el mundo.


## Buffering

- Double buffering, vertical sync, latencia, triple, tearing, etc.

Notas:
Acá es donde realmente entra en juego lo que vimos en elementos de programación con respecto a double buffering.
Cuando hay movimiento o animación es cuando vemos problemas de tearing y tenemos que considerar vertical synchronization.


## Percepción

- No hay refresh rate biológico.
- Sensible menos de 25Hz, invisible más allá de 80Hz.
- Ampieza a partir de 10Hz, pero depende de solapado!

Notas:
Los modelos biológicos actuales no tienen noción de refresh rate o un shutter
uniforme en el ojo o en el cerebro, pero esto funciona. Aparentemente casi
todo el fenómeno de movimiento (vs. cosas que aparecen y desaparecen
rápidamente) ocurre en el cerebro, aunque la retina exhibe la tendencia de
mantener imágenes por algunos milisegundos, lo cual puede interactuar con el
proceso de imágenes.

Uno de los efectos de esta prolongación es que el sistema humano es sólo
sensible de manera considerable a los parpadeos o cambios de imagen hasta los
25Hz, y es insensible a frecuencias mayores de 80Hz. Es por eso que la luz
fluorescente, a 50 o 60Hz, es prácticamente imperceptible, y la mayoría de los
monitores puede refrescar a 60 a 85Hz (y algo más con dispositivos tipo
head-mounted display).

Este fenómeno de percepción de movimiento arranca a los 10Hz cuando los
objetos tienen cierto 'overlap' en la secuencia. Noten que es el mínimo, y si
el overlap es insuficiente, parecen objetos que separados que aparecen y
desaparecen. Con lo cual, cuanto más rápido se mueve un objeto, más framerate
necesitan para mantener la ilusión de movimiento.


## Interlacing

<img src='images/interlacing-malo.jpg' height='440' />

Notas:
Varios formatos de transmisión de televisión usan interlacing, donde se
alternan la mitad de las filas. Cada una de estas mitades son 'fields' o
'campos'. Las filas de pixels se llaman 'rasters', y deben ser combinados
correctamente.

La ventaja de interlacing es que sólo se transmite la mitad de la información,
pero rara vez puede ser percibido.

Este es un caso donde está mal hecho, y aparece el efecto de 'combing'.


## Motion blur

<img src='images/motion-blur.jpg' height='440' />

Notas:
En cámaras reales (y el ojo), el tiempo de apertura no es cero. Con tiempos de
apertura pequeños (10 ms) y luz interior, el ruido de fondo sobre los sensores
pueden introducir ruido en la imagen. Con tiempos muy pequeños, (0.1ms) puede
no haber suficientes fotones incidentes en cada pixel para que los resultados
queden 'smooth'.

El efecto que ocurre con exposición muy rápida es que no hay sensación de
movimiento, con lo cual un auto en movimiento y uno que no se mueve son
idénticos. Algo que ocurre en la realidad es con un tiempo de exposición real,
vamos a tener motion blur, que interpreptamos como sensación de movimiento.

Una de las formas de aminorar el alias temporal es elevar el refresh rate y
hacer un render por refresh; con un dispositivo de 240Hz, podemos cuadruplicar
los frames contra uno de 60Hz. Pero esto reduce el impacto, no lo elimina
completamente (más allá de que 240 no es común).

Otra técnica es hacer la integración a través de varios frames, lo cual
produce el efecto de motion blur sin tener que aumentar el refresh rate. Esto
se utilizar en ray tracing y en rasterización. En juegos, técnicas comunes
incluyen agregar geometría traslúcida sobre el vector de movimiento, aumentar
el MIP level artificalmente, y screen-space como post-proceso cuando hay una
velocidad asociada a los pixels.


## Coherencia temporal

- Cambios limitados de un frame al siguiente.
- Ojo con pifiar.
- Ojo con inconsistencias (stutter).

Notas:
Normalmente los cambios de un frame a otro son limitados. Esto es lo que
decimos en 'frame coherency' o 'temporal coherency'. En 2D, la técnica clásica
era usar 'dirty rectangles', cosa que todavía pueden ver en programación de
Win32. En 3D, se puede aplicar por ejemplo en no recalcular shadow maps a
menos que algo se mueva dentro del frustrum visible.

Hay dos problemas con las cuales hay que tener cuidado. El primero es que hay
un costo asociado a ver si los resultados anteriores, memoizados o en un
cache, son válidos. Si no es así, te comés el costo de chequeo y además tenés
que hacer el trabajo. El segundo es que esto lleva a tiempos de ejecución
inconsistente, y la inconsistencia puede ser problemática para aplicaciones
como juegos que esperan mantener un frame rate.

Otra consideración para utilizar coherencia temporal es el problema del primer
frame. En el caso de juegos, el costo de 'steady state' es muy alto, muchas
veces escondido detrás de una pantalla de carga de nivel. En el caso de
películas, los nodos distribuidos de render farms no comparten cómputos
intermedios, con lo cual todos los frames son el primer frame.


## Representaciones

- Pose, estado, parametrización
- Nivel de detalle
- Tradeoffs

Notas:
El estado de un objeto o escena es toda la información requerida para
especificar su pose. Para animar, necesimatos el estado y un esquema de cómo
parametrizarlo; por ejemplo, para una manzana que cae, necesitamos su
posición, su forma y la cómo actúa la gravedad sobre ella.

Noten que el nivel de detalle que usamos no es uniforme. Muchas veces tenemos
modelos bastante detallados de forma y geometría para rendering, pero usamos
un modelo simplificado para simulación física.

Podemos modelar un "objeto" a distinto nivel de abstracción y complejidad. Por
ejemplo, un auto como un único objeto nos dá muy pocas partes, pero
necesitamos un modelo más complejo para controlarlo. Modelar los pistones,
engranajes y ruedas como objetos produces más partes, pero cada una tiene
modelos más sencillos. Una de las consideraciones es qué comportamientos se
producen de forma natural vs. cuáles tienen que programarse
explícitamente. Por ejemplo, en un choque, separamos las partes del auto que
se mueven de forma independiente, vs. tener que determinar cómo crear las
partes e inicializarles a partir del objeto del auto.


## Representaciones

- Partículas: humo, balas, gente en una muchedumbre.
- Cuerpos rígidos: naves espaciales, cajas.
- Cuerpos rígidos deformables: pelota de volley.
- Cuerpos rígidos articulados: robot
- Sistemas de resortes: ropa, cuerdas
- Esqueleto con piel: humano, animales
- Fluidos: agua, aire, barro

Notas:

Algunas representaciones comúnmente utilizadas son éstas, en nivel de
complejidad (más o menos).

También tenemos una idea de 'level of detail', donde podemos hacer inercia y
aceleración de una nave espacial como si fuera un cuerpo rígido, pero hacer
colisiones o animaciones como si fueraun cuerpo rígido articulado.


## Sistemas de representaciones

- Keyframes
- Dinámicos (leyes mecánicas o no)
- Mixtos

Notas:
En un sistema de key frames o key poses, un animador (el artista de animación) especifica las poses.
La interpolación intenta decidir qué hubiera elegido el animador; como es un creación expresiva y no necesariamente algorítmica o realista, no es un problema completamente resuelto.
Sin embargo, para poses suficientemente densas, es un problema tratable y es una técnica común.

En un sistema de dinámica, los objetos se representan por posición y velocidad, y aplicamos leyes físicas (que pueden o no ser las del mundo real).
Las leyes mecánicas de física son conocidas, pero tienen dos problemas: estabilidad numérica (evitar incrementar la energía del sistema) y control artístico.
Puede ser también difícil hacer efectos realísticos en la forma deseada, por ejemplo una explosión donde una parte en particular se dirige hacia la cámara.

El el caso de animación procedimental, hay un programador y/o artista que define una ecuación para la pose en función del tiempo.
Se utiliza por ejemplo para animar el movimiento de un sistema solar o algo por el estilo, donde no hay un sistema dinámica en el sentido general pero no trabajamos con keyframes.


## Sistemas de representaciones

```glsl
void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 sun_center = vec2(200, 200);
    vec2 earth_center = sun_center;
    float sun_dia = 10.0;
    float earth_dia = 10.0;
    
    earth_center.x += 30.0 * sin(iTime);
    earth_center.y += 30.0 * cos(iTime);

    float sun_dist = distance(fragCoord, sun_center);
    float earth_dist = distance(fragCoord, earth_center);
    fragColor = vec4(0, 0, 0, 0);
    if (sun_dist < sun_dia)
        fragColor = vec4(1, 1, 0, 0);
    if (earth_dist < earth_dia)
        fragColor = vec4(0, 0, 1, 0);
}
```

Notas:
ShaderToy - https://www.shadertoy.com/new

ShaderToy es medio raro porque pensamos 'per pixel'. La pregunta es si estamos
dentro de un circulo u otro. La animacion viene de antes, en este caso
considerando el centro, y usamos cos/sin para hacer la tierra rote alreadedor
del sol.


## Sistemas híbridos

- Keyframes y sistemas dinámicos
- Inverse kinematics (demo Urho3D)

Notas:

Algo que se utiliza por ejemplo es combinar poses clave con sistemas
dinámicos. Por ejemplo, para caminar, buscamos evitar que el pie se hunda,
usando inverse kinematics (IK). La idea es resolver un sistema donde tenemos
poses, una serie de restricciones o constraints, y una meta; la solución son
las poses intermedias que mejor satisfacen las restricciones (y tal vez la
pose final). Algunas restricciones pueden ser que todas las articulaciones
permanezcan juntas, que ninguna articulación exceda su límite angular, que el
objeto no pierda su equilibrio.

https://urho3d.github.io/samples/45_InverseKinematics.html

Esto funciona muy bien para movimientos simples y situaciones controladas,
pero se complica más para hacer movimientos realistas por ejemplo al
agacharse - cuánto doblar las rodillas vs. la espalda (que tambiés es en gran
parte una decisión artística - ¿qué refleja del personaje un movimiento u
otro?).


## Sistemas híbridos

<img src='images/pescados.jpg' height='440' />

Notas:
Otras complicaciones que requieren atención es en movimiento de muchos
personajes en masa, donde decisiones locales tienen que tener sentido global,
y el problema se asemeja un poco a movimientos de fluidos.

Además del movimiento raíz o root motion, tenemos movimientos secundarios que
normalmente son consecuencia o están atados al primario. Por ejemplo, el
movimiento de la ropa o el pelo que acompaña un movimiento primario.

Otra técnica es el de transferencia de movimiento. Por ejemplo, en vez de
tener varios actores de distintos tamaños para distintos personajes, tenemos
un único actor y traspasamos los movimientos. O combinamos movimientos de
persona y caballo para hacer un centauro.

La solución de una animación posible (plausible animation) es el problema de
determinar dado el estado final, cuál es una animación que podría haber
terminado en ella. Por ejemplo, si queremos que un par de dados caiga de forma
determinada, podemos calcular cómo podrían tener que rodar.


## Interpolación de poses

- Lineal si es posible, sin cambios en la malla
- Ojo con discontinuidades

Notas:
La forma más directa es que cada key frame tenga una malla particular, con una topolgía constante, donde las posiciones de los vértices varían pero no su orden ni adyacencia, y lo único que hacemos es interpolar la posición.
El problema con una simple interpolación lineal es que produce velocidad discontinua cuando cambiamos de keyframe. Una solución es usar splines, pero requiere más costo de cómputo y datos, y los resultados pueden ser difíciles de controlar. Otras variantes son utilizar parámetros de aceleración e ir calculando velocidades.


## Animación de root frame

- Movimiento en el mundo
- Representación de modelado vs. rendering

Notas:
Normalmente expresamos geometría y animación respectos al marco de referencia del objeto.
Esto hace que por ejemplo para caminar, el cuerpo no se mueve y las piernas se columpian debajo del torso.
Lo que hacemos luego es aplicar el movimiento al marco de referencia del objeto como vinimos haciendo con transformaciones sucesivas.

Si bien usamos una matriz de 4x4 para rendering como representación más común, a la hora de editar un objeto es común usar ángulos de Euler (roll, yaw, pitch) y un vector de traslación.
A la hora de animar, en cambio, utilizamos un cuaternón y un vector de traslación para facilitar operaciones como integración.


## Cuerpos articulados

- Árbol de objetos al rescate
- Restricciones y límites

Notas:
Para cuerpos articulados que no siempre se mantienen en una misma posición con respecto uno al otro, podemos modelarlos como distintos cuerpos u objetos que son parte de un subgrafo o sub-escena.
Uno de los objetos es la raíz, y el resto se articula con respecto a él.
Naturalmente, puede haber más de un nivel.

Llamamaos a esta estructura cuerpo articulado porque comúnmente son articulaciones en el modelo.
La articulación es una restricción en el movimiento relativo de los dos objetos.
Por rejemplo, en un auto, el centro de las ruedas tiene que estar sobre el eje del auto.
Una puerta tiene que articularse sobre el marco.


## Animación de esqueleto

- Combinación de malla y 'huesos' (articulaciones)
- No se lo tomen literalmente

Notas:
La idea en animación de esquelto es definir una serie de marcos de referencia
que llamamos huesos (aunque en general terminan modelando articulaciones), en
un espacio común o en una jerarquía.

Definimos los vértices en la malla como una combinación weighted de múltiples
marcos de referencia, por ejemplo diciendo que un vértice en el antebrazo está
a mitad de camino entre el codo y la muñeca, alejado un poco hacia afuera.

El método común es poner huesos dentro de una malla en una pose estándar, y
asignarle pesos de hueso a cada vértice, para que el sistema compute el peso
sobre cada vértice. Luego movemos el esqueleto a otra pose estándar, y
corregimos las articulaciones que quedan fuera de lugar, y el sistema puede
reajustar los pesos para minimizar los errores en ambas poses.

El sistema queda 'overconstrained' rápido, con lo cual el artista puede ir
introduciendo más huesos para ajustar el sistema, incluyendo huesos que no
tienen un análogo biológico. Introducir estos nuevos huesos para que un
optimizador de los resultados correctos es difícil y parte del motivo por lo
cuales los animadores de rigs están en demanda.


## Preguntas

