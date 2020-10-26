#   学  校：广西大学
#   开发者：王小勇
#   python:python3.9
#   开发时间：2020/10/11 14:21
# 转义字符
print('hello\nworld')   #\ +转义功能的字母     n-->newline的首字母表示换行
print('hello\tworld')
print('helloooo\tworld')    #跳到下一个制表符
print('hello\rworld')   #world将hello进行了覆盖
print('hello\bworld')   #\b-->退格,将o退没了

print('http:\\\\www.baidu.com')
print('老师说：\"大家好！\"')

#原字符：不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上r或R
print(R'hello\tworld')
#注意：最后一个字符不能是反斜杠\
# print(R'hello\tworld'\)
print(R'hello\tworld\\')
