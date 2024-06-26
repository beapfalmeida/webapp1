files = [r"C:\Users\beatr\Downloads\a.txt",r"C:\Users\beatr\Downloads\b.txt",r"C:\Users\beatr\Downloads\c.txt"]

for file in files:
    doc = open(f"{file}",'r')
    content = doc.read()
    print(content)
