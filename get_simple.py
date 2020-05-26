from TwitterAPI import TwitterAPI
import config

api = TwitterAPI(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

res = api.request('tweets/search/30day/:research', {'query': 'ねこ'})
rj = res.json()

next_id = ''
if 'next' in rj:
    next_id = rj['next']

for item in r.get_iterator():
    print(item['id'], item['user']['screen_name'], item['user']['id'], item['text'])
print("next:{}".format(next_id))
