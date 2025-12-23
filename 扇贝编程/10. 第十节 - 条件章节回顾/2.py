"""
店铺优惠政策如下：凡是在 9 点至 15 点之间到店消费的，是冒险者就打八折，不是冒险者就打九折。
请你补全 discount() 函数，discount() 函数的第一个参数 time 是消费时间，用 1-24 表示 1 点至 24 点。第二个参数 is_adventurer 用来表示是否是冒险者。
要求：
time 在 9 到 15 之间（包括 9 和 15）且是冒险者时，打印 冒险者八折；
time 在 9 到 15 之间（包括 9 和 15）且不是冒险者时，打印 优惠九折；
time 不在 9 到 15 之间时，打印 没有优惠。
"""

def discount(time, is_adventurer):
    if 9 <= time <= 15:
        if is_adventurer:
            print("冒险者八折")
        else:
            print("优惠九折")
    else:
        print("没有优惠")

discount(12, True)