# Pipeline de gráficos: de triángulos a pixels

Notas:
- [D3D11 Graphics Pipeline](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476882(v=vs.85).aspx)
- [A trip through the Graphics Pipeline 2011: Index](https://fgiesen.wordpress.com/2011/07/09/a-trip-through-the-graphics-pipeline-2011-index/)


## De triángulos a pixels

<img src='images/d3d11-pipeline-stages.jpg' height='440' />


## Pipeline

- Input assembler: lee información
- Vertex shader: calcula atributos para cada vértice
- Rasterizer: proyecta geometría para calcular pixels
- Pixel shader: calcula atributos para cada pixel
- Output merger: escribe información


## Input Assembler

- Configurable, no programable
- Lee información, genera geometría ("primitives") si es necesario
- Genera índices
- Puede usarse para generar sólo índices, pero no es común
- Configuración consiste en buffer de vértices, índices, tipo de primitivos,
  y layout de datos

Notas:
- eficiencia en lectura
- structure of array vs array of structure


## Vertex Shader

- Trabaja de a un vértice por vez.
- Típicamente para aplicar transformaciones y deformarlo
- La aplicación de luz y o materiales por vértice
- Puede utilizar un índice de vértice y uno de instancia

Notas:
- ¿qué hace shadertoy con vértices?


## Rasterizer

- Convierte triángulos en pixels
- Trabaja con viewports, utilizado para ir de 3D a 2D
- Trabaja con scissor rectangles, utilizado para eliminar pixels
- Aplica perspectiva dividendo por z
- Otros atributos: pruebas de profundidad y ajustes de valores, multisampling


## Rasterizer

<img src='images/d3d10-rasterrulestriangle.png' height='440' />

Notas:
- Any pixel center which falls inside a triangle is drawn; a pixel is assumed to be inside if it passes the top-left rule.
- The top-left rule is that a pixel center is defined to lie inside of a triangle if it lies on the top edge or the left edge of a triangle.
- A top edge, is an edge that is exactly horizontal and is above the other edges.
- A left edge, is an edge that is not exactly horizontal and is on the left side of the triangle. A triangle can have one or two left edges.
- The top-left rule ensures that adjacent triangles are drawn once. 
- https://msdn.microsoft.com/en-us/library/windows/desktop/cc627092(v=vs.85).aspx


## Pixel Shader

- Trabaja de a un pixel por vez
- Importante: no toma dependencias en otros pixels para correr en paralelo
- Toma como entrada posición y atributos asociados a vértices, posiblemente interpolado
- Emite colores, profundidad (opcional, gana sobre valor interpolado)


## Output Merger

- Configurable, no programable
- Escribe el color correcto (y profundidad si está habilitado)
- Hace pruebas de profundidad
- Hace pruebas contra stencil


## Preguntas

