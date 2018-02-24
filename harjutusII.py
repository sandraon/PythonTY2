from time import sleep
sisestatud_pin = ""
katseid = 3
while sisestatud_pin != "1234" and katseid > 0:
    print("Sisesta PIN-kood:")
    print("Jäänud on " + str(katseid) + " katset.")
    katseid -= 1
    sisestatud_pin = input()
if sisestatud_pin == "1234":
    print("Sisenesid pangaautomaati!")
else:
    print("Enesehävitusrežiim aktiveeritud:")
    i = 10
    while i > 0:
        print(i)
        i -= 1
        sleep(1)