#use of numpy package
import numpy as np

a1=([2,3,8])
print(a1)

a=np.array([2,3,4,2,7,9]) #using array object
print(a)

print(a+a) #adding arrays

print(a*a) #multiplying arrays

print(np.dot(a,a)) #using dot method to get the sum of product

#shape and reshape
print(a.shape)
print(a.reshape(2,3))
print(a.reshape(3,2))

#check the type, returns ndarray
print(type(a))

a=np.array([5,7,9])
print(a[2])
print(a[1: ])
print(a[0] + a[2])

b=np.array([[1,3,5],[7,8,9]])
print(b[1])
print(b[0][2])
print(b[1,2])
print(b[:,1])
print(b[:,2])

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr[1, 1:4])
print(arr[:, 2:4])
print(arr[0:2, 2:4])
print(arr[1:2, 3:4])

#masking
a=np.array([230,10,284,39,76])
cutoff=200
print(a>cutoff)
a[a>cutoff]=0
print(a)

#Broadcasting
c=np.array([[0,1,2],[3,4,5]])
d=np.array([10,100])
print(c * d[:,None])







