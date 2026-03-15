'''TaskPY200_T5: Chessboard with Numbers
Input: N
Print an N x N grid:
• If (row+col) is even → print 1
• else → print 0
But if row == col → print X instead.'''

N = int(input("Enter the Number: "))

for row in range(N):
    for col in range(N):
        if (row==col):
            print("X", end=" ")
        elif (row+col)%2==0:
            print(1, end=" ")
        else:
            print(0, end=" ")
            