# Hanged Game
import random 
import os


def palabra_oculta(s_word):
    oculta = []
    for i in range(s_word):
        oculta.insert(i,'X')   
    return oculta


def get_word():
    my_words = ('terminal','code','devops','github','python','tuplas')
    item = random.randint(0,5)
    the_word = my_words[item]
    the_word = "".join(the_word)
    return the_word


def run():
    cont = 1
    word = get_word()
    s_word = len(word)
    h_word = s_word*'X'
    print ("""
                H A N G E D    G A M E 

                ............(0 0)
                    .---oOO-- (_)-----.
                    ╔═════════════════╗
                    {}       {}    
                    ╚═════════════════╝
            ----------------------oOO
                    ........|__|__|
                .......... || ||
                ||||....... ooO Ooo 
            """.format('║',h_word))
    

    # print('')
    # print(word)
    print('')
    list_oculta = palabra_oculta(s_word)
    palabra = list(word)
    cont = 0
    cont2 = 0
    while True:

        while list_oculta != palabra: 
            letter = input('Type a letter: ')
            os.system("clear")
            flag = False

            for i in palabra:
                if letter == i:      
                    pos_letra_correcta = word.find(i)
                    list_oculta[pos_letra_correcta] = letter
                    flag = True

            if flag == True:
                cont2 = cont2+1
                list_oculta
            else:
                list_oculta
                print('Error! Intenta con otra letra')
                print('Te quedan {} intentos'.format(5-cont))
                cont = cont+1
                if cont == 6:
                    break
                                   
            list_develada = " ".join(list_oculta)
            list_develada = list_develada.upper()
            print ("""
                H A N G E D    G A M E 

                ............(0 0)
                    .---oOO-- (_)-----.
                    ╔═════════════════╗
                    {}   {}    
                    ╚═════════════════╝
            ----------------------oOO
                    ........|__|__|
                .......... || ||
                ||||....... ooO Ooo 
            """.format('║',list_develada))

            if cont2 >= 3:
                print('')
                print('conoces la palabra, te animas a escribirla ? Y/N')
                resp = input()
                if resp == 'Y' or resp == 'y':
                    texto = input('Digita la palabra: ')
                    texto = texto.lower()
                    texto = list(texto)
                    if texto == palabra:
                        word = list(word)
                        word = " ".join(word)
                        os.system("clear")
                        print('¡Felicitaciones, Ganaste!')
                        print ("""
                                H A N G E D    G A M E 

                                ............(0 0)
                                    .---oOO-- (_)-----.
                                    ╔═════════════════╗
                                    {}   {}    
                                    ╚═════════════════╝
                            ----------------------oOO
                                    ........|__|__|
                                .......... || ||
                                ||||....... ooO Ooo 
                            """.format('║',word.upper()))
                        break 
                    else:
                        print('Palabra incorrecta, la palabra es {} '.format(word.upper()))
                        break

        break
    print('Game Over')

if __name__ == "__main__":
    run()