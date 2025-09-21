"""Contains code for connecting and querying PostgreSQL database.
"""
import os
import sys

import pandas as pd
import psycopg2 
import psycopg2.extras
import smtplib 
from email.message import EmailMessage 
import markdown

sys.path.append(os.path.abspath('..'))
import mySecrets

def query_db(query_path: str
             ) -> pd.DataFrame:
    """
    Returns a Pandas DataFrame based on passed query.
    """
    conn = None
    # Initialise objects with context manager
    try:
        with psycopg2.connect(mySecrets.psqlKey) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
                # Run SQL query
                with open(query_path, 'r') as f:
                    sql_query = f.read()
                # Execute SQL query
                cur.execute(sql_query)
                # Format output to Pandas DataFrame
                rows = cur.fetchall()
                column_names = [i[0] for i in cur.description]
                df = pd.DataFrame(rows, columns = column_names)
    except Exception as e:
        print(e)
        return None
    finally:
        if conn is not None:
            conn.close()
    return df


def send_email(inputMessage: str) -> None:
	"""
	Send an email with text of inputMessage formatted in Markdown.
	"""
	# Connect to email
	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
		# Login using secret credentials
		server.login(mySecrets.gmailEmail, mySecrets.gmailKey) # The password is from 'myaccount.google.com/apppasswords' - App Passwords
		# Write up message components
		# msg = MIMEMultipart('alternative')
		msg = EmailMessage()
		msg['Subject'] = f'Birthdays today'
		msg['From'] = mySecrets.gmailEmail
		msg['To'] = mySecrets.gmailEmail
		# Plain text fallback
		msg.set_content('Hello, this is the plain text version.')
		# Attach also html version, if it renders
		html_content = markdown.markdown(inputMessage, extensions = ['extra', 'sane_lists'])
		# center the text
		msg.add_alternative(html_content, subtype='html')
		# Send the message
		server.send_message(msg)
		server.quit()
	return None


