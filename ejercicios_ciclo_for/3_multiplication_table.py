#Haz una tabla de multiplicar utilizando el ciclo for

def run():
    for i in range(11):
        for j in range(11):
            res = i*j
            print(str(i)+ "x" +str(j)+ " = " +str(res))
        

if __name__ == "__main__":
    run()