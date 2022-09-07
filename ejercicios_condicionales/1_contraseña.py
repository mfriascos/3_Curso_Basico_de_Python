# Escribir un programa que almacene la cadena de caracteres contraseña en una 
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas.
def imp():
    c_pass = ''
    print('')
    print('************************************************************')
    print('*******************C O N T R A S E Ñ A**********************')
    print('')
    c_pass = input("Compruebe su contraseña: ")
    c_pass = c_pass.strip()
    c_pass = c_pass.lower()
    return c_pass


def passw(c_pass,password):
    flag = True 
    contador = 0
    while flag == True:
        if c_pass != password:
            c_pass = imp()
            contador += 1
            if contador == 3:
                print('')
                print("Pasaste el número de intentos. Ingresa nuevamente")
                print('')
                flag = False
        else:
            print('')
            print("Gracias, su contraseña es correcta")
            print('')
            flag = False  
        


def run():
    flag2 = True
    while flag2 == True:
        print('')
        print('*********************************************************')
        print('*******************NUEVA CONTRASEÑA**********************')
        print('')
        password = input('Digite su nueva contraseña: ')
        print('')
        password_v = input('Escriba nuvamente su contraseña: ')
        password = password.strip()
        password = password.lower()
        password_v = password_v.strip()
        password_v = password_v.lower()

        if password == password_v:
            c_pass = imp()
            passw(c_pass, password)
            flag2 = False

        else:   
            print('')
            print('SU CONTRASEÑA NO COINCIDE, INTENTELO NUEVAMENTE')
            print('')
        
if __name__ == "__main__":
    run()