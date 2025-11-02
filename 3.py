num=int(input("enter a number:"))
lst=[] #list to store binary numbers
temp=num #temporary variable to avoid data loss
bin=0 #binary value will be stores here
while temp>0:
    rem=temp%2 #when we do short division and then reverse the order of remainders, we get binary
    lst.append(rem)
    temp//=2 #continues with the quotient
lst=lst[::-1] #reversing to get the order right
for i in lst:
    bin=bin*10+i #converting list to int
print(num, "in binary is:",bin)