-*- mode: markdown; coding: utf-8 -*-

# Machine Learning - Clasico y Deep Learning

http://www.deeplearningbook.org/


## ¿Qué es Machine Learning?

- Sistemas expertos
- Machine learning clásico (features a mano)
- Deep learning

Notas:

Buscamos software inteligente para asistir en una variedad de aplicaciones.

Fundamentalmente, un sistema de machine learning es uno en el que la computadora va a ir desarrollando o ajustando conocimiento a partir de casos de ejemplo - la computadora 'aprende' de estos casos.

Categorización básica

- Primero sistemas por reglas 'a mano', o sistemas expertos donde se explora (con asistencia) un espacio de problema.
- Clásico: input, features a mano, y luego un mapping aprendido de features a output.
- Deep learning: features simples son aprendidos, y la abstracción de estos features también es aprendida, además del mapping


## Ejemplos Clásicos

- Recomendaciones
- Spam

Notas:

Un par de modelos clásicos son el de logistic regression, que se puede usar por ejemplo para recomendar un tratamiento, y el de naive Bayes para encontrar spam.

http://www.deeplearningbook.org/
http://www.deeplearningbook.org/slides/01_intro.pdf


## Ejemplos Clásicos

<img src='images/ml-representaciones.png' height='440' />

Notas:

La performance de estos modelos dependen en gran parte de la representación. No es lo mismo encontrar patrones con coordenadas cartesianas que con coordenadas polares (ejemplo).

Supongamos un sistema que va a recomendar un tratamiento, y le hace preguntas a un médico sobre el paciente. Cada pregunta que hace a la representación del paciente es un 'feature'.

En el caso de regresión logística, aprendemos cómo estos features correlacionan con los resultados del tratamiento; sin embargo, no tienen influencia sobre qué features se utilizan ni cómo se representan.

Muchos problemas de inteligencia artifical se pueden resolver con este tipo de modelos.


## Deep learning

<img src='images/ml-auto.png' height='440' />

Notas:

En muchos otros problemas, sin embargo, es difícil saber qué features utilizar.

Por ejemplo, reconocer un auto en una foto es díficil - si queremos saber si tiene ruedas, reconocer ruedas a partir de pixels es diíficil porque puede tener sombras, estar tapado, estar en ángulo, etc.

Una solución a este problema es crear sistemas de representation learning, donde la representación en sí es aprendida; esto evita tener que pasar mucho tiempo haciendo reglas a mano (décadas de especialistas!) y permite que el sistema sea más flexible y evolucione.

El caso clásico es el de autoencoder, que es una combinación de encoder donde convertimos entradas a otra representación, con algunas características deseables, y un decoder que lo regresa al formato original. Por ejemplo, reconocer corners, o reconocer qué datos son noise y se pueden descartar.

La noción esencial de deep learning es que se pueden hacer representaciones en base a representaciones más simples para hacer algo útil (si el sub-problema es tan difícil como el problema original, no ayuda). El caso clásico es un 'multilayer perceptron', o feedforward deep network, donde hay varias funciones matemáticas que se componen.


## Capas (layers)

<img src='images/ml-capas.png' height='440' />

Notas:

En este caso, vemos hay una capa visible (visible layer) que son los pixels, que vemos directamente en los datos de entrada, y luego vamos a ir viendo una serie de capas ocultas (donde la información no está directamente en los datos), que van a encadenarse para entender representaciones más abstractas.

Podemos ver edges, y de ahí contornos y rincones, y partes de objetos a partir de contornos, y objetos enteros a partir de sus partes.

Parte de la representación no tiene que ver con los datos de entrada en sí, sino que puede ser información adicional que se genera para otras capas más adelante.


## Capas (layers)

- No hay definición de "deep" en "deep learning"
- Grafos de operaciones, de alto o bajo nivel
- Es, en general, "más deep que antes" (dos o tres capas de alto nivel)

Notas:

Ahora, ojo que no hay un única forma de medir profundidad (¿cuentan iteraciones? ¿cuentas operaciones básicas u operaciones compuestas?), y no hay una cantidad de capas para calificar 'deep' - son simplemente modelos más profundos de lo que se solía usar antes (muchas veces dos o tres capas de alto nivel).

Los modelos lineales de threshold sin embargo tienen limitaciones, como no poder descubrir XOR (no hay un factor que ajuste linealmente estos valores).


## Hmmm... datos ...

<img src='images/ml-crecimiento.png' height='440' />

Notas:

Uno de los cambios más influyentes es que los tamaños de datasets van aumentando dramáticamente con el tiempo. Empezando con miles de datos, a milliones, a decenas o cientos de millones, a miles de millones.

La 'rule of thumb' es que con 5000 ejemplos por categoría podemos tener resultados aceptables en un algoritmo supervisado, y podemos exceder la performance de humanos con 10 millones de ejemplos.


## Hmmm... datos ... también ...

- Más velocidad de CPUs, redes
- Infraestructura de distribución
- Más atención al software, facilidad de uso, experimentación

Notas:

Otro cambio es el tamaño de los modelos. Acá es donde entran a jugar los GPUs, así como mejor velocidad de CPUs, de redes, e infrastructura para computación distribuida.

Finalmente, hay mucha más atención en el software, con varios toolkits utilizados en research que facilitan y aceleración la experimentación.


## Breve historia

- Cybernetic (40-60)
- Connectionism (80-90)
- Neural networks (hoy)
- Ojo con el nombre
- SGD ('43)

Notas:

Deep learning en sí es lo que se solía llamar 'cybernetics' en los 40-60, y 'connectionism' en los 80-90 (con una o dos capas ocultas). Hoy hablamos de 'neural networks', pero mucho de esto existía antes.

Los modelos de neuronas existen desde hace mucho, no porque puedan aproximar el comportamiento del cerebro humano, sino porque el cerebro es prueba de que podemos tener comportamiento sofisticado a partir de conexiones más básicas.

Una de las técnicas más viejas de adaptación es la de stochastic gradient descent, usada en una variante en 1943, y todavía utilizada hoy. Los modelos lineales de funciones de entonces todavía se utilizan hoy (aunque las técnicas de entrenamiento son distintas).


## Aplicaciones - Escalas

- Conectividad
- Tamaño y redes de recursos
- Implementación importa (fijo, caché)
- Performance mueve la aguja en otras dimensiones

Notas:

El principio es la conectividad - una neurona biológica o un feature no es inteligente, pero una población de neuronas exhibe comportamiento inteligente. Pero la población tiene que ser grande.

El tamaño de información y neuronas en el sistema es lo que requiere implementaciones especializadas de software y hardware.

Los primeros modelos se entrenaban en una única CPU. Hoy es insuficiente, lo que se usan son GPUs o varios CPUs en red (o varios GPUs en red).

A veces impacta la implementación. Por ejemplo, hay versiones de software para CPU que se especializan corriendo en aritmética de punto fijo; depende de las características de CPU cómo armamos la representación de datos y redes.

Hay estrategias de optimizar para el tamaño de datos para que tenga mejor utilización de caché, por ejemplo.

No es sólo cuestión de performance por satisfacción - con una implementación más rápida, se pueden utilizar modelos más grandes con mejores resultados, o realizar más iteraciones e investigaciones.


## Organización de datos en GPU

- Buffers (parámetros, activación, gradiente, memoria)
- Operaciones sencillas
- Inicios: renderar un quad en lugar de matriz

Notas:

Las redes neuronales normalmente van a tener muchos buffers con parámetros, valores de activación, valores de gradiente, memoria, de gran tamaño.

Las neuronas en sí son bastante simples y no requieren demasiada sofistifación, y normalmente actúan de forma independiente, con lo cual se ajustan muy bien a GPU.

Para dar una idea de líneas de tiempo, tipo 2005 había implementaciones usando GPUs con pipelines de gráficos, y más cerca de 2009 se adopta como compute only (DirectCompute es del 2009 más o menos).


## Cambios de enfoque en GPU

- Más atado al hardware
- Más comunicación warp-level (`WaveActiveAllSum`, `WavePrefixAllSum`, `WaveIsFirstLane`)
- Más encapsulado desde afuera: Theano, cuda-convnet

Notas:

Suele ser menos heterogéneo el tipo de GPUs en uso, con lo cual van a ver más cosas especializadas, incluyendo técnicas, librerías, stack.

Algo que se usa mucho, por ejemplo, es el uso de warp-level o wave-level programming, donde cada thread habla con otros en sincronía, se pasan datos en registros, o eligen un único representante para que haga trabajo (por ejemplo, reservar espacio y asignar valores para hacer una escritura "coalesced"). Normalmente oculto por portabilidad.

Hay frameworks que aparecen para tratar de evitar que el usuario tenga que saber usar GPUs, por ejemplo Pylearn2 usa Theano y cuda-convnet para sus operaciones, y esas librerías hacen la aceleración.


## Distribución de datos

- Distribución de ejecución de inferencia (según el tipo)
- Distribución de modelo (por partes, también para entrenamiento)
- Minibatches, secuencialidad de gradients

Notas:

Para trabajar en redes con modelos a gran escala, hay dos enfoques.

- Distribuir inferencia. Es más fácil, porque cada inferencia en sí se puede distribuir según el caso - paralelismo de datos.
- Distribuir el modelo. En este caso una máquina corre ciertas partes y otra máquina corre otras. Sirve para inferencia y entrenamiento.

Distribuir entrenamiento es más difícil; se pueden usar minibatches más grandes en cada SGD pero la mejor es sub-lineal. Sería mejor distribuir los gradient descents, pero son secuenciales.


## Distribución de datos

- Asynchronous stochastic gradient descent 
- Sobreescribe, pero gana en performance

Notas:

Una solución al problema de secuencialidad de pasos de gradient es 'asynchronous stochastic gradient descent', donde varios cores comparten parámetro, calculan el gradient, e incrementan el parámetro sin locks; algunos gradients se sobreescriben, pero la velocidad hace que se aprenda más rápido.


## Adaptación de datos

- Compresión de modelos
- Entrenamiento con mejores models

Notas:

Normalmente la inferencia tiene que ser pequeña y rápida, porque puede correr en cualquier lado, un celular o incluso un Raspbery Pi. Para poder realizar esto, podemos comprimir el modelo, reemplazando el modelo original por uno que requiera menos memoria y poder de cómputo.

Muchas veces el modelo es más grande porque aprende a reconocer distintos casos con un número limitado de ejemplos. Pero podemos utilizar el modelo generado como referencia y entrenar un modelo que aprenda a devolver los mismos resultados, generado entradas aleatorias (idealmente con una distribución similar a los originales).


## Estructura dinámica

- Buscar particionar partes del modelo, evitar trabajo
- Dentro del modelo, o a mano - jerarquía de clasificadores

Notas:

Otra idea para mejorar la performance es utilizar estructuras dinámicas, donde hay partes disjuntas en modelos, y no todas van a utilizar la misma información. Si determinamos de antemano que una entrada no va a necesitar cierta información, podemos evitar generarla.

Por ejemplo, una estrategia es tener una "cascada" de clasificadores. Primero detectamos un objeto o evento poco frecuente, después utilizamos un clasificador más sofisticado (y caro) para analizarlo. Pero como el caso es raro, la versión sofisticada no se dispara seguido; el primer clasificador es rápido, el segundo preciso.

Por ejemplo, Street View en Google corre dos clasificadores para leer la altura de la calle: uno para encontrar las letras, otro para transcribirlas.


## Estructura dinámica - ojo

- Inconsistencia de performance
- Side-channel disclosure
- Falta de coherencia
- Ojo con load-balancing

Notas:

Consideren si necesitan smooth framerate o si es un one-shot operation (o si es offline processing), consideren el impacto en percepcion en el primer caso. Relacionen con el caso de side-channel attacks como otro caso interesante de variaciones en tiempo de proceso que importan.

Los árboles de decisiones son ejemplos de estructuras dinámicas.

El problema de estructuras dinámicas es que cuando las decisiones están embebidas en las operaciones, ya no se pueden describir como simple álgebra de matrices; CPU pierden coherencia en cache, y GPU pierde coherencia de ejecución y memoria.

Ojo con particionar modelos por máquinas para evitar esto, porque ahora el trabajo de distribución va a empezar a reflejar la distribución de la población, con lo cual es común que algunas máquinas tengan mucha más carga y otras muy poca.


## Otro hardware especializado

- ASICs
- FPGA
- CV, sensores de movimiento

Notas:

ASICs: application-specific integrated circuits. Algunos pueden operar con señales analógicas también, donde el voltaje representa valores.

FPGA: field programmable gate array (más flexibles que ASICs, pueden reescribirse). Microsoft ahora tiene un proyecto, Catapult, para usar FPGA en el cloud (Bing lo usaba de antes).

Normalmente la inferencia puede correr con precisión muy baja, con lo cual hay cosas raras como valores de 4 o 2 bits. Pero 8 y 16 bits de precisión ya son más comunes, sobre todo 16 (8 pronto, pero es menos uniforme).


## Computer Vision

- Muchos benchmarks
- Reproducir (en general) habilidades humanas
- Reconocer: caras, objetos, categorías, bounding boxes, describir, transcribir

Notas:

CV es un áreas clásica para deep learning; muchos de los benchmarks son de reconocimiento de objetos o de caracteres. La mayoría (aunque no todas) las aplicaciones intentan reproducir habilidades humanas, como reconocer caras o categorizar objetos. Las tareas clásicas son reconocer algo, describir dónde está en la foto con un bounding box, transcribir información, y etiquetar la imagen con información del objeto reconocido (persona, tipo de objeto, características).

Hay relativamente poco preprocesamiento en imágenes - la idea es trabajar con la imagen más o menos como aparece. Normalmente las redimensionamos para que tengan más o menos el mismo tamaño, aunque algunos modelos se encargan de aceptar entradas de tamaño variable.


## Computer Vision

- Dataset augmentation
- Ojo con preprocesos que quite variación para generalizar (no se cancelen!)
- Va quedando fuera de moda el preprocesamiento clásico

Notas:

Una de las técnicas que se usa es 'dataset augmentation', donde la misma imagen aparece varias veces, por ejemplo con distinta área de crop o distinto foco, o flippeada horizontalmente, o con ruido, o con los colores corridos en tono, que puede usarse para entrenar o testear.

A veces hay preprocesamiento para quitar variación, para que haya modelos más simples, con la idea de que generalicen más.

Por ejemplo, una de las cosas para eliminar variación de forma segura es el contraste. El contraste es la diferencia entre las áreas o pixels claros y oscuros de una imagen.


## Computer Vision - Equalización

<img src='images/ml-histograma-1.jpg' height='440' />

Notas:

- Fotos del tutorial de OpenCV de [equalización de histogramas](https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/histogram_equalization/histogram_equalization.html)
- Foto original


## Computer Vision - Equalización

<img src='images/ml-histograma-2.jpg' height='440' />

Notas:

- Histograma de foto original


## Computer Vision - Equalización

<img src='images/ml-histograma-4.jpg' height='440' />

Notas:

- La idea es transformalo en éste histograma, con mejor utilización del espectro (y hacerlo consistente con todas las fotos, para evitar variaciones de contraste a la hora de aprender).


## Computer Vision - Equalización

<img src='images/ml-histograma-3.jpg' height='440' />

Notas:
Ojo que en el ejemplo estamos aumentando el contraste, pero en la referencia van a encontrar funciones para crear el histograma, ajustarlo por un factor, y aplicar el histograma a la imagen.


## Computer Vision - Proceso Local

- Contraste global vs. contraste local
- Local Contrast Normalizacion (LCN) para border

Notas:

Hay dos formas de normalización de contraste - una es global y otra local. En la global, buscamos que el contraste tenga cierto parámetro a través de toda la imagen, con lo cual las áreas oscuras van a ser distinguidas de las claras, pero no necesariamente se van a notar los bordes.

En el caso de normalización de contraste local, cada pixel se modifica según la media y desviación estándar de los pixels cercanos (o con otro tipo de distribuciones o coeficientes), normalmente con una convolución para encontrar las medias y desviaciones locales y después haciendo la resta y división por elemento.

En ambos casos, pero sobre todo en el local, hay que tener cuidado cuando no hay ninguna desviación para evitar divisiones por cero.

Local Contrast Normalization, LCN, se puede utilizar para detectar edges.


## Computer Vision - Canny Edge Detection

<img src='images/ml-canny.jpg' height='440' />

Notas:
- Los bordes son muy útiles para reconocer cosas.


## Computer Vision - Canny Edge Detection

1. Blur para reducir el ruido
2. Filtro para gradientes x 3
3. Quitar pixels que no sean máximos locales en dirección gradiente
4. Conexión según parámetros de max y min

Notas:

También: https://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html Canny Edge detection.

Blur para quitar noise, filtro para buscar gradients horizontales, verticales y en diagonales, quitar pixels que no sean local maxima en la dirección del gradient (es decir, te queda el borde 'finito), y finalmente conexión - hay un máximo y mínimo que determina si un pixel es un edge (sobre máx), no lo es (bajo min), o tal vez(entre min y max); los 'tal vez' se determinan si están conectado a un píxel que 'seguro' es.


## Reconocimiento de voz

- Señal acústica a secuencia de palabras
- Features base: 20ms
- ¿Cuál es la secuencia linguística más probable?

Notas:

La tarea en reconocimiento de voz es mapear una señal acústica con una frase en lenguaje natural a una secuencia de palabras que una persona quiso decir.

Tradicionalmente, dividimos la secuencia de entrada en 20ms en X; en algunos sistemas, los features se reconocen a mano, pero en varios de deep learning los features los aprende el sistema.

El reconocimiento (ASR) consiste de crear una función que mapee X a la secuencia linguística de y más probable.


## Reconocimiento de voz

- Chau HMM y GMM, hola LSTM
- Long short-term memory (con memoria, a diferencia de feedforward, para RNNs)

Notas:

Los modelos de 1980 hasta más o menos el 2010 usaban Hidden Markov Models (HMMs) y Gaussian Mixture Models (GMMs). GMMs modelas la asociación entre features de acústica y fonemas, y HMMs modela la secuencia de fonemas.

El corpus clásica para reconocimiento de voz es TIMIT (es en inglés, así que ojo por el tipo de features que necesitan). Juego el rol de MNIST para reconocimiento - es decir, bueno para benchmark y papers.

Después con la disponibilidad de muchos más datos se pasa a redes neuronales.

Luego se agregan extensiones como features que se adaptan al interlocutor, y luegos expandir de reconocmiento de fonemas a reconocimiento de gran-vocabulario, donde no se reconocen sólo fonemas sino secuencias de palabras en un gran vocabulario.

Otro cambio fue la representación de entradas no como una dimensión, sino como arrays de dos dimensiones como si fueran imágenes (donde las filas son el tiempo y las columnas frecuencia), utilizados con redes convolucionales.

Finalmente (por ahora) hay uso de deep long short-term memory RNNs, con un error del 17.7%.


## Proceso de lenguaje natural

- Lenguajes humanos no computadoras
- Distribución de probabilidad en secuencias palabras
- Muchas dimensiones en un espacio discreto muy 'sparse'

Notas:

Natural Language Processing (NLP) es el uso de lenguajes humanos (en vez de lenguajes de computadora), ambiguos y sin buena descripción. Se utiliza por ejemplo para hacer resúmenes o traducciones. Muchos de los NLP se basan en modelos de lenguaje que definen una distribución de probabilidad en secuencias de palabras (o caracteres).

El reto en este caso es que para tener buenos resultados modelamos palabras, que tienen un espacio secuencial muy grande, con lo cual tenemos muchas dimensiones en un espacio discreto muy 'sparse'.


## n-grams

- Secuencias fijas de 'n' tokens
- Probabilidad de siguiente dada probabilidad n-1 tokens

Notas:
Los primeros modelos utilizaban n-grams, secuencias fijas de 'n' tokens (donde un token puede ser una palabra, caracter o incluso byte). Los modelos definen la probabilidad condicional del token 'n' dado los n-1 tokens.

$ P(x_1,...,x_tau) = P(x_1,...,x_(n-1)) prod _(t=n) ^tau P(x_t|x_(t-n+1),...,x_(t-1)) $

Los valores de n pequeños se llaman unigram, bigram, trigram.


## n-grams

- Información muy local
- Smoothing, categorías, backoff

Notas:
El problema con estos modelos es que la información es muy local.

Es muy común que una frase particular no aparezca en el corpus y no tengamos una probabilidad para ella, entonces hay que empezar a compensar con eso, con algún tipo de smoothing donde todo tiene alguna probabilidad mínima por ejemplo.

No hay información sobre relación, aunque hay class-based language models donde se intenta hacer eso, pero entonces se pierde mucha información en la representación (por ejemplo, si puedo decir 'mi camisa es roja', entender 'roja' como un color). Hay modelos que intentan combinar ambos con back-off (cuando hay algo nuevo al corpus, como 'mi camisa es linda' o 'mi camisa es prestada', o 'mi camisa es de la seleccion del 86').


## Neural Language Models

- Problema de dimensionalidad
- Dos palabras son similares pero distintas
- "Word embedding"
- Representación - hot vector

Notas:
Neural Language Models (NLMs) son modelos que intentan solucionar el problema de dimensionalidad, con la capacidad de ver que dos palabras son similares sin perder noción de que son distintas. Cada palabras y su contexto comparte su fuerza estadística con otras palabras y contextos similares.

Estos modelos a veces se refieren como 'word embedding', donde cada palabra es un punto en un espacio de dimensiones iguales al tamaño del vocabulario (donde es un 'hot vector'), y la representación de palabras los pone en un feature space de menores dimensiones, donde las palabras que suelen aparecer en el mismo contexto están más cercanas. En un mundo discreto, no hay distancias!


## Aplicaciones de lenguages

- Reconocimiento de caracteres (OCR).
- Reconocimiento de escritura a mano.
- Traducción.
- Corrección ortográfica.
- Sugerencias gramáticas.
- Generar títulos de imágenes.
- Generar resúmenes.

