L = [4,5,1,2,9,7,10,8]
print("Original list :", L)

# variable to store the sum of
# the list
count = 0

# finding the sum
for i in L:
    count += i

# divide the number of lists by
# number of elements

avg = count / len(L)

print("sum is :", count)
print("average is :", avg)

#sorting the element of the list
L.sort()

#printing the first element
print("the smallest element is :", L[0])

#printing the largest element
print("the largest element is :", L[-1])