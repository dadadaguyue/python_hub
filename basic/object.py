'''
常见的数据类型有以下六种：
可变三种：
    Number（数字），String（字符串），Tuple（元组）
不可变三种：
    List（集合），Dictionary（字典），Set（集合）
'''
name = '张三'
age = 18
height = 1.88  # 浮点型
print(type(name), type(age), type(height))

# 字符串相关使用
# 可以使用[头下标 ：尾下标] 头下标从0开始
str = 'apple'
print(str[1:5])
# 字符串连接
val = 'hello world'
print(val, ',python')
print(val + '+python')
# List
list_demo = ['张三', 34, 5.6, 'beijing']
print(list_demo)
# 获取集合值
print(list_demo[0])
print(list_demo[0:2])
# 添加与删除集合
list_demo.append('test')
del list_demo[4]
# 元组同集合类似，但是元组的元素不能修改,删除
# 元组使用小括号，集合使用中括号
tuple_demo = ('李四',22,5.3,'北京')
print(tuple_demo)
# 空元组创建
tup1 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号
tup2 = (55,)
print(tuple_demo[0])
print(tuple_demo[0:2])
# 元组连接
tup = tup1 + tup2
# 元组元素无法删除，但可以删除整个元组
del tup
# set

# dictionary

