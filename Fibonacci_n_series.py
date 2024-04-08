num=int(input("Enter Limit:"))
n1=int(input())
n2=int(input())
print(n1,n2,end=" ")
if num<0:
    print(num)
elif num==1:
     print(num)
elif num>1:
    for i in range(2,num):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")

'''
Output:
Enter Limit:5
0
1
0 1 1 2 3 
'''


        

     
