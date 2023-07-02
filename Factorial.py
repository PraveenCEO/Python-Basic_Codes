# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
def fact(n):
    factt=1
    for i in range(1,n+1):
        factt=factt*i
    return factt
num=int(input())
result=fact(num)
print(result)
