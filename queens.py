q = int(input("Enter no. of queens:"))

board = [[0] * q for i in range(q)]

def is_attack(i, j):
    for k in range(q):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(q):
        for l in range(q):
            if (k + l == i + j) or (k - l == i - j):
                if board [i][j] == 1:
                    return True       
    return False

def N_queen(n):
    if n == 0:
        return True

    for i in range(q):
        for j in range(q):
            if (not is_attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1

                if N_queen(n-1):
                    return True

                board[i][j] = 0  
    return False

N_queen(q)

print("Solution")
for row in board:
    print(row)

