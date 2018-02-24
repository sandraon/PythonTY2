import re

print("Sisesta postiindeks:")
postiindeks = input()

indeks = "^[1-9][0-9]{4}$"
if re.search(indeks, postiindeks):
    print("On Eesti postiindeks")
else:
    print("Ei ole Eesti postiindeks")