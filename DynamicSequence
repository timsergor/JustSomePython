# Дано целое число 1≤n≤103 и массив A[1…n] натуральных чисел, не превосходящих 2⋅109. Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n длины k, в которой каждый элемент делится на предыдущий (формально: для  всех 1≤j<k, A[ij]|A[ij+1]).

# put your python code here
k = int(input())
M = [int(i) for i in input().split()]

def DS(M):
    L = [1]*len(M)
    for i in range(len(M)):
        for j in range(i):
            if L[j]+1 > L[i] and M[i]%M[j] == 0:
                L[i] = L[j] + 1
    k = 0
    for i in range(len(M)):
        if L[i] > k:
            k = L[i]
    return(k)

print(DS(M))
