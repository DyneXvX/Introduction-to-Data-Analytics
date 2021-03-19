#%%
import pandas as pd
import numpy as np

fl_population = np.genfromtxt('DataSets/Dataset 15 - Population.csv', dtype=str, delimiter=',', skip_header=2)
population_frame = pd.DataFrame(fl_population, columns=['County', '2015', '2016', '2017', '2018', '2019'])

average_income = np.genfromtxt('DataSets/Dataset 6 - AverageIncome.csv', dtype=str, delimiter=',', skip_header=2)
income_frame = pd.DataFrame(average_income, columns=['County', '2015', '2016', '2017', '2018', '2019'])

death_rates = np.genfromtxt('DataSets/Dataset 1 - DeathRates.csv', dtype=str, delimiter=',' , skip_header=1)
death_frame = pd.DataFrame(death_rates, columns=['County', '2015', '2016', '2017', '2018', '2019'])


# %%
#Population Numbers
population_frame[['2015', '2016', '2017', '2018', '2019']] = population_frame[['2015', '2016', '2017', '2018', '2019']].apply(pd.to_numeric)
sum_column = population_frame['2015'] + population_frame['2016'] + population_frame['2017'] + population_frame['2018'] + population_frame['2019']
average = sum_column / 5
population_frame['Average'] = average
print('Total population per county with their average over the course of 5 years.')
print()
print(population_frame)
#population_frame.to_excel('Exported Data/population.xlsx')

# %%
#Income Numbers
income_frame[['2015', '2016', '2017', '2018', '2019']] = income_frame[['2015', '2016', '2017', '2018', '2019']].apply(pd.to_numeric)
sum_column = income_frame['2015'] + income_frame['2016'] + income_frame['2017'] + income_frame['2018'] + income_frame['2019']
average = sum_column / 5
income_frame['Average'] = average
print('Average income per county with their average over the course of 5 years.')
print()
print(income_frame)
#income_frame.to_csv('Exported Data/averageIncome.csv')

# %%
#Death Rates from Opioid
death_frame[['2015', '2016', '2017', '2018', '2019']] = death_frame[['2015', '2016', '2017', '2018', '2019']].apply(pd.to_numeric)
sum_column = death_frame['2015'] + death_frame['2016'] + death_frame['2017'] + death_frame['2018'] + death_frame['2019']
average = sum_column / 5
death_frame['Average'] = average
print('The total death rate for each county due to Opioid Overdose related problems. (Percent of Deaths were Opioid Related.)')
print()
print(death_frame)
#death_frame.to_csv('Exported Data/averageDeathRate.csv')

# %%
