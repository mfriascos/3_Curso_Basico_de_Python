# Los tramos impositivos para la declaración de la renta en un determinado país son los
# siguientes:

# Renta	                Tipo impositivo
# Menos de 10000€	         5%
# Entre 10000€ y 20000€	    15%
# Entre 20000€ y 35000€	    20%
# Entre 35000€ y 60000€	    30%
# Más de 60000€	            45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el 
# tipo impositivo que le corresponde.
def tax(income):
    if income < 10000 and income >=0:
        income = income*0.05
    elif income >= 10000 and income < 20000:
        income = income*0.15
    elif income >= 20000 and income < 35000:
        income = income*0.2
    elif income >= 35000 and income < 60000:
        income = income*0.3
    elif income >= 60000:
        income = income*0.45
    else:
        print('')
        print("Digite un valor correcto")
        print('')
    return income


def run():
    print('')
    print('**************************************************')
    print('*******************I N C O M E********************')
    print('')

    name = input('Name: ')
    print('')

    income = float(input("Enter the value of your annual income: U$"))
    print('')
    tax(income)

    newtax = income + tax(income)

    print(name + ', your total payout is {}'.format(newtax))
    print('')
    print('Thank You')
    print('')
        

if __name__ == "__main__":
    run()
