import csv

with open('departement.csv', mode='r', encoding="utf8") as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for row in rd:
        departements.append(row[2])
        if len(departements) > 5:
            break
    print(sorted(departements))
    print(departements.sort())