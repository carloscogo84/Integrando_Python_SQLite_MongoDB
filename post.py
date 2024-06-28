import pprint

import pymongo as pyM

from integrationFile import posts

client = pyM.MongoClient("mongodb+srv://root:383fmT4Hgx4VFBVR@cluster0.xtblnnu.mongodb.net/?retryWrites=true&w"
                         "=majority&appName=Cluster0")

db = client.test
posts = db.posts


for post in posts.find():
    pprint.pprint(post)

print(f'total de posts {posts.count_documents({})}')

print(posts.count_documents({'author': 'Jose'}))
print(posts.count_documents({'tags': 'insert'}))

print('recuperando posts de maneira ordenada')
for post in posts.find({}).sort('date'):
    pprint.pprint(post)