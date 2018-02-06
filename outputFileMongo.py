from pymongo import MongoClient
import datetime
import pprint

timeseries = [[20,21,22,23],[20,21,22,23], [40,50,60,70], [10010,10020,10030,10040]]

#np.savetxt('timeseries.txt', timeseries)
def outputToFile(file):
    text_file = open("timeseries.txt", "a")
    for x in range(len(timeseries)):
        for y in range(len(timeseries[0])):
            text_file.write("%s " % timeseries[x][y])
        text_file.write("\n")
    text_file.close()

#outputToFile("timeseries.txt")
client = MongoClient()
#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
#db = client['test-database']
collection = db.test_collection
#collection = db['test-collection']
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow}
post2 = {"temperatura": "10",
        "pressione": "1001",
        "umidita": "50"}
post3 = {"temperatura": "dieci",
        "pressione": "mille",
        "umidita": "cinquanta"}
posts = db.posts
#inserisci elemento nel db
#post_id = posts.insert_one(post).inserted_id
post_id = posts.insert_one(post2).inserted_id
#post_id
#db.collection_names(include_system_collections=False)
#pprint.pprint(posts.find_one({"temperatura": "10"}))
#dbs = MongoClient().database_names()
#print(dbs)
cursor = collection.find({})
for document in cursor:
    pprint(document)
