x = 10 
y = 2.3
z = 'This is fun'

print (x,y,z)

age = 18

if age >=18:
    print ("You are an adult")
else:
    print ("You are a child")

number = 5

if number > 0:
    print ("The number is positive")
elif number <0:
    print ("The number is negative")
else:
    print("The number is 0")

for i in range(5):
    print ("This is a loop", i)

count = 0

while count <3:
    print ("Count", count)
    count +=1

for i in range(21):
    if i %2 ==0:
        print ("This is the even number", i)

def greet(name):
    return f"Hello, {name}"

print(greet("Sakshi"))

def sum(a,b):
    return a+b

print(sum(3,4))

#numpy array
import numpy as np

arr1 = np.array([1,2,3,4,5])
print("1D Array:", arr1)
print(arr1 + 2)

arr2 = np.array([[1,2,3],[4,5,6]])
print("2D Array:", arr2)
arr2 * 3
print(arr2 * 3)

arr3 = np.array([[[1,2],[2,3],[3,4]]])
print("3D Array:", arr3)
print(arr3 ** 2)

arr4 = np.array([2,3,4,5,6])
print("Addition",arr1 + arr4)
print("Multiplication", arr1 * arr4)

print("Mean", np.mean(arr1))
print("Sum", np.sum(arr2))
print("Standard Deviation", np.std(arr3 ))

#zeroes
zeros = np.zeros((2,3))
print("Zeroes\n", zeros)

#ones
ones = np.ones((3,2))
print("Ones", ones)

#range
range_array = np.arange(1,10,2)
print("Range array", range_array)

range_array = np.arange(3,10,3)
print("Range array", range_array)

#Random numbers
random_array = np.random.rand(3,3)
print("Random Array", random_array)

#Creation of 1D, 2D and 3D Array

arr1 = np.array([1,2,3,4,5,6])
print(arr1)

arr2 = np.array([[1,2,2], [2,5,6]])
print(arr2)

arr3 = np.array([[[1,2,3], [5,5,6], [2,9,4]]])
print(arr3)

#Addition and Multiplication

arr1 = np.array([1,7,2,4])
arr2 = np.array([1,4,2,6])

sum_array = arr1 + arr2
print(sum_array)
multi_array = arr1 * arr2
print(multi_array)

#Generation of zeros and ones
zeros = np.zeros((2,3))
print(zeros)

ones = np.ones((3,2))
print(ones)

#Mean, standard deviation and sum of an array

arr = np.array([1,3,4,5])
print(np.mean(arr))
print(np.sum(arr))
print(np.std(arr))

#array of random numbers
print(np.random.rand(3,3))

#Indexing 
arr = np.array([1,2,3,4,5])
print(arr[-1])

arr = np.array([[1,2,3], [1,3,4]])
print(arr[0,2])

arr = np.array([[[1,2,3], [2,3,4], [2,3,4]]])
print(arr[0,2,2])

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3[0,1,2])

# Slicing

arr = np.array([1,2,3,4,5])
print(arr[1:3])

arr2 = np.array([[1,2,3],[2,3,4],[0,1,2]])
print(arr2[0:2, 1:3])

arr3 = np.array([[[1,2,3,4], [1,2,3,4]], [[1,4,5,6],[1,4,5,6]]])
print(arr3[0,1:2,0:2])

#Reshaping

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)

arr2 = np.array([[1,2,3], [4,5,6], [6,7,8]])
print(arr2.flatten())

#Fancy Indexing

arr = np.array([1,2,3,4,5])
print(arr[[0,2,3]])

arr2 = np.array([[1,2,3], [2,3,4], [4,5,6]])
print(arr[[0,2]])

#Indexing
arr = np.array([1,2,3,4])
print(arr[0])

arr2 = np.array([[1,2,3],[1,2,3],[4,5,6]])
print(arr2[0,1])

arr3 = np.array([[[1,2,3],[2,3,4]],[[2,3,4],[1,2,3]]])
print(arr3[1,0,2])

#Slicing
arr = np.array([1,2,3,4,5])
print(arr[1:4])

arr2 = np.array([[1,2,3],[1,2,3],[4,5,6]])
print(arr2[0:1, 1:2])

arr3 = np.array([[[1,2,3],[2,3,4]],[[2,3,4],[1,2,3]]])
print(arr3[0,0:1,0:2])

#Reshaping
arr = np.array([1,2,3,4,5,6])
reshap_arr = arr.reshape(2,3)
print(reshap_arr)

arr2 = np.array([[1,2,3],[1,2,3],[4,5,6]])
flatten_array = arr2.flatten()
print(flatten_array)

#Fancy Indexing
arr2 = np.array([[1,2,3],[1,2,3],[4,5,6]])
print(arr2[[1,2]])


#Dot Product
A = np.array([[1,2,3],[2,3,4],[2,3,4]])
B = np.array([[2,3,4],[3,4,5],[3,4,5]])
print("Dot Product", np.dot(A,B))
print("Transpose of A", A.T)

#Boolean Indexing
arr = np.array([1,2,3,4,5,6,7,8])
print("Elements greater than 3", arr[arr>3])

#Adding array scalar to array 
print(arr +5)

#Adding arrays of different shapes
A = np.array([[1,2],[2,3]])
B= np.array([1,2])
print(A+B)

#Numpy Exercise
A = np.array([[1,2,3],[4,5,6],[4,7,8]])
B = np.array([[10,11,12],[13,14,15],[16,17,18]])
print(A+B)
print(A*B)
print(np.dot(A,B))

#Boolean Indexing
print("Greater than 4", A[A>4])
B[B>15] =0
print("Setting all elements greater than 15 to 0", B)
#print(C=0)

#Slicing and Reshaping
print(A[1:])
print(B.flatten())
print(A.flatten())

print(np.mean(A))
print(np.std(A))
print(np.sum(A))

print(A+10)

C = np.array([1,2,3])
print(B-C)

#Bonus
def function(B):
    return ((B.T), np.mean(B), np.sum(B))

B = np.array([[1,2,3],[1,4,5],[3,4,5]])

