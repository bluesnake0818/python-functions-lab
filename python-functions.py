def sum_to (n):
  counter = n
  sum = 0
  while counter > 0:
    sum = sum + counter 
    counter -= 1
  return sum
    

print(sum_to(6))  # returns 21
print(sum_to(10)) # returns 55)

def largest (listNum):
  return max(listNum)

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231