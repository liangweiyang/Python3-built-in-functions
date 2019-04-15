#all函数，用于判断可迭代参数是否都为true，是则返回true，否则返回false
#可迭代对象包括字典、元祖、列表等
#元素出0 空 NONE false外都算true
a=[1, 2, 3]
print(all(a))

b=[0, 1, 2]
print(all(b))

c = (1, 2, 3)
print(all(c))

d = {"m": "1"}

print(all(d))