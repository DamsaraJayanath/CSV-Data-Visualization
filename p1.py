import matplotlib.pyplot as plt
import csv
from collections import Counter

with open('train.csv') as file:
    csv_reader = csv.DictReader(file)

    threat_counter = Counter()

    for row in csv_reader:
        threat_counter.update(row['Type_of_Breach'].split('/'))

threats = []
size = []

for item in threat_counter.most_common(5):
    threats.append(item[0])
    size.append(item[1])

plt.bar(threats, size)
plt.grid()
plt.show()