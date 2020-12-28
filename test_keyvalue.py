import unittest
import keyvalue
from pymongo import MongoClient

class TestKeyValue(unittest.TestCase):

    def test_connectivity(self):
        self.testClass = keyvalue.CRD('keyValue','keyValue')

    def test_ifduplicate(self):
        self.assertEqual(self.testClass.insert("3","testing"),False)

    def test_ifValueAdding(self):
        x = self.testClass.insert("3","testing")
        self.assertEqual(x,True)

    def test_ifDeletion(self):
        result = self.testClass.delete("3")
        self.assertNotEqual(result,0)

    def test_nullDeletion(self):
        result = self.testClass.delete("3")
        self.assertEqual(result,0)
    
    def test_ifread(self):
        result = self.testClass.read("3")
        self.assertEqual(result,True)

if __name__ =='__main__':
    test = TestKeyValue()
    test.test_connectivity()
    test.test_ifValueAdding()
    test.test_ifduplicate()
    test.test_ifread()
    test.test_ifDeletion()
    test.test_nullDeletion()