# Escribir un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la 
# entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años 
# debe pagar 5€ y si es mayor de 18 años, 10€.

def run(age):
    if age < 4:
        print('')
        print('Customer enters for free')
    elif age < 18:
        print('')
        print('Ticket cost $5')
    else: 
        print('')
        print('Ticket cost $10')
        

if __name__ == "__main__":
    flag = True
    while flag == True:
        print('')
        age = int(input("Type the user's age: "))
        if age <= 0:
            print('')
            print('That is incorrect')
        else: 
            flag = False
    run(age)
    print('')