def greeting(person):
    return f"Hi {person}"


greeting = greeting(input("Enter your name: "))
print(greeting)


def greeting(name):
    return f"Hi {name}"


greeting = greeting("What's your name?")
print(greeting)