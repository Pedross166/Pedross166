double_palindromes = []
for x in range(10**6):
  s = str(x)
  if s == s[::-1]:
    b = bin(x).replace('0b', '')
    if b == b[::-1]:
      double_palindromes.append(x)

sum = 0
for i in double_palindromes:
  sum += i

print(sum)