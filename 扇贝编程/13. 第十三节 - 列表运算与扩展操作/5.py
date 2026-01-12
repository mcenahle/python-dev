"""
用刚刚学过的代码帮他对 books_favorite 进行操作，附上数字表示的排名吗？
要求：
用 zip() 函数将 books 和 authors 以“著作名，作者”的形式结合成新列表。并将结果打印在屏幕上。
用 enumerate() 函数，从 1 开始，枚举 books_favorite 列表，将结果打印在屏幕上。
最终的打印结果参考：
[('红楼梦', '曹雪芹'), ('三国演义', '罗贯中'), ('水浒传', '施耐庵'), ('西游记', '吴承恩')]
[(1, '三国演义'), (2, '西游记'), (3, '红楼梦'), (4, '水浒传')]
"""
books = ['红楼梦', '三国演义', '水浒传', '西游记']
authors = ['曹雪芹', '罗贯中', '施耐庵', '吴承恩']
# 用 zip() 将两个列表绑定
zipped = zip(books, authors)
# 转换回列表后打印绑定结果
print(list(zipped))
# 新建 books_favorite 列表，顺序按小贝的喜好来
books_favorite = ['三国演义', '西游记', '红楼梦', '水浒传']
# 用 enumerate() 函数枚举 books_favorite，从 1 开始
rank_with_favourite = list(enumerate(books_favorite, start = 1))
# 转换回列表后打印结果
print(rank_with_favourite)