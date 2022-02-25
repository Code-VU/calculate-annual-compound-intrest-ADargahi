def calculateCompoundInterest():
    
# This first 3 lines are provided for you
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
    a = client_one_principal * ((1 + client_one_rate/100) ** client_one_time)
    compInt = a - client_one_principal
    limited_float = round(compInt, 2)
    print('Compound Interest:',limited_float)
    print('---')

    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
    a = client_one_principal * ((1 + client_one_rate/100) ** client_one_time)
    compInt = a - client_one_principal
    limited_float = round(compInt, 2)
    print('Compound Interest:',limited_float)
    print('---')
    
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
    a = client_one_principal * ((1 + client_one_rate/100) ** client_one_time)
    compInt = a - client_one_principal
    limited_float = round(compInt, 2)
    print('Compound Interest:',limited_float)


    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
