import os

import csv

budget_data_csv_path = os.path.join('..', 'Users', 'ryancrandall', 'Desktop', 'Starter_Code-3', 'PyBank', 'Resources', 'budget_data.csv')

with open(budget_data_csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)
