nums = [1,7,3,6,5,6]
left_sum = nums.copy()
right_sum = nums.copy()
a = sum(nums);
print(a)
n = len(nums);
count = 0
for i in range(n):
    if i == 0:
        left_sum[i] = 0
        right_sum[i] = a - nums[i]
        count = count + nums[i];
    elif i == n-1:
        right_sum[i] = 0
        left_sum[i] = a - nums[i]
    else:
        left_sum[i] = count;
        right_sum[i] = a - count - nums[i];
        count = count + nums[i];
for i in range(n):
    if left_sum[i] == right_sum[i]:
        print(i);
print(-1);
print(left_sum)
print(right_sum)




