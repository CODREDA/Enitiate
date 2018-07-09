def again():
    x=0
    a=0
    g=(input("enter a grade"))
    while g!="":
        g=eval(g)
        a=a+g
        x=x+1
        g=(input("enter a grade"))
    print("the average is :",a/x)
