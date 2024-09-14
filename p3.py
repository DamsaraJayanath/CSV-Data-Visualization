import matplotlib.pyplot as plt
import csv
from collections import Counter
import pandas as pd

language_counter = Counter()

data = pd.read_csv('data.csv')
ids = data['Responder_id']
languages_responses = data['LanguagesWorkedWith']

for response in languages_responses:
    language_counter.update(response.split(';'))

languages = []
numbers = []

for item in language_counter.most_common(10):
    languages.append(item[0])
    numbers.append(item[1])

plt.barh(languages, numbers)
plt.grid()
plt.tight_layout()
plt.show()