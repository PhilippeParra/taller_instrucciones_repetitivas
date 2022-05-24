



X = int(input("Digite el valor de X: "))

N = 1
p1 = 0

while N <= X:
    P = X % N
    N = N + 1

    if P == 0:
        p1 = p1 + 1


print("---------------------------")
if p1 == 2:
    print("El numero dado es primo.")

else:
    print("El numero dado no es primo.")
print("---------------------------")