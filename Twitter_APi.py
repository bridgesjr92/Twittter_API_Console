import tweepy
import Information

client = tweepy.Client(bearer_token=Information.BEARER_TOKEN,
                       access_token=Information.Access_Token,
                       access_token_secret=Information.Access_Token_Secret,
                       consumer_key=Information.API_Key,
                       consumer_secret=Information.API_Key_Secret
                       )




