# Imprima el siguiente patrón con el ciclo for:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

def run():
    print('')
    for i in range(5,0,-1):
        for j in range(i,0,-1):
            print(' ',end=str(j))
        print('\n')  
    


if __name__ == "__main__":
    run()