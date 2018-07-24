# Librerías: OpenGL, WebGL, Metal, DirectX 

Notas:
- ¿Qué hacen todas estas librerías?
- ¿Qué diferencia tienen?
- ¿Cómo uso una de ellos?


## OpenGL

- https://www.opengl.org/
- Especificacíon de 1992
- GLSL como lenguaje de programación
- Hoy manejado por Khronos
- Gran enfoque en extensiones
- OpenGL ES para dispositivos móbiles
- Seguido por Vulkan

Notas:
- mucho empuje de IHVs, Google y Mozilla
- mucho empuje de ciertas aplicaciones y juegos
- complementado por otros estándares
- tradicionalmente, mucha variación
- más estructurado en su última versión, mitad del compilador no existe
- versión restringida en OpenGL ES, por ejemplo Apple usa OpenGL ES 1.1


## OpenCL

- https://www.khronos.org/opencl/
- Especificación de 2009
- uso de aceleradores para cómputo
- no sólo GPUs, pero mayoritariamente GPUs
- C o C++ ('OpenCL C', 'C++ subset')
- Khronos

Notas:
- distinto lenguaje
- normalizando una representación intermedia
- problemas con representación de cosas que el hardware no hace o no hace bien


## WebGL

- https://www.khronos.org/webgl/
- Más reciente, 2011
- Basado en OpenGL ES 2 pero para web
- GLSL como lenguaje de programación
- Problemas de aislar y proteger tabs vs. procesos

Notas:
- shadertoy como repositorio de cosas interesantes
- pude hacer bolsa la máquina
- no esperen a que termine


## Metal

- De Apple: iOS, tvOS, macOS
- Estilo Vulkan/AMD Mantle/MS D3D12, mejor integrado
- Metal Shading Language, tipo C++

Notas:
- Exclusivo de Apple
- GPGPU y rendering
- Los frameworks de Apple lo usan mucho


## DirectX

- Exclusivo de Microsoft (excepto ports)
- D3D9, 10, 11, 12, similar a OpenGL/Vulkan
- No soporta extensiones de IHVs
- HLSL como lenguaje de programación 

Notas:
- Hay formas MS para soportar extensiones sólo para investigación y desarrollo
- Puede no ser una gran idea soportar extensiones por compatibilidad
- GPGPU y rendering


## Otros

- CUDA (NVidia)
- HSA (AMD y ARM)

Notas:
- NVidia ha tenido un gran éxito en compute
- Heterogeneous System Architecture, basado en encolar, no copias y schedule


## Ejercicio - WebGL

```html
<body onload="start()">
  <canvas id="glcanvas" width="640" height="480">
   Tu navegador parece no soportar el elemento HTML5 <code>&lt;canvas&gt;</code>.
  </canvas>
</body>

var gl; // Un variable global para el contexto WebGL
```

Notas:
- adaptado de https://developer.mozilla.org/es/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL
- elemento de canvas donde vamos a hacer rendering
- función start() para arrancar


## Ejercicio - WebGL

```javascript
function start() {
  var canvas = document.getElementById("glcanvas");

  gl = initWebGL(canvas);      // Inicializar el contexto GL
  
  // Solo continuar si WebGL esta disponible y trabajando
  
  if (gl) {
    gl.clearColor(0.0, 0.0, 0.0, 1.0); // negro opaco
    gl.enable(gl.DEPTH_TEST); // habilita profundidad
    gl.depthFunc(gl.LEQUAL);  // cercanos opacan lejanos
    // Limpiar el buffer de color asi como el de profundidad
    gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);
  }
}
```

Notas:
- inicializamos el contexto, lo vemos en un segundo
- lo primero que hacemos es seleccionar negro opaco de fondo
- la prueba de profundidad hace que los pixels mas cercanos opaquen los mas lejanos
- limpiamos los buffers de color (lo que mostramos) y profundidad


## Ejercicio - WebGL

```
function initWebGL(canvas) {
  gl = null;
  
  try {
    // Tratar de tomar el contexto estandar.
    // Si falla, retornar al experimental.
    gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
  }
  catch(e) {}
  
  // Si no hay contexto GL, chau pinela
  if (!gl) {
    alert("imposible inicializar WebGL");
    gl = null;
  }
  
  return gl;
}
```

Notas:
- browsers modernos soportan webgl, puede haber alguna version anterior que corra con experimental-webgl


## Ejercicio - WebGL

```glsl
  const vsSource = `
    attribute vec4 aVertexPosition;

    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;

    void main() {
      gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
    }
  `;

  const fsSource = `
    void main() {
      gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
    }
  `;
```

Notas:
- Nuestro primer shader!
- Ejemplo de shader de vertice y fragmento (vertice y pixel en HLSL)
- uniform indica que todos los vertices comparten la posicion
- attribute indica que es un dato asociado a un vertice
- gl_Position es una variable "magica"
- gl_FragColor es una variable magica tambien
- 1, 1, 1, 1 es RGBA para blanco opaco


## Ejercicio - WebGL

```javascript
function initShaderProgram(gl, vsSource, fsSource) {
  const vertexShader = loadShader(gl, gl.VERTEX_SHADER, vsSource);
  const fragmentShader = loadShader(gl, gl.FRAGMENT_SHADER, fsSource);

  // Crear el programa.
  const shaderProgram = gl.createProgram();
  gl.attachShader(shaderProgram, vertexShader);
  gl.attachShader(shaderProgram, fragmentShader);
  gl.linkProgram(shaderProgram);

  // Si falla, llorar y llorar, llorar y llorar ...
  if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
    alert('Unable to initialize the shader program: ' + gl.getProgramInfoLog(shaderProgram));
    return null;
  }

  return shaderProgram;
}
```

Notas:
- vamos a cargar el shader con una función auxiliar
- creamos un programa formado por dos shaders
- tomamos un parámetro del programa, en este caso si funcionó el link
- hay una tradición de no validar demasiado en llamadas de alta frecuencia, aunque no suele ser éste el caso


## Ejercicio - WebGL

```javascript
function loadShader(gl, type, source) {
  const shader = gl.createShader(type);

  // Send the source to the shader object
  gl.shaderSource(shader, source);

  // Compile the shader program
  gl.compileShader(shader);

  // See if it compiled successfully
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    alert('An error occurred compiling the shaders: ' + gl.getShaderInfoLog(shader));
    gl.deleteShader(shader);
    return null;
  }

  return shader;
}
```

Notas:
- el shader se compila de texto
- los shaders se enlazan (link) para formar un programa


## Ejercicio - WebGL

```javascript
const shaderProgram = initShaderProgram(gl, vsSource, fsSource);

const programInfo = {
  program: shaderProgram,
  attribLocations: {
    vertexPosition: gl.getAttribLocation(shaderProgram, 'aVertexPosition'),
  },
  uniformLocations: {
    projectionMatrix: gl.getUniformLocation(shaderProgram, 'uProjectionMatrix'),
    modelViewMatrix: gl.getUniformLocation(shaderProgram, 'uModelViewMatrix'),
  },
};
```

Notas:
- el programa y sus entradas forman la interfaz
- creamos un objeto para mantener referencias a los valores


## Ejercicio - WebGL

```javascript
function initBuffers(gl) {
  // buffer para un cuadrado
  const positionBuffer = gl.createBuffer();

  // a partir de este punto, las operaciones de
  // buffer se aplican a éste.
  gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);

  // coordenadas de puntos para el cuadrado.
  const positions = [
     1.0,  1.0,
    -1.0,  1.0,
     1.0, -1.0,
    -1.0, -1.0,
  ];

  // creamos un Float32Array a partir del array de JavaScript,
  // y lo usamos para inicializar el buffer
  gl.bufferData(gl.ARRAY_BUFFER,
                new Float32Array(positions),
                gl.STATIC_DRAW);

  return {
    position: positionBuffer,
  };
}
```

Notas:
- creamos un buffer donde ponemos los vertices y le agregamos datos


## Ejercicio - WebGL

```javascript
function drawScene(gl, programInfo, buffers) {
  // fondo negro, profundidad 1, test activo
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clearDepth(1.0);
  gl.enable(gl.DEPTH_TEST);
  gl.depthFunc(gl.LEQUAL);

  // limpiamos todo
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

  // matriz de perspectiva, 45 grados de campo de visión,
  // valores de clip cercano y lejano, aspect ratio del
  // elemento canvas
  const fieldOfView = 45 * Math.PI / 180;   // in radians
  const aspect = gl.canvas.clientWidth / gl.canvas.clientHeight;
  const zNear = 0.1;
  const zFar = 100.0;
  const projectionMatrix = mat4.create();

  // vamos a ver esto más adelante en el curso
  mat4.perspective(projectionMatrix,
                   fieldOfView,
                   aspect,
                   zNear,
                   zFar);

  // una matriz identidad en el centro
  const modelViewMatrix = mat4.create();

  // movemos un poco
  mat4.translate(modelViewMatrix,     // destino
                 modelViewMatrix,     // matriz a mover
                 [-0.0, 0.0, -6.0]);  // cantidad de movimiento

  // le decimos a WebGL cómo encontrar las posiciones del
  // buffer de posición para el atributo de vertexPosition
  {
    const numComponents = 2;  // 2 valores por iteración
    const type = gl.FLOAT;    // 32bit floats
    const normalize = false;  // sin normalizar
    const stride = 0;         // cuántos bytes moverse (0=calculado)
    const offset = 0;         // offset en el buffer
    gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
    gl.vertexAttribPointer(
        programInfo.attribLocations.vertexPosition,
        numComponents,
        type,
        normalize,
        stride,
        offset);
    gl.enableVertexAttribArray(
        programInfo.attribLocations.vertexPosition);
  }

  // a laburar
  {
    const offset = 0;
    const vertexCount = 4;
    gl.drawArrays(gl.TRIANGLE_STRIP, offset, vertexCount);
  }
}
```

Notas:
- dibujamos la escena final con una llamada a drawArray con los vertices
- https://mdn.github.io/webgl-examples/tutorial/sample2/


## Ejercicio - D3D11

- `ejemplos\d3d11`

Notas:
- primero vemos que hace el programa
- despues muestro los shaders
- despues vemos main y un nivel dentro de cada funcion
- hablar de vcpkg
- hacer debug graphics: in debug, event list, objects, input assembler, select pixel
 - View->Options->Graphics Diagnostics->Enable gather of GPU Disassembly.
 - ver las matrices de cbuffer


## Ejercicio - shadertoy

https://www.shadertoy.com/new

Notas:
- Panel de vista previa sobre la izquierda
 - render
 - tiempo
 - frames per second
- botones: grabar a .webm, activar VR, manejo de volumen, pantalla completa
- Con pantalla completa: normalmente permite evitar el compositor del sistema operativo.
- Sobre la derecha
 - entradas para el shader - uniform (constant buffers)
 - botones: compilar, cuenta de caracteres, pantalla completa, tamaño de letra, ayuda de glsl
- La ayuda de GLSL es bastante útil.

```
c:\work\sto\src\projects\impossible-channel\shader.glsl
pushd C:\work\sto\src
npm start
```

```
void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
  // Normalized pixel coordinates (from 0 to 1)
  vec2 uv = fragCoord/iResolution.xy;

  // Time varying pixel color
  vec3 col = 0.5 + 0.5*cos(iTime+uv.xyx+vec3(0,2,4));

  // Output to screen
  fragColor = vec4(col,1.0);
}
```

Descripción del programa:
- las coordenadas vienen en pixels
- sabemos cuál es la resolución final porque el programa lo informa
- parece redundante, pero hay varias configuraciones posibles (y comunes) para
  trabajar sólo con una proyección (view rectangle), y no siempre tiene sentido
  pensar en 'pantalla completa'
- el color tiene tres componentes: rojo, verde, azul; el cuarto es alpha que
  se agrega al final

Vamos a probar algunas variaciones sobre el programa
- alpha no importa a la hora de composición final - prueben cambiar a cero (bugbug en local?)
- vec3 col = uv.xyx; hace algo obvio - qué es? dónde está el negro? qué nos dice del sistema de coordenadas?
  en GL, el rincón de abajo a la izquierda es 0,0, y se incrementa hacia arriba a la derecha
- vec3 col = uv.xyx + vec3(0,2,4); - qué pasó con los colores donde nos excedimos de 1? por qué es horizontal la banda de colores?
  los canales de verde y azul están saturados; el eje vertical sólo se aplica al verde, con lo cual no hay
  diferencia, sólo x, que llega al blanco cuando llega a uno
- vec3 col = cos(uv.xyx + vec3(0,2,4)); - aplicando el coseno, ya no queda saturado; qué pasa cuando cambiamos
  el cero a uno, dos y tres? queda negro, por qué?
  la función se aplica por canal, y en la parte de la función donde el resultado es negativo (el codominio va
  de -1 a 1), el canal se apaga y queda en negro
- sumarle medio y cambiar el dominio por multiplicación a -0.5 a 0.5 nos deja la onda que queríamos, con
  los canales diferenciados
- para más variedad, sumamos el tiempo en un término donde no cambia el análisis 


## Preguntas de librerías

