# 导入calendar模块、日历
import calendar
'''
yy = 2025
mm = 12
print(calendar.month(yy, mm))
'''
# 年历

cal = calendar.TextCalendar()

# 打印 2026 年的年历
print(cal.formatyear(2026))