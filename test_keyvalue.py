import unittest
import keyvalue
from pymongo import MongoClient

class TestKeyValue(unittest.TestCase):

    def test_connectivity(self):
        self.testClass = keyvalue.CRD('keyValue','keyValue')

    def test_ifduplicate(self):
        self.testClass.insert(1,"test")
        self.assertEquals(self.testClass.insert(1,"test"),"This Key already exists")

    def test_ifValueAdding(self):
        pass
    def test_ifDeletion(self):
        pass
    def test_nullDeletion(self):
        pass
if __name__ =='__main__':
    test = TestKeyValue()
    test.test_connectivity()
    test.test_ifduplicate()
