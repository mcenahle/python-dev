scores = [100, 92, 77, 85, 81, 90, 100, 86, 79, 93, 91, 96, 75, 84]

# 对 scores 进行排序
scores.sort()
# 计算这次考试成绩的极差
result = scores[-1] - scores[0]
print(result)

# 统计考100分的人数
scores_100 = scores.count(100)
print(scores_100)