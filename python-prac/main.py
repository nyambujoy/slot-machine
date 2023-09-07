#TECH WITH TIM LEARN PYTHON WITH THIS ONE PROJECT

import random

MAX_LINES=3
MAX_BET = 100   
MIN_BET = 1

ROWS = 3
COLMS = 3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns=[[],[],[]]#they are set up as rows for now but we will rectify [a,b,b] they need to be [a]
                                                                                                  #[b]
                                                                                                  #[c]
    for col in range (cols) :
        column=[]
        current_symbols= all_symbols[:]#this copies a list the slice operator
        for row in range (rows):
            value= random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):#here we spin the col
    for row in range(len(columns[0])) :
        for i,column in enumerate(columns): #enumarate means gives the index aswell as the value
            if i != len(columns) -1:
                print(column[row], "|")
            else:
                print(column[row], )



def deposit():
    while True:
        amount =input("what would you like to deposit? $") 
        if amount.isdigit():#to confirm that its a whole number -negatives wont do
            amount=int(amount)
            if amount > 0:
                break
            else :
                print("amount must be greater than zero")
        else:
            print("please enter a number")        
    return amount        


def get_number_of_lines():
    while True:
        lines = input("how many lines do you want(1-"+ str(MAX_LINES)+")? ")
        if lines.isdigit():#to confirm that its a whole number -negatives wont do
            lines=int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else :
                print("ENTER A VALID NUMBER OF LINES")
        else:
            print("please enter a number")        
    return lines

def get_bet():
    while True:
        amount = input("how much would you like to bet on each line ?")
        if amount.isdigit():#to confirm that its a whole number -negatives wont do
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else :
                print(f"amount be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number")        
    return amount

      
def main():
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        bet = get_bet() 
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you don't have enough to bet that amount ,your current balance is ${balance}")
        else:
            break

   
    print(f"you are betting ${bet} on ${lines} lines. Total bet is equal ${total_bet}")
    print(balance,lines)    
    slots = get_slot_machine_spin(ROWS,COLMS,symbol_count)
    print_slot_machine(slots)

main()    