import numpy as np
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])
matrix2 = np.array([[7, 8, 9],
                    [10, 11, 12]])

# try:
result = np.add(matrix1, matrix2)
print('Matri1:')
print(matrix1)
print('Matrix2:')
print(matrix2)
print('Resultant Matrix after addition:')
print(result)

# except ValueError as e:print(f'Error:{e}')

# matrix3 = np.array([[1,2],[3,4],[5,6]])

# try:
  #  result_error = np.add(matrix1, matrix3)
 #   print(f'Resultant matrix after addition:')
 #   print(result_error)
 #   except ValueError as e:
#   print(f'Error:{e}')
