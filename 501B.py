def get_key(my_dict,val):
    for key, value in my_dict.items():
        if val == value:
            return key

numero_persone = int(input())

persone = {}
listanomi = []

for i in range(numero_persone):
    x,y = input().split()
    listanomi.append(y)
    if(x in listanomi):
        t = (get_key(persone,x))
        persone.pop(t)
        persone[t]=y
    else:
        persone[x]=y
    
number = len(persone.keys())
stringa = ""
for i in range(number):
    a,b = persone.popitem()
    stringa += a+" "+b+"\n"
    
print(str(number)+"\n"+stringa) 