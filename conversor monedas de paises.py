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
agradecimiento="Gracias por usar este rpograma hasta la próxima 😍"
def calculo (valordolar, pesos, moneda):
       while True:
           valordolar = (valordolar)
           pesos = (pesos)
           conversion = float(pesos / valordolar)
           conversion = round(conversion, 2)
           moneda = (moneda)
           print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
           nuevocalculo = (str(input("¿Quieres hacer un nuevo calculo de " + moneda + " ¿Si o No? : ")))
           if nuevocalculo == "no":
               print(agradecimiento)
               exit()
           elif nuevocalculo == "No":
               print(agradecimiento)
               exit()
           elif nuevocalculo == "n":
               print(agradecimiento)
               exit()
           elif nuevocalculo == "NO":
               print(agradecimiento)
               exit()
           elif nuevocalculo == "not":
               print(agradecimiento)
               exit()
           else:
               print("¡Vamos por un nuevo calculo! 🤞 ")
               break

def validacionmenu (opcion):
    while True:
        try:
            opcion=opcion
        except ValueError:
            print("Debes esribir un número no texto")
            continue
        else:
            if opcion == 1:
                calculo(4700,pesos = float(input("¿Cuantos pesos Colombianos  quieres convertir? 🤔 ")),moneda="PESOS COLOMBIANOS")
            elif opcion == 2:
                calculo(153.83,pesos = float(input("¿Cuantos pesos Argentinos quieres convertir? 🤔 ")),moneda="PESOS ARGENTINOS")
            elif opcion == 3:
                calculo(19.90,pesos = float(input("¿Cuantos pesos Méxicanos quieres convertir? 🤔 ")),moneda="PESOS MEXICANOS")
            else:
                print(""" Debes elegir un número del menú 
                1, 2 o 3  """)
                return validacionmenu (opcion=int(input(menu)))
validacionmenu(opcion=int(input(menu)))