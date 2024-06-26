#bonus example dia 5
filenames = ['doc.text','report.txt','presentation.txt']
content = "Hello"

for filename in filenames:
    file = open(f"{filename}",'w') #se o documento não existir não podemos abrir em modo read, tem de ser write para o criar
    file.writelines(content)
    file.close() #outra coisa - atenção à f-string !

