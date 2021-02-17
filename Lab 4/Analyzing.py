#%%

import numpy as np
import statistics as statistics

from numpy.core.defchararray import split

data = np.genfromtxt('Data\\brfss-cdc.csv', delimiter=',', skip_header=1)
int_data = data.astype(np.int)

# 2. First Five Rows of Data and the shape
print('First Five Rows of the Data')
print(int_data[:5])
print('Shape of the data: ', int_data.shape)
print()

# 3. Calculate weight Change (Current Weight - Weight a year ago)
weightChange = (data[:, 2] - data[:, 3])

# 4. Calculate and display mean, median, standard deviation, and interquartile range for the weight change.
mean_weightChange = np.mean(weightChange)
mean_weightChange = mean_weightChange.round(decimals=2)

median_weightChange = np.median(weightChange)
median_weightChange = median_weightChange.round(decimals=2)

sd_weightChange = np.std(weightChange)
sd_weightChange = sd_weightChange.round(decimals=2)

q75, q25 = np.percentile(weightChange, [75, 25])
iqr_weightChange = q75 - q25

print('Descriptive Statistics for Weight Change Data:')
print('Mean: ', mean_weightChange)
print('Median: ', median_weightChange)
print('Standard Deviation: ', sd_weightChange)
print('Interquartile Range: ', iqr_weightChange)
print()


# 5. Concatentat weight change array with the main data array.
int_data = np.insert(int_data, 6, weightChange, axis=1)


# 6. Display the five rows and shape of data.
print('Data with Weight Change Values Added')
print(int_data[:5])
print('Shape of the data: ', int_data.shape)
print()

# 7. Split the concatenated array based on the gender column.
male_data = int_data[int_data[:, 5] == 1]

# 8. Display the five rows and shape of the arrray relevant to males data.
print('-------Male Data--------')
print(male_data[:5])
print('Shape of the data: ', male_data.shape)
print()

# 9. Calculate and display mean, meadian, standard deviation, and interquartile range for the data relevant to males.
mean_weightChange = np.mean(male_data)
mean_weightChange = mean_weightChange.round(decimals=2)

median_weightChange = np.median(male_data)
median_weightChange = median_weightChange.round(decimals=2)

sd_weightChange = np.std(male_data)
sd_weightChange = sd_weightChange.round(decimals=2)

q75, q25 = np.percentile(male_data, [75, 25])
iqr_weightChange = q75 - q25

print('Descriptive Statistics for Male Weight Change Data:')
print('Mean: ', mean_weightChange)
print('Median: ', median_weightChange)
print('Standard Deviation: ', sd_weightChange)
print('Interquartile Range: ', iqr_weightChange)
print()

# 10. Display the five rows and shape of the array relevant to females data
print('--------Female Data--------')
female_data = int_data[int_data[:, 5] == 2]
print(female_data[:5])
print('Shape of the data: ', female_data.shape)
print()

# 11. Calculate and display mean, median, standard deviation, and interquartile range for the data relevant to females
mean_weightChange = np.mean(female_data)
mean_weightChange = mean_weightChange.round(decimals=2)

median_weightChange = np.median(female_data)
median_weightChange = median_weightChange.round(decimals=2)

sd_weightChange = np.std(female_data)
sd_weightChange = sd_weightChange.round(decimals=2)

q75, q25 = np.percentile(female_data, [75, 25])
iqr_weightChange = q75 - q25

print('Descriptive Statistics for Female Weight Change Data:')
print('Mean: ', mean_weightChange)
print('Median: ', median_weightChange)
print('Standard Deviation: ', sd_weightChange)
print('Interquartile Range: ', iqr_weightChange)

print()
print('-------------------------------------------------')
print('Thank you for using a Justin Thoms Python Program')
print('--------------CAP 4784 Spring 2021---------------')

# %%
