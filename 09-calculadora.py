# Segundo ejercicio aplicando lo aprendido en el curso
print("Bienvenido a la calculadora")
print("Escribe salir para salir")
print("Las operaciones son suma, resta, multi, div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    op = input("Ingresa operación ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida")
        break
    print(f"El resultado es: {resultado}")
