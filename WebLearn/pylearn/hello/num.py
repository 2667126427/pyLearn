nums = input("enter a number:")
length = len(nums)
if sum([int(i)**length for i in nums]) == int(nums):
    print("yes")
else:
    print("no")
