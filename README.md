# Python3-built-in-functions
## 重写文件练习

## 目录
- [0x01abs.py](#0x01abs.py)
- [0x02dict.py](#0x02dict.py)
- [0x03all.py](#0x03all.py)
- [0x04any.py](#0x04any.py)
	







# [0x01abs.py](0x01abs.py)
	a = -6

	print(abs(a))
# [0x02dict.py](0x02dict.py)
	print(dict(键="值", a="a", b="b"))

	print(dict(zip(["键", "a", "b"], ["值", "a", "b"])))   #映射函数方式构造字典，前面为键，后面为值

	print(dict([("键", "值"), ("a", "a"), ("b", "b")]))   #以数组的形式构建

	a = {"a": 1, "b": 2}

	print(a)
# [0x03all.py](0x03all.py)
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
	
# [0x04any.py](0x04any.py)
	#any函数，用于判断可迭代参数是否全部为false，是则返回false，如果有一个为true，则返回true

	a=[1, 2, 3]
	print(any(a))

	b=[0, 0, 0]
	print(any(b))

	c = (0, 0, 0)
	print(any(c))

	d = {'m': 0, 'n':0, 'l':0}      #字典里面0值不为false

	print(any(d))