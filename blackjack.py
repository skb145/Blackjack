import random 

print("\n" + "Hello, Welcome to Sriram's Blackjack table!" + "\n") 

def blackjack():
    winnings = 0 # When playing the game it resets the money value to 0, or starts it at 0
    while True:
        hand_num = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10,'Ace': 11}
        hand_keys = list(dict.keys(hand_num)) # Picks a key from han_num (Ex: 'Queen')
        hand_suit = ['Clubs', 'Diamonds','Hearts','Spades'] 
        cards = []
        numbers = []
        values = []
        split_cards = []
        split_values = []
        # All of the empty lists were created to append to later
        ace_counter = 0
        card_sum = 0
        action_counter = 0
        

        try:
            # Ensures that a number typed so the code won't break
            while True:
                bet = int(input("\n"+ "How much money would you like to wager: "))
                if bet > 1000000:
                    print("The max bet amount is 1,000,000")
                else:
                    break
        except ValueError:
            print("Please enter a number")
            continue
        
        print("\n")
        card_index = 0
        
        def card_gen():
                number = random.choice(hand_keys) 
                nonlocal numbers
                value = int(hand_num[number]) #Gives the value of key (Ex: value = 10 when 'Queen')             
                suit = random.choice(hand_suit) 
                the_card = f"{number} Of {suit}" #Combines number & suit (Ex:'Queen Of Spades')
                cards.append(the_card)
                numbers.append(number)
                values.append(value)
                nonlocal card_sum
                card_sum = sum(values) #Adds the values of the values list 
                
                if len(numbers) <= 2:
                    print("Your card is: " + the_card)
                elif len(numbers) > 2:
                    for card_1 in cards:
                        print("Your card is: " + card_1)
 
                if number == 'Ace':
                    nonlocal ace_counter
                    ace_counter = 1 + ace_counter
        
        for card in range (2): 
            card_gen() #When playing it will give 2 Cards (Ex: '4 of Hearts, Queen Of Spades', and card_sum would be 14)
        
        if card_sum == 21:
            try: 
                    4 + "11"
            except TypeError: #Forcing a value to end the blackjack function, getting 21 on inital 2 cards is an automatic win
                    print("Blackjack!")
                    winnings = int((1.5 * bet) + winnings)
                    if winnings >= 0:
                        print("\n" + f"Your current winnings are: ${winnings}")
                    else:
                        print("\n" + f"Your current winnings are: -${abs(winnings)}")
                    continue
        
        def Ace_func(): #When given an Ace, you can choose the value to be either 1 or 11
            while True:
                ace_action = input("Would you like your Ace to be 1 or 11: ")
                match ace_action:
                    case '1':
                        ace_value = 1
                        ace_index = numbers.index('Ace')
                        values[ace_index] = ace_value
                        nonlocal card_sum
                        card_sum = sum(values)
                        break
                    case '11':
                        card_sum = sum(values)
                        break
                    case _:
                        print("Please pick either 1 or 11")

        if ace_counter == 1:
            Ace_func()
        elif ace_counter == 2:
            card_sum = 12 #Having 2 Aces where is each an 11 would lead you to automatically bust, so value has to be 12
        
        def dd(): #Option to double initial bet and you can only draw one more card
            if len(split_cards) < 1:
                double_down = input("\n"+ "Would you like to double down (Please type yes or no): ")
                if double_down == 'yes':
                    nonlocal action_counter
                    action_counter =  action_counter + 1
                    nonlocal bet
                    bet = bet * 2
        
        if len(set(numbers)) != len(numbers):
            split = input("Would you like to split your hands (Please type yes or no): ")
            match split:
                case 'yes':
                    split_cards.append(cards[1])
                    split_values.append(values[1])
                    cards.pop(1)
                    numbers.pop(1)
                    values.pop(1)
                    card_gen()
                    Ace_func()
 
        print("\n" + f"Your count is: {card_sum}") # (Ex: '4 of Hearts, Queen Of Spades', and card_sum would be 14)
        card_index = 2
        
        while action_counter < 1:
            
            def stand():
                nonlocal winnings
                nonlocal bet
                print("\n" + f"Your final score is: {card_sum}")
        
                while True:
                    dealer = input("\n"+ "Lets find out what the dealer has (type yes): ")

                    dealer_cards = [17, 18, 19, 20, 21, 22] 
                    dealer_hand = random.choices(dealer_cards, weights=(16.58, 14.81, 13.48, 17.58, 12.18, 25.37), k=1)
                    dealer_hand = int(dealer_hand[0])
                    
                    insurance_list = ['Ace', 'Not Ace']
                    insurance_ace = random.choices(insurance_list, weights=(8, 92), k=1)
                    insurance_ace = insurance_ace[0]

                    if insurance_ace == 'Ace':
                        while True: 
                            insurance = input("\n"+ "Would you blackjack insurance (Please type yes or no): ")

                            match insurance:
                                case 'yes':
                                    try:
                                        while True:
                                            print(f"Your original bet is: {bet}, it can only be at most half the original bet")
                                            side_bet = int(input("\n"+ "Enter bet amount: "))
                                            if side_bet > int(0.5 * bet):
                                                print("The max side bet allowed is half the initial")
                                            else:
                                                break
                                    except ValueError:
                                        print("Please enter a number")
                                        continue
                                    
                                    insurance_blackjack = ["21", "Not 21"]
                                    insurance_21 = random.choices(insurance_blackjack, weights=(32.7, 67.3), k=1)
                                    insurance_21 = insurance_21[0]
                                    if insurance_21 == '21':
                                        side_bet = 2 * side_bet
                                        bet = bet + side_bet
                                    elif card_sum > dealer_hand:
                                        bet = bet - side_bet
                                    break
                                case _:
                                    break
                        
                    match dealer:
                        case 'yes':
                            if dealer_hand == 22:
                                print("Dealer busts, You Win!")
                                winnings = winnings + bet
                                if winnings >= 0:
                                    print("\n" + f"Your current winnings are: ${winnings}")
                                else:
                                    print("\n" + f"Your current winnings are: -${abs(winnings)}")
                            elif card_sum > dealer_hand:
                                print("\n" + f"The dealer's score is {dealer_hand}")
                                print("Your score is higher than the dealer's, You Win!")
                                winnings = winnings + bet
                                if winnings >= 0:
                                    print("\n" + f"Your current winnings are: ${winnings}")
                                else:
                                    print("\n" + f"Your current winnings are: -${abs(winnings)}")
                            elif card_sum < dealer_hand:
                                print(f"The dealer's score is {dealer_hand}")
                                print("Your score is lower than the dealer's, Sorry Try Again!")
                                winnings = winnings - bet
                                if winnings >= 0:
                                    print("\n" + f"Your current winnings are: ${winnings}")
                                else:
                                    print("\n" + f"Your current winnings are: -${abs(winnings)}")
                            else:
                                print(f"The dealer's score is {dealer_hand}")
                                print("Your score is the same than the dealer's!")
                                if winnings >= 0:
                                    print("\n" + f"Your current winnings are: ${winnings}")
                                else:
                                    print("\n" + f"Your current winnings are: -${abs(winnings)}")
                            break     
            
            action = input("\n"+ "Would you like to hit or stand: ") 

            match action:
                case 'hit':
                    dd()
                    card_gen()
                    
                    if (numbers[card_index] == 'Ace' or ace_counter == 1):
                        Ace_func()
                    elif ace_counter == 2:
                        if 1 in values:
                            sum(values)
                        else:
                            card_sum = sum(values) - 10
                    
                    
                    print("\n" + f"Your count is: {card_sum}")
                    
                    if card_sum > 21:
                        if len(split_cards) == 1:
                            winnings = winnings - bet
                            print("Bust, Your Over 21")
                            if winnings >= 0:
                                print("\n" + f"Your current winnings are: ${winnings}")
                                cards.clear()
                                cards.append(split_cards[0])
                                values.clear()
                                values.append(split_values[0]) 
                                split_cards.append("Hello")
                            else:
                                print("\n" + f"Your current winnings are: -${abs(winnings)}")
                                cards.clear()
                                cards.append(split_cards[0])
                                values.clear()
                                values.append(split_values[0])
                                split_cards.append("Hello")
                        else:
                            winnings = winnings - bet
                            print("Bust, Your Over 21")
                            if winnings >= 0:
                                print("\n" + f"Your current winnings are: ${winnings}")
                            else:
                                print("\n" + f"Your current winnings are: -${abs(winnings)}")
                            break
                    card_index = card_index + 1
                
                    
                    if ('Ace' in numbers and len(split_cards) == 1):
                        action_counter =  action_counter + 1

                    if action_counter == 1:
                        stand()
                
                case 'stand':
                    if len(split_cards) == 1:
                        stand()
                        cards.clear()
                        values.clear()
                        cards.append(split_cards[0])
                        values.append(split_values[0]) 
                        split_cards.append("Hello")
                    else:
                        stand()
                        break

        while True:
            countine_playing = input("\n"+ "Would you like to continue playing? (Please type yes or no): ")
            match countine_playing:
                case 'no':
                    print("\n" + "Thank you for playing!")
                    if winnings >= 0:
                        exit(f"You've won a total of: ${winnings}")
                    else:
                        exit(f"You've lost a total of: ${abs(winnings)}")
                case 'yes':
                    break
blackjack()