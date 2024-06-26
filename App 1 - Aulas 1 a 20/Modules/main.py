import glob

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().title())

# faz uma lista dos ficheiros terminados em .txt
# útil se quisermos fazer um loop over todos os ficheiros deste tipo
