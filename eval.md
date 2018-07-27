-*- mode: markdown; coding: utf-8 -*-

# Inferencia


## Diferencias

- Entrenamiento vs inferencia
- Selección, datos disponibles, tiempo de cómputo, distribución, especificidad
- Latencia, mínimo aprendizaje, baja precisión, bajo poder
- Idea ya de sistemas expertos (fwd o back vs learn)

Notas:

Cuando tenemos un modelo de machine learning, normalmente distinguimos dos etapas bastante distintas: entrenamiento e inferencia.

Entrenamiento es la actividad que hacemos para armar un modelo, donde elegimos qué capas vamos a tener, qué tipo de operaciones realizar, y vamos entrenando el modelo con datos para ajustar los coeficientes y operaciones para que el modelo haga lo que queremos que haga.

Normalmente, este trabajo ocupa mucho tiempo, pueden ser horas o días de proceso distribuido para entrenar un modelo. Normalmente hay data scientists viendo cómo se desarrolla, y estudiamos el comportamiento del modelo.

Una vez que tenemos el modelo armado, vamos a hacerle preguntas 'en la vida real'. Por ejemplo, queremos tener una recomendación para un cliente, o estos tratando de reconocer una posición en el espacio para un dispositivo.

Si bien las herramientas no son necesariamente distintas (un toolkit de entrenamiento puede hacer una evaluación, y de hecho necesariamente tiene que hacerlo), muchos de los escenarios de inferencia son de casi-tiempo-real, y pueden estar corriendo en dispositivos con poco poder de procesamiento (por ejemplo, un parlante que reconozca 'hey alexa').

Utilizamos entonces herramientas y sistemas que están optimizados para minimizar recursos y latencia, muchas veces a costo de capacidades y precisión.

Existe la posibilidad de ajustar modelos en un engine de inferencia para continuar el aprendizaje, pero normalmente es algo limitado como ajustar ciertos coeficientes, pero no cambiar el grafo en sí.

Vale la pena mencionar que en arquitecturas de sistemas expoertos donde hay una base de datos de 'facts' con probabilidades y reglas, ya existía la idea de un motor de inferencia que trabajaba en 'forward chaining' (de facts a nuevos facts) o 'background chaining' (de una meta hacia los facts necesarios). 


## Escenarios 'edge'

- Reconocimiento de voz ('trigger').
- Reconocimiento de caras u ojos (tipo Windows Hello).
- Efectos gráficos de corrección de post-proceso.
- Reconocimiento de escritura a mano.
- Recomendaciones de gramática y estilo en Word.
- Reconocimiento de gente en fotos, asignación de etiquetas.

Notas:
- Algunos escenarios clásicos de inferencia 'on the edge' que pueden ver frecuentemente.
- Reconocimiento de voz (como mínimo, una frase 'trigger', tipo Alexa).
- Reconocimiento de caras u ojos (tipo Windows Hello).
- Efectos gráficos de corrección de post-proceso.
- Reconocimiento de escritura a mano.
- Recomendaciones de gramática y estilo en Word.
- Reconocimiento de gente en fotos, asignación de etiquetas.


## Alternativas

- Caffe2
- CoreML
- TensorFlow Lite
- Windows ML


## ONNX

- Formato de intercambio
- Microsoft, Facebook, Amazon
- Flujo de datos con operadores
- Los nodos son operadores, toman varios inputs, generan varios outputs

Notas:
- Más que nada con tensors, pero agregamos algunas cosas para ML clásico tipo diccionarios
- Hay entradas que pueden estar pre-inicializadas, donde ponemos los coeficientes


## ONNX

- Metadata: licencia, generador, autor
- Versiones de formato y operadores
- Librería en C++ y Python
- Protobuf

Notas:
- Ejemplo (inception): python c:\python37\scripts\netron C:\Users\marce\Downloads\model.onnx
- https://github.com/lutzroeder/Netron


## Windows ML - Arquitectura

- API para apps windows (C++/C#/JS)
- API para C++
- Formato de modelos, scheduling, execution
- Shaders para aceleración (meta ops?)

Notas:
- API para aplicaciones modernas
- API para C++, permite reutilizar buffers y da más control sobre memoria y ejecución
- 'Engine' que lee modelos, scheduling, execution
- Librería de shaders para muchos operadores
- Fundamentalmente, proceso de tensors (y, en la gran mayoría de los casos, 2D)
- Extensión en GPU para implementar algunos operadores
- ¿Por qué es necesario? Memoria!
- Integración con video para imágenes y proceso de cámara
- https://docs.microsoft.com/en-us/windows/uwp/machine-learning/integrate-model


## Windows ML - Uso

Notas:
https://docs.microsoft.com/en-us/windows/uwp/machine-learning/get-started

Walk-through de todas las partes

C:\work\wml\src>git clone https://github.com/Microsoft/Windows-Machine-Learning src

1. Open Get_Started
2. Walk through Helper.cs
3. Run and show window
4. Add MNIST.onnx to Assets.
5. Change Build Action to Content.
6. Show generated file.
7. Open ONNX in Netron:
https://www.lutzroeder.com/ai/netron/
https://github.com/lutzroeder/Netron/releases/latest

Instalacion de https://github.com/lutzroeder/Netron/releases/latest
Or just use https://lutzroeder.github.io/Netron/
8. Add variables to Page:
	    private MNISTModel ModelGen = new MNISTModel();
	    private MNISTModelInput ModelInput = new MNISTModelInput();
	    private MNISTModelOutput ModelOutput = new MNISTModelOutput();
9. Talk about Load / Bind / Eval
10. Add to LoadModel:
    StorageFile modelFile = await StorageFile.GetFileFromApplicationUriAsync(new Uri($"ms-appx:///Assets/MNIST.onnx"));
    ModelGen = await MNISTModel.CreateMNISTModel(modelFile);
11. Add to button click:

```C#
     ModelInput.Input3 = await helper.GetHandWrittenImage(inkGrid);
    //Evaluate the model
    ModelOutput = await ModelGen.EvaluateAsync(ModelInput);
            
    //Iterate through evaluation output to determine highest probability digit
    float maxProb = 0;
    int maxIndex = 0;
    for (int i = 0; i < 10; i++)
    {
        if (ModelOutput.Plus214_Output_0[i] > maxProb)
        {
            maxIndex = i;
            maxProb = ModelOutput.Plus214_Output_0[i];
        }
    }
    numberLabel.Text = maxIndex.ToString();
```
12. Add to clear.

```C#
    inkCanvas.InkPresenter.StrokeContainer.Clear();
    numberLabel.Text = "";
```

13. Corran y vean. Luego, ver probabilidades. Consideren como impacta el uso cuando hay ambiguedades!

```C#
            var q = ModelOutput.Plus214_Output_0
                .Select((val, idx) => new { digit = idx, prob = val })
                .OrderByDescending(item => item.prob)
                .Take(3)
                .Select(item => $"{item.digit}={item.prob/100}%");
            numberLabel.Text = String.Join(" ", q);
            numberLabel.FontSize = 8;
            numberLabel.TextWrapping = TextWrapping.Wrap;
```

14. Veamos como se estan consumiendo los recursos. Agregamos un timer, bool running, y levantamos GPU.

```C#
        private DispatcherTimer timer;
        private bool running;

        private void recognizeButton_Click(object sender, RoutedEventArgs e)
        {
            running = true;
            DoRun();
        }

        private async void DoRun()
        { 
            if (timer != null) { timer.Stop(); timer = null; }
            ModelInput.Input3 = await helper.GetHandWrittenImage(inkGrid);
            //Evaluate the model
            ModelOutput = await ModelGen.EvaluateAsync(ModelInput);

            //Iterate through evaluation output to determine highest probability digit
            var q = ModelOutput.Plus214_Output_0
                .Select((val, idx) => new { digit = idx, prob = val })
                .OrderByDescending(item => item.prob)
                .Take(3)
                .Select(item => $"{item.digit}={item.prob/100}%");
            numberLabel.Text = String.Join(" ", q);
            numberLabel.FontSize = 8;
            numberLabel.TextWrapping = TextWrapping.Wrap;
            if (running)
            {
                timer = new DispatcherTimer() { Interval = TimeSpan.FromMilliseconds(500) };
                timer.Tick += (_, __) => { DoRun(); };
                timer.Start();
            }
        }

        private void clearButton_Click(object sender, RoutedEventArgs e)
        {
            inkCanvas.InkPresenter.StrokeContainer.Clear();
            numberLabel.Text = "";
            running = false;
        }
```

Déjenlo corriendo, observen en task manager como empieza a usar (un poco) de GPU.

Consideren la arquitectura, drivers, extensiones.

Consideren qué pueden optimizar (lo que vimos en BLAS), y que no le damos acceso a todo el grafo entero.

## Preguntas
