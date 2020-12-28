from pymongo import MongoClient
class CRD:
    def __init__(self):
        self.client = MongoClient()
        self.dataBase = client['keyValue']
        self.collection= dataBase['keyValue'] 

    def insert(key,value):
        pass
    def update(key,value):
        pass
    def delete(key):
        pass

if __name__ =='__main__':
    pass