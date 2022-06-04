# 这是一个示例 Python 脚本。
import urllib.request
import jqdatasdk
from jqdatasdk import *
auth('15770832129','He201314') #账号是申请时所填写的手机号；密码为聚宽官网登录密码
display_name = get_security_info('000001.XSHE').display_name
print(display_name)
df = get_price('000001.XSHE', end_date='2022-06-01 14:00:00',count=10, frequency='minute', fields=['open','close','high','low','volume','money'])
#print(df)
tick = (df.close)
print(tick)