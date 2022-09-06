def conversor(tipo_pesos,valor_dolar):
        pesos = float(input("Cuántos pesos "+ tipo_pesos + " tienes?: "))
        dolares = pesos/valor_dolar
        dolares = round(dolares,2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos 
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos",4466)
elif opcion == 2:
    conversor("Argentinos",140)

elif opcion == 3:
    conversor("Mexicanos",20)
else:
    print("Digite una opción correcta")
