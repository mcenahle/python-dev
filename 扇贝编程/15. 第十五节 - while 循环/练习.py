"""已知一张纸厚度大约为 0.08mm。假设纸张能够无限次对折，那么它对折多少次之后，纸张总厚度能达到珠穆朗玛峰的高度（8848.13 米）呢？
为解决这一问题，我们可以设置变量 mount 保存珠峰高度，设置变量 paper 保存当前纸张总厚度，设置变量 count 统计对折次数。之后编写 while 循环指挥计算机：
当 paper 变量值小于 mount 时，不断对折纸张，令厚度翻倍，记录对折次数；
直到纸张总厚度与珠峰高度相等，循环结束，打印 count 变量值。
问题分析完毕，下面请你自己编写程序，看看究竟需要对折多少次吧～"""

# 珠峰高度
mount = 8848130
# 当前纸张厚度
paper = 0.08
# 当前对折次数
count = 0
while paper < mount:
    count += 1
    paper *= 2
"""
while paper < mount:
    count += 1
    paper = paper * 2
    if paper == mount:  # 使用 "==" 进行比较，请注意区分 = 和 ==
        print(count)
        break
"""
print('需要对折' + str(count) + '次')