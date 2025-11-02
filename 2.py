obj=input("enter the data you want to permute:")
r=int(input("enter the length you want for the data:"))
n=len(obj)
lst=list(obj) #converting to list
k=0
res=[]
#combination ncr=n!/r!(n-r)!
def comb(start, current):
    if len(current) == r: #if it satisfies the length req we print a combination
        print("".join(current))
    for i in range(start, n): #else we add more elements to the current until =r
        current.append(lst[i]) #adding element of index i
        comb(i + 1, current) #combination for next element
        current.pop() # revert to how it wass

comb(0, [])