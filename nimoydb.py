import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = conn.['Nimoy'] #http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/
brain = db.brain

def learn(trigger, response): #add association
  data = {}
  data['trigger'] = trigger
  data['response'] = response #find way to add new responses
  brain.insert(data)
