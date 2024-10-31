import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    password = 'root',
    database = 'sakila'
)

# if connection.is_connected():
#     print("Povezani smo na MySQL server")

#     cursor = connection.cursor()
#     cursor.execute("SELECT DATABASE();")
#     record = cursor.fetchone()
#     print("Povezani smo na bazu podataka:", record)

#     cursor.close()
#     connection.close()
#     print("Povezivanje sa bazom je zatvoreno")

cursor = connection.cursor()
cursor.execute("SELECT * FROM actor;")

svi_rezulatati = cursor.fetchall()

for red in svi_rezulatati:
    print(red)

cursor.close()
connection.close()