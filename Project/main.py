#%%
import pandas as pd
import numpy as np

fl_population = np.genfromtxt('DataSets/population.csv', dtype=str, delimiter=',', skip_header=2)

population_frame = pd.DataFrame(fl_population, columns=['County', '2015', '2016', '2017', '2018', '2019'])
print(population_frame)

average_income = np.genfromtxt('DataSets/Dataset 6.csv', dtype=str, delimiter=',', skip_header=2)

income_frame = pd.DataFrame(average_income, columns=['County', '2015', '2016', '2017', '2018', '2019'])
print(income_frame)

death_rates = np.genfromtxt('DataSets/deathRates.csv', dtype=str, delimiter=',' , skip_header=1)
death_frame = pd.DataFrame(death_rates, columns=['County', '2015', '2016', '2017', '2018', '2019'])

print(death_frame)
# %%

