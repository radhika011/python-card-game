import random
def convert_royals_to_commons(value):
    if(value=='Ace'):
        value = 14
    elif(value=='King'):
        value =13
    elif(value=='Queen'):
        value = 12
    elif(value=='Jack'):
        value = 11
    return value

class Card:
    def __init__(self,suit,value):                            #attributes of a card - suit and value
        self.suit = suit
        self.value = value
    def show(self):                                            #returns the suit and value of the card in the required format
        return "{} of {}".format(self.value,self.suit)
    def return_value(self):
        return self.value
class Deck:
    def __init__(self):
        self.deck =[]                                          #declaring an array to work with in the class
    def build(self):                                           #method to buid the deck
        for i in ('Spades','Clubs','Diamonds','Hearts'):
            for j in ('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'):
                self.deck.append(Card(i,j))                     #creating instances of Card class and appending them to deck
    def show_deck(self):                                       #method to display the entire deck from index 0 in deck to 51 since there are 52 cards
        for i in range(0,len(self.deck),+1):
            print(Card.show(self.deck[i]))
    def shuffle(self):                                          #using Python's shuffle() function to shuffle the cards
        random.shuffle(self.deck)
    def drawCard(self):
        return self.deck.pop()                                     #using Python's pop() function to take the last card in the pile and remove it from the deck. Last index element will be removed from the array
    def end_game(self):
        if(len(self.deck)==0):
            print('Game Over!!!')
            no = 0
        
class Player:
    def __init__(self,name,deck):                               #attributes of a player - name
        self.hand = []
        self.name = name
        self.deck = deck
    def draw(self):                                             #drawing a card from the deck and appending it the the hand of the player(hand is different for each instance of the class)
        self.hand.append(self.deck.drawCard())
    def show_hand(self,name):                                   #showing the entire hand of the player using the show() function in Card class in the required format              
        print(name+"'s hand:")
        for i in range(0,len(self.hand)):
            print(Card.show(self.hand[i]))
        print('\n')
    def remove_card(self):
        return self.hand.pop()
def main():
    name1 = input("Enter your name(Player 1):")
    name2 = input("Enter your name(Player 2):")
    score1 = 0
    score2 =0
    deck1 = Deck()                                              #deck1 is the instance of Deck class
    deck1.build()                                               #buiding the deck1
    #deck1.show_deck()                                          #displaying deck1
    deck1.shuffle()                                            #shuffling the deck1
    #deck1.show_deck()                                          #displaying shuffled deck deck1
    #print(Card.show(deck1.draw()))
    player1 = Player(name1,deck1)
    player2 = Player(name2,deck1)
    no = 1
    while(no):
        player1.draw()
        player1.show_hand(name1)
        player2.draw()
        player2.show_hand(name2)
        hand_length1 = len(player1.hand)-1
        hand_length2 = len(player2.hand)-1
        value1 = Card.return_value(player1.hand[hand_length1])
        value2 = Card.return_value(player2.hand[hand_length2])
        value1 = convert_royals_to_commons(value1)
        value2 = convert_royals_to_commons(value2)
        #print(value1)
        #print(value2)
        if(value1!=value2):
            if(value1>value2):
                player1.hand.append(player2.remove_card())
                score1 = score1+1
                
            else:
                player2.hand.append(player1.remove_card())
                score2=score2+1
        else:
            print("WAR!!!!!")
            player1.draw()
            player1.draw()
            player2.draw()
            player2.draw()
            hand_length1 = len(player1.hand)-1
            hand_length2 = len(player2.hand)-1
            print("WAR HANDS!!!")
            player1.show_hand(name1)
            player2.show_hand(name2)
            print('\n')
            value1 = Card.return_value(player1.hand[hand_length1])
            value2 = Card.return_value(player2.hand[hand_length2])
            value1 = convert_royals_to_commons(value1)
            value2 = convert_royals_to_commons(value2)
            if(value1!=value2):
                if(value1>value2):
                    player1.hand.append(player2.remove_card())
                    player1.hand.append(player2.remove_card())
                    player1.hand.append(player2.remove_card())
                    score1 = score1+3
                    
                else:
                    player2.hand.append(player1.remove_card())
                    player2.hand.append(player1.remove_card())
                    player2.hand.append(player1.remove_card())
                    score2=score2+3
            
        print('\n')    
        print("After round:")
        player1.show_hand(name1)
        player2.show_hand(name2)
        print(name1+"'s score:{}".format(score1))
        print(name2+"'s score:{}".format(score2))
        deck1.end_game()
        if(no!=0):
            choice = input('Next Round?(Y/N):')
            if(choice=='N' or choice=='n'):
                no =0
        
        
                
        
        
        
if(__name__=='__main__'):
    main()
