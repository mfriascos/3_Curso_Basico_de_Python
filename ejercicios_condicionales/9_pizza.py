# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los 
# ingredientes para cada tipo de pizza aparecen a continuación.

# * Ingredientes vegetarianos: Pimiento y tofu.
# * Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en 
# función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas 
# la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
# todos los ingredientes que lleva.

def menu():
    
    print('- Mozarella ')
    print('- Tomato')
    print('Do you want (1).Pepperoni? ')
    print('(2). Ham? ')
    print('(3). Salmon')
    print('')
    ingredient = int(input(': '))
    print('')

    if ingredient == 1:
        print('********** Pizza ********')
        print('- Mozarella ')
        print('- Tomato')
        print('- Pepperoni')
    elif ingredient == 2:
        print('********** Pizza ********')
        print('- Mozarella ')
        print('- Tomato')
        print('- Ham')
    elif ingredient == 3:
        print('********** Pizza ********')
        print('- Mozarella ')
        print('- Tomato')
        print('- Salmon')
    else: 
        print('That is incorrect!')        
    print('')


def menu_v():

    print('- Mozarella ')
    print('- Tomato')
    print('Do you want (1).Bell Pepper? ')
    print('(2). Tofu? ')
    print('')
    ingredient = int(input(': '))
    print('')

    if ingredient == 1:
        print('********Vegetarian Pizza******')
        print('- Mozarella ')
        print('- Tomato')
        print('- Bell Pepper')
    elif ingredient == 2:
        print('********Vegetarian Pizza******')
        print('- Mozarella ')
        print('- Tomato')
        print('- Tofu')
    else: 
        print('That is incorrect!')        
    print('')


def run(vegetarian):
    print('')
    print('************************************************************')
    print('************************ M E N U ***************************')
    print('')
    print('********************** INGREDIENTS *************************')
    print('')

    if vegetarian == True:
        menu_v()
    else:
        menu()
    
    
if __name__ == "__main__":
    print('')
    vegetarian = input("Do you want vegetarian pizza ? (Y/N): ")
    
    if vegetarian == 'y' or vegetarian == 'Y':
        vegetarian = True
    elif vegetarian == 'n' or vegetarian == 'N':
        vegetarian = False
    else: 
        print('')
        print('Your entry is incorrect!')

    run(vegetarian)
    print('')