## Conversor de dolares a pesos Colombainos
print("Bienvenido a mi segundo programa conversor de dolares a pesos 🤑🤑🤑")

##valor_pesos = int(input("¿Que precio tiene el peso hoy?: "))
Valordolar = 4735

while True:
    try:
        mis_dolares = float(input("¿Cantidad de USD a convertir a COP?: 🤑 "))
    except ValueError:
        print("""Debes ingresar un valor númerico 🤔""")
        continue
    conversion = float(mis_dolares * Valordolar)
    conversion = round(conversion, 2)
    print("El resultado es  $" + str(conversion) + " pesos Colombianos 😊")
    try:
        otro_calculo = str(input("¿Quieres hacer otro calculo Si o No?: "))
    except ValueError:
        print(" Si o No: 🤔 ")
        continue
    if otro_calculo != "No" or otro_calculo != "no":
        print("😊 Nueva conversión 😊")
    elif otro_calculo == "No" or otro_calculo == "no":
        print("😍😍😍 Gracias por usar mi programa 😍😍😍")
    elif otro_calculo == "NO" or otro_calculo == "n":
        print("😍😍😍 Gracias por usar mi programa 😍😍😍")
        break
