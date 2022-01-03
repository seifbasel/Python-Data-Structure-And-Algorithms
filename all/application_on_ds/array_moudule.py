import array as arr

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
a =arr.array("i",list_1)
print("first element is: ",a[0])
print("second element is: ", a[1])
print(" elements from the third to the last is: ", a[2:])
a.append(10)
a.append(15)
print(a)
a.extend([17,18,19])
print(a)
del a[5]
print(a)
