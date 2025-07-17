import array as arr
array_num = arr.array('i',[1, 2, 3, 4, 5, 7, 6, 9, 3])
print("Original array: "+str(array_num))

print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))
print()
array_num.reverse()
print("reverse the order of the items:")
print(str(array_num))