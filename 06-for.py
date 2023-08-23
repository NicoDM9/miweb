# For - Se utliza para iterar una lista de elementos

# Primer ejercicio
# for numero in range(5):
#     print(numero, numero * "holamundo")

# Segundo ejercicio buscando un elemento y una vez encontrado detener la aplicación
# buscar = 3
# for numero in range(5):
#     print(numero)
#     if numero == buscar:
#         print("Encontrado", buscar)
#         break

# Tercer ejercicio buscando un elemento pero no encuentra el elemento
buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("no encontre el numero buscado:(")


for char in "Ultimate Python":
    print(char)
