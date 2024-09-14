import matplotlib.pyplot as plt
import csv
from collections import Counter

with open('train.csv') as file:
    csv_reader = csv.DictReader(file)

    location_counter = Counter()

    for row in csv_reader:
        location_counter.update(row['Location_of_Breached_Information'].split(' '))

locations = []
numbers = []

for item in location_counter.most_common(10):
    locations.append(item[0])
    numbers.append(item[1])

locations.reverse()
numbers.reverse()

plt.barh(locations, numbers)
plt.grid()
plt.tight_layout()
plt.savefig('aa.png')
plt.show()