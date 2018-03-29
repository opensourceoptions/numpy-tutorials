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