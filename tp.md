-*- mode: markdown; coding: utf-8 -*-

# Trabajo Práctico


## Visualización

- Cuarto cerrado
- 3m de alto
- 6x6
- 720p

Notas:

Realizar una visualización de un cuarto cerrado con el techo a 3 metros, con
6x6 metros, en una resolución de 720p.


## Contenido

- Sobre una pared, un cuadro de 1m de ancho, 0.5m de altura, borde superior a
  20cm sobre nivel visión (elijan).
- Escritorio de 0.5m x 1m, 1m de altura.
- Lámpara sobre escritorio, bombita de luz blanca.
- Luz en el centro de la habitación (techo).

Notas:

Sobre una pared, un cuadro de 1 metro de ancho y medio metro de altura, con el
borde superior a 20cm. sobre el nivel de visión. Indiquen el nivel de visión.

Una versión anterior de este documento indicaba que el cuadro era de 1m ancho
por 1m alto. Cualquiera de las dos configuraciones es aceptada.

En el medio, un escritorio de 1 metro de largo, medio de ancho y 1 metro de
altura, con una lámpara. La lámpara tiene una bombita de luz blanca siempre
prendida en su interior, y una pantalla amarilla.

La segunda fuente de luz está en el techo, en el centro de la habitación. Pueden elegir el tipo de luz y lámpara que prefieran.


## Interacción

- Moverme con WASD, girar izquierda o derecha con flechas o JK.
- Hacer click en lámpara con el mouse para prender y apagar.
- Al apagarse, la lámpara se eleva 10cm. sobre el escritorio, desciende al
  prenderse; 2seg de animación.
- No pasar a través de paredes ni suelo ni muebles.


## Display

- FPS (en pantalla o consola, o en archivo)
- Memoria utilizada (como mínimo su propio accounting)


## Resultado

- Código fuente con build support (CMake, .cmd)
- .zip con ejecutable y archivos de datos
- .md con preguntas y respuestar (ver notas en archivo)

Notas:
- Nombre y apellido del cursante
- ¿Cómo es la estructura del programa?
- ¿Qué enfoque utilizó para generar la visualización?
- ¿Qué herraminetas y librerías utilizó para generar la visualización?
- ¿Cómo afecta la pantalla a la iluminación de la escena?
- ¿Cómo implementa la animación?
- ¿Cómo verifica el nivel de utilización del GPU?
- ¿Qué técnicas utiliza para lograr 60fps?
- Conclusión: reflexión final sobre enfoque, problemas interesantes, lecciones aprendidas


## Extras?

- Dénle color a la luz de la bombita.
- Voy a hacer click en el cuadro - sorpréndanme.
- Sombras (vean notas)

Notas:
Para hacer sombras, piensen qué hace sobre qué.
https://learnopengl.com/Advanced-Lighting/Shadows/Shadow-Mapping

Para simplificar, el personaje es invisible.

## FAQ

### ¿Se puede usar OpenGL? ¿Qué versiones?
Sí, pueden usar OpenGL.

Pueden usar Vulkan si quieren, pero van a tener que manejar algunas cosas a mano.
Por ejemplo, cómo están en memoria los descritpors (resource views en DX), barreras, transiciones de estado, y estado de pipeline. 

### ¿Qué hago si sólo tengo accesso a una Mac?
Si tienen una Mac, puede entregar el proyecto usando OpenGL.

### ¿Tiene que ser físicamente correcto el rendering?
No, no hace falta que mantengan energía o hagan un modelo completo de luz. Sí espero que tengan en considaración los materiales de los elementos como para que sean distinguibles, y que tengan en consideración las fuentes de luz en la escena; pero pueden usar 'luz ambiente' y otras aproximaciones.

