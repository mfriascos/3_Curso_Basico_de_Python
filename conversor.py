pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos) #Transformamos el contenido a decimal 
valor_dolar = 4466
dolares = pesos/valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)

print("Tienes $" + dolares + " dólares")
