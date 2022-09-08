# En una determinada empresa, sus empleados son evaluados al final de cada año. Los 
# puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
# pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación 
# del nivel.

# Nivel	            Puntuación
# Inaceptable	        0.0
# Aceptable	            0.4
# Meritorio	            0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.
import random


def rand():
    flag = True
    while flag == True:
        aux = random.randrange(0,11,2)
        if aux == 2:
            aux = random.randrange(0,11,2)
        else:
            flag = False
            print(aux)
    return aux


def performance(name,aux):
    print('')
    if aux == 0:
        print("{}, your level is inacceptable".format(name))
    elif  aux == 4:
        print("{}, your level is acceptable".format(name))
    else:
        print("{}, your level is outstanding".format(name))


    
def run():
    print('')
    name = input('User name: ')
    print('')
    aux = rand()
    performance(name,aux)
    print('and, your payment is ${}'.format((2400*aux)/10))
    print('')

        

if __name__ == "__main__":
    run()