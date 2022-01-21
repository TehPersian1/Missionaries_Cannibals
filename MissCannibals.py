from search import *

class MissCannibals(Problem):
  def __init__(self, initial, goal = (0,0,False)):
    super().__init__(initial, goal)
    self.missionaries = 3
    self.cannibals = 3
    self.boat = True

  def goal_test(self, state):
    if state == (0,0,False):
        return True
    else:
        return False
  
  def result(self, state, action):
    
    numberOfCannibals = state[1]
    numberOfMissionaries = state[0]
    boatOnLeft = state[2]

    #print("(", numberOfMissionaries, ", ", numberOfCannibals, ", ", boatOnLeft, ")", " In result" )

    #-------------------------------------Boat on Left------------------------------------------------

    if action == 'MM' and boatOnLeft:
        newState = (numberOfMissionaries - 2, numberOfCannibals, False)
    elif action == 'CC' and boatOnLeft:
        newState = ( numberOfMissionaries, numberOfCannibals - 2, False)
    elif action == 'M' and boatOnLeft:
        newState = ( numberOfMissionaries - 1, numberOfCannibals, False)
    elif action == 'C' and boatOnLeft:
        newState = ( numberOfMissionaries, numberOfCannibals - 1, False)
    elif action == 'MC' and boatOnLeft:
        newState = ( numberOfMissionaries - 1, numberOfCannibals - 1, False)

    #-------------------------------------Boat on Right------------------------------------------------

    elif action == 'MM' and not boatOnLeft:
        newState = (numberOfMissionaries + 2, numberOfCannibals, True)
    elif action == 'CC' and not boatOnLeft:
        newState = (numberOfMissionaries, numberOfCannibals + 2, True)
    elif action == 'M' and not boatOnLeft:
        newState = (numberOfMissionaries + 1, numberOfCannibals, True)
    elif action == 'C' and not boatOnLeft:
        newState = (numberOfMissionaries, numberOfCannibals + 1,  True)
    elif action == 'MC' and not boatOnLeft:
        newState = (numberOfMissionaries + 1, numberOfCannibals + 1, True)

    return newState
    

  def actions(self, state):

    possible_actions = ['MM', 'CC', 'C', 'M', 'MC']
    numberOfCannibals = state[1]
    numberOfMissionaries = state[0]
    boatOnLeft = state[2]

    # print()
    print("(", numberOfMissionaries, ", ", numberOfCannibals, ", ", boatOnLeft, ")")

    output = ""

    # if numberOfMissionaries == 3:
    #     output+="MMM "
    # elif numberOfMissionaries == 2:
    #     output+="MM "
    # elif numberOfMissionaries == 1:
    #     output+="M "

    # "".join("M" * numberOfMissionaries)

    output+= "M" * numberOfMissionaries

    if numberOfMissionaries > 0:
        output+=" "

    # if numberOfCannibals == 3:
    #     output+="CCC "
    # elif numberOfCannibals == 2:
    #     output+="CC "
    # elif numberOfCannibals == 1:
    #     output+="C "

    output+= "C" * numberOfCannibals

    if numberOfCannibals > 0:
        output+=" "

    if boatOnLeft:
        output+="(B) "

    output+="~~~ "

    output+= "M" * (3 - numberOfMissionaries)
    
    if (3 - numberOfMissionaries) > 0:
        output+=" "

    # if numberOfMissionaries == 2:
    #     output+="M "
    # elif numberOfMissionaries == 1:
    #     output+="MM "
    # elif numberOfMissionaries == 0:
    #     output+="MMM "

    # if numberOfCannibals == 2:
    #     output+="C "
    # elif numberOfCannibals == 1:
    #     output+="CC "
    # elif numberOfCannibals == 0:
    #     output+="CCC "

    output+= "C" * (3 - numberOfCannibals)

    if (3 - numberOfCannibals) > 0:
        output+=" "

    if not boatOnLeft:
        output+="(B) "

    print(output)


    if not (numberOfCannibals < 0 or numberOfMissionaries < 0) and not (numberOfCannibals > 3 or numberOfMissionaries > 3):#(numberOfCannibals > numberOfMissionaries and numberOfMissionaries > 0) or (numberOfCannibals < numberOfMissionaries and numberOfMissionaries < 3)

        #-------------------------------------KILL THESE--------------------------------------------------
        # if numberOfCannibals == 3 and numberOfMissionaries == 2:
        #     possible_actions = []
            
        # if numberOfCannibals == 3 and numberOfMissionaries == 1:
        #     possible_actions = []

        # if numberOfCannibals == 2 and numberOfMissionaries == 1:
        #     possible_actions = []

        # if numberOfCannibals == 1 and numberOfMissionaries == 2:
        #     possible_actions = []

        #-------------------------------------Boat on Left------------------------------------------------

        if numberOfMissionaries == 3 and numberOfCannibals == 3  and boatOnLeft:
            # print("chose 3, 3, true")
            possible_actions.remove('MM')
            possible_actions.remove('M')

        elif numberOfMissionaries == 0 and numberOfCannibals == 3 and boatOnLeft:
            # print("chose 3, 0, true")
            possible_actions.remove('MM')
            possible_actions.remove('M')
            possible_actions.remove('MC')

        elif numberOfMissionaries == 3 and numberOfCannibals == 2 and boatOnLeft:
            # print("chose 3, 2, true")
            possible_actions.remove('MM')
            possible_actions.remove('MC')

        elif numberOfMissionaries == 2 and numberOfCannibals == 2 and boatOnLeft:
            # print("chose 2, 2, true")
            possible_actions.remove('M')
            possible_actions.remove('CC')
            possible_actions.remove('C')

        elif numberOfMissionaries == 0 and numberOfCannibals == 2 and boatOnLeft:
            # print("chose 0, 2, true")
            possible_actions.remove('MM')
            possible_actions.remove('M')
            possible_actions.remove('MC')

        elif numberOfMissionaries == 3 and numberOfCannibals == 1 and boatOnLeft:
            # print("chose 3, 1, true")
            possible_actions.remove('M')
            possible_actions.remove('CC')
            possible_actions.remove('MC')

        elif numberOfMissionaries == 1 and  numberOfCannibals == 1 and boatOnLeft:
            # print("chose 1, 1, true")
            possible_actions.remove('MM')
            possible_actions.remove('CC')
            possible_actions.remove('C')
        
        elif numberOfMissionaries == 0 and numberOfCannibals == 1 and boatOnLeft:
            # print("chose 0, 1, true")
            possible_actions.remove('MM')
            possible_actions.remove('M')
            possible_actions.remove('CC')
            possible_actions.remove('MC')

        #-------------------------------------Boat on Right------------------------------------------------

        elif numberOfMissionaries == 3 and numberOfCannibals == 3 and not boatOnLeft:
            # print("chose 3, 3, false")
            possible_actions.remove('MM')
            possible_actions.remove('M')
            possible_actions.remove('CC')
            possible_actions.remove('C')
            possible_actions.remove('MC')
        
        # if numberOfCannibals == 3 and numberOfMissionaries == 2:???not possible too many on Can on Left
        
        # if numberOfCannibals == 3 and numberOfMissionaries == 1:???not possible too many on Can on Left

        elif numberOfMissionaries == 0 and numberOfCannibals == 3 and not boatOnLeft:
            # print("chose 0, 3, false")
            possible_actions.remove('CC')
            possible_actions.remove('C')
            possible_actions.remove('MC')

        elif numberOfMissionaries == 3 and numberOfCannibals == 2 and not boatOnLeft:
            # print("chose 3, 2, false")
            possible_actions.remove('MM')
            possible_actions.remove('M')
            possible_actions.remove('CC')
            possible_actions.remove('MC')

        elif numberOfMissionaries == 2 and numberOfCannibals == 2 and not boatOnLeft:
            # print("chose 2, 2, false")
            possible_actions.remove('MM')
            possible_actions.remove('CC')
            possible_actions.remove('C')

        # if numberOfCannibals == 2 and numberOfMissionaries == 1: ???not possible too many on Can on Left

        elif numberOfMissionaries == 0 and numberOfCannibals == 2 and not boatOnLeft:
            # print("chose 0, 2, false")
            possible_actions.remove('M')
            possible_actions.remove('CC')
            possible_actions.remove('MC')

        elif numberOfMissionaries == 3 and numberOfCannibals == 1 and not boatOnLeft:
            # print("chose 3, 1, false")
            possible_actions.remove('MM')
            possible_actions.remove('M')
            possible_actions.remove('MC')

        # if numberOfCannibals == 1 and numberOfMissionaries == 2: ???not possible too many on Can on right

        elif numberOfMissionaries == 1 and numberOfCannibals == 1 and not boatOnLeft:
            # print("chose 1, 1, false")
            possible_actions.remove('M')
            possible_actions.remove('CC')
            possible_actions.remove('C')
        
        elif numberOfMissionaries == 0 and numberOfCannibals == 1 and not boatOnLeft:
            # print("chose 0, 1, false")
            possible_actions.remove('MC')
    else:
        # print("Default")
        possible_actions = []

    # print()
    # print(possible_actions)
    # print()

    return possible_actions


if __name__ == '__main__':
    initial_state = (3,3,True)
    print(initial_state[0], initial_state[1], initial_state[2])
    misscann = MissCannibals(initial_state)
    path = depth_first_graph_search(misscann).solution()
    print(path)