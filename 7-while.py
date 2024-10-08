a = 1
while a < 10:
    print(a)
    a = a + 1  # a += 1

b = 10
while b <= 15:
    print(f"Trenutna vrednost B je: {b}")
    b += 1 

lista = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1

telefoni = ('iphone', 'samsung', 'nokia', 'honor', 'huawei')
i = 0
while i < len(telefoni):
    print(telefoni[i])
    i = i + 1

i = 5
while i < 10:
    i = i + 1
    if i == 7:
        continue
    print(i, end=" ")

brojac  = 0
while brojac < 5:
    print("Trenutna vrendost brojaca:", brojac)
    brojac += 1
else:
    print("Petlja je zavrsena, konacna vrednost brojaca je: ", brojac)

brojac = 0
while True: 
    print("Trenuta vednost brojaca je: ", brojac)
    brojac += 1
    if brojac == 5:
        break

brojac = 0
while brojac < 10:
    brojac += 1
    if brojac % 2 == 0:
        continue
    print(brojac)