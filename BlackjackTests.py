#Blackjack Testing
#ideal function seems to be working
playerTotal = 9
playerAces = 2
def ideal(total, ace):
    if ace == 0:
        return total
    elif (total+11+(ace-1)) <= 21:
        return (total+11+(ace-1))
    else:
        return total + ace

print(ideal(playerTotal, playerAces))
