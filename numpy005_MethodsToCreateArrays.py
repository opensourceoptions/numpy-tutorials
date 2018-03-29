#import the numpy package
import numpy as np

#create an 'empty' array
a = np.empty((2,2), dtype=np.float32)
print a

#now an array of ints
b = np.empty((5,3), dtype=np.int)
print b

#fill a with the value 99.99
a.fill(99.99)
print a

#fill b with the value 99.99
b.fill(99.99)
print b

#create an array of zeros
z = np.zeros((3,4), dtype=np.float32)
print z

#create an array of ones
o = np.ones((3,4), dtype=np.int)
print o

#create an array with 2 sequential elements
a = np.arange(2)
print a

#create an array with the values 5-10
a = np.arange(5,11)
print a

#create an array with even values from 10-30
a = np.arange(10,31,2)
print a

#create a 3x3x3 array ranging from 0 to 26
a = np.arange(27).reshape((3,3,3))
print a

#create array from inputdata.csv
a = np.genfromtxt("importdata.csv", dtype=np.float32, delimiter=",")
print a

