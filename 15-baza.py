import mysql.connector

baza  = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'root',
    database = 'projekat'
)

# print(baza)

cursor = baza.cursor()

#### KREIRANJE BAZE  #####
# cursor.execute("CREATE DATABASE projekat")

# cursor.execute('SHOW DATABASES')
# # print(cursor)
# for lista in cursor:
#     print(lista[0])

#### KREIRANJE TABELE #####
# cursor.execute("CREATE TABLE korisnici (ime VARCHAR(50), email VARCHAR(30), godine INT(11), id INT AUTO_INCREMENT PRIMARY KEY)")
# cursor.execute("SHOW TABLES")
# for tabela in cursor:
#     print(tabela)

#### UNOS JEDNOG KORISNIKA #####
# unos = "INSERT INTO korisnici (ime, email, godine) VALUES (%s, %s, %s)"
# unos1 = ('Slobodan', 'slobamiric@gmail.com', 47)

# cursor.execute(unos, unos1)
# baza.commit()

#### UNOS vise KORISNIKA #####
# unos = "INSERT INTO korisnici (ime, email, godine) VALUES (%s, %s, %s)"
# vise_korisnika = [
#     ("Tamara", "tasa@gmail.com", 47),
#     ("Jovana", "jocka@gmail.com", 18),
#     ("Marko", "maki@gmail.com", 12)
# ]

# cursor.executemany(unos, vise_korisnika)
# baza.commit()

#### SELECT #####
# cursor.execute("SELECT * FROM korisnici")
# rezultat = cursor.fetchall()
# for red in rezultat:
#     print(red[2])

# cursor.execute("SELECT godine FROM korisnici")
# rezultat = cursor.fetchone()
# for red in rezultat:
#     print(red)

# cursor.execute("SELECT * FROM korisnici")
# rezultat = cursor.fetchall()
# print("IME\tEMAIl\t\t\tGODINE\tid")
# print("---\t-----\t\t\t------\t--")
# for red in rezultat:
#     print(red[0] + "\t%s" %red[1] + "\t\t%s" %red[2] + " \t%s" %red[3])
#     # print(f"{red[0]} {red[1]} {red[2]} {red[3]}")

#### WHERE #####
# cursor.execute("SELECT * FROM korisnici WHERE ime = 'Marko'")
# rezultat = cursor.fetchall()
# for red in rezultat:
#     print(red)

#### LIKE #####
# cursor.execute("SELECT * FROM korisnici WHERE ime LIKE 'M%'")
# rezultat = cursor.fetchall()
# for red in rezultat:
#     print(red)

#### AND OR #####
# cursor.execute("SELECT * FROM korisnici WHERE ime LIKE '%a%' OR godine = 180")
# rezultat = cursor.fetchall()
# for red in rezultat:
#     print(red)

#### UPDATE #####
# izmena = "UPDATE korisnici SET godine = 18 WHERE id = 5"
# cursor.execute(izmena)
# baza.commit()

#### LIMIT #####
# cursor.execute("SELECT * FROM korisnici LIMIT 2")
# cursor.execute("SELECT * FROM korisnici LIMIT 2 OFFSET 2")
# cursor.execute("SELECT * FROM korisnici ORDER BY ime ASC")
# rezultat = cursor.fetchall()
# for red in rezultat:
#     print(red)

#### DELETE #####
# brisanje = "DELETE FROM korisnici WHERE id = 5"
# cursor.execute(brisanje)
# baza.commit()

brisanje = "DROP TABLE korisnici"
cursor.execute(brisanje)