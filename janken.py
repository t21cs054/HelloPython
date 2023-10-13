'''
Created on 2023/10/13

@author: t21cs054
'''
import random

def get_hand(choice):
    if choice == 0: 
        return "グー"
    elif choice == 1: 
        return "チョキ"
    elif choice == 2:
        return "パー"
    else:
        return ""
    

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(choiceA, choiceB):
    if choiceA == choiceB:
        return "引き分け"
    if (choiceA == 0 and choiceB == 1) or (choiceA == 1 and choiceB == 2) or (choiceA == 2 and choiceB == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"

def main():
    choiceA = get_computer_choice()
    choiceB = get_computer_choice()
    print(f"Aの手: {get_hand(choiceA)} v.s. Bの手: {get_hand(choiceB)}")
    result = determine_winner(choiceA, choiceB)
    print(f"-> {result}")

if __name__ == "__main__":
    main()