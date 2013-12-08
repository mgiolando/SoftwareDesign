"""
Victoria Preston
A test in using MongoDB for data share
"""

import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient()


db = client.test_database
collection = db.test_collection

post = {'author':'Victoria', 'text':'My first entry', 'tags': ['mongodb', 'python', 'pymongo'], 'date': datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert(post)


posted =  posts.find_one()
for key in posted:
    print key
    print posted[key]
    
#can also be of the syntax posts.find_one({'author': 'Victoria'}) or via object id

new_posts = [{'author': 'Victoria', 'text': 'One more post!', 'tags':['bulk', 'insert'], 'date': datetime.datetime(2013, 11, 16, 11, 42)},{'author': 'Alex', 'title': 'MongoDb is nifty!', 'text':'and pretty straightforward', 'date':datetime.datetime(2013, 11, 16, 11, 45)}]

posts.insert(new_posts)

for post in posts.find():
    for key in post:
        print key, post[key]

print posts.count()
print posts.find({'author':'Victoria'}).count()

"""A range query will look like this:

d = datetime.datetime(2013,11,16,12)
for post in posts.find({'date':{'$lt':d}}).sort('author'):
    print post

to index, write something like this:

from pymongo import ASCENDING, DESCENDING
posts.create_index([('data,DESCENDING),('author', ASCENDING)])
posts.find({'date': {'$lt':d}}).sort('uthor').explain()['cursor'] (or use 'nscanned'



posts.find({'date':{'$lt':d}}).sort('author').e


#left off at Bulk Inserts in Tutorial at http://api.mongodb.org/python/current/tutorial.html



