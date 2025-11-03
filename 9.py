import random
import time

otp=f"{random.randint(0,9999):}" #generating  and adding as value for otp
print("generated otp:",otp)

start=time.time()
attempts=0

for i in range(10000):
    guess=f"{i:04d}" #4 digit string w leading 0s
    attempts+=1
    if guess==otp:
        end=time.time()
        print("otp found:",guess)
        print("total attempts:",attempts)
        print("time taken:",round(end-start,4),"seconds")
        break
else:
    print("otp not found")
