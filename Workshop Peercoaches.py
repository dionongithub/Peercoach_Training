Size = 4
S = ""

Y = 0
while(Y < Size):
    if(Y == 0 or Y == Size -1):
        X = 0
        while (X < Size):
            S = S + "*"
            X = X + 1
        S = S + "\n"
    else:
        X = 2
        S = S + "*"
        while (X < Size):
            S = S + " "
            X = X + 1
        S = S + "*"
        S = S + "\n"
    Y = Y  + 1

print(S)
input()
