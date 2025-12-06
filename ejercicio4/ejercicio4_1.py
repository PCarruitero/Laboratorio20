def normalizar(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        raise ValueError("Modo no válido.")
    nueva = lista[:] 
    minimo = min(lista)
    maximo = max(lista)
    media = sum(lista) / len(lista)
    var = sum((x - media) ** 2 for x in lista) / len(lista)
    desviacion = var ** 0.5
    norma = sum(x*x for x in lista) ** 0.5
    resultado = []
    for x in lista:
        if modo == "minmax":
            denominador = maximo - minimo
            resultado.append((x - minimo) / denominador if denominador != 0 else 0)
        elif modo == "zscore":
            resultado.append((x - media) / desviacion if desviacion != 0 else 0)
        elif modo == "unit":
            resultado.append(x / norma if norma != 0 else 0)
    return resultado
valores = [10, 20, 30]
print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))
print("Original:", valores)