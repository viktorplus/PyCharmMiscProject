nums = [10, 20, 30, 40]
# очистка всего списка
fruits = ["apple", "banana", "cherry", nums]
nums.clear()
# nums[6]
nums = 1
print(fruits)
fruits2 = fruits
fruits2.clear()
print(fruits)
print(fruits2)
print(nums)