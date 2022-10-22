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

valordolar = 0
while True:
    try:
        opcion = int(input(menu))
    except ValueError:
        print("Debes seleccionar una opción valida")
        continue
    if opcion == 1:
        valordolar = 4700
        solonumeros = "Debes ingresar un valor númerico 🤞"
        while True:
            try:
                pesos = float(input("¿Cuantos pesos Colombianos quieres convertir? 🤔 "))
            except ValueError:
                print(solonumeros)
                continue
            conversion = float(pesos / valordolar)
            conversion = round(conversion, 2)
            print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
            try:
                otra_conversion = str(input(" ¿Quieres hacer otro calculo Si o No? 🤔"))
            except ValueError:
                print("¿Si o No? 🤔 ")
                continue
            if otra_conversion != "No" and otra_conversion != "no":
                print("Vamos con un nuevo calculo 😊")
            elif otra_conversion == "No" or otra_conversion == "no":
                print("😍😍😍 Gracias por usar mi primer programa 😍😍😍")
                break

    elif opcion == 2 :
        valordolar = 153.83
        solonumeros = ("Debes ingresar un valor númerico 🤞")
        while True:
            try:
                pesos = float(input("¿Cuantos pesos Argentinos quieres convertir? 🤔 "))
            except ValueError:
                print(solonumeros)
                continue
            conversion = float(pesos / valordolar)
            conversion = round(conversion, 2)
            print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
            try:
                otra_conversion = str(input("¿Quieres hacer otro calculo Si o No? 🤔"))
            except ValueError:
                print("¿Si o No? 🤔 ")
                continue
            if otra_conversion != "No" and otra_conversion != "no":
                print("Vamos con un nuevo calculo 😊")
            elif otra_conversion == "No" or otra_conversion == "no":
                print("😍😍😍 Gracias por usar mi primer programa 😍😍😍")
                break
    elif opcion == 3 :
        valordolar = 19.92
        solonumeros = ("Debes ingresar un valor númerico 🤞")
        while True:
            try:
                pesos = float(input("¿Cuantos pesos Méxicanos quieres convertir? 🤔 "))
            except ValueError:
                print(solonumeros)
                continue
            conversion = float(pesos / valordolar)
            conversion = round(conversion, 2)
            print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
            try:
                otra_conversion = str(input("¿Quieres hacer otro calculo Si o No? 🤔"))
            except ValueError:
                print("¿Si o No? 🤔 ")
                continue
            if otra_conversion != "No" and otra_conversion != "no":
                print("Vamos con un nuevo calculo 😊")
            elif otra_conversion == "No" or otra_conversion == "no":
                print("😍😍😍 Gracias por usar mi primer programa 😍😍😍")
                break
    else:
        print("Debes seleccionar una opción del menú")