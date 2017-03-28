# 输入
arr = []
try:
    temp = "input"
    while temp is not "":
        temp = input("input a number，Enter to end:")
        t = int(temp)  #
        arr += [t]  # add to the array
except ValueError as err:
    print(err)
# order by ascending
i = 1  # i the number which to be insert
if len(arr) >= 2:  # if len(arr) < 2， no need to sort.
    for i in range(1, len(arr)):  # i is from [1, len) integer
        temp = arr[i]  # save arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:  # to find the end
            arr[j + 1] = arr[j]  # move j forward
            j -= 1
        arr[j + 1] = temp

print(arr)
