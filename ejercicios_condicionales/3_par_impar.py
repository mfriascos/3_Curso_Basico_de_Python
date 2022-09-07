# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla si es par o impar.

def run():
    print('')
    numero = int(input('Digite un número entero: '))
    
    if numero % 2 == 0:
        print('')  
        print('El número {} es par'.format(numero))
        print('')
    else:
        print('')  
        print('El número {} es impar'.format(numero)) 
        print('')

        
if __name__ == "__main__":
    run()