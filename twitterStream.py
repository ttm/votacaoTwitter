#-*- coding: utf8 -*-
import pymongo, time as T, sys
from twython import TwythonStreamer
from twython import Twython
HTAG="#cibervoto" # tag para configuracao
HTAG_=HTAG.replace("#","NEW")

from maccess import tw
TWITTER_API_KEY             = tw.tak
TWITTER_API_KEY_SECRET      = tw.taks
TWITTER_ACCESS_TOKEN        = tw.tat
TWITTER_ACCESS_TOKEN_SECRET = tw.tats

t = Twython(app_key=TWITTER_API_KEY, 
            app_secret=TWITTER_API_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

from maccess import mdc as U
U=U.u1
client=pymongo.MongoClient(U)
db = client[U.split("/")[-1]]
C = db[HTAG_] #collection

##### Continuar aqui p streaming
# ativar interface de streaming
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                C.insert(data)            
            except:
                client=pymongo.MongoClient(U)
                db = client[U.split("/")[-1]]
                C = db[HTAG_] #collection
                C.insert(data)            
            print data['user']["screen_name"].encode('utf-8'),data['text'].encode('utf-8'),data["created_at"]
    def on_error(self, status_code, data):
        print status_code

print "iniciando streaming"
stream=MyStreamer(tw.tak,tw.taks,tw.tat,tw.tats)
stream.statuses.filter(track=HTAG)

sys.exit()
    
tweets=[ff for ff in foo]
print 1


#since_id
#search = t.search(q='#arenaNETmundial', count=150,since_id="444663164026638336")
#search = t.search(q='#arenaNETmundial', max_id="445939520354406401",result_type="mixed")
#search = t.search(q='#arenaNETmundial', max_id="446756730140385280",result_type="recent")
#search = t.search(q='#arenaNETmundial', since_id="444663164026638336",max_id="445564745635348480",result_type="recent",count=150)
#
while 1:
    search = t.search(q='#arenaNETmundial',count=150,max_id=tweets[-1]['id']-1)
    i=0
    while len(search['statuses'])>0:
        tweets +=search['statuses']
        #search = t.search(q='#arenaNETmundial', count=150, max_id=tweets[-1]['id']-1)
        print "older", i, len(tweets),search['statuses']; i+=1

    search2 = t.search(q='#arenaNETmundial',count=150,since_id=tweets[0]['id'])
    i=0
    while len(search2['statuses'])>0:
        tweets =search2['statuses']+tweets
        #search = t.search(q='#arenaNETmundial', count=150, since_id=tweets[0]['id'])
        print "newer", i, len(tweets),search2['statuses']; i+=1

    #db.twitter.remove()
    if search['statuses'] or search2['statuses']:
        print "tweets"
        db.sna.remove()
        #C = db['twitter'] #collection
        #C.insert({"arenaNETmundial":tweets})
        db.sna.insert((i for i in tweets))
        #db2.sna.insert((i for i in db.sna.find()))
    print("atualizado")
    T.sleep(60*60) # atualizar BD de 2 em 2 minutos

stream=Twython.TwythonStreamer(tw.tak,tw.taks,tw.tat,tw.tats)
stream.statuses.filter(track=HTAG)
