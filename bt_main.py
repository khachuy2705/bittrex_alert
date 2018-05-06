# -*- coding: utf-8 -*-
import requests
# import os
import config
import json
import time
import telegram_module
# from twilio.rest import Client
#
#def send_sms(list_nguoi_nhan,noi_dung):
#	# return nguoi_nhan
#	may_khach = Client(config.account, config.token)
#	for a in list_nguoi_nhan:
#		a="+84"+a[1:len(a)]
#		message = may_khach.messages.create(to='+84888354345', from_=config.from_twilio,body=noi_dung)
# print(r.content)
def main():
	r = requests.get(config.pre_link)
	data = json.loads(r.content)
	if data['success'] == True:
		# print(data['result'][0])
		newest_price=data['result'][0]['Last']
		print(newest_price)
		change=(newest_price - config.first_price)/config.first_price*100
		print(change)
		if change > 5:
			sms='Chenh lech '+str(round(change,2))+' %\r\n'+'Gia cu = '+str(config.first_price)+'\r\n'+'Gia moi = '+str(newest_price)+'\r\n'+'my volume = '+str(config.current_value*newest_price)+'\r\n'+data['result'][0]['MarketName']
			# send_sms(config.sdt, sms)
			a=telegram_module.telegram_send_to(config.chat_id,sms,config.api_telegram)
			# print(a)
			time.sleep(60)
if __name__ == '__main__':
	while True:
		try:
			main()
			time.sleep(60)
		except Exception as value:
			print(value)
			pass
		time.sleep(60)
# may_khach = Client(account, token)
	# print(result)
# print(data['success'])