"Bienvenido a mi 3er programa de medidor de edad legal"
edadlegal = 18
while True:
    try:
        edadusuario = int(input("¿Que edad tienes? : "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    if  edadusuario == edadlegal:
        print("Eres ahora mayor de edad")
    elif edadusuario > edadlegal:
        edadmayor = (edadusuario - edadlegal)
        print("Ya tienes " + str(edadmayor) + " años más que la edad legal")
    elif edadusuario < edadlegal:
        edadmenor = (edadlegal - edadusuario)
        print( "Aún te faltan " + str(edadmenor) + " años para llegar a la edad legal")
    else:
        print("debes ingresar un edad en número")

    nuevocalculo = (str(input("¿Quieres saber si tienes las edad legar? : ")))
    if nuevocalculo == "si" or  nuevocalculo == "SI":
        print("Nuevo Calculo")
    elif nuevocalculo == "No" or nuevocalculo =="no":
        print("Gracias por usar mi tercer programa")
        break


