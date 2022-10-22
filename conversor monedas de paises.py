bienvenida = """
Bienvenido al 4to programa este programa es un conversor de monedad de 3 paises a dolares 👌
"""
print(bienvenida)
menu = """
Opciones para convertir a dolares

Marca 1 para Colombianos
Marca 2 para Argentinos
Marca 3 para Méxicanos

"""
solonumeros = "Debes ingresar un valor númerico 🤞"

###Validación de menú
opcion = int(input(menu))
def validarmenu (opcion):
    while True:
        try:
            opcion = (opcion)
        except ValueError:
            print(solonumeros)
            break

def calculo (valordolar, pesos, moneda):
    while True:
        valordolar = (valordolar)
        try:
            pesos = (pesos)
        except ValueError:
            print(solonumeros)
        conversion = float(pesos / valordolar)
        conversion = round(conversion, 2)
        moneda = (moneda)
        print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
        nuevocalculo = (str(input("¿Quieres hacer un nuevo calculo de " + moneda + " ¿Si o No? : ")))
        if nuevocalculo == "Si" or nuevocalculo == "si":
            print("Vamos por ese nuevo calculo")
        elif nuevocalculo == "No" or nuevocalculo == "no":
            print("Gracias por usar mi programa")
            break

while True:
    if opcion == 1:
        calculo(4700,pesos = float(input("¿Cuantos pesos Colombianos quieres convertir? 🤔 ")),moneda="PESOS COLOMBIANOS")
    elif opcion == 2 :
        calculo(153.83,pesos = float(input("¿Cuantos pesos Argentinos quieres convertir? 🤔 ")),moneda="PESOS ARGENTINOS")
    elif opcion == 3 :
        calculo(19.90,pesos = float(input("¿Cuantos pesos Colombianos quieres convertir? 🤔 ")),moneda="PESOS MEXICANOS")
    else:
        print("Debes seleccionar una opción del menú")
        break