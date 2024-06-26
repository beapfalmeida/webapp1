from parser14 import parse
from convert14 import convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

meters = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {meters} meters")

if meters < 1:
    print("Kid's too small.")
else:
    print("Kid can use the slide.")
