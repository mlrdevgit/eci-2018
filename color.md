-*- mode: markdown; coding: utf-8 -*-

# Color


## Historia del color

Teoría de antigua Grecia:
- los colores existen en espectro de oscuro a claro
- los cuatro colores primarios son fuego, aire, agua y tierra
- la oscuridad no es un color sino ausencia de luz (!!)
- Newton: luz blanca es mezcla de color

Notas:

Newton descubre que la luz blanca no es ausencia sin mezcla de colores (experimentos con prismas)
Puede hacer colores como magenta que no existe en arco iris, recombinando colores no adyacentes


## Historia del color

<img src='images/goethe-rueda.jpg' height='440' />

Notas:

Goethe hace su rueda colores como Newton, pifia con la oscuridad, pero usa
magenta, amarillo y azul, y hace experimentos de percepción.


## ¿De qué color hablamos?

- Física
- Percepción

Notas:

Distintas combinaciones de luz pueden producir la misma percepción de
color. Entonces es bueno ser claros de si hablamos del fenómenos físico (esta
luz tiene cierta combinación de frecuencias) vs. perceptivo (esta luz la veo
verde).

Vamos a hablar de color como el fenómeno perceptivo, y como distribución de
espectro como el fenómeno físico.


## Problemas de color

<img src='images/verde-rojo.png' height='440' />

Notas:
El ojo es aproximadamente logarítmico - la diferencia entre 1 unidad de
intensidad y 4 unidades es la misma que la diferencia entre 16 y 64.

Algo para preguntar - ¿quién tiene algún problema viendo colores?
Aproximadamente 1% de las mujeres tiene, y entre 8-10% de los hombres. Los más
comunes son deficiencias de percepción entre rojo y verde (terrible para
charts); hay amarillo-azul (raro) y todos los colores (muy raro).

No diseñen entonces usando sólo color para interfaces. La recomendación de mi
amigo es diseñar en blanco y negro, usando tonos de gris y patrones, y después
agregar color al final. Igual para presentaciones de datos.


## Distribución de espectro

<img src='images/espectro-lamparitas.png' height='440' />

Notas:
La luz es una forma de radición electromagnética; la luz visible va entre 400
a 700 nanómetros. Las lamparitas comunes emites una mezcla que percibmos como
blanco, un LED emite unos 640nm que percibimos como rojo.

La distribución de poder de espectro ('spectral power distribution' (SPD)) es
una función que describe el poder en cada longitud de onda. Puede tener casi
cualquier forma, pero no puede ser negativa.

Se pueden utilizar filtors que permiten pasar sólo algunas longitudes de
ondas, o sólo ciertas regiones; podemos sumar las funciones para tener una
nueva distribución, podemos multiplicarlas por una constante positiva para
tener una nueva.


## Distribución de espectro

- Funciones monoespectrales
- Onda de luz dominante

Notas:

Algunas funciones son importantes y fáciles de entender. Las monoespectrales
tienen poder en una única longitud de onda (o una banda pequeña). Todos los
otros SPD pueden escribirse como una (infinita) combinación lineal de ellas.

Ojo: en este modelo una luz completamente monoespectral no lleva energía,
porque la describimos en parte como una integral sobre la longitud de onda;
tiene que tener un intervalos, por ejemplo de 650 a 650.1 nm.

En SPDs, hay infinitos valores para tabular, o hay que presentar información
abreviada. En colorimetría, consideramos algunos valores fijos, y usamos
términos como longitud de onda dominante, pureza de excitación o luminancia
para presentar resúmenes.

La onda de luz dominante es la de mayor intensidad; la pureza de excitación va
entre 100% (si es la única longitud existente) a 0% si hay varias de misma
intensidad - mide qué tan 'monoespectral' es.

Con radiación de cuerpos negros (resultado de calentar metal con electricidad
en una lamparita), las funciones son bastante 'smooth', no 'spiky', con lo
cual estos parámetros dan una buena descripción.


## Percepción y psicología

- Nombres
- Qué cosa tiene color
- Constancia de color ("color constancy")

Notas:

Hay mucha psicología y sociología detrás de nuestra percepción de color, desde
los nombres de colores que usamos ('azul', 'índigo', 'celeste', 'cobalto'),
hasta la asignación de color ("luz marrón" vs. "árbol marrón"). Tenemos la
habilidad de identificar color a través de iluminación, 'color constancy'; una
remera azul en un armario oscuro es azul aunque no entre luz, no es negra.

Pero fisiológicamente, no hay diferencia entre luz que llega directo de un
emisor y luz reflejada. Son distinciones que hacemos a un nivel más alto.


## Hue / Saturation / Value

- Intensidad
- Saturación
- Matiz

Notas:

Uno de los modelos para describir luz es intensidad, saturación y matiz
("hue"). Un color puede ser azul oscuro o claro pero seguir siendo azul; más
azul o menos azul (más gris); o más o menos violáceo. Como son mayormente
independientes y no otro factor fácil de percibir que sí lo sea, los usamos
como un espacio de tres dimensiones.

Demo paint, color picker.


## Conos

<img src='images/cones-spectrum.svg' height='440' />

Notas:

Los receptores del ojo vienen como conos y bastones. Los bastones son sensible
a todas las longitudes de onda, los conos vienen en tres tipos, con distintas
longitudes de onda: 580, 545, 440, comúnmente rojo, verde y azul, aunque el
rojo y verde son más bien un amarillo naranja y un amarillo verdoso. Usamos a
veces LMS por longitud long-medium-small, pero también decimos rgb.

Noten que hay frecuencias que estimulan varios conos a la vez, y que hay
frecuencias en las que necesitamos más energía para producir el mismo nivel
de estimulación.


## Brillo

- La eficiencia es personal, la manejamos de forma estadística.
- Candelas (intensidad luminosa, considerando percepción).
- Otros: nits (sobre área), lux (ángulo sólido), lumen (área y ángulo sólido)

Notas:

Hay una función de eficiencia luminosa que indica, para distintas frecuencias,
cuánta intensidad es necesaria para que parezca igual de brillante que
otra. Las frecuencias 'en el centro' de nuestro rango de percepción de 400 a
700 son las más eficientes, y tiene una distribución campana.

La eficiencia luminosa varía según la persona y según la edad; los valores
que usamos como referencia son tabulaciones de muchas observaciones.

El valor que usamos es en candelas, que mide la intensidad luminosa. Una
pantalla LCD puede dar unas 250 candelas sobre metro cuadrado (una candela
sobre metro cuadrado es un 'nit'). La luz de la pantalla de un cine es de unas
40 candelas por metro cuadrado.

Ojo que no podemos usar candelas para representar escenas en escala de gris,
porque distintas superficies absorben/reflejan distintas longitudes en
distintas cantidades, y perdemos esta información importante a medida que se
propaga.

Aside: ángulo sólido se mide en steridians (sr), y es una medida de cuánto
campo de visión (field of view) es abarcado por un objeto.

Los bastones dominan a los conos cuando hay luz baja 'photopic' vs
'scotopic'. La curva de respuesta de la segunda es distinta de la primera,
tiene un pico an ondas más cortas y baja a cero cerca de los 650nm, con lo
cual no pueden detectar luz roja hacia este extremo, con lo cual la luz roja
es buena para instrumental que tiene que usarse con luz baja, porque no hace
que los bastones se ajusten para considerar su intensidad.


## CIE Lightness

$ L^star = {(116(Y/Y_n)^(1/3)-16,Y/Y_n<0.008856),(903.3Y,Y/Y_n>=0.008856):} $

Notas:

La CIE (Commission Internationale de l'Eclairage, Comisión Internacional de
Iluminación) define 'lightness' (valor, tono) - http://www.cie.co.at/ con esta
fórmula.

La fórmula toma Y ('luminance' o luminosidad), Y_n es el valor blanco de
referencia. Tiene un segmento para valores de luz muy baja, menos de 100 veces
más bajo que el blanco de referencia (0.008856), con lo cual termina siendo
negro y no se suele considerar por separado, y luego tiene una parte
logarítmica.


## CIE 1931

<img src='images/cie-1931.png' height='440' />

Notas:

Espacio de colores de CIE 1931. No es perfecto, hay muchos verdes, pero sirve
para varias cosas interesantes que vamos a ver en un momento.

https://en.wikipedia.org/wiki/Color_model#/media/File:CIE_1931_XYZ_Color_Matching_Functions.svg


## Más complicaciones

<img src='images/helmholtz.svg' height='440' />

Notas:

Ojo que la percepción cambia según el color también.

Ahora, como la vista se adapta, si bien el rango total es de 10^9 en luminance
de habitación oscura a pista de esquí de día, hay un rango más estrecho, fuera
del cual la luminosidad queda saturada en los bastones; los conos empiezan a
adaptarse, de a segmentos y también se van adaptando.


## Descripción

- Variedad de formas de describir

Notas:

Usamos muchos términos para describir la luz que vemos. Hablemos de
luminosidad en superficies, brillo de fuentes de luz, matiz (hue) para
caracterizar rojo, violeta, etc., gris para combinaciones de blanco y negro,
tintes para colores puros con blanco, otros como 'shades', 'tones'.

Los colores que percibimos como más puros son las fuentes monoespectrales que
tienen distintos picos de percepción en conos.


## Descripción

<img src='images/espacios-colores.png' height='440' />

Notas:

Podemos armar diagramas con combinaciones monoespectrales (aunque hay una
infinidad de ondas para combinar) y cambiar esas combinaciones. Una
combinación se percibe como un color, según cuánto excite los conos S, M y
L. El diagrama de las respuestas de mayor valor para S, M y L tiene forma de
cono.


## Mitos

- Colores primarios.
- Violeta.
- Objetos coloreados.
- $ A + B = C $

Notas:

Tres colores primarios. La idea de la luz suma y a las pinturas restan se basa
en la idea de absorción. En realidad, hay infinidad de colores que pueden
elegirse como 'primarios', pero algunos van a permitir más combinaciones que
otros.

El violeta no es un color real. No ocurre en el arcoiris, mezclando distintos
puntos del espectro, pero sí produce sensaciones de color!

Los objetos tienen color. Más bien tienen un perfil de ondas que
reflejan. Incluso la 'luz blanca' del sol es distinta a la 'luz blanca' de un
estudio de televisón, lo cual la gente de cosméticos te puede decir.

Color A y B hacen C. Depende de cómo! Mezclar colores es distinto, por
ejemplo, que dejarlos secar y crear capas de colores, donde parte de la luz va
a ser reflejada en cada parte.


## Descripciones estandarizadas

- Pantone
- Munsell
- CIE 1931

Notas:

Un sistema clásico es el de Pantone, donde distintos colores tienen números
estandarizados para impresión, con mezclas calibrada de tintas estandarizadas.

También hay un sistema de Munsell, donde varios colores están organizados en
hue, value y chroma, donde colores adyacentes tienen una misma 'distancia' en
el espacio de color, según observadores.


## CIE 1931 (de nuevo)

<img src='images/cie-1931.png' height='440' style='background-color: gainsboro' />

Notas:

Hay varios model de CIE, uno de los más conocidos es de 1931, que define tres
primarias X,Y,Z con la propiedad que el triángulo con estos tres vértices
incluye casi todas las respuestas de sensores - algunos tienen regiones
negativas, con lo cual no son físicamente realizables, pero tienen ciertas
ventajas - Y define la curva de eficicencia luminosa (importante para
televisión en blanco y negro, donde el color se transmite por otra banda), y
X,Y,Z son cero o positivos en todos sus puntos, con lo cual todos los colores
se pueden expresar como combinaciones no lineales de primarias. RGB es
convertible a XYZ.

El diagrama de cromacidad de CIE muestra las combinaciones de X e Y (los
colores están definidos para tener brillo constante, con lo cual se puede
recuperar Z) de esta definición.

X, Y y Z (mayúsculas) son los valores que incluyen su poder, se normalizan
dividiéndolos por X+Y+Z para obtener los valores x,y,z. Con lo cual la
transmisión suele ser de x,y e Y - z es 1-x-y, y luego X=Y(x/y), Y=Y, Z=Y
(1-(x+y))/y


## CIE 1931

<img src='images/cie-1931-notas.gif' height='440' style='background-color: gainsboro' />

Notas:

El diagrama de 1931 usa mucho espacio para verdes, y no tanto para los
púrpuras y rojos donde podemos ver más. Hay uno de 1976 que mejora esto, pero
no ganó aceptación.

El diagrama puede utilizarse para buscar colores complementarios, aquellos que
combinados forman el iluminante blanco (están simétricamente opuestos al
punto). Podemos definir la pureza según cuán cerca está del borde (y lejos del
blanco).

Otro uso es para determinar la gama de un dispositivo; dados tres puntos
dentro de la curva, cualquier luz dentro de ese triángulo puede producirse -
con lo cual, por cierto, ningún dispositivo puede producir todos los colores
sin un número infinito de monoespectrales.

Hay una línea de púrpuras que no son colores monoespectrales como los de la
parte curva; tienen que formarse con la combinación de monoespectrales de
adentro.


## CIE (no luv)

```glsl
float hue2rgb(float p, float q, float t) {
    if(t < 0.0) t += 1.0;
    if(t > 1.0) t -= 1.0;
    if(t < 1.0/6.0) return p + (q - p) * 6.0 * t;
    if(t < 1.0/2.0) return q;
    if(t < 2.0/3.0) return p + (q - p) * (2.0/3.0 - t) * 6.0;
    return p;
}

vec3 hslToRgb(float h, float s, float l){
    vec3 rgb;
    if(s == 0.0){
        rgb = vec3(1.0,1.0,1.0); //achromatic
    }else{
        float q = l < 0.5 ? l * (1.0 + s) : l + s - l * s;
        float p = 2.0 * l - q;
        rgb.r = hue2rgb(p, q, h + 1.0/3.0);
        rgb.g = hue2rgb(p, q, h);
        rgb.b = hue2rgb(p, q, h - 1.0/3.0);
    }
    return rgb;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
    const float bandas_x = 10.0;
    const float bandas_y = 3.0;

    vec2 uv = fragCoord/iResolution.xy;
    vec3 ca_rgb = vec3(1,0,0);
    vec3 cb_rgb = vec3(0,1,0);
    vec3 ca_hsl = vec3(0,1.0,0.5);
    vec3 cb_hsl = vec3(0.33,1.0,0.5);
    
    if (uv.y < 0.5) {
	    fragColor = vec4(mix(ca_rgb, cb_rgb, uv.x), 1);
    }
    else {
	    vec3 interp_hsl = mix(ca_hsl, cb_hsl, uv.x);
	    fragColor = vec4(hslToRgb(interp_hsl.x, interp_hsl.y, interp_hsl.z), 1);
    }
}
```

Notas:

https://www.shadertoy.com/new

Noten que hay otros espacios de color CIE Luv y CIE Lab que son uniformes en
lo perceptivo en cuanto a distancias en el diagrama - el 1931 no lo es
(distancia en XYZ no parecen ser uniformes, distancias de verdes parecen más
pequeñas que cuando atravesamos de verde a rojo, por ejemplo).

En este caso, RGB es el de abajo, se oscurece y pasa mucho tiempo en verde.
En HLS, perceptualmente todavía vemos cambios en qué brillante es el color.
En HLSLuv, sin embargo, esto está corregido.

Ejemplo de cómo no es uniforme: https://programmingdesignsystems.com/color/perceptually-uniform-color-spaces/

Noten que como la luz de un color puede tener varias combinaciones que no se
perciben, en la presencia de ciertos objetos o filtros sí se notan. La luz
blanca en general no tiene este efecto porque no es 'spiky', pero sí se nota
en algunas luces tipo LED.


## Blancos y temperatura

<img src='images/cie-temperatura.png' height='440' />

Notas:

Noten finalmente que el punto blanco puede variar un poco, y varias de las
fórmulas lo usan como referencia, por ejemplo para convertir Luv a XYZ. Hay
varios blancos 'estándar' definidos por CIE, que intentan acercarse a la
distribución de cuerpos negros de distinta "temperatura", D65 para 65000 K por
ejemplo.


## Espacios de colores

- Percepción de colores no es uniforme en cuanto a luminosidad.
- R'G'B' es RGB con corrección de gamma 

Notas:

La percepción de luz no es uniforme; distinguimos más cambios en el lado
oscuro del espectro. Con lo cual vamos a utilizar una fórmula para que quede
cuantizado correctamente - queremos que la representación numérica sea más
exacta en el espectro donde importa.

Los CRT que se utilizaban en la primeras televisiones emitían intensidad
proporcianal a 5/2 del voltaje. Con lo cual se puede tomar el L* (que tiene un
exponente 1/3) y aproximar bastante bien (es decir, la respuesta del sistema
visual parece I^1/3). La señal representative de luminance es ^0.42 (en vez de
0.3, para que la diferencia con CRT cancele, y 0.42 en vez de 0.4 para
compensar un poco la diferencia de luz de hogar más oscura vs. luz de día o
estudio más fuerte).

Luma es el la weighted sum de r^0.42, g^0.42, b^0.42. rgb son lineales en la
intensidad (doble valor, doble intensidad), pero luma Y' no lo es. Hay que
elevar a la 2.2 para recuperar el valor de RGB que toman las cámaras.

El exponente 2.2 para convertir video R'G'B' en RGB se llama gamma, y el
proceso de aplicar el exponente es gamma correction. Como los factores no son
precisos a través de todos los dispositivos reales, van a ver que muchas veces
hay un proceso donde el usuario puede usar gamma correction.


## Codificación de colores

- RGB: simple para usar con CRTs y LCDs
- HSV y HLS: facilidad de uso
- Y'IQ: transmisión de señales de televisión
- CMY: impresión

Notas:

Hay varios sistemas comunes.

Técnicas de codificar color para cambiar de un dispositivo a otro, donde no
sólo hay coeficientes sino una descripción del modelo, incluyes los profiles
de ICC (International Color Consortium) y sRGB.

No todos los modelos se pueden convertir de uno a otro. Por ejemplo, CMY está
basado en tinta y papel bajo cierta luz, y no puede representar un blanco más
brillante que el del papel.


## RGB

<img src='images/rgb-cubo.png' height='440' />

Notas:

RGB - en CRT, corresponde a tres fósforos que brillan cuando les pega un haz
de electrones. Con el uso de HDTV, se fueron estandarizando los valores en
sRGB. sRGB propone una matriz para hacer un mapping entre ciertos colores
"estándar" de R, G, y B y su relación con las coordenadas CIE XYZ.


## CMYK

<img src='images/cmyk-separado.png' height='440' />


## Piepline video

- XYZ
- RGB
- R'G'B'
- Y'CbCr
- Subsampled Y'CbCr

Notas:

En video el pipeline de transformación suele ser XYZ -> RGB -> R'G'B' -> Y'CbCr -> subsampled Y'CbCr


## HSL y HSV

<img src='images/hsl-hsv.png' height='440' />

Notas:

HSV y HLS se utilizan mayormente como selección de colores, porque son cambios más intuitivos.

La interpolación está pobremente definida fuera de lo aritmético, porque la
percepción puede variar. ¿Cambia la intensidad siempre? ¿Pasa por blanco?
Según los valores que querramos cambiar, una representación pueder ser más
conveniente que otra.


## Preguntas
