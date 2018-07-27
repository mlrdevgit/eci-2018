-*- mode: markdown; coding: utf-8 -*-

# Machine Learning Frameworks


## Generalidades

- ¿Quién soporta?
- ¿Uso activo?
- ¿Qué dispositivos soporta?
- ¿Qué lenguajes soporta?
- ¿Cómo distribuye?
- Zoológico de modelos (modelo zoo)

Notas:
Algunos parámetros para considerar:

- ¿Quién soporta el framework? Afecta con qué está integrado.
- ¿Popularidad? Afecta disponibilidad de recursos y gente.
- ¿Dispositivos soportados? Afecta dónde puede correr. ¡Ojo con vendors!
- ¿Lenguajes? Python y C++ y no demasiado más a la hora de entrenar.
- Model zoo - modelos ya entrenados.
- Distribución - MPI, Spark


## Caffe

- Berkeley
- Buenos tutoriales y walk-throughs
- Layers (operators), blobs (tensors), nets (flows), forward/backward passes (inputs a outputs o dados outputs calcular gradients)
- Protobuf
- http://caffe.berkeleyvision.org/

Notas:
- http://caffe.berkeleyvision.org/tutorial/layers.html


## Caffe2

- Facebook
- Operators en lugar de layers, un poco más fácil de extender
- Intención es darle más bola a mobile
- Sparse tensors
- protobuf, ONNX

Notas:
- https://caffe2.ai/docs/operators.html


## Caffe2 (layers vs operators)

<img src='images/caffe2-operators-comparison.png' height='440' />


## Cognitive Toolkit (CTNK)

- Microsoft
- Python, C#, C++
- Menos popular, buena performance (CUDA reciente), ONNX


## Keras

- Google
- Front-end para TensorFlow, CNTK, Theanos, usabilidad
- Python
- Keras.js

Notas:
https://transcranial.github.io/keras-js/#/mnist-cnn


## MXNet

- Amazon (Apache)
- Bien soportado por AWS (incluyendo Lambda y containers), buen soporte de distribucion
- ONNX


## CoreML

- Apple
- iOS & macOS
- Metal y Accelerate y BNNS (basic neural network subroutines)
- Integracion con otros frameworks: Vision, natural language (idiomas, lugares, sustantivos, etc)
- Herramientas de Python para conversion de modelos (algo de training local, tambien)

Notas:
- Modelos clásicos de scikit-learn, caffe y keras para neural networks
- tensorflow y mxnet, 3rd party


## CoreML

<img src='images/frameworks-coremltrain.png' height='440' />

Notas:
- Nota de color: hay un playground para cargar en XCode con una UI del trainer
- https://developer.apple.com/documentation/create_ml/creating_an_image_classifier_model


## Scikit-Learn

- scikit-learn
- scipy
- numpy
- matplotlib
- pandas

Notas:
- Stack clásico de Python
- scikit-learn: classification, regression, clustering, etc.
- scipy: optimization, linear algebra, integration, interpolation, FFT, signal processing, etc.
- numpy: homogeneous arrays and operations
- matplotlib: plots for image, contour, scatter, line, 3D
- pandas: numerical tables and data series, data set merge/slice/fill-in, etc.
- Typical flow: use pandas
- http://scikit-learn.org/


## Scikit-Learn

<img src='images/frameworks-scikit-learn.png' height='440' />


## SparkML

- Apache (Berkeley originalmente)
- Spark Core - distribución de tareas y comunicación
- MLlib - par de formatos, evolucionando

Notas:
https://spark.apache.org/docs/2.1.1/ml-pipeline.html


## TensorFlow

- Google
- Training, inferencia, distribución, ejecución
- TensorFlow lite para inferencia, mobile, .js para browsers


## Otras Herramientas

- Python: por supuesto
- IPython
- Jupyter Notebooks
- Librerías de base
- Otro hardware

Notas:
- Python: por supuesto
- IPython: interactive Python, eventualmente notebooks
- Jupyter Notebooks: server, mezcla editor con código y visualizaciones, hosteado o local
- Librerías de base: cuBlas, cuDNN, clBlas, clDNN, MKL (Math Kernel Library, Intel)
- Otro hardware: FPGA (Bing), ASIC (Google TPU), DSP (QC Hexagon), GPU (NVidia Tesla)
