import random

def equation():
    
    return(random.randint(1,9),random.randint(1,9))

num1,num2=equation()

ans=int(input("How much is "+str(num1)+" times "+str(num2)+"? "))

if(num1*num2==ans):
    
    print("done")
    
    num1,num2=equation()
    ans=int(input("How much is "+str(num1)+" times "+str(num2)+"? "))
    while(num1*num2!=ans):
        
        ans=int(input("No. Please try again. "))
    
    print("done")
else:
    #loop enter correct answer is made
    while(num1*num2!=ans):
        
        ans=int(input("No. Please try again. "))
    
    print("done")