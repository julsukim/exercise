num=int(input())
L=input().split()
L2=[]
for x in range(num):
    L2.append(int(L[x]))
L2.sort()
print(L2[num//2])