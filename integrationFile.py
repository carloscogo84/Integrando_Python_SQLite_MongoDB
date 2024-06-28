import pymongo as pyM
import pprint
from datetime import datetime

client = pyM.MongoClient("mongodb+srv://root:383fmT4Hgx4VFBVR@cluster0.xtblnnu.mongodb.net/?retryWrites=true&w"
                         "=majority&appName=Cluster0")

#criando collection
db = client.test
collection = db.test_collection
print(db.test_collection)

# definição para compor o doc
post = {
    "author": "Pedro",
    "text": "My firts mongdb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.utcnow()
}

# preparando para submeter a infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# bulk inserts
new_posts = [{
    'author': 'Pedro',
    'text': 'Outro post',
    'tags': ['bulk', 'insert', 'insert'],
    'date': datetime.utcnow()
    },
    {
    'author': 'Mateus',
    'text': 'Post do Mateus',
    'tittle': 'Mongo is fun',
    'date': datetime(2020, 5, 13, 16, 17)
    }
]
result = posts.insert_many(new_posts)
print(result.inserted_ids)

for post in posts.find():
    pprint.pprint(post)
    print('----')



