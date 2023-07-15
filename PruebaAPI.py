#!/usr/bin/env python
# coding: utf-8

# # Caso de vuelo con retraso
# ###### Este corresponde a un vuelo de Latin American Wings, Nacional y en el mes de Octubre

# In[4]:


import requests
import json
import numpy as np

# URL de la API
url = 'http://127.0.0.1:5000/'

# Datos de entrada
input_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]  # Inserta tus datos aquí

# Crear el payload de la solicitud POST
payload = {'data': input_data}

# Realizar la solicitud POST
response = requests.post(url, json=payload)

# Verificar el código de respuesta de la API
if response.status_code == 200:
    try:
        # Analizar la respuesta en formato JSON
        json_response = response.json()
        prediction = json_response['prediction']

        # Imprimir la respuesta
        print('Respuesta:', json_response)
        print('Predicción:', prediction)
    except json.JSONDecodeError:
        print('Error al decodificar la respuesta en formato JSON:', response.text)
else:
    print('Error en la solicitud:', response.text)


# # Caso de vuelo sin retraso
# ###### Este corresponde a un vuelo de Aerolineas Argentinas , Internacional y en el mes de Diciembre

# In[5]:


import requests
import json
import numpy as np

# URL de la API
url = 'http://127.0.0.1:5000/'

# Datos de entrada
input_data = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]  # Inserta tus datos aquí

# Crear el payload de la solicitud POST
payload = {'data': input_data}

# Realizar la solicitud POST
response = requests.post(url, json=payload)

# Verificar el código de respuesta de la API
if response.status_code == 200:
    try:
        # Analizar la respuesta en formato JSON
        json_response = response.json()
        prediction = json_response['prediction']

        # Imprimir la respuesta
        print('Respuesta:', json_response)
        print('Predicción:', prediction)
    except json.JSONDecodeError:
        print('Error al decodificar la respuesta en formato JSON:', response.text)
else:
    print('Error en la solicitud:', response.text)


# In[ ]:




