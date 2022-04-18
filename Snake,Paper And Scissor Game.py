import random
list=["rock","paper","scissor"]
Ucount=0
Mcount=0
print("-----------WELCOME TO OUR SNAKE WATER GUN GAME-----------\n\n")
name=input("Please enroll your name-")
print("1.START\n2.EXIT")
a=int(input("enter 1 or 2 :"))
if a==1:
    
    print("You have 10 chance----")
    for i in range(1,11):
        print("ROUND-",i)
        print("1.r=rock\n2.p=paper\n3.s=scissor")
        your_choice=input("Press r or p or s to start this game--")
        if your_choice== "r" :
            print("You select ROCK")
            your_choice="rock"
        elif your_choice== "p" :
            print("You select PAPER")
            your_choice="paper"
        elif your_choice== "s" :
            print("You select SCISSOR")
            your_choice="scissor"
        else:
            print("INVALID INPUT")
            
        choice=random.choice(list)
        
        print("Computer select",choice.upper())
        if your_choice==choice:
            print("GAME DRAW")
            
        elif(choice=="paper" and your_choice=="scissor")or(choice=="rock" and your_choice=="paper")or(choice=="scissor" and your_choice=="rock")  :
            print("You Win")
            Ucount+=1
        else :
            print("Computer Win")
            Mcount+=1
           
else:
    print("Than you for visiting.....")
    
print("RESULT :")
print(f"{name.upper()} score-",Ucount)
print("Computer score-",Mcount)
if Ucount>Mcount:
    print("!!!!!!!Congro you win!!!!!!!!")
else:
    print("------GAME OVER-------")

