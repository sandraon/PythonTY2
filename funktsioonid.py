def välgu_kaugus(kaugus): 
    valem = round(kaugus * 300 / 1000)
    return valem

print("Mitu sekundit kulus välgu nägemisest müristamise kuulmiseni?")
aeg = float(input())

kauguskm = välgu_kaugus(aeg)
print("Välgulöögi kaugus kilomeetrites:", kauguskm)


