f=open("text.txt", "r")
x=0
y=0
for eachLine in f:
    for char in eachLine:
        if char==f or char==c or char==k or char==r:
          y+=1
        else
          x+=1
        if char=='' or char==',' or char=='.' :
            if y>x :
                print("It's a bad word")
                x=0
                y=0
            else:
                print("It's a good word")
                x=0
                y=0
f.close()

        
               
            
