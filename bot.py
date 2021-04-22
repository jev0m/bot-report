tttext = '''
import account
EzTG = account
import json
import login
l = login
import time
try:
	
	async def callback(bot, update):
	    # here's your bot
	    if 'message' in update:
	        # messages "handler"
	        message_id = update['message']['message_id']  
	        user_id = update['message']['from']['id']
	        chat_id = update['message']['chat']['id']
	        text = update['message']['text']
	        if text == '/start':
	            if str(chat_id) in open('data.json','r').read():
	            	keyboard = EzTG.Keyboard('inline')
	            	keyboard.add(' - كيف أستخدم البوت ❔ ', 'help')
	            	keyboard.add(' - لوحة التحكم 📬⚙', 'sppam')		 
	            	keyboard.newLine()     
	            	keyboard.add('- SAYCO', 'https://t.me/brofhak')
	            	await bot.sendMessage(chat_id=chat_id, text=' - By: @brofhak',
	                            reply_markup=keyboard)

	            else:
	            	file = open('data.json','r').read()
	            	js = json.loads(file)
	            	js[str(chat_id)] = {"user":"NULL","pass":"NULL","target":"NULL","type":"spam","com":"200","yes":"True"}
	            	
	            	filee = open('data.json','w')
	            	filee.write(json.dumps(js))
	            	filee.close()
	            	keyboard = EzTG.Keyboard('inline')
	            	keyboard.add(' - كيف أستخدم البوت ❔ ', 'help')
	            	keyboard.add(' - لوحة التحكم 📬⚙', 'sppam')		 
	            	keyboard.newLine()     
	            	keyboard.add('- SAYCO', 'https://t.me/brofhak')
	            	await bot.sendMessage(chat_id=chat_id, text=' - By: @brofhak',
	                            reply_markup=keyboard)
	
					
	        
	        if text.count(':') == 2:
				       		
	        	if text.count(':') == 2:
	    
	        		keyboard = EzTG.Keyboard('inline')
	        		keyboard.add('- حفظ ✅', 'save')
						     
	        		keyboard.add('- إلغاء ❎','no')			
	        		await bot.sendMessage(chat_id=chat_id,
	                                text=f"- User: {text.split(':')[0]} \n- Pass: {text.split(':')[1]}\n- Target: {text.split(':')[2]} " ,reply_markup=keyboard)
												 
							       
						 
	        		
	
	        		
	    if 'callback_query' in update:
	  
	        message_id = update['callback_query']['message']['message_id']
	        user_id = update['callback_query']['from']['id']
	        chat_id = update['callback_query']['message']['chat']['id']
	        cb_id = update['callback_query']['id']
	        cb_data = update['callback_query']['data'];text= update['callback_query']['message']['text']
	        #try:
	        if True or True:
	         		
		        		
		        if cb_data == 'sppam':
	
		            filedata = open('data.json','r').read()	    				 
		            js = json.loads(filedata)
							  
		            keyboard = EzTG.Keyboard('inline')
		            keyboard.add('- قسم الحسابات 📬⚙', 'acc')
		            keyboard.newLine()        
		            keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		            keyboard.add('- نوع البلاغات ©','type')
	
	
	#	            keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		            keyboard.newLine()
		            keyboard.add(f'{js[str(chat_id)]["com"]}','con')
		            keyboard.add('- عدد البلاغات 🎰','count')
						       
	#	            keyboard.add(f'{js[str(chat_id)]["com"]}','con')
		            keyboard.newLine()
		            keyboard.add('- بدأ 🎯','start')
						      
		            keyboard.newLine(      )
		            keyboard.add('- SAYCO ','https://t.me/brofhak')
								 
			     
		            await bot.editMessageText(chat_id=chat_id, message_id=message_id,
		                                text='- By: @brofhak', reply_markup=keyboard)
		        
	
		
		        if cb_data == 'acc':
		            filedata = str(open('data.json','r').read());h=str(filedata)	    				 
		            js = json.loads(h)
		            if js[str(chat_id)]['user'] == 'NULL':
				 			  
		             keyboard = EzTG.Keyboard('inline')
		             keyboard.add('- إضافة حساب ➕', 'add');keyboard.newLine()
						   
		             keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
		             await bot.editMessageText(chat_id=chat_id, message_id=message_id,
			                                text='- Calss Acounts', reply_markup=keyboard)
			
		            	
		            	
		            else:
		            	
			            keyboard = EzTG.Keyboard('inline')
			            keyboard.add(' - User: ', 'ushhher')
			            keyboard.add(f'{js[str(chat_id)]["user"]}', 'user')
			            keyboard.newLine()
			            keyboard.add('- Pass:','passu')
			            keyboard.add(f'{js[str(chat_id)]["pass"]}','pass')
						       
			            keyboard.newLine()
			            keyboard.add('- Target:','couggnt')
			            keyboard.add(f'{js[str(chat_id)]["target"]}','target')
			   			       		  
			            keyboard.newLine();keyboard.add('- تغير المعلومات ♻','add');keyboard.newLine()
							 			   
			            keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
			            await bot.editMessageText(chat_id=chat_id, message_id=message_id,
			                                text='- Calss Acounts', reply_markup=keyboard)
			
					   
		        if cb_data == 'mn':
		        		edite= open('data.json','r').read()
		        		js = json.loads(edite)
		        		keyboard = EzTG.Keyboard('inline')
		        		keyboard.add('- قسم الحسابات 📬⚙', 'acc')
		        		keyboard.newLine()
		        		keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		        		keyboard.add('- نوع البلاغات ©','type')
		        #		keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		        		keyboard.newLine()
		        		keyboard.add(f'{js[str(chat_id)]["com"]}','con')
		        		keyboard.add('- عدد البلاغات 🎰','count')
			
	
		        	#	keyboard.add(f'{js[str(chat_id)]["com"]}','con')
		        		keyboard.newLine()
		        		keyboard.add('- بدأ 🎯','start')
								  
		        		keyboard.newLine()     
		        		keyboard.add('- SAYCO ','https://t.me/brofhak')
		        		await bot.editMessageText(chat_id=chat_id, message_id=message_id,
		                                text='- By: @brofhak', reply_markup=keyboard)
		        
		
		
		        
		        if cb_data == 'add':
		                                keyboard = EzTG.Keyboard('inline')
		                                keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
		                                await bot.editMessageText(chat_id=chat_id,message_id=message_id,
		                                text='أرسل حسابك و يوزر الضحية با هدا الشكل:\nyour_user:your_pass:your_target\n- مثال:\nbrofhak:12345:isreal',reply_markup=keyboard)
		                                
		                                
													 
		        	
		        
		        if cb_data == 'save':
			        	edite= open('data.json','r').read()
			        	js = json.loads(edite)
			        	js[str(chat_id)]["user"] = text.split(' ')[2]
			        	js[str(chat_id)]["pass"] = text.split(' ')[5].split('\n')[0]
			        	js[str(chat_id)]["target"] = text.split(' ')[7]
#			        	print (js)
			        	file = open("data.json","w")
			        	file.write(json.dumps(js))
			        	file.close()
			        	
			        	
			        	
			        	keyboard = EzTG.Keyboard('inline')
			        	keyboard.add(' - User: ', 'ushhher')
			        	keyboard.add(f'{js[str(chat_id)]["user"]}', 'user')
			        	keyboard.newLine()
			        	keyboard.add('- Pass:','passu')
			        	keyboard.add(f'{js[str(chat_id)]["pass"]}','pass')
			        	keyboard.newLine()
			        	keyboard.add('- Target:','couggnt')
			        	keyboard.add(f'{js[str(chat_id)]["target"]}','target')
			        	keyboard.newLine();keyboard.add('- تغير المعلومات ♻','add');keyboard.newLine()
			        	keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
			        	await bot.editMessageText(chat_id=chat_id, message_id=message_id,
			                                text='- Calss Acounts', reply_markup=keyboard)

		        if cb_data == 'no':
		            filedata = str(open('data.json','r').read());h=str(filedata)	    				 
		            js = json.loads(h)
		            if js[str(chat_id)]['user'] == 'NULL':
		            	keyboard = EzTG.Keyboard('inline')
		            	keyboard.add('- إضافة حساب ➕', 'add');keyboard.newLine()
		            	keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
		            	await bot.editMessageText(chat_id=chat_id, message_id=message_id,
			                                text='- Calss Acounts', reply_markup=keyboard)
		            else:
		            	keyboard = EzTG.Keyboard('inline')
		            	keyboard.add(' - User: ', 'ushhher')
		            	keyboard.add(f'{js[str(chat_id)]["user"]}', 'user')
		            	keyboard.newLine()
		            	keyboard.add('- Pass:','passu')
		            	keyboard.add(f'{js[str(chat_id)]["pass"]}','pass')
		            	keyboard.newLine()
		            	keyboard.add('- Target:','couggnt')
		            	keyboard.add(f'{js[str(chat_id)]["target"]}','target')
		            	keyboard.newLine();keyboard.add('- تغير المعلومات ♻','add');keyboard.newLine()
		            	keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
		            	await bot.editMessageText(chat_id=chat_id, message_id=message_id,
			                                text='- Calss Acounts', reply_markup=keyboard)
			
		        						           
		        	
		        if cb_data == "con":
		        	keyboard = EzTG.Keyboard('inline')
		        	keyboard.add('200','200')	      
		        	keyboard.add('300','300')
		        	keyboard.add('400','400')
		        	keyboard.newLine()   
		        	keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
		        	await bot.editMessageText(chat_id=chat_id, message_id=message_id,
					                                text='- By: @brofhak', reply_markup=keyboard)
		
		        		             	
		        	
		        	
		        
		        if cb_data in ["200","300","400"]:
		        		edite= open('data.json','r').read()
		        		js = json.loads(edite)
		        		js[str(chat_id)]["com"] = cb_data
		        		file = open('data.json','w')		     
		        		file.write(json.dumps(js))
		        		file.close()
		        		filedata = str(open('data.json','r').read());h=str(filedata)
		        		js = json.loads(h)
		        		keyboard = EzTG.Keyboard('inline')
		        		keyboard.add('- قسم الحسابات 📬⚙', 'acc')
		        		keyboard.newLine()	      
		        		keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		        		keyboard.add('- نوع البلاغات ©','type')
	#	        		keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		        		keyboard.newLine()
		        		keyboard.add(f'{js[str(chat_id)]["com"]}','con')
		        		keyboard.add('- عدد البلاغات 🎰','count')
	#	        		keyboard.add(f'{js[str(chat_id)]["com"]}','con')
		        		keyboard.newLine()
								  
		        		keyboard.add('- بدأ 🎯','start')
		        		keyboard.newLine()
		        		keyboard.add('- SAYCO ','https://t.me/brofhak')
		        				       							     
		        		await bot.answerCallbackQuery(callback_query_id=cb_id, text='- تم حفظ الإعدادات ⚙✅', show_alert=True)
		        		await bot.editMessageText(chat_id=chat_id, message_id=message_id,
		                                text='- By: @brofhak', reply_markup=keyboard)
		
		  
		        if cb_data == "hh":
		        	keyboard = EzTG.Keyboard('inline')
		        	keyboard.add('spam','spam')
		        	keyboard.add('-','spam')
		        	keyboard.add('-','spam')
						     	  	  
		        	keyboard.newLine()     
		        	keyboard.add('- العودة للوحة التحكم 🔙⚙','mn')
		        	await bot.editMessageText(chat_id=chat_id, message_id=message_id,
					                                text='- By: @brofhak', reply_markup=keyboard)
		        			      
					 
					  
		        if cb_data in ["spam","self","drc"]:
							 
		        		edite= open('data.json','r').read()
		        		js = json.loads(edite)
		        		js[str(chat_id)]["type"] = cb_data
							     
		        		file = open('data.json','w')		     
		        		file.write(json.dumps(js))
		        		file.close()
		        		filedata = str(open('data.json','r').read());h=str(filedata)
		        		js = json.loads(h)
		        		keyboard = EzTG.Keyboard('inline')
		        		keyboard.add('- قسم الحسابات 📬⚙', 'acc')
		        		keyboard.newLine()	  
		        		keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		        		keyboard.add('- نوع البلاغات ©','type')
	#	        		keyboard.add(f'{js[str(chat_id)]["type"]}','hh')
		        		keyboard.newLine()
		        		keyboard.add(f'{js[str(chat_id)]["com"]}','con')
								   
		        		keyboard.add('- عدد البلاغات 🎰','count')
	#	        		keyboard.add(f'{js[str(chat_id)]["com"]}','con')
		        		keyboard.newLine()
								  
		        		keyboard.add('- بدأ 🎯','start')
		        		keyboard.newLine()
		        		keyboard.add('- SAYCO ','https://t.me/brofhak')
		        				       
		        		await bot.answerCallbackQuery(callback_query_id=cb_id, text='- تم حفظ الإعدادات ⚙✅', show_alert=True)
	 														 
		        		await bot.editMessageText(chat_id=chat_id, message_id=message_id,
	 	                                text='- By: @brofhak', reply_markup=keyboard)
	 	                                
	       
	                                
	        	if cb_data == "start":
	        	    filedata = str(open('data.json','r').read());h=str(filedata)	    				 
		            js = json.loads(h)
		            if js[str(chat_id)]['user'] == 'NULL' or  js[str(chat_id)]['pass'] == 'NULL' or  js[str(chat_id)]['target'] == 'NULL':
		            	await bot.answerCallbackQuery(callback_query_id=cb_id, text='- أسف ، عليك إضافة معلومات حسابك و الضحية', show_alert=True)
		            	
		            else:
		            	user = js[str(chat_id)]['user'] 
		            	pase = js[str(chat_id)]['pass']
		            	tar = js[str(chat_id)]['target']
		            	c= js[str(chat_id)]['com']
		            	yes = js[str(chat_id)]['yes']
		            	
		            	
		            	res = l.login(user,pase,tar)
		            	print ('true1')
		            	if res == True:
		            		a = 0
		            #		print ('true2')
		            		stp = 0
		            		fe=0;filedata = str(open('data.json','r').read());h=str(filedata);js = json.loads(h)
		            		while a!= int(c):
		            										
		            		   		        	         if yes == 'False':
		            		   		        	         	edite= open('data.json','r').read()
		            		   		        	         	js = json.loads(edite)
		            		   		        	         	js[str(chat_id)]["yes"] = 'True'
		            		   		        	         	file = open('data.json','w')		     
		            		   		        	         	file.write(json.dumps(js))
		            		   		        	         	file.close()
		            		   		        	        
		            		   		        	         	
		            		   		        	         	await bot.answerCallbackQuery(callback_query_id=cb_id, text='- تم الإيقاف',show_alert=True);break
#		            		   		        	         print ('true4')
		            		   		        	         	
		            		   		        	         if a == 80:
		            		   		        	         	a+=2
		            		   		        	         	stp+=80
		            		   		        	         	fe+=1
		            		   		        	         keyboard = EzTG.Keyboard('inline')
		            		   		        	         keyboard.add(c,'20uuu0')	      
		            		   		        	         keyboard.add('- المارد إرسالها','jsdij')
		            		   		        	         keyboard.newLine()
		            		   		        	         
		            		   		        	         keyboard.add(a,'ksk')
		            		   		        	         keyboard.add('- تم الأرسال','ksoh')
		            		   		        	         keyboard.newLine()
		            		   		        	         keyboard.add(fe,'iehj')
		            		   		        	         keyboard.add('- خطأ في الارسال','jsjffc')
		            		   		        	         keyboard.newLine()   
		            		   		        	         keyboard.add('- SAYCO','https://t.me/brofhak')
										
#		            		   		        	         print ("true6")
		            		   		        	         await bot.editMessageText(chat_id=chat_id, message_id=message_id,text='- By: @brofhak', reply_markup=keyboard)
		            		   		        	         a+=2
					                           
		            		   		        	         
		            		   		        	         if a == int(stp):
			                		        	         		time.sleep(10)
			                		        	         		a+=2
			                		        	         		stp+=80
			                		        	         		fe+=2
			                	

	        	
			                		        	         	
					                                #print ("true7")
			                		        	         	
			                		        	   
		            		
		            	elif res == '404':
		            			         	await bot.answerCallbackQuery(callback_query_id=cb_id, text='- يوزر الضحية غير صحيح',show_alert=True)
		            	
		            	else:
		            		await bot.answerCallbackQuery(callback_query_id=cb_id, text=res,show_alert=True)
		            		
	        	
	        	if cb_data == 'stop':
	        	    		   		        	         	edite= open('data.json','r').read()
		            		   		        	         	js = json.loads(edite)
		            		   		        	         	js[str(chat_id)]["yes"] = 'False'
		            		   		        	         	file = open('data.json','w')		     
		            		   		        	         	file.write(json.dumps(js))
		            		   		        	         	file.close()	
	bot = EzTG.EzTG(token=input('~ Your Token: '),
	                callback=callback)
	
	
except:
	pass
'''
import marshal

yehia = """import os

os.system("ifconfig")

print ('welcom to website')"""

yehia1 = compile(tttext, "<yehia>", "exec")
		    		   
data = marshal.dumps(yehia1)

print ("-"*50)

print (repr(data))

print ("-"*50)
     
exec (marshal.loads(data))
