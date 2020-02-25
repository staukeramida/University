f=open("text.txt", "r")
x=0
y=0
for eachLine in f:
    for char in eachLine:
        x+=1
        if char=="f" or char=="c" or char=="k" or char=="r" :
            #count the bad letters
            x+=1
    
        else:
           #count the good letters 
            y+=1
            
        if char.isspace() or char=="," or char==' '' '' ' or char==".":
            if x>y:
                print('Bad word')
            else:
                print('Good word')
            x=0
            y=0
        
            
           
f.close()

        
               
            
