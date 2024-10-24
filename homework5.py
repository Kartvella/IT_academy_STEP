#Exercise N1

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
result = mylist[2] + mylist[8] + mylist[13]
print(result)
print('\n')


#Exercise N2

import random
listt = [random.randint(1, 100) for _ in range(20)]
odd_list = [i for i in listt if i % 2!=0]
smallest = odd_list[0]
largest = odd_list[0]

for num in odd_list:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
        
print('main list: ', listt)
print('odd list: ', odd_list)
print("smallest odd number:", smallest)
print("largest odd number:", largest)
print('\n')

    
#Exercise N3

my_llist = [43, '22', 12, 66, 210, ["hi"]]

print('id of 210 is: ', my_llist.index(210))

my_llist[-1].append('hello')

my_llist.pop(2)
print('element with id of 2 was removed: ', my_llist)

my_llist_2 = my_llist.copy()
my_llist_2.clear()

print('second list(which was copied and then cleared): ', my_llist_2)
print('original list:', my_llist)
print('\n')

 

#Exercise N4
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
    sum_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    print("sum of matrix's:")
    for row in sum_matrix:
        print(row)
else:
    print("matrix's dimensions do not match")
print('\n')

#Exercise N5

matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
example_matrix = [[0] * len(matrix3) for _ in range(len(matrix3[0]))]

for i in range(len(matrix3)):
    for j in range(len(matrix3[0])):
        example_matrix[j][i] = matrix3[i][j]

print("original matrix:")
for row in matrix3:
    print(row)

print("\ntransposed matrix:")
for row in example_matrix:
    print(row)   


#Exercise N6

matrix4= [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
print("generated matrix:")
for row in matrix4: 
    print(row)
