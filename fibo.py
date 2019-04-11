def fibo(n):
    tab=[0]*(n+1)
    tab[1]=1
    for i in range(2,n+1):
        tab[i]=tab[i-1]+tab[i-2]
    return tab
#print(fibo(500))

def fibor(n):
    i=0
    if i==0:
        tab=[0]*(n+1)
        tab[1]=1
    elif i<n:
        return tab
    else:
        tab[i]=tab[i-1]+tab[i-2]
        i+=1
        fibor(i)
print(fibo(10))
