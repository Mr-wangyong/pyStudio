print("hello")


# 定义一个函数 用 def
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 可以函数引用传递给一个变量 然后变量当函数用(闭包)
a = my_abs

print(a(10))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
