nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Dãy ban đầu:")
for num in nums:
    if num % 2 != 0:
        print(num)
        
print("Dãy đảo ngược:")        
for i in range(len(nums)-1, -1, -1):
    if nums[i] % 2 != 0:
        print(nums[i])