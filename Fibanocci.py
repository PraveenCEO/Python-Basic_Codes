num = int(input())
if num == 0:
   print(num)
elif num < 0:
     print("enter valid num")
else:
    n1,n2=0,1
    print(n1, n2, end=" ")
    for i in range(2,num):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3, end=" ")



