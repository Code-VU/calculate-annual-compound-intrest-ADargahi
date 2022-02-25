def calculateCompoundInterest():
    count = 0
    for i in range(0, 3):
        count += 1
        # This first 3 lines are provided for you
        client_one_principal = float(input("Principle (amount): "))
        client_one_time =      float(input("Time:               "))
        client_one_rate =      float(input("Rate:               "))

        amount = client_one_principal * (1.0 + client_one_rate/100.0)**client_one_time
        compInt = amount - client_one_principal

        print("Compound Interest: "+str("{:.2f}".format(compInt)))

        if count == 3:
            break
        else:
            print("---")


    # end assignment
## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
