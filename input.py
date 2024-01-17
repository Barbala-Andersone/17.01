r=input("Ieraksti savu vārdu un uzvārdu: ")

with open("ziema.txt", "w", encoding="utf8") as l:
    l.write(r)
