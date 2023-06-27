import psycopg2
import psycopg2.extras

import datetime

import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

import mySecrets


### Module 1. Get Birthdays

conn = None

birthdaysToday = []

try:
	with psycopg2.connect(mySecrets.psqlKey) as conn:
		with conn.cursor() as cur:
			cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
			# SQL statements
			cur.execute("SELECT * FROM notable_dates;")
			for i in cur.fetchall():
				date = i['date']
				if date.strftime("%d.%m") == datetime.date.today().strftime("%d.%m"):
				# if date == datetime.date.today():
					# print(i['name'], i['date'], i['type_of_event'])
					birthdaysToday.append([i['name'], i['date']])
			# print(birthdaysToday)
except Exception as error:
	print(error)
finally:
	if conn is not None:
		conn.close()


### Module 2. Format birthdays

birthdaysTodayOutput = ''
for i in birthdaysToday:
    date = i[1].strftime("%d.%m.%y")
    birthdaysTodayOutput += f"{date} {i[0]}\n"

### Module 3. Send email

def send_email(inputMessage):
	server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server.login(mySecrets.gmailEmail, mySecrets.gmailKey) # The password is from 'myaccount.google.com/apppasswords' - App Passwords
	msg = EmailMessage()
	message = msg.set_content(inputMessage)
	msg['Subject'] = f'Birthdays today'
	msg['From'] = mySecrets.gmailEmail
	msg['To'] = mySecrets.gmailEmail
	server.send_message(msg)
	server.quit()

message = \
f"""Hello there!

Today's birthdays:

{birthdaysTodayOutput}
"""

if birthdaysTodayOutput == '':
	pass
else:
	send_email(message)
