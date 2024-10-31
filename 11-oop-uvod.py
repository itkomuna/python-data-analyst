class Automobil:
    def __init__(self, marka_automobila, model_automobila, kubikaza):
        self.marka = marka_automobila
        self.model = model_automobila
        self.kubikaza = kubikaza

    def prikazi_info(self):
        print(f"Automobil marke {self.marka}")
        print(f"Kubikaza automobila je {self.kubikaza}")

moj_automobil = Automobil('Renault', 'Megane', 1900)
print(moj_automobil.marka)
print(moj_automobil.model)
print(moj_automobil.kubikaza)

moj_automobil.prikazi_info()