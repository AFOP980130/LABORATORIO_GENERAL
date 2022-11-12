def runB():
    for i in range(1000):
        if i % 2 == 0:
            continue
        print(i)


def runa():
    cadena = input("Escribe una palabra para contar cuantas H tiene: ")
    cantidadh = 0
    for i in cadena:
        if i == 'h' or i == "H":
            cantidadh += 1
        else:
            continue
    if cantidadh == 0:
        print("No se encontró la H")
    else:
        print("Se encontró la H", cantidadh , "veces en tu palabra")
def run3(primo,numero):
    if primo == 0:
        print("Tu número ",numero, "es primo")
    else:
        print(numero, "no es primo")
    run()
def run2(numero):
    primo = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            primo += 1
    run3(primo,numero)
def run():
    numero = int(input("Escribe un número para saber si es primo o no: "))
    run2(numero)

if __name__ == "__main__":
    run()