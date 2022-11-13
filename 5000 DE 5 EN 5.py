

def run():
    presentacion = """Vamos a imprimir los números
     desde el 1000 hasta en 5000 de 5 en 5"""
    print(presentacion)
    run2()


def run2():
    numbersde5en5 = [i for i in range(1000, 5000, 5)]
    print(numbersde5en5)

if __name__ == '__main__':
    run()
