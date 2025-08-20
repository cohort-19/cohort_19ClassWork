# 1. Static Function 
def static_netpay():
    print("/// Static Function ///")
    gross = 1000000      
    paye_rate = 0.3      
    nssf_rate = 0.05      
    
    paye = gross * paye_rate
    nssf = gross * nssf_rate
    netpay = gross - (paye + nssf)
    
    print("Gross:", gross)
    print("PAYE:", paye)
    print("NSSF:", nssf)
    print("Net Pay:", netpay)
    print()

# 2. Interactive Function 
def interactive_netpay():
    print("/// Interactive Function ////")
    gross = float(input("Enter gross salary: "))
    paye_rate = float(input("Enter PAYE rate: "))
    nssf_rate = float(input("Enter NSSF rate: "))
    
    paye = gross * paye_rate
    nssf = gross * nssf_rate
    netpay = gross - (paye + nssf)
    
    print("Gross:", gross)
    print("PAYE:", paye)
    print("NSSF:", nssf)
    print("Net Pay:", netpay)
    print()

# Call the function 
interactive_netpay()

# 3. Dynamic Function 
def dynamic_netpay(gross, paye_rate, nssf_rate):
    print("//// Dynamic Function ///")
    paye = gross * paye_rate
    nssf = gross * nssf_rate
    netpay = gross - (paye + nssf)
    
    print("Gross:", gross)
    print("PAYE:", paye)
    print("NSSF:", nssf)
    print("Net Pay:", netpay)
    print()

# call all examples 
static_netpay()                           
interactive_netpay()                       
dynamic_netpay(1500000, 0.3, 0.05)            
dynamic_netpay(2000000, 0.25, 0.05)
