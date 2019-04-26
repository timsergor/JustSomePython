# Переводит строку из латинских букв в кратчайший вариант перекодированнй строки с расшифровкой. Первой строкой число различных символов в инпуте и длина аутпута.

s = input()

def convert(s):
  M = [0]*27
  for i in range(len(s)):
    M[ord(s[i])-97] += 1
  return(M)    


def HC(M):
  N = []
  for i in range(len(M)):
    if M[i] > 0:
      N = N + [[chr(i+97), M[i], '']]
  return(N)

def step(N):
  a = 0
  while len(N[a]) >3 :
    a += 1
  b = len(N)-1
  for i in range(a+1,len(N)):
    if N[i][1] <= N[a][1] and (i != a) and len(N[i]) < 4:
      b = a
      a = i
    elif N[i][1] < N[b][1] and len(N[i]) < 4:
      b = i
  N = N + [[N[a][0] + ' ' + N[b][0], N[a][1]+N[b][1], '']]
  N[a][2] = N[a][2] +'0'
  N[a] = N[a]+[len(N)-1]
  N[b][2] = N[b][2] + '1'
  N[b] = N[b]+[len(N)-1]
  return(N)

def getcode(M,x):
  s = ''
  while x < len(M)-1:
    s = M[x][2] + s
    x = M[x][3]
  return(s)

'''
sripvprijipejipipwpjiwapoapoapopapopjovpoapovo
aaaabbbbccccdddd
s = 'vsvsdvtnryjntrhjergwrpfwepofjewpojepwp'
'''

if len(s) == 0:
  print('0 0')
  print()
elif len(s) == 1:
  print('1 1')
  print(s + ': 0')
  print(0)
else:
  M = HC(convert(s))
  k = len(M)
  if k == 1:
    print('1 ' + str(len(s)))
    print(str(s[0]) +': 0')
    print('0'*len(s))
  else:
    for i in range(k-1):
      M = step(M)
    N = []  
    for i in range(k):
      M[i] = M[i] + [getcode(M,i)]
      N = N + [M[i][0]]
    translation = ''  
    for i in range(len(s)):
      translation = translation + M[N.index(s[i])][4]
    print(str(len(N)) + ' ' + str(len(translation)))
    for i in range(len(N)):
      print(N[i] + ': ' + str(M[i][4]))
    print(str(translation))  