class Pravougaonik:
    def __init__(self,duzina, sirina):
        self.duzina = duzina
        self.sirina = sirina

    def povrsina(self):
        return self.duzina * self.sirina

    def obim(self):
        return 2 * (self.duzina + self.sirina)

pravougaonik1 = Pravougaonik(5,10)
print(pravougaonik1.povrsina())
print(pravougaonik1.obim())

pravougaonik2 = Pravougaonik(2,4)
print(pravougaonik2.povrsina())
print(pravougaonik2.obim())


class Automobil:
    ''' Docstring gocvori na ms ta radli klasa tj sta izvrsava '''
    def __init__(self, marka, model, godina):
        self.marka = marka
        self.model = model
        self.godina = godina

    def opis(self):
        print(f"{self.marka} {self.model} je u voznom stanju")

auto1 = Automobil('Renault', 'Clio 4 grandtoud', 2018)
auto1.opis()
print(f"Moj trenutni auto je {auto1.marka} {auto1.model} vozim ga 2 godine jos je mlad {auto1.godina} i planiram da ga vozim jos npr 2 godine")

auto2 = Automobil('Skoda', 'Octavia', 2015)
print(f"Moj brat je uzeo auto {auto2.marka} {auto2.model} koji je {auto2.godina} i to je sad vec skoro 10 godina i posle mesec dana odmah kvar 300 evra")

class Restoran:
    def __init__(self, ime, tip, radno_vreme):
        self.ime = ime
        self.tip = tip
        self.radno_vreme = radno_vreme

    def opis_restorana(self):
        print(f"{self.ime} je {self.tip}")

    def otvoren_zatvoren(self):
        print(f"{self.ime} je otvoren {self.radno_vreme}")

restoran1 = Restoran('kampanel', 'meditarnski tip restorana', 'od maja do oktobra')
restoran1.opis_restorana()
restoran1.otvoren_zatvoren()
print(f"{restoran1.ime} je {restoran1.tip} i otvoren je samo u full sezoni od {restoran1.radno_vreme}")

restoran2 = Restoran('Sabidoro', 'italijanski restoran', 'cele godine')
restoran2.opis_restorana()
restoran2.otvoren_zatvoren()
print(f"{restoran2.ime} je {restoran2.tip} i otvoren je {restoran2.radno_vreme}")
