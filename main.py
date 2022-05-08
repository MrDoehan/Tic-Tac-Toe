grid = [[" ", "1", "2", "3"], ["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]
for i in grid:
    print(i)
victory = False
while victory == False:
    p1 = input("Where do you want to place your marker (X): ")
    p11 = p1.split()
    one = int(p11[0])
    two = int(p11[1])
    if grid[one][two] == " ":
        grid[one][two] = "X"
    else:
        print("This space is already occupied, choose again, hehe you lose your turn")
    for row in range(3):
        if grid[row+1][1] == grid[row+1][2] == grid[row+1][3] == 'X':
            print("X Wins")
            victory = True
            break
        if grid[1][row+1] == grid[2][row+1] == grid[3][row+1] == 'X':
            print("X Wins")
            victory = True
            break
        if grid[1][1] == grid[2][2] == grid[3][3] == "X":
            print("X Wins")
            victory = True
            break
        if grid[3][1] == grid[2][2] == grid[1][3] == "X":
            print("X Wins")
            victory = True
            break
    for i in grid:
        print(i)
    p2 = input("Where do you want to place your marker (O): ")
    p22 = p2.split()
    three = int(p22[0])
    four = int(p22[1])
    if grid[three][four] == " ":

        grid[three][four] = "O"
    else:
        print("This space is already occupied, choose again, hehe you lose your turn")
    for row in range(3):
        if grid[row+1][1] == grid[row+1][2] == grid[row+1][3] == 'O':
            print("O Wins")
            victory = True
            break
        if grid[1][row+1] == grid[2][row+1] == grid[3][row+1] == 'O':
            print("O Wins")
            victory = True
            break
        if grid[1][1] == grid[2][2] == grid[3][3] == "O":
            print("O Wins")
            victory = True
            break
        if grid[3][1] == grid[2][2] == grid[1][3] == "O":
            print("O Wins")
            victory = True
            break
    for i in grid:
        print(i)