"""
补全函数 choose_reward，该函数有两个参数，分别是 math_score（数学成绩）和 physics_score（物理成绩）；
将每一级奖励都用布尔表达式表示，使用 if ... elif ... else 语句为刘星的成绩匹配学习奖励。比如如：若数学成绩达到 75 分，且物理成绩达到 70 分，也就是满足 math_score >= 75 and physics_score >= 70 的条件，就打印 奖励一台新电脑。
"""

reward1 = '奖励一台新电脑'
reward2 = '奖励一顿油焖虾'
reward3 = '奖励一顿胖揍'
def choose_reward(math_score, physics_score):
    if math_score >= 75 and physics_score >= 70:
        print(reward1)
    elif math_score >= 60 and physics_score >= 60:
        print(reward2)
    else:
        print(reward3)

# 假设刘星数学考了 76，物理考了 71
choose_reward(76, 71)