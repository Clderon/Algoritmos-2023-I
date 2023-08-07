# Lista de nombres de frutas
frutas = ["manzana", "naranja", "plátano", "uva", "pera"]

# Fruta que queremos buscar
fruta_buscada = "uva"

# Verificar si la fruta está en la lista
if fruta_buscada in frutas:
    # Obtener el índice de la fruta en la lista
    indice_fruta = frutas.index(fruta_buscada)
    print(f"{fruta_buscada} está en la lista en la posición {indice_fruta}.")
else:
    print(f"{fruta_buscada} no está en la lista.")
