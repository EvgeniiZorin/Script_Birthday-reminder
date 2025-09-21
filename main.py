from utils.connections import (
	query_db,
	send_email
)

### Module 1. Get Birthdays
if __name__ == '__main__':
	# Queries
	# Query birthdays that happened on this day and month
	df1 = query_db('sql/query_birthdays_current_month_day.sql')
	# Convert it into the markdown format
	df1_markdown = (
		df1
		[['name', 'date', 'type_of_event', 'anniversary_years']]
		.to_markdown(index = False)
	)
	# Query the next 3 birthdays
	df2 = query_db('sql/query_next_3_birthdays.sql')
	# Convert it into the markdown format
	df2_markdown = (
		df2 
		[['name', 'date', 'type_of_event', 'anniversary_years']]
		.to_markdown(index = False)
	)
	# Send an email
	message = \
	f"""
# Hello Evgenii! 👋

These are the birthdays that happened on this day and month:

{df1_markdown}

Additionally, these are the next 3 events to celebrate in the near future:

{df2_markdown}

<br><br>

You can see the code on the [Github page](https://github.com/EvgeniiZorin/Script_Birthday-reminder).
"""
	if len(df1) > 0:
		send_email(message)
