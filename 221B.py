n = int(input())
ris = 0

for i in range(1,int(n**.5) +1):
    if n % i == 0: #if number is divisor
        ris += int(any(j in str(n) for j in str(i))) #add
        tmp = n//i #divide number by divisor
        if i != tmp:
            ris  += int(any(j in str(n) for j in str(tmp))) #add
 
print(ris)

#100: 1 100, 2 50, 3, 4 25, 5 20, 6, 7, 8, 9, 10 10