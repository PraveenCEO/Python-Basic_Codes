def armstrong(num,d,temp,sum1):
    if temp<0:
        return False
    elif temp==0:
        if sum1==num:
            return True
        else:
            return False
    digit = temp % 10
    cube = digit ** d
    sum1 = sum1 + cube
    temp //= 10
    return armstrong(num,d,temp,sum1)
num=int(input())
sum1=0
d=len(str(num))
temp=num
result = armstrong(num,d,temp,sum1)
if result:
    print("armstrong")
else:
    print("not armstrong")

