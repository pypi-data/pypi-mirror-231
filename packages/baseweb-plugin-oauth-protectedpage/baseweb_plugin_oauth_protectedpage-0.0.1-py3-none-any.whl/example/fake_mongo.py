class FakeMongoCollection():
  def __init__(self):
    self.documents = [
      { "_id" : "contact@christophe.vg" }
    ]
  
  def insert_one(self, doc):
    if self.find_one({"_id" : doc["_id"]}):
      raise ValueError(f"{doc} already exists")
    self.documents.append(doc)

  def update_one(self, matching, update):
    for doc in self.documents:
      for key, value in matching.items():
        if not key in doc or doc[key] != value:
          continue
      else:
        doc.update(update["$set"])

  def find_one(self, matching):
    for doc in self.documents:
      for key, value in matching.items():
        if not key in doc or doc[key] != value:
          continue
      else:
        return doc.copy()
    return None

class FakeMongo():
  def __init__(self):
    self.collections = {}

  def __getitem__(self, collection):
    try:
      return self.collections[collection]
    except KeyError:
      self.collections[collection] = FakeMongoCollection()
    return self.collections[collection]
