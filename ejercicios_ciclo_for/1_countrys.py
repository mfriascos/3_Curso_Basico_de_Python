# Realice un programa que enumere los paises de la siguiente lista
#
# paises = ['Canada', 'USA', 'Mexico', 'Australia']

def run():
    paises = ['Canada', 'USA', 'Mexico', 'Australia']
    i = 1
    for pais in paises:
        print(str(i) + '. ' + pais)
        i = i+1
        

if __name__ == "__main__":
    run()