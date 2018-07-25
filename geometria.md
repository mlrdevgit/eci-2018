-*- mode: markdown; coding: utf-8 -*-

# Geometría


# Geometría

<img src='images/sphere.png' height='440' />

Notas:
- La idea es entender un proceso matemático lo suficientemente bien como para
  poder implementarlo.
- Con geometría, es importante diferenciar las propiedades de entidades de
  puntos o líneas y las de su representación numérica. Por ejemplo, al cambiar
  sistemas de coordenadas, las propiedades numéricas pueden varias, pero la
  geometría no se altera.
- Hay operaciones, como encontrar el punto medio entre dos puntos, que no se
  ven afectadas por el sistemas de coordenas; dividir un par de coordenadas en
  dos, sin embargo, sí (si están en el centro ni se mueven).
- Una combinación de operaciones donde los coeficientes suman uno es una
  combinación afín y no varía con el cambio de sistemas de coordenadas -
  tienen "significado geométrico".
- Una intuición es que la combinación termina dependiendo exactamente de los
  puntos, sin "contribuciones" externas.


## Trigonometría

<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <style>text { fill: white; font: 10px sans-serif; }</style>
  <polyline points="20,80 180,20 180,80, 20,80" stroke="azure" fill="none" />
</svg>

Notas:
- Con tener dos longitudes, se deriva la tercera, se deriva el ángulo, se deriva todo.
- Las identidades sirven porque empezás de distintos puntos de información y
  vas resolviendo el resto.


## Trigonometría

<img src='images/transportador-r.svg.png' height='440' />

2 pi radianes, ahorra conversiones.


## Trigonometría

<img src='images/transportador-g.svg.png' height='440' />

Grados sexagecimales, más intuitivos en el día a día.


## Trigonometría

<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <style>text { fill: white; font: 10px sans-serif; }</style>
  <polyline points="20,80 180,20 180,80, 20,80" stroke="azure" fill="none" />
  <text x="20" y="80" dx="30" dy="-2">&alpha;</text>
  <text x="70" y="40">hipotenusa</text>
  <text x="70" y="75">cateto adyacente</text>
  <text x="160" y="50" dx="-30">c. opuesto</text>
</svg>

Notas:
Para recordar nombres:
- empezando de un punto "interesante" (no el del ángulo rectángulo)
- hipotenusa y catetos
- hiptenusa es el que está inclinado
- los catetos adyacentes y opuestos son los otros, en relación al ángulo


## Trigonometría

<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <style>text { fill: white; font: 10px sans-serif; }</style>
  <polyline points="20,80 20,20 180,80, 20,80" stroke="azure" fill="none" />
  <text x="160" y="80" dx="-30" dy="-2">&alpha;</text>
</svg>

Notas:
- Uso fundamental: proyección sobre eje
- La altura es igual ya sea que dibuje los ejes de un lado u otro


## Trigonometría

- coseno: adyacente / hipotenusa (coxis)
- seno: opuesto / hipotenusa (yen)
- tangente: opuesto / adyacente (Dire Straits)

Notas:
Tres proporciones fundamentales: seno, coseno, tangente.

https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Trigonometria_aa1.svg/280px-Trigonometria_aa1.svg.png

Coseno del ángulo interesante es adyacente sobre hipotenusa. Tiene que ser
"sobre hipotenusa" porque siempre tiene que ser menor a 1, y la hipotenusa es
el lado más largo. Recuerden "cos" o "cox" por "coxis".

Seno del ángulo interesante es opuesto sobre hipotenusa. Yen, como la moneda japonesa.

Tangente del ángulo es sin hipotenusa; opuesto sobre adyacente. Dire Straits, "so far away from me", 'tan lejos de mí', 'tan' es el de lejos sobre el de cerca.


## Trigonometría

<img src='images/trigonometria-plot.svg.png' height='440' style='background-color: gainsboro' />


## Inversas

Razones inversa:
- Inversa de tan es cotan.
- Inversa de seno es cosecante (cruzados, o "inversos").
- Inversa de coseno es secante.


## Inversas

Funciones inversa:
- De seno, arco-seno arcsin.
- De coseno, arco-coseno arccos.
- De tangente, arco-tangente, arctan.
- Muchas veces escritas $sin^-1$ por arcsin.
- atan2(y,x) - angulo dado x,y (maneja cuadrantes)

Notas:
- Mil identidades y boludeces.


## Pitágoras

$ a^2+b^2=c^2 $

$ sqrt(a^2+b^2)=c $

Notas:
- Usado todo el tiempo para distancias
- Recuerden que no necesitan raíz a la hora de comparar


## Vectores

- Uso en puntos y desplazamientos
- Especiales: cero y elemento-"i-avo"
- Vector unidad (normalizado dividiendo por longitud)

Notas:
Se utilizan todo el tiempo, geométricamente para distinguir coordenadas.

Hay algunos vectores especiales; cero (todos elementos en cero),
elemento-i-avo (donde todos ceros excepto el i, útil para descomponer vector
en coeficientes).

La longitud de un vector es la raíz de la suma de los cuadrados. Si el vector
es un desplazamiento, la longitud es llamada "distancia".

Un vector con longitud 1 es un vector unidad. Para conseguir un vector unidad,
se puede normalizar un vector dividiéndolo por su longitud.

Operaciones comunes con vectores son sumarlos, multiplicarlos por una
constante (multiplicación escalar), producto punto/interno/escalar (dot product) y
producto cruzado (cross product).


## Puntos vs. distancias

$ (1-alpha) P + alpha Q $

donde:
- P y Q son dos vectores
- $ alpha $ está en `[0, 1]`, en 0 es P, en 1 es Q

Notas:
- Ojo que hay cosas que no tienen sentido. Dividir las coordenadas de un punto
  en dos dá distintos resultados si cambiamos el frame; no tiene un sentido
  geométrico. Para un desplazamiento, sí.
- Podemos tener una definición paramétrica de la línea que pasa por P y Q, y
  podemos extendernos antes de P o después de Q


## Cross Product

<img src='images/cross-product-components.gif' height='440' style='background-color: gainsboro' />

<small>https://www.mathsisfun.com/algebra/vectors-cross-product.html</small>

Notas:
- Para cross product, sale un vector perpendicular a los originales.
- Hay dos vectores perpendiculares, uno para cada lado.
- La regla de mano derecha es apuntar con indice el primero y mayor el segundo, y el vector sale para donde apunta el pulgar.
- Pruben invertir el orden de productos y van a ver lo que pasa.


## Cross Product

$ [[v_x], [v_y], [v_z]] times [[w_x], [w_y], [w_z]] = [[v_y w_z - v_z w_y], [v_z w_x - v_x w_z], [v_x w_y - v_y w_x]] $

Notas:
- Uso común es encontrar vectores normales a una superficie.


## Cross Product

<img src='images/cross-product-angle.gif' height='440' style='background-color: gainsboro' />

$ a times b = |a| |b| sin(theta) n $

Notas:
- donde a, b son vectores
- theta es el angulo entre ellos
- n es el normal perpendical


## Dot Product

$ v cdot w = v_1 w_1 + ... + v_n w_n $

Notas:

Dot product o inner product se utiliza para conseguir ángulos, resulta en un
escalar, no un vector.


## Dot Product - vectores unidad

$ v cdot w = cos(theta) $

$ theta = cos^-1 ((v cdot w) / (norm(v) norm(w)))  $

Notas:
- Dot Product es producto interno, producto interior, producto punto. Es escalar - unico valor por vectores.
- Algebraicamente, suma de productos de cada entrada. Nomenclatura '.'.
- Geometricamente, son las magnitudes multiplicadas por el coseno de su angulo (o la proyeccion)
- Intuición de resultados; 1 si es igual, -1 si contrario, 0 si perpendicular
- Las cosas ortogonales o perpendicular dan cero de dot product.
- Cuando son paralelos, el coseno es uno y entonces es el producto de las magnitudes.
- Uso: proyección de vectores sobre otros vectores, sin calcular ángulos


## Matrices

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <use xlink:href='images/matmul.svg#svg8'></use>
</svg>

Notas:
- Producto de matrices A nxk y B kxp es una matrix nxp (las dimension del
  medio son las mismas y 'desaparecen'), A está a la izquierda y B arriba en
  una visualización mnemónica.


## Operaciones

- La diferencia entre dos puntos es un vector.
- La suma de un punto y un vector es otro punto.
- La suma o diferencia de vectores se efectuá con la suma o diferencia por elemento.
- La suma de dos puntos no está definida.
- Ojo al programar si usan el mismo tipo!


## Líneas

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <use xlink:href='images/linea-implicita.svg#svg3931'></use>
</svg>

Notas:
- En general, y=mx+b como representación de líneas no se usa, porque no permite representar una línea vertical.
- Pueden usar un par de puntos sobre la línea, lo cual define un vector normal
  a la línea. Si el vector entre un punto y un punto original proyectado sobre
  este vector normal es cero, está sobre la línea. O sea, Ax+By+C=0, puesto
  distinto.


## Líneas

$ (X - P) cdot n = 0 $

Notas:
- Esta es la forma implícita (en vez de la paramétrica).
- Con eso podemos difinir la línea para cualquier X, diciendo que (X - P) . n
  = 0, donde P es un punto en la línea y n es el vector normal de ella.
- Una ventaja de trabajar con vector y productos internos es que sirve para 2d y 3d.
- A veces la misma generalizacion ayuda para entender mas dimensionalidades
  cuando es dificil de ver en 4d.


## Interseccion de líneas

$ gamma(t_0) = (1 - t_0) P + t_0 Q $

$ l = { X : (X - S) cdot n = 0 } $

$ v = P - S $

$ u = Q - P $

$ t_0 = (-v cdot n) / (u cdot n) $

Notas:
- Acá mezclamos forma implícita (isolíneas, cero), con paramétricas (dos
  puntos y una razón entre ellos).

donde:
- t_0 es la entrada a la funcion de la linea con la solucion
- v es P - S, donde P es un punto de una linea, S es punto de la linea l
- n es la normal a la linea l
- u es Q - P, donde Q y P son puntos de la linea

La funcion de la linea implica que si t_0 esta entre 0 y 1, la intersección está entre P y Q.

Derivación en pág 167 de la biblia.


## Planos

$ (X - Q) cdot n = 0 $

- donde `Q` es punto en plano y `n` es normal
- Como punto y línea, pero rayo y plano.


## Esferas

Definidas típicamente por distancia: un punto X está sobre la esfera cuando

$ (X - Q) cdot (X - Q) = r^2$

donde:
- Q es el centro
- r es el radio

Notas:
- Son longitudes cuadradas para hacer el cálculo más fácil.


## Esferas

$ (v cdot v - r^2) + t(2d cdot v) + t^2(d cdot d) = 0 $

$ t = (-b +- sqrt(b^2 - 4ac))/(2a) $

donde:
- v es es P - Q, y queremos `t` tal que `P+td` intersecte la esfera

Notas:
- Recuerden que hay dos soluciones a una cuadrática.
- Intersección de esfera con rayo.
- Hay una dualidad entre forma paramétrica e implícita.
- En general, las intersecciones más fáciles son cuando están en
  representaciones distintas.


## Triángulos

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <use xlink:href='images/triangulo-param.svg#svg3931'></use>
</svg>


## Triángulos

$ R=(1-s)(1-t)A+(1-s)tB+sC $

donde:
- A, B y C son los vértices del triángulo
- `Q=(1-t)A+tB` está entre A y B
- `R=(1-s)/q+s/c` está entre Q y C

Notas:
- con t y s entre 0 y 1, esto define a todos los puntos dentro del triángulo


## Triángulos

Como función:

$ F : [0,1] times [0,1] ->R^2: $

$ (s, t) -> (1-s)(1-t)A+(1-s)tB+sC $

Notas:
- Esta es una forma parametrizada del triángulo que se usa mucho.
- Esto es un punto dentro del triángulo, con proporciones.


## Triángulos

$ (1-s)(1-t)+(1-s)t+s $

$ = (1-s)((1-t) + t) + s $

$ = (1-s)+s $

$ = 1 $

$ alphaA + betaB + gamma C $

Notas:
- La suma de coeficientes es uno! Tiene significado geométrico!
- Reescribiendo alpha A + beta B + C gamma C para todos los puntos, llamamos
  alpha, beta y gamma las coordenadas baricéntricas.


## Semiplanos

- Una función $F(x,y)=Ax+By+C$, donde A y B no son ambos cero, es un plano que
intersecta una línea l en el plano x-y.

- El semiplano es la desigualdad $Ax+By+C>=0$ (y &lt; para el otro lado).

- Uso en determinar puntos dentro de triángulo.

Notas:
Ahora: un triángulo en un plano es equivalente al área entre tres
semiplanos. Sirve para saber si un punto está dentro del triángulo.

Por esto importa también el orden de los puntos: cada semiplano tiene un signo
en cada lado según su orientación, e invertir el orden de un par de puntos
invierte el signo.

Por cierto, una vez que está fuera del triángulo por un lado, ya se sabe que
está completamente afuera.


## AABB

- Axis-Aligned Bounding Boxes
- Cuboides alineados a los ejes
- Uso en física, detección de colisión, ray tracing, etc.

Notas:
- Representaciones muy sencillas, son cuboides alineados a los ejes, con lo
cual hacer tests es muy sencillos ("están las coordenadas del lado correcto?")

