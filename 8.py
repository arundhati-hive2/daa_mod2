def inp(name):
    rows=int(input("enter number of rows:"))
    cols=int(input("enter number of columns:"))
    print("enter the elements row by row:")
    m=[]
    
    for i in range(rows):
        row = []
        print(f"enter elements for the rows {i+1}:")
        for j in range(cols):
            n=int(input(f"element {j+1}:"))
            row.append(n)
        m.append(row)
    return m, rows, cols

m1=inp("matrix 1")
A=m1[0]
r1=m1[1]
c1=m1[2]
m2=inp("matrix 2")
B=m2[0]
r2=m2[1]
c2=m2[2]


if c1!=r2:
    print("invalid. pls enter same no. of rows for matrix 2 as columns for 1")
else:
    result = []
    for i in range(r1):  #zero initialization
        row = []
        for j in range(c2):
            row.append(0)
        result.append(row)

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j]+=A[i][k]*B[k][j]

    print("resultant matrix:")
    for row in result:
        print(row)
