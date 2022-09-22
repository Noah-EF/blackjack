#Blackjack code version 0.1
#Basic Blackjack functionality
#Lacks rules customization, proper ace coding, deck nonreplacement, results recording, GUI
import random
print('Welcome to Blackjack')
global active
active = True
over = False
cards = [['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
          'Nine', 'Ten', 'Jack', 'Queen', 'King'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
                                            10, 10]]
playerTotal = int(0)
hand = []
dealerTotal = int(0)
dealerHand = []
def dealPlayer():
    cardId = random.randint(0, 12)
    hand.append(cards[0][cardId])
    global playerTotal
    playerTotal += cards[1][cardId]
    return
def dealer():
    cardId = random.randint(0, 12)
    dealerHand.append(cards[0][cardId])
    global dealerTotal
    dealerTotal += cards[1][cardId]
    return
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
deal()
while active:
    print('Dealer Hand: blank', end=' ')
    print(dealerHand[1])
    print('Your Hand:', end=' ')
    print(*hand)
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
        if x.lower()=='y':
            dealPlayer()
        if x.lower()=='n':
            if playerTotal < dealerTotal:
                print('Loss')
                over = True
            if playerTotal == dealerTotal:
                print('Tie')
                over = True
            if playerTotal > dealerTotal:
                print('Win')
                over = True
    if over:
        print('Play Again? (Y/N)')
        play = input()
        if play.lower()=='y':
            over = False
            deal()
        if play.lower()=='n':
            active = False
