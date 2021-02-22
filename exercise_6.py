"""
Γράψτε ένα κώδικα σε Python ο οποίος συνδέεται στο twitter (χρησιμοποιείστε το tweepy)
και επιλέξτε τα 10 τελευταία tweets του χρήστη που θα σας δηλώσει ο χρήστης.
Εμφανίστε τις 5 μεγαλύτερες λέξεις και τις 5 μικρότερες λέξεις του.

"""
import tweepy

# Twitter API keys
API_KEY  = "hTs5lBFE5B81mKRHma42WPpOE"
API_SECRET_KEY  = "0b3m2sHkBfFp3JRwf0om8sovJBUneVnrHX6SNHqbiK9p8zlN0P"
ACCESS_TOKEN = "1341066897866055681-PeIyczJIh465DCQstGcNoeWGdXDeeS"
ACCESS_TOKEN_SECRET = "GuEtonI8Oiw2f9ZF7mbZ9yDt5i9iTnBRwEPNg1UBIn2Rb"

# Initialize tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Enter username
username = input("Enter username: ")

# Get 10 latest tweets of user, excluding retweets and replies
tweets = tweepy.Cursor(api.user_timeline, screen_name=username, count=None, include_rts = False, exclude_replies=True, tweet_mode = 'extended').items(10)

# Get text of the tweets
words = ""

for tweet in tweets:
    words += tweet.full_text

# Seperate each word and list them
word_list = sorted(set(words.split(' ')), key=len)
# Sort the words by length
word_list = [word.replace('\n', '') for word in word_list]

# Get 5 shortest and 5 longest words
max_words = word_list[-5:]
min_words = word_list[:5]

# Print results
print("\nLongest words:")
for word in max_words:
    print(word)

print("\nShortest words:")
for word in min_words:
    print(word)