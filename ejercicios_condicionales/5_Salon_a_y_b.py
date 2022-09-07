# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y 
# el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir 
# un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el 
# grupo que le corresponde.

def run():
    print('')
    name = input('Type your name: ')
    print('')
    gender = input('Type your gender (M or W): ')
    gender = gender.upper()
    name = name.lower()
    letter = name[0]
    if (gender == 'W' and letter < 'm') or (gender == 'M' and letter > 'n'):
        print('')
        print('{} is in the group A'.format(name.capitalize()))
        print('')
    else:
        print('')
        print('{} is in the group B'.format(name.capitalize()))
        print('')
        

if __name__ == "__main__":
    run()