x = 0
if x == True:
    print(True)
else:
    print(False)

x = 100
y = 20
if x < y:
    print('Izraz je tacan X je veci od Y')
else:
    print('Izraz je netacan X je manji od Y')

year = 2020
if (year == 2024):
    print("Trenutno je godina: 2024")
else:
    print("Trenutna godina nije 2024")

godisnji = True
if godisnji == True:
    print("Uzivaj dok odmaras i nemoj se nervirati")
else:
    print('Strpi se jos malo pa ce nova godina tu cemo da stponemo nedelju dve')

x = 9
if(x%2 == 0):
    print('Broj je paran')
else:
    print('Broj je neparan')


a = 290
b = 2090
if a < b:
    print('A je manje od B')
elif a == b:
    print('A i B su jedanki')
else:
    print('A je vece od B')

temperatura = 2
if temperatura > 30:
    print('Sorc i papuce su resenje')
elif temperatura > 20:
    print('Fino je napolju ako nema vetra moze i kratka majica')
elif temperatura > 15:
    print('Nije hladno previse, neki dobar duks resava stvar')
else:
    print('Ladnoca brale obuci se dobro')


rezultat_testa = 45
if rezultat_testa > 90:
    print("ovo je odlican rezultat odlicno si se spremio/la")
elif(rezultat_testa >= 70 and rezultat_testa <= 90):
    print("Skroz dobar rezultat cestitam")
elif(rezultat_testa >= 50 and rezultat_testa <= 70):
    print('Prosao si ali moze i bolje')
else:
    print('Pojma nemas nauci za sledeci put')

# WHILE
broj = 1
while broj <= 10:
    print(broj)
    broj += 1 # broj = broj + 1

limit = 10
counter = 1
while(counter <= limit):
    print(counter)
    counter += 1
print(counter)

# FOR
brojevi = [1,2,3,4,5]
for broj in brojevi:
    print(broj * 2)

print(1*2)
print(2*2)
print(3*2)
print(4*2)
print(5*2)
# print(brojevi)
# for i in range(1,6):
#     print(i)


# for($i=1;$i<count($brojevi);$i++) {
#     echo $brojevi[$i] * 2;
# }

# const brojevi = [1,2,3,4,5];
# for(let broj of brojevi) {
#     console.log(broj *2)l
# }