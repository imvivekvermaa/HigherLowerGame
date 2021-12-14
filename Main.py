from game_data import data
from art import logo
from art import vs
from replit import clear
import random

def higher_lower():
    score=0

    game_mode_on= True

    while game_mode_on:
        a1= random.randint(0, len(data)-1)
        a2= random.randint(0, len(data)-1)
        print(logo)
        a_option= (f"Compare A: {data[a1]['name']}, a {data[a1]['description']}, from {data[a1]['country']}")

        b_option= (f"Compare B: {data[a2]['name']}, a {data[a2]['description']}, from {data[a2]['country']}\n")

        compare_a= int(data[a1]['follower_count'])
        compare_b= int(data[a2]['follower_count'])
        print(a_option)
        print(vs)
        print(b_option)

        if compare_a == compare_b:
            higher_lower()
        
        user_input= input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_input == 'A':
            if compare_a > compare_b:
                score+=1
                clear()
            else:
                print("Sorry You guessed it wrong\n")
                break

        elif user_input == 'B':
            if compare_a < compare_b:
                score+=1
                clear()
            else:
                print("Sorry You guessed it wrong\n")
                break
            
        else:
            print("YOu've entered invaid input!!")
            break
        print(f"Your score is {score}")
        print(a1)
        print(a2)
    clear()
    play_again=input("To play the game again Type 'Y' or 'N' to exit: ").upper()
    if play_again == 'Y':
        clear()
        higher_lower()

a= higher_lower()
print(a)