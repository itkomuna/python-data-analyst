print('Ja sam string')
print("I ja sam string")

print("I'm ukulele player and I also played the harmonica")
print("I\"m ukulele player and I also played the harmonica")

guitar = 'Fender stratocaster'
print(guitar)

car = "Renault Clio"
#      01234567891011
auto = "R    e    n   a   u   l    t"
#       0   -6   -5  -4  -3  -2   -1
print(auto[-1])

##################
#  SLICING
##################
# string[start : stop : step]
kurs = 'Python kurs'

# osnovni slicing
print(kurs[0:6:2])

print(kurs[7:11])

# Slicing bez starta i stopa
print(kurs[:7]) 
print(kurs[:]) # sve

# korak u slicingu
print(kurs[::2])

# obrnuti slicing
print(kurs[::-1])

# negativni indexi
print(kurs[-1:])
print(kurs[-4:])
print(kurs[-12:])

print(kurs[12:6:-1])
print(kurs[-1:-5:-1])


brojevi = list(range(0,11))
print(brojevi)
print(brojevi[0:11:2])
print(brojevi[0:11:3])

user = 'Sloba'
print("Dobrodosao " + user + " na na su aplikaciju")

print("Sloba ima {} godina".format(47))

print("{0} {2} {1}".format('setanje psa', 'aktivnost', 'je moja glavna'))

print("{s} ima hobi i to su {u} i {h}".format(u = 'ukulele', s = 'Sloba', h = 'usna harmonika'))


ljubimac = 'Freeda'
starost = 4
print(f"Moj ljubimac je pas {ljubimac} i ima {starost} godine")