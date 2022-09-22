
# Blackjack code version 0.7
# Basic Blackjack functionality
# Completed: deck nonreplacement, input error resiliance, proper ace coding, results recording as json,
# In progress: results reporting/analysis
# Lacks: rules customization, more advanced input processing, proper dealer play
# splitting, betting, GUI, results reporting/analysis, how to play guide
import random, copy, json
print('Welcome to Blackjack')
global active
active = True
over = False
blind = True
deckNum = 1
'''just finish adding in data changing for ends, and recording the final data'''
settings = [blind, deckNum]
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
pAce = 0
dAce = 0
dataTemplate = {
    'pScores': [],
    'dScores': [],
    'dWins': 0,
    'ties':0,
    'pWins': 0,
    'settings': settings
}
f = open('data.json', 'r+')
global data
data = json.load(f)
def ideal(total, ace):
    if ace == 0:
        return total
    elif (total + 11 + (ace - 1)) <= 21:
        return (total + 11 + (ace - 1))
    else:
        return total + ace


def dealPlayer():
    global playerTotal, pAce
    cardId = random.randint(0, len(deck[0]) - 1)
    hand.append(deck[0][cardId])
    # print(cardId)
    if deck[1][cardId] == 1:
        pAce += 1
    else:
        playerTotal += deck[1][cardId]
    usedCards.append(deck[0][cardId])
    deck[0].pop(cardId)
    deck[1].pop(cardId)
    return


def dealer():
    global dealerTotal, dAce
    cardId = random.randint(0, len(deck[0]) - 1)
    # print(cardId)
    dealerHand.append(deck[0][cardId])
    if deck[1][cardId] == 1:
        dAce += 1
    else:
        dealerTotal += deck[1][cardId]
    usedCards.append(deck[0][cardId])
    deck[0].pop(cardId)
    deck[1].pop(cardId)
    return


def shuffle():
    global deck
    deck = copy.deepcopy(cards)


def deal():
    global playerTotal, dealerTotal, dAce, pAce
    playerTotal = int(0)
    dealerTotal = int(0)
    pAce = int(0)
    dAce = int(0)
    hand.clear()
    dealerHand.clear()
    dealer()
    dealer()
    dealPlayer()
    dealPlayer()

def helpMenu():
    print('Help Menu. Here are some options, type key and press enter:')
    print('key - description')
    print('how - print instructions on how to play the game')
    print('data - opens data reporting and analysis menu')
    print('exit - leaves help menu and continues game')
    while True:
        x = input().lower()
        if x == 'exit':
            return
        elif x == 'how':
            print('Instructions to come')
        elif x == 'data':
            dataMenu()
            return
def dataMenu():
    print('Data Menu. To select option, type key and press enter:')
    print('key - description')
    print('raw - prints raw saved data as a string')
    print('winloss - shows win, loss and tie statistics')
    print('reset - clears all data')
    print('exit - exits data and help menus and returns to game')
    while True:
        x = input().lower()
        if x == 'exit':
            return
        elif x == 'raw':
            print(data)
        elif x == 'winloss':
            total = data['pWins']+data['dWins']+data['ties']
            print('Out of ', end = '')
            print(total, end = ' ')
            print('games')
            print('Player Win Percentage:', end=' ')
            print(100*data['pWins']/total)
            print('Player Loss Percentage:', end=' ')
            print(100*data['dWins']/total)
            print('Tie Percentage:', end=' ')
            print(100*data['ties']/total)
        elif x == 'reset':
            data['pWins'] = 0
            data['dWins'] = 0
            data['ties'] = 0
            data['pScores'].clear()
            data['dScores'].clear()

shuffle()
deal()
while active:
    if blind:
        print('Dealer Hand: blank', end=' ')
        print(dealerHand[1])
    else:
        print('Dealer Hand:', end=' ')
        print(*dealerHand, sep=', ')
    print('Your Hand:', end=' ')
    print(*hand, sep=', ')
    if len(deck[0]) <= 26:
        print('Half of deck used. Discards replaced and shuffled.')
        shuffle()
    if ideal(dealerTotal, dAce) == 21 and ideal(playerTotal, pAce) == 21:
        print('Tie')
        data['ties'] += 1
        data['pScores'].append(ideal(playerTotal, pAce))
        data['dScores'].append(ideal(dealerTotal, dAce))
        over = True
    elif ideal(playerTotal, pAce) == 21:
        print('Win!')
        data['pWins'] +=1
        data['pScores'].append(ideal(playerTotal, pAce))
        data['dScores'].append(ideal(dealerTotal, dAce))
        over = True
    elif ideal(dealerTotal, dAce) == 21:
        print('Loss')
        data['dWins'] +=1
        data['pScores'].append(ideal(playerTotal, pAce))
        data['dScores'].append(ideal(dealerTotal, dAce))
        over = True
    elif ideal(playerTotal, pAce) > 21:
        print('Loss')
        data['pScores'].append(ideal(playerTotal, pAce))
        data['dScores'].append(ideal(dealerTotal, dAce))
        data['dWins'] += 1
        # print(playerTotal)
        over = True
    else:
        print('Hit? (Y/N) or enter help for the Help Menu')
        x = input()
        x = x.replace(' ', '')
        if x.lower() == 'y':
            dealPlayer()
        elif x.lower()== 'help':
            helpMenu()
        elif x.lower() == 'n':
            while ideal(dealerTotal, dAce)<=16:
                dealer()
                print('Dealer Hand: blank', end=' | ')
                for c in dealerHand[1:]:
                    print(c, end='| ')
            if ideal(dealerTotal, dAce)>21:
                print('Win | Dealer Bust')
                data['pScores'].append(ideal(playerTotal, pAce))
                data['dScores'].append(ideal(dealerTotal, dAce))
                data['pWins'] += 1
                over = True
            elif ideal(playerTotal, pAce) < ideal(dealerTotal, dAce):
                print('Loss')
                data['pScores'].append(ideal(playerTotal, pAce))
                data['dScores'].append(ideal(dealerTotal, dAce))
                data['dWins'] += 1
                over = True
            if ideal(playerTotal, pAce) == ideal(dealerTotal, dAce):
                print('Tie')
                data['pScores'].append(ideal(playerTotal, pAce))
                data['dScores'].append(ideal(dealerTotal, dAce))
                data['ties'] +=1
                over = True
            if ideal(playerTotal, pAce) > ideal(dealerTotal, dAce):
                print('Win')
                data['pScores'].append(ideal(playerTotal, pAce))
                data['dScores'].append(ideal(dealerTotal, dAce))
                data['pWins']+=1
                over = True
        else:
            print('Please enter either the character Y or N and press enter')
    if over:
        print('Play Again? (Y/N) or enter help for Help Menu')
        play = input()
        play = play.replace(' ', '')
        if play.lower() == 'y':
            over = False
            # print(deck)
            deal()
        elif play.lower() =='help':
            helpMenu()
        elif play.lower() == 'n':
            active = False
            # print(*usedCards)
        else:
            print('Please enter either the character Y or N and press enter')
f.close()
f = open('data.json', 'w')
json.dump(data, f)
f.close()