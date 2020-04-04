"""
Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:

(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)

you need to provide coordinates by space-seperating two integers between 1 to 3. i.e., 1 2
The first user is X and second is O and so on.

"""

ex = [[" ", " ", " "] for i in range(3)]
X = 0
O = 0
count = 0
while True:
    x = None
    y = None
    print("---------")
    print('|', ex[0][2], ex[1][2], ex[2][2], '|')
    print('|', ex[0][1], ex[1][1], ex[2][1], '|')
    print('|', ex[0][0], ex[1][0], ex[2][0], '|')
    print("---------")
    ex_list = [j for i in ex for j in i]
    if (X == 0 and O == 0) and ' ' not in ex_list:
        print("Draw")
        break
    elif X == 1 and O == 0:
        print("X wins")
        break
    elif O == 1 and X == 0:
        print("O wins")
        break
    while True:
        try:
            x, y = [int(i) for i in input("Enter the coordinates:").split()]
            if x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
            elif ex[x-1][y-1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                if 1 <= x <= 3 and 1 <= y <= 3:
                    count += 1
                if count % 2 == 1:
                    ex[x-1][y-1] = 'X'
                else:
                    ex[x-1][y-1] = 'O'
                break
        except:
            print("You should enter numbers!")
    rl = [ex[0], ex[1], ex[2]]
    cl = [[ex[0][i], ex[1][i], ex[2][i]] for i in range(3)]
    dia = [[ex[0][2], ex[1][1], ex[2][0]], [ex[0][0], ex[1][1], ex[2][2]]]
    for i in range(3):
        if rl[i].count('O') == 3 or cl[i].count('O') == 3:
            O += 1
        if rl[i].count('X') == 3 or cl[i].count('X') == 3:
            X += 1
    for i in range(2):
        if dia[i].count('O') == 3:
            O += 1
        if dia[i].count('X') == 3:
            X += 1