"""
闻闻使用 Python 记录了自己的书单，总共有两份。现在，让我们对闻闻的书单进行简单的处理。
我们总共需要做两件事：
将两份书单合并；
写一个查询书籍是否在书单里的函数 check_book()，如果在就打印出 已查询到xxx，否则打印出 未查询到xxx（xxx 为要查询的书名）。
"""

books1 = ['活着', '围城', '平凡的世界', '骆驼祥子']
books2 = ['边城', '城南旧事', '撒哈拉的故事', '三体全集']

# 合并两个书单
books = books1 + books2

def check_book(name):
    if name in books:
        print("已查询到" + name)
    else:
        print("未查询到" + name)

check_book('边城')
check_book('红楼梦')