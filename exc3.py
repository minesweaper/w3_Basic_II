# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty

def remove_numbers(x):
    position = 3 - 1
    idx = 0
    len_list = (len(x))
    while len_list > 0:
        idx = (position + idx)%len_list
        print(x.pop(idx))
        len_list -=1


nums = [10,20,30,40,50,60,70,80,90]
remove_numbers(nums)
print(nums)