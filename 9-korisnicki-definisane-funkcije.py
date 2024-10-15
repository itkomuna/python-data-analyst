# def moja_funckija():
#     print("Pozdrav iz funkcije")
# moja_funckija()

# def sabiranje(broj1,broj2):
#     return broj1 + broj2
# rezultat = sabiranje(10, 30)
# print(rezultat)

# def povrsina_kruga(r):
#     povrsina = 3.14 * r * r
#     print(povrsina)
# povrsina = povrsina_kruga(2)
# # print(povrsina)

# def povrsina_kruga(r):
#     povrsina = 3.14 * r * r
#     return povrsina
# povrsina = povrsina_kruga(4)
# print(povrsina)

# def podeli(a,b):
#     if b == 0:
#         print('Nije dozvoljeno deljenje sa nulom')
#         return
#     rezultat = a / b
#     return rezultat
# print(podeli(100,5))
# print(podeli(100,0))

def lokalne_varijable():
    x = 100
    print(x)
lokalne_varijable()
# print(x)

y = 29
def globalne_varijable():
    print(y)
globalne_varijable()

z = 20
def moja_funkcija():
    global z
    z = 60
moja_funkcija()
print(z)

# z = 100
# def amelova_f():
#     print(z)
# amelova_f()

def uporedi(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print('Brojevi su jednaki')
        return x
print(uporedi(30,30))

def odakle_si(drzava='Njemacka'):
    print('Moja rodna gruda je ' + drzava)
odakle_si('Hrvatska')
odakle_si('Srbija')
odakle_si('BIH')
odakle_si()

def puno_ime(ime, prezime):
    print(ime + " " + prezime)
puno_ime('Amel', 'Omanovic')
puno_ime('Sandra', 'Cirkovic')
puno_ime('Svetlana', 'Stojnovic')

def porodica(*clan):
    print('Danas su na redu za usisavanje ' + clan[0] + ' i ' + clan[3])
porodica('Tamara', 'Jovana', 'Mirka', 'Dragica')

