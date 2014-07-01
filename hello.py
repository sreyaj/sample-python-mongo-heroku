import os
import flask
import urlparse
from pymongo import MongoClient

application = flask.Flask(__name__)
application.debug = True

@application.route('/')
def hello_world():
  storage = Storage()
  storage.populate(1234)
  score = storage.get_score()
  return "Hello world, %d!" % score

class Storage():
  def __init__(self):
    mongo_url = os.environ['MONGOLAB_URI']
    db_name = urlparse.urlparse(mongo_url).path[1:]
    client = MongoClient(mongo_url)
    self.db = client[db_name]
    self.scores = self.db.scores

  def populate(self, score):
    self.scores.insert({"score": score})

  def get_score(self):
    return self.scores.find_one().get("score")

if __name__ == "__main__":
  application.run(host='0.0.0.0')
