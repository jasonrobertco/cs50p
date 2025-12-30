# ask user for their name
name = input("What's your name? ")


"""
anything in between here is a comment
"""

# say hello to user
"""
# print("hello, " + name) # concatenate
# print("hello, ", name) # multiple arguments auto add 1 space
"""
# print("hello, ", end="???")
# overwrote sep
print("hello, ", name, sep=' ')

#corner case with quotation
print("hello, \"friend\"")
