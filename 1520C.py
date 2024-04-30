def print_matrix(matrix):
    if matrix == -1:
        print("-1")
    else:
        for row in matrix:
            row_str = ""
            for elem in row:
                row_str += str(elem) + " "
                row_str.strip()
            print(row_str)

def calculate(n):
    M = [[0] * n for _ in range(n)]
    
    M[0][0] = 1
    M[n-1][n-1] = 2
    
    k = 3
    for d in range(n + n - 1):
        for i in range(max(0, d - n + 1), min(n, d + 1)):
            j = d - i
            if i == 0 and j == 0:
                M[i][j] = 1
            elif i == n-1 and j == n-1:
                M[i][j] = 2
            else: 
                M[i][j]= k
                k+=1
    
    if n == 2:
        return -1
    else:
        return M
                
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
    print_matrix(calculate(num))