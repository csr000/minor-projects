import re

pwd  = re.compile(r'''
                  
                  ^
                  
                  
                  
                  
                  (?=.*\w)[\S+]
                  {6,20}
                  $
                  
                  ''', re.VERBOSE)

matches = pwd.findall('skrr33333rrr')
#for match in matches:
print(matches)

'''
                  ^
                  (?=.*[a-z])
                  (?=.*[A-Z])
                  (?=.*\d)
                  (?=.*[@$!%*#?&])
                  [A-Za-z\d@$!#%*?&]
                  {6,20}
                  $
'''





'''
strong pwd detector
====================
musthave
--------
at least 8 characters
upper n lowercase
a digit



'''