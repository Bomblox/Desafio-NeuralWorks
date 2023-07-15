#!/usr/bin/env python
# coding: utf-8

# ### 3. Serializa el modelo seleccionado (puede ser de los construidos en el punto 2) e implementa una API REST para poder predecir atrasos de nuevos vuelos.
# 

# ###### Dato: en la creacion del modelo de XGBoost la variable a predecir "labels_" está vacía por lo que se solucionó esto

# ###### Se serealizó el modelo de XGBoost después del GridCV. Utilicé Flask para implementar tu modelo y crear una API porque Flask es un framework ligero y fácil de usar para el desarrollo de aplicaciones web en Python

# In[1]:


from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo desde el archivo .pkl
modelo = joblib.load('XGBoost_GridCV.pkl')

@app.route('/', methods=['POST'])
def predict():
    # Obtener los datos de entrada
    data = request.json

    # Realizar la predicción
    prediction = modelo.predict(np.array(data['data']).reshape(1, -1))

    # Devolver la predicción como respuesta en formato JSON
    response = {'prediction': prediction.tolist()}

    return jsonify(response)

if __name__ == '__main__':
    app.run()


# ###### Este código crea una API REST utilizando Flask que carga un modelo de aprendizaje automático desde un archivo .pkl y realiza predicciones en función de los datos de entrada enviados a través de solicitudes POST a la ruta raíz ("/"). La predicción se devuelve en formato JSON. Al ejecutarlo se inicia la instancia y se dejó otro archivo PruebaAPI.ipynb donde ejecutando la request se puede utilizar la API.
