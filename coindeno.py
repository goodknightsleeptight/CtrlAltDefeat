coin = 1
note = 10
t=int(input("Enter number of tests:"))
if t < 1 or t > 1000 :
        print("Invalid number of test cases. Please enter a value between 1 and 1000")
elif t > 1 or t < 1000 :
    for test in range(t):
        X=int(input("Enter amount of X:"))
        if X < 1 or X > 1000 :
            print("Invalid number of X. Please enter a value between 1 and 1000")
        elif X > 10 and X < 1000:
            print("Chef can use", X//10, "notes and", X%10, "coins in the optimal case")
        else: print("Chef can only use", X, "coins")
