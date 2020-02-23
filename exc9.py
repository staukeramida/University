f=open("number.txt", "r")
y=f.read()
l=len(y)
x=int(y)
syn=0
b=0
while l>1 :
       x*=3
       x+=1
       syn=0
       p=1
       while p!=0 :
           h=x//10
           yp=x%10
           syn+=yp
           p=h
       s=str(syn)
       l=len(s)
       x=syn
       
f.close()
