def comma(some_list):
    result = ''
    for count, i in enumerate(some_list):
        if count < len(some_list) - 1:
            result += i + ', '
        else:
            result += 'and ' + i
    return result

print(comma(['apples', 'bananas', 'tofu', 'cats']))
