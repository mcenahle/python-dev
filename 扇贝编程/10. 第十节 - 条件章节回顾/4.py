"""
改错：
enemy = '镜妖'
if enemy = '银狼' or enemy = '黑魔法师'
print('使用火球术进行攻击')
else enemy = '镜妖'
print('使用荆棘术进行攻击')
else
print('使用苹果炸弹进行攻击')
"""
enemy = '镜妖'
if enemy == '银狼' or enemy == '黑魔法师':
    print('使用火球术进行攻击')
elif enemy == '黑魔法师':
    print('使用荆棘术进行攻击')
else:
    print('使用苹果炸弹进行攻击')