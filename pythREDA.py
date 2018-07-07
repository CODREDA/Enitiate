m = 0
f = 0
while f>=0 and m>=0 :
    m = eval(input("please enter the midterm grade"))
    f = eval(input("please enter the final grade"))
    fg = 0.2*m + 0.8*f
    print("the final grade is :",fg)
if f<0 or m<0 :
    print("not possible")









while True :





print("you scored %d and %d in your two midterms and %d in your final exam and your grade is %s" %(midterm1, midterm2, final, grade))
you scored 60 and 50 in your two midterms and 85 in your final exam and your grade is A    




def one (base,expo):
    result = base**expo
    print("result is :",result)
def two (base,expo):
    import math
    result=pow(base,expo)
    print("result is :",result)
def tri (base,expo):
    result = 1
    for i in range(expo):
        result=result*base
    print("result is :",result)
    


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
