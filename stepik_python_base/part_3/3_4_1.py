import csv
from collections import Counter

with open("Crimes.csv", "r") as f:
    reader = csv.DictReader(f)
    crimes = []
    for row in reader:
        crimes.append(row['Primary Type'])
    c = Counter(crimes).most_common(1)
print(c[0][0])

'''
from collections import Counter as c

with open('Crimes.csv') as f:
 data = csv.reader(f)
 print(c( row[5] for row in data if '2015' in row[2] ))
'''

'''
import csv

with open("Crimes.csv") as f:
     reader = csv.reader(f)
     crimes = []
     for row in reader:
         if "2015" in row[2]:
             crimes.append(row[5])
     print(max(crimes, key=crimes.count))
'''

'''
import csv

with open("Crimes.csv") as fi:
    reader = csv.reader(fi)
    next(reader)
    crime_cnt = dict()
    for row in reader:
        year = row[2][6:10]
        if year == "2015":
            crime_type = row[5]
            if crime_type not in crime_cnt:
                crime_cnt[crime_type] = 0
            crime_cnt[crime_type] += 1

a = list(map(lambda x: (crime_cnt[x], x), crime_cnt))
a.sort(key=lambda x: -x[0])

print(a[0][1])
'''