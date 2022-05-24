



X = int(input("Digite el valor de X: "))

N = 1
X1 = X -1
X2 = X

if X > 0:
    while N <= X1:
        X2 = X2 * N
        N = N + 1

print("-------------------------------")
print("El factorial del numero " , X , "\nes: " , X2)
print("-------------------------------")