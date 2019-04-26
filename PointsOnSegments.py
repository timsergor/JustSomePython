# По данным k отрезкам находит множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.

G = []
k = int(input())
for i in range(k):
    G = G + [[int(i) for i in input().split()]]

for i in range(k-1):  # упорядочивает по последним точкам отрезков
    for j in range(len(G)-i):
        if G[i][1] > G[i+j][1]:
            g = G[i]
            G[i]=G[i+j]
            G[i+j]=g
amount = 0
points = ''
last = 0
if len(G) == 0:
    print(0)
else:    
    amount += 1
    last = G[0][1]
    points = points + str(last)
    for i in range(1,len(G)):
        if last < G[i][0]:
            amount += 1
            last = G[i][1]
            points = points + ' ' + str(last)
print(amount)
print(points)    
