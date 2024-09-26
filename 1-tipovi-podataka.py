#################
# TIPOVI PODATA #
#################

#   NAME               TYPE
# integers             int         brojevi  2,9,90
# floating points      float       decimalne vrednosti pi = 3.14
# strings              str         uredjena sekvenca karaktera   'neki tekst'
# booleans             bool        logicke vrednosti True i False
# lists                list        uredjena sekvenca objekat, kada zelim da skladistimo vise varijabli ['snjeza', 'milica', 3.14, True]
# dictionaries         dict        neuredhjene lista key value parova
# tuples               tup         uredjene imutabilna sekvenca objekata     
# sets                 set         neuredjena kolekica unique vrednosti      

print(type('sloba'))   # type()

a = str('Python')
print(type(a))

b = int(' 30 ')
print(b)

#################
#    INTEGERS   #
#################
a = 5
b = str(100)
c = 1000
print(type(b))
print(a + int(b) + c)

print(20//5)
print(type(20/5))

#################
#    FLOAT      #
#################
pi = 3.14
print(type(pi))
x = int(3.9)
print(type(x))
print(x)

#################
#    COMPEX     #
#################
x = 2 + 3j
print(type(x))

#################
#    STRINGS    #
#################
a = 'string'
b = "STRING"
c = ''' DOCSSTRING'''
print(type(a))
d = str(300)
print(type(d))

print('Hello ' + ' World')
ime = 'Jovan'
prezime = 'Jovanovic'
print(ime + ' ' + prezime)
puno_ime = ime + " " + prezime
print(puno_ime)

# join()
delovi_imena = ['Nikola', 'Tesla']
puno_ime = " / ".join(delovi_imena)
print(puno_ime)

# f string
ime = 'Sloba'
godine = 47
opis = f"Moje ime je {ime} i imam {godine} godina"
print(opis)

# format
name = 'Sneza'
age = 36
message = "Cao ja sam {} i imam {} godina".format(name, age)
print(message)

# podaci = {"ime": "Sloba", "grad":"Novi Sad"}
# poruka = "Stanujem u {grad} i zovem se {ime}".format(**podaci)
# print(poruka)

#################
#     LIST      #
#################
numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers))

moja_lista = []
moja_lista.append(1)
moja_lista.append(2)
moja_lista.append(3)
print(moja_lista)

lista = [3.14, True, False, 100, ['x', 'y', 'z']]
print(lista)

laptops = ['dell lattitude', 'lenovo think pad', 'macbook pro']
#                 0                  1                 2
print('Ja od ovih modela koristim npr u kancelariji ' + laptops[1] + ' a na terenu i kuci ' + laptops[2])

brojevi = [1,2,3,5,8]
print(brojevi)
brojevi[3] = 4
brojevi[4] = 5
brojevi.append(6)
print(brojevi)
dodatni_brojevi = [7,8,9,10]
brojevi.extend(dodatni_brojevi)
brojevi.insert(9, 1000)
print(brojevi)

brojevi.remove(1000)
brojevi.append(10)
brojevi.remove(10)
print(brojevi)

brojevi = [1,2,3]
poslednji = brojevi.pop()
print(brojevi)
print(poslednji)

brojevi.clear()
print(brojevi)

brojevi = [100, 200, 300]
print(200 in brojevi)
print(2000 in brojevi)

#################
#  DICTIONARIES #
#################
kursevi = {'kurs' : 'python data analyst', 'predavac': 'Slobodan Miric'}
print(kursevi)
print(kursevi['kurs'])
print(kursevi['predavac'])

zaposleni = {
    'ime': 'Snezana',
    'godine': '36',
    'grad': 'Novi Sad'
}
print(zaposleni)

primer = dict(ime='Marko', godine=29,grad='Beograd')
print(primer)

primer2 = {1: 'jedan', 2: 'dva', 3: 'tri'}
print(primer2)

zaposleni = {
    '1': {'ime': 'marko', 'pozicija': 'web designer'},
    '2': {'ime': 'ana', 'pozicija': 'python developerka'},
}
print(zaposleni['1']['ime'])
print(zaposleni['2']['pozicija'])

#################
#     TUPLES    #
#################
kurs = ('python data analyst', 3, 'meseca')
print(type(kurs))
print(kurs[0] + ' kurs traje ' + str(kurs[1]) + ' ' + kurs[2])

brojevi = (1,2,3,4,5)
print(brojevi[0])
# brojevi[0] = 2000
# brojevi.append(400)
print(brojevi)

#################
#     SETS      #
#################
rokovi = {'decembar', 'jun', 'septembar', 'jun'}
print(type(rokovi))
print(rokovi)

brojevi = {1,2,3}
brojevi.add(4)
brojevi.remove(4)
print(brojevi)

neparni = {1, 3, 5, 7, 9}
parni = {2, 4, 6, 8, 10}
unija = neparni.union(parni)
print(unija)

#################
#  BOOLEANS     #
#################
print(True)
print(False)

ljubimac = 100
ljubimac = ['Pas', 'Frida']
print(ljubimac)