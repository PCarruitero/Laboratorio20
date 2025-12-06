lista = []
cantidad = int(input("¿Cuantos valores deseas ingresar? "))
for i in range(cantidad):
    lista.append(float(input(f"Valor {i+1}: ")))
modo = input("Modo de normalizacion (minmax / zscore / unit): ").lower()
def normalizar(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        raise ValueError("Modo no valido")
    minimo = min(lista)
    maximo = max(lista)
    media = sum(lista) / len(lista)
    var = sum((x - media) ** 2 for x in lista) / len(lista)
    desviacion = var ** 0.5
    norma = sum(x*x for x in lista) ** 0.5
    resultado = []
    for x in lista:
        if modo == "minmax":
            resultado.append((x - minimo) / (maximo - minimo) if maximo != minimo else 0)
        elif modo == "zscore":
            resultado.append((x - media) / desviacion if desviacion != 0 else 0)
        elif modo == "unit":
            resultado.append(x / norma if norma != 0 else 0)
    return resultado
print("\nResultado:")
print(normalizar(lista, modo))
print("Original:", lista)