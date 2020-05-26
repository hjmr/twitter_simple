from TwitterAPI import TwitterAPI
import twitter_tokens as tokens

api = TwitterAPI(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, tokens.ACCESS_KYE, tokens.ACCESS_SECRET)

res = api.request('tweets/search/30day/:research', {'query': 'ねこ'})
rj = res.json()

next_id = ''
if 'next' in rj:
    next_id = rj['next']

for item in r.get_iterator():
    print(item['id'], item['user']['screen_name'], item['user']['id'], item['text'])
print("next:{}".format(next_id))
