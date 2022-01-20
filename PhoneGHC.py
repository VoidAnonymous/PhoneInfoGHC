import requests
import os
import time
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict
from colorama import Fore, init
from urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()

#colores fachas "GCH"
verde = Fore.GREEN
lverde = Fore.LIGHTGREEN_EX
rojo = Fore.RED
lrojo = Fore.LIGHTRED_EX
amarillo = Fore.YELLOW
blanco = Fore.WHITE
cyan = Fore.CYAN
violeta = Fore.MAGENTA
azul = Fore.BLUE
lazul = Fore.LIGHTBLUE_EX


# Informacion De numeros telefonicos :)

def consultaindividual():
    numerotelefonico = input("[+] ESCRIBE EL NÚMERO TELEFÓNICO: ")
    url1 = f"http://apilayer.net/api/validate?access_key=a34d97f03e51e991d6699b9de0b8694c&number={numerotelefonico}&country_code&format=1"
    url2 = f"https://phonevalidation.abstractapi.com/v1/?api_key=49f4fe982a1b4f5cacdde03608161cdd&phone={numerotelefonico}"

    data1 = requests.get(f"{url1}")
    data2 = requests.get(f"{url2}")

    dataJson1 = data1.json()
    dataJson2 = data2.json()

    existeono = dataJson1['local_format']

        # datos url numero 1
    validar = dataJson1['valid']
    prefijo = dataJson1['country_prefix']
    codigo = dataJson1['country_code']
    codigo_pais = dataJson1['country_name']
    localizacion = dataJson1['location']
        #datos url numero 2
    formato_local_pais = dataJson2['format']['local']
    carril = dataJson2['carrier']
    if existeono == '':
        print(f"{lrojo}NO EXISTE ")
    elif existeono is None:
        print(f"{lrojo}NO EXISTE ")
    else:
        print(f"{cyan}ES VALIDO ? :{blanco} {validar}\n{cyan}PREFIJO :{blanco} {prefijo}\n{cyan}FORMATO LOCAL :{blanco} {formato_local_pais}\n{cyan}CODIGO DEL PAIS :{blanco} {codigo}\n{cyan}PAIS :{blanco} {codigo_pais}\n{cyan}LOCALIZACIÓN :{blanco} {localizacion}\n{cyan}COMPAÑIA :{blanco} {carril}\n")


def portada():
    print(f"""{rojo} _________________________¶¶¶______________________
_____________________¶¶¶¶¶¶¶¶¶¶¶¶_________________
___________________¶¶¶_________¶¶¶________________
__________________¶¶_____________¶¶_______________
_________________¶¶________________¶______________
________________¶¶_________________¶¶_____________
________________¶__________________¶¶_____________
_______________¶¶___________________¶_____________
_______________¶¶___________________¶¶____________
_______________¶_¶¶_________________¶¶____________
_______________¶_¶¶_________________¶¶____________
_______________¶¶¶__________________¶_____________
___¶___________¶¶¶__________________¶_____________
___¶¶__________¶¶¶___¶¶¶¶____¶¶¶____¶___________¶¶
___¶¶__________¶¶¶__¶¶__¶¶__¶¶¶¶¶___¶¶__________¶¶
___¶¶¶_________¶¶¶_¶¶____¶__¶___¶¶_¶¶¶__________¶_
____¶¶_________¶¶¶_¶___¶¶¶__¶¶___¶_¶¶__________¶¶_
____¶¶¶_________¶__¶¶¶¶¶__¶__¶¶¶¶¶_¶__________¶¶¶_
____¶¶¶¶_______¶____¶¶¶__¶¶____¶¶¶_¶¶¶________¶¶¶_
_____¶_¶______¶¶¶_______¶¶¶¶________¶¶_______¶¶¶__
_____¶¶¶¶_______¶¶¶_____¶__¶_______¶¶_______¶¶¶¶__
______¶_¶¶________¶¶¶___¶__¶¶____¶¶¶________¶_¶___
_______¶_¶¶_____¶¶__¶___¶_¶¶¶___¶¶_________¶_¶____
_______¶¶_¶_____¶¶¶¶¶¶__¶¶¶¶¶__¶¶¶¶_______¶_¶¶____
________¶¶¶¶_____¶_¶¶¶__¶¶_¶___¶¶¶¶______¶¶_¶_____
_________¶_¶¶_____¶_¶¶¶_______¶¶¶¶______¶¶_¶______
__________¶_¶¶____¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶______¶_¶_______
___________¶_¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶_______
____________¶_¶¶____¶¶_________¶¶¶___¶¶_¶¶________
_____________¶_¶¶¶__¶¶¶¶¶¶_¶¶¶¶¶¶___¶¶_¶¶_________
______________¶¶_¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_¶¶__________
_______________¶¶_¶¶_¶_¶¶¶¶¶¶__¶_¶¶__¶¶___________
________________¶¶_¶¶_¶_______¶¶¶¶__¶_____________
_________________¶¶_¶¶¶¶¶¶¶¶¶¶¶¶__¶¶______________
________¶¶________¶¶_¶¶¶_¶¶¶¶¶___¶¶_______________
_______¶¶¶¶_________¶__¶¶__¶____¶¶________________
________¶¶¶¶_______¶_¶¶_¶¶¶¶¶¶¶¶__________¶¶______
_¶¶¶_____¶¶¶¶_¶¶¶¶¶¶¶_¶¶__¶¶¶¶¶_________¶¶¶¶¶_____
¶__¶¶¶¶¶__¶¶_¶¶¶¶____¶¶¶¶¶__¶¶¶¶¶______¶¶__¶______
¶__¶¶_¶¶¶¶¶¶¶_¶¶¶__¶¶¶¶__¶¶¶___¶¶¶¶¶__¶¶_¶¶_____¶¶
¶¶¶¶¶¶_____¶¶_¶¶¶¶¶¶¶______¶¶¶____¶¶¶¶¶¶¶¶_____¶¶¶
__¶__¶¶¶¶¶¶¶¶_¶______________¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_
_____________¶¶¶________________¶¶¶¶¶_¶¶______¶¶¶¶
_____________¶¶¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶¶¶___
______________¶¶¶¶¶____________¶¶¶¶¶_¶____________
_______________________________¶¶__¶¶_____________


{rojo}    . .   
 {verde}PROGRAMADO POR VOID ANONYMOUS                 {azul}Versión 1.0
 {lverde}═══════════════════════════════════════════════════════
 {lrojo}INSTAGRAM: {blanco}void_anonymous_
 {rojo}GITHUB:{blanco} https://github.com/VoidAnonymous
 {rojo}coloca numero las demas opciones estaran disponible en la version 1.5
 {lverde}═══════════════════════════════════════════════════════
    """)
    time.sleep(0.2)

      		
def eleccion():
    print(f"{verde}")
    opc = input(f"[Anonymous@root]>> ")
    if opc == "dni":
        consulta_dni()
        eleccion()
    elif opc == "help":
        menu_ayuda()
        eleccion()
    elif opc == "ayuda":
        menu_ayuda()
        eleccion()
    elif opc == "?":
        menu_ayuda()
        eleccion()
    elif opc == "casa":
        direccion_casa()
        eleccion()
    elif opc == "ruc":
        consultaruc()
        eleccion()
    elif opc == "numero":
        consultaindividual()
        eleccion()
    elif opc == "buscar":
        consulta_por_nombres()
        eleccion()
    elif opc == "clear":
        os.system("clear")
        portada()
        eleccion()
    elif opc == "cls":
        os.system("cls")
        portada()
        eleccion() 
    elif opc == "exit":
        exit()   
    else:
        print(f"""{rojo}
    [ ! ] OPCION INCORRECTA
        {verde}""")
        eleccion()
    
    
# inicio de tool
if __name__ == "__main__":
    portada()
    eleccion()
