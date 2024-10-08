# for <varijabla> in <niz>:
    # <blok koda>
for i in range(1,11,3):
    print(i)

brojevi = list(range(0,10))
print(type(brojevi))

x = []
for i in range(1,6):
    y = i ** 2
    x.append(y)
print(x)
print(max(x))
print(min(x))

brojevi = [1,2,3,4,5,6,7,8,9,10]
for broj in brojevi:
    print(broj)

print("______________________")

for broj in brojevi:
    print(broj * 3)

print("______________________")

for broj in brojevi:
    print(broj + 3)

print("______________________")

for x in brojevi:
    if x%2 == 0:
        print(f"Ispis parnog broja: {x}")
    else:
        print(f"Ispis neparnog broja: {x}")

print("______________________")

lista = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for broj in lista:
    suma = suma + broj
print(suma)

print("______________________")

string = "Python je fantastican jezik za programiranje"
for i in string:
    print(i, end="")

print("______________________")
band = ['lars', 'james', 'kirk', 'robert']
for member in band:
    print(f"{member.title()}, je clan benda Metallica")

print("______________________")
niz = [1,2,3,4,5,6,7,8,9,10]
broj = 5
for i in niz:
    if i == broj:
        print("Broj je pronadjen u nizu")
        break
else:
    print("Broj nije pronadjen")

print("______________________")
for broj in range(10):
    if broj % 2 == 0:
        continue
    print(broj)

print("______________________")
for broj in [2,4,6,8,10]:
    if broj % 3 == 0:
        print(f"Broj {broj} je deljiv sa 3")
        break
else:
    print("Nema broja deljivog sa 3")

print("______________________")
predavaci = {
    'Boban' : "Html i css",
    'Danijel': 'Javascript',
    'Jovana' : 'React',
    'Sloba Miric' : 'Python',
    'Milan' : 'Machine learning',
    'Milica' : 'Data analyst',
    'Sloba Zelic': 'Django'
}
for predavac in predavaci:
    # print(predavac)
    print(f"{predavac.title()} drago mi je da pronosis znanje WW polaznicima")