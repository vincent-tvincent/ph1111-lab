import math
from array import array

import numpy
import matplotlib.pyplot as plt
#part 1
#answer of question 1
def cylinder_volume (hight, radius):
    return math.pi * math.pow(radius,2)*hight

#answer of question 2
def pythagorean_Theorem (leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

#answer of question 3
def Quadratic_formula (a,b,c):
    delta = b**2 - 4*a*c
    return [(-b + math.sqrt(delta))/2, (-b - math.sqrt(delta))/2]

#part 2
data =numpy.delete(numpy.genfromtxt('lab1data.csv', delimiter = ","),0,0)
print(data)
x_set = []
y_set = []
for i in data:
    x_set.append(i[0])
    y_set.append(i[1])
plt.scatter(x_set,y_set)
plt.axis([0,10,0,10])
plt.xlabel("mass")
plt.ylabel("distance")
plt.show()
distance_sum = 0
mass_sum = 0
for i in data:
    mass_sum += i[0]
    distance_sum += i[1]
distance_mean = distance_sum / len(data)
mass_mean = mass_sum / len(data)
distance_std_sum = 0
mass_std_sum = 0
for i in data:
    mass_std_sum += (i[0] - mass_mean)**2
    distance_std_sum += (i[1] - distance_mean)**2
mass_standard_division = math.sqrt(mass_std_sum /len(data))
distance_standard_division = math.sqrt(distance_std_sum / len(data))
print("mean value of distance: ",distance_mean , "\n standard division of distance: ", distance_standard_division ,"\n\n", "mean value of mass: ", mass_mean, "\n standard division of mass: ", mass_standard_division)

#part 3
# the data are accurate, but the division of data are too large, thus the reseachers should improve their precision







