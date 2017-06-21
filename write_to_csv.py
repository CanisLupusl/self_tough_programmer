import csv

items = [['Top Gun', 'Risky Business', 'Minority Report'],['Titanic', 'The Revenant', 'Inception'],['Training Day', 'Man on Fire', 'Flight']]

with open('filmai.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    for i in items:
        w.writerow(i)
