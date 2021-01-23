import amino
import random
import time
client=amino.Client()

email=input("Email: ")
password=input("Password: ")

client.login(email=email ,password=password)
print ("Done Loggining")

chatlink=input("Chat Link")

chatinfo=client.get_from_code(chatlink)
chatId=chatinfo.objectId
comId=chatinfo.path[1:chatinfo.path.index('/')]
subclient=amino.SubClient(comId=comId, profile=client.profile)

#subclient.send_message(chatId=chatId, message="تم التفعيل", messageType=0)

def getmess():
	messages=subclient.get_chat_messages(chatId=chatId, size=25, pageToken=None)
	contents=messages.content
	messagesId=messages.messageId
	messagename=messages.author.nickname
	for content in contents:
		for messageN in messagename:
			for messageId in messagesId:
				print ("MesssageId = ",messageId,":",messageN,":",content)
				def on_group_member_join(self,data):
								        f=data.message.author.nickname
								        subclient.send_message(chatId=chatId, message=f,messageType=0, replyTo=messageId)
				if content == "خرا":
				    subclient.send_message(chatId=chatId, message="الزم لسانك",messageType=0, replyTo=messageId)
				    try:
				        subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
				    except:
				        pass
				        getmess()
				    getmess()
				elif content=="كل خرا":
				       subclient.send_message(chatId=chatId, message="الزم لسانك",messageType=0, replyTo=messageId)
				       try:
				           subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
				       except:
				           pass
				           getmess()
				       getmess()
				elif content == "زق":
				    subclient.send_message(chatId=chatId, message="الزم لسانك",messageType=0, replyTo=messageId)
				    try:
				        subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
				    except:
				        pass
				        getmess()
				    getmess()
				elif content == "كل زق":
				    subclient.send_message(chatId=chatId, message="الزم لسانك",messageType=0, replyTo=messageId)
				    try:
				        subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
				    except:
				        pass
				        getmess()
				    getmess()
				elif content == "يا حمار":
				    subclient.send_message(chatId=chatId, message="الزم لسانك",messageType=0, replyTo=messageId)
				    try:
				        subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
				    except:
				        pass
				        getmess()
				    getmess()
				elif content == "حمار":
				    subclient.send_message(chatId=chatId, message="الزم لسانك",messageType=0, replyTo=messageId)
				    try:
				        subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
				    except:
				        pass
				        getmess()
				    getmess()
				
				
				def mvirus():
				          try:
				              if len(content) > 2000:
				                  subclient.send_message(chatId=chatId, message="ممنوع ارسال الفيروسات", messageType=0, replyTo=messageId)
				                  
				                  subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
				                  getmess()
				          except:
				              pass
				              getmess()
				mvirus()
				if content == "السلام عليكم":
					subclient.send_message(chatId=chatId, message="وعليكم السلام " +messageN,messageType=0, replyTo=messageId)
					getmess()
				if content == "كلب":
					message="الزم لسانك"
					subclient.send_message(chatId=chatId, message=message, messageType=0,replyTo=messageId)
					try:
					    subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
					except:
					    pass
					    getmess()
					getmess()
				if content == "هلا":
					message="هلا والله"
					subclient.send_message(chatId=chatId, message=message, messageType=0,replyTo=messageId)
					getmess()
				if content == "/لعبة/1/حجرة" :
						subclient.send_message(chatId=chatId, message="حجرة ورقة مقص", messageType=0)
						rpc=('حجرة','ورقة','مقص')
						rpcr=random.choice(rpc)
						subclient.send_message(chatId=chatId, message=rpcr, messageType=0,replyTo=messageId)
						getmess()
				elif content == "/لعبة/1/ورقة":
						subclient.send_message(chatId=chatId, message="حجرة ورقة مقص", messageType=0)
						rpc=('حجرة','ورقة','مقص')
						rpcr=random.choice(rpc)
						subclient.send_message(chatId=chatId, message=rpcr, messageType=0 ,replyTo=messageId)
						getmess()
				elif content == "/لعبة/1/مقص":
						subclient.send_message(chatId=chatId, message="حجرة ورقة مقص", messageType=0)
						rpc=('حجرة','ورقة','مقص')
						rpcr=random.choice(rpc)
						subclient.send_message(chatId=chatId, message=rpcr, messageType=0, replyTo=messageId)
						getmess()
				elif content == "/لعبة/1":
						subclient.send_message(chatId=chatId, message="حجرة ورقة مقص", messageType=0)
						getmess()
				if content == "يا كلب":
						    subclient.send_message(chatId=chatId, message="الزم لسانك", messageType=0,replyTo=messageId)
						    try:
						        subclient.delete_message(chatId=chatId, messageId=messageId, asStaff=False, reason=None)
						    except:
						        pass
						        getmess()
						    getmess()
				if content == "/لعبة/2":
				    subclient.send_message(chatId=chatId, message="تخمين", messageType=0)
				    getmess()
				if content == "اخرجني":
				    messageinfo=subclient.get_message_info(chatId=chatId, messageId=messageId)
				    userId=messageinfo.author.userId
				    try:
				        subclient.kick(userId=userId, chatId=chatId, allowRejoin=True)
				        subclient.send_message(chatId=chatId, message="الله وياك", messageType=0, replyTo=messageId)
				        getmess()
				    except:
				        pass
				        subclient.send_message(chatId=chatId, message="الخدمة غير متوفرة", messageType=0, replyTo=messageId)
				        getmess()
				if content == "معلوماتي":
				      messageinfo=subclient.get_message_info(chatId=chatId, messageId=messageId)
				      userId=messageinfo.author.userId
				      userinfo=subclient.get_user_info(userId=userId)
				      usercon=userinfo.content
				      userinfoo1="اسمك: "+messageN
				      userinfoo2=usercon
				      userinfoo3="Id خاصتك: "+userId
				      subclient.send_message(chatId=chatId, message=userinfoo1, messageType=0, replyTo=messageId)
				      try:
				          subclient.send_message(chatId=chatId, message="وصفك: "+userinfoo2, messageType=0, replyTo=messageId)
				      except:
				           pass
				      subclient.send_message(chatId=chatId, message=userinfoo3, messageType=0, replyTo=messageId)
				      subclient.send_message(chatId=chatId, message="متابعينك: "+followc, messageType=0, replyTo=messageId)
				      getmess()
				elif content ==  "/معلوماتي/id":
				    messageinfo=subclient.get_message_info(chatId=chatId, messageId=messageId)
				    userId=messageinfo.author.userId
				    subclient.send_message(chatId=chatId, message=userId, messageType=0, replyTo=messageId)
				    getmess()
				elif content == "/معلوماتي/اسمي":
				    subclient.send_message(chatId=chatId, message=messageN, messageType=0, replyTo=messageId)
				    getmess()
				 
				elif content=="/معلوماتي/متابعيني":
				     messageinfoo=subclient.get_message_info(chatId=chatId, messageId=messageId)
				     userId=messageinfoo.author.userId=""
				     userinfoo=subclient.get_user_info(userId=userId)
				     userf=userinfoo.followers.userId
				     f=0
				     for follow in userf:
				         f += 1
				     myf=str(f)
				     subclient.send_message(chatId=chatId, message=myf, messageType=0, replyTo=messageId)
				     getmess()
				 
				elif content == "/معلوماتي/id_الرسالة":
			 	    subclient.send_message(chatId=chatId, message=messageId, messageType=0, replyTo=messageId)
			 	    getmess()
			     
			      
		getmess()
getmess()

#delete_message(chatId: str, messageId: str, asStaff: bool = False, reason: str = None)
# get_chat_messages(chatId: str, size: int = 25, pageToken: str = None)
#get_chat_thread(chatId: str)
#get_user_info(userId: str)
# get_message_info(chatId: str, messageId: str)
# kick(userId: str, chatId: str, allowRejoin: bool = True)
# on_chat_invite(data)
# on_group_member_join(data)
# on_group_member_leave(data)
# on_text_message(data)
#send_message(chatId: str, message: str = None, messageType: int = 0, file: BinaryIO = None, fileType: str = None, replyTo: str = None, mentionUserIds: list = None, stickerId: str = None, embedId: str = None, embedType: int = None, embedLink: str = None, embedTitle: str = None, embedContent: str = None, embedImage: BinaryIO = None)
