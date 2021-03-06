#字符串类型的表示
#由0个或多个字符组成的有序字符序列
#-字符串是字符的有序序列，可以对其中的字符进行索引
#“请”是“请进入操作界面”的第0个字符
'''字符串有两类4种表示方式，包括 “” '' ''''''
其中三单引号也是字符串，是多行字符串，具有注释的作用
'''
#使用[]获取字符串中的一个或者多个字符
#-索引：返回字符串中的单个字符,"请输入带有符号的温度值："[0] 或者 TempStr[-1]
#-切片：返回字符串中的一段字符字串，"请输入带有符号的温度值："[0:5] 或者 TempStr[0:-1]
"请输入带有符号的温度值："[1:5]#<字符串>[M:N],M表示缺失到开头但不包括M，N表示缺失到结尾包括N
TempStr[0:-1]
print('TempStr'[0:3])
print("零一二三四五六七"[:3])
#<字符串>[M:N:K],根据步长对字符串切片
print('零一二三四五六七八九十勾圈凯'[0:8:2])#根据M和N的数值对字符串掐头去尾后，以两个字节为步长，每个步长中选前面那个字
#将字符串中的内容顺序倒置
'零一二三四五六七八九十勾圈凯'[::-1]
#转义符\,转义符表示特定字符的本意
"这里有个双引号(\")"
#字符串操作符
"x"+"y"#连接两个字符串x和y
n*"x"或者"x"*n#复制n次字符串x
"x" in "s"#如果x是s的字串，返回True，否则返回False
#获取星期字符串#
#WeekNamePrintV1.py
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekID=eval(input("请输入星期数字（1-7）："))
pos=(weekID-1)*3
print(weekStr[pos:pos+3])
#获取星期字符串简化版#
#WeekNamePrintV2.py
weekStr="一二三四五六七"
weekID=eval(input("请输入星期数字（1-7）："))
print("星期"+weekStr[weekID-1])
