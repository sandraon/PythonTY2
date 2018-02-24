def välgu_kaugus(kaugus): 
    valem = round(aeg*330/1000)
    return valem

print("Mitu sekundit kulus välgu nägemisest müristamise kuulmiseni?")
aeg = int(input())

print("Välgulöögi kaugus kilomeetrites: " + str(välgu_kaugus(aeg)))


