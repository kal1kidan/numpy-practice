import numpy as np

print(np.__version__)

array =np.array([1234, 5678, 91011])
array=array*2
print(array)

#word array
word_array= np.array([[["A","B","C"],["D","E","F"],["G","H","I"]]
                      ,[["J","K","L"], ["M","N","O"],["P","Q","R"]]
                      ,[["S","T","U"], ["V","W","X"],["Y","Z","0"]]])
WORD=word_array[0,0,2]+word_array[0,0,0]+word_array[2,0,1]
print(WORD)

#area of circle
radii=np.array([0.5, 1.0, 1.5, 2.0, 2.5])
area=np.pi*radii**2
print(area)

#multiplication table using broadcasting
num1=np.array([[1,2,3,4,5,6,7,8,9,10]])
num2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(num1.shape)
print(num2.shape)
multiplication_table=num1*num2
print(multiplication_table)