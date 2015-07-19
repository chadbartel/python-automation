
def collatz(number):
    if number % 2:
        return 3 * number + 1
    return number // 2

def recursive_collatz():
    num = int(input("Enter number: "))
    print(num)
    while num > 1:
        num = collatz(num)
        print(num)

recursive_collatz()
