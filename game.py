import random
print("Rock,paper,scissor game:")
comp_point=0
user_point=0
while True:
    user=input("Enter rock,paper or scissor:")
    choices=["rock","paper","scissor"]
    comp=random.choice(choices)
    print("Your choice:",user)
    print("Computer choice:",comp)
    if comp==user:
        print("It's a tie")
        continue
    elif comp=="rock" and user=="paper":
        print("You win!")
        user_point+=1
    elif comp=="paper" and user=="rock":
        print("Computer wins!")
        comp_point+=1
    elif comp=="scissor" and user=="paper":
        print("Computer wins!")
        comp_point+=1
    elif comp=="paper" and user=="scissor":
        print("You win!")
        user_point+=1
    elif comp=="rock" and user=="scissor":
        print("Computer wins!")
        comp_point+=1
    elif comp=="scissor" and user=="rock":
        print("You win!")
        user_point+=1
    else:
        print("Invalid input")
        continue
    ans=input("Do you want to play again? (yes or no):")
    if ans=="yes" or ans=="YES":
        continue
    else:
        print("Game over")
        break
print("Scorecard:")
print("Your score:",user_point)
print("Computer's score:",comp_point)
