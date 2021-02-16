#%%
import numpy as np
import statistics as statistics

np.random.seed(20)
data = np.random.choice(range(20), size=(9,5))
print("Student Assignment Scores:")
print(data)


print()
mean_students = np.mean(data, axis=1)
mean_students = mean_students.round(decimals=2)
print("Mean score for each student: ", mean_students)

mean_assignments = np.mean(data, axis=0)
mean_assignments = mean_assignments.round(decimals=2)
print("Mean score for each assignment: ", mean_assignments)

print()
median_students = np.median(data, axis=1)
print("Median score for each student: ", median_students)

median_assignments = np.median(data, axis=0)
print("Median score for each assignment: ", median_assignments)

print('\n--Mode--')
mode_students = []
for list in data:
    mode_students.append(statistics.mode(list))
print("Mode for each student: ", mode_students)

mode_assignments = []
for list in data.T:
    mode_assignments.append(statistics.mode(list))
print("Mode for each assignment: ", mode_assignments)

print('\n--Range--')
range_students = np.ptp(data, axis=1)
max_students = np.amax(data, axis=1)
min_students = np.amin(data, axis=1)
i=1
for val in range(range_students.size):
    print('Range for student', i, ': ', max_students[val] , ' - ', min_students[val], ' = ',  range_students[val])
    i=i+1
print()

range_assignments = np.ptp(data, axis=0)
max_assignments = np.amax(data, axis=0)
min_assignments = np.amin(data, axis=0)
i=1
for val in range(range_assignments.size):
    print('Range for assignment', i, ': ', max_assignments[val] , ' - ', min_assignments[val], ' = ',  range_assignments[val])
    i=i+1
print()


print('\n--Percentiles and Quartiles--')
percentile_students_25 = np.percentile(data, 25, axis=1)
print('25th Percentile - First Quartile for Students:', percentile_students_25)
percentile_students_50 = np.percentile(data, 50, axis=1)
print('50th Percentile - Second Quartile for Students:', percentile_students_50)
percentile_students_75 = np.percentile(data, 75, axis=1)
print('75th Percentile - Third Quartile for Students:', percentile_students_75)
print()

percentile_assignments_25 = np.percentile(data, 25, axis=0)
print('25th Percentile - First Quartile for Assignments:', percentile_assignments_25)
percentile_assignments_50 = np.percentile(data, 50, axis=0)
print('50th Percentile - Second Quartile for Assignments:', percentile_assignments_50)
percentile_assignments_75 = np.percentile(data, 75, axis=0)
print('75th Percentile - Third Quartile for Assignments:', percentile_assignments_75)
print()
# %%
