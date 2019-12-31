f = open("veriler")

for line in f :
    print(line.strip())
f.close()

with open("veriler") as f :
    for line in f:
        print(line.strip())
f.close()