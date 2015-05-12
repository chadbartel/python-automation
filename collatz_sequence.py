def collatz(number):
    if number % 2 == 0:
        return int(number // 2)
    else:
        return int(3 * number + 1)

def recursive_collatz():
    print("Enter number:")
    try:
        num = int(input())
        collatz_num = collatz(num)
        print(collatz_num)
        while collatz_num != 1:
            collatz_num = collatz(collatz_num)
            print(collatz_num)
    except ValueError as ve:
        print('ERROR:', ve)

recursive_collatz()
