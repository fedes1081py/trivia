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
            return []
        return list(self.preguntas)


    def generar_preguntas_random(self, tematica):
        #vamos a generar las preguntas random
        if not tematica.strip():
            return []
        preguntas_random = random.sample(self.preguntas[tematica],k=5)
        return preguntas_random


class Juego:
    def __init__(self,ruta_preguntas):
        self.usuario = self.validar_nombre()
        self.puntaje = 0
        self.correctas = 0
        self.incorrectas = 0
        self.preguntas = Preguntas(ruta_preguntas)
    
    @property
    def puntaje(self):
        return self._puntaje
    @puntaje.setter
    def puntaje(self,puntaje):
        #colocamos un max para que si el numero puntaje es negativo se sume 0
        self._puntaje = max(0,puntaje)

    
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
        return self.puntaje,self.usuario
        

    def calcular_puntaje(self,respuesta_correcta, ayuda):
        if respuesta_correcta and ayuda:
            self.puntaje +=5
        elif respuesta_correcta and not ayuda:
            self.puntaje+=10
        if respuesta_correcta:
            self.correctas+=1
        else:
            self.incorrectas+=1


