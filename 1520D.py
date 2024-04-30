"""
def calculate(arr,lun):
    t = 0
    for i in range(lun):
        for j in range(i+1,lun):
            if(arr[i]-arr[j] == i-j):
                t+=1
    return t
    
time limit exceeded
"""
    
def prendi():
    numTest = int(input())
    listaPar = []
    listaArr = []
    for _ in range((numTest)):
        a = int(input())
        b = input().split()
        b = [int(x) for x in b]
        listaPar.append(a)
        listaArr.append(b)
    return listaPar, listaArr

listaPar, listaArr = prendi()

for test in range(len(listaPar)):
    arr = listaArr[test]
    lun = listaPar[test]
    print(calculate(arr,lun))