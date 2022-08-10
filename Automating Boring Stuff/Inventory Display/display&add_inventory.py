from collections import Counter #_Used for converting list value into a dictionary

def displayInventory(inventory): #_Takes in dictionary and prints the total number of item(s)
    total = 0
    for x, y in inventory.items(): #_x, y == key, value of dictionary
        if y > 1:
            print(str(y)+' '+x+'(s)') #_prints the plural form
        else:
            print(str(y)+' '+x)
        total += y # summation of values of the dictionary
    print('total = ' + str(total) + ' (items)')
    
def addToInventory(inventory, addedItems): #_Takes in dictionary & list respectively to return a dictionary
    addedItems = Counter(addedItems) #_converts list to a grouped dictionary(i.e 'string': 'number of times it appeared')
    
    for k in addedItems.keys(): #_stores items from the 2nd dict to the 1st if item is not found in it
        if k not in inventory.keys():
            inventory.setdefault(k, 0) #_This sets the value item stored to 0
    for z in inventory.keys(): #_stores items from the 1st dict to the 2nd if item is not found in it
        if z not in addedItems.keys():
            addedItems.setdefault(z, 0) #_This sets the value item stored to 0
    count = {}
    #_Main Engine
    # Compares the items in 1st & 2nd dict, if all conditions are met, it prints saves the current version of the items in count{}
    # Therefore, count will look something like this: count = {'key1': 'value1, 'key2': 'value2, 'key(n+1)': 'value1(n+)}
    for x, y in inventory.items():
        for z, u in addedItems.items():
            if x == z:    
                count.setdefault(x, 0) #_stores item key in count with value 0 
                count[x] = count[x] + (y+u) #_adds item's value to the count, In summary, changes the value of each item in the count from 0(initial value) to its final value
    return count

# Test

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)





















'''


#total = 0
#print(inv)
#for x, y in inv.items():
    #if y > 1:
       # print(str(y)+' '+x+'s')
    #else:
       # print(str(y)+' '+x)
    #total += y 
#print('total = ' + str(total))
from collections import Counter
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = Counter(['gold coin', 'dagger', 'dagger', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope', 'rope', 'rope'])
#print(dragonLoot)

#for i in dragonLoot.values():
   # print(i)

ting = 0
for k in dragonLoot.keys():
    if k not in inv.keys():
        inv.setdefault(k, 0)

for x, y in inv.items():
    
    print('-----------------------------------------------------------------------')
    print('x= '+ str(x) + ' y= ' + str(y))
    for z, u in dragonLoot.items():
        print('x= '+ str(x) + ' y= ' + str(y) + ' z= '+ str(z))
        if x == z:
            print('if x == z:')
            print('x= '+ str(x) + ' y= ' + str(y) + ' z= '+ str(z))
            print('dragonLoot.values()= '+ str(dragonLoot.values()) + ' u= '+ str(u))
            print('dragonLoot.keys()= '+ str(dragonLoot.keys()) + ' z= '+ str(z))
            print('x= '+ str(x) + ' z= ' + str(z) + ' u= '+ str(u))
            print('sirrr'+ str(y + u))'''