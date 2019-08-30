lists=["Nogizaka46","Keyakizaka46","Hinatazaka46"]

print(lists)

dicts={lists[0]:"Mai Shiraishi",lists[1]:"Yurina Hirate",lists[2]:"Nao Kosaka"}

a=input("""Do you like 46-Groops?
Which groop do you like?
I show you its center member!!:""")

if a in dicts:
    center=dicts[a]
    print(center)
else:
    print("It's Yosimotozaka46!!")
