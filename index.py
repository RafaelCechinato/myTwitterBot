import tweepy
import time

print("Ate aqui tudo bem kkkkk")

CONSUMER_KEY = 'SfwKkcyFnR1jjTJG4yQnif2MJ'
COMSUMER_SECRET = '4Q7LhNYVktcf4gBY8OucqxKspX7sOXpBLKfSPIL8GaX8aKo5AA'
ACCESS_KEY = '1360686991743008772-ZZkBOThmp21Pd17k5c5ZcqzvwJdwWI'
ACCESS_SECRET = 'U4FnxO7htOnwIGiIBRFYmrLH6uigWXpvrGgzgnwDxoG2I'

auth = tweepy.OAuthHandler(CONSUMER_KEY,COMSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def searchTweets():
    print("searching")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.search_30_day(environment_name="dev",query="Land of the Lustrous")

    for mention in reversed(mentions):
        if 'date' in mention.text.lower():
            if not mention.id == last_seen_id:
                last_seen_id = mention.id
                store_last_seen_id(last_seen_id,FILE_NAME)
                myId = api.get_user(screen_name="@rafael_crespim")
                api.send_direct_message(recipient_id=myId.id,text="@"+mention.user.screen_name+" - "+mention.text)

while True:
    searchTweets()
    time.sleep(15)


