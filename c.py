from random import randint

def game():
    n=2
    x=7
    y=eval(input("guess:"))
    while n!= 0:
        if y<x :
            print("sgher")
            
        elif y>x :
            print("fettih")
            
        else :
            print("LAS9AAAA!")
            break
        y=eval(input("guess:"))
        n=n-1
    if n==0 and y==x :
        print ("Congrats!")
    else :
        print("game over")
