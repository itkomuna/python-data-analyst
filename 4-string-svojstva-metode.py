# len duzina stringa
ime = 'Snjeza'
print(len(ime)) 
print(ime.upper())
print(ime.lower())
space = "razmak             izmedju                  reci"
print(space.capitalize())

word = "Ja sam neki STRING"
print(word)
rec_kao_title = word.title()
print(rec_kao_title)

# split
name = 'Predrag Miki Manjolovic'
print(name.split())

car = "Renaul clio, mali gradski auto, 74 konja, bela boja"
print(car.split(','))

# strip
tekst = "      Pozdrav svima koliko vas ima!        "
ociscen_tekst = tekst.strip()
print(ociscen_tekst)

text = "------------Python ekipo pozdrav----------------"
clean_text = text.strip("-")
print(clean_text)

tekst = "yyyyyyyyyyyyPythonyyyyyyyyyyyyy"
clean = tekst.strip("y")
print(clean)

# replace
team_lead = "Sloba je nas novi team lead"
print(team_lead.replace('Sloba','Milan'))

# count
zaposleni = "Sloba je nas prvi zaposleni, ali je dojadio i Bogu i ljudima pa bi moga Sloba da se skloni"
print(zaposleni.count('Sloba'))
print(zaposleni.count('a'))

# in
izbor = "PHP ili Python ili pak Java, pitanje je sad? Sta odabrati u 2024."
print('PHP' in izbor)

# not in
print('Python' not in izbor)

# join
words = ['Ovo', 'cemo', 'da', 'spojimo', 'pomocu', 'join','metode']
spoji = " ".join(words)
print(spoji)

# isalnum
tekst = "Slobadobroucidobioje=10!."
print(tekst.isalnum())

# isalpha
tekst = "Slobajeopetdobio10naispitu"
print(tekst.isalpha())