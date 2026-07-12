nums = [1, 2, 40, 79, 67, 69, 12]

sum = 0
for n in nums:
    sum = sum + n
print(sum)
avg = sum/len(nums)
print(avg)

nums.sort()
print(nums)
print(nums[0], nums[-1])

nums.sort(reverse = True)
print(nums)