import time
now=time.strftime("%d/%m/%Y")
f=open("date.txt","r")
date=f.readline()
k=date[0:2]
l=date[3:5]
o=date[6:10]
p=now[0:2]#now day
q=now[3:5]#now month
r=now[6:10]#now year
d=int(k)
m=int(l)
y=int(o)
n_m=int(q)
n_y=int(r)
n_d=int(p)
n_day=0
feb_day=0
day=0
ny_d=0
#if the year is a leap year or not
if y%4==0 and y%100!=0 or y%400==0:
    y_d=366
    feb_day=29
else:
    y_d=365



#if the now year is a leap year or not
        
if n_y%4==0 and n_y%100!=0 or n_y%400==0:
        ny_day=366
else:
        ny_day=365


#the days of the month
        
if m%2!=0:
    day=31
    print("The number of the days at this month is:",day)
if m%2==0:
   day=30
   if m==8:
     day=31

   if m==2 and y_d==366: 
         day=29 
    
          
   print("The number of the days at this month is:",day)

#the days of now month

   if n_m%2!=0:
     n_day=31

   if n_m%2==0:
       n_day=30
       if n_m==8:
           n_day=31
       if n_m==2:
           if ny_day==366:
              n_day=29
           else:
              n_day=30

#the days until now year

yp=day-d
n_yp=n_day-n_d
ypm=12-m
n_ypm=12-n_m
yp=int(yp)
n_yp=int(n_yp)
ypm=int(ypm)
n_ypm=int(n_ypm)

#days until the end of the year
if ypm%2==0:
    meres=((ypm/2)+1)*31+((ypm/2)-1)*30+yp
    if m<2 and y_d==365:
           meres-=1
    if m<8:
        meres+=1
    
else:
    meres=(ypm/2)*30+((ypm/2)+1)*31+yp
    if m<2 and y_d==365:
           meres-=1
    if m<8:
        meres+=1

#days until the end of the now year

if n_ypm%2==0:
    n_meres=((n_ypm/2)+1)*31+((n_ypm/2)-1)*30+yp
    if n_m<2 and ny_d==365:
           n_meres-=1
    if n_m<8:
        n_meres+=1
    
else:
    n_meres=(n_ypm/2)*30+((n_ypm/2)+1)*31+yp
    if n_m<2 and ny_d==365:
           n_meres-=1
    if n_m<8:
        n_meres+=1


x=((n_y-1)-(y+1)) 
       
final=((x/4)+1)*366+(x-((x/4)+1))*365+meres+n_meres
print("The days until the today date is:",+final)

final1=final*24
print("The hours until the today date is:",+final1)

final2=final1*60*60
print("The seconds until the today date is:",+final2)




    
f.close()
        
