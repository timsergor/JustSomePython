'''
G = []
k = int(input())
for i in range(k):
  G = G + [[int(i) for i in input().split()]]
print(G)
'''
k = 5
G = [[1, 5], [3, 8], [34, 56], [3, 89], [19, 23]]
g = []
print(G)
for i in range(len(G)-1):
  for j in range(len(G)-i):
    if G[i][1] > G[i+j][1]:
      g = G[i]
      G[i]=G[i+j]
      G[i+j]=g
      print(G)
print(G)

amount = 0
points = ''
last = 0
if len(G) == 0:
    print(0)
else:    
  amount += 1
  last = G[0][1]
  points = points + str(last)
  print(amount)
  print(points)
  for i in range(1,len(G)):
    if last < G[i][0]:
      amount += 1
      last = G[i][1]
      points = points + ' ' + str(last)
      print(amount)
      print(points)