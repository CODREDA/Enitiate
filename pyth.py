m = 0
f = 0
while f>=0 and m>=0 :
    m = eval(input("please enter the midterm grade"))
    f = eval(input("please enter the final grade"))
    fg = 0.2*m + 0.8*f
    print("the final grade is :",fg)
if f<0 or m<0 :
    print("not possible")
