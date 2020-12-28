from pymongo import MongoClient

if __name__ =='__main__':
    client = MongoClient()
    dataBase = client['keyValue']
    collection= dataBase['keyValue'] 