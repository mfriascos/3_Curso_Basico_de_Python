# Mostrar series de Fibonacci hasta 10 términos 

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)


def run():

    for x in range(11):
        print(fib(x))

if __name__ == "__main__":
    run()