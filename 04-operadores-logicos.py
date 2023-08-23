# and, or, not

# Ejercico de encender un auto

# Uso del operador and
# gas = True
# encendido = True

# if gas and encendido:
#     print("Puedes avanzar")

# uso del operador or
# gas = False
# encendido = True

# if gas or encendido:
#     print("Puedes avanzar")

# Uso del operador not
# gas = False
# encendido = True

# if not gas and encendido:
#     print("Puedes avanzar")

# otra forma de aplicar operadores lógicos
# gas = True
# encendido = True
# edad = 20

# if gas and encendido and edad > 18:
#     print("Puedes avanzar")

gas = False
encendido = True
edad = 20

if not gas and (encendido or edad > 25):
    print("Puedes avanzar")
