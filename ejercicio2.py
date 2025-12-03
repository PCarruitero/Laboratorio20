salario = float(input("Ingrese su salario: "))
total = salario * 14
restante = total
impuesto = 0
tramo = []
limite1 = 20000
if total > 0:
    parte = min(total, limite1)
    impuesto1 = parte * 0
    tramo.append(impuesto1)
    impuesto += impuesto1
    restante -= parte
limite2 = 50000
if restante > 0:
    parte = min(restante, limite2 - limite1)
    impuesto2 = parte * 0.1
    tramo.append(impuesto2)
    impuesto += impuesto2
    restante -= parte
limite3 = 100000
if restante > 0:
    parte = min(restante, limite3 - limite2)
    impuesto3 = parte * 0.2
    tramo.append(impuesto3)
    impuesto += impuesto3
    restante -= parte
if restante > 0:
    parte = restante
    impuesto4 = parte * 0.3
    tramo.append(impuesto4)
    impuesto += impuesto4
    restante -= parte
for i, imp in enumerate(tramo):
    print("Impuesto por tramo: ", tramo[i])
print("Total del impuestos: ", impuesto)
tasa_efectiva_real = (impuesto / total) * 100
print("Tasa efectiva real: ", tasa_efectiva_real, "%")