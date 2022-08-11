import pyperclip

l='* '+ pyperclip.paste()
l=l.split('\n')
if pyperclip.paste().endswith('\n'):
    del l[-1]
l='\n* '.join(l)
print(l)



'''
Lists of animals 
Lists of aquarium life 
Lists of biologists by author abbreviation 
Lists of cultivar
'''
'''
Lists of animals \n
Lists of aquarium life \n
Lists of biologists by author abbreviation \n
Lists of cultivar \n
'''