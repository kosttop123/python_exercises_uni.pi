"""
7. Χρησιμοποιήστε το API του ΟΠΑΠ (https://www.opap.gr/web-services) από την Python 
για να βρείτε τον αριθμό που εμφανίζεται συχνότερα στο ΚΙΝΟ κάθε μέρα του τρέχοντα μήνα.

"""
from statistics import mode
import requests

game_id = "1100"

# Get data from 1st of December to 20th of December
for i in range(1, 21):
    date = f'2020-12-0{i}' if i in range(10) else f'2020-12-{i}'

    numbers = []
    

    # Get all wining numbers of the day
    url = f"https://api.opap.gr/draws/v3.0/{game_id}/draw-date/{date}/{date}"
    response = requests.get(url).json()

    for draw in response['content']:
        numbers += draw['winningNumbers']['list']

    # Get most frequent number of current date
    print(f"Most frequent number on {date}: {mode(numbers)}")