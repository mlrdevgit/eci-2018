-*- mode: markdown; coding: utf-8 -*-

# Percepción

Notas:
- Referencias:
 - https://www.uv.es/asamar4/exelearning/index.html
 - http://duruofei.com/Research/KernelFoveatedRendering
 - http://www.cnbc.cmu.edu/~tai/readings/active_vision/ballard_eye_vr.pdf


## Percepción

<img src='images/ojo-interno.png' height='440' />

De Artwork by Holly Fischer - File:Three Internal chambers of the Eye.png, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=66465544


## Sistema visual

- Tolera mala información
- Tremendamente sensible a _ciertos_ errores
- Sistema con historia

Notas:
- Tolera mala información (con lo cual reconocen figuras humanas de niños)
- Tremendamente sensible a ciertos errores - por ejemplo, un pixel negro en una pantalla blanca
- Sistema con historia: la misma imagen se procesa distinta si vengo de un cuarto oscuro o brillante
- Historia: puedo reconocer más rápido objetos que vi hace poco


## Proceso

- Ojo (que enfoca y percibe luz)
- Nervio óptico
- Corteza visual (visual cortex)

Notas:
- No se sabe bien cómo funciona, pero no es monolítico; hay partes que
  funcionan primero y detectan contrastes de brillo, pequeños cambios de
  orientación y color, y frecuencias espaciales (cambios de claro a escuro por
  centímetro)
- Gruesamente, detecta "patrones"


## Proceso

- Detección de cambios
- Agrupación
- Movimiento
- Color

Notas:
- La detección de cambios de orientación y color es local; cosas adyacentes de
  distinto color, no cosas lejanas con cambios pequeños

- También empiezan a constituir agrupaciones ("un cambio acá y uno allá hacen
  un cambio grande")

- Hay características contradictorias: podemos ver rápido qué piedra es
  distinta, pero ignoramos scratches en la película

- Gran sensibilidad al movimiento

- Poca sensibilidad de color en momentos discontinuos - pequeños cambios de un
  día al otro ("envejecimiento de pintura")

- Muy buen reconocimiento de similaridades de color bajo distinta luz - algo
  es reconocible al sol y la sombra - incluso a la vez ("toda la manzana")


## Generación de imágenes

- Meta: buena percepción
- Percepción no es uniforme
- Percepción miente
- Todo es una porquería: https://en.wikipedia.org/wiki/Filling-in

Notas:
- La meta es generar buena percepción - más es al pedo

- Muy difícil encontrar una buena medida de similaridad de imágenes; distancia
  cuadrada es común, pero no toma para nada en cuenta la distribución ("un
  punto blanco local es igual a un level cambio de tono de gris")

- La sensibilidad no es lineal, sino logarítmica; notamos más diferencias en
  superficies más oscuras (el blanco "satura" la visión)

- Experimentos auditivos muestran que un pequeño sonido en lugar de un fonema
  no es percibido - se percibo el fonema "correcto" - la señal no llega a la
  conciencia, sino la información procesada

- Aparentemente, somos concientes de una mezcla procesada de señales de bajo
  nivel e inferencias de alto nivel, con backtracking corrigiendo errores de
  más alto nivel ("no hay una cara en el árbol, es una corteza con forma
  rara")

- Tarea para el hogar: https://en.wikipedia.org/wiki/Filling-in, ver cómo el
  cerebro rellena áreas estables con su alrededor - es un proceso global


## Ojo

<img src='images/ojo-interno.png' height='440' />

Notas:
- De un nivel alto, el ojo es un globo, encajado en el cráneo, con músculos
  enganchados y otros soft tissues

- Dos focos ayudan a estimar distancia y posición (probar alternan rápido
  entre un ojo y otro viendo algo de un metro)


## Ojo

<img src='images/eyesection.svg' height='440' />

<small>De Based on Eyesection.gif, by en:User_talk:Sathiyam2k. Vectorization and some modifications by user:ZStardust - Trabajo propio, Dominio público, https://commons.wikimedia.org/w/index.php?curid=2411216</small>

Notas:
- Córnea y lente (cristalino) mueven luz, la pupila controla la apertura, y el
  eje de visión encaja en la fóvea.
- La imagen se invierte al pasar por el lente, y si no encaja sobre la fóvea,
  aparece fuera de foco
- El índice de refracción varía levemente con la frecuencia de la onda; en un
  microscopio, el borde tiene "colores"
- La pupila puede ajustar unas 10 veces la luz (sistema rápido), pero el resto
  del ajuste es químico (los cambios de iluminación son diez órdenes de
  magnitud en intensidad en la vida cotidiana, de un cuarto oscuro a luz de
  sol de verano)
- La retina es "la parte de atrás", donde están los receptores.
- Hay un disco óptico que es un punto ciego, donde encaja el nervio óptico; no
  verlo es parte de la compensación de alto nivel, a unos 3-4mm de la fóvea
  para el lado nasal


## Ojo - Retinografía

<img src='images/retinografia.png' height='440' />

https://en.wikipedia.org/wiki/Blind_spot_(vision)

Notas:
- Chapter 28 de la biblia
- Tarea para el hogar: https://en.wikipedia.org/wiki/Blind_spot_(vision), ver
  cómo hay un punto ciego


## Fóvea

- Más conos que bastones
- Luz azul
- Distintos tipos de conos para color

Notas:
- Dos tipos de receptores: conos y bastones (cones and rods)

- Hay otras células que responden a luz en el espectro azul pero no alimentan
  al nervio óptico, sino que usan para ajustar el ritmo circadiano

- Bastones detectan luz en situaciones de luz baja, y los conos con más luz

- Hay tres tipos de conos, que responden a distintas longitudes de onda, que
  dan la sensación de color

- Hay muchos más bastones que conos, unos 20:1, de distribución no uniforme,
  menos concentrados la fóvea


## Fóvea

<img src='images/rcdist.gif' height='440' style='background-color: gainsboro' />

Notas:
- Las adaptaciones de luz reducen la sensibilidad en áreas cercanas
  (inhibición lateral), lo cual hace que resalten más los cambios abruptos

- ¿Cuál es la sensibilidad a cambios o bordes? Hagan líneas alternadas de
  blanco y negro y aléjenlas hasta que se confundan; aproximadamente 1.6
  minutos (1 minuto es 1/60 de un grado)


## Fóvea

http://duruofei.com/Research/KernelFoveatedRendering


## Movimientos sacádicos

- Movimientos de ojo
- Engañapichanga suprime blurring

Notas:
- La fóvea en sí abarca uno o dos grados de visión; el ojo se mueve
  continuamente en movimientos sacádicos (saccades) (o en movimiento más largo
  de más de 200ms) para cubrir áreas; hay adaptación engañapichanga para
  evitar problemas de percepción (suprime blurring; motion blur en Alan Wake
  Live).

- Tarea para el hogar: delante de un espejo, medio metro, mirar un ojo, luego
  el otro; no se percibe el movimiento. Fílmense con una cámara para ver el
  cambio de posición


## Continuidad de color

<img src='images/grey-square-illusion-1.gif' height='440' />

Notas:
- Tomando información del ambiente, la percepción adapta
- Un auto de día o de noche se reconoce con el mismo color, no como dos colores distintos


## Continuidad de color

<img src='images/grey-square-illusion-2.gif' height='440' />


## Continuidad de color

<img src='images/gradient-illusion.svg.png' height='440' />


## Continuidad de formas

- Un auto visto más grande cuando todo es más grande está visto de más cerca; no creció todo
- Un auto de costado cuando todo está de costado rotó, no se deformó


## Continuidad de formas - ojo

<img src='images/vertical-illusion.png' height='440' />


## Leyes de Gestalt

- Enumeración de efectos, 1920, psicólogos alemanes
- Proximidad
- Similitud
- Buena continuidad
- Contraste

Notas:
- https://www.uv.es/asamar4/exelearning/21_las_leyes_de_la_gestalt.html
- Proximidad: agrupación de elementos
- Similitud: agrupación por características comunes como forma o color
- Buena continuidad: agrupación (e identificación) de cosas orientadas de forma similar
- Contraste: los elementos se distinguen por sus diferencias


## Aplicaciones

- Espacio de colores
- Diseño de funciones de corrección gamma
- Motion blur
- Simular defectos en córnea o lente
- Simular adaptación de luz
- Movimientos sacádicos en VR (y su supresión) para orientar gente
- Discontinuidaddes en percepcion, swapchain y buffers

Notas:
- Precisión no lineal (espacio de colores, más adelante)
- Diseño de funciones de corrección gamma (valores no lineales de brillo entre 0 y 1 en dispositivos y en percepción)
- Motion blur para evitar una sucesión de frames fijos
- Simular defectos en córnea o lente (video: Tomb Raider Bloom Flare)
- Simular adaptación de luz - 21.51-22.20
- Saccades en VR (y su supresión) para orientar gente
https://youtu.be/eDk4HrEtGrM
- discontinuidaddes en percepcion, cosas de swapchain

