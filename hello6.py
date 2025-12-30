def main():
    name = input("What's your name? ")
    hello(name)

def hello(to = "world"): #goes to world by default
    #everything indented is part of this function
    print("hello,", to)

main()