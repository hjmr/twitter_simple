def show_tweets(tweets):
    for t in tweets:
        print("------------------------------------")
        print("tweet id: {}".format(t['id']))
        print("screen_name: {}".format(t['user']['screen_name']))
        print("user id: {}".format(t['user']['id']))
        print("retweeted count: {}".format(t['retweet_count']))
        if "retweeted_status" in t:
            print("retweet: True")
        else:
            print("retweet: False")
        print(t['text'])
