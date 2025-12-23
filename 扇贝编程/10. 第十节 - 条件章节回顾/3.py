"""
小红帽买装备的时候，店老板告诉她，充值 1000 元返利 300 元，充值 500 元返利 100 元，充值 100 元返利 20 元，返利不叠加。小红帽二话不说就充了 1000 元，却只拿到了 20 元的返利，她大为光火，结果店老板竟然一脸无辜地告诉她这是 Python 算的，不关他的事。
下面是店老板用来计算返利额度的代码，你能帮助小红帽发现其中的问题，并将代码改得符合店家的宣传吗？

recharge = 1000
if recharge >= 100:
    rebate = 20
elif recharge >= 500:
    rebate = 100
elif recharge >= 1000:
    rebate = 300
print(rebate)
"""
recharge = 1000
if recharge >= 1000:
    rebate = 300
elif recharge >= 500:
    rebate = 100
elif recharge >= 100:
    rebate = 20
print(rebate)