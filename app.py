from pathlib import Path
import random
import json
import pandas as pd
import csv

ruta_historial = Path(__file__).resolve().parent / 'historial.csv'
ruta_preguntas = Path(__file__).resolve().parent / 'preguntas.json'





class Preguntas:
    #Esta clase solamente vamos a colocar la logica de las preguntas
    def __init__(self,ruta_preguntas):
        self.preguntas = self.cargar(ruta_preguntas)
    def cargar(self,ruta):
        if not ruta.exists():
            return {}
        with open(ruta,'r') as file:
            return json.load(file)

    def obtener_tematicas(self):
        if not self.preguntas:
            return {}
        return self.preguntas.keys()

    def generar_preguntas_random(self, tematica):
        #vamos a generar las preguntas random
        if not tematica.strip():
            return []
        preguntas_random = random.sample(self.preguntas[tematica],k=5)
        return preguntas_random


class Juego:
    def __init__(self,ruta_preguntas):
        self.puntaje = 0
        self.correctas = 0
        self.incorrectas = 0
        self.usuario = ""
        self.preguntas = Preguntas(ruta_preguntas)
    
    @property
    def puntaje(self):
        return self._puntaje
    
    @puntaje.setter
    def puntaje(self,puntaje):
        if puntaje<0:
            print("Error")
        else:
            self._puntaje = puntaje

    
    def imprimir_tematicas(self,tematicas):
        for tematica in tematicas:
            print(f"-) {tematica}")
    
    def pedir_tematica(self,tematicas):
        while True:
            self.imprimir_tematicas(tematicas)
            op = input("Decime la tematica que quieres: ").strip().capitalize()
            if op in tematicas:
                return op
            print("Dato invalido, intenta de vuelta")
                
    
    def validar_ayuda(self):
        while True:
            op = input("Necesitas ayuda: ").lower()
            if not op in ('si','no'):
                print("Dato invalido, intenta de vuelta")
                continue
            return True if op == 'si' else False

    def mostrar_opciones(self,opciones):
        print("Las opciones son: ")
        for opcion in opciones:
            print(f"-){opcion}")

    def validar_respuesta(self,respuesta_correcta):
        while True:
            respuesta = input("Decime la respuesta: ")
            if respuesta.strip():
                return respuesta.lower() == respuesta_correcta.lower()
            print("Dato invalido")
    
    def validar_nombre(self):
        while True:
            op = input("Decime el nombre del usuario: ")
            if op.strip():
                return op
            print("Dato invalido,intenta de vuelta")
    
    def empezar(self):
        self.usuario = self.validar_nombre()
        while True:
            tematicas = self.preguntas.obtener_tematicas()
            tematica_elegida = self.pedir_tematica(tematicas)
            preguntas_tematica = self.preguntas.generar_preguntas_random(tematica_elegida)

            for pregunta_completa in preguntas_tematica:
                pregunta = pregunta_completa['pregunta']
                respuesta = pregunta_completa['respuesta']
                print(pregunta)
                ayuda = self.validar_ayuda()
                if ayuda:
                    opciones = pregunta_completa['opciones']
                    self.mostrar_opciones(opciones)
                es_correcta = self.validar_respuesta(respuesta)
                self.calcular_puntaje(es_correcta, ayuda)
            seguir_jugando = self.seguir()
            if not seguir_jugando:
                print("Adios ")
                break
            
    def seguir(self):
        while True:
            op = input("Queres seguir? ").strip().lower()
            if op in ('si','no'):
                return True if op == 'si' else False
            print("Intenta de vuelta, dato invalido")




    def calcular_puntaje(self,respuesta_correcta, ayuda):
        if respuesta_correcta:
            self.puntaje+=5
            self.correctas+=1
        else:
            self.incorrectas+=1
        if ayuda:
            self.puntaje+=5






