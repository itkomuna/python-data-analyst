class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def prikazi(self):
        print("Osoba : ", self.ime, self.prezime)

class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa):
        self.broj_indeksa = broj_indeksa

        super().__init__(ime, prezime)

    def prikazi(self):
        print("Student: ", self.ime, self.prezime, self.broj_indeksa)

class Profesor(Osoba):
    def __init__(self, ime, prezime, predmet):
        self.predmet = predmet

        super().__init__(ime, prezime)

    def prikazi(self):
        print("Profesor: ", self.ime, self.prezime, self.predmet)

osoba = Osoba('Slobodan', 'Miric')
student = Student('Jovana', 'Miric', '1/2025')
profesor = Profesor('Dejan', 'Celic', 'interna medicina')

osoba.prikazi()
student.prikazi()
profesor.prikazi()

class Oblik:
    def __init__(self, ime):
        self.ime = ime

    def izracunaj_povrsinu(self):
        print('ne mogu da izracunam porvrsinu nekog neodredjenog generickog oblika')

class Kvadrat(Oblik):
    def __init__(self, ime, stranica):
        super().__init__(ime)
        self.stranica = stranica

    def izracunaj_povrsinu(self):
        povrsina = self.stranica * self.stranica
        print(f"Povrsina kvadrata {self.ime} je: {povrsina}")

class Krug(Oblik):
    def __init__(self, ime, poluprecnik):
        super().__init__(ime)
        self.poluprecnik = poluprecnik

    def izracunaj_povrsinu(self):
        povrsina = 3.14 * self.poluprecnik * self.poluprecnik
        print(f"Povrsina kruga {self.ime} je: {povrsina}")

kvadrat1 = Kvadrat('K1', 3)
kvadrat2 = Kvadrat('K2', 6)
krug1 = Krug('C1', 2)
krug2 = Krug('C2', 4)

oblici = [kvadrat1, kvadrat2, krug1, krug2]
for oblik in oblici:
    oblik.izracunaj_povrsinu()