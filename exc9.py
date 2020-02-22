s=0
f=open("test.txt", "r")
if f.mode == 'r':
   y=f.read()
   l=len(y)
   x=int(y)
   while s<l :
       x*=3
       x+=1
       syn=0
       p=1
       while p!=0 :
           h=x/10
           yp=x%10
           syn+=yp
           x=h
           p=h
           print(x)
       x=syn
       s+=1
f.close()
