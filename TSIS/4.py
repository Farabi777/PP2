n = int(input())
def pir(n):
    for i in range(n):
        for j in range (2 * n):
            if j >= n-i and j<=n+i:
                print("*", end ='')
            else:
                print(" ", end ='')    
        print()   
pir(n)   