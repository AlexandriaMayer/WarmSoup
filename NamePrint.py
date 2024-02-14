import pandas as pd
import re

f_name = input('First Name \n')
m_name = input('Middle Name \n')
l_name = input('Last Name \n')

#pattern = r'^(\w).*(\s+\w+)$'
#initals = re.search(pattern, name)
#print((initals.group(1)+initals.group(2)+ " ") * 100)
pattern = r'^(\w).*(\s+\w+)$'
fi = re.search(pattern, f_name)
mi = re.search(pattern, m_name)
li = re.search(pattern, l_name)

print(fi+mi+li+" "* 100)

# this is printing out the first inital, but returns the full name of the other string.
# Maybe I should split the string by spaces.
# I think I'm discovering why every last name form asks for seperate first middle, and last names.
