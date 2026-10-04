import numpy as np

print(np.__version__)

array =np.array([1234, 5678, 91011])
array=array*2
print(array)

word_array= np.array([[["A","B","C"],["D","E","F"],["G","H","I"]]
                      ,[["J","K","L"], ["M","N","O"],["P","Q","R"]]
                      ,[["S","T","U"], ["V","W","X"],["Y","Z","0"]]])
WORD=word_array[0,0,2]+word_array[0,0,0]+word_array[2,0,1]
print(WORD)

radii=np.array([0.5, 1.0, 1.5, 2.0, 2.5])
area=np.pi*radii**2
print(area)