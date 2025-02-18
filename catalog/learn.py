def sumnum(x,y,z):
    print(x+y+z)

def p_args(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}--->{v}")

def examp(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    for m in args:
        print(m)
    for k, v in kwargs.items():
        print(f"key is {k} and value is {v}")


atup=(3,6,9)
alist=[4,5,6]
p_args(a=4,b=3,c=9)
examp("One",7,"Three",10,9,8,animal="Dog",color="Red")