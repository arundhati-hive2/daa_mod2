weight=eval(input("enter list of 6 weights:"))
value=eval(input("enter list of 6 values:"))
capacity=int(input("enter capacity limit:"))

n=6
maxv=0
best_set=0

for i in range(2**n):
    totw=0 #total weight
    totv=0 #total value
    
    for j in range(2**n):
        if i&(1<<j): #tests whether bit j of i is 1. 
            #1<<j shifts 1 left by j places. & is bitwise-and. 
            # if result nonzero, item j is included.
            totw+=weight[j]
            totv+=value[j]
            
    if totw<=capacity and totv>maxv:
        maxv=totv
        best_set=i
        
print("best combination (binary):",format(best_set,'0'+str(n)+'b'))
print("items included:",end=" ")
for j in range(6):
    if best_set&(1<<j):
        print(j+1,end=" ")
print("\nmaximum value=",maxv)
