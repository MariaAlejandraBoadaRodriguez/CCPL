dp = [0] * 100001

def costo_iterativo(alturas, n):
    i = 0
    #for i in range(n + 1):
    while i <= n:
        if i == 0 or i == 1:
            dp[i] = 0
        elif i == 2:
            dp[i] = abs(alturas[i]-alturas[i-1])
        else:
            dp[i] = min(abs(alturas[n]-alturas[n-1])+dp[n-1],abs(alturas[n]-alturas[n-2])+dp[n-2])
        i = i + 1
    return dp[n]

def costo(alturas, n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return abs(alturas[n]-alturas[n-1])
    else:
        return min(abs(alturas[n]-alturas[n-1])+costo(alturas,n-1),abs(alturas[n]-alturas[n-2])+costo(alturas,n-2))

n = int(input())
stones = input().split()
alturas = [0]
for i in range (len(stones)):
    alturas.append(int(stones[i]))
print(costo(alturas, n))