n = int(input())

if n>=1 and n<10:
    for i in range(n, 0, -1):
        for j in range(1, n+1):
            if j >= i:
                print(n-i, end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("input error")