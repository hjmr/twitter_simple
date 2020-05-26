import os

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
    print("CONSUMER_KEY = {}".format(CONSUMER_KEY))
    print("CONSUMER_SECRET = {}".format(CONSUMER_SECRET))
    print("ACCESS_TOKEN = {}".format(ACCESS_TOKEN))
    print("ACCESS_TOKEN_SECRET = {}".format(ACCESS_TOKEN_SECRET))
