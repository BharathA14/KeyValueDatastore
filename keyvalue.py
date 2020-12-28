import pymongo
import sys
class CRD:
    def __init__(self,dataBase,collection):
        self.client = pymongo.MongoClient()
        self.dataBase = self.client[dataBase]
        self.collection= self.dataBase[collection] 

    def insert(self,key,value,ttl=None):
        
        if (len(str(key))>32):
            print("The maximum key length is 32.")
            return False
        if (sys.getsizeof(value)>16000):
            print("The value size must be less than 16KB.")
            return False
        try:
            self.collection.insert_one({"id":key,"value":value})
        except pymongo.errors.DuplicateKeyError:
            print("This Key already exists")

    def read(self,key):
        try:
            x = self.collection.find({"id":key},{"value":1})
            print(list(x)[0]['value'])
        except IndexError:
            print('No such key in database.')

    def delete(self,key):
        result = self.collection.delete_many({"id":key})
        if(result.deleted_count==0):
            print("No such element exists.")
        else:
            print("Item deleted successfully")

if __name__ =='__main__':
    test = CRD('keyValue','keyValue')
    # test.insert(5,"{'test':'success'}")
    test.delete(1)
    # test.read(6)