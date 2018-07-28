# Material de curso ECI 2018


## Contenido

El material está armado a partir de archivos de texto plano, con formato en markdown.

Pueden leerlo directamente, o pueden utilizar los scripts dentro de `utils` para armar la presentación.

Si quieren ver las fórmulas que aparecen como `$ ... $` pueden verlas en la presentación o pegando el contenido en [AsciiMath](http://www.asciimath.org/).


### Lunes

Arrancamos viendo la arquitectura de software que utilizamos clásicamente para utilizar GPUs.

- [Introducción](intro.md)
- [Arquitectura de software](arquitecture-soft.md)
- [Librerías: OpenGL, WebGL, Metal, DirectX](libs.md)
- [Lenguajes de programación: GLSL, MetalSL, HLSL](langs.md)
- [Pipeline de gráficos: de triángulos a pixels](pixels.md)


### Martes

Vemos la arquitectura de hardware, que explica por qué todo es tan raro.
Y lo que no llegamos a cubrir el lunes.

- [Tessellation](tess.md)
- [Percepción](percepcion.md)
- [Geometría](geometria.md)
- [Transformaciones](transform.md)
- [Arquitectura de ejemplo: GCN](gcn.md)
- [Unidades programables](programables.md)
- [Unidades de función fijas](fijas.md)
- [Memoria y cachés](caches.md)
- [Performance Intro](performance-intro.md)


### Miércoles

Representaciones aproximadas de realidad, física y arte.

- [Representaciones](representaciones.md)
- [Animación](animacion.md)


### Jueves

Aplicación a aprendizaje de máquina: redes neuronales, inferencia, entrenamiento.

- [Aprendizaje de máquina](ml.md)
- [Frameworks](frameworks.md)
- [Inferencia](eval.md)
- [Modelos de programación](modelos-prog.md)
- [Color](color.md)


### Viernes

Aplicación a rendering: técnicas, color, etc.

- [vcpkg](vcpkg.md)
- [Performance](performance.md)
- [Mallas](meshes.md)
- [Cámaras](camaras.md)
- [Dispositivos Móbiles](mobile.md)
- [Escenas](escenas.md)
- [Trabajo Práctico](tp.md)


## Preparado de presentación

Los siguientes scripts pueden utilizarse para armar la presentación, incluyendo dependencias en contenido externo.

- `external\download.py`: baja imágenes y videos, arma clips
- `utils\presentacion.py`: arma la presentación (asumiendo que corrió download) con algún contenido particular, y la ejecuta

Para conseguir todo el software, pueden utilizar algo como [Chocolatey](https://chocolatey.org/). Por ejemplo, una vez disponible, desde una consola de administración, pueden correr los siguientes comandos.

```
choco install ffmpeg
choco install firefox
choco install git
choco install nodejs
choco install python2
choco install python3
choco install sysinternals
choco install vlc
choco install youtube-dl
```

Las siguientes son herramientas útiles a la hora de preparar material, pero no necesarias para correr la presentación.

```
choco install anaconda3
choco install blender
choco install emacs
choco install graphviz
choco install inkscape
```

## Preguntas

Si tienen preguntas adicionales o encuentran problemas con el material, prueben abrir un item en

https://github.com/mlrdevgit/eci-2018/issues

