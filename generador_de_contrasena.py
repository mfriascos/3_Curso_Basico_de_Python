import random


def password_generator():

    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}',
             ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    char_t = MAYUS + MINUS + NUMS + CHARS

    passwd = []

    for i in range(15):
        char_random = random.choice(char_t)
        passwd.append(char_random)

    passwd = ''.join(passwd)                            #Método Para Convertir una lista a un String 

    return passwd


def run():
    password = password_generator()
    print('')
    print('Your new password is: ' + password )
    print('')


if __name__ == '__main__':
    run()
