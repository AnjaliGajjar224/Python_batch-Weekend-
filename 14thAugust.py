# def Armstrong(start,end):
#     for i in range(start,end+1):
#         temp = i
#         sum = 0
#         while temp > 0:
#             digit = temp % 10
#             sum += digit ** len(str(i))
#             temp //= 10

#         if i == sum:
#             print(i,end=" ")

# Armstrong(int(input("Enter Starting Range: ")),int(input("Enter Ending Range:")))

# def Armstrong(start,end):
data = {}

def Register():
    name = input("Enter User Name: ")
    pw = input("Enter Password: ")
    data.setdefault(name,pw)

    print("----------------------------------------------------")
    print("Your User Name is: ",name)
    print("Your Password is: ",pw)
    print(data)

def Login():
    name = input("Enter User Name: ")
    pw = input("Enter Password: ")
    if name in data.keys():
        if pw == data.get(name):
            print("Login Successful")

        else:
            print("Invalid Password")

    else:
        print("User not Found So Please Sign Up first")
        print("----------------------------------------------------")
        print("You want to Register? Press Y for Yes and N for No")
        if input().lower() == "y":
            Register()
        else:
            print("Thank You")
            exit()


print("WELCOME TO THE SYSTEM")
while(True):
    print("1--->Sign Up")
    print("2--->Login")
    print("3--->Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Register()
        print("You are Successfully Signed Up")

    elif choice == 2:
        Login()
        

    elif choice == 3:
        break

    else:
        print("Invalid Choice")
        continue

