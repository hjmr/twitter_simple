import os

DEV_ENV_LABEL = os.getenv("TWITTER_DEV_ENV")

API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
    print("Dev environment label = {}".format(DEV_ENV_LABEL))
    print("API_KEY = {}".format(API_KEY))
    print("API_KEY_SECRET = {}".format(API_KEY_SECRET))
    print("ACCESS_TOKEN = {}".format(ACCESS_TOKEN))
    print("ACCESS_TOKEN_SECRET = {}".format(ACCESS_TOKEN_SECRET))
