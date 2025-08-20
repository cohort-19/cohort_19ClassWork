# 1. Static Function
def static_netpay():
    print("hello, client, welcome to our static netpay calculator")
    gross = 1000000
    is_ugandan = True  

    if not is_ugandan:
        paye_rate = 0.35
        nssf_rate = 0.05
    elif gross >= 700000:
        paye_rate = 0.3
        nssf_rate = 0.05
    elif gross > 300000:
        paye_rate = 0.0
        nssf_rate = 0.05
    else:
        paye_rate = 0.0
        nssf_rate = 0.05

    paye = gross * paye_rate
    nssf = gross * nssf_rate
    netpay = gross - (paye + nssf)

    print("Gross:", gross)
    print("PAYE:", paye)
    print("NSSF:", nssf)
    print("This is your Net Pay:", netpay)
    print()

# 2. Interactive Function
def interactive_netpay():
    print("Hello Client, welcome to our interractive net pay calculator")
    gross = float(input("Enter gross salary: "))
    nationality = input("Are you Ugandan? (yes/no): ")

    is_ugandan = nationality == 'yes'

    if not is_ugandan:
        paye_rate = 0.35
        nssf_rate = 0.05
    elif gross >= 700000:
        paye_rate = 0.3
        nssf_rate = 0.05
    elif gross > 300000:
        paye_rate = 0.0
        nssf_rate = 0.05
    else:
        paye_rate = 0.0
        nssf_rate = 0.05

    paye = gross * paye_rate
    nssf = gross * nssf_rate
    netpay = gross - (paye + nssf)

    print("Gross:", gross)
    print("PAYE:", paye)
    print("NSSF:", nssf)
    print("This is your Net Pay:", netpay)
    print()

# 3. Dynamic Function
def dynamic_netpay(gross, is_ugandan=True):
    print("Hello Client, welcome to our dynamic netpay calculator")

    if not is_ugandan:
        paye_rate = 0.35
        nssf_rate = 0.05
    elif gross >= 700000:
        paye_rate = 0.3
        nssf_rate = 0.05
    elif gross > 300000:
        paye_rate = 0.0
        nssf_rate = 0.05
    else:
        paye_rate = 0.0
        nssf_rate = 0.05

    paye = gross * paye_rate
    nssf = gross * nssf_rate
    netpay = gross - (paye + nssf)

    print("Gross:", gross)
    print("PAYE:", paye)
    print("NSSF:", nssf)
    print("This is your Net Pay:", netpay)
    print()

# //// Call the functions ////
#static_netpay()

interactive_netpay()

# Dynamic examples
#dynamic_netpay(250000)                    
#dynamic_netpay(600000)                    
#dynamic_netpay(900000)                    
#dynamic_netpay(500000, is_ugandan=False)  