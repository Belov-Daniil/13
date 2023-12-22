#4.	Определить количество взрослых(=>18) и детей(<18)
# d 1,2 и 3 классе , севших в порту Квинстаун, и сколько из них выжило
import csv

adults = [[], [], []]
unoun = [[], [], []]
kids = [[], [], []]
with open('titanic.csv', newline='') as File:
    all_ages = []
    file = csv.reader(File)
    for i in file:
        if i[11] == 'Q':
            try:
                if int(i[5]) < 18:
                    kids[int(i[2]) - 1].append(i[1])
                else:
                    adults[int(i[2]) - 1].append(i[1])
            except ValueError:
                unoun[int(i[2]) - 1].append(i[1])

print('Определить количество взрослых(=>18) и детей(<18) d 1,2 и 3 классе , севших в порту Квинстаун, и сколько из них выжило')
print('')
print('количество взрослых, севших в порту Квинстаун, в 1 классе: ' + str(len(adults[0])) + " выживших: " + str(adults[0].count('1')))
print('вo 2 классе: ' + str(len(adults[1])) + " выживших: " + str(adults[1].count('1')))
print('в 3 классе: ' + str(len(adults[2])) + " выживших: " + str(adults[2].count('1')))
print('')
print('количество детей, севших в порту Квинстаун, в 1 классе: ' + str(len(kids[0])) + " выживших: " + str(kids[0].count('1')))
print('вo 2 классе: ' + str(len(kids[1])) + " выживших: " + str(kids[1].count('1')))
print('в 3 классе: ' + str(len(kids[2])) + " выживших: " + str(kids[2].count('1')))
print('')
print('количество людей с неизвестным возрастом, севших в порту Квинстаун, в 1 классе: ' + str(len(unoun[0])) + " выживших: " + str(unoun[0].count('1')))
print('вo 2 классе: ' + str(len(unoun[1])) + " выживших: " + str(unoun[1].count('1')))
print('в 3 классе: ' + str(len(unoun[2])) + " выживших: " + str(unoun[2].count('1')))