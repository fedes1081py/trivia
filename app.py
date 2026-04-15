from pathlib import Path
import random
import json
import pandas as pd
import csv

ruta_historia = Path(__file__).resolve().parent / 'historial.csv'
ruta_preguntas = Path(__file__).resolve().parent / 'preguntas.json'





class Preguntas:
    #Esta clase solamente vamos a colocar la logica de las preguntas
