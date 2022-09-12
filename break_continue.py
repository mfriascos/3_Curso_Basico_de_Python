def run():
    
    # for i in range(1000):
    #     if i%2 != 0:
    #         continue
    #     print(i)
    
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    text = input('Type a text: ')
    for letter in text:
        if letter == 'o':
            continue
        print(letter)    

if __name__ == "__main__":
    run()