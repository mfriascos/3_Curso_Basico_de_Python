# Hanged Game
import random 

def comparar_palabras(word,s_word):
    letter = input('Type a letter: ')
    list_oculta = palabra_oculta(s_word)
    palabra = list(word)
    print(list_oculta)
    print(palabra)

    for i in word:
        if letter == i:      
            pos_letra_correcta = word.find(i)
            list_oculta[pos_letra_correcta] = letter.upper()
            print(list_oculta)
            True
        else:
            False
            

def palabra_oculta(s_word):
    oculta = []
    for i in range(s_word):
        oculta.insert(i,'X')
    #oculta = " ".join(oculta)
    #print(oculta)   
    return oculta


def get_word():
    my_words = ('terminal','code','devops','github','python','tuplas')
    item = random.randint(0,5)
    the_word = my_words[item]
    return the_word


def run():

    attempts = 6
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

    print('')
    print(word)
    print('')

    comparar_palabras(word,s_word)
    
            
            




if __name__ == "__main__":
    run()