#any函数，用于判断可迭代参数是否全部为false，是则返回false，如果有一个为true，则返回true

a=[1, 2, 3]
print(any(a))

b=[0, 0, 0]
print(any(b))

c = (0, 0, 0)
print(any(c))

d = {'m': 0, 'n':0, 'l':0}      #字典里面0值不为false

print(any(d))