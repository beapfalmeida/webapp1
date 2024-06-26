temperatures = [10, 12, 14]

temperatures = [str(i) + '\n' for i in temperatures]
# IMPORTANTE - para escrever num textfile tem de ser strings

file = open("file.txt", 'w')
file.writelines(temperatures)