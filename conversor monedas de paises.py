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
opcion=int(input(menu))
def calculo (valordolar, pesos, moneda,opcion):
       while True:
           valordolar = (valordolar)
           pesos = (pesos)
           conversion = float(pesos / valordolar)
           conversion = round(conversion, 2)
           moneda = (moneda)
           print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
           nuevocalculo = (str(input("¿Quieres hacer un nuevo calculo de " + moneda + " ¿Si o No? : ")))
           if nuevocalculo != "no" and nuevocalculo != "No":
               break
           else:
               print("Gracias por usar mi programa")
               #break
def validacionmenu (opcion):
    while True:
        try:
            opcion = int(input(menu))
        except ValueError:
            print("Debes elegir esribir un número disponible en el menú")
            continue
        else:
            if opcion == 1:
                calculo(4700,pesos = float(input("¿Cuantos pesos Colombianos  quieres convertir? 🤔 ")),moneda="PESOS COLOMBIANOS",opcion=opcion)
            elif opcion == 2:
                calculo(153.83,pesos = float(input("¿Cuantos pesos Argentinos quieres convertir? 🤔 ")),moneda="PESOS ARGENTINOS",opcion=opcion)
            elif opcion == 3:
                calculo(19.90,pesos = float(input("¿Cuantos pesos Méxicanos quieres convertir? 🤔 ")),moneda="PESOS MEXICANOS",opcion=opcion)
            else:
                print("Debes leer bien")

validacionmenu(opcion)