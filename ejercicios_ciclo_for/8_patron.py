#Imprima el siguiente patrón con el ciclo for:
#
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def ch(i):
    h = '*'*i
    return h


def run():
    for i in range(1,6):
        print(ch(i))
    for j in range(4,0,-1):
        print(ch(j))
        

if __name__ == "__main__":
    run()

