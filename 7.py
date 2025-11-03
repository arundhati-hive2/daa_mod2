import math
def distance(p1, p2):
    x=math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return x

def minDistance(points):
    n = len(points)
    minDist = float('inf') #set to infinity

    for i in range(n):
        for j in range(i + 1, n):
            dist=distance(points[i], points[j])
            if dist < minDist:
                minDist = dist

    return minDist

points=eval(input("enter the list of points:"))
pts=minDistance(points)
print(pts)