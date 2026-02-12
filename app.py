""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(values[0])
    print(values[6]) """

""" x = "this is a thing"
y = x.split()
z = y[0]
print(y)
print(z) """



""" def discount(age, is_member, is_resident):
    if age < 12 or age > 65:
        print("eligible for discount")
    else:
        print("not eligible for discount")
    
    if is_member == True or is_resident == True:
        print("eligible for discount")
    else:
        print("not eligible for discount")
    return
age = 13
is_resident = False
is_member = False

discount(age, is_member, is_resident) """

""" user_sentence = input("Type a sentence")

x = user_sentence.split( )

print(len(x)) """

""" x = "test"
print(f"hello {x}")

temp =68
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" number = int(input("Insert a number"))
x = number
if x % 2 == 0:
    print('even')
else:
    print('odd') """

""" """ 
""" bill = float(input("Enter the bill value"))
service = input("How was the service?: Bad, Okay, Good, or Great").lower()
tip = 0

if service == 'bad':
    tip = 0*bill
    print(tip)
elif service == 'okay':
    tip = 0.15*bill
    print(tip)
elif service == 'good':
    tip = 0.20*bill
    print(tip)
elif service == 'great':
    tip = 0.25*bill
    print(tip)

final_bill = bill+tip
print(final_bill) """


""" number = int(input("Enter a Number"))
x = number

for i in range(1, x+1):
    if x%i == 0:
        print(i) """



y = 100
x = 20

for gcf in range(1, x+1):
    if x%gcf == 0 and y%gcf == 0:
        print(f"The gcf of {x} and {y} is {gcf}")




""" ## Tip Calculator

bill = float(input("What is the bill amount?"))
tip = float(input("Tip"))

cal_tip = bill*(1+(tip/100))
print(f"Your total is: ${cal_tip}") 
 """ 
