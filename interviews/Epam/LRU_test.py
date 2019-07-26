import unittest

from LRU import LRUCache, LinkedNode

class TestLRUCache(unittest.TestCase):

    def test_init(self): 

        cache = LRUCache(4) 
        self.assertEqual(cache.capacity, 4) 
        self.assertEqual(cache.head, cache.tail)
        self.assertEqual(len(cache.key_to_prev), 0) 
        self.assertTrue(isinstance(cache, LRUCache)) 

    def test_operation1(self):
        
        cache = LRUCache(2) 

        cache.set(2, 1, 11)
        cache.set(1, 1, 11)
        self.assertEqual(cache.get(2), 1) 
        cache.set(4, 1, 11)
        self.assertEqual(cache.get(1), -1) 
        self.assertEqual(cache.get(2), 1) 

    def test_operation2(self):

        cache = LRUCache(1)
        cache.set(2, 1, 11)
        self.assertEqual(cache.get(2), 1)

        cache.set(3, 2, 11)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 2)

if __name__ == '__main__':
    unittest.main() 