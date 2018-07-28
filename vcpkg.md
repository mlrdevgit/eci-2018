-*- mode: markdown; coding: utf-8 -*-

# vcpkg


## ¿Qué es?

Manejo de librerías en Windows, Linux, MacOS


## ¿Cómo funciona?

- Registro de proyectos online
- Baja fuentes y compila local
- Quedan headers y librerías para linking
- Queda alguna librería
- Parecido al pip de python

Notas:
- Cada proyecto al registrarse incluye información sobre dónde están fuentes y
  cómo compilar


## ¿Cómo se usa?

```
git clone https://github.com/Microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
.\vcpkg integrate install
.\vcpkg install sdl2 curl ...
```

Notas:
- Normalmente en algún lugar, por máquina
- O con CMake, otro programa de configuración de builds


## Otros comandos

- Qué hay instalado: `vcpkg list`
- Qué hay disponible: `vcpkg search [pat]`
- Qué targets hay: `vcpkg help triplet`


## Aviso

- vcpkg maneja distintas combinaciones de plataforma y bit-ness, por ejemplo (los "triplets")
- Ojo que el proyecto de ejemplo puede usar x64 por default, pero vcpkg compila a x86 por default
- En ese caso, van a ver que no encuentra headers, o no encuentra funciones a la hora de linking
- Asegúrense de instalar la versión o versiones que necesitan, por ejemplo para `dxut`:

```
.\vcpkg install dxut:x86-windows dxut:x64-windows
```


## Preguntas

