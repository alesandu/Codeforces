def contest(a,b,c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    m = max(3/10*a,a-a/250*c) 
    v = max(3/10*b,b-b/250*d)
    if(m>v):
        print("Misha")
    elif(m<v):
        print("Vasya")
    else:
        print("Tie")

a,b,c,d = input().split()
contest(a,b,c,d)
