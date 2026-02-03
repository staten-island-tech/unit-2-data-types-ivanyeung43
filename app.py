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



def discount(age, is_member, is_resident):
    if age < 12 or age > 65:
        print("eligible for discount")
    else:
        print("not eligible for discount")
    
    if is_member == True or is_resident == True:
        print("eligible for discount")
    else:
        print("not eligible for discount")
    return
age = 11
is_resident = True
is_memeber = True
