def moja_funckija():
    print("Pozdrav iz funkcije")
moja_funckija()

def sabiranje(broj1,broj2):
    return broj1 + broj2
rezultat = sabiranje(10, 30)
print(rezultat)

# def povrsina_kruga(r):
#     povrsina = 3.14 * r * r
#     print(povrsina)
# povrsina = povrsina_kruga(2)
# print(povrsina)

def povrsina_kruga(r):
    povrsina = 3.14 * r * r
    return povrsina
povrsina = povrsina_kruga(4)
print(povrsina)