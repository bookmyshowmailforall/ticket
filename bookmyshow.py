from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import requests,json
def send_mail(subject,body,to):
	msg=EmailMessage()
	msg.set_content(body)
	msg["subject"]=subject
	msg["to"]=to
	user="bookmyshowmailforall@gmail.com"
	msg["from"]="Ticket Script"+movie
	password="oljyrbbfhuzbiehp"
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(user,password)
	server.send_message(msg)
	server.quit()
url="https://in.bookmyshow.com/pondicherry/movies/beast/ET00311733"
movie=url[45:url.rindex("/")].upper()
head={'User-Agent':'PostmanRuntime/7.28.2','Accept':'*/*','Connection':'keep-alive'}
content=requests.get(url,headers=head)
#,"chris.thompson@zohocorp.com"
user_list=["hariharan.dass@zohocorp.com"]
flag=False
for i in content:
	if("Book tickets" in str(i)):
		print(" Booking are OPEN !!! ")
		flag=True
		break
if(flag==True):
	for user in user_list:
		send_mail(movie,"Booking is open for "+movie,user)
else:
	print("Booking is not opened")
	
	
