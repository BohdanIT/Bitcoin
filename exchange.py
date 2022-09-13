bitcoin = 21000
amount = "BTC"

# Welcome new user.
question = input("Hello, do you want to by a BTC?\nInput yes/no: ")

# The user decides if he wants to exchange currency.
if question.lower() == "yes":
    print("Bitcoin price today is 21 000.")
    try:
        how_much = int(input("How much $ do you have?: "))
    except ValueError:
        print("Hmm... Please input valid number.")
    can_buy = '{:.7f}'.format(how_much / bitcoin)
    print(f"You can buy {can_buy} {amount}.")

elif question.lower() == "no":
    print("Bitcoin price today is 21 000.")
    exit("See you later.")

else:
    exit("Please try again.")
