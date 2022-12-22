import math

#sine of angles ranging from 0 to 345 in 15° increment
for k in range(24):
    print("sin("+str(15*k)+"):",round(math.sin(15*k),4))

#to leave a blank line inbetween sine and cos values we used this function "\n"
print("\n")     

#cosine of angles ranging from 0 to 345 in 15° increment
for k in range(24):
    print("cos("+str(15*k)+"):",round(math.cos(15*k),4))
