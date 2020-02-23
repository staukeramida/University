import time
import random

def linebreak(sec=2):
    print('\n'+'*'*60+'\n'+'*'*60+'\n')
    time.sleep(sec)

#list of cards
suit_list=['clubs','diamonds','hearts','spades']
value_list=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']


#list of random card the 0 is the card value the 1 is the card suit
def rand_card():
    rand_suit=random.choice(suit_list)
    rand_value=random.choice(value_list)
    return[str(rand_value),rand_suit]


#takes a card argument and gets the value and the suit of the card
def get_card_value(card):
    return card[0]

def get_card_value(card):
    return card[1]

#print the hand of the player

def deal_player():
    print('\nYou are dealt the five cards:')
    player_hand=[]
    i=0
    while i<5:
        letter_list=['a','b','c','d','e']
        given_card=rand_card()
        if given_card not in player_hand:
            print('%s %s of% s' %(letter_list[i],get_card_value(given_card),get_card_value(given_card)))
            player_hand.append(given_card)
            i=i+1
    return player_hand

#number of card the player wants to discard
def discard_cards():
    time.sleep(4)
    print('\nYou can choose up to 3 cards to discard for new ones')
    print('How many cards you want to swap')
    while True:
        try:
            discard_x_cards=int(input('\n'))
            if valid_discard_num(discard_x_cards):
                break
            else:
                print('That is not allowed you can choose the most 3 cards to swap')
        
        except ValueError:
            print('invalid command, input a number between 0-3')
    return discard_x_cards

#true only if player choose 0-3 cards

def valid_discard_num(discard_num):
    if 0<=discard_num<=3:
        return True

#ask witch want to discard
#if number 0 return none
#else return list of lower-case letters (representing cards) to be discarded
def specify_discard_cards(tot_discarded_cards):
    if tot_discarded_cards==0:
        print('You dont want to change any card')
        time.sleep(2)
        return[]
    else:
        print('the numbers of cards that wil be discarded is %s' % tot_discarded_cards)
        time.sleep(2)
        discard_card_list=[]

        i=0
        while i< tot_discarded_cards:
            print('\nType the letter of card  #%s to be discarded. (a-e)' % (i+1))
            discard_card=input('>').lower()
            if not valid_card_letter(discard_card):
                continue
            if not check_card_exists(discard_card,discard_card_list):
                continue
            discard_card_list.append(discard_card)
            i=i+1
        return discard_card_list

#return true if player input a letter between a-e
#return false and message if the user does not type valid letter
def valid_card_letter(letter_input):
    five_letters=['a','b','c','d','e']
    if letter_input.lower() not in five_letters:
        print("wrong data choose onr card in range a-e")
        return False
    else:
        return True
    
#return true if the player hasnt choose already a letter to discard a card
#return false and print message if the user choose to discard the same card again
#first argument is the inputted letter and second the alread inputed letter
def check_card_exists(letter_input, used_letters):
       if letter_input.lower() not in used_letters:
           return True
       else:
           print('You already chose to discard this card.What else do you want to discard')
           return False

#returns a list of identified cards to be discarded
#first argument a list of requested discard cards
#second argument is the list representing players hand

def identify_discard_cards(discard_list, player_hand):
    cards_to_remove=[]
    for letter in discard_list:
        if letter=='a':
            cards_to_remove.append(player_hand[0])
        if letter=='b':
            cards_to_remove.append(player_hand[1])
        if letter=='c':
            cards_to_remove.append(player_hand[2])
        if letter=='d':
            cards_to_remove.append(player_hand[3])
        if letter=='e':
            cards_to_remove.append(player_hand[4])
    return cards_to_remove
#remove the cards the player wants to discard
#return the remaining cards

def throw_discard_cards(discard_list, player_hand, card_to_chuck):
    for card in cards_to_chuck:
        if card in player_hand:
            player_hand.remove(card)
    return player_hand

#return the hand of the player with the new cards
#make sure the new cards arent the same with the obe the player already have
#print the cards

def receive_new_cards(num_discard_cards, player_hand, cards_to_chuck):
    i=0
    while i<num_discard_cards:
        received_card=rand_card()
        if received_card not in player_hand and received_card not in cards_to_chuck:
            player_hand.append(received_card)
            i+=1
    linebreak()
    print("Your final hand is:")
    time.sleep(2)
    for card in player_hand:
        print(' %s of %s' % (card[0], card[1]))
    return player_hand


#return the hand in order of value


def order_card_values(player_hand, value_list):
    ordered_hand=[]
    for value in value_list:
        for card in player_hand:
            try:
                if int(card[0])==value:
                    ordered_hand.append(card)
            except ValueError:
                if card[0]==value:
                    ordered_hand.append(card)
    return ordered_hand


#function required in the is_straight() function
#return a list of two strings

def concatenate_player_values(ordered_hand):
    player_values=[]
    for card in ordered_hand:
        player_values.append(str(card[0]))

    low_aces_value_str=''.join(player_values)
    trailing_aces=''
    for letter in low_aces_value_str:
        if letter=='A':
            trailing_aces+='A'
    high_aces_value_str=low_aces_value_str[len(trailing_aces):]+ trailing_aces
    return [low_aces_value_str, high_aces_value_str]

#return true if sequential values is in the players hand else false
def is_straight():
    ordered_values_list=concatenate_player_values(ordered_hand)
    for string in ordered_values_list:
        if string in 'A2345678910JQKA':
            return True
        else :
            return False

#return true if all cards are of the same suit else false

def is_flush(player_hand):
    player_hand_suit_list=[]
    for card in player_hand:
        player_hand_suit_list.append(card[1])
    if player_hand_suit_list[1:]==player_hand_suit_list[:-1]:
        return True
    else:
        return False

#check for duplicate card values in the player hands

def check_dup_values(player_hand):
    values_list=[]
    for card in player_hand:
        values_list.append(card[0])
    counted_values=[]
    already_checked_value=[]
    for value in values_list:
        if value not in already_checked_value:
            already_checked_value.append(value)
            if values_list.count(value)==2:
                counted_values.append([value, 2])
            
            if values_list.count(value)==3:
                counted_values.append([value, 3])

            if values_list.count(value)==4:
                counted_values.append([value, 4])
    return counted_values

#store the returned list from check_dup_values as variable
#return the type of the hand the player has on basis of duplicate value cards

def compute_dup_values(player_hand):
    duplicate_values_list=check_dup_values(player_hand)

    if len(duplicate_values_list)==0:
       #no duplicate
        return False

    if len(duplicate_values_list)==1:
        for mini_list in duplicate_values_list:
            if mini_list[1]==4:
                return 'FOUR OF A KIND'
            if mini_list[1]==3:
                return 'THREE OF A KIND'
            if mini_list[1]==2:
                return 'PAIR OF' +str(mini_list[0])+ 's'
    if len(duplicate_values_list)==2:
        #must be two pairs or full house
        for mini_list in duplicate_values_list:
            if mini_list[1]==3:
                return 'FULL HOUSE'
        pair_list=[]
        for mini_list in duplicate_values_list:
            pair=str(mini_list[0])+ 's'
            pair_list.append(pair)
        return 'TWO PARTS OF'+pair_list[0] +'AND' + pair_list[1]

#return the hand the player has
#row from the best to worst hand
def determine_hand(player_hand):
    processed_duplicates=compute_dup_values(player_hand)
    if is_straight() and is_flush(player_hand):
        return 'STRAIGHT FLUSH'
    elif processed_duplicates=='FOUR OF A KIND':
        return 'FOUR OF A KIND'
    elif processed_duplicates=='FULL HOUSE':
        return 'FULL HOUSE'
    elif is_flush(player_hand):
        return 'FLUSH'
    elif is_straight():
        return 'STRAIGHT'
    elif processed_duplicates=='THREE OF A KIND':
        return 'THREE OF A KIND'
    elif processed_duplicates:
        return processed_duplicates
    else:
        return determine_high_card(player_hand)

#return the highest card the player has when the best hand is high card
#aces highest values
def determine_high_card(player_hand):
    reversed_value_list=value_list[::-1]
    for value in reversed_value_list:
        for card in player_hand:
            if card[0]=='A':
                return 'HIGH CARD ACE'
            if card[0]==value:
                return 'HIGH CARD' + str(value)


"""
return a list with two items the one the name of the hand the opponet has
been assigned second a list with 2 values that will provide the strenght for the
hands
"""
def opponent_hand(value_list):
    rand_num=random.randint(0,100)

    opponent_value_cards=[]
    i=0
    #create the list for the two values for the second item of the return
    while i<2:
        rand_value=random.choice(value_list)
        if rand_value not in opponent_value_cards:
            opponent_value_cards.append(rand_value)
            i+=1
    if rand_num<=300:
        opponent_value_cards[0]=str(random.choice(value_list[6:]+['A']))
        opp_hand="HIGH CARD" + opponent_value_cards[0]
    elif rand_num<=700:
        opp_hand="PAIR OF" + str(opponent_value_cards[0])+'s'
    elif rand_num<=900:
        opp_hand='TWO PAIRS(' + str(opponent_value_cards[0]) + 's AND '+ str(opponent_value_cards[1]) +'s)'
    elif rand_num<=950:
        opp_hand='THREE OF A KIND(' +str(opponent_value_cards[0])+ 's)'
    elif rand_num<=975:
        opp_hand='STRAIGHT'
    elif rand_num<=987:
        opp_hand='FLUSH'
    elif rand_num<=995:
        opp_hand='FULL HOUSE (THREΕ' + str(opponent_value_cards[0])+'s AND TWO ' + str(opponent_value_cards[1])+ 's)'
    elif rand_num<=999:
        opp_hand='FOUR OF A KIND(' + str(opponent_value_cards[0])+ 's)'
    else:
        opp_hand='STRAIGHT FLUSH'
    return [opp_hand,opponent_value_cards]

def play_again():
    print('Would you like to play another round y/n ')
    if input('>').lower() in ['yes','y']:
        return True
    else:
        return False

#game loop

while True:
    time.sleep(3.5)
    dealt_hand= deal_player()

    tot_discarded_cards=discard_cards()
    discarded_cards_list=specify_discard_cards(tot_discarded_cards)
    cards_to_chuck=identify_discard_cards(discarded_cards_list, dealt_hand)
    remaining_hand=throw_discard_cards(discarded_cards_list, dealt_hand, cards_to_chuck)
    new_hand=receive_new_cards(tot_discarded_cards, remaining_hand, cards_to_chuck)
    ordered_hand=order_card_values(new_hand, value_list)
    name_player_hand=determine_hand(ordered_hand)

    time.sleep(4)
    print('You reveal your hand:\n%s' % name_player_hand)
    time.sleep(3)
    enemy_hand=opponent_hand(value_list)
    print('\n Your opponent reveals their hand:\n'+ enemy_hand[0])

    if not play_again():
          print('Thanks for playing')
          time.sleep(1)
          break
    linebreak()

            
    


            
    
