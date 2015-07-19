def comma(some_list):
    if(len(some_list)>1):
        return ', '.join(some_list[:-1]) + ' and ' + some_list[-1]
    return ''.join(some_list)

print(comma(['apples', 'bananas', 'tofu', 'cats']))
