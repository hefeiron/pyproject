
#-*- coding: utf-8 -*-
from jqdatasdk import *
auth('15770832129','He201314') #账号是申请时所填写的手机号；密码为聚宽官网登录密码
display_name = get_security_info('000001.XSHE').display_name
print(display_name)
df = get_price('000001.XSHE', end_date='2022-01-30 14:00:00',count=20, frequency='minute', fields=['open','close','high','low','volume','money'])
print(df)
tick = (df.close,df.data)
last = float(mt_info[1])
trade_datetime = mt_info[ 30] +‘ '+ mt_info[31]tick = (last，trade_datetime)
return tick
trade_time = time(9,3o)
while time(9) < trade_time < time(15):
last_tick = getTick()
strategy (last_tick)
trade_time = parser.parse( last_tick[1]).time()#wait for 1 second
sleep( 3)
print( "job done")
def strategy(tick):

