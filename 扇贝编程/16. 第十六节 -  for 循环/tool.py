# 下方代码用于生成密码，请勿更改！

# 导入 random 模块（将在第 20 关学习
import random
# 密码生成函数 generate_password()
def generate_password(type, digit=4):
  '''
  随机生成并返回 ``digit`` 位密码

  参数列表
  -------
  ``digit``: 整数，表示需要生成多少位密码，默认为 4 位
  ``type``:  字符串，值为 ``'date'`` 表示生成一个 4 位日期，值为 ``'mix'`` 表示生成混合密码

  返回值
  -----
  一个有 ``digit`` 个字符的字符串
  '''

  # 数字列表
  nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  # 小写字母列表
  lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  # 月份-日期范围字典（将在第 18 关学习
  month_max_days = {
    '01': 31,
    '02': 29,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31,
  }

  # 根据 type 参数的值，生成对应密码
  if type == 'date':
    month = random.choice(list(month_max_days.keys()))  # 随机挑选一个月份
    day = random.randint(1, month_max_days[month])  # 随机挑选一个日期
    return f'{month}{str(day).zfill(2)}'  # （将在第 17 关学习
  elif type == 'mix':
    valid_chars = nums + lower_chars  # 合并得到合法字符表
    password = [random.choice(valid_chars) for i in range(digit)]  # 生成密码
    return ''.join(password)  # 返回密码（将在第 17 关学习
  else:
    return ''