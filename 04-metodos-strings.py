# Metodos reservadas(son funciones que se encuentra dentro de un objeto)
animal = "  chanCHito feliz  "
print(animal.upper())  # Lo convierte todo en mayúscula
print(animal.lower())  # Lo covierte todo en minúscula
# capitalize - la primera letra lo convierte en mayúscula y también se puede encadenar los métodos asi como se muestra en el ejemplo
print(animal.strip().capitalize())
# title - La primeras letras de cada palabra con convierte en mayúscula
print(animal.title())
# strip-Remueve(elimina) todos los espacios en blanco en los lados tanto de izquierda y derecha
print(animal.strip())
print(animal.lstrip())  # Quita el espacio de la izquierda
print(animal.rstrip())  # Quita es espacio de la derecha
print(animal.find("cH"))  # Busca el caracter y devuelve el valor del índice
print(animal.replace("nCH", "j"))  # reemplaza caracteres
# el resultado es Booleano,donde nos dice si se encuentra o no encuentra los
# caracteres buscados, similiar al método find
print("nCH" in animal)
print("nCH" not in animal)  # Busca por si nose encuentra el caracter buscado
