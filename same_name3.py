def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bagon'

def ham():
    print(eggs)

eggs = 42
print(eggs)
spam()
print(eggs)
