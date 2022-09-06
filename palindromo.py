def palindromo(frase):
    frase = frase.replace(' ','')
    frase = frase.lower()
    frase_inv = frase[::-1]

    if frase == frase_inv:
        return True
    else:
        return False


def run():                                          #Función principal
    frase = input('Escribe una frase: ')
    es_palindromo = palindromo(frase)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')
    

if __name__ =='__main__':
    run()

