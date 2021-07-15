# lets start learining python
print("Hello world")
x = "2hello"
y = 4
print(x, y)

# types of declyaring

x, y, z = "kalugota", "Ravi", "Teja"
print(x, y, z)
# 2
x = y = z = "KRT"
print(x)
print(y)
print(z)

# Unpacking List
listl = ["Ravi", "Teja", "K"]
x, y, z = listl
print(x)
print(y)
print(z)

a = "awesome"
b = " is "
print("raviteja" + b + a)
c = b + a
print("HAAHHA  raviteja " + c)

# variables that are created outside the function is called Global variable
x = "awesome"


def randomfun():
    print("shit is getting real " + x)


randomfun()


def tt_randfun():
    x = "great"
    print("LOL No Global varible " + x)


tt_randfun()
print("lol Yes Global variable" + x)
