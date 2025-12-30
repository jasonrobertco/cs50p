name = input("What's your name? ").strip().title()

# split into first and last uses the space
first, last = name.split(" ")

# say hello to user
print(f"hello, {first}")