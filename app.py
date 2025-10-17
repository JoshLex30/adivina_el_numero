#Bahena Praxedis Maria Adalid
#Estrada Romero Angeles
#Dario Emiliano 

#Importacion y conf basica
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta'