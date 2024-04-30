def calculate(job,lun):
    jobsdone = [0]
    for i in range(1,lun):
        if (job[i] != job[i-1]) and (job[i] in jobsdone):
            return "NO"
        elif (job[i] != job[i-1]) and (job[i] not in jobsdone): 
            jobsdone.append(job[i-1])
    return "YES"
                
def prendi():
    numTest = int(input())
    listaPar = []
    listaStr = []
    for _ in range((numTest)):
        a = int(input())
        b = input()
        listaPar.append(a)
        listaStr.append(b)
    return listaPar, listaStr

listaPar, listaStr = prendi()

for test in range(len(listaPar)):
    job = listaStr[test]
    lun = listaPar[test]
    print(calculate(job,lun))