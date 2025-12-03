import unittest
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        assert(sphere.volume(2) == 33.510321638291124)

    def test_volume2(self):
        assert(sphere.volume(3) == 113.09733552923254)

    def test_volume3(self):
        assert(sphere.volume(4) == 268.082573106329)

    #failing test
    #def test_volume3(self):
        #assert(sphere.volume(10,1000) == ??)


if __name__ == '__main__':
    unittest.main()
