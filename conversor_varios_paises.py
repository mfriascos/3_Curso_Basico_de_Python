menu = """
Bienvenido al conversor de monedas $$$

1 - Pesos Colombianos
2 - Pesos Argentinos 
3 - Pesos Mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos) #Transformamos el contenido a decimal 
    valor_dolar = 4466
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)

    print("Tienes $" + dolares + " dólares")

elif opcion == '2': 
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos) #Transformamos el contenido a decimal 
    valor_dolar = 140
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)

    print("Tienes $" + dolares + " dólares")    

elif opcion == '3':
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos) #Transformamos el contenido a decimal 
    valor_dolar = 20
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)

    print("Tienes $" + dolares + " dólares")
    
else:
    print("Digite una opción correcta")
