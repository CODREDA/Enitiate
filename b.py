print(".....................Menu......................")
print("1.historical")
print("2.nature")
print("3.social")
print("...............................................")
a=input("please enter your choice")
if a.isdigit():
    a=eval(a)
    if a==1 :
        print("lion statue in downtown")
    if a==2 :
        print("ain vitel nature park")
    if a==3 :
        print("visiting Dar-Al-Hanae women’s baking cooperative")
    if a<1 or a>3 :
        print("error , please enter 1 , 2 or 3 ")
