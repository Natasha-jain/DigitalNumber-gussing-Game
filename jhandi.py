
import random
print('welcome to the game \n enter no between 1-50 \n u have 5 chances')
a=(random.randrange(1,50))
i=0
while(i<5):
    b=int(input("enter your no."))
    i=i+1
    if(b==a):
        print("you won")
        break
    elif(b>a):
        print("high")
    else:
        print("low")
        


print("game over")            

            
            
