names = []
user_prompt = input("Enter a new member: ") + '\n'
user_prompt = user_prompt.title()

file = open(r'C:\Users\beatr\Downloads\members.txt', 'r') #importante colocar o r antes do path do ficheiro!
names = file.readlines()
file.close()

names.append(user_prompt)

file = open(r'C:\Users\beatr\Downloads\members.txt', 'w')
file.writelines(names)
file.close()
