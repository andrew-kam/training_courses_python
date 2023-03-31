import csv
from collections import Counter

with open("Crimes.csv", "r") as f:
    reader = csv.DictReader(f)
    crimes = []
    for row in reader:
        crimes.append(row['Primary Type'])
    c = Counter(crimes).most_common(1)
print(c[0][0])

# https://stepik.org/lesson/24473/step/2?auth=login&unit=6777
