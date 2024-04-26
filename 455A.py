lista = []
x = int(input())
y = input().split()

#a
for car in y:
    i = int(car)
    lista.append(i)

a = max(lista)
a = a+1
cnt = [0]*(a)
for element in lista:
    cnt[element] += 1 

opt = [0]*(a)
for element in range(a):
    opt[element] = max(cnt[element]*element + opt[element-2], opt[element-1])
        
print(opt[a-1])
