def sum_to (n):
  counter = n
  sum = 0
  while counter > 0:
    sum = sum + counter 
    counter = counter - 1
  return sum
    

print(sum_to(6))  # returns 21
print(sum_to(10)) # returns 55)
# print(sum_to(-1))