import sqlite3

db = sqlite3.connect("sport.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Sorev(Rang INT, Vid TEXT, Year INT, Country TEXT, Uchas TEXT)""")

Sorevs = (
    (1, "Лыжи", 2000,  "Россия", "Сборная России"),
    (1, "Лыжи", 2000,  "Россия", "Сборная Японии"),
    (2, "Баскетбол", 2020,  "Япония", "Поколение чудес"),
    (2, "Баскетбол", 2020,  "Япония", "Сэйрин"),
)

cur.executemany("INSERT INTO Sorev VALUES(?, ?, ?, ?, ?)", Sorevs)

cur.execute("""CREATE TABLE IF NOT EXISTS Uchas(Name TEXT, Ucountry TEXT, Rez TEXT)""")

Uchass = (
    ("Сборная России", "Россия", "Золото"),
    ("Сборная Японии", "Япония", "Серебро"),
    ("Поколение чудес", "Япония", "Серебро"),
    ("Сэйрин", "Япония", "Золото"),
)

cur.executemany("INSERT INTO Uchas VALUES(?, ?, ?)", Uchass)

cur.execute("""CREATE TABLE IF NOT EXISTS Rez(UName TEXT, SopName TEXT, TypeRez TEXT)""")

Rezs = (
    ("Сборная России" , "Сборная Японии", "Выигрыш"),
    ("Сборная Японии", "Сборная России", "Проигрыш"),
    ("Поколение чудес", "Сэйрин", "Проигрыш"),
    ("Сэйрин", "Поколение чудес", "Выигрыш"),
)

cur.executemany("INSERT INTO Rez VALUES(?, ?, ?)", Rezs)

cur.close()
db.commit()
db.close()
