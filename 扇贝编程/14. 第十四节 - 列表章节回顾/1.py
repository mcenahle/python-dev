"""
现在有两个列表：letters1 和 letters2，它们中间各藏着一句七言诗。只要在每个列表的 首尾各截去三个元素，就可以看出其中包含的七言诗是什么了。
请你补全 print_center 函数，作用是打印出 letters1 列表和 letters2 列表里 首尾各截去三个元素 后的新列表。
"""
letters1 = ['天', '前', '我', '最', '是', '人', '间', '留', '不', '住', '去', '日', '台']
letters2 = ['而', '红', '的', '朱', '颜', '辞', '镜', '花', '辞', '树', '他', '轩', '徐']

def print_center(letters):
    # 截去开头三个元素
    letters1_cut_1 = letters1[3:]
    letters2_cut_1 = letters2[3:]
    # 截去末尾三个元素
    letters1_cut_2 = letters1_cut_1[:-3]
    letters2_cut_2 = letters2_cut_1[:-3]
    # 打印处理后的列表
    print(letters1_cut_2)
    print(letters2_cut_2)

print_center(letters1)
print_center(letters2)