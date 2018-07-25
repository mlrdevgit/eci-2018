-*- mode: markdown; coding: utf-8 -*-

# Performance Intro


## Conceptos

<img src='images/perf-wpa-sample.png' height='440' />

Notas:

Los sistemas modernos son muy complejos. Hay muchas partes que interactúan de
forma independiente, a través de muchos subsistemas, los cuales a su vez
tienen comportamiento complejo.

Por una cuestión de entropía, los sistemas que no tienen objetivos de
performance y no controlan su performance, corren un enorme riesgo de no tener
buena performance.

Este módulo es un repaso de ingeniería de performance en lo abstracto - más
adelante vamos a hablar de performance en particular.


## Plan

<img src='images/perf-objetivos.jpg' height='440' />

Notas:

La idea es comenzar por objetivos de performance. Los más comunes van a estar
relacionados con tiempo de respuesta, throughput, utilización de recursos, y
cargas de trabajo soportadas.

Fundamentalmente los objetivos se establecen fuera del marco de lo puramente
ingenieril, por ejemplo si el tiempo de respuesta de una operación es de 500ms
o de 100ms o de 10ms. A veces está atado a una métrica de negocio, por ejemplo
en web van a ver que el número de conversiones puede estar influenciado por el
tiempo de carga o de proceso de un sistema. A veces está atado a otra métrica,
como puede ser frames per second para simular animación frente a una pantalla
para cierto tipo de contenido, pero incluso ahí el valor no es absoluto y
puede caer dentro de un rango donde entran otras consideraciones, como el
costo de optimización, o consideraciones de calidad o complejidad de
simulación.


## Metodología

- 60 frames per second
- 16ms por frame
- ¿qué trabajo necesito por frame?
- ¿cuánto puedo "gastar"?

Notas:

Empezamos con los objetivos, por ejemplo queremos un juego de 60fps para ser
competitivos en el mercado, para hacer un juego tipo Witcher, con un mundo
abierto con un número limitado de actores y una mezcla de ambientes abiertos y
cerrados.

De ahí derivamos un presupuesto. Si tenemos 60fps, tengo 16ms para hacer un
frame. Puedo tener más latencia por ejemplo, 100ms, pero el pipeline tiene que
sacar cada 16ms.


## Presupuesto

<img src='images/perf-loop.png' height='440' />

Notas:

Por ejemplo podemos modelar un 'game loop' clásico como leer inputs, aplicar
input, animaciones y física, y dibujar. Hay más sistemas que pueden correr
antes o después en paralelo, por ejemplo el proceso de input, y lo que tarda
el contenido en pasar por el compositor, y si está en una televisión el tiempo
de proceso en el televisor (que muchas veces depende del modo). Con lo cual no
es tan raro que un juego de 60fps tenga 100ms de latencia (recuerden que hay
una radio en el controlador, una radio en la consola).

La noción de prespuesto es importante porque permite dividir, por ejemplo,
dedicando parte a input, parte a física, parte a dibujo. Cosa que también
puede utilizarse para dividir por equipos, con lo cual la parte organizacional
también importa (así como la arquitectura es un reflejo de la organización, el
presupuesto también está atado).

Ley de Conway: "organizations which design systems ... are constrained to
produce designs which are copies of the communication structures of these
organizations."


## Presupuesto

- 600MB de memoria
- X cantidad de código paginado
- ¿qué tipo de datos necesito mantener en memoria?
- ¿cuánto uso de audio, video, comunicaciones, simulación?
- ¿cómo lo mido, pongo límites, ajusto?

Notas:
En consolas es más fácil decidir el prespuesto, con lo cual es más común ver
su utilización, pero funciona para cualquier cosa.

Pueden tener un presupuesto por cada objetivo o recurso escaso. Otro ejemplo
clásico es tener un prespuesto para CPU (en consolas es fácil sabiendo cuántos
cores, entonces los sistemas más importantes culturalmente terminan con más
cores, y cosas tipo audio que son muy importantes pero no demandan tanto
terminan compartiendo tiempo en un core).


## Otros recursos

- ancho de banda
- CPU
- memoria
- ancho de banda de memoria
- proceso de audio
- espacio en disco
- ancho de banda de disco

Notas:

Una vez que hay objetivos y presupuestos, vas midiendo contra ellos y
refinándolos. Al principio del proyecto, se puede trabajar con prototipos que
pueden medir el peor caso o mejor caso, o para evaluar distintos diseños.

Es importante ser proactivo; ser reactivo hace el trabajo mucho más difícil,
porque a veces no es sólo cuestión de deshacer un cambio que produjo un
problema (lo que ya es difícil), sino deshacer todo lo que vino después. Y
hace muy difícil encontrar el punto donde hay que revisitar objetivos.


## Consideraciones prácticas

- Manejo de riesgo
- Diseño de organización
- Válvula de escape
- Sean medidos :D

Notas:

Es un ejercicio de manejo de riesgo. Donde hay más riesgo porque algo es más
desconocido e importante, hay que poner más recursos; en otras áreas, menos.

Asociar responsabilidades con personas y prespuestos es una buena forma de dar
autoridad y autonomía. A la vez, el arquitecto sabio no se gasta todo el
prespuesto; muchas veces hay una reserva para emergencias. Pero es bueno
penalizar y no permitir que todo el mundo cuente con que le van a sacar las
papas del fuego.

Schedule Chicken: cuando dos grupos trabajando para un objetivo común en
colaboración, y ambos dicen que llegan a tiempo aunque ninguno de los dos lo
hace; cada uno espera que el otro declare primero que no llega para que se
demore el proyecto completo (y se lleve la culpa).

Empiecen con una medida chota, alguien con un profiler a mano. Pero midan en
el hardware correcto. Si entienden lo que midieron, ya tienen la mitad de la
batalla ganada. Tener un proceso de medida automatizado también ayuda
mucho. Para ver un ejemplo de reportes y demás, por ejemplo, la gente de
Google Chromium tenía bastante buena documentación y recursos en su momento.

Una buena idea es centralizar toda la información (o tener todos los links
centralizados), con objetivos, prespuesto, cargas de trabajo, pruebas y
resultados.


## La vida es difícil

- Cambios externos
- Cambios internos
- "Mejoras" (unicornios!)
- Cambios no locales

Notas:

Idealmente cuando hay una regresión pueden encontrar la causa. Ojo entonces al
cambiar el sistema. Por ejemplo, distinto sistema operativo, distinto driver,
distinta placa de GPU, distinto procesador, distinta cantidad de memoria,
velocidad de memoria, otro trabajo que esté ocurriendo, cambios en velocidad o
consumo de poder del dispositivo, cambios de datos (nuevo artwork).

Ojo con cambios internos, también, cuando una optimización en un lugar hace
que otro funcione mejor, hay que tomarse el tiempo y tal vez trabajar de forma
aislada para asegurarse de que las mejoras son globalmente positivas.


## Consideraciones generales

- Comunicación: bajo coupling, colas
- Concurrencia con cuidado
- Manejo de recursos - ¿qué necesitan y qué están comprando?
- SOA vs AOS
- Un caché sin evicción es un leak

Notas:

Hay principios que vale la pena tener en cuenta en muchos dominios.

Por ejemplo, cuando el canal de comunicación es lento, conviene tener diseños
con bajo coupling y minimizar el costo.

Las colas son un buen mecanismo para separar creación de trabajo de su
ejecución, pero necesitan cuidado en diseño y uso.

Cuidado con uso de concurrencia - simple suele ser mejor, por una cuestión de
complejidad, falta de reproducibilidad, y porque en un cerebro chico es más
fácil considerar un programa lineal que todos los posibles programas que
pueden correrse en un momento.

Cuidado con el manejo de recursos, y cuidado con cuánto van a pagar por
manejarlos.

Ejemplos clásicos de juego son allocators de área, que se liberan de una, o colas circulares.

Estructura de arrays vs. arrays de structuras - cuál es el patrón de acceso?

Cachés - cómo inicializarlos, cuál es la política de eviction, qué datos poner
vs. recomputar.


## Engañapichanga

- Demorar
- Bajar calidad (¡con cuidado!)
- Distraer
- Agregar elementos baratos

Notas:
- Demorar trabajo (resultado listo, haga clic para terminar).
- Bajar resolución y upsample. Tal vez de forma adaptiva.
- Bajar resolución y blur.
- Temporal antialiasing.
- Temporal y blur.
- Animación de transición (fade to black, fade to grayscale, zoom in or out).
- Cambios de diseño de nivel o experiencia.


## Ejemplos

<img src='images/perf-wpa-sample.png' height='440' />

Notas:

- Windows Performance Recorder: qué hace cada control.
- Windows Performance Analyzer: símbolos
- taskmgr
- Otras herramientas: memoria (memoria virtual, heaps, heaps manejados),
  comunicación de red (Fiddler, netmon)


## Cerrando

- Objetivos
- Presupuesto
- Medidas
- Pruebas
- Reportes
- Feedback
- Arquitectura, diseño, programación, review

Notas:

La idea de trabajo en performance no es concentrarse en trucos; son
divertidos, pero para conseguir resultados hay una disciplina efectiva que no
es obvia pero que sí es efectiva: objetivos, presupuesto, medidas, pruebas,
reportes, feedback; actividades de arquitectura, diseño, programación,
review.

Dentro de esta disciplina, podemos buscar soluciones de forma creativa, y
podemos encontrar resultados que nos llevan a replantear objetivos, de forma
positiva y negativa.

Acá es donde 'premature optimization' es raro - la optimización tiene que ser
el nivel correcto en el área correcto en el momento correcto.

Referencias

Improving .NET Application Performance and Scalability

https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff647946(v%3dpandp.10)#improving-net-application-performance-and-scalability


## Preguntas

