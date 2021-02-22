"""
3. Χρησιμοποιήστε το API του ΟΠΑΠ (https://www.opap.gr/web-services) από την Python 
για να εμφανίσετε τα στατιστικά των αριθμών που κερδίζουν την πρώτη κλήρωση 
της ημέρας για το ΚΙΝΟ τον τρέχον μήνα.

"""

import requests

game_id = '1100'

numbers = []

# Get data from 1st of December to 20th of December
for i in range(1, 21):
    date = f'2020-12-0{i}' if i in range(10) else f'2020-12-{i}'

    # Get winning numbers of the first draw of the day
    url = f"https://api.opap.gr/draws/v3.0/{game_id}/draw-date/{date}/{date}"
    winning_numbers = requests.get(url).json()['content'][0]['winningNumbers']['list']
    
    numbers += winning_numbers

numbers_count = []

# Get count of each number in the list
for i in range(1, 81): # From 1 to 80
    numbers_count.append({i: numbers.count(i)})

# Sort numbers_count in desending order
numbers_count.sort(key=lambda d: sorted(list(d.values())), reverse=True)

# Print the results
for number in numbers_count:
    for num, count in number.items():
        print(f"{num} shows up {count} times")