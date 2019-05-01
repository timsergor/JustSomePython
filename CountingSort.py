# Первая строка содержит число 1≤n≤104, вторая — n натуральных чисел, не превышающих 10. 
# Выведите упорядоченную по неубыванию последовательность этих чисел.

k = int(input())
M = [int(i) for i in input().split()]

def digit4sort(M):
    D1,D2,D3,D4 = [0]*10,[0]*10,[0]*10,[0]*10
    for i in range(len(M)):
        D1[M[i]%10] += 1
        D2[(M[i]//10)%10] += 1
        D3[(M[i]//100)%10] += 1
        D4[(M[i]//1000)%10] += 1
    for i in range(1,10):
        D1[i] += D1[i-1]  
        D2[i] += D2[i-1]  
        D3[i] += D3[i-1]  
        D4[i] += D4[i-1]  
    M1,M2,M3,M4 = list(M),list(M),list(M),list(M)
    for i in range(len(M)):
        s = M[len(M)-1-i]
        M1[D1[s%10]-1] = s
        D1[s%10] -= 1
    for i in range(len(M)):
        s = M1[len(M)-1-i]
        M2[D2[(s//10)%10]-1] = s
        D2[(s//10)%10] -= 1
    for i in range(len(M)):
        s = M2[len(M)-1-i]
        M3[D3[(s//100)%10]-1] = s
        D3[(s//100)%10] -= 1
    for i in range(len(M)):
        s = M3[len(M)-1-i]
        M4[D4[(s//1000)%10]-1] = s
        D4[(s//1000)%10] -= 1      
#  for i in range(M):
    return(M4)

M4 = digit4sort(M)
s = str(M4[0])
for i in range(1,len(M4)):
    s = s + ' ' + str(M4[i])
print(s)  
