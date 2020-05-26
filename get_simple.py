from TwitterAPI import TwitterAPI
import config

api = TwitterAPI(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

res = api.request('tweets/search/30day/:research', {'query': 'ねこ'})

for item in res.get_iterator():
    print(item['id'], item['user']['screen_name'], item['user']['id'], item['text'])
