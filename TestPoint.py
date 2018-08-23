import unittest
import sys
from Point import Point

class TestPoint(unittest.TestCase):
    def test_near_zero_2_list(self):
        position_list = [
            {'id':2,'location':{'lat':2,'long':0}},
            {'id':1,'location':{'lat':1,'long':0}}
            ]
        result = Point({'lat':0,'long':0}).sort_by_distance(position_list)
        ans = [
            {'id':1,'location':{'lat':1,'long':0}},
            {'id':2,'location':{'lat':2,'long':0}}
            ]
        self.assertListEqual(result, ans)

    def test_near_zero_10_list(self):
        position_list = [
            {'id':10,'location':{'lat':10,'long':0}},
            {'id':9,'location':{'lat':9,'long':0}},
            {'id':8,'location':{'lat':8,'long':0}},
            {'id':7,'location':{'lat':7,'long':0}},
            {'id':6,'location':{'lat':6,'long':0}},
            {'id':5,'location':{'lat':5,'long':0}},
            {'id':4,'location':{'lat':4,'long':0}},
            {'id':3,'location':{'lat':3,'long':0}},
            {'id':2,'location':{'lat':2,'long':0}},
            {'id':1,'location':{'lat':1,'long':0}}
            ]
        result = Point({'lat':0,'long':0}).sort_by_distance(position_list)
        ans = [
            {'id':1,'location':{'lat':1,'long':0}},
            {'id':2,'location':{'lat':2,'long':0}},
            {'id':3,'location':{'lat':3,'long':0}},
            {'id':4,'location':{'lat':4,'long':0}},
            {'id':5,'location':{'lat':5,'long':0}},
            {'id':6,'location':{'lat':6,'long':0}},
            {'id':7,'location':{'lat':7,'long':0}},
            {'id':8,'location':{'lat':8,'long':0}},
            {'id':9,'location':{'lat':9,'long':0}},
            {'id':10,'location':{'lat':10,'long':0}}
            ]
        self.assertListEqual(result, ans)



if __name__ == '__main__':
    unittest.main()