import sys

import math

#Used to read the input of the player. sys.argv is reading the number after .py

#e.g  4 5 2 6 3 the number of 4

n = int(sys.argv[1])

player1Hand = []

player2Hand = []

currentPH = []

oppenontPH = []

pile = [0,1,2,3,4,5,6,7,8]

move = []



for i in range(n):

    if (i % 2 == 0):

        player1Hand.append(int(sys.argv[i+2]))

        pile.remove(int(sys.argv[i+2]))

    else:

        player2Hand.append(int(sys.argv[i+2]))

        pile.remove(int(sys.argv[i+2]))

    move.append(int(sys.argv[i+2]))



if (n % 2 == 0):

    currentPH = player1Hand

    oppenontPH = player2Hand

else:

    currentPH = player2Hand

    oppenontPH = player1Hand



def winningHand(currentPH):

    for i in range(len(currentPH)):

        curPoint = 0

        pointLeft = 14

        for j in range(len(currentPH)):

            if (i != j):

                curPoint = currentPH[i] + currentPH[j]

                pointLeft -= curPoint

                if (pointLeft in pile):

                    return pointLeft

                curPoint = 0

                pointLeft = 14

    return False

    



def combinationHand(cardInPool, currentPH,oppenontPH):

    if winningHand(currentPH) != False:

        return winningHand(currentPH)

    comArr = []

    tempArr = []

    if len(cardInPool) == 9 or len(currentPH)== 0:

        countWay = 0

        for i in range(len(cardInPool)):

            leftPoint = 14

            leftPoint = 14 - cardInPool[i]

            for j in range(len(cardInPool)):

                for k in range(len(cardInPool)):

                    if (j != k and j != i):

                        if(leftPoint - cardInPool[j] - cardInPool[k] == 0):

                            #output = str(i) + " : " + str(i) + " + " + str(j) + " + " + str(k)

                            #print(output)

                            countWay += 1

            comArr.append(countWay)

            countWay = 0

    elif len(cardInPool) > 3:

        countWay = 0

        if(len(currentPH)<=2):

            for i in range(len(currentPH)):

                leftPoint = 14

                leftPoint = 14 - currentPH[i]

                for j in range(len(cardInPool)):

                    for k in range(len(cardInPool)):

                        if (j != k and j != i):

                            if(leftPoint - cardInPool[j] - cardInPool[k] == 0):

                                countWay += 1

                                if(findCommend(cardInPool[j],cardInPool[k],oppenontPH,cardInPool) != False):

                                    return findCommend(cardInPool[j],cardInPool[k],oppenontPH,cardInPool)

                                    

                comArr.append(countWay)

                countWay = 0

    elif len(cardInPool) == 1:

        return cardInPool[0]

    else:

        countWay = 0

        for i in range(len(currentPH)):

            leftPoint = 14

            leftPoint = 14 - currentPH[i]

            for j in range(len(currentPH)):

                if (j != i):

                    for k in range(len(cardInPool)):

                        if(leftPoint - oppenontPH[j] - oppenontPH[k] == 0):

                            #output = str(i) + " : " + str(i) + " + " + str(j) + " + " + str(k)

                            #print(output)

                            countWay += 1

            comArr.append(countWay)

            countWay = 0

    return cardInPool[comArr.index(max(comArr))]



def findCommend(firstNum, secNum,oppenontPH,cardInPool):

    for i in range(len(oppenontPH)):

        leftPoint = 14

        leftPoint = 14 - oppenontPH[i]

        for j in range(len(cardInPool)):

            for k in range(len(cardInPool)):

                if (j != k and j != i):

                    if(leftPoint - cardInPool[j] - cardInPool[k] == 0):

                        if(firstNum == cardInPool[j]):

                            return firstNum

                        elif(firstNum == cardInPool[k]):

                            return firstNum

                        elif(secNum == cardInPool[j]):

                            return secNum

                        elif(secNum == cardInPool[k]):

                            return secNum

    return False





#print(combinationHand(pile, currentPH))

#highCom = combinationHand(pile, currentPH)

#indexMax = highCom.index(max(combinationHand(pile, currentPH)))

n = n+1

output = str(n)

myMove =combinationHand(pile,currentPH,oppenontPH)

move.append(myMove)



for i in range(n):

    output = output+" "+str(move[i])

print(output)

