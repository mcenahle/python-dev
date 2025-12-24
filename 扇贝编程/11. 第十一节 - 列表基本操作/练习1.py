"""
今天英语课上，老师教了十二个月份对应的英语单词。贾宝玉为了让自己记住全部的十二个单词，都将他们保存在了列表里。
但是粗心的贾宝玉有些地方写错了，需要聪明的你通过刚刚学到的列表操作帮助他修改一下，具体要求如下：
将错写的英文单词 Mach 修正为 March；
在七月（July）后添加八月对应的英文单词 August；
在列表最后添加十二月对应的英文单词 December；
打印出正确的 month 列表
"""

month = [
  'January',
  'February',
  'Mach',
  'April',
  'May',
  'June',
  'July',
  'September',
  'October',
  'November'
]

month[2] = "March"
month.insert(6, "August")
month.append("December")
print(month)