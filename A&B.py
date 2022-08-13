print("Number of test cases must be between 1 and 1000")
print("Alice's and Bob's height cannot be equal.")
print("Their height must be between 100 and 200 centimetres.")
z=int(input("Enter number of test cases:"))
if z<1 or z>1000:
    print("Invalid number of test cases")
elif z>=1 and z<=1000:
    for test in range(z):
        X=int(input("Enter Alice's height:"))
        Y=int(input("Enter Bob's height:"))
        if X>200 or X<100:
            print("Invalid height input")
            break
        elif X==Y:
            print("Height cannot be same")
            break
        elif Y>200 or Y<100:
            print("Invalid height input")
            break
        elif X>Y:
            print("Alice's taller")
        else:
            print("Bob's taller")



