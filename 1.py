obj=input("enter the data you want to permute:")
n=len(obj)
lst=list(obj) #converting to list
fact=1 # factorial initialization
k=0
def swap(fn,x,y):
    fn[x],fn[y]=fn[y],fn[x]
    return fn
#perm: npr=n!/(n-r)!
def perm(fn,curr,last):
    if curr==last: #we swap current element with every index after it until the last one
        print("".join(fn))
    else:
        for i in range(curr, last+1):
            swap(fn, curr, i) #swapping current with i
            perm(fn, curr+1, last) #recursion for the remaining
            swap(fn, curr, i) #list reverts to how it was
perm(lst,0,n-1)