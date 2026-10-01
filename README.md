# Apuntes de Ciencia de Datos y Redes Neuronales

Repositorio desarrollado como parte de la asignatura de **Ciencia de Datos**, en el cual se recopilan diferentes ejercicios, prácticas y talleres relacionados con aprendizaje automático y redes neuronales utilizando Python.

## Contenido del repositorio

### Perceptrón

La carpeta `Perceptron` contiene prácticas introductorias sobre redes neuronales y clasificación, incluyendo:

- Implementación y funcionamiento básico de un perceptrón.
- Clasificación mediante `Perceptron` de Scikit-learn.
- Ejercicios de clasificación utilizando edad y colesterol.
- Uso de redes neuronales multicapa (`MLPClassifier`).
- Clasificación de datos no lineales mediante círculos concéntricos.
- Introducción a TensorFlow y Keras.
- Almacenamiento de modelos entrenados mediante `joblib`.

### Redes densas

La carpeta `Redes densas` contiene ejercicios orientados a la construcción y entrenamiento de redes neuronales utilizando TensorFlow y Keras.

Entre los temas trabajados se encuentran:

- Configuración de TensorFlow y Keras.
- Verificación del uso de GPU.
- Funciones de activación.
- Funciones de pérdida.
- Redes neuronales secuenciales.
- Regresión con redes neuronales.
- Redes densas para clasificación.
- Preprocesamiento y normalización de datos.
- Entrenamiento y almacenamiento de modelos.
- Ejercicios con datasets como Auto MPG.

### Taller

La carpeta `taller` contiene una aplicación sencilla de predicción de riesgo cardíaco a partir de dos variables:

- Edad.
- Nivel de colesterol.

El proceso incluye:

1. Lectura y limpieza de los datos.
2. Eliminación de valores nulos y datos fuera de los rangos establecidos.
3. Estandarización de las variables mediante `StandardScaler`.
4. Generación de datos procesados en formato JSON.
5. Visualización mediante gráficos de dispersión.
6. Uso de una red neuronal para realizar la clasificación.
7. Desarrollo de una interfaz web mediante Streamlit.

La aplicación permite ingresar la edad y el nivel de colesterol de una persona y visualizar el resultado producido por el modelo.

## Estructura

```text
.
├── Perceptron/
│   ├── Avanzada_Cuaderno_1_ANN_El_Perceptron.ipynb
│   ├── Cuanderno_1_1_Perceptron_con_Sklearn_ipynb (1).ipynb
│   ├── Avanzada_Cuaderno_2_ANN_Red_Neuronal_sklearn_keras_tensorflow.ipynb
│   ├── mlp circulos jupyter.ipynb
│   └── modelo_circulos.pkl
│
├── Redes densas/
│   ├── Avanzada_Cuaderno_3_ANN_Red_neuronal_básica_de_regresion_lineal_Ejemplo.ipynb
│   ├── Avanzada_Cuaderno_4_ANN_Red_Neuronal_Clasificación_(Redes_densas).ipynb
│   ├── configuración de una reed neuronal.ipynb
│   ├── cuaderno 5.ipynb
│   └── modeloGasolina.keras
│
├── taller/
│   ├── app.py
│   ├── procesamiento.py
│   ├── pacientes.csv
│   ├── datos_procesados.json
│   ├── grafico_dispersion.png
│   ├── modelo_estandarizacion.joblib
│   └── requirements.txt
│
└── imagenes/
```

## Tecnologías utilizadas

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- TensorFlow
- Keras
- Streamlit
- Joblib

## Ejecutar el taller

Para ejecutar la aplicación de Streamlit:

```bash
cd taller
pip install -r requirements.txt
streamlit run app.py
```

Luego Streamlit mostrará en la terminal la dirección local desde la cual se puede abrir la aplicación en el navegador.

## Objetivo

El objetivo de este repositorio es reunir las prácticas realizadas durante el curso y documentar el proceso de aprendizaje desde modelos sencillos como el perceptrón hasta redes neuronales densas y pequeñas aplicaciones de clasificación.

Los ejercicios permiten practicar conceptos como preparación de datos, entrenamiento de modelos, clasificación, regresión, evaluación y despliegue básico de modelos mediante una interfaz web.

## Nota

Este repositorio tiene fines exclusivamente académicos y los modelos desarrollados corresponden a ejercicios de aprendizaje. La aplicación relacionada con riesgo cardíaco no constituye una herramienta de diagnóstico médico.
