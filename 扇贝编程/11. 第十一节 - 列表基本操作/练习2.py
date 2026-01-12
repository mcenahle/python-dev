"""
贾宝玉不满足前面好不容易写好的十二月份单词列表。他还想自己制作一个月份翻译器。他希望编写一个函数，自己输入一个月份对应的英文单词，函数就可以输出对应的月份中文，如“一月”。
接下来，我们按照下面的步骤完成这个函数吧：
创建一个 translate() 函数，参数为 word，代表输入的单词；
translate() 函数作用是打印输入月份单词的翻译，比如输入 January 则打印出一月。
提示：可以创建一个列表保存翻译内容，位置和英文单词一一对应，这样就可以通过位置来查询翻译结果。
"""

month = [
  'January',  'February',  'March',  'April',
  'May',  'June',  'July',  'August',
  'September',  'October',  'November',  'December'
]

translated_month = [
  '一月',  '二月',  '三月',  '四月',  '五月',  '六月',
  '七月',  '八月',  '九月',  '十月',  '十一月',  '十二月'
]

def translate():
    word = input("请输入一个月份对应的英文单词：")
    if word in month:
        idx = month.index(word)    # 在 month 中找到对应的序号，记为 idx
        print(translated_month[idx])     # 在 translated_month 中找到第 idx 项
    else:
        print("没有该项。")

# 调用
translate()