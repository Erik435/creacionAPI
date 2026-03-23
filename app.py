#Tratamiento de datos..
#Grupo3
#Dev Erik Flores
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route('/')
def home():
    return {"mensaje": "API funcionando correctamente"}

if __name__ == '__main__': #Esta linea ejecuta la aplicacion cuando yo en terminal haga python app.py
    app.run(debug=True, host='0.0.0.0', port=8080)