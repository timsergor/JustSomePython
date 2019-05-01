def Up(M,i):
  if M[i] > M[(i-1)//2]:
    a = M[i]
    M[i] = M[(i-1)//2]
    M[(i-1)//2] = a
    Flag = True
  else:
    Flag = False  
  return(M,Flag)

def Insert(M,n):
  if len(M) == 0 or M[len(M)-1] != -1:
    M = M +[n]
  else:
    M[len(M)-1] = n  
  Flag = True
  i = len(M)-1
  while Flag == True and i>0:
    M,Flag = Up(M,i)
    i = (i-1)//2 
  return(M)  

def ExtractMax(M):
  if len(M) == 0:
    print('Oops')
  else:
    print(M[0])
    k = 0
    while k*2+2 < len(M):
      if M[2*k+1] >= M[2*k+2]:
        M[k] = M[2*k+1]
        k = 2*k+1
      else:
        M[k] = M[2*k+2]
        k = 2*k + 2
    if k*2+1 < len(M):
      M[k] = M[2*k+1]  
      k = k*2 +1
    M[k] = -1
    while len(M) > 0 and M[len(M)-1] == -1:
      M.pop()
  return(M)   

M = []
k = int(input())
for i in range(k):
  y = [s for s in input().split()]
  if len(y) == 1:
    M = ExtractMax(M)
  else:
    M =Insert(M,int(y[1]))  
  print(M)
