dist_matrix = []
print("enter the distance matrix[5][5]:")
for i in range(5):
    row=eval(input("row (5 members): "))
    dist_matrix.append(row)
print("Distance matrix:",dist_matrix)

permutations=[]

source=0 #let index of source city be 0

min_dist=99999 #setting distance to minus one instead of infinity as distance is scalar and cant be negative

best_path=[]

#list of all cities except source
cities=eval(input("enter list of city indices except source (3 cities)"))

n=len(cities)
fact=1 # factorial initialization
k=0
def swap(fn,x,y):
    fn[x],fn[y]=fn[y],fn[x]
    return fn
#perm: npr=n!/(n-r)!
def perm(fn,curr,last):
    if curr==last: #we swap current element with every index after it until the last one
        permutations.append(fn[:])
    else:
        for i in range(curr, last+1):
            swap(fn, curr, i) #swapping current with i
            perm(fn, curr+1, last) #recursion for the remaining
            swap(fn, curr, i) #list reverts to how it was
perm(cities,0,n-1)

print("permutations of cities:")
for p in permutations:
    print(p)

for p in permutations:
    path=[source]+p+[source]
    total_distance=0
    for i in range (len(path)-1):
        total_distance+=dist_matrix[path[i]][path[i + 1]] #path from current to next city
    
    if total_distance<min_dist:
        min_dist=total_distance
        best_path=path

print("minimum distance:", min_dist,"\nbest path:",best_path)
