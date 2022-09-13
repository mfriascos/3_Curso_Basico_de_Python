# Dado un número, cuente el número total de dígitos de un número
# * Por ejemplo, el número es 75869, por lo que la salida debería ser 5.

from re import I


def run():
    number = input('Type a number: ')
    j=0
    for i in number:
       j = j+1
       i = j 
    print(i)    

if __name__ == "__main__":
    run()