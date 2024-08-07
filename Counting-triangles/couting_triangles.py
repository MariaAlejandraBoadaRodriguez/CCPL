t = int(input())

def counting_triangles():
    [n, k] = [int(x) for x in input().split()]
    vertical = n + 1
    horizontales = k + 1
    suma = (vertical * (vertical + 1)) // 2 
    
    resultado = (suma * horizontales) % 1000000007
    print(resultado)

while t > 0:
    counting_triangles()
    t -= 1