
# def squares(nums):
#     i = 0
#     square = []
#     while(i<len(nums)):
#         nums[i] = (nums[i])**2
#         i += 1
#     nums.sort()
#     return nums

def squares(nums):
    square = list(map(lambda a: a**2, nums))
    square.sort()
    return square

a = [-10, 3, 4, 4, 6]

print(squares(a))