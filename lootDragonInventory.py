__author__ = 'cbartel'


def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print('Total number of items: ' + str(itemTotal))


def addToInventory(inventory, addedItems):
    count = {}
    for item in addedItems:
        count.setdefault(item, 0)
        count[item] += 1
    for k, v in count.items():
        if k in inventory.keys():
            inventory[k] += v
    return inventory

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
