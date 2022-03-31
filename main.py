import sqlite3

db = sqlite3.connect("sport.db")
cur = db.cursor()
from array import*
# 1 задание
flag=0
flag2=0
qq=array('i', [0,0])
print("1. Найти ранг соревнования, в котором участвовало минимальное число команд, в заданном году и виде спорта:\n")
cur.execute("SELECT Vid FROM Sorev")
SelectedVid = cur.fetchall()
print("Выберите вид спорта:\n")
for i in range(len(SelectedVid)):
    if i == 0:
        print(i, " - ", SelectedVid[i])
    if i != 0:
        if SelectedVid[i] != SelectedVid[i-1]:
            print(i, " - ", SelectedVid[i])
inputv = int(input())
cur.execute("SELECT Year FROM Sorev")
SelectedGod = cur.fetchall()
cur.execute("SELECT Rang FROM Sorev")
SelectedRang = cur.fetchall()
print("Выберите год:\n")
for i in range(len(SelectedGod)):
    if i == 0:
        print(i, " - ", SelectedGod[i])
    if i != 0:
        if SelectedGod[i] != SelectedGod[i-1]:
            print(i, " - ", SelectedGod[i])
inputg = int(input())
for i in range(len(SelectedGod)):
    if SelectedGod[inputg] == SelectedGod[i]:
        if SelectedVid[inputv] == SelectedVid[i]:
            q, = SelectedRang[i]
            if q == 1:
                qq[0] = qq[0]+1
            else:
                qq[1] = qq[1]+1
if qq[0] == 0:
    if qq[1] == 0:
        print("Не найдено")
    else:
        print("Ранг: 2")
else:
    if qq[1] == 0:
        print("Ранг: 1")
    else:
        if qq[0] > qq[1]:
            print("Ранг: 2")
        else:
            print("Ранг: 1")


# 2 задание
print("2. Найти все команды указанного ранга и года проведения соревнований, у которых не было ни одного проигрыша\n")
cur.execute("SELECT Year FROM Sorev")
SelectedGod = cur.fetchall()

cur.execute("SELECT Rang FROM Sorev")
SelectedRang = cur.fetchall()

cur.execute("SELECT Uchas FROM Sorev")
SelectedUch = cur.fetchall()

cur.execute("SELECT UName FROM Rez")
SelectedSop = cur.fetchall()

cur.execute("SELECT TypeRez FROM Rez")
SelectedT = cur.fetchall()
print("Выберите год:\n")
for i in range(len(SelectedGod)):
    if i == 0:
        print(i, " - ", SelectedGod[i])
    if i != 0:
        if SelectedGod[i] != SelectedGod[i-1]:
            print(i, " - ", SelectedGod[i])
inputg = int(input())
print("Выберите ранг:\n")
for i in range(len(SelectedRang)):
    if i == 0:
        print(i, " - ", SelectedRang[i])
    if i != 0:
        if SelectedRang[i] != SelectedRang[i-1]:
            print(i, " - ", SelectedRang[i])
inputr = int(input())

for i in range(len(SelectedGod)):

    if SelectedGod[inputg] == SelectedGod[i]:
        if SelectedRang[inputr] == SelectedRang[i]:

            for j in range(len(SelectedT)):

                if SelectedUch[i] == SelectedSop[j]:
                    if SelectedT[j] == ('Проигрыш',):
                        flag=0
                        break
                    else:
                        flag=1
            if (flag == 1):
                print(SelectedUch[i])
                flag = 0
                flag2 = 1
if (flag2 == 0):
    print("Команд не найдено")

# 3 задание
print("3. Найти всех соперников указанной команды в заданном ранге и заданном году:\n")

print("Выберите команду:")
for i in range(len(SelectedUch)):
    if i == 0:
        print(i, " - ", SelectedUch[i])
    if i != 0:
        if SelectedUch[i] != SelectedUch[i-1]:
            print(i, " - ", SelectedUch[i])
inputu = int(input())

print("Выберите год:\n")
for i in range(len(SelectedGod)):
    if i == 0:
        print(i, " - ", SelectedGod[i])
    if i != 0:
        if SelectedGod[i] != SelectedGod[i-1]:
            print(i, " - ", SelectedGod[i])
inputg = int(input())

print("Выберите ранг:\n")
for i in range(len(SelectedRang)):
    if i == 0:
        print(i, " - ", SelectedRang[i])
    if i != 0:
        if SelectedRang[i] != SelectedRang[i-1]:
            print(i, " - ", SelectedRang[i])
inputr = int(input())

cur.execute("SELECT SopName FROM Rez")
SelectedSop = cur.fetchall()

cur.execute("SELECT UName FROM Rez")
SelectedU = cur.fetchall()

flag=0
for i in range(len(SelectedGod)):

    if SelectedGod[inputg] == SelectedGod[i]:
        if SelectedRang[inputr] == SelectedRang[i]:
            if SelectedUch[inputu] == SelectedUch[i]:

                for j in range(len(SelectedSop)):

                    if SelectedUch[i] == SelectedU[j]:
                        print(SelectedSop[j])
                        flag=1
if flag == 0:
    print("Соперников не найдено")



# 4 задание
print("4. Найти вид спорта, в котором проводились соревнования в заданном году:\n")

cur.execute("SELECT Vid FROM Sorev")
SelectedS = cur.fetchall()

print("Выберите год:\n")
for i in range(len(SelectedGod)):
    if i == 0:
        print(i, " - ", SelectedGod[i])
    if i != 0:
        if SelectedGod[i] != SelectedGod[i-1]:
            print(i, " - ", SelectedGod[i])
inputg = int(input())

for i in range(len(SelectedGod)):
    if SelectedGod[inputg] == SelectedGod[i]:
        if i!=len(SelectedGod)-1:
            if SelectedS[i] == SelectedS[i+1]:
                flag=i
            else:
                print(SelectedS[flag])
        else:
            print(SelectedS[i])


# 5 задание
print("5. Найти все команды указанной страны, участвовавшие в соревнованиях заданного ранга:\n")

cur.execute("SELECT Ucountry FROM Uchas")
SelectedCoun = cur.fetchall()

cur.execute("SELECT Name FROM Uchas")
SelectedName = cur.fetchall()

print("Выберите страну:\n")
for i in range(len(SelectedCoun)):
    if i == 0:
        print(i, " - ", SelectedCoun[i])
    if i != 0:
        if SelectedCoun[i] != SelectedCoun[i-1]:
            print(i, " - ", SelectedCoun[i])
inputc = int(input())

print("Выберите ранг:\n")
for i in range(len(SelectedRang)):
    if i == 0:
        print(i, " - ", SelectedRang[i])
    if i != 0:
        if SelectedRang[i] != SelectedRang[i-1]:
            print(i, " - ", SelectedRang[i])
inputr = int(input())

flag = 0

for i in range(len(SelectedCoun)):
    if SelectedCoun[inputc] == SelectedCoun[i]:
        for j in range(len(SelectedUch)):
            if SelectedName[i] == SelectedUch[j]:
                if SelectedRang[inputr] == SelectedRang[j]:
                    print(SelectedName[i])
                    flag = 1
if flag == 0:
    print("Команд не найдено")
cur.close()
db.commit()
db.close()
