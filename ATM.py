for i in range(3):
    AccNo = int(input("Enter your Account Number: "))
    TempAccNo = AccNo
    Count = 0

    while TempAccNo != 0:
        TempAccNo = TempAccNo//10
        Count = Count + 1

    if Count == 8:
        for j in range(3):
            Password = int(input("Enter the Password: "))
            TempPassword = Password
            Count1 = 0

            while TempPassword != 0:
                TempPassword = TempPassword//10
                Count1 = Count1 + 1

            if Count1 == 4:
                print("Welcome to MONEY PULSE ATM")
                break
            else:
                print("Incorrect Password")

        if Count1 == 4:
            break
        else:
            print("Failed to proceed after 3 attempts")
    else:
        print("Invalid Account Number")

if Count != 8 or Count1 != 4:
    print("Failed to proceed after 3 attempts")
else:

    Balance = 1200
    Options = ["Balance", "Credit", "Debit", "Exit"]
    while True:
        print(Options)
        Choose = str(input("Choose any of the above given: "))

        if Choose == Options[0]:
            print(Options[0] + " " + ":" + " " + str(Balance) + "rs")

        elif Choose == Options[1]:
            for l in range(3):
                PIN = int(input("Enter your PIN number: "))
                Count2 = 0
                CurPin = PIN

                while CurPin != 0:
                    CurPin = CurPin//10
                    Count2 = Count2+1
                
                if Count2 == 4:
                    Cash = int(input("Enter the Cash: "))
                    if Cash%100 == 0:
                        Balance = Balance + Cash
                        print(str(Cash) + " " + "rs" + " " + "has been successfully credited to your account!")
                        print("Your Balance: " + str(Balance) + " " + "rs")
                        break
                    else:
                        print("Please enter the cash only in the multiples of 100")
                        break
                else:
                        print("Incorrect PIN")
            if Count2 != 4:
                print("Maximum Attempts reached ... Please try again after sometime")
                break

                
        elif Choose == Options[2]:
            for k in range(3):
                PIN = int(input("Enter your PIN number: "))
                Count3 = 0
                TempPin =  PIN

                while TempPin != 0:
                    TempPin = TempPin//10
                    Count3 = Count3 + 1

                if Count3 == 4:
                    Amt = int(input("Enter the Amount in rupees: "))
                    if Amt <= Balance:
                        print("Here you go:" + " " + str(Amt) + " " + "rs")
                        print("Transaction Successful")
                        Balance = Balance - Amt
                        print("Your Balance:" + " " + str(Balance) + "rs")
                        break
                    elif Amt > Balance:
                        print("Insufficient Balance")
                        print("Your Balance:" + " " + str(Balance) + " " + "rs")
                        break
                else:
                    print("Incorrect PIN")
            if Count3 != 4:
                print("Maximum Attempts reached. Transaction Failed")
                break

        elif Choose == Options[3]:
            print("Your Balance:" + " " + str(Balance) + " " + "rs")
            print("Thank You")
            break
        else:
            print("Invalid Option")
    