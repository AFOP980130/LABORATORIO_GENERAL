## Conversor de dolares a pesos Colombainos
print("Bienvenido a mi segundo programa conversor de dolares a pesos ๐ค๐ค๐ค")

##valor_pesos = int(input("ยฟQue precio tiene el peso hoy?: "))
Valordolar = 4735

while True:
    try:
        mis_dolares = float(input("ยฟCantidad de USD a convertir a COP?: ๐ค "))
    except ValueError:
        print("""Debes ingresar un valor nรบmerico ๐ค""")
        continue
    conversion = float(mis_dolares * Valordolar)
    conversion = round(conversion, 2)
    print("El resultado es  $" + str(conversion) + " pesos Colombianos ๐")
    try:
        otro_calculo = str(input("ยฟQuieres hacer otro calculo Si o No?: "))
    except ValueError:
        print(" Si o No: ๐ค ")
        continue
    if otro_calculo != "No" or otro_calculo != "no":
        print("๐ Nueva conversiรณn ๐")
    elif otro_calculo == "No" or otro_calculo == "no":
        print("๐๐๐ Gracias por usar mi programa ๐๐๐")
    elif otro_calculo == "NO" or otro_calculo == "n":
        print("๐๐๐ Gracias por usar mi programa ๐๐๐")
        break
