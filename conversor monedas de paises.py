bienvenida = """
Bienvenido al 4to programa este programa es un conversor de monedad de 3 paises a dolares 👌
"""
print(bienvenida)
menu = """
Opciones para convertir a dolares

Marca 1 para convertir de pesos Colombianos
Marca 2 para convertir de pesos Argentinos
Marca 3 para convertir de pesos Méxicanos

"""
solonumeros = "Debes ingresar un valor númerico 🤞"
agradecimiento="Gracias por usar este programa hasta la próxima 😍"
def calculo (valordolar, pesos, moneda,opcion):
       while True:
           valordolar = (valordolar)
           pesos = (pesos)
           conversion = float(pesos / valordolar)
           conversion = round(conversion, 2)
           moneda = (moneda)
           print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
           nuevocalculo = (str(input("¿Quieres hacer un nuevo calculo ¿Si o No? : ")))
           if nuevocalculo == "no":
               exit(agradecimiento)
           elif nuevocalculo == "No":
               exit(agradecimiento)
           elif nuevocalculo == "n":
               exit(agradecimiento)
           elif nuevocalculo == "NO":
               exit(agradecimiento)
           elif nuevocalculo == "not":
               exit(agradecimiento)
           else:
               print("¡Vamos por un nuevo calculo! 🤞 ")
               break



def inicio (opcion):
    while True:
        try:
            opcion=int(input(menu))
        except ValueError:
            print("Debes esribir un número no texto")
            continue
        else:
            if opcion == 1:
                calculo(4800,pesos=float(input("¿Cuantos pesos Colombianos  quieres convertir? 🤔 ")),moneda="PESOS COLOMBIANOS",opcion=1)
            elif opcion == 2:
                calculo(153.83,pesos=float(input("¿Cuantos pesos Argentinos quieres convertir? 🤔 ")),moneda="PESOS ARGENTINOS",opcion=2)
            elif opcion == 3:
                calculo(19.90,pesos=float(input("¿Cuantos pesos Méxicanos quieres convertir? 🤔 ")),moneda="PESOS MEXICANOS",opcion=3)
            else:
                print(""" Debes elegir un número del menú 1, 2 o 3  """)
                return inicio(opcion=int(input(menu)))
if __name__ == "__main__":
    inicio(opcion=int)