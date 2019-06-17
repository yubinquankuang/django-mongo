# _*_ coding: utf-8 _*_
__author__ = 'yubinquan'
__date__ = '2019/6/13 13:55'

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(host="localhost",port=27017)

databaseName = "djangodb"

db = client[databaseName]

collectionName = "col"

collection = db[collectionName]

person1 = {"name": "John Doe",
           "age": 25, "dept": 101, "languages": ["English", "German", "Japanese"]}

person2 = {"name": "Mike",
           "age": 27, "languages": ["English", "Spanish", "French"]}

result = collection.insert([person1,person2])
result = collection.find_one({"name":"Mike"})
result = collection.find_one({'_id': ObjectId('5d01e97dbacac279ab386299')})
print(result)