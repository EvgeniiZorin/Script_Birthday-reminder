/* Select the next 3 events
that have anniversaries, 
not counting today's event
*/
SELECT
    name,
    date,
    type_of_event,
    type,
    EXTRACT(
        YEAR FROM
        AGE(NOW(), date)
    ) AS anniversary_years
FROM notable_dates
WHERE
	CASE
		WHEN EXTRACT(MONTH FROM date) = EXTRACT(MONTH FROM NOW()) 
		THEN (EXTRACT(DAY FROM date) > EXTRACT(DAY FROM NOW() ) )
		ELSE ( EXTRACT(MONTH FROM date) > EXTRACT(MONTH FROM NOW() ) )
	END
ORDER BY
    EXTRACT(MONTH FROM date) ASC,
    EXTRACT(DAY FROM date) ASC
LIMIT 3
