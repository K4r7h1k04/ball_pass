def findCurrentPlayer(numberOfFriends, friendsList, numberOfBallPassed, ballPassedlist):
    # Find the index of the starting player in the list
    currentPlayerIndex = friendsList.index(ballPassedlist[0])
    direction = "Clockwise"

    # Simulate passing the ball
    for i in range(numberOfBallPassed):
        # Skip the next player
        currentPlayerIndex = (currentPlayerIndex + 2) % numberOfFriends

        # Check if we need to switch the direction
    if (friendsList.index(ballPassedlist[0]) < friendsList.index(ballPassedlist[1])):
      direction = "Clockwise"
    else:
      direction = "Anti Clockwise"

    # Print the results
    print("Direction -", direction)
    print("Current player -", friendsList[currentPlayerIndex])
    
numberOfFriends = int(input())
friendsList = []

for _ in range(numberOfFriends):
    friend = input()
    friendsList.append(friend)

numberOfBallPassed= int(input())
ballPassedlist = []
for _ in range(2):
    ballPassed = input()
    ballPassedlist.append(ballPassed)

findCurrentPlayer(numberOfFriends, friendsList, numberOfBallPassed, ballPassedlist)


    

