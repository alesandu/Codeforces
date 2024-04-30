
numTest = int(input())

listaNum = []
listaCarte = []
listaRis = [0]*numTest

for _ in range((numTest)):
    a = int(input())
    listaNum.append(a)
    b = input().split()
    c = []
    for car in b:
        c.append(int(car))
    listaCarte.append(c)
    
for test in range(len(listaNum)):
    listaGioco = [0] * (max(listaCarte[test])+1)
    for i in range(len(listaCarte[test])):
        listaGioco[listaCarte[test][i]] += 1    
    for x in listaGioco:
        if x == 2:
            listaRis[test] += 1 

for x in listaRis:
    print(x)
    
    
