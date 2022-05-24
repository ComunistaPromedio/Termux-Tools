#!/bin/python

# Importando librerias
from colorama import Fore
import os, time, base64

# Declarando función

def ecdc():
    print(Fore.CYAN + """
 #######  #####  ######   #####  
 #       #     # #     # #     # 
 #       #       #     # #       
 #####   #       #     # #       
 #       #       #     # #       
 #       #     # #     # #     # 
 #######  #####  ######   #####  
                                 """ + Fore.RESET)
    print("_____________________")
    print("[1] Encode base64    |")
    print("[2] Descode base64   |")   
    print("[3] Salir            |")
    print("_____________________|")
    
    # Hacer que el usuario elija una opción 

    eleccion = input("\nElige una opcion: ")
    
    # Opción 1, encargada de encriptar alguna palabra 

    if eleccion == "1":
        encript = input("Escribe el texto que quieras codificar: ")
        encr1pt = base64.b64encode(bytes(encript, 'utf-8'))
        print(encr1pt)

        # Opción 2, encargada de desencriptar la palabra


    elif eleccion == "2":
        descript = input("Escribe el texto que quieras descodificar: ")
        descr1pt = base64.b64decode(bytes(descript, 'utf-8'))
        print(Fore.GREEN + descr1pt)


     # Opción 3, le da al usuario la opción de salirse del programa

    elif eleccion == "3":
        exit()
ecdc()
