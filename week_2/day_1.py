# comparison use of comparing a value or data.

'''
== is equal
!= not equal
> greater than
< less than
> greater or equal to
< less than or equal to
'''
stored_value = 10
search_value = 4

# not Equal 
is_equal = stored_value == search_value
print("not equal:",is_equal)

#not equal to
is_equal = stored_value == search_value
print("not eqal to:", is_equal)

# greater than
greater_than = stored_value > search_value
print("greater than:", greater_than)

# less than
less_than = stored_value < search_value
print("less than:",less_than)

# greater than and equal to
greater_than_and_equal_to = stored_value >= search_value
print("greater than and equal to:",greater_than_and_equal_to)

# less than and equal to
less_than_and_equal_to = stored_value <= search_value
print("less than and equal to:", less_than_and_equal_to)

# ----- logical operators - are used to make more one comparison
""""
AND - checks both comparison are true
OR - checks which one them are true
NOT -(Negetion operator: makes the value the oposite)
"""
age = 20 
nysc = "done"

# AND OPERATION
is_one_true = age >= 20 and nysc =="done"
print("AND:",is_one_true)

# OR OPERATOR
is_one_is_true = age >= 20 or nysc =="in_transit"
print("OR:", is_one_is_true)

# NOT OPERATOR - gives the oposite value
value = False
negate_value = not value
print("not",negate_value)

print(True and True and True and False)

#-------- DATA STRUCTURES---------
'''
dictionary
lsit
tuple
set

'''
# -------STRINGS-------
# single qoute string - a single line
# double quote string - a single line
# triple single quote - multiple line
# triple double quote - multiple line
'''
\n - line character
\t - tab character
\\ - backslash
\b - erases charecter 
'''
sentence = '\tit was a rainy day\b day to day and a lot of people. \\just using a backslash here. got stuck from coming'
print(sentence)




      