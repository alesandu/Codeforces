'''
def calculate(n, c, d, Mat):
    x = min(Mat)
    t = x - d
    removed_elements = []
    for j in range(n):
        x = t + d
        for i in range(1, n):
            a = x + c * i
            if a in Mat:
                removed_elements.append(a)
            else:
                return 0
        t = x
        removed_elements.append(x)
    return removed_elements

def check(m ,a, b):
    n = m*m
    if a == 0:
        return 0
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] != b[i]:
            return 0
    return 1
    
    
def prendi():
    numTest = int(input())
    listaPar = []
    listaMat = []
    for _ in range((numTest)):
        a = input().split()
        b = input().split()
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        listaPar.append(a)
        listaMat.append(b)
    return listaPar, listaMat

listaPar, listaMat = prendi()
listaRis = ""
    
for test in range(len(listaPar)):
    n = listaPar[test][0]
    c = listaPar[test][1]
    d = listaPar[test][2]
    x = calculate(n,c,d,listaMat[test])
    y = check(n,x,listaMat[test])
    if y == 1:
        listaRis += "YES\n"
    else:
        listaRis += "NO\n"
   

print(listaRis)

time exceeded code
'''


'''
code by IonutZbir
'''
import pprint as pp

def get_input() -> list:
    tests = int(input())
    inputs = []
    for _ in range(tests):
        n, c, d = input().split(" ")
        arr_as_strings = input().split(" ")
        arr = [int(num) for num in arr_as_strings]
        
        inputs.append((int(n), int(c), int(d), arr))
    return inputs
    

def create_progressive_square(n: int, a_11: int, c: int, d: int) -> list:
    m = [[0] * n for _ in range(n)]
    b = []
    
    m[0][0] = a_11
    
    for i in range(n - 1):
        for j in range(n):
            m[i + 1][j] = m[i][j] + c
            
    for i in range(n):
        for j in range(n - 1):
            m[i][j + 1] = m[i][j] + d
    
    for i in range(n):
        for j in range(n):
            b.append(m[i][j])

    b.sort()
    return b

def check(a: list, b: list):
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            return "NO"
    return "YES"

inp = get_input()
for n, c, d, arr in inp:
    arr.sort()
    b = create_progressive_square(n, arr[0], c, d)
    res = check(arr, b)
    print(res)