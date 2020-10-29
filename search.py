import json
import argparse
import time
from pprint import pprint

from TwitterAPI import TwitterAPI
import config
import utils


API = 'tweets/search/30day/:{}'.format(config.DEV_ENV_LABEL)
api = TwitterAPI(config.API_KEY, config.API_SECRET_KEY, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)


def parse_arg():
    args = argparse.ArgumentParser(description="search tweets by query.")
    args.add_argument("-f", "--filename", type=str, help="specify output JSON filename.")
    args.add_argument("-q", "--query", type=str, help="specify query keyword.")
    args.add_argument("-c", "--count", type=int, default=200, help="the number of tweets to retrieve.")
    args.add_argument("--min_retweet", type=int, help="collect tweets retweeted at least specified number of times.")
    args.add_argument("--min_quote", type=int, help="collect tweets quoted at least specified number of times.")
    args.add_argument("--min_reply", type=int, help="collect tweets replied at least specified number of times.")
    return args.parse_args()


def search_tweets(query, count=200):
    tweets = []
    next_id = None

    while(len(tweets) < count):
        c = max(min(count - len(tweets), 100), 10)  # maxResults must be between 10 and 100
        params = {
            'query': query,
            'maxResults': c
        }
        if next_id is not None:
            params["next"] = next_id

        res = api.request(API, params=params)
        if res.status_code == 429:  # 時間内の取得数リミットに引っかかった場合
            secs_to_wait = int(res.headers["X-Rate-Limit-Reset"])
            print("Exceed rate limit.")
            print("Waiting for rate limit reset: {} secs.".format(secs_to_wait))
            time.sleep(secs_to_wait)
            continue
        elif res.status_code != 200:  # それ以外の理由で正常終了出来なかった場合
            print("Error with code: %d" % res.status_code)
            pprint(res.json())
            break
        else:
            rj = res.json()
            next_id = rj["next"]
            for tweet in rj["results"]:
                tweets.append(tweet)
            print("Got {} tweets. Total {} tweets.".format(len(rj["results"]), len(tweets)))
            print("Possible API calls: {}".format(res.headers["X-Rate-Limit-Remaining"]))
    return tweets


def filter_by_min_retweet(tweets, min_retweet):
    tweets_filtered = []
    for t in tweets:
        if min_retweet <= t["retweet_count"]:
            tweets_filtered.append(t)
    return tweets_filtered


def filter_by_min_quote(tweets, min_quote):
    tweets_filtered = []
    for t in tweets:
        if min_quote <= t["quote_count"]:
            tweets_filtered.append(t)
    return tweets_filtered


def filter_by_min_reply(tweets, min_reply):
    tweets_filtered = []
    for t in tweets:
        if min_reply <= t["reply_count"]:
            tweets_filtered.append(t)
    return tweets_filtered


if __name__ == '__main__':
    args = parse_arg()
    if args.query:
        tweets = search_tweets(args.query, args.count)
        if args.min_retweet:
            tweets = filter_by_min_retweet(tweets, args.min_retweet)
        if args.min_quote:
            tweets = filter_by_min_quote(tweets, args.min_quote)
        if args.min_reply:
            tweets = filter_by_min_reply(tweets, args.min_reply)
        if args.filename:
            with open(args.filename, "w+") as f:
                json.dump(tweets, f, indent=2, ensure_ascii=False)
        else:
            utils.show_tweets(tweets)
