nested_list = [[2,4,6,8,10], [1,3,5,7,9]]

print("accessing the third element of the second list", nested_list[1][2])

for i in nested_list:
    print("list",i,"elements")
    for j in i:
        print(j)