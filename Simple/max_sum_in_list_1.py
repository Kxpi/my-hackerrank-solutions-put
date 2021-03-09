nums=list(map(int, input().split()))
temp_max=nums[0]
actual_max=nums[0]
for i in range(1,len(nums)):
    temp_max=max(nums[i], temp_max+nums[i])
    actual_max=max(temp_max, actual_max)
if actual_max<0:
    print("0")
else:
    print(actual_max)
