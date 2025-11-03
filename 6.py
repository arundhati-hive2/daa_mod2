v=eval(input("enter list of values:"))
w=eval(input("enter list of weights:"))
c=int(input("enter capacity:"))
n=len(v)

mv=0
bc=[]

def comb(s,cur):
    global mv,bc
    tw=0
    tv=0
    for i in cur:
        tw+=w[i]
        tv+=v[i]
    if tw<=c and tv>mv:
        mv=tv
        bc=cur[:]
    for i in range(s,n):
        cur.append(i)
        comb(i+1,cur)
        cur.pop()

comb(0,[])
print("best combo:",bc)
tw=0
print("max value:",mv)
