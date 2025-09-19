def faktoriyal(n):
    natija = 1
    for i in range(1, n+1):
        natija *= i
    return natija
son = int(input("Son kiriting: "))
print(f"{son} sonining faktoriyali = {faktoriyal(son)}")