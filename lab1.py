import random


def run():
    bienvenida = """
    Vamos al juego de la adivinanza, trata de adivinar el número que la computadora eligio.
    ES DEL 1 AL 100
    TIENES 5 VIDAS 
    """
    print(bienvenida)
    numerovariado = random.randint(1, 100)
    numeroelegido = int(input("Escribe tu número: "))
    vidas = 5
    run2(numerovariado, numeroelegido, vidas)


def run2(numerovariado, numeroelegido, vidas):
    while numeroelegido != numerovariado:
        if vidas == 0:
            print("Perdiste el número era: ", numerovariado, "👀")
            run()
        print("Te quedan:", vidas, " vidas.")
        if numeroelegido < numerovariado:
            vidas -= 1
            print("Elige un número mayor ⬆️")
            numeroelegido = int(input("Escribe tu número: "))
        elif numeroelegido > numerovariado:
            vidas -= 1
            print("Elige un número menor ⬇️")
            numeroelegido = int(input("Escribe tu número: "))
    if numeroelegido == numerovariado:
        print("Ganaste 😍")
        run()


if __name__ == "__main__":
    run()
