#import the numpy package
import numpy as np

#create a 1d array
a = np.array([1,2,3])

#print the shape of a
print "1D shape"
print np.shape(a)

#this gives us the same answer
print "Getting shape as property of a"
print a.shape

#create a 2d array
a2d = np.array([[1,2,3],
               [1,2,3]])

#print the shape
print "2D shape"
print a2d.shape

#create a 3d array
a3d = np.array([[[1,2,3,4],
                 [1,2,3,4],
                 [1,2,3,4]],
                [[1,2,3,4],
                 [1,2,3,4],
                 [1,2,3,4]]
                ])

#print the shape
print "3D shape"
print a3d.shape

#reshape arrays
#create a 1d array
a = np.array([1,2,3,4])

#reshape the array to create a new array with the same values but a different shape
b = np.reshape(a, (2,2))

#print the new array and its shape
print "1D reshape to 2D"
print b
print "Shape of new 2D"
print b.shape

#modify the original array
b = a.reshape((2,2))

#print the array and its shape
print "Same result using the shape property of a"
print b
print b.shape

#create a 12 element 1d array
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

#reshape to a 3d array
b = a.reshape((2,2,3))

#print the array
print "Reshape to 3D"
print b

#more 3d shapes
b2 = a.reshape((3,2,2))
b3 = a.reshape((2,3,2))
b4 = a.reshape((1,3,4))

#print the arrays
print "3 different 3D arrays from the same 1D array"
print b2
print b3
print b4

#2d equivalent to b4
b4_2d = a.reshape((3,4))
print "This 2D array is equivalent to the previous 3D array"
print b4_2d