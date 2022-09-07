

def potencia(numero):
    i=0
    resultado = numero**i
    while resultado <100000:
        print("{}^{} = {}".format(numero,i,resultado))
        i=i+1
        resultado = numero**i
    

def run():
    base = int(input("Digite un número para cosultar sus potencias: "))
    potencia(base)
        

if __name__ == "__main__":
    run()