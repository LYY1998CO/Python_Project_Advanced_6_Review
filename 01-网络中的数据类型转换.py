"""
计算机中保存的数据是二进制类型的(我们给计算发的数据也是要字符串类型转换成二进制类型),
而返回给我们的数据也是二进制类型,想要看懂计算机返回的什么内容,需要将二进制类型转换成字符串类型
编码:将字符串转换成二进制 str.encode(编码格式)
解码:将二进制转换成字符串 bytes.decode(编码格式)
"""

str1 = 'hello world'
print(str1)
# 转换成二进制类型,编码
bytes1 = str1.encode('utf-8')
print(bytes1)

# 将bytes1转换成字符串,解码
str2 = bytes1.decode('utf-8')
print(str2)

str3 = '你好，世界'
print(str3.encode('gbk'))
print(str3.encode('gbk').decode('gbk'))

str4 = '你好，世界'
print(str4.encode('utf-8'))
print(str4.encode('utf-8').decode('utf-8'))
