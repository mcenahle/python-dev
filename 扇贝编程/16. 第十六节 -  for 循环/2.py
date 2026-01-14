# 蟹堡王今日订单数据
orders = [91, 4, 20, 67, 24, 13, 84, 40, 77, 47]
# 大额订单（> 70 元的）
big_deals = [fee for fee in orders if fee > 70]
# odd_nums = [num for num in nums if num % 2 == 1]
print(big_deals)