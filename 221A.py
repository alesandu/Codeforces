lista = []

def f(y):
    lista = list(range(1,y))
    lista.insert(0,y)
    return lista

y = int(input())
    
a = f(y)
stri = ""

for elem in a:
    stri += str(elem)
    stri += " "
    
print(stri)