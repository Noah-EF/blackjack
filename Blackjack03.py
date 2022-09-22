#Blackjack code version 0.3
#Basic Blackjack functionality
#Completed: deck nonreplacement, input error resiliance
#Lacks: rules customization, more advanced input processing, proper ace coding,
#splitting, betting, results recording, saving, GUI
import random, copy
print('Welcome to Blackjack')
global active
active = True
over = False
cards = [['Ace of Hearts', 'Ace of Diamonds', 'Ace of Clubs', 'Ace of Spades',
          'Two of Hearts', 'Two of Diamonds', 'Two of Clubs', 'Two of Spades',
          'Three of Hearts', 'Three of Diamonds', 'Three of Clubs', 'Three of Spades',
          'Four of Hearts', 'Four of Diamonds', 'Four of Clubs', 'Four of Spades',
          'Five of Hearts', 'Five of Diamonds', 'Five of Clubs', 'Five of Spades',
          'Six of Hearts', 'Six of Diamonds', 'Six of Clubs', 'Six of Spades',
          'Seven of Hearts', 'Seven of Diamonds', 'Seven of Clubs', 'Seven of Spades',
          'Eight of Hearts', 'Eight of Diamonds', 'Eight of Clubs', 'Eight of Spades',
          'Nine of Hearts', 'Nine of Diamonds', 'Nine of Clubs', 'Nine of Spades',
          'Ten of Hearts', 'Ten of Diamonds', 'Ten of Clubs', 'Ten of Spades',
          'Jack of Hearts', 'Jack of Diamonds', 'Jack of Clubs', 'Jack of Spades',
          'Queen of Hearts', 'Queen of Diamonds', 'Queen of Clubs', 'Queen of Spades',
          'King of Hearts', 'King of Diamonds', 'King of Clubs', 'King of Spades'],
         [1, 1, 1, 1,
          2, 2, 2, 2,
          3, 3, 3, 3,
          4, 4, 4, 4,
          5, 5, 5, 5,
          6, 6, 6, 6,
          7, 7, 7, 7,
          8, 8, 8, 8,
          9, 9, 9, 9,
          10, 10, 10, 10,
          10, 10, 10, 10,
          10, 10, 10, 10,
          10, 10, 10, 10]]
usedCards = []
deck = []
playerTotal = int(0)
hand = []
dealerTotal = int(0)
dealerHand = []
def dealPlayer():
    global playerTotal
    cardId = random.randint(0, len(deck[0])-1)
    hand.append(deck[0][cardId])
    #print(cardId)
    playerTotal += deck[1][cardId]
    usedCards.append(deck[0][cardId])
    deck[0].pop(cardId)
    deck[1].pop(cardId)
    return
def dealer():
    global dealerTotal
    cardId = random.randint(0, len(deck[0])-1)
    #print(cardId)
    dealerHand.append(deck[0][cardId])
    dealerTotal += deck[1][cardId]
    usedCards.append(deck[0][cardId])
    deck[0].pop(cardId)
    deck[1].pop(cardId)
    return
def shuffle():
    global deck
    deck = copy.deepcopy(cards)
def deal():
    global playerTotal, dealerTotal
    playerTotal = int(0)
    dealerTotal = int(0)
    hand.clear()
    dealerHand.clear()
    dealer()
    dealer()
    dealPlayer()
    dealPlayer()
shuffle()
deal()
while active:
    print('Dealer Hand: blank', end=', ')
    print(dealerHand[1])
    print('Your Hand:', end=' ')
    print(*hand, sep=', ')
    if len(deck[0])<=26:
        print('Half of deck used. Discards replaced and shuffled.')
        shuffle()
    if playerTotal==21:
        print('Win!')
        over = True
    elif playerTotal>21:
        print('Loss')
        print(playerTotal)
        over = True
    else:
        print('Hit? (Y/N)')
        x = input()
        x = x.replace(' ','')
        if x.lower()=='y':
            dealPlayer()
        elif x.lower()=='n':
            if playerTotal < dealerTotal:
                print('Loss')
                over = True
            if playerTotal == dealerTotal:
                print('Tie')
                over = True
            if playerTotal > dealerTotal:
                print('Win')
                over = True
        else:
            print('Please enter either the character Y or N and press enter')
    if over:
        print('Play Again? (Y/N)')
        play = input()
        play = play.replace(' ', '')
        if play.lower()=='y':
            over = False
            #print(deck)
            deal()
        elif play.lower()=='n':
            active = False
            #print(*usedCards)
        else:
            print('Please enter either the character Y or N and press enter')





            
