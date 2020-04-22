# ENCRYPTION OF A STRING
import math as m

s=input()
s=s.replace(" ","")
l=len(s)
col=m.ceil(m.sqrt(len(s)))
row=m.floor(m.sqrt(len(s)))
print(l,col,row,end="  ")
for i in range(0,col):
    j=i
    while j<l:
        print(s[j],end="")
        j+=col
    print(" ",end="") 
