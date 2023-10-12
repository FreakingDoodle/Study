import random
## быстрая сортировка
nums = [1, 0, 2, 7, 10, 3, 5, 6, 3, 1, 2, 9, 8, 11, 1, 12, 13, 14, 2, 0, 20]
n=1
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)
print(quicksort(nums))
## сортировка расческой
ls = [1, 0, 2, 7, 10, 3, 5, 6, 3, 1, 2, 9, 8, 11, 1, 12, 13, 14, 2, 0, 20]
n = len(ls)
step = n
while step > 1 or flag:
   if step > 1:
       step -= 1
   flag, i = False, 0
   while i + step < n:
      if ls[i] > ls[i + step]:
          ls[i], ls[i + step] = ls[i + step], ls[i]
          flag = True
      i += step
print(*ls)
