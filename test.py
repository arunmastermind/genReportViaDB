import pandas as pd
from pymongo import MongoClient
def getQueryData():
    client = MongoClient('mongodb://onega:27017')
    db = client.AutoRedGreen
    collection = db.QUERY
    data = pd.DataFrame(list(collection.find()))
    return data

a = getQueryData()
print(a)