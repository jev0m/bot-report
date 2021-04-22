import requests,uuid,secrets
from time import sleep
uid = uuid.uuid4()
r = requests.Session()
cookie = secrets.token_hex(8)*2
#target = input('target:')
#sle = int(input('sleep:'))
def login(user,password,tar):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':user,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login= r.post(url,headers=headers,data=data);n=req_login	
    if 'checkpoint' in n.text:
    	return '- الحساب طالب سكيور ❎🔒'

    elif '"authenticated":false' in n.text:
    	return '- كلمة السر او اليوزر غير صحيح ❎'
#	    return n.text
    elif 'userId' in n.text:
    	r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
    	url_id = 'https://www.instagram.com/{}/?__a=1'.format(tar)
    	if r.get(url_id).status_code == 200:
    	              		        	req_id = r.get(url_id).json()
    	              		        	user_id = str(req_id['logging_page_id'])
    	              		        	idd = user_id.split('_')[1]#
    	              		        	url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
    	              		        	datas = {'source_name':'','reason_id':1,'frx_context':''}
    	              		        	report = r.post(url_report,data=datas)
    	              		        	return True
    	else:
    	         		return '404'
    	         		
    	         		
    	         		

    else:
    	return False

 		       
