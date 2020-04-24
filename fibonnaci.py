
n = input('Enter the value for n: ')
f0 = 0
f1 = 1

for i in range(0,n):
  if i == 0 or i == 1:
    print(i)
  else:
    result = f0 + f1
    f0 = f1
    f1 = result
    print(result)
