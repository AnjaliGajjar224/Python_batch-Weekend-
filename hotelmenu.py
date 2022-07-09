print("1------>South Indian")
print("2------>Italian")
print("3------>Chinese")

choice = int(input("Enter your choice:"))

if choice == 1:
    print("You have selected SouthIndian")
    print("1--->Dosa")
    print("2--->Idli")
    print("3--->Uttapam")

    choice_2 = int(input("Enter your choice:"))
    if choice_2 == 1:
        print("Types of Dosa:")
        print("1--->Paper dosa...........120/-")
        print("2--->Masala dosa..........180/-")

        subchoice = int(input("Enter Your choice:"))

        if subchoice == 1:
            print("You have selected Paper Dosa")
            plates = int(input('Enter number of plates you want to order:'))
            total_amount = plates * 120
            print("Grand Total---> ",total_amount)

        elif subchoice == 2:
            print("You have selected Masala Dosa")
            plates = int(input('Enter number of plates you want to order:'))
            total_amount = plates * 180
            print("Grand Total---> ",total_amount)

        else:
            print("Invalid Choice")

    elif choice_2 == 2:
        print("Types of Idli")
        print("1---->Rava Idli..........140/-")
        print("2---->Plain Idli.........130/-")

        subchoice = int(input("Enter Your choice"))

        if subchoice == 1:
            print("You have selected Rava Idli")
            plates = int(input('Enter number of plates you want to oder:'))
            total_amount = plates * 140
            print("Grand Total--->",total_amount) 

        elif subchoice == 2:
            print("You have selected Plain Idli")
            plates = int (input('Enter number of Plates you want to oder:'))
            total_amount = plates *130
            print("Grand Total--->", total_amount)

        else:
            print("Invalid Choice")
    
    elif choice_2 == 3:
        print("Types of Uttapam")
        print("1---->Cheese Utapam...........150/-")
        print("2---->Onion Utapam...........160/-")

        subchoice = int(input("Enter Your  choice"))

        if subchoice == 1:
            print("You have selected Plain Cheesse Utapam")
            plates = int(input('Enter number of Plates you want to oder:'))
            total_amount = plates *150
            print("Grand Total--->", total_amount)

        elif subchoice == 2:            
            print("You have selected Onion Utapam")
            plates = int (input('Enter Your choice'))
            total_amount = plates *160
            print("Grand Total--->", total_amount) 
        
        else:
            print("Invalid choice")


elif choice == 2:
    print("You have selected Italian")
    print("1--->Pizza")
    print("2--->Pasta")
    print("3--->Burger")

    choice_2 = int(input("Enter your choice:"))
    if choice_2 == 1:
        print("Types of Pizza:")
        print("1--->Margherita...........180/-")
        print("2--->Four Season..........210/-")

        subchoice = int(input("Enter Your  choice"))

        if subchoice == 1:
            print("You have selected Margherita")
            plates = int(input('Enter number of Plates you want to oder:'))
            total_amount = plates *180
            print("Grand Total--->", total_amount)

        elif subchoice == 2:            
            print("You have selected Four Season")
            plates = int (input('Enter Your choice'))
            total_amount = plates *210
            print("Grand Total--->", total_amount) 
        
        else:
            print("Invalid choice")

    elif choice_2 == 2:
        print("Types of Pasta")
        print("1---->Red sauce Pasta..........130/-")
        print("2---->White sauce Pasta........150/-")

        subchoice = int(input("Enter Your  choice"))

        if subchoice == 1:
            print("You have selected Red sauce Past")
            plates = int(input('Enter number of Plates you want to oder:'))
            total_amount = plates *130
            print("Grand Total--->", total_amount)

        elif subchoice == 2:            
            print("You have selected White sause Pasta")
            plates = int (input('Enter Your choice'))
            total_amount = plates *150
            print("Grand Total--->", total_amount) 
        
        else:
            print("Invalid choice")

        
    elif choice_2 == 3:
        print("Types of Burger")
        print("1---->Veg Burger.....................220/-")
        print("2---->Double Cheese Burger...........260/-")

        subchoice = int(input("Enter Your  choice"))

        if subchoice == 1:
            print("You have selected Veg Burger")
            plates = int(input('Enter number of Plates you want to oder:'))
            total_amount = plates *220
            print("Grand Total--->", total_amount)

        elif subchoice == 2:            
            print("You have selected Doubel Chesse Burger")
            plates = int (input('Enter Your choice'))
            total_amount = plates *260
            print("Grand Total--->", total_amount) 
        
        else:
            print("Invalid choice")


elif choice == 3:
    print("You have selected Chinese")
    print("1--->Noodles")
    print("2--->Manchurian")
    print("3--->Soup")

    choice_2 = int(input("Enter your choice:"))
    if choice_2 == 1:
        print("Types of Noodles:")
        print("1--->Haka Noodles...........170/-")
        print("2--->Veg Noodles..........230/-")

        subchoice = int(input("Enter Your  choice"))

        if subchoice == 1:
            print("You have selected Haka Noodles")
            plates = int(input('Enter number of Plates you want to oder:'))
            total_amount = plates *170
            print("Grand Total--->", total_amount)

        elif subchoice == 2:            
            print("You have selected Veg Noodles")
            plates = int (input('Enter Your choice'))
            total_amount = plates *230
            print("Grand Total--->", total_amount) 
        
        else:
            print("Invalid choice")

    elif choice_2 == 2:
        print("Types of Manchurian")
        print("1---->Gravy Manchuran..........240/-")
        print("2---->Dry Manchurian........280/-")
        
        subchoice = int(input("Enter Your  choice"))

        if subchoice == 1:
            print("You have selected Gravy Manchurian")
            plates = int(input('Enter number of Plates you want to oder:'))
            total_amount = plates *240
            print("Grand Total--->", total_amount)

        elif subchoice == 2:            
            print("You have selected Dry manchurian")
            plates = int (input('Enter Your choice'))
            total_amount = plates *280
            print("Grand Total--->", total_amount) 
        
        else:
            print("Invalid choice")
    elif choice_2 == 3:
        print("Types of Soup")
        print("1---->Noodles Soup.....................210/-")
        print("2---->Hot and Sour Soup................250/-")
        subchoice = int(input("Enter Your  choice"))

        if subchoice == 1:
            print("You have selected Noodles Soup")
            plates = int(input('Enter number of Plates you want to oder:'))
            total_amount = plates * 210
            print("Grand Total--->", total_amount)

        elif subchoice == 2:            
            print("You have selected Hot and Sour Soup")
            plates = int (input('Enter Your choice'))
            total_amount = plates * 250
            print("Grand Total--->", total_amount) 
        
        else:
            print("Invalid choice")

    else:
        print("Invalid choice")


else:
    print("Invalid choice")

