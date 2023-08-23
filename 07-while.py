# Primer ejericio con while
# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

# Segundo ejercio con while
# comando = ""
# Al agregar el método lower, al ejecutar el prometa se puede escribir la forma que uno quiere el comando salir ya sea minuscula o mayuscula
# y la aplicacion sin problema
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print("comando")

# Loop infinito
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
