## Conversor de dolares a pesos Colombainos
print("Bienvenido a mi segundo programa conversor de dolares a pesos")

##valor_pesos = int(input("¿Que precio tiene el peso hoy?: "))
valor_dolar= 4735

while True:
    mis_dolares = float(input("¿Cantidad de dolar a convertir?: "))
    conversion = float(mis_dolares*valor_dolar)
    conversion = round(conversion, 2)
    print("El resultado es  $" + str(conversion) + " pesos Colombianos")
    otro_calculo = str(input("¿Quieres hacer otro calculo Si o No?: "))
    if otro_calculo != "No" and otro_calculo != "no":
        print("Nueva conversión")
    elif otro_calculo == "No" or otro_calculo == "no":
        print("Gracias por usar mi programa :D")
        break
