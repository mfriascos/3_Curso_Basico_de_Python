# Escribir un programa que pida al usuario dos números y muestre por pantalla 
# su división. Si el divisor es cero el programa debe mostrar un error.
def division(dividendo,divisor):
    resultado = float(round(dividendo/divisor,4))
    print('')
    print ("{}/{} = {}".format(dividendo,divisor,resultado))
    print('')

def run():
    flag = True
    print('')
    print('********************************************************')
    print('*******************D I V I S I Ó N**********************')
    print('')
    dividendo = int(input('Dividendo: '))
    while flag == True:
        print('')
        divisor = int(input('Divisor: '))
        if divisor == 0:
            print('')
            print('El divisor debe ser diferente a 0')

        else:
            division(dividendo,divisor)
            flag = False
            
            

if __name__ == "__main__":
    run()