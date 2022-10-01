"""method 1"""

# x = int(input()) + 1
# y = int(input()) + 1
# z = int(input()) + 1
# n = int(input())
# ans = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if ((i + j + k) != n)]
# print (ans)


"""method 2"""

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))