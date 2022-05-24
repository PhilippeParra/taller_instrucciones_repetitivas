

X = int(input("Digite la cantidad de veces a girar el dado: "))
from random import Random
import random
i = 1
n = 0

while ( i <= X):
    numero = random.randint(1 , 6)
    print(str(numero))
    i = i +1
    if numero == 3:
        n = n + 1

print("---------------------------------------")
if n == 1:
    print("El numero 3 a salido" , n , "vez.")
else:
    print("El numero 3 a salido" , n , "veces.")

print("---------------------------------------")
