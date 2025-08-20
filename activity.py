#print out a welcoming note to the employee
#get a variable to store the gross pay of an employee
#get avariable to store the tax rates
#get a variable to keep the calculation of tax rate multiply it with the gross pay
#get another variable to store the net pay after the tax from the variable above is deducted from the gross pay
#with a message prin ot the net pay to the employee



print("Welcome, Maria")
def gross() :
    gross, taxrate = 900000, 0.3
    tax= gross * taxrate
    netpay = gross - tax
    print("your netpayis: ", netpay )
gross()
print("Hey maria, thank you for choosing us, see you next time")




def PAYE(gross, taxrate):
    print("Welcome, calculate your netpay with us")
    tax = gross * taxrate
    netpay = gross - tax
    print("Your net pay is:", netpay)
    print("Hey, thank you for choosing us, see you next time")
PAYE(1000000, 0.3)
PAYE(500000, 0.3)
PAYE(2300000, 0.3)


#using a static function, an interractive functuion and synamic function demonstrate how u can calculate an employee's net pay after deducting PAYE and NSSF (with input to capture info from the keyboard).




