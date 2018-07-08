num=input("please enter a number")
if num.isdigit():
    numbr=eval(num)
    square=numbr**2
    print("square:",square)
else:
    print("error, please enter a number")
