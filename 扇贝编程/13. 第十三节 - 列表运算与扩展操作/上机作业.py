"""
体育老师为要测试金陵十二钗的体育成绩，于是组织她们进行了一次立定跳远测试。老师将她们分成三组，每组四个人，分别记录她们的成绩（单位厘米），储存在列表 group1, group2, group3 中。
现体育老师在要对三组的数据汇总，从高到低排列并附上排名，你能帮帮他吗？
要求：
将题目中的 group1、group2、group3 合并在一起；
对合并后的成绩从高到低排序；
用 enumerate() 函数将排序后的列表从 1 开始枚举，将结果储存在列表 run_rank 中；
打印出 run_rank。
"""

group1 = [198, 133, 154, 166]
group2 = [188, 172, 119, 142]
group3 = [168, 153, 131, 128]

# 将三组的成绩合并到一起
grades = group1 + group2 + group3
# 对合并后的成绩从高到低排序
grades.sort(reverse = True)
# 将合并后的成绩用数字枚举出来，并转换成列表放进 run_rank 中
run_rank = list(enumerate(grades, start = 1))
# 打印最后的排名和成绩
print(run_rank)