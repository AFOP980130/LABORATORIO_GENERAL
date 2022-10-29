bienvenida = """
Bienvenido 😍
"""
print(bienvenida)
menu = """
Elige la moneda que quieres convertir

Marca 1 para convertir de pesos Colombianos
Marca 2 para convertir de pesos Argentinos
Marca 3 para convertir de pesos Méxicanos

Ingresa tu opción aquí ⬇️.
"""
solonumeros = "Debes ingresar un valor númerico 🤞"
agradecimiento="Gracias por usar este programa, hasta la próxima 😍"
def nuevocalculo():
    nuevocalculo = (str(input("¿Quieres hacer un nuevo calculo ¿Si o No? : ")))
    if nuevocalculo == "no" or nuevocalculo =="NO":
        exit(agradecimiento)
    else:
        print("¡Vamos por un nuevo calculo! 🤞 ")
        inicio()
def calculo (valordolar, pais):
           valordolar = (valordolar)
           while True:
               try:
                   pesos = float(input("¿Cuantos pesos " + str(pais) + " quieres convertir? 🤔 "))
               except ValueError:
                   print(solonumeros)
                   return
               else:
                   conversion = float(pesos / valordolar)
                   conversion = round(conversion, 2)
                   print("El resultado es $" + str(conversion) + " dolares Americanos 🤑👌")
                   nuevocalculo()
def inicio ():
    while True:
        try:
            opcion=int(input(menu))
        except ValueError:
            print(solonumeros)
            continue
        else:
            if opcion == 1:
                calculo(valordolar=4800,pais="COLOMBIANOS")
            elif opcion == 2:
                calculo(valordolar=153.83,pais="ARGENTINOS")
            elif opcion == 3:
                calculo(valordolar=19.90,pais="MÉXICANOS")
            else:
                print(""" Debes elegir un número del menú 1, 2 o 3  """)
                return inicio()
if __name__ == "__main__":
    inicio()