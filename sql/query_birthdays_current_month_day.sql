/* This SQL query searches for birthdays 
with the month and day of the field `date`
that equal to today's values
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
    EXTRACT(MONTH FROM date) = EXTRACT(MONTH FROM NOW())
    AND EXTRACT(DAY FROM date) = EXTRACT(DAY FROM NOW())
ORDER BY
    EXTRACT(MONTH FROM date) ASC,
    EXTRACT(DAY FROM date) ASC
