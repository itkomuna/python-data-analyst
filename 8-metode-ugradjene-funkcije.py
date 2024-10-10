import math
def pozdrav(ime):
    print(f"Zdravo, {ime}")

pozdrav('Amele')
pozdrav('Snezo')
pozdrav('Branislave')
pozdrav('Bojana')
pozdrav('Marko')

# ime = input('Unesite svoje ime: ')
# print('Dobrodosli', ime)

# godina_rodjenja = int(input("Unesite godinu rodjenja"))
# trenutna_godina = 2024
# godine = trenutna_godina - godina_rodjenja
# print("Imate ", godine, " godina")

python = "Zdravo svete"
print(len(python))
print(python.upper())

lista = [1,2,3,4,5]
print(type(lista))
lista.append(6)
lista.pop()
print(lista)

brojevi = [1,2,3,4]
ukloni_broj = brojevi.pop(1)
print(brojevi)
print(ukloni_broj)

brojevi = [1,2,3,4]
del brojevi[1:3]
print(brojevi)

brojevi = [1,2,3,2,4]
brojevi.remove(2)
print(brojevi)

# new_list = [expression for item in itrerable if condition]
numbers = [1,2,3,4,5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

matrica = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# for red in matrica:
#     for element in red:
#         print(element, end=" ")
#     print()

# new_list = [expression for item in itrerable if condition]
spajanje = [num for row in matrica for num in row]
print(spajanje)

brojevi = [1,2,3,4,5]
brojevi = [x for x in brojevi if x %2 != 0]
print(brojevi)

brojevi = [1,2,3,4,5]
neparni_brojevi = []
for x in brojevi:
    if x% 2 != 0:
        neparni_brojevi.append(x)
print(neparni_brojevi)

niz = [10, 20, 30, 40, 50]
print(min(niz))
print(max(niz))

stringovi = ['Tamara', 'Marko', 'Jovana', 'Slobodan']
print(min(stringovi))
print(max(stringovi))

array = ['Sneza', 40, True, 'Python']
# print(max(array))

x = round(9.876543)
x = round(9.876543,1)
x = round(9.876543,2)
print(x)

broj = 7.9
zaokruzi_nadole = math.floor(broj)
print(zaokruzi_nadole)
zaokruzi_nagore = math.ceil(broj)
print(zaokruzi_nagore)

mojtupl = (1,2,3,4,5,6,7,8,9,10)
print(mojtupl)
zbroji = sum(mojtupl)
print(zbroji)

mojalista = [1,2,3,4,5,6,7,8,9,10]
saberi = sum(mojalista)
print(saberi)

lista = [2,4,1.44,4/3, 3.14,2,18.19]
suma = sum(lista)
suma = round(sum(lista), 3)
print(suma)

x = pow(2,3)
print(x)

lista = [10, 67, 270, 149, 14]
print(sorted(lista))

print(lista)

nova_lista = sorted(lista)
print(nova_lista)

obrni_listu = sorted(nova_lista, reverse=True)
print(obrni_listu)

# rezultat = input("Unesi ime: ")
# print("Dobrododao " + rezultat + " na Python data analyst kurs")
# print(type(rezultat))

from random import shuffle
lista = [1,2,3,4,5,6,7,8,9,10]
shuffle(lista)
print(lista)

voce = ['banana', 'jagoda', 'ananas', 'jabuka', 'sljiva', 'visnja']
shuffle(voce)
print(voce)

from random import randint
broj = randint(0,100)
print(broj)

from random import choice
smuti = ['banana', 'jabuka', 'kruska', 'malina', 'sojino mleko', 'jogurt']
element = choice(smuti)
print(element)