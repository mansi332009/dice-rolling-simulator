#dice rolling stimulator
import random
import time
player1=input("enter player1 name ")
player2=input("enter player2 name ")
player3=input("enter player3 name ")

count=1
player1_score=0
player2_score=0
player3_score=0

while(count<=3):
    count +=1
    print("rolling the dice")
    time.sleep(5)

    chance1=(random.randint(1,6))
    chance2=(random.randint(1,6))
    chance3=(random.randint(1,6))


    print("player1 rolled a ",chance1)
    print("player2 rolled a ",chance2)
    print("player3 rolled a ",chance3)
    print("---------------new scores------------------")
    
    player1_score +=chance1;
    player2_score +=chance2;
    player3_score +=chance3;
    
    print("player1: ",chance1)
    print("player2: ",chance2)
    print("player3: ",chance3)

if(player1_score>player2_score):
    if(player3_score>player1_score):
        print(player3," wins")
    else:
        print(player1," wins")
elif(player1_score<player2_score):
    if(player3_score>player2_score):
        print(player3," wins")
    else:
        print(player2," wins")
elif(player1_score==player2_score):
    if(player3_score>player1_score):
        print(player3," wins")
else:
    print("match draws")