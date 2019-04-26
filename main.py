# пример наибольшего разбиения на максимальное число различных слагаемых

n = int(input())
if n == 0:
  print(0)
  print('')
elif n == 1:
  print(1)
  print(1)
elif n == 2:
  print(1)
  print(2)
else:
    s = 1
    summond = '1'
    n = n-1
    while 3*s+2 < n:
      s = s+1
      summond = summond + ' ' + str(s)
      n = n-s
#      print(s,n)
#      print(summond) 
    s = s + 1
    if 2*s+1 <= n:
#      print('first')
      print(s+1)
      print(summond + ' ' + str(s) + ' ' + str(n-s))  
    else:
#      print('second')
      print(s)
      print(summond + ' ' + str(n))
