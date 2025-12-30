def hello(to = "world"): #goes to world by default
    #everything indented is part of this function
    print("hello,", to)



# create a function with def
hello()
name = input("What's your name? ")
hello(name)