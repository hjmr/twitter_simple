import os

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
    print("API_KEY = {}".format(API_KEY))
    print("API_SECRET_KEY = {}".format(API_SECRET_KEY))
    print("ACCESS_TOKEN = {}".format(ACCESS_TOKEN))
    print("ACCESS_TOKEN_SECRET = {}".format(ACCESS_TOKEN_SECRET))
