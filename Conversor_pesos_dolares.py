##Copiando conversor de monedas Platzi
print(" Hola Bienvenido a mi conversor de dolares a pesos ")
valor_dolar = float(input("¿Que precio tiene el USD hoy en COP? "))

while True:
    pesos = float(input("¿Cuantos COP quieres convertir? "))
    conversion = float(pesos / valor_dolar)
    conversion = round(conversion, 2)
    print("El resultado es $" + str(conversion) + " dolares Americanos")
    otra_conversion = str(input("¿Quieres hacer otro calculo Si o No? "))
    if otra_conversion != "No" and otra_conversion != "no":
        print("Nuevo calculo")
    elif otra_conversion == "No" or otra_conversion == "no":
        print("Gracias por usar mi primer programa")
        break


