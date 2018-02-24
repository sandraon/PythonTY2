print("Sisestage ridade arv:")
ridade_arv = int(input())
arv = 1
summa = 0

while ridade_arv >= arv:
    summa = summa + arv
    arv = arv + 1
print(summa)