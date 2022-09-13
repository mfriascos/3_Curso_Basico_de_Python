# Escriba un programa en Python para imprimir todos los números primos entre 0 y 100 e imprima cuántos
# números primos hay.

def run(): 
    flag = True
    cont = 0
    for i in range(2,101):
        for j in range(2,i):
            mod = i%j
            if mod == 0:
                flag = False 
                break
            else:
                flag = True
        if flag == True:
            print(i)
            cont = cont+1   

    print('')
    print('El total de Número primos entre 1 y 100 son: {}'.format(cont))
        

if __name__ == "__main__":
    run()