##Andres Orozco primerps pasos
print(" ๐ค๐ค๐ค Hola Bienvenido a mi conversor de dolares a pesos ๐ค๐ค๐ค ")
solonumeros = ("Debes ingresar un valor nรบmerico ๐ค")
while True:
    try:
        valor_dolar = float(input("ยฟQue precio tiene el USD hoy en COP? ๐ค "))
    except ValueError:
        print(solonumeros)
        continue
    try:
        pesos = float(input("ยฟCuantos COP quieres convertir? ๐ค "))
    except ValueError:
        print(solonumeros)
        continue
    conversion = float(pesos / valor_dolar)
    conversion = round(conversion, 2)
    print("El resultado es $" + str(conversion) + " dolares Americanos ๐ค๐")
    otra_conversion = str(input("ยฟQuieres hacer otro calculo Si o No? ๐ค"))
    if otra_conversion != "No" and otra_conversion != "no":
        print("Vamos con un nuevo calculo ๐")
    elif otra_conversion == "No" or otra_conversion == "no":
        print("๐๐๐ Gracias por usar mi primer programa ๐๐๐")
        break