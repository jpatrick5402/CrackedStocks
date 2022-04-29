with open("file.txt", "r") as f:
    fstring = f.read()

a = fstring.split("$")

for index in a:
    b = index[-6:-1].strip(" ")
    print(b)
