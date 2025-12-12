# 定义函数时，括号中写进预设的变量 fruit
def make_juice(fruit):
  # 把 fruit 写进函数体中
    print('将' + fruit + '去皮')
    print('将' + fruit + '切块')
    print('将切碎的' + fruit + '放进榨汁机')
    print('将果汁倒进杯子中')
    print('制作完成！')

# 做苹果汁
make_juice('苹果')
# 做桃子汁
make_juice('桃子')