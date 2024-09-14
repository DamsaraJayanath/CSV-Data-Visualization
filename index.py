import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    # row = next(csv_reader)
    # print(row)
    # print(row['LanguagesWorkedWith'])

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))


x = language_counter.most_common(10)
languages = []
numbers = []

for lang, num in x:
    languages.append(lang)
    numbers.append(num)

languages.reverse()
numbers.reverse()


plt.title('Most Used Programming Languages in USA')
#plt.xlabel('Programming Languages')
plt.xlabel('Number of Users')

plt.barh(languages, numbers)
plt.grid()

plt.tight_layout()
plt.show()



    
