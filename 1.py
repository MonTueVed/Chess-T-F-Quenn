a=int(input())
b=int(input())
c=int(input())
d=int(input())
bishop = ''
rook = ''
if abs(c-a) == abs(d-b):
    bishop = True
if abs(c-a) != abs(d-b):
    bishop = False
if a == c or b == d:
    rook = True
if a != c and b != d and bishop == False:
    rook = False
if bishop == True or rook == True:
    print('YES')
elif bishop == False or rook == False:
    print('NO')
