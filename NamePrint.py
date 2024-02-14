import pandas as pd
import re

name = input('What is your name? \n')

#pattern = r'^(\w).*(\s+\w+)$'
#initals = re.search(pattern, name)
#print((initals.group(1)+initals.group(2)+ " ") * 100)
f_i1, m_i1, l_i1 = name.split (' ', 2)
pattern = r'^(\w).*(\s+\w+)$'
f_i2 = re.search(pattern, f_i1)
m_i2 = re.search(pattern, m_i1)
l_i2 = re.search(pattern, l_i1)
print(f_i2+m_i2+l_i2+" "* 100)

# this is printing out the first inital, but returns the full name of the other string.
# Maybe I should split the string by spaces.
# I think I'm discovering why every last name form asks for seperate first middle, and last names.