#multiplication table using broadcasting array
num1=np.array([[1,2,3,4,5,6,7,8,9,10]])
num2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(num1.shape)
print(num2.shape)
multiplication_table=num1*num2
print(multiplication_table)
