##############################
##############################
##############################
#          OPERATORI         #
##############################
##############################
##############################
# Vrste
    # Aritmeticki
    # Operatori dodele
    # Operatori poredjenja
    # Logicki operatori
    # Bitovni operatori

##############################
#    ARITMETICKI OPERATORI   #
##############################
print(100 + 300) # sabiranje
a = 100
b = 20
c = a + b
print(c)

a = 'BMW'
b = 10
# b = '10'
print(a + ' ' + str(b))

a = 20
b = 5
c = a - b # oduzimanje
print(c)

a = 10
b = 10
c = a * b # mnozenje
print(c)
a = 'Sloba'
b = 10
c = a * b
print(c)

a = 30
b = 6
c = a / b # deljenje rezultat je float
c = a // b # celobrojno deljenje
print(c)

a = 20
b = 7
c = a % b # modulo oeprater - ostatak pri deljenje
print(c) 

print(5**2) # eksponent 
print(5**3)


##############################
#### redosled operacija #####
##############################

print(1 + 4 * 2 + 3 - 1)
print(1 + (4 * 2) + 3 - 1)
print((2 + 2) * 10)

##############################
#    OPERATORI DODELE        #
##############################
a = 30  # operator dodele
print(a)

a += 20 # sabiranje i dodela       a = a(30) + 20
print(a)
b = 10
b += 20  #   b = b + 20       b = 10 + 20   10 + 20 = b

a -= 20  # oduzimanje i dodela     a = a(50) - 20  
print(a)
c = 100
c -= 70 # c = c(100) - 70
print(c)

d = 25  # deljenje i dodela
d /= 5  # d = d(25) / 5
print(d)

e = 25  # celobrojno deljenje i dodela
e //= 5  # e = e(25) // 5
print(e)

f = 3  # stepenovanje i dodela
f **= 2  # f = f ** 2  f = 3 ** 2
print(f)

##############################
#    OPERATORI POREDJENJA    #
##############################
print('python' == 'python')
x = 10
y = 10
print(x == y)  # jednako je
print(10 == 10.0)

print(20 != 30) # nije jednako

print(10 > 3) # vece od 

print(10 >= 10) # vece ili jednako od

print(3 < 30) # manje od
print(30 <= 30) # manje ili jednako od

print(5 + 5 >= 5 + 5)

##############################
#    LOGICKI    OPERATORI    #
##############################
# AND = Uslov je tacana ako su oba izraza True
print(type(2 < 10 and 20 > 5))
print(10 > 20 and 10 > 2)

# OR - uslov je tacan ako je jedan od izraza tacan
x = 2
print(x == 2 or x == 100)

# NOT
x = 100
y = 100
print(not(x == y))  # reverse od true je false
print(not(100 > 5))
