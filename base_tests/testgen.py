
###### Imports #######
import sys
import PySimpleGUI as sg  
import time    
import serial
import numpy as np
import json
#######################

def generar_string_comando (modo,x0,x1,x2):
    comm = '{"mode" : %s, "x0" : %s , "x1" : %s , "x2" : %s }' % (modo, x0, x1, x2)
    return comm

while True:
    Modo = str(input("Modo: "))
    X0 = str(input("X0: "))
    X1 = str(input("X1: "))
    X2 = str(input("X2: "))

    comando = generar_string_comando (Modo, X0, X1, X2)
    print (comando)
    comandoDict=json.loads(comando)

    #Extraer comando
    modo = comandoDict["mode"]  # 0 = XYZ, 1=Q123
    x0 = comandoDict["x0"]
    x1 = comandoDict["x1"]
    x2 = comandoDict["x2"]
    print (modo)
    print (x0)
    print (x1)
    print (x2)