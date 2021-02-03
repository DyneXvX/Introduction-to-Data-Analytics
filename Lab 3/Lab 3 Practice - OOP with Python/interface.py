#%%
from Patient import *

karthik = Patient('Karthik Umapathy', 230, 75, "Mayo Clinic")
thandie = Patient('Thandie Newton', 112, 63)

print("First patient name is " + karthik.name.title() + " and his BMI value is " + str(karthik.calculate_bmi()) + ".")
print("Second patient is " + thandie.name.title() + " and they are " + str(thandie.height_m) + "meters tall.")
print(karthik.name.title() + " is staying at " + karthik.hospital)

# %%

leslie = OutPatient('Leslie Nielsen', 74, 210, 'Pulmonary Medicine', 'Dr. Sumera Smith', '2020-12-21', '11:00', True, 0.65, 5413)
print(leslie)
# %%
