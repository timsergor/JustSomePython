# Вычислите расстояние редактирования двух данных непустых строк длины не более 102, содержащих строчные буквы латинского алфавита.

s = input()
t = input()

def dif(x,y):
    if x == y:
        return(0)
    else:
        return(1)  

A = [[]]
for i in range(len(s)+1):
    A[0].append(i)
for j in range(1,len(t)+1):
    A.append([j]+[0]*len(s))
for i in range(len(s)):
    for j in range(len(t)):
        a = A[j+1][i] + 1
        b = A[j][i+1] + 1
        c = A[j][i]+dif(s[i],t[j])
        A[j+1][i+1] = min(a,b,c)
print(A[len(t)][len(s)]) 
