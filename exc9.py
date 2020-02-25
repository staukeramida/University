test_text=input('enter a number:')
if test_text.isnumeric():
  x=int(test_text)   
  while x>9:
     x*=3
     x+=1
     p=1
     while p!=0:
       h=x//10
       yp=x%10
       p=h
       x=yp
       print(h,yp)
else:
    print('you didnt write a number')
