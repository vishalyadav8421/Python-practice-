'''
betting game
balance : 100
user >> num (0-9)>> 5 
user >> bet amount (amt) 10
random >> randomrange(0,9) == randomnumber >>6
randomnumber == user 5 == 6 F balance -10 = 90

'''
import random as r 
def betting_game():
    initial_balance = 100
    while True:
        print(f"Your balance is : {initial_balance}Rs")
        user_input= input("Enter a number (0-9) to bet on (q to quit) : ")
        if user_input.lower() == 'q':
            break
        if not user_input.isdigit() or int(user_input)< 0 or int(user_input) > 9:
            print("Please enter a valid number between 0-9")
            continue
        bet_number = int(user_input)#konse number pe lagana hai 5
        bet_amount = int(input(f"Enter amount to be bet on number {bet_number} : "))#kitna rupya lagana hai
        if bet_amount > initial_balance:
            print(f"Insufficent balance {initial_balance}, please enter a lower bet amount")
            continue
        random_number = r.randrange(0,10)

        if random_number == bet_number :
            initial_balance = initial_balance + (bet_amount*2)-(bet_amount)
            print(f"The drawn number is {random_number}")
            print(f"Congratulations you won the bet your new balance is {initial_balance}")
        else :
            initial_balance = initial_balance - (bet_amount)
            print(f"The drawn number is {random_number}")
            print(f"Opps that was close !! better luck next time updated balance is {initial_balance} ")
    print("Thank you for playing the game !!!!!!!")
                  
        
betting_game()        
            
        
        
    
    
