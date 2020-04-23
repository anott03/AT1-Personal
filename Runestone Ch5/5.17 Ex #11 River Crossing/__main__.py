# the first item in each bank is the number of missionaries
# and the second item in each bank is the number of cannibals 
# first element of boat  is the bank the boat is currently at
# second element of boat is the number of missionaries
# third element of boat is the number of cannibals
def cross(b1=[3, 3], b2=[0, 0], boat=[1, 0, 0]):
    while b1[0] >= b1[1] and boat[1]+boat[2] <= 2:
        b1[0] -= 1
        boat[1] += 1

    while boat[1] + boat[2] <= 2:
        b1
