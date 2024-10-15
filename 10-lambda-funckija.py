# lambda argumenti: izraz
def sabiranje(x):
    return x + 50
print(sabiranje(200))
print(sabiranje(500))

saberi = lambda x: x + 50
print(saberi(5))
print(saberi(50))

lambda_sabiranje = lambda a, b: a + b
print(lambda_sabiranje(100, 200))

x = lambda a,b,c: a - b - c
print(x(100,50,10))

def ispitaj_broj(x):
    if x % 2 != 0:
        return True
    else:
        return False
print(ispitaj_broj(100))
print(ispitaj_broj(103))

ispitaj_brojeve = lambda x: x % 2 != 0
print(ispitaj_brojeve(20))
print(ispitaj_brojeve(21))

lista_tuplova = [(1,5), (3,2), (4,1), (2,4)]
sortirano = sorted(lista_tuplova, key=lambda x: x[1])
print(sortirano)

lista = [5,17,32,12,15,62,237,244,76,21]
print(lista)
filtrirana_lista = list(filter(lambda x: (x % 5 == 0), lista))
print('Brojevi deljivi sa pet su: ', filtrirana_lista)

niz = ['python', 'PHP', 'Javascript', 'Java', 'SQL', 'Scala']
print(niz)
filtrirana_lista = list(filter(lambda x: (x[0].lower() == 'j'), niz))
print("Reci koje pocinju slovom P : ", filtrirana_lista)

def kvadriraj(broj):
    return broj**2
print(kvadriraj(2))
lista = [1,2,3,4,5,6,7,8,9,10]
print(map(kvadriraj, lista))
nova_lista = list(map(kvadriraj, lista))
print(nova_lista)

lambda_lista = list(map(lambda broj: broj ** 2, lista))
print(lambda_lista)

moja_lista = ['data analyst', 'data science', 'machine learning', 'ai']
mapirana_lista = list(map(lambda x: x[0].upper()+x[1:], moja_lista))
print(mapirana_lista)

from functools import reduce
lista = [1,2,3,4,5,6,7,8,9,10]
suma = reduce((lambda x, y: x + y), lista)
print("Suma elemenata liste je " , suma)

lista = [110, 53, 3, 424, 255, 16, 42, 256]
najveci_broj = reduce((lambda x, y: x if (x>y) else y), lista)
print('Najveci broj liste je: ', najveci_broj)

starost=37
poruka = "Punoletan(na) si " if starost >= 18 else "Maloletan(na) si"
print(poruka)

lista = ['Dragan','Marko', 'Jovan', 'Milica', 'Tamara', 'Slobodan']
filtrirana_lista = list(filter(lambda x: (x[-1] == 'a'), lista))
print("Imane koja zavrsavaju na slovo N su " , filtrirana_lista)
