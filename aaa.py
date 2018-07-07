def reda(str,pos):
        if pos < len(str) and pos >= 0:
            print(str[pos])
        else:
            print("impossible! please enter again")









def func(name):
    a = ""
    for i in range (1,(len(name)+1)):
        a=a+name[-i]
    print(a)
