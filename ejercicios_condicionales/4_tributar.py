# Para tributar un determinado impuesto se debe ser mayor de 16 años 
# y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos 
# mensuales y muestre por pantalla si el usuario tiene que tributar o 
# no.

def run():
    print('')
    nombre = input('Nombre: ')
    print('')
    edad = int(input('Edad: '))
    print('')
    ingreso = int(input('Digite sus ingresos sin espacios ni puntos: '))

    if edad >= 16 and ingreso >= 1000:
        print('')
        print('{}, necesita declarar renta'.format(nombre))
        print('')
    elif edad < 16:
        print('')
        print('{}, no tiene edad para declarar renta'.format(nombre))
        print('')
    else:
        print('')
        print('{}, No necesita declarar renta'.format(nombre))
        print('')
        

if __name__ == "__main__":
    run()