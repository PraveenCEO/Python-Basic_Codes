# # Palindrome with numbers!!!
num=int(input())
rev=0
temp=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")
    
# ------------------------------------------------------------------------

# Palindrome with string
string=str(input())
rev_string=""
for i in string:
    rev_string=i+rev_string
if(string==rev_string):
    print("palindrome")
else:
    print("not palindrome")
