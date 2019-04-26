# В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел, не превышающих 10^9, в порядке возрастания, 
# во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих 109. 
# Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=b_i, или −1, если такого j нет.

M = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]
m = M.pop(0)
l = L.pop(0)

import math

def find(M,n):
    l = 0
    r = len(M)-1
    while l <= r:
        m = (l + r)//2    
        if M[m] == n:
            return(m+1)
        elif M[m] > n:
            r = m - 1
        else:
            l = m + 1
    return(-1)   

if len(L) == 0:
    print('')
else:    
    s = str(find(M,L[0]))
    for i in range(1,len(L)):
        s = s + ' ' + str(find(M,L[i]))
    print(s) 
