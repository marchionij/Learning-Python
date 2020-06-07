# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# # re-declaring the variable works
f="abc"
print(f)


# # ERROR: variables of different types cannot be combined
print("this is a string " + str(123))



# Global vs. local variables in functions
def someFunction():
    # global f 
    # Use if you want to make f a global variable
    # AKA the function will change the value of f EVERYWHERE
    f = "def"
    print(f)

someFunction()
print(f)

# del f
# print (f)
# Use del to delete the value of a variable
# In this case, it will cause an error when printing f because f has no definition