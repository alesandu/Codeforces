def calculate(num):
    lista = []
    x = 0
    lun = len(str(num))
    for i in range(1,lun+1):
        for j in range(1,10):
            b = int(str(j)*i)
            lista.append(b)
    for i in lista:
        if i<=num:
            x+=1
    return x
                
def prendi():
    numTest = int(input())
    listaPar = []
    for _ in range((numTest)):
        a = int(input())
        listaPar.append(a)
    return listaPar

listaPar = prendi()

for test in range(len(listaPar)):
    num = listaPar[test]
    print(calculate(num))