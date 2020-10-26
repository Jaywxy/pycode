#   学  校：广西大学
#   开发者：王小勇
#   python:python3.9
#   开发时间：2020/10/11 14:00


#   print()函数
#   内容可以是数字，字符串，含有运算符的表达式
print(520)
print(98.5)

print('hello world')
print("hello world")
print("hello world\n"*3)

print(2+3)
#   目的地：显示器、文件
#   输出到文件中，注意点：1.所指定的盘符要存在 2.使用file=fq
fq = open('E:/test.txt','a+')    # 'a+'表示如果该路径中没有该文件就创建，有就在文件后附加
print("hello world",file=fq)
fq.close()

#   输出方式：换行，不换行(用,隔开)
print('hello','world','python')

