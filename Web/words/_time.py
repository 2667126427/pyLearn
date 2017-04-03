from datetime import datetime

date_str = '2016年07月14日20点00分'
date = datetime.strptime(date_str, '%Y年%m月%d日%H点%M分')
print(date)