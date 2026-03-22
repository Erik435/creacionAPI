#Tratamiento de datos
#Grupo3
#Dev Erik Flores
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

