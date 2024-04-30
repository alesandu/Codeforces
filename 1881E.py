def calculate(arr,lun):
    var = [0]*(lun+1)
    for i in range(lun-1,-1,-1):
        if arr[i] >= lun-i:
            var[i] = var[i+1]+1
        else:
            var[i] = min(var[i+arr[i]+1],var[i+1]+1)
    return var[0]

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