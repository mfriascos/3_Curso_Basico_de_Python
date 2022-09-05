dolares = input("Digite la cantidad de dólares que tiene: ")
dolares = float(dolares)
valor_del_peso = 4466
#valor_del_peso = float(valor_del_peso)
pesos = dolares*valor_del_peso
pesos = round(pesos,2)
pesos = str(pesos)

print("Tienes " + pesos + " pesos")
